# Magneton: three Magnemite, so Magnemite's rows and dials. The art here paints the magnets darker (mostly 6,
# with pale streaks 5 and 4), the poles in two shades each, and a white four-point sparkle (1) on two spheres.
SOURCE = "sources/black2-white2/0082-magneton.spu"
MATERIALS = [
    # black, and the softened gray line (5, 6) the back view draws around each sphere
    dict(name="outline", shades=[15, 6, 5], finish=0.1, body=0),
    # "three Magnemite linked": Magnemite's polished steel spheres
    dict(name="metal", shades=[14, 13, 12, 11], base=1, finish=0.9, body=-1),
    # the white four-point sparkle (1) painted on two spheres: the same steel in its own row, so it dims to the
    # sphere's pale green in the dark. As the spheres' top shade it turned them white all over under a lamp
    dict(name="metal, sparkle", shades=[11, 1], base=1, finish=0.9, body=-1),
    # the screw on top of each sphere and the cross-head screws in front: bright bare steel
    dict(name="metal, screws", shades=[6, 5, 4, 3, 2, 1], base=2, finish=0.9, body=-1),
    # the horseshoe magnets: dark, duller metal, painted mostly in its darkest gray with pale streaks
    dict(name="metal, magnets", shades=[6, 5, 4], base=0, finish=0.6, body=-1),
    # the painted poles are color on the same bars: the magnets' dials. Each is drawn as a lit face (7, 9) and a
    # darker side (8, 10); the lit face is the base
    dict(name="metal, red pole", shades=[8, 7], base=1, finish=0.6, body=-1),
    dict(name="metal, blue pole", shades=[10, 9], base=1, finish=0.6, body=-1),
    dict(name="seams and wrinkles", shades=[], finish=0, body=0),   # a screw head's cross slot, a screw's thread
    dict(name="eye (line art)", shades=[15, 2, 1], finish=0.9, body=0),
]
INNER = "seams and wrinkles"
def to(name, colors): return {c: name for c in colors}
COLORS = {15: "outline", **to("metal", [14, 13, 12, 11]), **to("metal, screws", [3, 2, 1]),
          **to("metal, magnets", [6, 5, 4]), **to("metal, red pole", [8, 7]), **to("metal, blue pole", [10, 9])}
EYE = to("eye (line art)", [1, 2, 15])
SCREW = to("metal, screws", [6, 5, 4])
def rects(drawing, view, colors, *rs): return [dict(view=view, drawings=[drawing], rect=r, colors=colors) for r in rs]
RULES = [
    # one pale pixel at the end of the top magnet's streak
    dict(view="front", drawings=["h"], colors={3: "metal, magnets"}),
    # front: every gray on a sphere drawing is a screw; a slot or thread drawn in black inside one is a cut, not a crease
    dict(view="front", drawings=["body?b"], colors=SCREW, interior={15: ([6, 5, 4, 3, 2, 1], INNER)}),
    # the white sparkle painted on two of the spheres
    *rects("body2b", "front", {1: "metal, sparkle"}, [4, 6, 5, 5]),
    *rects("body4b", "front", {1: "metal, sparkle"}, [9, 7, 5, 5]),
    # the eyes: white, gray corners and the pupil
    *rects("body3b", "front", EYE, [8, 12, 7, 7]),
    *rects("body2b", "front", EYE, [5, 12, 7, 7]),
    *rects("body4b", "front", EYE, [10, 13, 7, 7]),
    dict(drawings=["body*-eyes-*"], colors=EYE),
    # back: gray (5, 6) is the softened outline of a sphere, except the screw standing on top of one
    dict(view="back", drawings=["body", "body-2", "body-3"], colors=to("outline", [5, 6])),
    *rects("body-2", "back", SCREW, [7, 4, 7, 6]),
    dict(view="back", drawings=["b3-neji"], colors=SCREW),
]
