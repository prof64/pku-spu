SOURCE = "sources/black2-white2/0332-cacturne.spu"
MATERIALS = [
    # black; and the body's dark olive (3, 4) where it is drawn as the edge of the hat
    dict(name="outline", shades=[1, 3, 4], finish=0.1, body=0),
    # cactus flesh: body, arms, legs, feet, face and neck. A thick trunk: less light through than a bulb
    # (at 0.25 the whole sprite went khaki with the sun behind it)
    dict(name="plant body", shades=[3, 4, 5, 6, 7, 8], base=2, finish=0.1, body=0.15),
    # the hat: the same flesh, dark green and thin; its pale ridge line and brim glint (6, 7) stay as painted
    dict(name="plant body, hat", shades=[9, 10, 11, 12], base=1, finish=0.1, body=0.25),
    # the rhombus marks down the neck and chest (bigger on the female): pigment in the flesh
    dict(name="plant body, diamonds", shades=[9, 10, 12], base=1, finish=0.1, body=0.15),
    # thorns on the shoulders, arms, sides and legs: hard and solid; the art paints them in flat facets
    dict(name="spines", shades=[9, 10, 12, 6, 7], base=1, finish=0.15, body=0),
    dict(name="seams and wrinkles", shades=[], finish=0, body=0),   # the line down the back: tinted, never a crease
    dict(name="eye (line art)", shades=[2, 13, 14], finish=0.9, body=0),
]
INNER = "seams and wrinkles"
def to(name, colors): return {c: name for c in colors}
HAT = to("plant body, hat", [9, 10, 11, 12])
DIAMOND = to("plant body, diamonds", [9, 10, 12])
COLORS = {1: "outline", **to("plant body", [3, 4, 5, 6, 7, 8]), **to("spines", [9, 10, 11, 12]),
          **to("eye (line art)", [2, 13, 14])}
LIMBS = ["body*", "lhand", "rhand", "lfoot*", "rfoot*"]
RULES = [
    # --- head: the dark greens are the hat
    dict(drawings=["head", "head-eyes-*"], colors=HAT),
    # front: above the face everything is hat; its pale ridge and brim glint, and its olive edge pixels
    dict(view="front", drawings=["head"], rect=[0, 0, 48, 25],
         colors={6: "plant body, hat", 7: "plant body, hat", 3: "outline", 4: "outline"}),
    dict(view="front", drawings=["head"], rect=[19, 25, 5, 1], colors={6: "plant body, hat", 3: "outline"}),
    dict(view="front", drawings=["head"], rect=[17, 28, 1, 1], colors={3: "outline"}),   # edge of the flap over the face
    dict(view="front", drawings=["head-eyes-*"], rect=[0, 0, 16, 2], colors={3: "outline"}),
    # back: the hat's olive edge; below it the neck's own contour stays flesh
    dict(view="back", drawings=["head"], rect=[0, 0, 48, 24], colors={3: "outline"}),
    dict(view="back", drawings=["head"], rect=[32, 24, 16, 2], colors={3: "outline"}),
    # --- the rhombus marks: neck (both views) and chest
    dict(view="front", drawings=["body", "body-female"], rect=[21, 3, 3, 3], colors=DIAMOND),
    dict(view="front", drawings=["body", "body-female"], rect=[13, 6, 16, 19], colors=DIAMOND),
    dict(view="back", drawings=["body"], rect=[19, 3, 3, 4], colors=DIAMOND),
    # --- thorns: the pale green on a limb is a thorn's lit facet
    dict(drawings=LIMBS, colors={6: "spines"}),
    dict(view="front", drawings=["lhand"], rect=[18, 11, 1, 1], colors={6: "plant body"}),
    dict(view="front", drawings=["body", "body-female"], rect=[18, 4, 1, 1], colors={7: "spines"}),
    dict(view="front", drawings=["rhand"], rect=[23, 2, 1, 1], colors={7: "spines"}),
    dict(view="front", drawings=["rhand"], rect=[22, 3, 1, 1], colors={7: "spines"}),
    dict(view="front", drawings=["rhand"], rect=[27, 6, 2, 1], colors={7: "spines"}),
    dict(view="front", drawings=["rhand"], rect=[26, 7, 1, 1], colors={7: "spines"}),
    dict(view="back", drawings=["lfootb-2"], rect=[21, 2, 1, 1], colors={7: "spines"}),
    dict(view="back", drawings=["lfootb-2"], rect=[20, 3, 1, 1], colors={7: "spines"}),
    dict(view="back", drawings=["lfootb-2"], rect=[27, 6, 1, 1], colors={7: "spines"}),
    dict(view="back", drawings=["lfootb-2"], rect=[26, 7, 1, 1], colors={7: "spines"}),
    dict(view="back", drawings=["lfootb-2"], rect=[25, 8, 1, 1], colors={7: "spines"}),
    # --- the line drawn down the middle of the back: a line on one surface
    dict(view="back", drawings=["body"], interior={3: ([4, 5, 7], INNER)}),
]
# the pale chest is a broad painted shade of the front view, not a glint: left out of the row it stayed
# a pale disc while the body around it went dark
KEEP_TOP = ["plant body"]
