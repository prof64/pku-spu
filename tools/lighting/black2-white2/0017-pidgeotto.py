SOURCE = "sources/black2-white2/0017-pidgeotto.spu"
# Pidgeotto: brown plumage above, cream below and under the wings, a red crest and red and cream tail feathers,
# a black mask through the eye, a pink beak and legs, white talons.
# Colors: 4 black; 11 10 9 the browns; 7 6 the creams; 15 14 13 12 the reds; 8 5 pink; 3 2 1 gray to white.
MATERIALS = [
    dict(name="outline", shades=[4, 11, 10, 15, 3], finish=0.1, body=0),
    dict(name="feathers", shades=[11, 10, 9], base=1, finish=-0.2, body=0.05),
    # the cream underside, cheek and flight feathers: the browns are its contour and the soft ends of its feather lines
    dict(name="feathers, cream", shades=[11, 10, 9, 7, 6], base=3, finish=-0.2, body=0.05),
    dict(name="feathers, crest", shades=[15, 14, 13, 12], base=2, finish=-0.2, body=0.05),
    dict(name="feathers, tail", shades=[15, 14, 13], base=1, finish=-0.2, body=0.05),
    # the black mask through the eye; the palette's darkest brown is the step light can lift it to
    dict(name="feathers, mask", shades=[4, 11], base=0, finish=-0.2, body=0.05),
    dict(name="beak", shades=[15, 14, 8, 5], base=2, finish=0.4, body=0.05),
    dict(name="dry hide, legs", shades=[15, 8, 5], base=1, finish=0.05, body=0.03),
    dict(name="claws and teeth", shades=[3, 2, 1], base=2, finish=0.7, body=0.05),
    dict(name="eye (line art)", shades=[4, 11, 3, 2, 1], finish=0.9, body=0),
]
def to(name, colors): return {c: name for c in colors}
BROWN, CREAM, RED, TAIL, MASK, BEAK, LEGS, LINE, EYE = ("feathers", "feathers, cream", "feathers, crest", "feathers, tail",
                                                        "feathers, mask", "beak", "dry hide, legs", "outline", "eye (line art)")
COLORS = {4: LINE, **to(BROWN, [11, 10, 9]), **to(CREAM, [7, 6]), **to(RED, [15, 14, 13, 12]),
          **to(BEAK, [8, 5]), **to("claws and teeth", [3, 2, 1])}

HEAD = {"front": ("atama", 1, 11), "back": ("head", 14, 8)}     # the head drawing, and where the eye drawings sit on it
def head(view, rect, colors):
    """A rule for a region of the head, given once for the head and for the eye drawings laid over it."""
    name, ox, oy = HEAD[view]
    return [dict(view=view, drawings=[name], rect=rect, colors=colors),
            dict(view=view, drawings=[name + "-eyes-*"], rect=[rect[0]-ox, rect[1]-oy, rect[2], rect[3]], colors=colors)]

WINGS = ["hane*", "wing-*"]
# where the brown band along a wing's leading edge narrows to one pixel (it is still the band, not a cream feather's line)
BAND = {
    ("front", "hane"): [[22, 7, 1, 1], [21, 8, 1, 1], [20, 9, 1, 1], [19, 10, 1, 1], [18, 11, 2, 1], [18, 12, 1, 1], [17, 13, 2, 1], [8, 29, 1, 1],
                        [7, 30, 2, 1], [7, 31, 1, 1], [7, 32, 1, 1], [6, 33, 2, 1], [6, 34, 1, 1], [6, 35, 1, 1], [5, 38, 1, 1], [2, 45, 1, 2]],
    ("front", "hane-3"): [[25, 1, 1, 1], [1, 19, 1, 1]],
    ("front", "hane-2"): [[12, 5, 1, 1], [9, 6, 1, 1], [9, 7, 1, 1], [19, 20, 1, 1], [19, 30, 2, 1]],
    ("front", "hane2"): [[10, 9, 1, 1], [11, 10, 1, 1], [12, 11, 1, 1], [13, 12, 1, 1], [13, 13, 2, 1], [14, 14, 2, 1], [15, 15, 2, 1], [39, 44, 1, 1]],
    ("front", "hane2-3"): [[15, 5, 1, 1], [2, 23, 1, 1], [2, 24, 1, 1]],
    ("front", "hane2-2"): [[44, 16, 1, 1]],
    ("back", "wing-r"): [[9, 34, 1, 1], [8, 35, 2, 1], [7, 36, 1, 1]],
    ("back", "wing-r-3"): [[17, 11, 1, 1], [17, 12, 1, 1], [8, 16, 2, 1], [7, 17, 2, 1], [4, 18, 1, 1]],
    ("back", "wing-r-2"): [[19, 7, 1, 1], [20, 8, 1, 1], [20, 9, 2, 1]],
    ("back", "wing-l"): [[30, 30, 2, 1], [31, 31, 1, 1], [32, 32, 1, 1], [33, 33, 1, 1]],
    ("back", "wing-l-3"): [[13, 12, 1, 1], [33, 17, 1, 1], [33, 18, 3, 1], [36, 19, 1, 1]],
    ("back", "wing-l-2"): [[44, 8, 1, 1]],
}
RULES = [
    # wings: layers of feathers. The dark lines between them are creases; a thin stroke of the light brown is the
    # soft end of such a line or a cream feather's lit contour, the cream's own shade
    dict(drawings=WINGS, thin_all={10: LINE, 11: LINE, 9: CREAM}),
    *[dict(view=v, drawings=[d], rect=r, colors={9: BROWN}) for (v, d), rects in BAND.items() for r in rects],
    dict(drawings=["hane2*"], colors={3: LINE}),                      # one stray gray pixel at the wing's root
    # tail: red and cream feathers side by side, the body's brown over their roots
    dict(drawings=["o", "tail"], colors=to(TAIL, [15, 14, 13]), thin_all={15: LINE, 11: LINE, 10: LINE, 9: CREAM}),
    dict(view="front", drawings=["karada"], colors=to(TAIL, [15])),   # the tail's root under the body
    # front body: the cream belly's contour down the left and round the bottom
    dict(view="front", drawings=["karada"], rect=[2, 18, 4, 8], colors=to(CREAM, [11])),
    dict(view="front", drawings=["karada"], rect=[0, 26, 9, 8], colors=to(CREAM, [9, 10, 11])),
    # back body: the cream flank shows down the right edge
    dict(view="back", drawings=["body"], rect=[15, 17, 11, 16], colors=to(CREAM, [9])),
    dict(view="back", drawings=["body"], rect=[24, 19, 1, 5], colors=to(CREAM, [10])),
    dict(view="back", drawings=["body"], rect=[23, 25, 1, 2], colors=to(CREAM, [10])),
    dict(view="back", drawings=["body"], rect=[19, 31, 1, 1], colors=to(CREAM, [10])),
    # legs: bare pink skin under a cream thigh
    dict(drawings=["asi*", "foot"], colors={**to(LEGS, [15, 8, 5]), **to(CREAM, [9, 10, 11])}),
    dict(view="front", drawings=["asi1"], rect=[15, 13, 1, 1], colors=to(LINE, [10])),
    dict(view="front", drawings=["asi2"], colors=to(LINE, [10])),
    # front head: beak, cheek, mask, eye
    *head("front", [2, 20, 5, 3], to(BEAK, [14, 15])),
    *head("front", [4, 22, 2, 1], to(LINE, [15])),                     # the line between the two halves of the beak
    *head("front", [5, 25, 1, 1], to(BEAK, [15])),
    *head("front", [7, 21, 2, 4], to(CREAM, [10])),
    *head("front", [7, 18, 9, 5], to(MASK, [4])),
    *head("front", [13, 23, 2, 3], to(MASK, [4])),
    *head("front", [5, 22, 1, 1], to(LINE, [10])),
    dict(view="front", drawings=["atama-eyes-open"], rect=[6, 7, 4, 3], colors=to(EYE, [1, 2, 4, 11])),
    dict(view="front", drawings=["atama-eyes-closed"], rect=[7, 10, 2, 1], colors=to(LINE, [11])),    # the shut eye's lower line
    # back head
    *head("back", [19, 12, 5, 5], to(MASK, [4])),
    *head("back", [18, 13, 1, 4], to(MASK, [4])),
    *head("back", [24, 14, 2, 1], to(MASK, [4])),
    *head("back", [19, 17, 2, 1], to(MASK, [4])),
    *head("back", [23, 15, 2, 1], to(BEAK, [15])),
    *head("back", [22, 19, 2, 1], to(CREAM, [10])),
    *head("back", [20, 16, 1, 1], to(CREAM, [11])),
    dict(view="back", drawings=["head-eyes-open"], rect=[6, 5, 3, 3], colors=to(EYE, [1, 2, 3, 4])),
]
