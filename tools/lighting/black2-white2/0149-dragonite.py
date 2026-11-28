# Dragonite: a big orange dragon. Smooth orange hide, a cream underside ridged with lines from the throat to
# the tip of the tail, two thin cream antennae, small wings (teal membrane inside, orange outside), white claws.
# No Pokédex entry describes any surface; the painted art shades the hide with broad soft pale patches and the
# belly flat, with a hard highlight only on the claws.
# Palette: 1 black; 6 5 4 3 2 the orange (6 its brown contour, 5 its shadow and the belly's darkest lines);
# 9 8 7 the teal membrane (9 only the thin lines of its fingers); c b a the cream; f e d gray to white.
SOURCE = "sources/black2-white2/0149-dragonite.spu"
HIDE, CREAM, CLAW = [6, 5, 4, 3, 2], [5, 12, 11, 10], [15, 14, 13]
MATERIALS = [
    # black; the dark teal lines of the fingers inside the membrane; the brown line round each thin antenna
    dict(name="outline", shades=[1, 9, 6, 5], finish=0.1, body=0),
    dict(name="dragon hide", shades=HIDE, base=2, finish=0.5, body=0.05),
    # the antennae: the same skin in the belly's cream, one pixel wide
    dict(name="dragon hide, antennae", shades=[11, 10], base=0, finish=0.5, body=0.05),
    # throat, belly and the underside of the tail; its ridge lines are its own dark shades. Charizard's underbelly
    # lets more light through (0.25); at that value this much bigger belly stayed pale on a body gone dark
    dict(name="underbelly", shades=CREAM, base=2, finish=0.4, body=0.15),
    # the teal inner side of the wings
    dict(name="wing membrane", shades=[8, 7], base=0, finish=0.3, body=0.3),
    # the wings from behind: the same thin skin, its orange side
    dict(name="wing membrane, outer side", shades=[6, 5, 4, 3], base=2, finish=0.3, body=0.3),
    dict(name="claws and teeth", shades=CLAW, base=1, finish=0.7, body=0.05),
    dict(name="eye (line art)", shades=[1, 6, 14, 13], finish=0.9, body=0),
]
def to(name, colors): return {c: name for c in colors}
COLORS = {1: "outline", 9: "outline", **to("dragon hide", HIDE), **to("underbelly", [12, 11, 10]),
          **to("wing membrane", [8, 7]), **to("claws and teeth", CLAW)}
EYE = to("eye (line art)", [1, 6, 14, 13])
RULES = [
    # the reddish brown is the belly's darkest shade wherever the belly is: its edge against the hide, the ridge
    # lines of the throat and of the tail's underside
    dict(view="front", drawings=["karada", "o1"], colors={5: "underbelly"}),
    dict(view="back", drawings=["tail-a"], rect=[0, 19, 48, 9], colors={5: "underbelly"}),
    dict(drawings=["tuno*", "ear-*"], colors={**to("dragon hide, antennae", [11, 10]), 6: "outline", 5: "outline"}),
    dict(view="back", drawings=["wing-*"], colors=to("wing membrane, outer side", [6, 5, 4, 3])),
    # eyes: black, the brown iris, white and gray. Front: only on the eyes drawing (far eye, near eye)
    dict(drawings=["atama-eyes-open"], rect=[3, 2, 1, 4], colors=EYE),
    dict(drawings=["atama-eyes-open"], rect=[11, 2, 4, 5], colors=EYE),
    # back: on the head and again on the eyes drawing
    dict(view="back", drawings=["head"], rect=[16, 10, 3, 5], colors=EYE),
    dict(drawings=["head-eyes-open"], rect=[1, 1, 3, 5], colors=EYE),
]
# the palest orange is the broad lit patch on the forehead, snout, flank and thigh: a real shade. Left out of the
# row those patches turned olive under the studio lamp and stayed pale on a body gone dark with the sun behind.
KEEP_TOP = ["dragon hide"]
