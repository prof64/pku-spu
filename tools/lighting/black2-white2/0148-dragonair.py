# Dragonair: Dratini grown long. The same smooth blue serpent skin and white belly, the head fins grown into
# small white wing shapes, a white horn on the forehead, and three orbs (one under the chin, two on the tail)
# that the Pokédex calls crystal (Silver: "Its crystalline orbs"; Ruby: "the crystals on its neck and tail").
# The painted art shades body, belly and wings flat and soft and puts a small hard white highlight on every orb.
# Palette: 1 black; 6 5 4 3 the blue (6 its navy contour); a 9 8 7 gray to white (belly, wings, horn);
# d c b the orbs (gold in the shiny palette); e f the eye's red.
SOURCE = "sources/black2-white2/0148-dragonair.spu"
BLUE, WHITE, ORB = [6, 5, 4, 3], [10, 9, 8, 7], [13, 12, 11]
MATERIALS = [
    # black; the navy pixels drawn round the top of each orb; the dark gray lines between the wings' feather shapes
    dict(name="outline", shades=[1, 6, 10], finish=0.1, body=0),
    dict(name="snake scales", shades=BLUE, base=1, finish=0.15, body=0.05),
    dict(name="snake scales, belly", shades=WHITE, base=2, finish=0.15, body=0.05),
    # the head wings: Dratini's fins grown (FireRed: "Even though it has no wings, it has been seen flying")
    dict(name="fin", shades=WHITE, base=2, finish=0.3, body=0.15),
    dict(name="claws and teeth, horn", shades=WHITE, base=3, finish=0.7, body=0.05),
    # the three orbs: polished crystal, with the white of their painted highlight as the top shade
    dict(name="crystal, gem", shades=ORB + [7], base=1, finish=1, body=0.6),
    dict(name="eye (line art)", shades=[1, 7, 14, 15], finish=0.9, body=0),
]
def to(name, colors): return {c: name for c in colors}
COLORS = {1: "outline", **to("snake scales", BLUE), **to("snake scales, belly", WHITE), **to("crystal, gem", ORB)}
GEM = {7: "crystal, gem", 6: "outline"}
RULES = [
    dict(drawings=["wing-*", "mimi-*"], colors=to("fin", WHITE), thin_all={10: "outline"}),
    # the horn: on the head from the front, standing out past it from behind
    dict(view="front", drawings=["head"], rect=[0, 5, 6, 4], colors=to("claws and teeth, horn", WHITE)),
    dict(view="back", drawings=["atama"], rect=[16, 3, 7, 4], colors=to("claws and teeth, horn", WHITE)),
    # the orbs' white highlight and the navy pixels of their top edge
    dict(view="front", drawings=["neck"], rect=[4, 10, 7, 6], colors=GEM),
    dict(view="front", drawings=["tail"], rect=[8, 3, 3, 2], colors=GEM),
    dict(view="front", drawings=["tail"], rect=[4, 6, 3, 2], colors=GEM),
    dict(view="back", drawings=["kubi"], rect=[12, 3, 5, 6], colors=GEM),
    dict(view="back", drawings=["o"], rect=[28, 5, 8, 4], colors=GEM),
    # the eye is only on the eyes drawing: black, a white catchlight, a red iris
    dict(drawings=["head-eyes-open"], rect=[2, 1, 3, 6], colors=to("eye (line art)", [1, 7, 14, 15])),
    # one pixel of the near wing drawn on the closed-eyes picture
    dict(drawings=["head-eyes-closed"], rect=[7, 0, 1, 1], colors={8: "fin"}),
]
