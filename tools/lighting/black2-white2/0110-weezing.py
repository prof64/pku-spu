# Weezing: two thin, matte balloons of skin (and a third small lump) full of gas, and loose puffs of the
# gas around them. Koffing's skin: "Toxic gas is held within its thin, balloon-shaped body" (Koffing,
# Black 2/White 2); "WEEZING alternately shrinks and inflates its twin bodies to mix together toxic
# gases inside" (Sapphire).
SOURCE = "sources/black2-white2/0110-weezing.spu"
# Gas (the standard row, as on Gastly): soft and frosted, so light blurs through it; not clear glass
GAS = dict(finish=-0.5, body=0.75)
# The balloons, as on Koffing: the painted art shades them softly with no highlight anywhere, so matte;
# thin, so as much light through as skin may have (0.15) and no more: they are drawn opaque.
SKIN = dict(finish=0.15, body=0.15)
BALLOON = [14, 13, 12, 11, 10]
MATERIALS = [
    # black: the line around each ball, its craters and nubs, the brow furrows, the lines between teeth
    dict(name="outline", shades=[15], finish=0.1, body=0),
    # dark contour (14), nearly all of the back and the front's shaded side (13), the front's mid tone
    # (12), its lit bulk (11), the pale patches on both crowns (10)
    dict(name="balloon skin", shades=BALLOON, base=1, **SKIN),
    # the cream rings low on both heads (the skull mark, seen from above): pigment in the same skin
    dict(name="balloon skin, skull mark", shades=[3, 4], base=1, **SKIN),
    # the puffs. Smeargle gives a row named gas no shape (it stays facing the viewer), so a puff's three
    # yellows cannot be one row's shades: one row for each, the same dials (as on Gastly's cloud)
    dict(name="gas", shades=[8], base=0, **GAS),
    dict(name="gas, pale middle", shades=[7], base=0, **GAS),
    dict(name="gas, dark rim", shades=[9], base=0, **GAS),
    # the big head's row of teeth and the small head's two fangs
    dict(name="claws and teeth", shades=[2, 1], base=1, finish=0.7, body=0.05),
    dict(name="mouth", shades=[6, 5], base=0, finish=0.8, body=0),
    # the black lines of the shut eyes: tinted, never a crease
    dict(name="seams and wrinkles", shades=[], finish=0, body=0),
    # whites, their gray shade and the two-pixel pupils
    dict(name="eye (line art)", shades=[15, 2, 1], finish=0.9, body=0),
]
INNER = "seams and wrinkles"
def to(name, colors): return {c: name for c in colors}
COLORS = {15: "outline", **to("balloon skin", BALLOON), **to("balloon skin, skull mark", [3, 4]),
          8: "gas", 7: "gas, pale middle", 9: "gas, dark rim",
          **to("claws and teeth", [2, 1]), **to("mouth", [6, 5])}
EYE = to("eye (line art)", [15, 2, 1])
RULES = [
    # the open-eyes overlays draw nothing white or black but the eyes
    dict(drawings=["atama1-eyes-open", "atama3-eyes-open"], colors=EYE),
    # the small head's eyes as drawn on the head itself; its other whites are its two fangs
    dict(view="front", drawings=["atama3"], rect=[22, 13, 4, 3], colors=EYE),
    dict(view="front", drawings=["atama3"], rect=[11, 16, 6, 4], colors=EYE),
    # every black stroke of the shut-eyes overlays is a lid line lying on the ball: a line on it, not a crease
    dict(drawings=["atama1-eyes-closed", "atama3-eyes-closed"], colors={15: INNER}),
]
