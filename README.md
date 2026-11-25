# pku-spu

Animated Pokémon battle sprites as editable [SPU](https://github.com/prof64/spu)
files: drawings, parts, animations, shiny colors and lighting in one `.spu`
each. [Smeargle](https://smeargle.prof64.net) shows this library on its front
page.

| Folder | What is in it |
| --- | --- |
| `black2-white2/`, `uranium/`, `insurgence/` | The library: finished sprites, each looked over before it was filed here. `index.json` lists them, `thumbs/` has a picture of each. |
| `batches/` | Sprites made and waiting to be looked over, by batch. Smeargle shows them too, marked "In review". |
| `sources/` | Where new sprites start: every sprite of Pokémon Black 2 & White 2 (750, as the game stores them), Pokémon Uranium (334) and Pokémon Insurgence (50), as parts and animation without lighting. `sources/index.json` lists them. |

The artwork belongs to its original creators and the teams behind each game;
nothing here grants a license to it. The rigging and animation were made for
this library.

## One layout: Gen 5's

Every sprite in the library is laid out the way Black 2 and White 2 lay
theirs out, whichever game it comes from:

- **Real size.** One pixel of art is one pixel of the file. At rest a sprite
  fits Gen 5's 96 × 96 cell (the largest Gen 5 sprite is 111 across); a view's
  canvas is larger only where an animation reaches outside it.
- **A whole back.** The back shows the whole body, not the top half.
- **One scale.** Front and back are drawn at the same scale, so the two are
  about the same size.

The Gen 5 sources already are. The other two games' are not, and are redone
in this layout when they are made into library sprites:

| Sources | In the layout | What is different |
| --- | --- | --- |
| Black 2 & White 2 (750) | 717 | The 33 Pokéstar Studios props have only a placeholder back |
| Uranium (334) | none | 320 backs are drawn about 1.9 times as large as their fronts; 14 have no back |
| Insurgence (50) | 12 (the Deltas redone on Gen 5 rigs) | Most are kept at twice their size, and 34 backs are cut off at the bottom |

`tools/batch.py` checks this: `add` refuses a sprite that is not in the
layout, and `land` does not file one, unless it was added with `--as-is`.
Smeargle's review page says the same beside the sprite.

## Looking at sprites before they join

A sprite is looked at by a person before it goes in the library. Batches wait
in `batches/<name>/`, and `tools/batch.py` moves them along:

```sh
tools/batch.py add first-six black2-white2/0001-bulbasaur ~/work/bulbasaur.spu --note "what to look at"
tools/batch.py send first-six     # commit, push, and ask in the queue at console.prof64.net
tools/batch.py answer first-six   # what was answered
tools/batch.py land first-six     # file the good ones in the library, keep the rest to redo
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

The waiting sprites are listed, with thumbnails, in `batches/index.json`,
which the tool rewrites; the library itself is `index.json`.

The tool needs the `switchboard` command (to ask in the queue) and the `spu`
command from [the format's repository](https://github.com/prof64/spu) (to
check files and draw thumbnails).
