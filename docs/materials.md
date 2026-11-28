# What Pokémon are made of

Research for giving each surface of a Gen 5 (Black 2/White 2) battle sprite the right material, using the SPU material model:

- **finish**: -1 fuzzy (fur, felt, down), 0 matte, +1 polished (hard white highlight, mirrors surroundings)
- **body**: -1 metal, 0 solid, 0.5 lets light through (it glows back out at the shadow edge; on skin this looks slick), +1 clear (bends what is behind)
- **glow**: 0 to 255, the surface gives off its own light

Smeargle names the ranges like this: finish below 0.25 is "matte", 0.25 to 0.75 "satin", 0.75 and up "polished"; body below 0.25 is "solid", 0.25 to 0.6 "translucent", 0.6 to 0.9 "frosted", 0.9 and up "clear", -0.75 and below "metal".

## The standard materials

Every surface uses one of these. Skin is not one material: each Pokémon gets the kind of skin its Pokédex entries and art describe, and a new kind is added here when a new kind of animal needs one. They are set to match the format demo's lit sprites, which the owner judged the best looking (Charizard above all): a soft sheen on skin with only a trace of light through it, light through only what is thin, hard things solid. A new kind of surface gets a new standard material here before it is used.

| Material | finish | body | glow | What you see | For |
|---|---|---|---|---|---|
| Frog skin | 0.3 | 0.1 | 0 | Smooth, a faint sheen, not wet | Amphibians (Bulbasaur, Ivysaur) |
| Bumpy hide | 0.15 | 0.06 | 0 | Thick and dull | Bumpy, thick amphibian hide (Venusaur) |
| Lizard skin | 0.35 | 0.1 | 0 | Smooth and warm, a soft sheen | Smooth reptiles (Charmander) |
| Scales | 0.35 | 0.08 | 0 | The same soft sheen as lizard skin: the art paints Charmeleon no glossier than Charmander | Scaled reptiles (Charmeleon) |
| Dragon hide | 0.5 | 0.05 | 0 | A soft sheen, solid | Dragons (Charizard, from the format demo) |
| Turtle skin | 0.5 | 0.08 | 0 | Smooth aquatic skin, a wetter sheen | Turtles that swim (Squirtle, Wartortle) |
| Thick hide | 0.4 | 0.06 | 0 | The same skin, heavier and less wet | Heavy, thick-skinned animals (Blastoise) |
| Larval skin | 0.45 | 0.15 | 0 | Soft, a highlight on every segment | Caterpillars and larvae (Caterpie). The cream underside, feet and tail tip are painted without highlights: finish 0.2 |
| Belly | 0.4 | 0.25 | 0 | A sheen, and a little light through | Pale, fleshy undersides (the Charmander line) |
| Fur | -0.7 | 0.05 | 0 | Soft, broken edges; a bright rim lit from the side | Fur |
| Fluff | -1 | 0.2 | 0 | The same, glowing faintly at the edge | Down, cotton |
| Short fur | -0.2 | 0.05 | 0 | Velvety and flat, a faint soft edge | Sleek short coats (Rattata, Raticate, Pikachu, Raichu); each marking its own row |
| Feathers | -0.2 | 0.05 | 0 | Soft and matte | Body plumage (Pidgey, Pidgeotto, Spearow, Fearow) |
| Glossy feathers | 0.3 | 0 | 0 | A soft sheen | Only where a Pokédex entry says so (Pidgeot: "beautifully glossy feathers") |
| Beak | 0.4 | 0.05 | 0 | Smooth horn, a soft lighter top | Birds' beaks |
| Insect shell | 0.45 | 0 | 0 | Hard, a clear soft sheen | Cocoons, a wasp's body, smooth insect limbs (Metapod, Kakuna, Beedrill, Butterfree's hands and feet) |
| Insect body | 0.2 | 0.05 | 0 | Nearly matte | A butterfly's soft body (Butterfree) |
| Insect wing | 0.4 | 0.3 | 0 | Pale, lights up from behind | Veined insect wings (Beedrill). More light through made them sparkle and stay bright in the cave |
| Butterfly wing | 0.05 | 0.3 | 0 | Powdery, lights up from behind | Butterfree's wings; black margins are a tinted row |
| Snake scales | 0.15 | 0.05 | 0 | Dry and nearly matte | Ekans, Arbok; bands and hood pattern are their own rows. First set to 0.35 for the soft light streaks the art paints along the coils; the owner asked why Arbok was shiny. A soft broad streak is the shape catching light, which the sprite's own shades already paint; only a small hard highlight means a sheen |
| Rattle | 0.2 | 0.05 | 0 | Dry, nearly matte | Ekans's rattle |
| Plated hide | 0.2 | 0.03 | 0 | Dry plates, a soft pale patch on each | Sandshrew, Sandslash |
| Dry hide | 0.05 | 0.03 | 0 | Dead matte | Bare bird legs and feet; Sandshrew's cream belly (body 0.08) |
| Hide | 0.25 | 0.08 | 0 | Plain bare skin | Nidoran♀, Nidorina; a rat's bare tail and feet |
| Spines | 0.4 | 0 | 0 | Hard, a little sheen | Quills, barbs and hide-colored horns (Sandslash, the Nidoran line) |
| Whiskers | 0.1 | 0.05 | 0 | Smooth single hairs, matte | Whiskers |
| Comb | 0.1 | 0.08 | 0 | Bare skin, matte | Fearow's comb |
| Shell | 0.2 | 0 | 0 | Dull and hard, one smooth dome | Turtle shells, their white rims, Blastoise's cannons |
| Belly plate | 0.15 | 0 | 0 | The same shell, matte; solid, so it goes dark with the rest of the body | The pale underside of a shell |
| Claw and tooth | 0.7 | 0.05 | 0 | A small bright highlight | Claws, talons, white horns, teeth, stingers |
| Eye | line art | | 0 | Stays as drawn | Every pixel of an eye: white, iris, pupil, catchlight |
| Mouth | 0.8 | 0 | 0 | A wet shine | The inside of a mouth |
| Leaf | 0.15 | 0.35 | 0 | Matte; lights up when the light is behind it | Leaves. Glossy only where a source shows a waxy leaf |
| Petal | 0.2 | 0.25 | 0 | Nearly matte; lights up a little from behind | Petals, a flower's center |
| Bud and bulb | 0.1 | 0.25 | 0 | Matte, like a soft leaf; a little light through | A closed bud, a seed bulb |
| Bark | -0.45 | 0.05 | 0 | Dry and rough | Trunks, stems |
| Wing membrane | 0.45 | 0.5 | 0 | Bright, and lights up from behind | Thin skin between wing bones (its outer, skin-colored side: body 0.3) |
| Fur, large areas | -0.1 | 0.05 | 0 | Soft, without grain | A mane, a big tail, a whole long coat (Arcanine, Eevee's ruff, Snorlax). At -0.7 anything bigger than a tuft turned grainy and muddy |
| Glossy fur | 0.3 | 0.05 | 0 | A soft sheen | Only where an entry says so (Vulpix's tails, Ninetales: "fur that gleams gold") |
| Bat wing | 0.3 | 0.3 | 0 | Lights up a little from behind | Zubat, Golbat, Dragonite. At 0.45 / 0.5 the wings went hot pink in daylight and stayed bright in the cave |
| Aquatic skin | 0.5 | 0.08 | 0 | Smooth, a wetter sheen | Golduck, Lapras ("smooth skin") |
| Fish skin | 0.15 | 0.08 | 0 | Matte | Fish and sea horses (Goldeen, Magikarp, Gyarados, Horsea, Vaporeon); fins are Fin 0.3 / 0.15 |
| Ghost body | -0.1 | 0 | 0 | Soft and dark | Haunter, Gengar. At -0.5 a big body went grainy |
| Balloon skin | 0.15 | 0.15 | 0 | Matte, a little light through | Koffing, Weezing ("thin, balloon-shaped body") |
| Bone | 0.2 | 0 | 0 | Dull white | Cubone's and Marowak's skull and club |
| Ball shell | 0.6 | 0 | 0 | A hard highlight | Voltorb, Electrode. Higher looked like chrome |
| Mushroom | 0.1 | 0.1 | 0 | Matte | Paras, Parasect |
| Cloth | -0.2 | 0 | 0 | Matte, soft | Hitmonchan's tunic, Jynx's gown; boxing gloves 0.2 / 0 |
| Plant body | 0.1 | 0.15 | 0 | Matte | Bellsprout's line, Oddish's line (0.1 through); Tangela's vines are -0.1 / 0.1 ("fine hair") |
| Soft body | 0.3 | 0.1 | 0 | Smooth, not wet | Ditto. Porygon is a matte solid, 0.1 / 0.05 |
| Metal | 0.7 | -1 | 0 | Mirrors the room, tinted | Real metal (gold 0.8) |
| Flame | 0 | 0 | 180 to 255 | Glows, lights what is around it, flickers | Fire: brightest at the core |
| Outline | 0.1 | 0 | 0 | Stays as drawn | The black line, and lines between overlapping pieces |

**Matte means matte.** Until 2026-11-26 every sprite looked shiny under the studio lamp, and a matte snake looked oiled, whatever its row said. The cause was the renderer, not the materials (Smeargle #86): a lit pixel was moved to a lighter shade and also drawn up to 1.4 times as bright; near a light it went to an invented shade paler than the palette's lightest; and a lamp in front of the sprite put most of every surface on its lightest shade. Now light stops at a row's own shades, full light shows a shade as the palette has it, and a surface facing the viewer keeps its base shade under any light in front of it. Sheen comes only from the finish dial, so check a new sprite under the studio lamp from the front: a matte row must stay its base color there. Two more causes showed on broad flat surfaces (Arbok's hood from behind) and were fixed the next day (Smeargle #87): every part's shape was blown up like a full balloon, so a hood the art paints in one flat shade was lit like a ball and carved into light and dark wedges, and the renderer stepped a lit pixel's brightness through three hard tiers on top of its shade. Matte and satin surfaces now start a fifth as tall and take their roundness from the painted shading; polished, metal and clear ones keep the full shape. So a surface's finish also decides how round it is lit: do not raise a finish to 0.6 or more without a source.

**Letting light through makes skin look slick.** Body above about 0.3 fills a surface's shadows with a warm glow and washes out its color; skin set that way looks gummy and wet. Keep skin, hide and scales at body 0.15 or less. A trace (0.05 to 0.1) is right for skin: with none, a surface facing the viewer gets much less of a low sun and the sprite goes dull.

**Hard things are solid.** A shell's pale underside set to let light through stays bright in a dark cave while the body around it goes dark, as if it glowed. Shell, plates, claws and horn get body 0.

**After changing a body value, work out facing again** (`bake_facing`): how far light moves a pixel between shades depends on it, so old facing no longer gives back the art.

## What every pixel is: shades, lines and marks

The two dials matter less than which pixels are given to which row, and what the row's shades and base are. Light only moves a pixel along its row's shades, and the facing data is worked out from how far each pixel's painted shade is from the row's base. These rules are what the first ten were made with (`tools/light.py`, one small file per sprite in `tools/lighting/`); each was tried the other way first, and an independent review of the lit pictures decided several of them.

- **Read the sprite pixel by pixel first.** `tools/light.py plan` draws every drawing with each pixel's color number on it. Colors are shared between surfaces (the same white is eye, claw, tooth and shell rim; a belly's shade is the hide's highlight; a shell and the plate under it share one brown ramp), so a color-to-material table alone is wrong: say which drawings, or which region of a drawing, each use belongs to.
- **A surface's dark contour color is one of its shades.** Gen 5 art draws a surface's contour in its own darkest color on the lit side. Keep it in the surface's row, as its darkest shade. Put in a line-art row it is only tinted, never shaded by direction, so with the light behind the sprite the contour and every seam come out brighter than the shadowed surface they are drawn on (a teal outline glowing around a dark Squirtle, orange grooves on a dark belly).
- **Seams drawn in black inside one surface are not creases.** Black lines wholly inside a shell (every neighbor the shell or more black) go in a row with **no shades**, named **seams and wrinkles**: light only tints it, and because it is not line art the shape is not creased along it, so the shell stays one smooth dome. Left in the outline row, each plate bulges like a pillow.
- **Lines between pieces that overlap are creases.** Petals of a bud or flower, lobes of a bulb, clumps of fur, a caterpillar's segments: one-pixel strokes of the dark color there go in the outline row, so each piece is rounded on its own.
- **Base is the shade most of the surface is painted in.** The base is the shade a surface facing the viewer shows. Setting it a step lighter than what the bulk of the surface uses (to make it "the lit color") bends the whole surface away from the art's light: a back view, which Gen 5 paints a step darker, then falls off the bottom of its ramp and goes black in a field or a cave (Blastoise's back did). Count what the surface uses where it shows, both views together, without the contour strokes and hidden pixels. A white rim painted white and gray takes its light gray.
- **A ramp is what the art uses on that surface.** Do not add another surface's color as an extra highlight (a brown shell given the belly's yellow as its top shade turns gold in strong light). Light stops at a row's darkest and lightest shade.
- **A rare highlight color is a painted glint, not a shade.** Where the art uses a surface's lightest color on only a few of its pixels (under about 7%), that color is left out of the row and its pixels stay as painted. Left in, any other light spreads it over a third of the surface in hard-edged pale patches: Kakuna looked like polished brass under a lamp, Squirtle's head got a white wedge, and Charizard's wings, given an undrawn brighter blue as a top shade, went frosted. `tools/light.py` does this by itself for rows of three or more shades below finish 0.6; `KEEP_TOP` in a sprite's file names a row to leave alone.
- **White with no gray.** A white drawn in one color needs a second shade or light cannot give the art back. Never pair it with black (the claw goes black in shade). Use the palette's gray; if it has none, its first color, which no pixel uses and is a pale gray in most Gen 5 palettes (check the shiny palette too).
- **Eyes are line art, all of them.** White, iris, pupil and a bright ring around a pupil go in one row named "eye (line art)". Shaded, an eye a few pixels across turns gray or olive whenever it faces away from the light; as line art it stays as drawn, and its catchlight is already painted.
- **A mouth is wet, not lit from inside.** Finish 0.8, solid. With light through it, an open mouth stays vivid in a dark cave.
- **Markings.** A darker patch wholly inside lighter skin is pigment: its own row with the skin's dials and the skin's ramp one step down, so light reads it as color, not as a dent.
- **Fire.** Only the flame's own colors are in its row (not the dark tail tip under it); glow is strongest at the core, and the part's emission follows its drawn flicker, brighter on the bigger drawing.
- **Sheen needs a source: look at the painted art, part by part.** The Sugimori art paints light patches and highlights where a surface has a sheen (Squirtle's skin, Caterpie's green segments and antenna, claws, eyes) and flat soft shading where it has none (Bulbasaur's bulb, leaves and petals, every turtle shell and its rim and plate, Blastoise's cannons, cream bellies and undersides). Set each part from that, not from what the real plant or animal is like, and not from the HOME model alone, whose shading is soft on everything. Shells were first made glossy because real shells can be; the art shows them dull.
- **Check.** `tools/light.py check`: light alone must give back the art at rest for every pixel, in every look (shiny, eyes closed, female), and no row may be unused. Then look, front and back: field, studio, cave, rain, lit from behind and from the right, and the material map. Then someone who did not make it looks.

## How this was checked

- **Pokédex text**: every quote below is game text, taken from PokeAPI's species data (which mirrors each game's entries) and cross-checked for Black/White against Serebii's Black/White Pokédex pages (Bulbasaur, Charmander, Charizard, Blastoise and Caterpie matched word for word). The Black 2/White 2 entry is given first wherever it says something about material, since these are Black 2/White 2 sprites. Older entries keep the games' own capitals ("POKéMON").
- **Bulbapedia** (Biology, Origin and Trivia sections): Bulbapedia blocks automated reading, so the pages were read from Internet Archive snapshots taken December 30, 2025 to January 2, 2026 (links at the end).
- **Official art**: the Ken Sugimori-style artwork on the official Pokédex, and the **3D models** as rendered for Pokémon HOME (both from the PokeAPI sprite repository), were looked at directly.
- **The sprites themselves**: the Black 2/White 2 sources in `sources/black2-white2/` were rendered front and back to list the surfaces that are actually drawn, check which have an "eyes closed" look, and time the tail flames.

Nothing in any official source says how shiny or how see-through a surface is, so every number is a judgment from what the thing is. The confidence column says how directly the evidence supports it: **high** = a Pokédex entry or Bulbapedia names the material and the art agrees; **medium** = the material is named or clearly drawn, but the dial value is inferred from what that material is like in life; **low** = not stated anywhere official, an inference from design or origin.

## Rules that apply to all ten

These are not repeated in every table unless something differs.

| Surface | Made of | finish | body | glow | Why |
|---|---|---|---|---|---|
| Eyes | wet eyeball | line art | | 0 | At sprite size an eye is a few pixels and its highlight is already painted; shaded, it goes gray when it faces away from the light. The whole eye is one line-art row. None of the ten has an entry or art showing glowing eyes. |
| Mouth interior, tongue | wet tissue | 0.8 | 0 | 0 | Wet and fleshy. Usually 10 to 30 pixels, so the exact value matters little. |
| Teeth, fangs | enamel | 0.7 | 0.05 | 0 | Hard and smooth; often 1 or 2 pixels. |
| Claws | keratin | 0.7 | 0.05 | 0 | Like nails and horn: smooth and hard. |
| Painted markings (spots, cheek streaks, side rings) | pigment in the same skin | same as the surface they sit on | same | 0 | They are color, not a different material. Give them **their own material row with the same dials**, so the light treats them as color and does not read them as bumps (the lab's finding about markings painted as shades). |
| Outline | line art | Smeargle's outline row | | | Not a surface. |

---

## Part 1: the first ten Pokémon

### Bulbasaur (#001)

Drawn surfaces (front and back): skin, darker spots, bulb, claws, eyes (red with white pupils), open mouth with a tooth. Bulbasaur is a frog: Bulbapedia's Origin section says "Bulbasaur is based on a frog", and Ken Sugimori has said the line was inspired by frogs.

| Surface | Made of | Material | Evidence | Confidence |
|---|---|---|---|---|
| Skin (blue-green) | smooth amphibian skin | Frog skin | Bulbapedia Biology: "a small, quadrupedal amphibian Pokémon that has blue-green skin with darker patches." Official art is flat, matte watercolor; the HOME model is smooth with one soft broad highlight, no wet shine. **No Pokédex entry or Bulbapedia text calls the skin moist, slimy or glossy** (searched), so it is Frog skin: a faint sheen, not wet. | medium |
| Darker spots | pigment | Frog skin | Bulbapedia: "darker patches". Flat in art and the 3D model. Own material row. | high |
| Bulb | plant bulb grown from a seed: firm, fleshy plant tissue | Bud and bulb | Black 2/White 2: "For some time after its birth, it grows by gaining nourishment from the seed on its back." Yellow: "In the bulb on its back, it stores energy." Gold: "The seed on its back is filled with nutrients." Bulbapedia: "a green plant bulb... The bulb also provides it with energy through photosynthesis"; Origin: "The bulb on its back resembles a lily or onion." The official art and the HOME model both draw it matte, with soft broad shading and no highlight, like a closed bud of soft leaves: Bud and bulb, matte, a little light through. (It was first given a waxy sheen with nothing behind it but "bulbs are waxy"; the owner asked why it was shiny.) The lines between its lobes are creases. | medium |
| Claws | keratin | Claw and tooth | Bulbapedia: "Each of its thick legs ends with three sharp claws." White in art and sprite. | medium |
| Eyes, mouth, tooth | see shared rules | see shared rules | Bulbapedia: "red eyes with white pupils"; "Small, pointed teeth are visible in the upper jaw when the mouth is open." | high |

Notes: nothing on Bulbasaur glows. Bulbapedia mentions the bulb flashing blue before evolving, but that is an anime event, not a battle look.

### Ivysaur (#002)

Drawn surfaces: skin, darker patches, ear insides (dark), pink bud, leaves, claws, eyes, two small fangs. The brown trunk Bulbapedia describes is hidden by the leaves on this sprite.

| Surface | Made of | Material | Evidence | Confidence |
|---|---|---|---|---|
| Skin | smooth amphibian skin | Frog skin | Bulbapedia: "a quadrupedal amphibian Pokémon that has blue-green skin with darker patches." Same as Bulbasaur. | medium |
| Darker patches, ear insides | pigment | Frog skin | Bulbapedia: "pointed ears with black insides". Own row. | high |
| Bud (pink) | closed flower bud: thick, fleshy, tightly wrapped petals | Bud and bulb | Black 2/White 2: "When the bud on its back starts swelling, a sweet aroma wafts to indicate the flower's coming bloom." Gold: "Sunlight also makes the bud on its back grow larger." Bulbapedia Origin: "The bud on its back resembles a Rafflesia flower." Rafflesia buds are thick and fleshy: Bud and bulb, a little light through. The lines between its petals are creases. | medium |
| Leaves (fronds) | palm-like leaves | Leaf | Bulbapedia: "leafy green fronds"; Origin: "the leaves around the bud resemble palms." Palm leaves are thin: Leaf lets light through when lit from behind. | medium |
| Claws, eyes, fangs | see shared rules | see shared rules | Bulbapedia: "narrow red eyes", "two pointed teeth in its upper jaw", "Each of its feet has three claws". | high |

### Venusaur (#003)

Drawn surfaces: skin (bumpy, with lighter bumps and darker patches), ear insides (red), petals, white petal spots, yellow crown at the flower's center, brown trunk, leaves, white claws, red eyes, teeth. The sprite has a Female look that redraws the yellow center.

| Surface | Made of | Material | Evidence | Confidence |
|---|---|---|---|---|
| Skin | thicker, bumpy amphibian hide | Bumpy hide | Bulbapedia: "a squat, quadrupedal amphibian Pokémon with bumpy, blue-green skin." Art shows small bumps along the back and legs. | medium |
| Bumps and darker patches | real bumps plus pigment | Bumpy hide | Here the light dots **are** bumps ("bumpy"), so they may stay in the skin row and let the light shape them; the darker patches get their own row. | medium |
| Ear insides | skin | Bumpy hide | Bulbapedia: "small, pointed ears with reddish-pink insides." | high |
| Petals (pink-red) | large, thick, fleshy petals | Petal | Gold, HeartGold, X and Violet: "By spreading the broad petals of its flower and catching the sun's rays, it fills its body with power." Ruby/Sapphire: "The flower is said to take on vivid colors if it gets plenty of nutrition and sunlight." Bulbapedia Origin: "The flower on its back resembles the Rafflesia arnoldii", a thick, leathery, matte flower with pale warts. Thick, so Petal lets only a little light through. Art and HOME both show them matte. | medium |
| White petal spots | pigment (Rafflesia-like warts) | Petal | Bulbapedia: "a large pink, white-spotted flower". Own row. | high |
| Flower center (yellow crown) | floral organ | Petal | Bulbapedia: "A female Venusaur has a gynoecium in the center of its flower." The crown is on the default (male) sprite too and is redrawn for the female; it sits on top of the trunk in both the art and the HOME model. Not described in any Pokédex entry. | low |
| Trunk (brown) | palm-like trunk | Bark | Bulbapedia: "The flower is supported by a thick, brown trunk surrounded by green fronds." Art shows a zigzag, palm-trunk texture; HOME shows it matte. Palm trunks are dry and fibrous: slightly below matte so it mottles, not fur. | medium |
| Leaves | palm-like leaves | Leaf | Same as Ivysaur. Black 2/White 2 is about smell, not material: "After a rainy day, the flower on its back smells stronger." | medium |
| Claws, eyes, teeth | see shared rules | see shared rules | Bulbapedia: "small, circular red eyes", "three clawed toes on each foot", "two pointed teeth in the upper jaw and four in the lower jaw". | high |

### Charmander (#004)

Drawn surfaces: orange skin, cream belly and soles, tail flame (yellow core, orange-red outer tongues), white claws on the feet, blue eyes, open mouth with fangs.

| Surface | Made of | Material | Evidence | Confidence |
|---|---|---|---|---|
| Skin (orange) | smooth lizard skin | Lizard skin | Bulbapedia: "a bipedal, reptilian Pokémon with a primarily orange body"; Origin: "Charmander was designed as a lizard", also a salamander. No entry mentions scales on Charmander; art and HOME show it smooth with a soft sheen: Lizard skin. | medium |
| Belly and soles (cream) | the same skin, lighter | Belly | Bulbapedia: "Its underside from the chest down and the soles of its feet are cream-colored." Own row. | high |
| Tail flame, yellow core | fire | Flame (glow 230) | Black 2/White 2: "The fire on the tip of its tail is a measure of its life. If healthy, its tail burns intensely." Silver: "If it is healthy, the flame burns brightly." | high |
| Tail flame, orange-red outer tongues | fire, cooler edge | Flame (glow 180) | Same entries. The outer flame is redder and dimmer in the art, the HOME model and the sprite. | high |
| Claws, eyes, mouth, fangs | see shared rules | see shared rules | Bulbapedia: "blue eyes", "two small fangs visible in its upper jaw". | high |

How the flame should behave:
- **Brightness tracks health and mood.** Gold: "The flame on its tail shows the strength of its life force. If it is weak, the flame also burns weakly." Ruby/Sapphire: "The flame that burns at the tip of its tail is an indication of its emotions. The flame wavers when CHARMANDER is enjoying itself. If the POKéMON becomes enraged, the flame burns fiercely." FireRed: "Its life would end if the flame were to go out." So: the battle default is a healthy flame (values above). If anything ever drives it from HP, scale the flame's glow down to about 40% near fainting, never to zero; an angry look could push it up.
- **It flickers, and the sprite already does.** The Black 2/White 2 idle swaps between four flame drawings every 6 ticks (10 times a second). Key the flame part's glow multiplier to those swaps (about 1.0 on the largest drawing, 0.85 on the smallest), so brightness flickers with the shape. Yellow: "The flame at the tip of its tail makes a sound as it burns."
- **Glow does the work for fire**: the Flame material lets light through so its shadow side does not go dark.
- Red/Blue: "When it rains, steam is said to spout from the tip of its tail" (for a rain scene, not a material).

### Charmeleon (#005)

Drawn surfaces: dark red skin, cream belly and soles, head horn, white claws (long, on hands and feet), tail flame with loose embers, blue eyes, closed mouth.

| Surface | Made of | Material | Evidence | Confidence |
|---|---|---|---|---|
| Skin (dark red) | scaly reptile hide | Scales | Bulbapedia: "It has dark red scales and a cream underside from the chest down." No Pokédex entry describes the skin; art and HOME show no visible scale pattern. Its scales are harder than Charmander's skin, so a clearer sheen: Scales. | medium-low |
| Belly and soles (cream) | the same hide | Belly | Bulbapedia: "cream-colored soles". Own row. | high |
| Head horn | skin-covered horn | Scales | Bulbapedia: "On the back of its head is a single horn-like protrusion." Same color as the skin in art and sprite, so it is skin over horn, not bare keratin. | low |
| Claws | keratin | Claw and tooth | Bulbapedia: "relatively long arms with three sharp claws". Ruby/Sapphire: "CHARMELEON mercilessly destroys its foes using its sharp claws." | medium |
| Tail flame, core | fire | Flame (glow 240) | Black 2/White 2: "In the rocky mountains where Charmeleon live, their fiery tails shine at night like stars." Red/Blue: "When it swings its burning tail, it elevates the temperature to unbearably high levels." | high |
| Tail flame, outer tongues and embers | fire | Flame (glow 200) | Same. The sprite draws loose embers around the flame: give them the core's glow and let them flicker with it. | high |
| Eyes, mouth | see shared rules | see shared rules |  | high |

Note: when excited the flame turns bluish white. Ruby/Sapphire: "In this excited state, the flame at the tip of its tail flares with a bluish white color." Yellow: "When excited, it may blow out bluish-white flames." That would be a look (a palette swap), not a material.

### Charizard (#006)

Drawn surfaces: orange skin, cream belly, underside of tail and soles, wing membranes (teal on the inner side, orange outer edges), wing arms and finger (orange), two head horns, white claws, tail flame, blue eyes, open mouth with fangs. On this sprite the spur at each wing's joint is orange like the skin.

| Surface | Made of | Material | Evidence | Confidence |
|---|---|---|---|---|
| Body skin (orange) | dragon-like reptile skin | Dragon hide | Bulbapedia: "a draconic, bipedal Pokémon. It is primarily orange"; Origin: European dragons, lizards. Smooth in art and HOME. | medium |
| Belly, tail underside, soles (cream) | the same skin | Belly | Bulbapedia: "a cream underside from the chest to the tip of its tail", "cream-colored soles". Own row. | high |
| Wing membrane | thin skin stretched between wing bones | Wing membrane | Bulbapedia: "Two large wings with blue-green undersides sprout from its back... A single wing finger is visible through the center of each wing membrane." FireRed, Y, Shield: "Its wings can carry this Pokémon close to an altitude of 4,600 feet." **No official text or art says light passes through** (searched); translucency comes from what a wing membrane is (bat and pterosaur wings are thin skin). The two sides are colored differently, so it is pigmented skin: lets light through, never clear. This is the strongest visual effect on the sprite and worth keeping. | medium-low |
| Wing, outer side (orange, the whole wing seen from behind) | the same thin membrane, its skin-colored side | Wing membrane, body 0.3 | Same sources as the membrane. From behind the wing is all orange and the arm is not drawn apart from the membrane, so the whole wing lets a little light through: it glows when the sun or the tail flame is behind it. | low |
| Wing arms, finger and outer edge (orange, front view) | skin over bone | Dragon hide | Same color and outline as the body in art and sprite. | medium |
| Wing spur | horn | Dragon hide | Bulbapedia: "a horn-like appendage juts out from the top of the third joint of each wing." Skin-colored on this sprite; barely a few pixels. | low |
| Head horns | skin-covered horn | Dragon hide | Bulbapedia: "two horn-like structures protruding from the back of its rectangular head." Orange like the skin in art and HOME. | low |
| Claws | keratin | Claw and tooth | Bulbapedia: "each limb has three white claws." | medium |
| Tail flame, core | fire | Flame (glow 255) | Black 2/White 2: "It is said that Charizard's fire burns hotter if it has experienced harsh battles." Yellow: "When expelling a blast of super hot fire, the red flame at the tip of its tail burns more intensely." Red/Blue: "Spits fire that is hot enough to melt boulders." | high |
| Tail flame, outer tongues | fire | Flame (glow 215) | Same. Flicker as for Charmander. | high |
| Eyes, mouth, fangs | see shared rules | see shared rules | Bulbapedia: "small blue eyes", "Two fangs are visible in its upper jaw". **The open mouth does not glow**: only Gigantamax Charizard has "The glow of a flame can be seen in the mouth" (Bulbapedia). Fire it breathes in an attack is an effect, not the mouth. | high |

Note: Gold: "If CHARIZARD becomes furious, the flame at the tip of its tail flares up in a whitish-blue color." As with Charmeleon, that is a look, not a material.

### Squirtle (#007)

Drawn surfaces: light blue skin, brown upper shell (back view), pale yellow belly plate (front view), white rim between them, curled tail, reddish-brown eyes, open mouth.

**Is the shell glossy keratin?** The games never name the material. What they say: it grows out of the back and hardens (Red/Blue: "After birth, its back swells and hardens into a shell."), it is springy rather than brittle (Gold: "The shell is soft when it is born. It soon becomes so resilient, prodding fingers will bounce off it."), and it is smooth and streamlined (Ruby/Sapphire: "The shell's rounded shape and the grooves on its surface help minimize resistance in water, enabling this POKéMON to swim at high speeds."). That is a real turtle shell: bone grown from the back, covered in hard plates. Art and HOME show a soft sheen, not a mirror. So: satin, solid.

| Surface | Made of | Material | Evidence | Confidence |
|---|---|---|---|---|
| Skin (light blue) | smooth aquatic reptile skin | Turtle skin | Bulbapedia: "a small reptilian Pokémon that resembles a light-blue turtle"; Origin: baby turtles and terrapins; lives "around small ponds and lakes". Art and HOME: smooth, with a soft sheen; Turtle skin, a little wetter than land skin. | medium |
| Upper shell (brown) | hard, smooth, springy shell | Shell | The entries quoted above. Bulbapedia: "Its body is encased by a tough shell that forms and hardens after birth." Black 2/White 2: "It shelters itself in its shell then strikes back with spouts of water at every opportunity." | medium |
| Belly plate (pale yellow) | the same shell, underside | Belly plate | Bulbapedia: "This shell is brown on the top, pale yellow on the bottom". The drawn grooves are lines, not a different material. | medium |
| Shell rim (white) | the same shell | Shell | Bulbapedia: "has a thick white ridge between the two halves." | medium |
| Tail | skin | Turtle skin | Bulbapedia: "The end of its long, squirrel-like tail curls inward." | high |
| Eyes, mouth | see shared rules | see shared rules | Bulbapedia: "large, purplish, or reddish eyes". | high |

### Wartortle (#008)

Drawn surfaces: blue skin, dark cheek streaks, furry ears, big furry tail, brown upper shell, pale yellow belly plate, white rim, white claws, two fangs, brown eyes.

| Surface | Made of | Material | Evidence | Confidence |
|---|---|---|---|---|
| Skin (blue) | smooth aquatic reptile skin | Turtle skin | Bulbapedia: "a bipedal, indigo reptilian Pokémon similar to a turtle." | medium |
| Cheek streaks | pigment | Turtle skin | Bulbapedia: "a dark blue streak on each cheek". Own row. | high |
| Ear fur | fur | Fur | Silver and SoulSilver: "It cleverly controls its furry ears and tail to maintain its balance while swimming." Bulbapedia: "feather-like ears covered in pale blue fur". Fully fuzzy so it reads clearly at sprite size. | high |
| Tail fur | thick fur | Fur (its blue swirl lines their own Fur row) | Black 2/White 2: "It is said to live 10,000 years. Its furry tail is popular as a symbol of longevity." Ruby/Sapphire: "Its tail is large and covered with a rich, thick fur." Bulbapedia: "Air can be stored in its fur". Thick fur, so it does not let light through. Origin: the minogame, a 10,000-year-old turtle with a seaweed tail. | high |
| Upper shell (brown) | hard shell, scratched with age | Shell | Ruby/Sapphire: "The scratches on its shell are evidence of this POKéMON's toughness as a battler." Gold: "If its shell has algae on it, that WARTORTLE is very old." A worn, older shell: a little less shine than Squirtle's. | medium |
| Belly plate (pale yellow) | the same shell | Belly plate | Bulbapedia: "A brown shell with a pale yellow underside encases its body." | medium |
| Shell rim (white) | the same shell | Shell | Bulbapedia: "A thick, white rim separates the upper and lower halves of the shell." | medium |
| Claws, fangs, eyes | see shared rules | see shared rules | Bulbapedia: "brown eyes", "two sharp teeth protruding from its upper jaw", "three clawed fingers". | high |

### Blastoise (#009)

Drawn surfaces: blue skin, cream lower jaw, ear insides (black), brown upper shell, cream belly plate, white rim (around the arms too), two cannons with dark openings, white claws, brown eyes.

**Are the cannons gray metal?** Not by the evidence. No Pokédex entry or official page calls them metal: Black 2/White 2 calls them "rocket cannons", Violet "jet nozzles", Ruby/Sapphire "water spouts that protrude from its shell", and the official Gigantamax page "water cannons". Bulbapedia says "These cannons can be extended or withdrawn", which makes them part of the shell. In the Sugimori art and the HOME model they are **white with pale gray shading, the same white as the shell rim**, with no reflections and no metallic tint. The only metal hints are the word "rocket cannons" and Bulbapedia's Origin note that the design is "a turtle mixed with aspects of a tank". The Black 2/White 2 sprite draws them in a gray ramp with a white highlight band, which makes them look more like metal than the art does.

So they are shell, like the rim, and as dull: the Sugimori art paints them the rim's own off-white with soft shading and no highlight. (They were first made polished, from the sprite's gray ramp, and before that metal was tried, which mirrors the place and turns them green in a field.)

| Surface | Made of | Material | Evidence | Confidence |
|---|---|---|---|---|
| Skin (blue) | heavy, thick reptile skin | Thick hide | Bulbapedia: "Its body is blue and is mostly hidden by its tough, brown shell." HeartGold: "It deliberately makes itself heavy so it can withstand the recoil of the water jets it fires." | medium |
| Lower jaw (cream), ear insides (black) | the same skin | Thick hide, as its own cream row; the ear insides are drawn black, so line | Bulbapedia: "triangular ears that are black on the inside", "a cream-colored lower jaw". Own rows. | high |
| Upper shell (brown) | tough shell | Shell | Bulbapedia: "tough, brown shell". FireRed, X, Sword: "In a pinch, it will withdraw inside its shell." Art: weathered brown plates; HOME: soft sheen. | medium |
| Belly plate (cream) | the same shell | Belly plate | Bulbapedia: "This shell has a cream-colored underside". | medium |
| Shell rim (white) | the same shell | Shell | Bulbapedia: "a white ridge encircling its arms and separating the upper and lower halves." | medium |
| Cannons | hard tubes that grow from the shell (material never stated) | Shell | See above. | medium |
| Cannon openings (dark) | a hole | Outline | Keep dark; do not let a highlight land in it. | high |
| Claws, eyes | see shared rules | see shared rules | Bulbapedia: "small brown eyes", "three claws on each hand". | high |

Nothing on Blastoise glows. The water it fires is an attack effect, not part of the sprite.

### Caterpie (#010)

Drawn surfaces: green body segments, cream-yellow belly and feet, eye (black with a yellow ring) on each side of the head, yellow ring spots along the sides, red forked antenna with orange tips, yellow teardrop tail tip.

| Surface | Made of | Material | Evidence | Confidence |
|---|---|---|---|---|
| Body segments (green) | soft caterpillar skin | Larval skin | FireRed: "It is covered with a green skin. When it grows, it sheds the skin, covers itself with silk, and becomes a cocoon." Ultra Moon: "Its body is soft and weak." Black 2/White 2: "It grows by molting repeatedly." Crystal: "It crawls into foliage where it camouflages itself among leaves that are the same color as its body." Sugimori art draws white highlights on every segment and HOME shows slightly shiny segments, so Larval skin: that sheen, and only a little light through (more looked slick). | medium |
| Belly and feet (cream-yellow) | the same soft skin | Larval skin (the pale parts row) | Red/Blue: "Its short feet are tipped with suction pads that enable it to tirelessly climb slopes and walls." Bulbapedia: "a green caterpillar with a yellow underside". | medium |
| Eye (black with yellow ring) | eye | Eye | Bulbapedia Trivia: "It is inconsistent across the franchise whether or not the yellow and black spots on Caterpie's head are actually its eyes or merely spots resembling eyes." **On this sprite they are eyes**: the Black 2/White 2 sprite has an "eyes closed" look that shuts them with a green lid. | high (for this sprite) |
| Side ring spots (yellow) | pigment, false eyes | Larval skin | Bulbapedia: "Yellow ring-shaped markings down the sides of its segmented body resemble its eyes and are meant to scare off predators." Origin: swallowtail caterpillars' "yellow eyespots". Painted marks on the skin; own row. **No glow**: nothing says they give off light. | high |
| Red antenna (osmeterium) | soft scent organ | Larval skin | Black 2/White 2: "It releases a stench from its red antenna to repel enemies." Sword: "For protection, it releases a horrible stench from the antenna on its head to drive away enemies." Yellow: "If you touch the feeler on top of its head, it will release a horrible stink to protect itself." Bulbapedia: "the bright red antenna (osmeterium) on its head, which releases a stench to repel predators." A real swallowtail's osmeterium is soft, moist tissue (real-world biology, not game text); Larval skin. **No glow**: its color is a warning, not light. | glow 0: high; material: medium-low |
| Tail tip (yellow teardrop) | soft horn-like tip | Larval skin (the pale parts row) | Bulbapedia: "teardrop-shaped tail"; Origin: "The tip of its tail resembles the horn that many species of hawk moth larvae have on their rear ends." Those horns are soft skin. | low |
| Mouth | see shared rules | see shared rules | Small and dark on this sprite. | high |

## Part 1, continued: #011 to #030

Made one evolution line at a time, each part set from the Sugimori art first (light patches and highlights mean a sheen, flat soft shading means matte), then the Pokédex text, then checked lit by someone who did not make it. Quotes are game text from PokeAPI's species data; "HOME" is the Pokémon HOME render, used for shape and color only.

What that review changed across the set: short coats were first given more fuzz (-0.35), which left a bright dotted rim around a backlit Pikachu and a streaked white belly on Raichu, so Short fur is -0.2; beaks were first Claw and tooth (0.7) and went dark maroon in shade, and the art paints them with only a soft lighter top, so Beak is 0.4; Sandshrew's plates each have a soft pale patch in the art, so they are Plated hide (0.2), not dead matte; Spearow's flat black back is only tinted, so it does not lift to gray. Raichu alone glows, very faintly (glow 4 on the coat): Sapphire says "This POKéMON exudes a weak electrical charge from all over its body that makes it take on a slight glow in darkness." At glow 26 it lit the whole cave.

### Metapod (#011)


| Surface | Made of | Material | Evidence | Confidence |
|---|---|---|---|---|
| Shell (all the green) | hard chitin cocoon | Insect shell (0.45 / 0) | Black 2/White 2: "A steel-hard shell protects its tender body." Ruby/Sapphire: "The shell covering this POKéMON's body is as hard as an iron slab." Moon: "Its shell is hard, but it's still just a bug shell." Art: soft lighter patches on the horn, plates and belly, no white highlights, so satin rather than polished. | high |
| Plate lines and tail rings (dark green lines inside the shell) | edges between raised plates and overlapping rings | Outline (creases) | Art: the big plate under the eye overhangs the body with a shadow under its corner, and the tail is drawn as separate bulging rings. HOME models each plate as its own raised facet. The shell's outer contour in the same dark greens stays the shell's darkest shade. | medium |
| Eye (white, black pupil) | eye | Eye (line art) | Art: white eye with a heavy lid. The back view draws one pupil pixel in dark green; it is in the eye row. The eyes-closed lid is shell. | high |

Nothing glows. Base is the mid green (color 3), which most of both views is painted in.

### Butterfree (#012)


| Surface | Made of | Material | Evidence | Confidence |
|---|---|---|---|---|
| Wings (white, lavender and gray shading) | thin wing covered in powdery scales | Butterfly wing, 0.05 / 0.3 (starting row: 0.4) | Yellow: "Its wings, covered with poisonous powders, repel water." Ultra Sun: "Its wings are covered in toxic scales." FireRed: "The wings are protected by rain-repellent dust." Art: flat white with pale blue shading, no highlight, so matte. | finish high; light-through medium |
| Black wing margins and bands (navy) | pigment in the same wing | Butterfly wing, black markings (wing dials, no shades) | Art: flat black, no highlight. The sprite draws them in one navy, so light only tints them. They are not line art, so the wing is not creased along them. | high |
| Wing veins and the wings' soft upper edge (purple lines) | veins in one flat sheet | Seams and wrinkles | Art and HOME: thin lines on a flat wing, with no shading per cell. | medium |
| Female lower-wing patches (purple) | pigment | Butterfly wing, female spots (wing dials) | Painted by the sprite's Female look. Own row, with the navy as the darker shade. | high |
| Head, thorax, abdomen (purple) | an adult insect's body | Insect body, 0.2 / 0.05 (new kind) | No Pokédex entry describes the body. Art: soft shading with only a faint lighter area on the head. HOME is matte. | medium-low |
| Snout, hands, feet (blue) | smooth hard limbs | Insect shell (0.45 / 0), own row | Art paints a clear lighter patch on the snout, each hand and near each foot's tip. Gold/HeartGold/Shield: "It rubs honey onto the hairs on its legs to carry it back to its nest", but neither the art, HOME nor the sprite draws hair. | medium |
| Fangs (two white pixels) | tooth | Claw and tooth | Art: two small white fangs under the snout. The palette's first color is green, so the white's shade is the wings' pale lavender. | high |
| Eyes (red, pink highlight, dark red rim) | compound eyes | Eye (line art) | Sun: "each eye is composed of a myriad of tiny eyes." The art and the sprite both paint the highlight. | high |
| Antennae | thin black stalks | Outline | One pixel wide and black, with two dark pixels on each club tip. | high |
| Line between head and thorax | one ball overlapping the other | Outline (crease) | Drawn in navy at the neck in both views. | high |

Nothing glows. The wing base is white (color 14) and the body base is the dark purple (color 2).

### Weedle (#013)


| Surface | Made of | Material | Evidence | Confidence |
|---|---|---|---|---|
| Body: head and segments (brown) | soft larval skin | Larval skin, **finish 0.35** (standard 0.45), body 0.15 | Gold/HeartGold/Y: "Its bright-colored body is intended to warn off its enemies." No entry says what the skin is like. Art: a soft, broad pale patch on the upper left of the head and a soft lighter band on each segment, no white highlights like Caterpie's; HOME: soft everywhere. So a softer sheen than Caterpie's. The sprite paints one small pale patch on the front of the head. | medium |
| Nose (pink) | soft fleshy snout | Larval skin, own row "nose and feet", finish 0.45, body 0.15 | Ruby/Sapphire: "sniffing with its big red proboscis (nose)." Art: a crisp pale highlight spot on the nose. | medium |
| Feet (pink balls along the body) | the same soft pink tissue | same row as the nose | Not described in any entry. Art: every pink foot has its own small highlight dot. | medium |
| Head stinger, tail stinger (white, gray) | hard horn-like needle | Claw and tooth 0.7 / 0.05 | Black 2/White 2: "It fends off attackers with the needle on its head." FireRed/X: "a sharp, toxic barb of around two inches on top of its head." Red/Blue: "a sharp venomous stinger on its head." Art: white with gray shade; the tail stinger carries a white streak. Its dark gray edge is its darkest shade. | high |
| Eyes (black, white catchlight, a gray pixel) | eye | Eye (line art) | Art: black bead eyes with a white catchlight. Includes the eye drawn on the head itself in the back view. Closed eyes are drawn as black lines (outline). | high |
| Line between the two segments drawn in one picture (body4 both views, body5 back) | crease | Outline | Segments are separate bulges; the other segments are separate pictures, whose brown contour stays the skin's darkest shade. | high |

### Kakuna (#014)


| Surface | Made of | Material | Evidence | Confidence |
|---|---|---|---|---|
| Whole cocoon (yellow): head dome, shoulder plates, folded arms, tail rings | hard shell | Insect shell 0.45 / 0 | Red/Blue: "this POKéMON can only harden its shell to protect itself from predators." Silver/SoulSilver: "As its body becomes softer, the external shell hardens." Ruby/Sapphire: "how hot the shell becomes to the touch." Gold: "Although it is a cocoon, it can move a little." Art: a small pale highlight on the dome and pale edges on the plates: a satin sheen, no mirror. The sprite paints pale highlight patches on the head, an arm and the tail end. | high |
| Dark lines between plates (inside body, arms, neck) | where plates overlap | Outline (creases) | Art draws the shoulder plates, arms and tail rings as separate raised pieces, each shaded on its own. The same dark brown along the outside is the shell's darkest shade; the softer brown beside the lines stays shell. | medium |
| Eyes (black with gray sheen and white catchlight) | eye | Eye (line art) | Art: black triangular eyes with a white catchlight. The eyes-closed look is drawn the same as open in this sprite. | high |

### Beedrill (#015)


| Surface | Made of | Material | Evidence | Confidence |
|---|---|---|---|---|
| Head, thorax, abdomen (yellow) | hard wasp shell | Insect shell 0.45 / 0 | No entry names the body's surface (they are about speed and stingers: Black 2/White 2: "flying around at high speed, striking with poison needles"). Art: small pale highlights on the head, thorax and each yellow band; HOME: smooth. | medium |
| Black bands on the abdomen | pigment in the same shell | Insect shell, own row "stripes" (black with the blue-gray the sprite paints as its sheen) | Art: black bands with a gray highlight band on the upper left, the same sheen as the yellow. The black along the silhouette stays outline. | high |
| Legs, arms, antennae (drawn black with a blue-gray lit side) | the same hard shell, thin | Insect shell, own row "limbs" | Art: dark gray-purple limbs with a soft lighter side, no crisp highlight. They are surfaces, not line art, so light shapes them. One lilac pixel on a back-view antenna stays as drawn (outline). | medium |
| Arm stingers (white to lilac-gray cones) | hard needle | Claw and tooth 0.7 / 0.05 | Red/Blue: "its large venomous stingers on its forelegs and tail." X: "three poisonous stingers on its forelegs and its tail." Art: broad streaked light bands along each cone: the shiniest part of the design. Base is the lilac-gray the cones are mostly painted in. | high |
| Tail stinger (the yellow point of the abdomen: last 6 rows front, last 4 back) | hard needle, yellow | Claw and tooth, own row "tail stinger" on the yellow ramp | Silver/SoulSilver: "The barb on its tail secretes the most powerful poison." FireRed/Y: "the toxic stinger on its rear." Art: a yellow-orange cone with a pale streak down it, set off from the abdomen by a line. The sprite draws no line there; the cone starts where the abdomen steps in. | medium |
| Wings (white, lilac veins) | thin insect wing | Insect wing, finish 0.4, **body 0.3** (starting value 0.6) | No entry describes the wings. Art: flat white with a faint gray wash and thin veins, opaque (the arm's shadow falls on one); HOME: see-through gray. At 0.6 the wings sparkled with yellow specks and stayed salmon-bright in the cave, and their contour washed out against the field's sky. At 0.3 they are as bright next to the body in the cave as the art paints them (measured), keep their contour, and still light up pink with the sun behind. Finish cannot be read from the art (a highlight on white does not show): kept at the starting 0.4. | body: medium; finish: low |
| Wing veins and inner fold lines | lines inside one flat sheet | Seams and wrinkles | They do not separate overlapping pieces, so the wing stays one smooth sheet; the lilac contour of each wing is the wing's own darkest shade. | medium |
| Eyes (red, front view only) | eye | Eye (line art) | Art: red eyes with a white catchlight. The eyes-closed look is drawn the same as open in this sprite. | high |

### Pidgey (#016)


No entry in any game describes its plumage, beak or legs (Black 2/White 2: "It is docile and prefers to avoid conflict. If disturbed, however, it can ferociously strike back."), so every surface is set from the art.

| Surface | Made of | Material | Evidence | Confidence |
|---|---|---|---|---|
| Brown back, wings, crest, tail | body plumage | Feathers | Art: flat brown, soft shading, no light patch; HOME the same. | high |
| Cream chest, belly, cheek, brow tufts, wing tips | plumage, paler | Feathers (own row) | Art: flat cream; the paler chest streaks are drawn feather texture. The sprite's light brown streaks in the cream are the cream's own shade. | high |
| Mask through the eye | pigment in the plumage | Feathers (own row) | Art: black patch behind the eye. Sprite paints it dark brown in front, black behind; both in one row. | high |
| Beak | horn | Beak (0.4 / 0.05) | Art: pink with a lighter top; the sprite paints a highlight. The line between its halves is line. | medium |
| Legs and toes | bare, scaly bird skin | Dry hide | Art: flat pink, soft shading, no highlight; HOME flat. | medium |
| Claws | keratin | Claw and tooth | Art: white with a gray shade. | medium |
| Eye | eye | Eye (line art) | White and pupil in one row. | high |
| Lines between wing and tail feathers | lines | Outline | Overlapping feather layers. | high |

### Pidgeotto (#017)


Entries speak only of claws and beak; nothing describes the plumage.

| Surface | Made of | Material | Evidence | Confidence |
|---|---|---|---|---|
| Brown back, upper wings, head, wing leading edge | body plumage | Feathers | Art: flat brown, no highlights; HOME flat. | high |
| Cream belly, cheek, thighs, underwings, flight feathers | plumage, paler | Feathers (own row) | Art: flat cream with drawn feather lines. Thin light brown strokes inside the cream are its shade. | high |
| Red crest | head plumage | Feathers (own row) | Art: flat red-pink with drawn strands; no entry calls it glossy. | high |
| Red tail feathers (the cream ones are the cream row) | plumage | Feathers (own row) | Art: flat red and yellow feathers. | high |
| Black mask | pigment in the plumage | Feathers (own row) | Art: black marking around the eye. Second shade is the palette's darkest brown. | medium |
| Beak | horn | Beak (0.4 / 0.05) | Red/Blue: "this POKéMON will fiercely peck at any intruder." Art: pink, lighter top. The open beak's black gap stays line. | medium |
| Legs and toes | bare bird skin | Dry hide | Art: flat pink, scutes drawn as lines. | medium |
| Talons | keratin | Claw and tooth | Black 2/White 2: "downing it with its highly developed claws." FireRed: "The claws on its feet are well developed." | high |
| Eye | eye | Eye (line art) | White, gray, pupil and iris pixel in one row. | high |
| Lines between feathers | lines | Outline | Overlapping feather layers. | high |

### Pidgeot (#018)


| Surface | Made of | Material | Evidence | Confidence |
|---|---|---|---|---|
| Brown back and wings | glossy plumage | Glossy feathers | Ruby/Sapphire: "This POKéMON has a dazzling plumage of beautifully glossy feathers." Emerald: "This POKéMON has gorgeous, glossy feathers." Art paints no highlight; the entry is the source. | medium |
| Cream chest, belly, cheek, flight feathers | glossy plumage, paler | Glossy feathers (own row) | Same entries ("plumage" is the whole coat). Art: flat cream. | medium-low |
| Head feathers, yellow stripe | glossy plumage | Glossy feathers (own row) | Ruby/Sapphire: "Many TRAINERS are captivated by the striking beauty of the feathers on its head". | medium |
| Head feathers, red stripe; tail | glossy plumage | Glossy feathers (one row: the same red) | Same entries. Art: smooth red streamers, flat red tail. | medium |
| Black mask | pigment in the plumage | Glossy feathers (own row) | Art: black marking past the eye. Its lower edge is drawn in the darkest brown, the row's second shade. | medium |
| Beak | horn | Beak (0.4 / 0.05) | Art: pink, lighter upper side. | medium |
| Legs and toes | bare bird skin | Dry hide | Art: flat pink. | medium |
| Talons | keratin | Claw and tooth | Yellow: "Its large talons are feared as wicked weapons." | high |
| Eye | eye | Eye (line art) | White, gray, pupil in one row. | high |
| Lines between coverts, flight and tail feathers | lines | Outline | Overlapping feather layers. | high |

### Rattata (#019)


Drawn surfaces: purple coat (head, back, legs, tail), cream muzzle, lower jaw, belly and paws, yellow ear insides, cream whiskers, two white incisors, red tongue in a black mouth, red eye, and (back view only) pink pads on the raised hind feet. The female look shortens the whiskers and changes the tail tip in the back view.

| Surface | Made of | Material | Evidence | Confidence |
|---|---|---|---|---|
| Coat (purple): head, back, legs, tail | a rat's short, sleek coat | Short fur (-0.2 / 0.05) | No Pokédex entry describes the coat. Art: flat, soft shading over all the purple, no light patch or highlight, a smooth silhouette with no tufts. The tail is the same purple painted the same way, so it is coat, not bare skin. | medium |
| Muzzle, lower jaw, belly, paws (cream) | the same coat, paler | Short fur, own row | Art: flat cream, no highlight. Neither the art nor the sprite draws separate claws. | medium |
| Ear insides (yellow) | the thin fur inside the ear | Short fur, own row | Art paints them the same flat cream as the belly; the sprite gives them their own yellow. | medium-low |
| Whiskers | one stiff hair each | Whiskers (0.1 / 0.05), new row | Art: flat cream strokes, no highlight. A single hair is smooth, so not fuzzy like a coat; matte because painted flat. | medium-low |
| Incisors | enamel | Claw and tooth (0.7 / 0.05) | Black 2/White 2: "It gnaws on hard objects to wear down its fangs, which grow constantly during its lifetime." FireRed: "Its fangs are long and very sharp." Art: white with a pale gray shade. | high |
| Tongue | wet tissue | Mouth (0.8 / 0) | Shared rule. The rest of the open mouth is drawn black, so it is line. | high |
| Eye | eye | Eye (line art) | Red iris, white and gray in one row; the dark lid lines are the coat's own dark shade. | high |
| Hind-foot pads (pink, back view, 5 pixels) | bare skin | Hide (0.25 / 0.08), own row | Not in the art or any entry. The back sprite draws pink on the two raised hind feet. | low |

Other decisions:
- The coat's base is the darker purple (color 6): the back view is painted almost wholly in it (399 pixels, against 204 of the lighter one in front).
- The dark line of the tail's curl is a crease, since the tail lies over itself.
- The teeth's dark gray edge is the tooth's darkest shade, not line.

### Raticate (#020)


Drawn surfaces: tawny coat (head, crest, back, arms, backs of the ears), cream muzzle, chin, chest ruff and belly, pale whiskers, bare tan tail, hands and feet, dark ear insides, large white incisors in a black mouth, white eye with a black pupil. The female look shortens the whiskers.

| Surface | Made of | Material | Evidence | Confidence |
|---|---|---|---|---|
| Coat (tawny) | a rat's short coat, coarser, with tufts at the crest, cheeks and chest | Short fur (-0.2 / 0.05) | No Pokédex entry describes the coat. Art: flat, smooth shading with no highlight; the fur is ragged only along edges. Fur (-0.7) was tried: the whole body went grainy and got a bright rim in the cave, which the art does not show. | medium |
| Muzzle, chin, chest ruff, belly (cream) | the same coat, paler | Short fur, own row | Art: flat cream. The chest ruff is a separate drawing hanging over the belly; the lines of its points are creases. | medium |
| Tufts drawn on the back (back view) | clumps of the same coat | Short fur; their dark lines are creases | The back sprite draws zigzag tuft lines inside the coat. | medium |
| Whiskers | one stiff hair each | Whiskers (0.1 / 0.05), new row | Red/Blue: "It uses its whiskers to maintain its balance. It apparently slows down if they are cut off." Art: flat pale strokes, no highlight. | medium |
| Tail, hands, feet (tan) | bare skin: a ringed rat tail, webbed hind feet | Hide (0.25 / 0.08) | Yellow: "Its hind feet are webbed. They act as flippers, so it can swim in rivers and hunt for prey." FireRed: "Its rear feet have three toes each. They are webbed, enabling it to swim across rivers." Art: bare tan skin, ring lines on the tail, flat shading, no highlight. Claws are the color of the toes and not drawn apart in the sprite, so they stay skin. | medium |
| Ear insides (dark brown) | bare skin, in shadow | Hide, own row | Art: dull brown skin inside the ear; HOME: the tail's skin color. The sprite paints them in one color, the skin's darkest. | medium |
| Incisors | enamel | Claw and tooth (0.7 / 0.05) | Black 2/White 2: "With its long fangs, this surprisingly violent Pokémon can gnaw away even thick concrete with ease." Ruby: "RATICATE's sturdy fangs grow steadily." Art: white with soft gray shading. | high |
| Mouth interior | (drawn black) | Outline | The art paints a pink mouth, but the sprite draws it solid black with no tongue. | high (for this sprite) |
| Eye | eye | Eye (line art) | White (gray-shaded from behind) and the black pupil in one row. | high |

Other decisions:
- The coat's base is the darker tawny (color 11): the back view and the front's flank are painted in it.
- The cream's base is its second-lightest (color 6); the face is painted one step lighter.

### Spearow (#021)


| Surface | Made of | Material | Evidence | Confidence |
|---|---|---|---|---|
| Head, chest ruff, tail (brown) | plumage | Feathers | Bulbapedia: "It has rough, brown plumage on its head and three brown tail feathers." Art: flat brown, soft shading, no highlight. | high |
| Back and back of the head (black, back view) | plumage | Feathers (own row: black plus the dark gray the sprite highlights it with) | Bulbapedia: "Black feathers cover its back." The sprite paints it flat black with five dark gray highlight pixels. One-pixel black strokes stay outline. | high (what it is), medium (shaded rather than line art) |
| Wings (red) | plumage | Feathers | Black 2/White 2: "It flaps its small wings busily to fly." Bulbapedia: "The feathers covering its wings are pinkish-red with lighter tips". Art: a broad soft pale area, no hard highlight. | high |
| Wing tips (pale pink) | pigment in the same feathers | Feathers (own row) | Bulbapedia: "with lighter tips". The red lines between the three big feathers are creases (outline). | high |
| Belly, thighs (gray-tan) | plumage | Feathers (own row) | Bulbapedia: "a beige underside". Art: flat cream. | high |
| Belly stripes | pigment | Feathers (own row) | Bulbapedia: "two thin, horizontal stripes". Painted in black and dark gray-brown. | high |
| Beak (pink) | horn | Beak (0.4 / 0.05) | Gold: "It then plucks them with its stubby beak." Black 2/White 2: "Using its beak, it searches in grass for prey." Bulbapedia: "a short, hooked beak that is light pink". Art paints a pale highlight patch on top. | high |
| Red inside the open beak | mouth | Mouth (0.8 / 0) | Art and HOME show the beak open with the tongue. On the sprite it is six red pixels behind the hook; it could be the lower beak in shade. | medium |
| Feet (pink-red) | bare, scaly bird skin | Dry hide | Bulbapedia: "Its light pink feet have two toes in front and one in the back." Art: flat pink, no highlight. | medium |
| Claws (white) | keratin | Claw and tooth | Art and HOME: white claws. The sprite shades them with the belly's gray-browns. | high |
| Eyes | eye | Eye (line art) | Bulbapedia: "narrow, dark brown eyes with white pupils". Both eyes, and the lid line of the closed look. | high |

### Fearow (#022)


| Surface | Made of | Material | Evidence | Confidence |
|---|---|---|---|---|
| Body, neck, head, tail, wings (brown) | plumage | Feathers | Black 2/White 2: "It has the stamina to fly all day on its broad wings." Red/Blue: "With its huge and magnificent wings, it can keep aloft without ever having to land for rest." Bulbapedia: "a large, mostly brown avian Pokémon". Art: flat soft browns, no highlight on the wings. Lines between flight feathers are creases. | high |
| Flight feather tips (cream) | pigment in the same feathers | Feathers (own row) | Bulbapedia: "These feathers are cream-colored, as are the tips of its flight feathers." The back view paints them a step darker, so which colors are tips is set per drawing. | high |
| Ruff at the base of the neck (cream) | shaggy plumage | Feathers (own row) | Bulbapedia: "It has shaggy feathers at the base of its neck and covering the upper portion of its wings." Art: flat cream tufts. Lines between tufts are creases. | high |
| Comb (red) | bare skin | Comb (new: 0.1 / 0.08) | Bulbapedia: "a decorative red coxcomb on top of its head". No Pokédex entry mentions it. Art: flat red spikes, no highlight. | low |
| Beak (pink) | horn | Beak (0.4 / 0.05) | Black 2/White 2: "It fights by using its sharp beak." Silver: "It cleverly uses its thin, long beak to pluck and eat small insects that hide under the ground." Bulbapedia: "a long, pointed, pink beak". Art: pale pink, lighter along the top. | high |
| Feet (pink) | bare, scaly bird skin | Dry hide | Bulbapedia: "Its sharp-clawed talons are pink". Art: flat pink. | medium |
| Claws (white) | keratin | Claw and tooth | Bulbapedia: "sharp-clawed". White with a cream shade on the sprite. | high |
| Eyes | eye | Eye (line art) | Bulbapedia: "Its narrow eyes have very small pupils and do not appear to have colored irises." Both views, and the closed look's lid line. | high |

### Ekans (#023)


Drawn surfaces: purple body, yellow neck band, yellow underside, rings drawn across the body, rattle, open mouth with tongue, yellow eyes with slit pupils.

| Surface | Made of | Material | Evidence | Confidence |
|---|---|---|---|---|
| Body (purple) | smooth scaled snake skin | Snake scales (0.15 / 0.05) | No entry describes the skin. Black 2/White 2: "It sneaks through grass without making a sound and strikes unsuspecting prey from behind." Yellow: "At night, it wraps its long body around tree branches to rest." Painted art: pale streaks of light on the head, the neck, every coil and the tail, so a soft sheen. | medium |
| Neck band and underside (yellow) | the same scales in another color | Snake scales, own row (0.15 / 0.05) | No entry mentions them. Painted art: the band carries the same pale streak as the purple above it, so it keeps the scales' sheen; the stripe under the coils is thin and in shade. One row for both: the band runs into the underside in the same yellow, and the underside painted darker then reads as facing down. | medium |
| Rings across the body | lines drawn on one smooth tube | kept as the scales' darkest shade | Painted art: the light streaks run straight across the rings, so they are not creases between bulging segments. | medium |
| Rattle | hard, dry beads | Rattle (0.2 / 0.05), a new surface | No entry mentions the rattle. Painted art: every bead is softly shaded with no highlight, so dull; hard, so almost solid (the trace of body claws have). | low for the dials |
| Mouth and tongue | wet tissue | Mouth (0.8 / 0) | FireRed: "It flicks its tongue in and out to sense danger in its surroundings." Gold: "It can freely detach its jaw to swallow large prey whole." Painted art: pink mouth, a soft highlight on the tongue. | high |
| Eyes | eye | Eye (line art) | Ruby/Sapphire: "a glare from its upraised head". Yellow with a black slit and a painted catchlight; no entry says they glow. | high |

### Arbok (#024)


Drawn surfaces: purple body and hood, the face pattern on the hood (black, red, yellow), lines across the belly and coils, open mouth with tongue, fangs, small white eyes. The back of the hood is plain purple.

| Surface | Made of | Material | Evidence | Confidence |
|---|---|---|---|---|
| Body and hood (purple) | smooth scaled snake skin; the hood is its chest spread wide, not a thin membrane | Snake scales (0.15 / 0.05) | Crystal: "To intimidate foes, it spreads its chest wide and makes eerie sounds by expelling air from its mouth." Ruby/Sapphire: "This POKéMON is terrifically strong in order to constrict things with its body." Painted art: light patches on the head and the hood's rim, a sharp streak down the belly, so a soft sheen. | medium |
| Hood pattern (black, red, yellow) | pigment in the same scales | Snake scales, three own rows (black, red, yellow), the scales' dials | Black 2/White 2: "The pattern on its belly is for intimidation. It constricts foes while they are frozen in fear." Yellow: "The frightening patterns on its belly have been studied. Six variations have been confirmed." Gold: "Transfixing prey with the face-like pattern on its belly". Painted art: flat color, no relief. The black is a row with no shades (tinted by light, never a crease), so the hood stays one smooth dome. | high |
| Lines across the belly and coils | lines drawn on one smooth tube | kept as the scales' darkest shade | Painted art: the belly's light streak runs across the lines. | medium |
| Mouth and tongue | wet tissue | Mouth (0.8 / 0) | Crystal: "expelling air from its mouth". Painted art: pink mouth, long forked tongue. | high |
| Fangs | tooth | Claw and tooth (0.7 / 0.05) | Gold: "it binds and poisons the frightened victim." Painted art: white teeth. | medium |
| Eyes | eye | Eye (line art) | White with a black pupil and brow, a few pixels. No entry says they glow. | high |

### Pikachu (#025)


| Surface | Made of | Material | Evidence | Confidence |
|---|---|---|---|---|
| Yellow coat (head, body, arms, feet, ears, tail) | short, sleek fur | Short fur | No entry describes the coat. Art: flat yellow with broad soft light patches, no highlight; HOME: smooth. Brown contour colors are the row's darkest shades. Base is the mid yellow (656 visible pixels against 580, both views). | medium |
| Ear tips (black) | the same fur, black | Short fur (row "short fur, ear tips") | Art: solid black, no highlight. | high |
| Cheeks (red) | fur over the electric sacs | Short fur (row "short fur, cheeks") | FireRed/Y: "It has small electric sacs on both its cheeks." Sword: "Pikachu that can generate powerful electricity have cheek sacs that are extra soft and super stretchy." Art: flat red discs. No glow at rest. | high |
| Two back stripes, tail base (brown) | the same fur, brown | Short fur (row "short fur, stripes and tail base") | Art and HOME: brown stripes and a brown patch where the tail meets the body, flat. | high |
| Mouth inside, tongue | wet tissue | Mouth (0.8 / 0) | Shared rule. The brown mouth line and the one-pixel nose are drawn line. | high |
| Eyes | eye | Eye (line art) | Black, white catchlight, gray reflections and the closed lids, all in one row. | high |

### Raichu (#026)


| Surface | Made of | Material | Evidence | Confidence |
|---|---|---|---|---|
| Orange coat (head, body, arms, legs) | short, sleek fur | Short fur | No entry describes the coat. Art: soft flat orange, no highlight; HOME: smooth. Base is the darker orange (704 visible pixels against 423, both views). | medium |
| Belly (cream), and its edge seen from behind | the same fur, pale | Short fur (row "short fur, belly") | Art and HOME: a white-cream patch, matte. | high |
| Cheeks (yellow) | fur over the electric sacs | Short fur (row "short fur, cheeks") | Silver: "If the electric pouches in its cheeks become fully charged, both ears will stand straight up." Art: flat yellow discs. No glow at rest. | high |
| Lightning-bolt tail tip, ear insides (yellow) | the same fur, yellow | Short fur (row "short fur, tail and ear insides") | Black 2/White 2: "Its tail discharges electricity into the ground, protecting it from getting shocked." Art: flat yellow, no highlight. The bolt's olive and brown contours are its shades. | medium |
| Ear backs and rims, paws, feet (brown) | the same fur, brown | Short fur (row "short fur, paws and ears") | Art and HOME: brown, matte. | high |
| Two back stripes (brown) | pigment in the coat | Short fur (row "short fur, stripes") | Art: two brown stripes across the back; they run on over the left leg in the back view. | high |
| Soles (tan, back view) | paw underside | Short fur (row "short fur, soles") | Art: pale tan, flat, no highlight; no text. Painted in one color, with the belly's cream as its lighter step. Lines between the toes are creases (outline). | low |
| Orange spot on each sole | pigment | Short fur (row "short fur, sole spots") | Art and HOME: an orange oval on the sole. | medium |
| Tail cord (thin, dark gray) | long thin tail | Short fur (row "short fur, tail cord") | Red/Blue: "Its long tail serves as a ground to protect itself from its own high voltage power." Art: an even dark gray line, no highlight; nothing says it is bare skin. | low |
| Mouth inside | wet tissue | Mouth (0.8 / 0) | Shared rule. One red, with the dark line around it as its second shade. Mouth line and nose are drawn line. | high |
| Eyes | eye | Eye (line art) | Black with a cream catchlight; one edge pixel beside the left eye is kept with it. | high |

### Sandshrew (#027)


Drawn surfaces: yellow brick-patterned hide, cream stomach and muzzle, pale ear insides (front view), white claws, dark blue eyes. No open mouth.

| Surface | Made of | Material | Evidence | Confidence |
|---|---|---|---|---|
| Hide (yellow, with its brick lines and brown contour) | dry, tough, brick-like skin | Plated hide (0.2 / 0.03) | Sapphire: "SANDSHREW has a very dry hide that is extremely tough." Yellow: "Its body is dry. When it gets cold at night, its hide is said to become coated with a fine dew." Emerald: "Its hide has turned tough and solid as a result of living in the desert." Art: flat sandy yellow with soft shading and no highlight anywhere. The brick lines are drawn in the hide's darker yellow and stay its shades (grooves of one surface). | high |
| Stomach and muzzle (cream) | the same dry skin, soft, not plated | `dry hide, belly` (0.05 / 0.08) | Ultra Sun: "When danger approaches, it curls up into a ball to protect its soft stomach." Yellow: "Its body is dry." Art: flat cream, soft shading, no highlight. Matte like the hide; a trace more light through because it is soft skin, not plate. Not the standard Belly (0.4 / 0.25): nothing shows a sheen, and the body is dry. | medium |
| Ear insides (cream, front view) | skin | `dry hide, ear insides` (0.05 / 0.03) | Art and HOME: pale, flat. Own row: the left one is painted in shadow (tan), the right one lit (cream). | medium |
| Claws (white; cream, tan and gray in shade) | keratin | Claw and tooth (0.7 / 0.05) | Shield: "If hard stones impede its tunneling, it uses its sharp claws to shatter them and then carries on digging." Art: white with a gray shadow side. | high |
| Eyes (dark blue, white catchlight) | eye | `eye (line art)` | Art: black-blue with a white catchlight. Closed, the lid is hide with a darker line. | high |

Nothing glows.

### Sandslash (#028)


Drawn surfaces: yellow hide, brown quills (back, head crest), cream stomach, muzzle and cheek, long white claws, eyes. No open mouth.

| Surface | Made of | Material | Evidence | Confidence |
|---|---|---|---|---|
| Quills (brown) | hardened hide | Spines (0.4 / 0) | Black 2/White 2: "The spikes on its body are made up of its hardened hide. It rolls up and attacks foes with its spikes." Ruby: "SANDSLASH's body is covered by tough spikes, which are hardened sections of its hide." Sword: "The drier the area Sandslash lives in, the harder and smoother the Pokémon's spikes will feel when touched." Art: each quill has a lighter upper face and a darker underside, no white highlight: a soft sheen at most, which the starting value gives. The dark lines between quills are creases (outline). | medium |
| Hide (yellow) | dry, tough skin | Plated hide (0.2 / 0.03) | No entry describes Sandslash's own skin; it is Sandshrew's hide (quotes above), and the spikes are "hardened sections of its hide" (Ruby). Art: flat yellow, soft shading, no highlight. The palette's lightest yellow is never drawn and is the ramp's top step. | medium |
| Stomach, muzzle, cheek (cream; white along the jaw) | the same dry skin, soft | `dry hide, belly` (0.05 / 0.08) | Same reasoning as Sandshrew ("its soft stomach", Ultra Sun, is Sandshrew's entry). Art: flat cream, no highlight. | medium |
| Claws (white; cream and gray in shade) | keratin | Claw and tooth (0.7 / 0.05) | Yellow: "It is skilled at slashing enemies with its claws. If broken, they start to grow back in a day." Ultra Moon: "Thanks to its thick claws, it's good at climbing trees." Art: white with gray-blue shading. | high |
| Eyes | eye | `eye (line art)` | Art: black with a white catchlight. On the sprite the eye is black line with white, gray and one cream pixel. | high |

Nothing glows.

### Nidoran♀ (#029)


Drawn surfaces: pale lilac body, dark spots, big ears (dark ring and teal center inside), forehead horn, barbs on the back, whiskers, two incisors, open mouth (first two head drawings), white claws, red eyes.

| Surface | Made of | Material | Evidence | Confidence |
|---|---|---|---|---|
| Body, head, legs, ear backs and rims | bare skin, no coat | Hide (0.25 / 0.08) | No entry in any game mentions fur. The painted art shades the whole body with flat soft washes and no highlight anywhere; HOME is smooth and evenly soft. | medium |
| Dark spots | pigment in the same skin | Hide, own row `hide, spots` | Art and HOME: darker blue-violet patches on the flank and back, flat. | high |
| Ear inside, dark ring | pigment in the same skin | Hide, own row `hide, ear ring` | Art and HOME both paint two flat zones inside the ear: a dark violet ring and a teal center. No highlight. | medium |
| Ear inside, teal center | pigment in the same skin | Hide, own row `hide, ear center` | Same. | medium |
| Forehead horn | hardened spike that is part of the hide | Spines (0.4 / 0) | Yellow: "Beware, its small horns secrete venom." HeartGold: "The poison hidden in its small horn is extremely potent." Shield: "The tip of a female Nidoran’s horn is a bit more rounded than the tip of a male’s horn." The art paints it the body's own lilac, flat, so it is a hide-colored spike, not bare white horn. | medium |
| Back barbs | hardened spikes that are part of the hide | Spines (0.4 / 0) | Black 2/White 2: "While it does not prefer to fight, even one drop of the poison it secretes from barbs can be fatal." Red/Blue: "Although small, its venomous barbs render this POKéMON dangerous." Art: body-colored, flat. | medium |
| Whiskers (the pale strands free of the head; all of the back view's whisker drawings) | stiff hair | Whiskers (0.1 / 0.05), a new row | Sword: "While foraging, they’ll use their whiskers to check wind direction and stay downwind of predators." Art: pale strands in the body's color, flat. | that they are whiskers: high; the dials: low |
| Whiskers where they lie over the cheek | drawn strokes | Outline | The sprite draws them there as one-pixel black and dark strokes (in two head drawings they fade to lighter strokes while twitching). | high |
| Incisors | enamel | Claw and tooth (0.7 / 0.05) | Shield: "It uses its hard incisor teeth to crush and eat berries." White in art and sprite. | high |
| Claws | keratin | Claw and tooth (0.7 / 0.05) | White in art, HOME and sprite. No entry describes them. | medium |
| Mouth inside | wet tissue | Mouth (0.8 / 0) | Shared rule. | high |
| Eyes | eye | Eye (line art) | Red iris with white on both sides; the shut eye's line is outline. | high |

Nothing glows. Base shade: counted on what shows in both views together the darker lilac wins (519 to 328 pixels), so that is the hide's base.

### Nidorina (#030)


Drawn surfaces: light blue body, pale belly (front view only), dark patches, big ears (dark blue ring and bright blue center inside), barbs on the back (two in the front view, a cluster of five from behind), tail, white claws, one fang, mouth, red eyes. No horn is drawn (Sword: "The horn on its head has atrophied.").

| Surface | Made of | Material | Evidence | Confidence |
|---|---|---|---|---|
| Body, head, limbs, tail, ear backs and rims | bare skin, no coat | Hide (0.25 / 0.08) | No entry mentions fur or scales. Art: flat washes with soft lighter areas on thigh and arm, no hard highlight; HOME smooth and soft. | medium |
| Belly (front view) | the same skin, paler | Hide, own row `hide, belly` | Art and HOME: a paler underside from chest to belly, flat. From behind, the sprite's pale strip along the chest is a rim of light like the one along the head, so it stays in the hide row. | medium |
| Dark patches | pigment | Hide, own row `hide, spots` | Art and HOME: dark blue patches on flank and haunch, flat. | high |
| Ear inside, dark ring | pigment in the same skin | Hide, own row `hide, ear ring` | HOME: two flat zones, dark blue around a lighter blue panel. Art: dark blue with lighter blue streaks. | medium |
| Ear inside, bright center | pigment in the same skin | Hide, own row `hide, ear center` | Same. | medium |
| Back barbs | hardened spikes that are part of the hide | Spines (0.4 / 0) | Black 2/White 2: "When it senses danger, it raises all the barbs on its body. These barbs grow slower than Nidorino’s." Crystal: "If it is threatened with attack, it raises the barbs that are all over its body." Ruby/Sapphire: "they keep their barbs tucked away to prevent hurting each other." Art: body-colored, flat. | medium |
| Lines between barbs, and where a barb meets the back | drawn lines between overlapping pieces | Outline | Creases, so each barb is rounded on its own. With the lines shaded as surface the cluster merged into one lump under a lamp. | medium |
| Claws | keratin | Claw and tooth (0.7 / 0.05) | Red/Blue: "Prefers physical attacks such as clawing and biting." White in art and sprite. | high |
| Fang | enamel | Claw and tooth | Same entry ("biting"); one white fang in art and sprite. | high |
| Mouth inside | wet tissue | Mouth (0.8 / 0) | Shared rule. | high |
| Eyes | eye | Eye (line art) | Drawn only in the eye drawings; the same red on the head drawings is the mouth. | high |

Nothing glows. The palette's palest blue (color 10) is never drawn; it is the hide's own next lighter step and is added at the top of the hide's shades.

---

## Part 1, continued: #031 to #151

The rest of Gen 1 was made the same way on 2026-11-27 and 28, one evolution line at a time, after the owner approved the approach on two sets picked for their materials. Each line's table (surface, what it is made of, material, the Pokédex text and what the painted art shows, confidence) is kept as written in `docs/evidence/gen1/`, one file per line. Every sprite passed `tools/light.py check` and was looked at lit, front and back, in the field, under a lamp and in the cave before it was filed.

What that pass taught:

- **Fur at -0.7 is for tufts.** On a mane or a whole coat it turns grainy and muddy; -0.1 keeps it soft. Gengar's body had the same fault at -0.5.
- **A pale surface whose only darker colors are its contour.** White bone, a cream coat or a white fin with an olive or brown contour and no step between: with the contour as its darkest shade the whole surface went olive or speckled dark in daylight (Cubone's skull, Mankey, Chansey, Gyarados's belly). There the contour goes in the outline row.
- **Base is not always the most-used shade.** When the front is painted light and the back dark (Electabuzz, Jigglypuff, Dewgong, Voltorb), the most-used shade as base made the front dull or olive; the shade between the two views is right.
- **Glow only where an entry says so at rest:** Persian's jewel, Kabuto's eyes, Starmie's core, Electabuzz and Magmar faintly, and fire. Clefairy's moonlit wings, Golduck's gem and Dragonair's orbs do not glow at rest.
- **Metal only where a source says metal:** Kadabra's and Alakazam's spoons, Hypno's ring, Primeape's shackles (from the art). Meowth's coin, Machoke's belt and Kingler's "hard as steel" claw are painted flat and stay dull.

## Part 2: a general guide

Typical values for the kinds of surface Pokémon are made of. Quotes are game text and name the game.

| Surface | Examples | finish | body | glow | Notes |
|---|---|---|---|---|---|
| Fur | Growlithe, Eevee, Wartortle's ears and tail | -1 | 0 | 0 | |
| Flight feathers | Pidgeot ("a dazzling plumage of beautifully glossy feathers", Ruby), Fearow | 0.3 | 0 | 0 | Glossy plumage up to 0.5. |
| Down, cotton | Swablu ("light and fluffy wings that are like cottony clouds", Ruby), Altaria | -1 | 0.15 | 0 | |
| Scales | Gyarados, Dragonair, Milotic ("Its lovely scales are described as rainbow colored", Black 2/White 2) | 0.5 | 0 | 0 | There is no rainbow-sheen dial; paint the rainbow. |
| Smooth skin | Bulbasaur, Squirtle, Charmander | 0.5 | 0.05 | 0 | A soft sheen; letting light through makes it look slick. |
| Wet, slimy skin | Goomy ("covered in a slimy membrane", Y), Shellos ("its squishy body", Black 2/White 2) | 0.7 | 0.15 | 0 | The shine says wet; light through would make it jelly. |
| Shell, carapace | Squirtle line, Shuckle, Cloyster ("harder-than-diamonds shell", Yellow) | 0.6 | 0 | 0 | Pearly or lacquered shells 0.8. |
| Insect exoskeleton | Heracross, Pinsir, Beedrill | 0.6 | 0 | 0 | Beetles up to 0.9. Soft larvae are Skin. |
| Leaves | Leafeon ("With cells similar to those of plants", Black/White), Tropius ("flies by flapping the leaves on its back", Sapphire) | 0 | 0.3 | 0 | |
| Petals | Bellossom, Florges, Venusaur | 0 | 0.25 | 0 | |
| Bark, wood | Trevenant, Torterra's tree, Venusaur's trunk | -0.2 | 0 | 0 | |
| Rock, stone | Geodude ("At rest, it looks just like a rock", Black 2/White 2), Golem, Onix | 0 | 0 | 0 | Porous rock -0.2. |
| Sand, soil | Sandygast ("its sand-mound body", Moon), Palossand, Hippowdon | -0.3 | 0 | 0 | |
| Metal | Aron ("This POKéMON has a body of steel", Ruby), Skarmory ("Its metal body is sturdy, but it does rust rather easily", Moon), Klink, Magnemite | 1 | -1 | 0 | Old bronze (Bronzong) 0.6, -1. |
| Crystal, gem | Carbink ("its glittering, jewel-draped body", Moon), Sableye's gems, Diancie | 1 | 0.8 | 0 | Polished and frosted, so it glitters. |
| Ice | Regice ("The deep-frozen body can't be melted, even by fire", Ruby), Avalugg, Cryogonal | 0.8 | 0.8 | 0 | Snow (Vanillite) -0.5, 0.5. |
| Water | Jellicent ("Its body is mostly seawater", Black 2/White 2), Tentacool ("body is largely composed of water", Ruby) | 1 | 1 | 0 | |
| Jelly, goo, sludge | Goomy, Reuniclus, Grimer ("Made of hardened sludge", Yellow) | 0.8 | 0.7 | 0 | Opaque sludge 0.6, 0.2. |
| Flame | Charmander line, Rapidash, Litwick ("Its flame is usually out, but it starts shining when it absorbs life force", Black 2/White 2) | 0 | 0.5 | 180 to 255 | Brighter core, dimmer tips. Flicker with the glow multiplier. |
| Lava, magma | Slugma ("its magma body would cool and harden", Gold), Magcargo, Magmar ("Its body always burns with an orange glow", Red/Blue) | 0.5 | 0.5 | 120 to 200 | Cooled crust is rock, glow 0 (Magcargo: "The shell on its back is just skin that has cooled and hardened", Gold). |
| Electricity, plasma | Rotom ("Its body is composed of plasma", Diamond), sparks, electric cheeks | 0 | 0.5 | 200 to 255 | |
| Light organs | Lanturn ("The light it emits is so bright that it can illuminate the sea's surface", Gold), Ampharos's tail, Volbeat ("emits light from its tail", Ruby) | 0.5 | 0.5 | 180 to 255 | Glow only the light itself. |
| Gas, smoke, ghost wisps | Gastly ("Almost invisible, this gaseous POKéMON", Red/Blue), Koffing's fumes | -0.5 | 0.75 | 0 | Make it thin with pixel opacity, not clear (clear would bend the background). Koffing's balloon body is solid. |
| Cloth, fabric | Banette ("originally a pitiful plush doll that was thrown away", Ruby), Mimikyu's rag ("an old rag", Moon) | -0.6 | 0 | 0 | Banette's zipper is metal. |
| Porcelain, ceramic | Sinistea and Polteageist ("This species lives in antique teapots", Sword) | 0.9 | 0.1 | 0 | Unglazed clay (Golett: "Ancient science fashioned this Pokémon from clay", Black 2/White 2; Baltoy) is 0, 0. |
| Bone | Cubone's skull ("It wears the skull of its dead mother on its head", FireRed), Marowak | 0.2 | 0.1 | 0 | |
| Eyes | all | 1 | 0 | 0 | Glow only when stated (Sableye: "their eyes burn with a sinister glow in the darkness", Ruby). |
| Mouth interior | all | 0.8 | 0.2 | 0 | |
| Claws, horns, beaks; teeth | most | 0.7 | 0.05 | 0 | |

**Judgment calls**

- **Type is not material.** Steel types are rarely metal all over: Mawile's metal is only its jaw ("Its giant jaws are actually steel horns that transformed", Emerald); Lucario is fur with metal-colored spikes. Skarmory and Aron really are metal throughout. Scizor is a hard insect shell ("a body with the hardness of steel", Ruby): satin to polished, body 0, not metal. The reverse happens too: Sudowoodo looks like wood but "its composition appears to be closer to a rock than a plant" (Gold).
- **"Made of water" does not mean see-through.** Vaporeon "will melt away and become invisible in water" (Yellow) but is drawn as opaque skin: give it wet skin (0.6, 0.5), not clear.
- **Only light sources glow.** Fire, lava, plasma, light organs, and eyes a Pokédex says glow. Warning colors (Caterpie's antenna), gems, ghosts and Fire types' bodies do not, unless the text says so.
- **Commit to what reads.** Fur clearly fuzzy and metal fully metal, so they read at sprite size. Skin gets a soft sheen but no light through; light-through is for what really is thin.
- **Markings are not materials.** Spots, stripes and rings use the dials of the surface they are on, in their own row.
- **When the sources are silent, use the real animal.** Frogs, turtles, lizards and caterpillars are the stated origins of the ten above; mark such calls as low or medium confidence.

---

## Sources

Pokédex text (all games) and dex numbers:
- PokeAPI species data: https://pokeapi.co/api/v2/pokemon-species/1/ through /10/ (and the Part 2 examples by number)
- Serebii Black/White Pokédex, used to cross-check: https://www.serebii.net/pokedex-bw/001.shtml, https://www.serebii.net/pokedex-bw/004.shtml, https://www.serebii.net/pokedex-bw/006.shtml, https://www.serebii.net/pokedex-bw/009.shtml, https://www.serebii.net/pokedex-bw/010.shtml
- Official Pokédex (shows the current Scarlet/Violet entries), e.g. https://www.pokemon.com/us/pokedex/charmander

Bulbapedia (Biology, Origin, Trivia), read through Internet Archive snapshots:
- Bulbasaur: https://bulbapedia.bulbagarden.net/wiki/Bulbasaur_%28Pok%C3%A9mon%29#Biology (snapshot https://web.archive.org/web/20251231194338/https://bulbapedia.bulbagarden.net/wiki/Bulbasaur_%28Pok%C3%A9mon%29)
- Ivysaur: https://bulbapedia.bulbagarden.net/wiki/Ivysaur_%28Pok%C3%A9mon%29#Biology (snapshot 20251230012741)
- Venusaur: https://bulbapedia.bulbagarden.net/wiki/Venusaur_%28Pok%C3%A9mon%29#Biology (snapshot 20251231203932)
- Charmander: https://bulbapedia.bulbagarden.net/wiki/Charmander_%28Pok%C3%A9mon%29#Biology (snapshot 20260101085826)
- Charmeleon: https://bulbapedia.bulbagarden.net/wiki/Charmeleon_%28Pok%C3%A9mon%29#Biology (snapshot 20260101235549)
- Charizard: https://bulbapedia.bulbagarden.net/wiki/Charizard_%28Pok%C3%A9mon%29#Biology (snapshot 20260101072037)
- Squirtle: https://bulbapedia.bulbagarden.net/wiki/Squirtle_%28Pok%C3%A9mon%29#Biology (snapshot 20260102101131)
- Wartortle: https://bulbapedia.bulbagarden.net/wiki/Wartortle_%28Pok%C3%A9mon%29#Biology (snapshot 20260101071909)
- Blastoise: https://bulbapedia.bulbagarden.net/wiki/Blastoise_%28Pok%C3%A9mon%29#Biology (snapshot 20251231214449)
- Caterpie: https://bulbapedia.bulbagarden.net/wiki/Caterpie_%28Pok%C3%A9mon%29#Biology (snapshot 20251230145926)

Art and models:
- Official artwork: https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/other/official-artwork/9.png (1 to 10)
- Pokémon HOME 3D renders: https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/other/home/9.png (1 to 10)
- Gigantamax Blastoise, official Sword/Shield site (no material named for the cannons): https://swordshield.pokemon.com/en-ca/expansionpass/pokemon/gigantamax-blastoise
- Wikipedia, Blastoise (no material named for the cannons): https://en.wikipedia.org/wiki/Blastoise

Sprites: `sources/black2-white2/0001-bulbasaur.spu` through `0010-caterpie.spu`.

Searched and found nothing official for: moist or slimy skin on the Bulbasaur line; light passing through Charizard's wings; the Blastoise cannons being metal.
