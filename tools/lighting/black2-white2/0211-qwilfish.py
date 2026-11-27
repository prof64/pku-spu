SOURCE = "sources/black2-white2/0211-qwilfish.spu"
# Palette: 1 black; 4 5 6 7 the teal back; 8 9 10 11 the cream belly (8 its brown contour); 12 13 14 the lips;
# 15 white and 3 pale gray, the eyes only. The same teal and cream ramps also draw the spines that grow out of
# each, and the tail fin (teal rim and ovals, pale patch in the belly's two middle colors).
TEAL, CREAM = [4, 5, 6, 7], [8, 9, 10, 11]
MATERIALS = [
    # black, and the dark strokes where a spine overlaps the body behind it or the two lips meet
    dict(name="outline", shades=[1, 4, 8, 12], finish=0.1, body=0),
    # the art paints the back a flat teal with soft broad shading and no highlight: matte, a trace of light through
    dict(name="fish skin", shades=TEAL, base=1, finish=0.15, body=0.08),
    dict(name="fish skin, belly", shades=CREAM, base=1, finish=0.15, body=0.08),
    dict(name="fish skin, tail patch", shades=[9, 10], base=0, finish=0.15, body=0.08),
    dict(name="fish skin, lips", shades=[12, 13, 14], base=1, finish=0.25, body=0.08),
    # "The small spikes covering its body developed from scales": hard, part of the hide, hide-colored
    dict(name="spines", shades=TEAL, base=2, finish=0.4, body=0),
    dict(name="spines, belly", shades=CREAM, base=1, finish=0.4, body=0),
    dict(name="seams and wrinkles", shades=[], finish=0, body=0),   # closed eyelids: lines on the one ball, not creases
    dict(name="eye (line art)", shades=[1, 4, 3, 15], finish=0.9, body=0),
]
INNER = "seams and wrinkles"
def to(name, colors): return {c: name for c in colors}
def box(view, drawing, x0, y0, x1, y1, colors):      # corners included
    return dict(view=view, drawings=[drawing], rect=[x0, y0, x1 - x0 + 1, y1 - y0 + 1], colors=colors)
def dots(view, drawing, points, colors):
    return [dict(view=view, drawings=[drawing], rect=[x, y, 1, 1], colors=colors) for x, y in points]
COLORS = {1: "outline", **to("fish skin", TEAL), **to("fish skin, belly", CREAM), **to("fish skin, lips", [12, 13, 14])}
SPINE, BSPINE, LINE = to("spines", TEAL), to("spines, belly", CREAM), {4: "outline", 8: "outline", 12: "outline"}
EYE = to("eye (line art)", [1, 4, 3, 15])
F, B, H = "front", "back", "head01"
RULES = [
    # the tail fin: its pale patch is painted in the belly's colors
    dict(drawings=["tail01"], colors=to("fish skin, tail patch", [9, 10])),
    # the line where the two lips meet
    *dots(F, "mouth01", [(6, 7), (7, 7), (8, 8)], LINE),

    # front, teal spines: two on top, two on the right shoulder, two on the left, one on the right flank
    box(F, H, 11, 6, 14, 9, SPINE), box(F, H, 19, 4, 22, 9, SPINE), *dots(F, H, [(18, 9), (22, 10)], LINE),
    box(F, H, 23, 9, 28, 10, SPINE), box(F, H, 27, 11, 28, 11, SPINE), box(F, H, 29, 9, 34, 12, SPINE),
    box(F, H, 5, 10, 8, 13, SPINE), box(F, H, 3, 20, 5, 22, SPINE), box(F, H, 33, 19, 38, 22, SPINE),
    # front, belly spines: left (two), middle, right, and two underneath
    box(F, H, 5, 25, 7, 27, BSPINE), box(F, H, 8, 25, 10, 28, BSPINE),
    *dots(F, H, [(23, 25), (23, 26), (24, 26), (22, 27), (23, 27), (24, 27), (24, 28)], BSPINE),
    *dots(F, H, [(24, 24), (24, 25), (25, 26), (25, 27), (25, 28), (21, 27), (22, 28), (23, 28), (24, 29), (25, 29)], {8: INNER, 1: INNER}),
    box(F, H, 29, 26, 33, 28, BSPINE), box(F, H, 14, 33, 16, 35, BSPINE), box(F, H, 25, 32, 28, 34, BSPINE),
    # the eyes, drawn on the head and again on the eyes drawing: white, gray, pupil and the dark teal rim
    box(F, H, 8, 13, 11, 16, EYE), box(F, H, 19, 12, 23, 15, EYE),
    dict(drawings=["head01-eyes-open"], colors=EYE),
    dict(drawings=["head01-eyes-closed"], colors={1: INNER}),

    # back, teal spines: left shoulder, two on top, right shoulder (two), left flank, and one pointing at the viewer.
    # That one sits in the middle of the back: its dark ring and black underside are lines on the one ball, not
    # creases (as creases the back was lit like a ring around it). The same for the belly spine that points at
    # the viewer in the front view.
    box(B, H, 6, 8, 9, 11, SPINE), *dots(B, H, [(10, 10), (9, 11)], LINE),
    box(B, H, 15, 5, 17, 6, SPINE),
    box(B, H, 21, 4, 24, 7, SPINE), *dots(B, H, [(24, 8), (25, 8), (24, 9), (25, 9)], SPINE),
    *dots(B, H, [(23, 8), (23, 9), (25, 10), (26, 9)], LINE),
    *dots(B, H, [(28, 7), (28, 8), (27, 9), (28, 9), (29, 10), (29, 11), (29, 12), (30, 12)], SPINE), *dots(B, H, [(28, 10)], LINE),
    box(B, H, 3, 19, 7, 20, SPINE), box(B, H, 5, 21, 6, 21, SPINE),
    box(B, H, 19, 20, 21, 22, SPINE), *dots(B, H, [(19, 19), (20, 19), (21, 19), (18, 20), (22, 20), (18, 21)], {4: INNER}), box(B, H, 18, 21, 22, 23, {1: INNER}),
    # back, belly spines: right (one lit, one in shadow under it) and two underneath
    box(B, H, 33, 23, 34, 25, BSPINE), box(B, H, 30, 26, 32, 26, BSPINE),
    box(B, H, 10, 29, 12, 33, BSPINE), box(B, H, 24, 30, 27, 32, BSPINE),
]
