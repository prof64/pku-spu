# Sableye: a matte purple hide, and gems. Its eyes are cut gemstones (Black 2/White 2: "Its diet of gems has
# transformed its eyes into gemstones"), so they are a gem row, not line art, and they glow (Ruby: "their eyes
# burn with a sinister glow in the darkness"). The gems on its chest and back are the same crystal, no glow.
SOURCE = "sources/black2-white2/0302-sableye.spu"
HIDE = [1, 2, 3, 5, 6]
EYES = [8, 9, 10, 11]
MATERIALS = [
    # black, and the gray-blue (7) the eyes' facet edges are drawn in: edges between a cut gem's faces are
    # creases. As a shade of the gem they melted away under any light and the eye became a plain pale disc.
    dict(name="outline", shades=[15, 7], finish=0.1, body=0),
    # plain monster skin: the art paints one broad soft pale patch on the head and flat washes elsewhere, no
    # hard highlight. The slate contour (1) is its darkest shade. Fingers and toes end in points of the same
    # skin (the "sharp claws" are not drawn apart), so they are hide too.
    dict(name="hide", shades=HIDE, base=1, finish=0.25, body=0.08),
    # the eyes: cut gems, a white table among pale blue faces, teal in shade
    dict(name="gem, eyes", shades=EYES, base=2, finish=1, body=0.6),
    # chest gem, and the red one on the back
    dict(name="gem, red", shades=[12, 13, 14], base=1, finish=1, body=0.6),
    # the blue gem on the back (its edge shows past the right side from the front)
    dict(name="gem, blue", shades=[8, 9, 10], base=1, finish=1, body=0.6),
    # the small green gem low on the back: one green pixel and its teal shade
    dict(name="gem, green", shades=[8, 4], base=1, finish=1, body=0.6),
]
def to(name, colors): return {c: name for c in colors}
COLORS = {15: "outline", 7: "outline", **to("hide", HIDE), **to("gem, eyes", EYES), **to("gem, red", [12, 13, 14]),
          4: "gem, green"}
RULES = [
    dict(drawings=["body"], colors=to("gem, blue", [8, 9, 10])),
    # the teal pixel right under the green one
    dict(view="back", drawings=["body"], rect=[13, 11, 1, 2], colors={8: "gem, green", 4: "gem, green"}),
]
# the hide's palest purple is the lit patch on the head and the lit side of fingers and toes: a real shade.
# Left out of the row it stayed pale on a head and hands gone dark with the sun behind.
KEEP_TOP = ["hide"]
# Only the eyes give off light. Enough to burn in a cave and tint the face around them, not to light the cave;
# in daylight it hardly shows.
GLOW = [
    dict(material="gem, eyes", colors=[9, 10, 11], glow=80, intent="the eyes burn with a glow in the dark: their bright faces"),
    dict(material="gem, eyes", colors=[8], glow=30, intent="the eyes' faces in shade glow less"),
]
