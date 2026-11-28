SOURCE = "sources/black2-white2/0115-kangaskhan.spu"
# Kangaskhan: a brown hide with raised pads, a cream belly with the pouch, cream ear insides, a dark patch on
# top of the head, white claws and a fang, an open red mouth, and the lilac baby in the pouch (its own head
# patch, ears and claws). The painted art shades every part of the body flat and soft, with no highlight, and
# no Pokédex entry names fur or scales: all of it is plain Hide, as on the Nidoran line.
# Colors: 6 black; 15-12 the hide's browns (15 its dark contour, 12 its palest); 11-9 the head patch's olive
# grays (11 also draws the claws' dark edge); 4, 3 cream; 8, 7 the baby's lilac; 2, 1 claws, fang, eye white;
# 5 red (the open mouth, the iris).
H = dict(finish=0.25, body=0.08)
MATERIALS = [
    # black; the brown lines drawn on the cream and lilac parts, which have no dark shade of their own (the
    # belly's edge, the pouch's lip, the baby's contour, the fold in the ear, the eye's rim); the olive edge
    # of the claws and the fang (in the shiny palette that color is green, so it cannot be a claw's shade)
    dict(name="outline", shades=[6, 15, 14, 11], finish=0.1, body=0),
    # head, body, arms, legs, tail, the raised pads and the bumps on the back and tail. Its dark brown
    # contour is its darkest shade; both views are painted in 14
    dict(name="hide", shades=[15, 14, 13, 12], base=1, **H),
    # the cream belly and pouch: the same hide, pale
    dict(name="hide, belly", shades=[4, 3], base=0, **H),
    # inside the ears (mother and baby)
    dict(name="hide, ears", shades=[4, 3], base=0, **H),
    # the dark patch on top of the head (mother and baby): pigment in the hide
    dict(name="hide, head patch", shades=[11, 10, 9], base=0, **H),
    # the baby's lilac body and hands
    dict(name="hide, baby", shades=[8, 7], base=0, **H),
    dict(name="claws and teeth", shades=[2, 1], base=1, finish=0.7, body=0.05),
    dict(name="mouth", shades=[5], base=0, finish=0.8, body=0),
    dict(name="eye (line art)", shades=[6, 5, 2, 1], finish=0.9, body=0),
]
# the palest brown is few of the hide's pixels overall but a broad painted patch on the shoulder pad, the
# tail's top and the jaw ridge: a shade, not a glint
KEEP_TOP = ["hide"]
def to(name, colors): return {c: name for c in colors}
EARS, EYE, LINE = "hide, ears", "eye (line art)", "outline"
COLORS = {6: LINE, **to("hide", [15, 14, 13, 12]), **to("hide, belly", [4, 3]), **to("hide, head patch", [11, 10, 9]),
          **to("hide, baby", [8, 7]), **to("claws and teeth", [2, 1]), 5: "mouth"}
RULES = [
    # ears: cream inside, a brown hide rim; the dark fold line and the gray edge are lines
    dict(drawings=["mimi01", "mimi02", "l-mimi"], colors={**to(EARS, [4, 3]), 15: LINE, 11: LINE}),
    dict(drawings=["r-mimi"], colors={**to(EARS, [4, 3]), 11: LINE}),
    # the claws' dark edge
    dict(drawings=["ude02", "ude03", "foot-l", "foot-r", "r-asi", "r-ude", "l-asi"], colors={11: LINE}),
    # the fang's dark edge
    dict(view="front", drawings=["atama00"], rect=[15, 21, 5, 3], colors={11: LINE}),
    # the belly and pouch: the brown lines around the belly, along the pouch's lip and around the baby
    dict(view="front", drawings=["hara01"], rect=[0, 20, 40, 34], colors={15: LINE, 11: LINE}),
    # the baby: its contour, its cream ears
    dict(view="front", drawings=["aka", "aka-eyes-*"], colors={15: LINE, 14: LINE}),
    dict(view="front", drawings=["aka"], rect=[3, 4, 12, 3], colors=to(EARS, [4, 3])),
    dict(view="back", drawings=["body"], rect=[41, 16, 7, 11], colors={15: LINE}),
    dict(view="back", drawings=["body"], rect=[40, 16, 3, 1], colors=to(EARS, [4, 3])),
    dict(view="back", drawings=["body-eyes-*"], colors={15: LINE}),
    # eyes: white, red iris, pupil; their brown rim lines
    dict(view="front", drawings=["atama00-eyes-*"], rect=[2, 2, 6, 4], colors={15: LINE}),
    dict(view="front", drawings=["atama00-eyes-open"], rect=[3, 2, 4, 4], colors=to(EYE, [1, 5])),
    dict(view="front", drawings=["atama00-eyes-open"], rect=[4, 4, 1, 1], colors={6: EYE}),
    dict(view="front", drawings=["aka-eyes-open"], rect=[3, 2, 3, 3], colors=to(EYE, [6, 1])),
    dict(view="back", drawings=["body-eyes-open"], rect=[3, 4, 2, 1], colors=to(EYE, [6, 2])),
    dict(view="back", drawings=["atama-eyes-*"], rect=[2, 2, 3, 3], colors={15: LINE}),
    dict(view="back", drawings=["atama-eyes-open"], rect=[3, 2, 2, 3], colors=to(EYE, [1, 2, 5, 6])),
]
