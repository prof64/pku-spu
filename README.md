# pku-spu

Animated Pokémon fan-game battle sprites as editable [SPU](https://github.com/prof64/sprite-format)
files: drawings, parts, animations and shiny colors in one `.spu` each. This
is the library the Smeargle editor's Start screen browses.

| Collection | Sprites |
| --- | --- |
| `uranium/` — Pokémon Uranium | 334 |
| `insurgence/` — Pokémon Insurgence | 47 |

`index.json` lists every sprite with its name, file, thumbnail, views and
variants. `thumbs/` holds the first frame of each and `anim/` its first
animation as a looping animated PNG.

The artwork belongs to its original creators and the teams behind each game;
nothing here grants a license to it. The rigging and animation were made for
this library.

## Rebuilding

```sh
python3 tools/build.py --spu <path to the spu command> \
    --uranium <folder with Uranium's catalog.json and SPUs/> \
    --insurgence <folder of Insurgence .spu files>
```

Sources: `uranium-spu/dist/Uranium-SPUs-only.zip` (unzipped) and
`insurgence-spu/gallery/spus/`. Older files are upgraded to SPU version 1 and
every file is validated.
