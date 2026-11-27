SOURCE = "sources/black2-white2/0016-pidgey.spu"
# Pidgey: brown plumage above, cream below, a dark mask through the eye, a horny beak, bare legs, white claws.
# Colors: 4 black; 14 13 12 11 the browns; 10 9 8 the creams; 7 6 5 the beak's and legs' reds; 3 2 1 gray to white.
MATERIALS = [
    dict(name="outline", shades=[4, 14, 13], finish=0.1, body=0),
    dict(name="feathers", shades=[14, 13, 12, 11], base=2, finish=-0.2, body=0.05),
    # the cream underside, cheek, brow tufts and wing tips: drawn with the browns as its contour and its streaks
    dict(name="feathers, cream", shades=[14, 13, 11, 10, 9, 8], base=3, finish=-0.2, body=0.05),
    # the mask through the eye: dark brown from the front, black from behind
    dict(name="feathers, mask", shades=[4, 14, 13], base=1, finish=-0.2, body=0.05),
    dict(name="beak", shades=[14, 7, 6, 5], base=2, finish=0.4, body=0.05),
    dict(name="dry hide, legs", shades=[14, 13, 7, 6], base=2, finish=0.05, body=0.03),
    dict(name="claws and teeth", shades=[3, 2, 1], base=2, finish=0.7, body=0.05),
    dict(name="eye (line art)", shades=[4, 2, 1], finish=0.9, body=0),
]
def to(name, colors): return {c: name for c in colors}
CREAM, MASK, BEAK, LINE = "feathers, cream", "feathers, mask", "beak", "outline"
COLORS = {4: LINE, **to("feathers", [14, 13, 12, 11]), **to(CREAM, [10, 9, 8]),
          **to(BEAK, [7, 6, 5]), **to("claws and teeth", [3, 2, 1])}

EYES = {"front": (8, 8), "back": (11, 9)}      # where the eye drawings sit on the head
def head(view, rect, colors):
    """A rule for a region of the head, given once for the head and for the eye drawings laid over it."""
    ox, oy = EYES[view]
    return [dict(view=view, drawings=["atama1"], rect=rect, colors=colors),
            dict(view=view, drawings=["atama1-eyes-*"], rect=[rect[0]-ox, rect[1]-oy, rect[2], rect[3]], colors=colors)]

RULES = [
    # wings and tail are layers of feathers: the lines between them are creases
    dict(drawings=["hane*", "o"], thin_all={14: LINE, 13: LINE}),
    # the chest tuft is all cream; its streaks and contour are drawn in the browns
    dict(drawings=["mune"], colors=to(CREAM, [14, 13, 11])),
    # front body: the cream belly's contour down the left and along the bottom
    dict(view="front", drawings=["karada"], rect=[0, 12, 2, 12], colors=to(CREAM, [13])),
    dict(view="front", drawings=["karada"], rect=[0, 27, 24, 3], colors=to(CREAM, [13, 14])),
    # back body: the belly shows along the bottom and up the right side, in shade
    dict(view="back", drawings=["karada"], rect=[0, 14, 32, 8], colors=to(CREAM, [11, 13])),
    dict(view="back", drawings=["karada"], rect=[11, 21, 5, 1], colors=to(CREAM, [14])),
    # legs: bare skin; from behind the belly shows between them
    dict(drawings=["asi"], colors=to("dry hide, legs", [14, 13, 7, 6])),
    dict(view="back", drawings=["asi"], rect=[10, 4, 6, 5], colors=to(CREAM, [10, 11, 13, 14])),
    # front head
    *head("front", [7, 19, 1, 1], to(CREAM, [13])),                    # the throat's contour
    *head("front", [10, 10, 10, 9], to(MASK, [14])),
    *head("front", [3, 10, 7, 9], to(BEAK, [14])),
    *head("front", [4, 14, 3, 1], to(LINE, [14])),                     # the line between the two halves of the beak
    *head("front", [7, 15, 2, 1], to(LINE, [14])),
    dict(view="front", drawings=["atama1-eyes-open"], rect=[3, 4, 4, 2], colors=to("eye (line art)", [4, 1])),
    # back head: the cream tufts' and cheek's contours, the mask, the beak
    *head("back", [9, 4, 9, 8], to(CREAM, [13])),
    *head("back", [2, 6, 2, 3], to(CREAM, [13])),
    *head("back", [7, 8, 1, 1], to(CREAM, [13])),
    *head("back", [4, 9, 3, 1], to(CREAM, [13])),
    *head("back", [13, 14, 3, 8], to(CREAM, [13])),
    *head("back", [16, 19, 1, 1], to(CREAM, [14])),
    *head("back", [11, 11, 7, 3], to(MASK, [4, 14])),
    *head("back", [11, 14, 3, 5], to(MASK, [4, 14])),
    *head("back", [12, 18, 1, 1], to(MASK, [13])),
    *head("back", [17, 12, 4, 5], to(BEAK, [14])),
    *head("back", [18, 15, 2, 1], to(LINE, [14])),
    dict(view="back", drawings=["atama1-eyes-open"], rect=[3, 3, 4, 2], colors=to("eye (line art)", [4, 2, 1])),
    # eyes closed, from behind: the lid is a lighter line drawn on the mask
    dict(view="back", drawings=["atama1-eyes-closed"], rect=[0, 2, 6, 4], colors=to(MASK, [4, 14, 13])),
    dict(view="back", drawings=["atama1-eyes-closed"], rect=[6, 3, 1, 1], colors=to(MASK, [13])),
]
MARKS = [
    # short streaks of the light brown inside the cream: feather edges, the cream's own shade
    dict(drawings=["hane*", "karada", "asi"], color=11, on=[8, 9, 10, 13, 14, 4], to=CREAM, max=6, min=1),
]
