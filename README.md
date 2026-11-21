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

## One layout: Gen 5's

Every sprite in the rebuilt library (`v2/`) is laid out the way Black 2 and
White 2 lay theirs out, whichever game it comes from:

- **Real size.** One pixel of art is one pixel of the file. At rest a sprite
  fits Gen 5's 96 × 96 cell (the largest Gen 5 sprite is 111 across); a view's
  canvas is larger only where an animation reaches outside it.
- **A whole back.** The back shows the whole body, not the top half.
- **One scale.** Front and back are drawn at the same scale, so the two are
  about the same size.

The Gen 5 sprites already are. The other two games' are not yet, and are
redone in this layout before they are rebuilt in format 2 (measured
2026-11-20 on the version 1 files, at rest):

| Collection | In the layout | What is different |
| --- | --- | --- |
| Black 2 & White 2 (750) | 717 | The 33 Pokéstar Studios props have only a placeholder back |
| Uranium (334) | none | 320 backs are drawn about 1.9 times as large as their fronts; 14 have no back |
| Insurgence (47) | 9 (the Deltas already redone on Gen 5 rigs) | Most are kept at twice their size, and 34 backs are cut off at the bottom |

`tools/batch.py` checks this: `add` refuses a sprite that is not in the
layout, and `land` does not file one, unless it was added with `--as-is`.
Smeargle's review page says the same beside the sprite.

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
tools/batch.py remove first-six <id>   # take one sprite back out
tools/batch.py drop first-six     # give the batch up: withdraw its question, delete it
```

A batch asked about again (redone after what was said) is the next round of
the same question, so the queue shows one thing with its rounds: `send`
follows the batch's earlier question by itself (`--again` if that one is
still waiting, which the next round closes), and `send --follows <question>`
does when the redo has another name. `answer --wait` holds until the batch
has been looked at. `land --said-good <id>` files a sprite the owner called
good somewhere other than the queue's page, and leaves the rest waiting.

`send` and `land` commit and push the branch they are run on: work on a branch
and merge it (with a merge commit, so the commit a review points at stays).
The question shows `https://smeargle.prof64.net/?review=<name>&at=<commit>`:
every sprite of the batch lit and moving, to mark Good or Redo with a note.
Anyone can open that address to look.

Smeargle's front page shows the waiting sprites too, beside the library's
own and marked "In review", so what is being made can be seen before it is
looked over. They are listed, with thumbnails, in `batches/index.json`, which
the tool rewrites; only `v2/` is the library.

## Rebuilding

```sh
python3 tools/build.py --spu <path to the spu command> \
    --uranium <folder with Uranium's catalog.json and SPUs/> \
    --insurgence <folder of Insurgence .spu files>
```

Sources: `uranium-spu/dist/Uranium-SPUs-only.zip` (unzipped) and
`insurgence-spu/gallery/spus/`. Older files are upgraded to SPU version 1 and
every file is validated.
