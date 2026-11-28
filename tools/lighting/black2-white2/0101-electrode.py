# Electrode: the same polished ball casing as Voltorb, the colors the other way up; a grin of teeth.
SOURCE = "sources/black2-white2/0101-electrode.spu"
# Ball shell: a polished hard casing, solid, not metal. 0.6 is the least that is lit as a round ball;
# at 0.7 and 0.8 the white half mirrored the place in dark wedges like chrome
BALL = dict(finish=0.6, body=0) 
MATERIALS = [
    # black; the softened gray line (5) round the lit side, the brows and between the teeth, and its
    # paler end (4)
    dict(name="outline", shades=[15, 5, 4], finish=0.1, body=0),
    # the red half; 14 is the line of the lips, 11 the broad lighter band under the mouth
    dict(name="ball shell, red", shades=[14, 13, 12, 11], base=1, **BALL),
    # the white half: 2 from the front, a step darker (3) from behind, 1 the painted highlight. Base is the
    # darker one: with 2 the whole back fell to dark gray in a field
    dict(name="ball shell, white", shades=[3, 2, 1], base=0, **BALL),
    dict(name="claws and teeth", shades=[3, 1], base=1, finish=0.7, body=0.05),
    # the pinks where white meets red: blended pixels on the join of the two halves, the same casing.
    # In a row with no shades they stayed pale pink on a ball gone dark (sun behind)
    dict(name="ball shell, join", shades=[8, 7], base=0, **BALL),
    # the brows: strokes drawn on the one smooth ball, not pieces lying on it
    dict(name="seams and wrinkles", shades=[], finish=0, body=0),
    # the eyes are two short black strokes with a gray tail
    dict(name="eye (line art)", shades=[15, 4], finish=0.9, body=0),
]
INNER = "seams and wrinkles"
def to(name, colors): return {c: name for c in colors}
EYE = to("eye (line art)", [15, 4])
COLORS = {**to("outline", [15, 5, 4]), **to("ball shell, red", [14, 13, 12, 11]),
          **to("ball shell, white", [3, 2, 1]), **to("ball shell, join", [7, 8])}
RULES = [
    dict(drawings=["kuti", "mouth"], colors=to("claws and teeth", [3, 1])),
    dict(drawings=["kao-eyes-*", "body-eyes-*"], colors=EYE),
    # the brows' gray line; the paler gray inside a thick brow is the shell showing
    dict(drawings=["mayu*", "eyebrow"], colors=to(INNER, [5, 4])),
    dict(view="front", drawings=["kao"], rect=[13, 21, 1, 4], colors=EYE),
    dict(view="front", drawings=["kao"], rect=[28, 22, 1, 4], colors=EYE),
    dict(view="back", drawings=["body"], rect=[42, 18, 1, 4], colors=EYE),
]
