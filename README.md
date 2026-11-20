# pku-spu

Animated Pokémon battle sprites as editable [SPU](https://github.com/prof64/spu)
files: drawings, parts, animations and shiny colors in one `.spu` each. This
is the library the Smeargle editor's Start screen browses.

| Collection | Sprites |
| --- | --- |
| `black2-white2/` — Pokémon Black 2 & White 2, as the game stores them | 750 |
| `uranium/` — Pokémon Uranium | 334 |
| `insurgence/` — Pokémon Insurgence | 47 |

`index.json` lists every sprite with its name, file, thumbnail, views and
variants. `thumbs/` holds the first frame of each and `anim/` its first
animation as a looping animated PNG.

The artwork belongs to its original creators and the teams behind each game;
nothing here grants a license to it. The rigging and animation were made for
this library.

`featured.json` picks the three sprites shown on each game's and section's
card in the gallery.

## Format 2, and looking at sprites before they join

The sprites are being rebuilt in SPU format 2, which adds lighting: a material
for every pixel, which way it faces, and what glows. The rebuilt library is
`v2/` (its own `index.json` and `thumbs/`), which is what
[Smeargle](https://smeargle.prof64.net) lists. Everything else here is still
format 1 until its sprite has been rebuilt.

A rebuilt sprite is looked at by a person before it goes in `v2/`. Batches
wait in `batches/<name>/`, and `tools/batch.py` moves them along:

```sh
tools/batch.py add first-six black2-white2/0001-bulbasaur ~/work/bulbasaur.spu --note "what to look at"
tools/batch.py send first-six     # commit, push, and ask in the queue at console.prof64.net
tools/batch.py answer first-six   # what was answered
tools/batch.py land first-six     # file the good ones under v2/, keep the rest to redo
```

`send` and `land` commit and push the branch they are run on: work on a branch
and merge it (with a merge commit, so the commit a review points at stays).
The question shows `https://smeargle.prof64.net/?review=<name>&at=<commit>`:
every sprite of the batch lit and moving, to mark Good or Redo with a note.
Anyone can open that address to look.

## Rebuilding

```sh
python3 tools/build.py --spu <path to the spu command> \
    --uranium <folder with Uranium's catalog.json and SPUs/> \
    --insurgence <folder of Insurgence .spu files>
```

Sources: `uranium-spu/dist/Uranium-SPUs-only.zip` (unzipped) and
`insurgence-spu/gallery/spus/`. Older files are upgraded to SPU version 1 and
every file is validated.
