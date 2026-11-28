# Horsea: a small seahorse. Smooth blue skin, a cream belly of plates, one thin cream fin on its back
# (Gold: "adeptly controlling its dorsal fin"), red eyes. The painted art shades all of it softly, with no highlight.
SOURCE = "sources/black2-white2/0116-horsea.spu"
# Palette: 4 5 6 7 the blue (7 its dark contour, 4 a few painted glints); 8 9 10 the cream of the belly and of the
# fin (10 their brown contour, the lines between belly plates and the fin's rays); 11 12 red, 13 white and
# 14 gray, the eyes only; 15 black.
BLUE, CREAM = [7, 6, 5, 4], [10, 9, 8]
MATERIALS = [
    dict(name="outline", shades=[15], finish=0.1, body=0),
    # the art paints the body a flat blue with soft broad shading and no highlight: matte, a trace of light through.
    # The three nubs on the head are the same skin (rounded and soft here; they are spines only on Seadra)
    dict(name="fish skin", shades=BLUE, base=1, finish=0.15, body=0.08),
    # the cream belly plates: the same skin in another color; the brown lines between plates are its darkest shade
    dict(name="fish skin, belly", shades=CREAM, base=2, finish=0.15, body=0.08),
    # the fin on its back: thin skin with rays, painted flat and soft
    dict(name="fin", shades=CREAM, base=1, finish=0.3, body=0.15),
    dict(name="seams and wrinkles", shades=[], finish=0, body=0),   # closed eyelids: lines on the head, not creases
    dict(name="eye (line art)", shades=[15, 7, 12, 11, 14, 13], finish=0.9, body=0),
]
INNER = "seams and wrinkles"
def to(name, colors): return {c: name for c in colors}
COLORS = {15: "outline", **to("fish skin", BLUE), **to("fish skin, belly", CREAM),
          **to("eye (line art)", [11, 12, 13, 14])}
RIM = {7: "eye (line art)", 15: "eye (line art)"}       # the dark blue ring drawn round the eye, and the pupil
PUPIL = {15: "eye (line art)"}
RULES = [
    dict(drawings=["wing"], colors=to("fin", CREAM)),
    # front: the near eye (ring, white, red iris, pupil) and the far eye at the head's left edge
    dict(view="front", drawings=["head"], rect=[9, 11, 6, 8], colors=RIM),
    dict(view="front", drawings=["head"], rect=[3, 10, 2, 4], colors=PUPIL),
    # the eyes drawing sits 1 right, 5 down of the head's corner
    dict(view="front", drawings=["head-eyes-open"], rect=[8, 6, 6, 8], colors=RIM),
    dict(view="front", drawings=["head-eyes-open"], rect=[2, 5, 2, 4], colors=PUPIL),
    # back: the eye bulges at the head's right edge
    dict(view="back", drawings=["head-eyes-open"], rect=[1, 0, 3, 6], colors=RIM),
    dict(drawings=["head-eyes-closed"], colors={15: INNER}),
]
# the pale blue on top of the head and on the nubs' tips is the skin's lightest shade: left out of the row it stayed
# a pale patch on a head gone dark with the sun behind, and went dull under the studio lamp
KEEP_TOP = ["fish skin"]
