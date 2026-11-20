#!/usr/bin/env python3
"""Send a batch of rebuilt sprites to be looked at, and file the ones that are good.

The library's sprites are being rebuilt in SPU format 2, which adds lighting. Before a
rebuilt sprite joins the library (v2/), a person looks at it. A batch of them is put in
the queue at console.prof64.net, where each is shown lit and moving (Smeargle's review
page) and marked good or redo, with a note.

    tools/batch.py add first-six black2-white2/0001-bulbasaur ~/work/bulbasaur.spu --note "..."
    tools/batch.py send first-six       commit, push, and ask in the queue
    tools/batch.py answer first-six     what was answered, once it has been
    tools/batch.py land first-six       file the good ones under v2/; keep the rest to redo

A batch is the folder batches/<name>/: batch.json, and each sprite at the path it will
have in the library (<collection>/<file>.spu). Its page is
https://smeargle.prof64.net/?review=<name>&at=<commit>, which anyone can open to look.

Needs the `switchboard` command (to ask in the queue) and, to check files and draw their
thumbnails, the `spu` command from https://github.com/prof64/spu (--spu, or $SPU).
"""
import argparse, json, os, re, shutil, subprocess, sys
from datetime import datetime, timezone
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
BATCHES = ROOT / "batches"
LIBRARY = ROOT / "v2"
PAGE = "https://smeargle.prof64.net/?review={name}&at={at}"
MAGIC = bytes([0x89, 0x53, 0x50, 0x55, 0x0D, 0x0A, 0x1A, 0x0A])
COLLECTIONS = {
    "black2-white2": "Pokémon Black 2 & White 2",
    "uranium": "Pokémon Uranium",
    "insurgence": "Pokémon Insurgence",
}
PLAIN = re.compile(r"^[a-z0-9][a-z0-9._-]{0,63}$")


def fail(why):
    sys.exit(f"batch: {why}")


def run(*command, **more):
    return subprocess.run(command, cwd=ROOT, check=True, text=True, capture_output=True, **more).stdout.strip()


def git(*words):
    return run("git", *words)


def spu_command(given):
    found = given or os.environ.get("SPU") or shutil.which("spu")
    beside = ROOT.parent.parent / "sprite-format" / "target" / "release" / "spu"
    if not found and beside.exists():
        found = str(beside)
    return found


def folder(name):
    if not PLAIN.match(name):
        fail(f'"{name}" is not a batch name: lowercase letters, digits, - . _')
    return BATCHES / name


def read(name):
    file = folder(name) / "batch.json"
    if not file.exists():
        fail(f'there is no batch "{name}" (add a sprite to start one)')
    return json.loads(file.read_text())


def write(name, batch):
    file = folder(name) / "batch.json"
    file.parent.mkdir(parents=True, exist_ok=True)
    file.write_text(json.dumps(batch, indent=2, ensure_ascii=False) + "\n")


def old_names():
    """What each sprite is called in the library as it stands."""
    index = ROOT / "index.json"
    if not index.exists():
        return {}
    return {s["id"]: s["name"] for s in json.loads(index.read_text())["sprites"]}


def add(args):
    collection, _, stem = args.id.partition("/")
    if collection not in COLLECTIONS or not PLAIN.match(stem):
        fail(f'"{args.id}" is not a library id: <collection>/<file name>, collection one of {", ".join(COLLECTIONS)}')
    source = Path(args.file).expanduser()
    if not source.is_file():
        fail(f"{source} is not a file")
    if source.read_bytes()[:8] != MAGIC:
        fail(f"{source} is not SPU format 2 (an older file is upgraded with `spu convert` first)")
    spu = spu_command(args.spu)
    if spu:
        checked = subprocess.run([spu, "validate", str(source)], text=True, capture_output=True)
        if checked.returncode:
            fail(f"{source} does not pass `spu validate`:\n{checked.stdout}{checked.stderr}")
    else:
        print("batch: no spu command found, so the file was not checked (--spu)", file=sys.stderr)

    there = folder(args.batch)
    batch = json.loads((there / "batch.json").read_text()) if (there / "batch.json").exists() else {
        "format": "spu-batch", "version": 1, "name": args.batch, "sprites": []}
    if args.title:
        batch["name"] = args.title
    if args.about:
        batch["note"] = args.about
    target = there / f"{args.id}.spu"
    target.parent.mkdir(parents=True, exist_ok=True)
    shutil.copyfile(source, target)

    entry = {"id": args.id, "name": args.name or old_names().get(args.id) or stem.replace("-", " ").title(), "file": f"{args.id}.spu"}
    if args.note:
        entry["note"] = args.note
    before = f"anim/{args.id}.png"
    if (ROOT / before).exists():
        entry["before"] = before
    batch["sprites"] = [s for s in batch["sprites"] if s["id"] != args.id] + [entry]
    write(args.batch, batch)
    print(f'{entry["name"]} is in batch {args.batch} ({len(batch["sprites"])} so far)')


def send(args):
    batch = read(args.batch)
    there = folder(args.batch).relative_to(ROOT)
    if (folder(args.batch) / "question.json").exists() and not args.again:
        fail(f"this batch was already sent (see `answer`); --again asks afresh")
    for sprite in batch["sprites"]:
        if not (folder(args.batch) / sprite["file"]).is_file():
            fail(f'{sprite["file"]} is listed but is not in the batch')
    count = len(batch["sprites"])
    git("add", "--", str(there))
    if git("status", "--porcelain", "--", str(there)):
        git("commit", "-q", "-m", f'Batch {args.batch}: {count} sprite{"" if count == 1 else "s"} to look at', "--", str(there))
    git("push", "-q", "origin", "HEAD")
    at = git("rev-parse", "HEAD")

    question = {
        "title": f'Sprites to look at: {batch["name"]} ({count})',
        "text": batch.get("note", ""),
        "about": f"pku-spu batch {args.batch}",
        "page": PAGE.format(name=args.batch, at=at),
    }
    asked = subprocess.run(["switchboard", "POST", "/queue/items", "-"], input=json.dumps(question), text=True, capture_output=True)
    if asked.returncode:
        fail(f"the queue did not take the question:\n{asked.stderr or asked.stdout}")
    answer = json.loads(asked.stdout)
    if answer.get("page") != question["page"]:
        # A queue that does not know about pages would show a question with nothing to look at.
        subprocess.run(["switchboard", "DELETE", answer["address"]], capture_output=True)
        fail("the queue took the question without its page, so it was withdrawn")
    (folder(args.batch) / "question.json").write_text(json.dumps(
        {"address": answer["address"], "page": question["page"], "at": at,
         "asked": datetime.now(timezone.utc).isoformat(timespec="seconds")}, indent=2) + "\n")
    git("add", "--", str(there))
    git("commit", "-q", "-m", f"Batch {args.batch}: asked in the queue", "--", str(there))
    git("push", "-q", "origin", "HEAD")
    print(f'Asked: https://console.prof64.net/queue/{answer["id"]}')
    print(f'The page: {question["page"]}')


def asked_answer(name):
    file = folder(name) / "question.json"
    if not file.exists():
        fail("this batch has not been sent yet (`send`)")
    question = json.loads(file.read_text())
    got = subprocess.run(["switchboard", "GET", question["address"]], text=True, capture_output=True)
    if got.returncode:
        fail(f"the queue could not be read:\n{got.stderr or got.stdout}")
    return json.loads(got.stdout)


def answer(args):
    item = asked_answer(args.batch)
    if item["state"] != "answered":
        print(f'Not answered yet ({item["state"]}): https://console.prof64.net/queue/{item["id"]}')
        return
    print(json.dumps(item["answer"], indent=2, ensure_ascii=False))


def land(args):
    item = asked_answer(args.batch)
    if item["state"] != "answered":
        fail(f'the batch is not answered yet ({item["state"]})')
    said = item["answer"]
    good, redo, notes = set(said.get("good", [])), set(said.get("redo", [])), said.get("notes", {})
    batch = read(args.batch)
    spu = spu_command(args.spu)
    if not spu:
        fail("landing draws thumbnails, which needs the spu command (--spu)")

    index_file = LIBRARY / "index.json"
    index = json.loads(index_file.read_text()) if index_file.exists() else {"format": "spu-library", "version": 2, "sprites": []}
    kept, landed = [], []
    for sprite in batch["sprites"]:
        if sprite["id"] not in good:
            # Kept in the batch, with what was said, for whoever redoes it. (One that was
            # not marked either way is kept as it is, to be asked about again.)
            if sprite["id"] in redo:
                sprite["redo"] = notes.get(sprite["id"], "")
            kept.append(sprite)
            continue
        source = folder(args.batch) / sprite["file"]
        target = LIBRARY / sprite["file"]
        thumb = LIBRARY / "thumbs" / f'{sprite["id"]}.png'
        target.parent.mkdir(parents=True, exist_ok=True)
        thumb.parent.mkdir(parents=True, exist_ok=True)
        shutil.move(source, target)
        run(spu, "render", str(target), str(thumb))
        collection = sprite["id"].split("/")[0]
        entry = {"id": sprite["id"], "name": sprite["name"], "game": COLLECTIONS[collection], "file": sprite["file"],
                 "thumb": f'thumbs/{sprite["id"]}.png'}
        index["sprites"] = [s for s in index["sprites"] if s["id"] != sprite["id"]] + [entry]
        landed.append(sprite["name"])
    index["sprites"].sort(key=lambda s: s["id"])
    index_file.parent.mkdir(parents=True, exist_ok=True)
    index_file.write_text(json.dumps(index, indent=1, ensure_ascii=False) + "\n")

    if kept:
        batch["sprites"] = kept
        if said.get("note"):
            batch["said"] = said["note"]
        write(args.batch, batch)
        # The next `send` asks about what is left.
        (folder(args.batch) / "question.json").unlink()
        for empty in sorted((p for p in folder(args.batch).rglob("*") if p.is_dir()), reverse=True):
            if not any(empty.iterdir()):
                empty.rmdir()
    else:
        shutil.rmtree(folder(args.batch))
    git("add", "--", "v2", "batches")
    git("commit", "-q", "-m", f'Batch {args.batch}: {len(landed)} in the library, {len(kept)} still in the batch')
    git("push", "-q", "origin", "HEAD")
    print(f'In the library: {", ".join(landed) or "none"}')
    for sprite in kept:
        if "redo" in sprite:
            print(f'To redo: {sprite["name"]}' + (f': {sprite["redo"]}' if sprite["redo"] else ""))
        else:
            print(f'Not marked: {sprite["name"]}')


def main():
    parser = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument("--spu", help="path to the spu command")
    commands = parser.add_subparsers(dest="command", required=True)
    adding = commands.add_parser("add", help="put a rebuilt sprite in a batch")
    adding.add_argument("batch")
    adding.add_argument("id", help="its library id, e.g. black2-white2/0001-bulbasaur")
    adding.add_argument("file", help="the format 2 .spu file")
    adding.add_argument("--name", help="what it is called, when the library does not have it yet")
    adding.add_argument("--note", help="what to look at: shown beside the sprite")
    adding.add_argument("--title", help="what the batch is called")
    adding.add_argument("--about", help="a line about the whole batch")
    adding.set_defaults(act=add)
    sending = commands.add_parser("send", help="commit, push, and ask in the queue")
    sending.add_argument("batch")
    sending.add_argument("--again", action="store_true", help="ask afresh although it was asked before")
    sending.set_defaults(act=send)
    answering = commands.add_parser("answer", help="what was answered")
    answering.add_argument("batch")
    answering.set_defaults(act=answer)
    landing = commands.add_parser("land", help="file the good ones under v2/, keep the rest to redo")
    landing.add_argument("batch")
    landing.set_defaults(act=land)
    args = parser.parse_args()
    args.act(args)


if __name__ == "__main__":
    main()
