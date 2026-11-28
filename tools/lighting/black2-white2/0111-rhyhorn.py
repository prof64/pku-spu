SOURCE = "sources/black2-white2/0111-rhyhorn.spu"
HIDE = [5, 4, 3, 2]
MATERIALS = [
    # black: the silhouette, the lines where one plate lies over the next, and the dark gaps under the plates
    dict(name="outline", shades=[14], finish=0.1, body=0),
    # every gray plate: a thick hide in armor plates, dry and matte with a soft pale face on each (the same kind
    # and dials as Sandshrew's). The dark grays (5, 4) are its contour on the lit side, the bevel lines along the
    # plate edges and the shadowed underside; base is the mid gray (3)
    dict(name="plated hide", shades=HIDE, base=2, finish=0.2, body=0.03),
    # the near-white (1) the art paints along the lit edges of the frill and the plates: the same hide at its most
    # lit. In their own row so they darken with the plate; left as painted glints they stayed white on a body in
    # shade (the same reason as Onix's snout)
    dict(name="plated hide, edge light", shades=HIDE + [1], base=2, finish=0.2, body=0.03),
    # the nose horn: hard and hide-colored, painted the palest part of the head
    dict(name="spines, horn", shades=[5, 4, 3, 2, 1], base=4, finish=0.4, body=0),
    # white claws and the fang; in shade the art paints them off-white (1), and on the far hind leg light gray (2, 3)
    dict(name="claws and teeth", shades=[3, 2, 1, 15], base=3, finish=0.7, body=0.05),
    dict(name="eye (line art)", shades=[14, 6, 15], finish=0.9, body=0),
]
def to(name, colors): return {c: name for c in colors}
COLORS = {14: "outline", **to("plated hide", HIDE), 1: "plated hide, edge light", 15: "claws and teeth", 6: "eye (line art)"}
CLAW = to("claws and teeth", [1, 2, 3])
HORN = to("spines, horn", [5, 4, 3, 2, 1])
def horn(view, drawing, *rects): return [dict(view=view, drawings=[drawing], rect=r, colors=HORN) for r in rects]
RULES = [
    # the horn, from its tip to where it meets the snout (shorter on the female)
    *horn("front", "head01", [2, 17, 1, 1], [2, 18, 3, 1], [2, 19, 5, 1], [3, 20, 6, 1], [3, 21, 7, 1], [4, 22, 6, 1]),
    *horn("front", "head01-female", [3, 19, 3, 1], [3, 20, 5, 1], [3, 21, 6, 1], [5, 22, 4, 1]),
    *horn("back", "head01", [43, 17, 2, 1], [41, 18, 4, 1], [39, 19, 6, 1], [37, 20, 7, 1], [38, 21, 6, 1]),
    *horn("back", "head01-female", [41, 19, 3, 1], [38, 20, 6, 1], [38, 21, 6, 1]),
    # the eye: white, red iris and the black pupil (the other black in the front picture is the snout plate's edge)
    dict(drawings=["head01*-eyes-open"], colors={15: "eye (line art)", 6: "eye (line art)"}),
    dict(view="front", drawings=["head01*-eyes-open"], rect=[3, 5, 1, 1], colors={14: "eye (line art)"}),
    dict(view="back", drawings=["head01*-eyes-open"], colors={14: "eye (line art)"}),
    # claws in shade: the near forefoot's outer claw, one pixel of the off forefoot's, the far hind foot's two
    dict(view="front", drawings=["pl-foot01"], rect=[2, 10, 3, 3], colors=CLAW),
    dict(view="front", drawings=["pr-leg01"], rect=[18, 19, 1, 1], colors=CLAW),
    dict(view="front", drawings=["bl-leg01"], rect=[20, 27, 2, 3], colors=CLAW),
    dict(view="front", drawings=["bl-leg01"], rect=[25, 27, 2, 3], colors=CLAW),
]
