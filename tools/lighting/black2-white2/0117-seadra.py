# Seadra: a seahorse bristling with points. Blue skin, a cream belly of overlapping plates, two big spiked fins
# that are blue at the root and cream at the tips, and a cluster of spikes on each cheek (Black 2/White 2: "Its
# spines provide protection"; Silver: "Its fin-tips leak poison"). The painted art shades all of it flat and soft.
SOURCE = "sources/black2-white2/0117-seadra.spu"
# Palette: 2 3 4 5 6 the blue (6 its navy contour); 7 8 9 the cream of the belly and of the fins (9 their brown
# contour and the fins' rays); 15 white and 13 gray, the eyes only; 14 black.
BLUE, CREAM = [6, 5, 4, 3, 2], [9, 8, 7]
MATERIALS = [
    dict(name="outline", shades=[14], finish=0.1, body=0),
    # head, snout, body and tail. The points of the crest (on the head drawing, and the cluster behind it drawn as
    # its own piece) are painted as one flat surface with the head, with no line or highlight setting them apart:
    # they are its skin drawn out to points, not separate hard spines
    dict(name="fish skin", shades=BLUE, base=2, finish=0.15, body=0.08),
    # the cream belly: the same skin in another color; black lines part its overlapping plates
    dict(name="fish skin, belly", shades=CREAM, base=1, finish=0.15, body=0.08),
    # the pectoral fins ("wing-like pectoral fins", Red/Blue): thin skin, flat and soft in the art. Blue at the root
    dict(name="fin", shades=[6, 5, 4, 3], base=2, finish=0.3, body=0.15),
    # and cream toward the points
    dict(name="fin, tips", shades=CREAM, base=1, finish=0.3, body=0.15),
    dict(name="seams and wrinkles", shades=[], finish=0, body=0),   # closed eyelids: lines on the head, not creases
    dict(name="eye (line art)", shades=[14, 6, 13, 15], finish=0.9, body=0),
]
INNER = "seams and wrinkles"
def to(name, colors): return {c: name for c in colors}
def dots(view, drawing, points, colors):
    return [dict(view=view, drawings=[drawing], rect=[x, y, 1, 1], colors=colors) for x, y in points]
COLORS = {14: "outline", **to("fish skin", BLUE), **to("fish skin, belly", CREAM),
          **to("eye (line art)", [13, 15])}
LID, DARK = {6: "eye (line art)"}, {14: "eye (line art)"}
RULES = [
    dict(drawings=["wing-*", "*-wings01"], colors={**to("fin", [6, 5, 4, 3]), **to("fin, tips", CREAM)}),
    # front: the eye is only on the eyes drawing. White, a gray corner, the black lid and pupil, the navy rim
    dict(view="front", drawings=["head-eyes-open"], colors=DARK),
    dict(view="front", drawings=["head-eyes-open"], rect=[4, 2, 2, 5], colors=LID),
    # back: the eye is on the head and again on the eyes drawing, which sits 21 right, 9 down of the head's corner
    dict(view="back", drawings=["head01"], rect=[24, 10, 4, 6], colors=DARK),
    *dots("back", "head01", [(24, 10), (25, 11), (26, 12)], LID),
    dict(view="back", drawings=["head01-eyes-open"], colors=DARK),
    *dots("back", "head01-eyes-open", [(3, 1), (4, 2), (5, 3)], LID),
    dict(drawings=["head-eyes-closed", "head01-eyes-closed"], colors={14: INNER}),
]
