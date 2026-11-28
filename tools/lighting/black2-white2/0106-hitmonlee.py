# Hitmonlee: bare brown skin (Hide) all over; the cream ringed stretches of its arms and legs ("springlike legs",
# "elastic legs") are that same skin in another color, ring over ring; a yellow pad on each heel; white toe claws.
SOURCE = "sources/black2-white2/0106-hitmonlee.spu"
H = dict(finish=0.25, body=0.08)          # Hide: plain bare skin (the painted art shades it flat, no highlight)
BAND = [11, 10, 9]
MATERIALS = [
    # black; the olive-brown strokes (11) between the rings of a limb and along a few skin edges; and the
    # dark brown (5) where it closes the end of a ringed stretch
    dict(name="outline", shades=[15, 11, 5], finish=0.1, body=0),
    # the skin: its dark brown contours (5, 4) are its darkest shades
    dict(name="hide", shades=[5, 4, 3, 2], base=2, **H),
    # the palest patches (1) on top of the head, the fist and the back-view toes: the same skin at its most lit.
    # In their own row so they go dark with the body instead of staying pale as painted glints
    dict(name="hide, lit patches", shades=[5, 4, 3, 2, 1], base=2, **H),
    # the cream ringed stretches of the wrists and legs: the same skin, paler
    dict(name="hide, limb bands", shades=BAND, base=1, **H),
    # the yellow pad on each heel, with its olive rim
    dict(name="hide, heel pads", shades=[14, 13, 12], base=2, **H),
    dict(name="claws and teeth", shades=[8, 7, 6], base=1, finish=0.7, body=0.05),
    dict(name="eye (line art)", shades=[8, 7, 6], finish=0.9, body=0),
]
def to(name, colors): return {c: name for c in colors}
COLORS = {15: "outline", **to("hide", [5, 4, 3, 2]), 1: "hide, lit patches", **to("hide, limb bands", BAND),
          **to("hide, heel pads", [14, 13, 12]), **to("claws and teeth", [8, 7, 6])}
RULES = [
    # the rings of a limb lie one over the next: the lines between them are creases. The same olive-brown
    # also draws a few skin edges (thigh, arm, the body's lower tip): lines there too
    dict(thin_all={11: "outline"}),
    # ringed stretches drawn alone: a dark brown pixel there closes the end of the stretch
    dict(drawings=["asi01", "asi02", "asi04", "l-foot2"], colors={5: "outline"}),
    dict(view="back", drawings=["r-hand"], rect=[0, 0, 24, 12], colors={5: "outline"}),
    # the eyes share the claws' white and grays
    dict(drawings=["atama", "atama-eyes-*"], colors=to("eye (line art)", [8, 7, 6])),
]
