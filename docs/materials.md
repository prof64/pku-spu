# What Pokémon are made of

Research for giving each surface of a Gen 5 (Black 2/White 2) battle sprite the right material, using the SPU material model:

- **finish**: -1 fuzzy (fur, felt, down), 0 matte, +1 polished (hard white highlight, mirrors surroundings)
- **body**: -1 metal, 0 solid, 0.5 lets light through (it glows back out at the shadow edge; on skin this looks slick), +1 clear (bends what is behind)
- **glow**: 0 to 255, the surface gives off its own light

Smeargle names the ranges like this: finish below 0.25 is "matte", 0.25 to 0.75 "satin", 0.75 and up "polished"; body below 0.25 is "solid", 0.25 to 0.6 "translucent", 0.6 to 0.9 "frosted", 0.9 and up "clear", -0.75 and below "metal".

## The standard materials

Every surface uses one of these. They are set to match the format demo's lit sprites, which the owner judged the best looking (Charizard above all), then checked by an independent review of the first ten in a studio, a field, a cave and lit from behind: a soft sheen on skin with no light through it, light through only what is thin, and nothing that washes out pale colors or muddies a belly. Spots, stripes and rings use the material of what they sit on, as their own row, so the light reads them as color, not bumps. A new kind of surface gets a new standard material here before it is used.

| Material | finish | body | glow | What you see | For |
|---|---|---|---|---|---|
| Skin | 0.3 | 0.05 | 0 | A soft sheen; no light through | Skin, hide and scales |
| Belly | 0.4 | 0.25 | 0 | A sheen, and a little light through | Pale, fleshy undersides (Charizard's belly) |
| Fur | -0.7 | 0.05 | 0 | Soft, broken edges; a bright rim lit from the side | Fur; lines drawn in fur get their own row with the same values |
| Fluff | -1 | 0.2 | 0 | The same, glowing faintly at the edge | Down, cotton |
| Shell | 0.4 | 0 | 0 | A clear highlight | Turtle shells and their rims |
| Belly plate | 0.4 | 0.2 | 0 | The same, and stays bright in shade | The pale underside of a shell |
| Claw and tooth | 0.7 | 0.05 | 0 | A small bright highlight | Claws, horns, teeth, pads |
| Eye | 0.9 | 0 | 0 | A sharp highlight | Eye whites and catchlights |
| Iris | 0.9 | 0 | 0 | Stays as drawn | Dark irises, pupils and single-pixel catchlights, as a line-art row (its name says "line art"), which light only tints |
| Mouth | 0.8 | 0.2 | 0 | A wet shine | The inside of a mouth |
| Leaf | 0.4 | 0.35 | 0 | Lights up when the light is behind it | Leaves |
| Petal | 0.2 | 0.25 | 0 | Nearly matte; lights up a little from behind | Petals, buds, a seed bulb |
| Bark | -0.45 | 0.05 | 0 | Dry and rough | Trunks, stems |
| Wing membrane | 0.45 | 0.5 | 0 | Bright, and lights up from behind | Thin skin between wing bones |
| Metal | 0.7 | -1 | 0 | Mirrors the room, tinted | Real metal (gold 0.8) |
| Flame | 0 | 0 | 180 to 255 | Glows, lights what is around it, flickers | Fire: brightest at the core |
| Outline | 0.1 | 0 | 0 | | The drawn line |

**Letting light through makes skin look slick.** Body above about 0.3 fills a surface's shadows with a warm glow and washes out its color; skin set that way looks gummy and wet. Keep skin, hide and scales at body 0.05. A strong sheen washes pale skin out in sunlight, so skin's is soft (0.3); Charizard's saturated orange takes 0.5.

**After changing a body value, work out facing again** (`bake_facing`): how far light moves a pixel between shades depends on it, so old facing no longer gives back the art.

**Use the palette's headroom.** If the palette has a color the art never draws that is a lighter step of a surface's shades (Charizard's brighter blue), add it as that material's top shade: the surface can then catch the light past what was painted.

## Setting them in Smeargle

- One material row per surface, set to one of the standard materials above. Charizard keeps the format demo's own rows, which these are taken from.
- Give every material at least two shades. A material with one shade (white claws drawn in a single white, say) does not light back to the art it was drawn as; pair it with the nearest darker palette color.
- Glow goes on the pixels that give off light, strongest at a flame's core. A flame's glow flickers with its drawn flicker through the part's emission track.
- [material-hints.md](material-hints.md) lists, for every Pokémon in the sources, the surfaces that are easy to get wrong.

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
| Eyes | wet eyeball | 0.9 | 0 | 0 | Eyes are wet and hard; at sprite size the hard highlight is what makes an eye read. Dark irises and pupils are an Iris (line-art) row, so light cannot wash them out. None of the ten has an entry or art showing glowing eyes. |
| Mouth interior, tongue | wet tissue | 0.8 | 0.2 | 0 | Wet and fleshy. Usually 10 to 30 pixels, so the exact value matters little. |
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
| Skin (blue-green) | smooth amphibian skin | Skin | Bulbapedia Biology: "a small, quadrupedal amphibian Pokémon that has blue-green skin with darker patches." Official art is flat, matte watercolor; the HOME model is smooth with one soft broad highlight, no wet shine. **No Pokédex entry or Bulbapedia text calls the skin moist, slimy or glossy** (searched), so it is Skin, with no wet shine. | medium |
| Darker spots | pigment | Skin | Bulbapedia: "darker patches". Flat in art and the 3D model. Own material row. | high |
| Bulb | plant bulb grown from a seed: firm, fleshy plant tissue | Petal | Black 2/White 2: "For some time after its birth, it grows by gaining nourishment from the seed on its back." Yellow: "In the bulb on its back, it stores energy." Gold: "The seed on its back is filled with nutrients." Bulbapedia: "a green plant bulb... The bulb also provides it with energy through photosynthesis"; Origin: "The bulb on its back resembles a lily or onion." Onion and lily bulbs are fleshy plant; the HOME model shows it smooth and brighter than the skin. Petal: lets a little light through. | medium |
| Claws | keratin | Claw and tooth | Bulbapedia: "Each of its thick legs ends with three sharp claws." White in art and sprite. | medium |
| Eyes, mouth, tooth | see shared rules | see shared rules | Bulbapedia: "red eyes with white pupils"; "Small, pointed teeth are visible in the upper jaw when the mouth is open." | high |

Notes: nothing on Bulbasaur glows. Bulbapedia mentions the bulb flashing blue before evolving, but that is an anime event, not a battle look.

### Ivysaur (#002)

Drawn surfaces: skin, darker patches, ear insides (dark), pink bud, leaves, claws, eyes, two small fangs. The brown trunk Bulbapedia describes is hidden by the leaves on this sprite.

| Surface | Made of | Material | Evidence | Confidence |
|---|---|---|---|---|
| Skin | smooth amphibian skin | Skin | Bulbapedia: "a quadrupedal amphibian Pokémon that has blue-green skin with darker patches." Same as Bulbasaur. | medium |
| Darker patches, ear insides | pigment | Skin | Bulbapedia: "pointed ears with black insides". Own row. | high |
| Bud (pink) | closed flower bud: thick, fleshy, tightly wrapped petals | Petal | Black 2/White 2: "When the bud on its back starts swelling, a sweet aroma wafts to indicate the flower's coming bloom." Gold: "Sunlight also makes the bud on its back grow larger." Bulbapedia Origin: "The bud on its back resembles a Rafflesia flower." Rafflesia buds are thick and fleshy: Petal, a little light through. | medium |
| Leaves (fronds) | palm-like leaves | Leaf | Bulbapedia: "leafy green fronds"; Origin: "the leaves around the bud resemble palms." Palm leaves are thin: Leaf lets light through when lit from behind. | medium |
| Claws, eyes, fangs | see shared rules | see shared rules | Bulbapedia: "narrow red eyes", "two pointed teeth in its upper jaw", "Each of its feet has three claws". | high |

### Venusaur (#003)

Drawn surfaces: skin (bumpy, with lighter bumps and darker patches), ear insides (red), petals, white petal spots, yellow crown at the flower's center, brown trunk, leaves, white claws, red eyes, teeth. The sprite has a Female look that redraws the yellow center.

| Surface | Made of | Material | Evidence | Confidence |
|---|---|---|---|---|
| Skin | thicker, bumpy amphibian hide | Skin | Bulbapedia: "a squat, quadrupedal amphibian Pokémon with bumpy, blue-green skin." Art shows small bumps along the back and legs. | medium |
| Bumps and darker patches | real bumps plus pigment | Skin | Here the light dots **are** bumps ("bumpy"), so they may stay in the skin row and let the light shape them; the darker patches get their own row. | medium |
| Ear insides | skin | Skin | Bulbapedia: "small, pointed ears with reddish-pink insides." | high |
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
| Skin (orange) | smooth lizard skin | Skin | Bulbapedia: "a bipedal, reptilian Pokémon with a primarily orange body"; Origin: "Charmander was designed as a lizard", also a salamander. No entry mentions scales on Charmander; art and HOME show it smooth with a soft sheen: Skin. | medium |
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
| Skin (dark red) | scaly reptile hide | Skin | Bulbapedia: "It has dark red scales and a cream underside from the chest down." No Pokédex entry describes the skin; art and HOME show no visible scale pattern. With no scale pattern drawn, it is Skin like Charmander's. | medium-low |
| Belly and soles (cream) | the same hide | Belly | Bulbapedia: "cream-colored soles". Own row. | high |
| Head horn | skin-covered horn | Skin | Bulbapedia: "On the back of its head is a single horn-like protrusion." Same color as the skin in art and sprite, so it is skin over horn, not bare keratin. | low |
| Claws | keratin | Claw and tooth | Bulbapedia: "relatively long arms with three sharp claws". Ruby/Sapphire: "CHARMELEON mercilessly destroys its foes using its sharp claws." | medium |
| Tail flame, core | fire | Flame (glow 240) | Black 2/White 2: "In the rocky mountains where Charmeleon live, their fiery tails shine at night like stars." Red/Blue: "When it swings its burning tail, it elevates the temperature to unbearably high levels." | high |
| Tail flame, outer tongues and embers | fire | Flame (glow 200) | Same. The sprite draws loose embers around the flame: give them the core's glow and let them flicker with it. | high |
| Eyes, mouth | see shared rules | see shared rules |  | high |

Note: when excited the flame turns bluish white. Ruby/Sapphire: "In this excited state, the flame at the tip of its tail flares with a bluish white color." Yellow: "When excited, it may blow out bluish-white flames." That would be a look (a palette swap), not a material.

### Charizard (#006)

Drawn surfaces: orange skin, cream belly, underside of tail and soles, wing membranes (teal on the inner side, orange outer edges), wing arms and finger (orange), two head horns, white claws, tail flame, blue eyes, open mouth with fangs. On this sprite the spur at each wing's joint is orange like the skin.

| Surface | Made of | Material | Evidence | Confidence |
|---|---|---|---|---|
| Body skin (orange) | dragon-like reptile skin | Skin | Bulbapedia: "a draconic, bipedal Pokémon. It is primarily orange"; Origin: European dragons, lizards. Smooth in art and HOME. | medium |
| Belly, tail underside, soles (cream) | the same skin | Belly | Bulbapedia: "a cream underside from the chest to the tip of its tail", "cream-colored soles". Own row. | high |
| Wing membrane | thin skin stretched between wing bones | Wing membrane | Bulbapedia: "Two large wings with blue-green undersides sprout from its back... A single wing finger is visible through the center of each wing membrane." FireRed, Y, Shield: "Its wings can carry this Pokémon close to an altitude of 4,600 feet." **No official text or art says light passes through** (searched); translucency comes from what a wing membrane is (bat and pterosaur wings are thin skin). The two sides are colored differently, so it is pigmented skin: lets light through, never clear. This is the strongest visual effect on the sprite and worth keeping. | medium-low |
| Wing arms, finger and outer edge (orange) | skin over bone | Skin | Same color and outline as the body in art and sprite. | medium |
| Wing spur | horn | Skin | Bulbapedia: "a horn-like appendage juts out from the top of the third joint of each wing." Skin-colored on this sprite; barely a few pixels. | low |
| Head horns | skin-covered horn | Skin | Bulbapedia: "two horn-like structures protruding from the back of its rectangular head." Orange like the skin in art and HOME. | low |
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
| Skin (light blue) | smooth aquatic reptile skin | Skin | Bulbapedia: "a small reptilian Pokémon that resembles a light-blue turtle"; Origin: baby turtles and terrapins; lives "around small ponds and lakes". Art and HOME: smooth, with a soft sheen; Skin. | medium |
| Upper shell (brown) | hard, smooth, springy shell | Shell | The entries quoted above. Bulbapedia: "Its body is encased by a tough shell that forms and hardens after birth." Black 2/White 2: "It shelters itself in its shell then strikes back with spouts of water at every opportunity." | medium |
| Belly plate (pale yellow) | the same shell, underside | Belly plate | Bulbapedia: "This shell is brown on the top, pale yellow on the bottom". The drawn grooves are lines, not a different material. | medium |
| Shell rim (white) | the same shell | Shell | Bulbapedia: "has a thick white ridge between the two halves." | medium |
| Tail | skin | Skin | Bulbapedia: "The end of its long, squirrel-like tail curls inward." | high |
| Eyes, mouth | see shared rules | see shared rules | Bulbapedia: "large, purplish, or reddish eyes". | high |

### Wartortle (#008)

Drawn surfaces: blue skin, dark cheek streaks, furry ears, big furry tail, brown upper shell, pale yellow belly plate, white rim, white claws, two fangs, brown eyes.

| Surface | Made of | Material | Evidence | Confidence |
|---|---|---|---|---|
| Skin (blue) | smooth aquatic reptile skin | Skin | Bulbapedia: "a bipedal, indigo reptilian Pokémon similar to a turtle." | medium |
| Cheek streaks | pigment | Skin | Bulbapedia: "a dark blue streak on each cheek". Own row. | high |
| Ear fur | fur | Fur | Silver and SoulSilver: "It cleverly controls its furry ears and tail to maintain its balance while swimming." Bulbapedia: "feather-like ears covered in pale blue fur". Fully fuzzy so it reads clearly at sprite size. | high |
| Tail fur | thick fur | Fur (its blue swirl lines their own Fur row) | Black 2/White 2: "It is said to live 10,000 years. Its furry tail is popular as a symbol of longevity." Ruby/Sapphire: "Its tail is large and covered with a rich, thick fur." Bulbapedia: "Air can be stored in its fur". Thick fur, so it does not let light through. Origin: the minogame, a 10,000-year-old turtle with a seaweed tail. | high |
| Upper shell (brown) | hard shell, scratched with age | Shell | Ruby/Sapphire: "The scratches on its shell are evidence of this POKéMON's toughness as a battler." Gold: "If its shell has algae on it, that WARTORTLE is very old." A worn, older shell: a little less shine than Squirtle's. | medium |
| Belly plate (pale yellow) | the same shell | Belly plate | Bulbapedia: "A brown shell with a pale yellow underside encases its body." | medium |
| Shell rim (white) | the same shell | Shell | Bulbapedia: "A thick, white rim separates the upper and lower halves of the shell." | medium |
| Claws, fangs, eyes | see shared rules | see shared rules | Bulbapedia: "brown eyes", "two sharp teeth protruding from its upper jaw", "three clawed fingers". | high |

### Blastoise (#009)

Drawn surfaces: blue skin, cream lower jaw, ear insides (black), brown upper shell, cream belly plate, white rim (around the arms too), two cannons with dark openings, white claws, brown eyes.

**Are the cannons gray metal?** Not by the evidence. No Pokédex entry or official page calls them metal: Black 2/White 2 calls them "rocket cannons", Violet "jet nozzles", Ruby/Sapphire "water spouts that protrude from its shell", and the official Gigantamax page "water cannons". Bulbapedia says "These cannons can be extended or withdrawn", which makes them part of the shell. In the Sugimori art and the HOME model they are **white with pale gray shading, the same white as the shell rim**, with no reflections and no metallic tint. The only metal hints are the word "rocket cannons" and Bulbapedia's Origin note that the design is "a turtle mixed with aspects of a tank". The Black 2/White 2 sprite draws them in a gray ramp with a white highlight band, which makes them look more like metal than the art does.

So they are Shell, like the rim. Metal (finish 1, body -1) would be a style choice, not something the sources say; the owner is asked which.

| Surface | Made of | Material | Evidence | Confidence |
|---|---|---|---|---|
| Skin (blue) | heavy, thick reptile skin | Skin | Bulbapedia: "Its body is blue and is mostly hidden by its tough, brown shell." HeartGold: "It deliberately makes itself heavy so it can withstand the recoil of the water jets it fires." | medium |
| Lower jaw (cream), ear insides (black) | the same skin | Belly (jaw); the ear insides are drawn black, so line | Bulbapedia: "triangular ears that are black on the inside", "a cream-colored lower jaw". Own rows. | high |
| Upper shell (brown) | tough shell | Shell | Bulbapedia: "tough, brown shell". FireRed, X, Sword: "In a pinch, it will withdraw inside its shell." Art: weathered brown plates; HOME: soft sheen. | medium |
| Belly plate (cream) | the same shell | Belly plate | Bulbapedia: "This shell has a cream-colored underside". | medium |
| Shell rim (white) | the same shell | Shell | Bulbapedia: "a white ridge encircling its arms and separating the upper and lower halves." | medium |
| Cannons | hard tubes that grow from the shell (material never stated) | Shell | See above. | low |
| Cannon openings (dark) | a hole | Outline | Keep dark; do not let a highlight land in it. | high |
| Claws, eyes | see shared rules | see shared rules | Bulbapedia: "small brown eyes", "three claws on each hand". | high |

Nothing on Blastoise glows. The water it fires is an attack effect, not part of the sprite.

### Caterpie (#010)

Drawn surfaces: green body segments, cream-yellow belly and feet, eye (black with a yellow ring) on each side of the head, yellow ring spots along the sides, red forked antenna with orange tips, yellow teardrop tail tip.

| Surface | Made of | Material | Evidence | Confidence |
|---|---|---|---|---|
| Body segments (green) | soft caterpillar skin | Skin | FireRed: "It is covered with a green skin. When it grows, it sheds the skin, covers itself with silk, and becomes a cocoon." Ultra Moon: "Its body is soft and weak." Black 2/White 2: "It grows by molting repeatedly." Crystal: "It crawls into foliage where it camouflages itself among leaves that are the same color as its body." Sugimori art draws white highlights on every segment and HOME shows slightly shiny segments, so it is Skin (its sheen), without light through, which looked slick. | medium |
| Belly and feet (cream-yellow) | the same soft skin | Belly | Red/Blue: "Its short feet are tipped with suction pads that enable it to tirelessly climb slopes and walls." Bulbapedia: "a green caterpillar with a yellow underside". | medium |
| Eye (black with yellow ring) | eye | Eye | Bulbapedia Trivia: "It is inconsistent across the franchise whether or not the yellow and black spots on Caterpie's head are actually its eyes or merely spots resembling eyes." **On this sprite they are eyes**: the Black 2/White 2 sprite has an "eyes closed" look that shuts them with a green lid. | high (for this sprite) |
| Side ring spots (yellow) | pigment, false eyes | Skin | Bulbapedia: "Yellow ring-shaped markings down the sides of its segmented body resemble its eyes and are meant to scare off predators." Origin: swallowtail caterpillars' "yellow eyespots". Painted marks on the skin; own row. **No glow**: nothing says they give off light. | high |
| Red antenna (osmeterium) | soft scent organ | Skin | Black 2/White 2: "It releases a stench from its red antenna to repel enemies." Sword: "For protection, it releases a horrible stench from the antenna on its head to drive away enemies." Yellow: "If you touch the feeler on top of its head, it will release a horrible stink to protect itself." Bulbapedia: "the bright red antenna (osmeterium) on its head, which releases a stench to repel predators." A real swallowtail's osmeterium is soft, moist tissue (real-world biology, not game text); Skin. **No glow**: its color is a warning, not light. | glow 0: high; material: medium-low |
| Tail tip (yellow teardrop) | soft horn-like tip | Belly | Bulbapedia: "teardrop-shaped tail"; Origin: "The tip of its tail resembles the horn that many species of hawk moth larvae have on their rear ends." Those horns are soft skin. | low |
| Mouth | see shared rules | see shared rules | Small and dark on this sprite. | high |

---

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
