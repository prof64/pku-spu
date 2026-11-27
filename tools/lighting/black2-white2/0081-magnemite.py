SOURCE = "sources/black2-white2/0081-magnemite.spu"
MATERIALS = [
    # black, and the softened gray line (5, 6) the art draws around the sphere on its lit sides
    dict(name="outline", shades=[15, 6, 5], finish=0.1, body=0),
    # "a single eye embedded in an iron sphere": polished steel, its pale highlight (11) kept so it can move
    dict(name="metal", shades=[14, 13, 12, 11], base=1, finish=0.9, body=-1),
    # the screw on top and the two cross-head screws in front: bright bare steel
    dict(name="metal, screws", shades=[5, 4, 3, 2, 1], base=1, finish=0.9, body=-1),
    # the horseshoe magnets: dark, duller metal; its contour (6) is its dark shade
    dict(name="metal, magnets", shades=[6, 5], base=1, finish=0.6, body=-1),
    # the painted poles are color on the same bars: the magnets' dials
    dict(name="metal, red pole", shades=[8], base=0, finish=0.6, body=-1),
    dict(name="metal, blue pole", shades=[10], base=0, finish=0.6, body=-1),
    dict(name="seams and wrinkles", shades=[], finish=0, body=0),   # the cross slot cut in a screw head
    dict(name="eye (line art)", shades=[15, 2, 1], finish=0.9, body=0),
]
INNER = "seams and wrinkles"
def to(name, colors): return {c: name for c in colors}
COLORS = {15: "outline", **to("metal", [14, 13, 12, 11]), **to("metal, screws", [4, 3, 2, 1]),
          **to("metal, magnets", [6, 5]), 8: "metal, red pole", 10: "metal, blue pole"}
RULES = [
    # the sphere: gray (5, 6) is its softened outline, except on the screw standing on top of it
    dict(view="front", drawings=["body"], colors=to("outline", [5, 6])),
    dict(view="front", drawings=["body"], rect=[3, 1, 8, 4], colors={5: "metal, screws"}),
    dict(view="front", drawings=["body"], rect=[3, 5, 3, 1], colors={5: "metal, screws"}),
    # from behind: the top screw, and the two front screws' heads showing past the sphere's edge
    dict(view="back", drawings=["head01"], colors={6: "outline", 5: "metal, screws"}),
    dict(view="back", drawings=["head01"], rect=[13, 9, 1, 1], colors={5: "outline"}),
    # a cross-head screw: its dark ring (5) is its contour shade; the slot is a cut in one flat head
    dict(drawings=["neji-r"], colors={5: "metal, screws"}, interior={15: ([5, 4, 3, 2], INNER)}),
    # the eye: white, its gray corners and the pupil
    dict(drawings=["body-eyes-*"], colors=to("eye (line art)", [1, 2, 15])),
]
