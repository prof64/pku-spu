#!/usr/bin/env python3
"""Send a batch of rebuilt sprites to be looked at, and file the ones that are good.

The library's sprites are being rebuilt in SPU format 2, which adds lighting. Before a
rebuilt sprite joins the library (v2/), a person looks at it. A batch of them is put in
the queue at console.prof64.net, where each is shown lit and moving (Smeargle's review
page) and marked good or redo, with a note.

    tools/batch.py add first-six black2-white2/0001-bulbasaur ~/work/bulbasaur.spu --note "..."
    tools/batch.py send first-six       commit, push, and ask in the queue
    tools/batch.py answer first-six     what was answered, once it has been (--wait: held until it is)
    tools/batch.py land first-six       file the good ones under v2/; keep the rest to redo
    tools/batch.py land first-six --said-good <id>    file one the owner called good somewhere else
    tools/batch.py remove first-six <id>    take one sprite back out
    tools/batch.py drop first-six       give the batch up: withdraw its question, delete it

A batch is the folder batches/<name>/: batch.json, and each sprite at the path it will
have in the library (<collection>/<file>.spu). Its page is
https://smeargle.prof64.net/?review=<name>&at=<commit>, which anyone can open to look.

Asking again about a batch (redone after what was said about it) is the next round of the
same question, not a new one: `send` follows the batch's earlier question by itself, and
`send --follows <question>` does when the redo has another name. The queue closes a round
still waiting when the next is asked.

Needs the `switchboard` command (to ask in the queue) and, to check files and draw their
thumbnails, the `spu` command from https://github.com/prof64/spu (--spu, or $SPU).

Every sprite of the library is laid out as Gen 5's are (the README says how). `add` refuses one
that is not, and `land` does not file one, unless it was added with --as-is.
"""
import argparse, json, os, re, shutil, struct, subprocess, sys, tempfile, zlib
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


def read_png(path):
    """The pixels of an 8-bit RGBA picture (what `spu render` writes), row by row; None for any other kind."""
    data = Path(path).read_bytes()
    if data[:8] != b"\x89PNG\r\n\x1a\n":
        return None
    at, packed, head = 8, [], None
    while at < len(data):
        length, kind = struct.unpack(">I4s", data[at:at + 8])
        body = data[at + 8:at + 8 + length]
        at += 12 + length
        if kind == b"IHDR":
            head = struct.unpack(">IIBBBBB", body)
        elif kind == b"IDAT":
            packed.append(body)
    if not head or head[2:5] != (8, 6, 0) or head[6] != 0:
        return None
    width, height = head[0], head[1]
    raw, stride = zlib.decompress(b"".join(packed)), width * 4
    rows, above, at = [], bytearray(stride), 0
    for _ in range(height):
        how, line = raw[at], bytearray(raw[at + 1:at + 1 + stride])
        at += 1 + stride
        for x in range(stride):
            a = line[x - 4] if x >= 4 else 0
            b = above[x]
            c = above[x - 4] if x >= 4 else 0
            if how == 1:
                line[x] = (line[x] + a) & 255
            elif how == 2:
                line[x] = (line[x] + b) & 255
            elif how == 3:
                line[x] = (line[x] + (a + b) // 2) & 255
            elif how == 4:
                p = a + b - c
                pa, pb, pc = abs(p - a), abs(p - b), abs(p - c)
                line[x] = (line[x] + (a if pa <= pb and pa <= pc else b if pb <= pc else c)) & 255
        rows.append(line)
        above = line
    return width, height, rows


# A Gen 5 sprite at rest is never larger than this either way (its cell is 96 pixels; the largest is 111).
LARGEST = 112


def seen(spu, source, view):
    """What a view's plain picture at rest shows: the drawn part's size, how many pixels are drawn,
    whether every pixel is doubled (art kept at twice its real size, as some games store it), and
    whether the drawing runs off the bottom of its canvas along a wide edge (only part of the body
    is drawn). None if it cannot be told."""
    with tempfile.TemporaryDirectory() as folder:
        picture = Path(folder) / "rest.png"
        if subprocess.run([spu, "render", str(source), str(picture), "--view", view], capture_output=True).returncode:
            return None
        read = read_png(picture)
    if not read:
        return None
    width, height, rows = read
    pixel = lambda x, y: bytes(rows[y][x * 4:x * 4 + 4]) if rows[y][x * 4 + 3] else None
    across = [sum(1 for x in range(width) if rows[y][x * 4 + 3]) for y in range(height)]
    drawn_rows = [y for y in range(height) if across[y]]
    if not drawn_rows:
        return {"width": 0, "height": 0, "pixels": 0, "doubled": False, "cut": False}
    y0, y1 = drawn_rows[0], drawn_rows[-1]
    columns = [x for x in range(width) if any(rows[y][x * 4 + 3] for y in range(y0, y1 + 1))]
    x0, w, h = columns[0], columns[-1] - columns[0] + 1, y1 - y0 + 1
    doubled = w % 2 == 0 and h % 2 == 0 and w >= 8 and h >= 8 and all(
        pixel(x, y) == pixel(x0 + (x - x0) // 2 * 2, y0 + (y - y0) // 2 * 2)
        for y in range(y0, y1 + 1) for x in range(x0, x0 + w))
    # Feet and tails come to a point or two; a body that runs off the canvas leaves a wide straight edge.
    cut = y1 == height - 1 and across[y1] >= 0.45 * max(across)
    return {"width": w, "height": h, "pixels": sum(across), "doubled": doubled, "cut": cut}


def layout(spu, source):
    """Where a sprite is not laid out as Gen 5's are, which is what every sprite here is held to
    (see the README): drawn at its real size, a whole back, front and back at the same scale.
    A list of plain sentences; empty when it is."""
    listed = subprocess.run([spu, "info", str(source)], capture_output=True, text=True).stdout
    views = re.findall(r"^view (\S+) \((.*?)\):", listed, re.M)
    looked = [(name, seen(spu, source, view)) for view, name in views[:2]]
    if not looked or any(v is None for _, v in looked):
        return ["It could not be drawn to check its layout."]
    said = []
    for name, v in looked:
        if v["doubled"]:
            said.append(f'Every pixel of the {name.lower()} is doubled: it is drawn at twice its real size '
                        f'({v["width"]}×{v["height"]}, really {v["width"] // 2}×{v["height"] // 2}).')
        elif max(v["width"], v["height"]) > LARGEST:
            said.append(f'The {name.lower()} is {v["width"]}×{v["height"]}: larger than a Gen 5 sprite.')
    front = looked[0][1]
    if not front["pixels"]:
        return said
    back = looked[1][1] if len(looked) > 1 else None
    if not back or not back["pixels"]:
        return said + ["It has no back."]
    if back["cut"]:
        said.append("The back is cut off at the bottom: only part of the body is drawn.")
    scale = (back["pixels"] / front["pixels"]) ** 0.5
    if scale > 1.3:
        said.append(f"The back is drawn about {scale:.1f} times as large as the front. In Gen 5 they are the same scale.")
    elif scale < 0.75:
        said.append(f"The back is drawn smaller than the front (about {scale:.1f} times). In Gen 5 they are the same scale.")
    return said


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
        wrong = layout(spu, source)
        if wrong and not args.as_is:
            fail(f"{source} is not laid out like a Gen 5 sprite:\n  " + "\n  ".join(wrong)
                 + "\nRedo it in that layout first (see the README), or pass --as-is to have it looked at anyway.")
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
    if args.as_is:
        # Looked at as it is; `land` files it whatever its layout.
        entry["as_is"] = True
    before = f"anim/{args.id}.png"
    if (ROOT / before).exists():
        entry["before"] = before
    batch["sprites"] = [s for s in batch["sprites"] if s["id"] != args.id] + [entry]
    write(args.batch, batch)
    print(f'{entry["name"]} is in batch {args.batch} ({len(batch["sprites"])} so far)')


def queue_read(address, wait=False):
    """A question as the queue has it; None if its record is gone. With `wait`, the read is held
    until it is answered or withdrawn (a minute at a time, as the queue offers: never a sleep)."""
    while True:
        got = subprocess.run(["switchboard", "GET", address] + (["--wait", "60"] if wait else []), text=True, capture_output=True)
        if got.returncode:
            try:
                gone = json.loads(got.stderr).get("status") == 404
            except ValueError:
                gone = False
            if gone:
                return None
            fail(f"the queue could not be read:\n{got.stderr or got.stdout}")
        item = json.loads(got.stdout)
        if not wait or item["state"] != "open":
            return item


def earlier_question(name):
    """The question this batch was last asked with, as the queue has it now; None if it never was."""
    file = folder(name) / "question.json"
    return queue_read(json.loads(file.read_text())["address"]) if file.exists() else None


def send(args):
    batch = read(args.batch)
    there = folder(args.batch).relative_to(ROOT)
    # A batch asked about before is asked about again as the next round of that question. The
    # queue closes a round still waiting when the next is asked, so nothing is withdrawn here.
    follows = args.follows
    earlier = earlier_question(args.batch)
    if earlier:
        if earlier["state"] == "open" and not args.again:
            fail("this batch is in the queue, waiting to be looked at (see `answer`). `send --again` asks the next "
                 "round, about the sprites as they now are.")
        follows = follows or earlier["id"]
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
    if follows:
        question["follows"] = follows
    asked = subprocess.run(["switchboard", "POST", "/queue/items", "-"], input=json.dumps(question), text=True, capture_output=True)
    if asked.returncode:
        fail(f"the queue did not take the question:\n{asked.stderr or asked.stdout}")
    answer = json.loads(asked.stdout)
    if answer.get("page") != question["page"]:
        # A queue that does not know about pages would show a question with nothing to look at.
        subprocess.run(["switchboard", "DELETE", answer["address"]], capture_output=True)
        fail("the queue took the question without its page, so it was withdrawn")
    (folder(args.batch) / "question.json").write_text(json.dumps(
        {"id": answer["id"], "address": answer["address"], "thread": answer.get("thread"), "round": answer.get("round"),
         "page": question["page"], "at": at, "asked": datetime.now(timezone.utc).isoformat(timespec="seconds")}, indent=2) + "\n")
    git("add", "--", str(there))
    git("commit", "-q", "-m", f"Batch {args.batch}: asked in the queue", "--", str(there))
    git("push", "-q", "origin", "HEAD")
    print(f'Asked{f" (round {answer['round']})" if (answer.get("round") or 1) > 1 else ""}: https://console.prof64.net/queue/{answer["id"]}')
    print(f'The page: {question["page"]}')


def asked_answer(name, wait=False):
    if not (folder(name) / "question.json").exists():
        fail("this batch has not been sent yet (`send`)")
    question = json.loads((folder(name) / "question.json").read_text())
    item = queue_read(question["address"], wait)
    if not item:
        fail("the queue no longer has this batch's question; `send` asks again")
    return item


def answer(args):
    item = asked_answer(args.batch, args.wait)
    if item["state"] != "answered":
        print(f'Not answered yet ({item["state"]}): https://console.prof64.net/queue/{item["id"]}')
        return
    print(json.dumps(item["answer"], indent=2, ensure_ascii=False))


def land(args):
    batch = read(args.batch)
    if args.said_good:
        # The owner called these good somewhere other than the queue's page (in conversation). Only
        # they are filed; the rest of the batch stays as it is, still waiting to be looked at.
        unknown = [i for i in args.said_good if i not in {s["id"] for s in batch["sprites"]}]
        if unknown:
            fail(f'not in batch {args.batch}: {", ".join(unknown)}')
        said = {"good": args.said_good}
    else:
        item = asked_answer(args.batch)
        if item["state"] != "answered":
            fail(f'the batch is not answered yet ({item["state"]})')
        said = item["answer"]
    good, redo, notes = set(said.get("good", [])), set(said.get("redo", [])), said.get("notes", {})
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
        # Good to look at is not enough to join the library: it has to be laid out like the rest.
        wrong = [] if sprite.get("as_is") else layout(spu, source)
        if wrong:
            sprite["redo"] = "Not laid out like a Gen 5 sprite. " + " ".join(wrong)
            kept.append(sprite)
            continue
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
        # question.json stays: the next `send` asks about what is left, as the next round of it.
        for empty in sorted((p for p in folder(args.batch).rglob("*") if p.is_dir()), reverse=True):
            if not any(empty.iterdir()):
                empty.rmdir()
    else:
        shutil.rmtree(folder(args.batch))
    git("add", "--", "v2", "batches")
    how = " (called good outside the queue)" if args.said_good else ""
    git("commit", "-q", "-m", f'Batch {args.batch}: {len(landed)} in the library{how}, {len(kept)} still in the batch')
    git("push", "-q", "origin", "HEAD")
    print(f'In the library: {", ".join(landed) or "none"}')
    for sprite in kept:
        if "redo" in sprite:
            print(f'To redo: {sprite["name"]}' + (f': {sprite["redo"]}' if sprite["redo"] else ""))
        elif not args.said_good:
            print(f'Not marked: {sprite["name"]}')


def remove(args):
    batch = read(args.batch)
    kept = [s for s in batch["sprites"] if s["id"] != args.id]
    if len(kept) == len(batch["sprites"]):
        fail(f'{args.id} is not in batch {args.batch}')
    (folder(args.batch) / f"{args.id}.spu").unlink(missing_ok=True)
    batch["sprites"] = kept
    write(args.batch, batch)
    print(f'{args.id} is out of batch {args.batch} ({len(kept)} left); `send --again` asks about the rest')


def drop(args):
    read(args.batch)
    earlier = earlier_question(args.batch)
    # Only a question still waiting is withdrawn: the same call on a closed one removes its record.
    if earlier and earlier["state"] == "open":
        subprocess.run(["switchboard", "DELETE", earlier["address"]], capture_output=True)
        print("Its question was withdrawn.")
    there = str(folder(args.batch).relative_to(ROOT))
    shutil.rmtree(folder(args.batch))
    if git("ls-files", "--", there):
        git("add", "-A", "--", there)
        git("commit", "-q", "-m", f"Batch {args.batch}: given up", "--", there)
        git("push", "-q", "origin", "HEAD")
    print(f"Batch {args.batch} is gone")


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
    adding.add_argument("--as-is", action="store_true", help="take it although it is not laid out like a Gen 5 sprite")
    adding.set_defaults(act=add)
    sending = commands.add_parser("send", help="commit, push, and ask in the queue")
    sending.add_argument("batch")
    sending.add_argument("--again", action="store_true", help="ask the next round although the last is still waiting")
    sending.add_argument("--follows", help="the earlier question this is the next round of (its id or address), "
                                           "when the batch is a redo of one sent under another name")
    sending.set_defaults(act=send)
    answering = commands.add_parser("answer", help="what was answered")
    answering.add_argument("batch")
    answering.add_argument("--wait", action="store_true", help="hold until it is answered or withdrawn")
    answering.set_defaults(act=answer)
    landing = commands.add_parser("land", help="file the good ones under v2/, keep the rest to redo")
    landing.add_argument("batch")
    landing.add_argument("--said-good", nargs="+", metavar="ID",
                         help="file only these, which the owner called good somewhere other than the queue; the rest keep waiting")
    landing.set_defaults(act=land)
    removing = commands.add_parser("remove", help="take one sprite back out of a batch")
    removing.add_argument("batch")
    removing.add_argument("id")
    removing.set_defaults(act=remove)
    dropping = commands.add_parser("drop", help="withdraw the batch's question and delete the batch")
    dropping.add_argument("batch")
    dropping.set_defaults(act=drop)
    args = parser.parse_args()
    args.act(args)


if __name__ == "__main__":
    main()
