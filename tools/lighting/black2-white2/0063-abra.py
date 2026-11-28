SOURCE = "sources/black2-white2/0063-abra.spu"
MATERIALS = [
    # black: the line, the shut eyes, and the black skin at the neck and between the joints;
    # the browns where they are drawn line (eye-line ends, nostril, the edge of the ear, contours of limbs and plates)
    dict(name="outline", shades=[15, 7, 14, 6, 13, 5], finish=0.1, body=0),
    # the yellow coat: its brown contour colors are its darkest shades; the pale forehead patch is a painted highlight
    dict(name="short fur", shades=[14, 13, 12, 11, 10, 9], base=3, finish=-0.2, body=0.05),
    # the pale muzzle and the insides of the ears
    dict(name="short fur, muzzle and ear insides", shades=[10, 9], base=1, finish=-0.2, body=0.05),
    # the brown band around the tail, flush with the tail
    dict(name="short fur, tail band", shades=[6, 5], base=1, finish=-0.2, body=0.05),
    # the brown shoulder pieces and the piece around the chest: dry plates standing off the body
    dict(name="plated hide", shades=[7, 6, 5], base=2, finish=0.2, body=0.03),
]
def to(name, colors): return {c: name for c in colors}
COLORS = {15: "outline", **to("short fur", [14, 13, 12, 11, 10, 9]), **to("plated hide", [7, 6, 5])}
LINE = to("outline", [7, 6, 5])
def rects(drawing, view, colors, *boxes):
    return [dict(view=view, drawings=[drawing], rect=list(b), colors=colors) for b in boxes]
RULES = [
    # limbs: the plates' browns are only their contour on the shadow side and the lines between fingers and folds
    dict(drawings=["te0*", "asi*", "?-arm01", "?-leg01"], colors=LINE),
    # the head: brown is drawn line (the softened ends of the shut eyes, the nostril, the dotted edge of the ear)
    dict(view="front", drawings=["atama"], colors=LINE),
    *rects("atama", "front", {13: "outline"}, [20, 15, 1, 1], [15, 17, 1, 1]),
    *rects("atama", "front", {9: "short fur, muzzle and ear insides"}, [10, 19, 5, 3], [24, 7, 4, 5], [8, 4, 2, 3]),
    dict(view="back", drawings=["head01"], colors=LINE),
    # the body: a contour of the hand, and plate contours drawn in the coat's darkest brown
    *rects("karada", "front", LINE, [3, 15, 2, 1]),
    *rects("karada", "front", {14: "outline"}, [10, 5, 1, 1], [23, 3, 1, 1], [23, 8, 1, 1]),
    dict(view="back", drawings=["body01", "body02"], colors={14: "outline"}),
    *rects("body01", "back", LINE, [7, 19, 1, 2], [8, 5, 1, 1], [14, 5, 1, 1]),
    *rects("body02", "back", LINE, [11, 2, 1, 1], [17, 2, 1, 1]),
    # the tail band
    dict(drawings=["o2", "tail02"], colors=to("short fur, tail band", [6, 5])),
]
# the pale patch on the forehead and the belly is the coat's own top shade: left out, it stayed pale on a body gone dark
KEEP_TOP = ["short fur"]
