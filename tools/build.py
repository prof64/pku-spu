#!/usr/bin/env python3
"""Rebuild this library from the finished sprites of each source collection.

Each sprite is upgraded to SPU version 1 (if it is older), checked, and given
a thumbnail; index.json lists them all. Needs the `spu` command from
https://github.com/prof64/sprite-format (pass its path with --spu).

    python3 tools/build.py --spu ../../sprite-format/target/release/spu \
        --uranium <folder holding Uranium's catalog.json and SPUs/> \
        --insurgence <folder of Insurgence .spu files>
"""
import argparse, json, re, subprocess, sys, zipfile
from concurrent.futures import ThreadPoolExecutor
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
COLLECTIONS = {
    "uranium": "Pokémon Uranium",
    "insurgence": "Pokémon Insurgence",
}


def pretty(stem):
    """`0727-delta-bulbasaur-female` -> (727, "Delta Bulbasaur Female")."""
    number, _, rest = stem.partition("-")
    words = [w for w in rest.split("-") if w != "default"]
    return int(number), " ".join(w.capitalize() for w in words)


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--spu", required=True)
    ap.add_argument("--uranium")
    ap.add_argument("--insurgence")
    args = ap.parse_args()

    jobs = []  # (collection, source path, display name or None)
    if args.uranium:
        src = Path(args.uranium)
        for entry in json.loads((src / "catalog.json").read_text())["sprites"]:
            jobs.append(("uranium", src / entry["file"], entry["name"]))
    if args.insurgence:
        for path in sorted(Path(args.insurgence).glob("*.spu")):
            jobs.append(("insurgence", path, None))

    def build(job):
        collection, source, name = job
        stem = re.sub(r"[^a-z0-9]+", "-", source.stem.lower()).strip("-")
        number, fallback = pretty(stem)
        out = ROOT / collection / f"{stem}.spu"
        thumb = ROOT / "thumbs" / collection / f"{stem}.png"
        out.parent.mkdir(parents=True, exist_ok=True)
        thumb.parent.mkdir(parents=True, exist_ok=True)
        anim = ROOT / "anim" / collection / f"{stem}.png"
        anim.parent.mkdir(parents=True, exist_ok=True)
        subprocess.run([args.spu, "convert", str(source), str(out)], check=True)
        subprocess.run([args.spu, "render", str(out), str(thumb)], check=True)
        subprocess.run([args.spu, "animate", str(out), str(anim)], check=True)
        doc = json.loads(zipfile.ZipFile(out).read("sprite.json"))
        return {
            "id": f"{collection}/{stem}",
            "collection": collection,
            "number": number,
            "name": name or fallback,
            "file": f"{collection}/{stem}.spu",
            "thumbnail": f"thumbs/{collection}/{stem}.png",
            "animation": f"anim/{collection}/{stem}.png",
            "bytes": out.stat().st_size,
            "views": [v["name"] for v in doc["views"]],
            "variants": [v["name"] for v in doc.get("variants", [])],
        }

    for collection in {j[0] for j in jobs}:
        for old in list((ROOT / collection).glob("*.spu")) + list((ROOT / "thumbs" / collection).glob("*.png")) + list((ROOT / "anim" / collection).glob("*.png")):
            old.unlink()
    with ThreadPoolExecutor(8) as pool:
        built = list(pool.map(build, jobs))

    index_path = ROOT / "index.json"
    kept = []
    if index_path.exists():
        rebuilt = {j[0] for j in jobs}
        kept = [s for s in json.loads(index_path.read_text())["sprites"] if s["collection"] not in rebuilt]
    sprites = sorted(kept + built, key=lambda s: (list(COLLECTIONS).index(s["collection"]), s["number"], s["id"]))
    index = {
        "format": "spu-library",
        "version": 1,
        "collections": [
            {
                "id": c,
                "name": n,
                "count": sum(s["collection"] == c for s in sprites),
                # Three sprites to show on the game's card.
                "samples": [s["id"] for s in sprites if s["collection"] == c][:3],
            }
            for c, n in COLLECTIONS.items()
            if any(s["collection"] == c for s in sprites)
        ],
        "sprites": sprites,
    }
    index_path.write_text(json.dumps(index, ensure_ascii=False, indent=1) + "\n")
    print(f"{len(built)} built, {len(sprites)} listed")


if __name__ == "__main__":
    sys.exit(main())
