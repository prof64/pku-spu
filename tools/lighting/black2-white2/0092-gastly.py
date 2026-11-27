SOURCE = "sources/black2-white2/0092-gastly.spu"
# Gas (the standard row): soft and frosted, so light blurs through it; not clear glass
GAS = dict(finish=-0.5, body=0.75)
MATERIALS = [
    dict(name="outline", shades=[15], finish=0.1, body=0),
    # the cloud and the loose puffs. Smeargle gives a row named gas no shape (it stays facing the viewer),
    # so the cloud's three lilacs are how thick the gas is, not shading: one row for each, the same dials
    dict(name="gas", shades=[11], base=0, **GAS),
    dict(name="gas, thin edge", shades=[10], base=0, **GAS),
    dict(name="gas, dense", shades=[12], base=0, **GAS),
    # the black ball. The Pokedex calls the whole body gas, but the art, the 3D model and the sprite all draw
    # an opaque ball with a hard contour that hides the cloud behind it: soft like the gas (the art paints
    # one broad cloudy light on its crown, no highlight), and solid. Not named gas, so it keeps its shape.
    # At the gas's 0.75 the ball turned clear in a field and pink with the sun behind it.
    dict(name="dark core", shades=[9, 8, 7], base=0, finish=-0.5, body=0),
    dict(name="claws and teeth", shades=[2, 1], base=0, finish=0.7, body=0.05),
    dict(name="mouth", shades=[4, 3], base=0, finish=0.8, body=0),
    # red creases beside the eyes, the red and black lines of the shut eyes: tinted, never a crease
    dict(name="seams and wrinkles", shades=[], finish=0, body=0),
    # whites, their gray shade, the two-pixel pupils and the lilac pixels that soften the eyes' edges
    dict(name="eye (line art)", shades=[9, 8, 11, 10, 2, 1], finish=0.9, body=0),
]
INNER = "seams and wrinkles"
def to(name, colors): return {c: name for c in colors}
COLORS = {15: "outline", 11: "gas", 10: "gas, thin edge", 12: "gas, dense", **to("dark core", [9, 8, 7])}
EYE = to("eye (line art)", [1, 2, 10, 11])
PUPIL = to("eye (line art)", [8, 9])
RULES = [
    # 16 pixels of color 7 in the dense cloud are the same lilac in the normal palette (hidden behind the ball)
    dict(drawings=["gasu2", "gas-b"], colors={7: "gas, dense"}),
    dict(drawings=["gose-eyes-*"], colors={**EYE, 4: INNER}),
    dict(view="front", drawings=["gose-eyes-open"], rect=[7, 13, 1, 2], colors=PUPIL),
    dict(view="front", drawings=["gose-eyes-open"], rect=[16, 13, 1, 2], colors=PUPIL),
    # the shut eyes' black strokes lie wholly on the ball: lines on it, not creases
    dict(drawings=["gose-eyes-closed"], interior={15: ([9, 8, 7, 4], INNER)}),
    dict(drawings=["mouse*", "mouth*"], colors={**to("claws and teeth", [1, 2]), **to("mouth", [3, 4])}),
]
# the pale patch on the ball's crown is its painted shading, a tenth of the ball that shows, not a glint:
# kept in the row, so it goes dark with the rest of the ball when the light is behind
KEEP_TOP = ["dark core"]
