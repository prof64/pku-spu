SOURCE = "sources/black2-white2/0018-pidgeot.spu"
# Pidgeot: glossy plumage (Ruby: "a dazzling plumage of beautifully glossy feathers"): brown above, cream below,
# long head feathers striped yellow and red, a red tail, a black mask through the eye, a pink beak and legs, white talons.
# Colors: 15 black; 14 13 12 the browns; 5 4 cream and yellow; 9 8 7 the reds; 11 10 pink; 2 1 gray and white.
GLOSS = dict(finish=0.3, body=0)
MATERIALS = [
    dict(name="outline", shades=[15, 14, 13, 9, 12], finish=0.1, body=0),
    dict(name="glossy feathers", shades=[14, 13, 12], base=1, **GLOSS),
    dict(name="glossy feathers, cream", shades=[14, 13, 5, 4], base=2, **GLOSS),
    dict(name="glossy feathers, crest yellow", shades=[12, 5, 4], base=1, **GLOSS),
    dict(name="glossy feathers, crest red and tail", shades=[9, 8, 7], base=1, **GLOSS),
    # the black mask through the eye; its soft lower edge is drawn in the darkest brown
    dict(name="glossy feathers, mask", shades=[15, 14], base=0, **GLOSS),
    dict(name="beak", shades=[14, 13, 11, 10], base=3, finish=0.4, body=0.05),
    dict(name="dry hide, legs", shades=[14, 13, 11, 10], base=2, finish=0.05, body=0.03),
    dict(name="claws and teeth", shades=[2, 1], base=1, finish=0.7, body=0.05),
    dict(name="eye (line art)", shades=[15, 12, 2, 1], finish=0.9, body=0),
]
def to(name, colors): return {c: name for c in colors}
BROWN, CREAM, YELLOW, RED, MASK, BEAK, LEGS, LINE, EYE = (
    "glossy feathers", "glossy feathers, cream", "glossy feathers, crest yellow", "glossy feathers, crest red and tail",
    "glossy feathers, mask", "beak", "dry hide, legs", "outline", "eye (line art)")
COLORS = {15: LINE, **to(BROWN, [14, 13, 12]), **to(CREAM, [5, 4]), **to(RED, [9, 8, 7]),
          **to(BEAK, [11, 10]), **to("claws and teeth", [2, 1])}

HEAD = {"front": ("atama", 5, 6), "back": ("head01", 14, 3)}     # the head drawing, and where the eye drawings sit on it
def head(view, rect, colors):
    """A rule for a region of the head, given once for the head and for the eye drawings laid over it."""
    name, ox, oy = HEAD[view]
    return [dict(view=view, drawings=[name], rect=rect, colors=colors),
            dict(view=view, drawings=[name + "-eyes-*"], rect=[rect[0]-ox, rect[1]-oy, rect[2], rect[3]], colors=colors)]

CREST = ["kami0*", "ksmi011", "parts0*"]
# where the wing's brown narrows to one pixel (it is still the brown plumage, not a line between feathers)
BAND = {
    ("front", "hane02"): [[3, 9, 1, 2], [13, 19, 1, 1]],
    ("back", "r-wings01"): [[35, 6, 1, 1], [39, 20, 1, 1], [38, 21, 2, 1], [38, 22, 1, 1], [38, 23, 1, 1], [33, 24, 1, 1], [37, 24, 1, 1],
                            [37, 25, 1, 1], [36, 26, 2, 1], [36, 27, 1, 1], [35, 28, 1, 1]],
}
RULES = [
    # the near wing: layers of feathers, the dark lines between them are creases
    dict(drawings=["hane02", "r-wings01"], thin_all={13: LINE, 14: LINE}),
    *[dict(view=v, drawings=[d], rect=r, colors={13: BROWN}) for (v, d), rects in BAND.items() for r in rects],
    # head feathers: yellow and red stripes; their brown contour is a line, a light brown stroke the yellow's shade
    dict(drawings=CREST, colors=to(YELLOW, [4, 5, 12]), thin_all={13: LINE, 14: LINE}),
    # tail: red feathers, the dark red lines between them are creases
    dict(drawings=["o", "tail01"], thin_all={9: LINE, 14: LINE}),
    # bodies: the cream's contour, and the feather marks low on the belly
    dict(drawings=["karada", "body01"], colors=to(CREAM, [14])),
    dict(view="front", drawings=["karada"], rect=[0, 24, 40, 21], colors=to(CREAM, [13])),
    # beak
    dict(drawings=["kuti"], colors=to(BEAK, [13, 14])),
    dict(drawings=["kuti"], rect=[8, 8, 1, 1], colors=to(LINE, [13])),        # the line between its two halves
    # legs and feet: bare pink skin
    dict(drawings=["asi0*", "*-leg01", "*-foot01"], colors=to(LEGS, [10, 11, 13, 14])),
    dict(view="front", drawings=["asi04"], rect=[8, 7, 1, 1], colors=to(LINE, [12])),     # a knuckle's wrinkle
    # front head: mask and eye
    *head("front", [8, 6, 10, 11], to(MASK, [15, 14])),
    dict(view="front", drawings=["atama-eyes-open"], rect=[4, 2, 4, 3], colors=to(EYE, [1, 15])),
    # back head: mask, beak, cheek, eye
    *head("back", [12, 4, 9, 10], to(MASK, [15, 14])),
    *head("back", [15, 14, 2, 1], to(MASK, [15])),
    *head("back", [20, 11, 1, 1], to(LINE, [15])),                             # the line between the beak's halves
    *head("back", [21, 8, 3, 6], to(BEAK, [14])),
    *head("back", [19, 12, 1, 1], to(BEAK, [13])),
    *head("back", [19, 14, 1, 1], to(CREAM, [14])),
    *head("back", [18, 15, 1, 1], to(CREAM, [13])),
    dict(view="back", drawings=["head01-eyes-open"], rect=[3, 3, 3, 3], colors=to(EYE, [1, 2, 12, 15])),
]
