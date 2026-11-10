#!/usr/bin/env python3
"""Rebuild this library from the finished sprites of each source collection.

Each sprite is upgraded to SPU version 1 (if it is older), checked, and given
a thumbnail; index.json lists them all. Needs the `spu` command from
https://github.com/prof64/sprite-format (pass its path with --spu).

    python3 tools/build.py --spu ../../sprite-format/target/release/spu \
        --uranium <folder holding Uranium's catalog.json and SPUs/> \
        --insurgence <folder of Insurgence .spu files> \
        --gen5 <folder from `smeargle spu --rom white2.nds`>
"""
import argparse, hashlib, json, re, subprocess, sys, zipfile
from concurrent.futures import ThreadPoolExecutor
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
GROUPS = {}  # filled in below, once the group lists exist
COLLECTIONS = {
    "black2-white2": "Pokémon Black 2 & White 2",
    "uranium": "Pokémon Uranium",
    "insurgence": "Pokémon Insurgence",
    "review": "Drafts for review",
}


def pretty(stem):
    """`0727-delta-bulbasaur-female` -> (727, "Delta Bulbasaur Female")."""
    number, _, rest = stem.partition("-")
    words = [w for w in rest.split("-") if w != "default"]
    return int(number), " ".join(w.capitalize() for w in words)


# Pokémon from the official games that Uranium also includes.
OFFICIAL_IN_URANIUM = {
    "magikarp", "gyarados", "lotad", "lombre", "ludicolo", "ekans", "arbok", "gligar", "gliscor",
    "sableye", "corsola", "whimsicott", "spritzee", "aromatisse",
}
EVENTS = ["christmas", "halloween", "easter", "anniversary", "chef", "festive"]
URANIUM_GROUPS = [
    "New Pokémon",
    "Nuclear forms of new Pokémon",
    "Nuclear forms of existing Pokémon",
    "Other forms of existing Pokémon",
    "Event costumes",
]


def uranium(stem, catalog_name):
    """A plain name and a group, from the file name and the catalog's label."""
    tokens = stem.split("-")[1:]
    said = set(re.findall(r"[a-z]+", re.split(r" [—·-] ", catalog_name.lower())[0]))
    species, rest = [tokens[0]], tokens[1:]
    if species == ["mega"]:  # 174-mega-kiricorn
        species, rest = [rest[0]], ["mega"] + rest[1:]
    if rest[:1] == ["a"]:  # S51-A
        species.append(rest.pop(0))
    has = lambda w: w in rest or w in said
    form = next((int(n) for t in rest for n in re.findall(r"^(?:form)?0*(\d+)$", t)), None)
    event = next((e for e in EVENTS if has(e)), None)
    lead = [w for w in ("nuclear", "dark") if has(w)] + ([event] if event else []) + (["mega"] if has("mega") else [])
    shown = "-".join(species).upper() if species[0] == "s51" else species[0].capitalize()
    name = " ".join([w.capitalize() for w in lead] + [shown])
    notes = []
    if has("beta"): name += " Beta"
    if has("gamma"): name += " Gamma"
    if has("costume") or has("costumed"): notes.append("Costume")
    if not lead and not notes and form and not (has("beta") or has("gamma")): notes.append(f"Form {form}")
    if "extra" in rest: notes.append("Alternate back")
    elif "front" in rest: notes.append("Front")
    elif "back" in rest: notes.append("Back")
    if notes:
        name += f" ({', '.join(notes)})"
    official = species[0] in OFFICIAL_IN_URANIUM
    if event or "Costume" in notes:
        group = URANIUM_GROUPS[4]
    elif has("nuclear"):
        group = URANIUM_GROUPS[2 if official else 1]
    elif official:
        group = URANIUM_GROUPS[3]
    else:
        group = URANIUM_GROUPS[0]
    return name, group


def insurgence(stem):
    words = [w for w in stem.split("-")[1:] if w not in ("default", "base")]
    female = "female" in words
    mega = "mega" in words
    words = [w for w in words if w not in ("female", "mega")]
    name = " ".join((["Mega"] if mega else []) + [w.capitalize() for w in words])
    return name + (" (Female)" if female else "")


GEN5_GROUPS = ["Generation 1", "Generation 2", "Generation 3", "Generation 4", "Generation 5", "Pokéstar Studios", "Eggs"]
GEN_ENDS = [151, 251, 386, 493, 649]


def gen5_group(entry, name, species_gen):
    if name.startswith("Pokéstar"):
        return GEN5_GROUPS[5]
    if "Egg" in name:
        return GEN5_GROUPS[6]
    if entry <= 649:
        return GEN5_GROUPS[next(i for i, end in enumerate(GEN_ENDS) if entry <= end)]
    return GEN5_GROUPS[species_gen[name.split(" (")[0]]]  # a form: where its species is


def rename(path, name):
    """Set the sprite's own name, leaving everything else in the file as it is."""
    with zipfile.ZipFile(path) as z:
        members = [(i, z.read(i)) for i in z.infolist()]
    with zipfile.ZipFile(path, "w") as z:
        for info, data in members:
            if info.filename == "sprite.json":
                doc = json.loads(data)
                doc["name"] = name
                data = json.dumps(doc, ensure_ascii=False, indent=2).encode()
            fresh = zipfile.ZipInfo(info.filename)  # fixed date: rebuilds are identical
            fresh.compress_type = info.compress_type
            z.writestr(fresh, data)


GROUPS.update({"black2-white2": GEN5_GROUPS, "uranium": URANIUM_GROUPS})


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--spu", required=True)
    ap.add_argument("--uranium")
    ap.add_argument("--insurgence")
    ap.add_argument("--review", help="folder of draft .spu files to show for review")
    ap.add_argument("--gen5", help="folder of <entry>.spu files from `smeargle spu --rom <Black 2 or White 2>`")
    args = ap.parse_args()

    jobs = []  # (collection, source path, display name or None)
    if args.uranium:
        src = Path(args.uranium)
        for entry in json.loads((src / "catalog.json").read_text())["sprites"]:
            stem = re.sub(r"[^a-z0-9]+", "-", Path(entry["file"]).stem.lower()).strip("-")
            jobs.append(("uranium", src / entry["file"], *uranium(stem, entry["name"])))
    if args.insurgence:
        for path in sorted(Path(args.insurgence).glob("*.spu")):
            jobs.append(("insurgence", path, insurgence(path.stem), None))

    if args.review:
        for path in sorted(Path(args.review).glob("*.spu")):
            jobs.append(("review", path, None, None))
    if args.gen5:
        docs = []
        for path in sorted(Path(args.gen5).glob("*.spu"), key=lambda p: int(p.stem)):
            doc = json.loads(zipfile.ZipFile(path).read("sprite.json"))
            # Skip empty slots in the game's archive.
            if any(v["images"] for v in doc["views"]) and doc["name"] != "Placeholder":
                docs.append((int(path.stem), path, doc["name"]))
        species_gen = {n: next(i for i, end in enumerate(GEN_ENDS) if e <= end) for e, _, n in docs if e <= 649}
        for entry, path, name in docs:
            jobs.append(("black2-white2", path, name, gen5_group(entry, name, species_gen)))

    def build(job):
        collection, source, name, group = job
        stem = re.sub(r"[^a-z0-9]+", "-", source.stem.lower()).strip("-")
        if collection == "black2-white2":
            # Named by archive entry: 0001-bulbasaur.
            slug = re.sub(r"[^a-z0-9]+", "-", name.lower()).strip("-")
            stem = f"{int(source.stem):04d}-{slug}"
        number, fallback = pretty(stem)
        out = ROOT / collection / f"{stem}.spu"
        thumb = ROOT / "thumbs" / collection / f"{stem}.png"
        out.parent.mkdir(parents=True, exist_ok=True)
        thumb.parent.mkdir(parents=True, exist_ok=True)
        anim = ROOT / "anim" / collection / f"{stem}.png"
        anim.parent.mkdir(parents=True, exist_ok=True)
        subprocess.run([args.spu, "convert", str(source), str(out)], check=True)
        if name and collection != "black2-white2":
            rename(out, name)
        subprocess.run([args.spu, "render", str(out), str(thumb)], check=True)
        # The game's own sprites move on every tick; half the frames is plenty for a preview.
        step = ["--step", "2"] if collection == "black2-white2" else []
        subprocess.run([args.spu, "animate", str(out), str(anim), *step], check=True)
        doc = json.loads(zipfile.ZipFile(out).read("sprite.json"))
        entry = {
            "id": f"{collection}/{stem}",
            # Changes whenever the file does, so browsers fetch the new one.
            "rev": hashlib.sha1(out.read_bytes()).hexdigest()[:10],
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
        if group:
            entry["group"] = group
        return entry

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
    # The three sprites on each card: picked in featured.json, else the first three.
    featured = json.loads((ROOT / "featured.json").read_text())
    known = {s["id"] for s in sprites}

    def picks(collection, key, among):
        chosen = [f"{collection}/{stem}" for stem in featured.get(collection, {}).get(key, [])]
        missing = [i for i in chosen if i not in known]
        if missing:
            sys.exit(f"featured.json names sprites that aren't in the library: {missing}")
        return chosen or [s["id"] for s in among][:3]

    collections = []
    for c, n in COLLECTIONS.items():
        inside = [s for s in sprites if s["collection"] == c]
        if not inside:
            continue
        # Sections inside the game, in the order to show them.
        groups = [g for g in GROUPS.get(c, []) if any(s.get("group") == g for s in inside)]
        collections.append({
            "id": c,
            "name": n,
            "count": len(inside),
            "samples": picks(c, "game", inside),
            "groups": groups,
            "groupSamples": {g: picks(c, g, [s for s in inside if s.get("group") == g]) for g in groups},
        })
    index = {"format": "spu-library", "version": 1, "collections": collections, "sprites": sprites}
    index_path.write_text(json.dumps(index, ensure_ascii=False, indent=1) + "\n")
    print(f"{len(built)} built, {len(sprites)} listed")


if __name__ == "__main__":
    sys.exit(main())
