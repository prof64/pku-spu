# Koffing: a thin, matte balloon of skin full of gas, and loose puffs of the gas around it.
# "Toxic gas is held within its thin, balloon-shaped body" (Black 2/White 2); "Its thin, filmy body is
# filled with gases" (Gold); "observe, through its thin skin, the toxic gases swirling inside" (Emerald).
SOURCE = "sources/black2-white2/0109-koffing.spu"
# Gas (the standard row, as on Gastly): soft and frosted, so light blurs through it; not clear glass
GAS = dict(finish=-0.5, body=0.75)
# The balloon. The painted art shades it softly with no highlight anywhere, so it is matte; it is thin
# (the Pokedex says so three times), so it lets through as much light as skin may (0.15) and no more:
# the art, the 3D model and the sprite all draw it opaque.
SKIN = dict(finish=0.15, body=0.15)
MATERIALS = [
    # black: the line around the ball, its craters and nubs
    dict(name="outline", shades=[15], finish=0.1, body=0),
    # dark contour (14), the body's shaded lower half and most of the back (13), the lit upper half (12),
    # the pale crown (11)
    dict(name="balloon skin", shades=[14, 13, 12, 11], base=1, **SKIN),
    # the cream skull and crossbones: pigment in the same skin
    dict(name="balloon skin, skull mark", shades=[4, 3], base=0, **SKIN),
    # the puffs. Smeargle gives a row named gas no shape (it stays facing the viewer), so a puff's three
    # yellows cannot be one row's shades: one row for each, the same dials (as on Gastly's cloud)
    dict(name="gas", shades=[9], base=0, **GAS),
    dict(name="gas, pale middle", shades=[8], base=0, **GAS),
    dict(name="gas, dark rim", shades=[10], base=0, **GAS),
    dict(name="claws and teeth", shades=[2, 1], base=1, finish=0.7, body=0.05),
    dict(name="mouth", shades=[6, 5], base=1, finish=0.8, body=0),
    # the black lines of the shut eyes: tinted, never a crease
    dict(name="seams and wrinkles", shades=[], finish=0, body=0),
    # whites, their gray shade and the one-pixel pupils
    dict(name="eye (line art)", shades=[15, 2, 1], finish=0.9, body=0),
]
INNER = "seams and wrinkles"
def to(name, colors): return {c: name for c in colors}
BALLOON = [14, 13, 12, 11]
COLORS = {15: "outline", **to("balloon skin", BALLOON), **to("balloon skin, skull mark", [4, 3]),
          9: "gas", 8: "gas, pale middle", 10: "gas, dark rim",
          **to("claws and teeth", [2, 1]), **to("mouth", [6, 5])}
EYE = to("eye (line art)", [15, 2, 1])
RULES = [
    # the eyes drawn on the head and on its open-eyes overlay; the only black inside these is the pupils
    dict(view="front", drawings=["atama"], rect=[11, 10, 17, 3], colors=EYE),
    dict(drawings=["atama-eyes-open"], rect=[7, 2, 17, 3], colors=EYE),
    # the shut eyes' black strokes lie wholly on the ball: lines on it, not creases
    dict(drawings=["atama-eyes-closed"], interior={15: (BALLOON, INNER)}),
]
