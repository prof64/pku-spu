# Ditto: one soft body. No entry says what it is made of, only that it is cells it can rearrange
# ("It can reconstitute its entire cellular structure", Black 2/White 2). The painted art shades it flat
# and soft, with a small pale dot of light on top of each bump: smooth, a faint sheen, opaque, not wet.
SOURCE = "sources/black2-white2/0132-ditto.spu"
# smooth soft skin: the dials of Frog skin ("smooth, a faint sheen, not wet")
SOFT = dict(finish=0.3, body=0.1)
MATERIALS = [
    # black; and the dark purple line on the lit side. The palette has no step between that purple and
    # the body's shadow color: as the body's darkest shade it put a dark blotch on the back in a cave.
    dict(name="outline", shades=[1, 7], finish=0.1, body=0),
    # the body: its shadow color (6), the step between (5), the lit color (4). Base is the shadow color:
    # the back view is painted almost wholly in it, and it outweighs the lit color over both views.
    dict(name="soft body", shades=[6, 5, 4], base=0, **SOFT),
    # the pale patch of light painted on top of each bump. Its two colors are rare: in the body's row they
    # would spread in pale patches under a lamp, and left as painted they stayed pale on a body gone dark.
    # As their own row, one step up the body's colors, they darken with the body.
    dict(name="soft body, highlight", shades=[4, 3, 2], base=1, **SOFT),
    dict(name="eye (line art)", shades=[1], finish=0.9, body=0),
]
def to(name, colors): return {c: name for c in colors}
COLORS = {1: "outline", 7: "outline", **to("soft body", [6, 5, 4]), **to("soft body, highlight", [3, 2])}
RULES = [
    # the eyes: one black pixel each; shut, a short line (outline). The mouth (the drawing named "eye")
    # is a drawn line too, its soft ends in the body's shadow color.
    dict(drawings=["eye2", "eye2-eyes-open"], colors={1: "eye (line art)"}),
]
