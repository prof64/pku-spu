# Electabuzz: a yellow coat with black stripes (Short fur, as on Pikachu and Raichu), white claws and a fang.
# "Electricity runs across the surface of its body. In darkness, its entire body glows a whitish-blue"
# (Gold, HeartGold, X): a faint glow on the whole coat, as on Raichu.
SOURCE = "sources/black2-white2/0125-electabuzz.spu"
SHORT = dict(finish=-0.2, body=0.05)
MATERIALS = [
    # black line; the shut eyes' lid lines are drawn in the coat's dark brown, the fang's far edge in blue-gray
    dict(name="outline", shades=[1, 6, 10, 13], finish=0.1, body=0),
    # the yellow coat: its brown contour is its darkest shade. The back is painted in 5, the front in 5 and 3
    dict(name="short fur", shades=[6, 5, 4, 3, 2], base=2, **SHORT),
    # the black stripes and the bolt on the chest: black in shade (1 behind, 13 in front), blue-gray and gray where lit
    dict(name="short fur, stripes", shades=[1, 13, 10, 9], base=1, **SHORT),
    # white claws with their gray shade and dark-gray edge; the one fang
    dict(name="claws and teeth", shades=[9, 8, 7], base=2, finish=0.7, body=0.05),
    dict(name="mouth", shades=[12, 11], base=0, finish=0.8, body=0),
    dict(name="eye (line art)", shades=[6, 13, 7], finish=0.9, body=0),
]
# The coat's palest yellow (2) is few pixels but one broad painted patch on the forehead and the fists, and the
# stripes' gray (9) is one whole arm of the forehead's V: left out of their rows both stayed pale on a body gone
# dark in the cave and with the sun behind, so they stay shades.
KEEP_TOP = ["short fur", "short fur, stripes"]
def to(name, colors): return {c: name for c in colors}
STRIPES = "short fur, stripes"
COLORS = {1: "outline", **to("short fur", [6, 5, 4, 3, 2]), **to(STRIPES, [13, 10, 9]),
          **to("claws and teeth", [8, 7]), **to("mouth", [12, 11])}
EYE = to("eye (line art)", [6, 13, 7])
RULES = [
    # seen from behind the stripes are painted in the line's own black: broad black is stripe, a one-pixel stroke is line
    dict(view="back", drawings=["body", "hand-l", "hand-r", "leg-l", "leg-r"], colors={1: STRIPES}, thin_all={1: "outline"}),
    # the feet: the gray there is the claws' shade and edge (two toes and a heel spur on each foot)
    dict(drawings=["foot-*"], colors={9: "claws and teeth"}),
    # the eyes: white, pupil, and the dark brown ring and brow line
    dict(view="front", drawings=["head"], rect=[8, 15, 3, 4], colors=EYE),
    dict(view="front", drawings=["head"], rect=[15, 15, 4, 4], colors=EYE),
    dict(drawings=["head-eyes-open"], rect=[2, 2, 3, 4], colors=EYE),
    dict(drawings=["head-eyes-open"], rect=[9, 2, 4, 4], colors=EYE),
    dict(drawings=["head-eyes-closed"], rect=[2, 2, 3, 4], colors={6: "outline"}),
    dict(drawings=["head-eyes-closed"], rect=[9, 2, 4, 4], colors={6: "outline"}),
    # the dark edge beside the fang, and one dark pixel under the jaw
    dict(view="front", drawings=["head"], rect=[22, 18, 1, 3], colors={10: "outline"}),
    dict(drawings=["mouse"], colors={13: "outline"}),
]
GLOW = [dict(material=m["name"], glow=4, intent="in darkness its entire body glows")
        for m in MATERIALS if m["name"].startswith("short fur")]
