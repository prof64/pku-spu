# Golduck: smooth blue skin all over (the painted art gives it soft pale patches, like Squirtle's), a cream bill,
# cream webbing between fingers and toes, white claws, and a red gem on its forehead.
# Colors: 15 black; 14 13 12 11 the blues (14 their dark contour); 9 8 7 6 the creams of bill and webbing;
# 2 1 gray and white (claws, the eyes' whites, the gem's catchlight); 5 4 3 the reds (eyes, gem).
SOURCE = "sources/black2-white2/0055-golduck.spu"
SKIN = dict(finish=0.5, body=0.08)        # smooth aquatic skin: Turtle skin's dials
MATERIALS = [
    dict(name="outline", shades=[15], finish=0.1, body=0),
    # both views together are mostly painted in 13 (the back wholly)
    dict(name="aquatic skin", shades=[14, 13, 12], base=1, **SKIN),
    # the palest blue (11): the lit patches on the forehead, shoulder, knees and crest, the same skin at its most
    # lit. In their own row so they go dark with the body; left as painted glints they stayed pale with the sun behind
    dict(name="aquatic skin, lit patches", shades=[14, 13, 12, 11], base=1, **SKIN),
    # the webbing between fingers and toes: the same skin, cream, painted flat
    dict(name="aquatic skin, webbing", shades=[9, 7, 6], base=1, finish=0.2, body=0.08),
    dict(name="beak", shades=[9, 8, 7, 6], base=2, finish=0.4, body=0.05),
    dict(name="claws and teeth", shades=[2, 1], base=1, finish=0.7, body=0.05),
    # the red gem on the forehead: polished, with a painted white catchlight. It shines only when Golduck
    # uses its power, so no glow at rest
    dict(name="gem, red", shades=[5, 4, 3, 1], base=1, finish=1, body=0.6),
    dict(name="eye (line art)", shades=[5, 4, 2, 1], finish=0.9, body=0),
]
def to(name, colors): return {c: name for c in colors}
WEB, BEAK, GEM, EYE = "aquatic skin, webbing", "beak", "gem, red", "eye (line art)"
COLORS = {15: "outline", **to("aquatic skin", [14, 13, 12]), 11: "aquatic skin, lit patches", **to(WEB, [9, 8, 7, 6]),
          **to("claws and teeth", [2, 1]), **to(EYE, [5, 4]), 3: GEM}
RULES = [
    # the head, both views: the bill (the drawings named "head 2" are a hand and a patch of the back)
    dict(drawings=["head"], colors=to(BEAK, [9, 8, 7, 6])),
    # the eyes' whites
    dict(view="front", drawings=["head", "head-eyes-open"], colors=to(EYE, [2, 1])),
    # the gem between and above the eyes
    dict(view="front", drawings=["head"], rect=[10, 16, 3, 3], colors=to(GEM, [5, 4, 3, 1])),
]
