SOURCE = "sources/black2-white2/0208-steelix.spu"
# Steelix: steel all over (head, jaw, every body ball and its prongs, the tail), white teeth, a red eye
# in a black socket. "The many small metal particles that cover this POKeMON's body reflect bright light
# well" (Crystal); the painted art gives every ball and the snout a hard pale band over a dark underside.
STEEL = [4, 5, 6, 7, 8]
METAL, TEETH, INNER, EYE = "metal", "claws and teeth", "seams and wrinkles", "eye (line art)"
MATERIALS = [
    dict(name="outline", shades=[14], finish=0.1, body=0),
    # the dark slate (4) is the steel's own darkest shade: broad shadow fills in the back view and the
    # soft contour on lit edges (it turns brown with the gold in the shiny palette). Base is the blue (5),
    # by far the most painted shade with both views together
    dict(name=METAL, shades=STEEL, base=1, finish=0.9, body=-1),
    # the square teeth: white, the ones further back in the mouth in the pale gray
    dict(name=TEETH, shades=[7, 15], base=1, finish=0.7, body=0.05),
    dict(name=INNER, shades=[], finish=0, body=0),   # facet edges drawn in black inside one piece of steel
    dict(name=EYE, shades=[14, 4, 13, 6, 7, 8], finish=0.9, body=0),
]
def to(name, colors): return {c: name for c in colors}
COLORS = {14: "outline", **to(METAL, STEEL), 15: TEETH, 13: EYE}
def rects(view, drawings, rs, colors):
    return [dict(view=view, drawings=drawings, rect=r, colors=colors) for r in rs]
HEADS_F, HEADS_B = ["head-a", "head-a-female"], ["atama", "atama-female"]
RULES = [
    # facet edges and ridges drawn in black wholly inside one piece of steel: lines on it, not creases
    dict(interior={14: (STEEL, INNER)}),
    # front: the black eye socket under the brow, and the brow line running up from it
    *rects("front", HEADS_F, [[25, 23, 14, 11]], {14: EYE}),
    # front: the teeth in shade (the white ones are the only use of color 15)
    *rects("front", HEADS_F, [[17, 40, 11, 1], [20, 41, 7, 1]], {7: TEETH}),
    # front, eyes open: the socket and slit pupil, and the eye's white wedge, shaded in the steel's grays
    dict(view="front", drawings=["head-a*-eyes-*"], colors={14: EYE}),
    *rects("front", ["head-a*-eyes-open"], [[8, 1, 2, 1], [7, 2, 3, 1], [6, 3, 4, 2], [7, 5, 1, 1]], to(EYE, STEEL)),
    # front, eyes closed: the lid is steel; the dark lines that draw it stay lines
    *rects("front", ["head-a*-eyes-closed"], [[4, 3, 4, 4]], {4: EYE}),
    # back: brow, socket, the white and its dark corner
    *rects("back", HEADS_B, [[40, 7, 10, 4]], {14: EYE}),
    *rects("back", HEADS_B, [[44, 8, 3, 1], [45, 9, 1, 1]], to(EYE, STEEL)),
    *rects("back", ["atama*-eyes-*"], [[4, 7, 10, 4]], {14: EYE}),
    *rects("back", ["atama*-eyes-open"], [[8, 8, 3, 1], [9, 9, 1, 1]], to(EYE, STEEL)),
]
