# Voltorb: "It looks just like a Poké Ball" (Black 2/White 2). One hard, polished ball casing in two
# colors; the painted art puts a small hard white highlight inside a pale patch on the red half.
SOURCE = "sources/black2-white2/0100-voltorb.spu"
# Ball shell: a polished hard casing, solid, not metal. 0.6 is the least that is lit as a round ball;
# higher values mirrored the place like chrome (see Electrode)
BALL = dict(finish=0.6, body=0)
MATERIALS = [
    dict(name="outline", shades=[15], finish=0.1, body=0),
    # the red half. 14 is its contour on the lit side and the furrows of the brow; 10 and 9 are the
    # painted highlight, kept so it can move. The front is painted in 11 and the back a step darker in 13,
    # near level over both views, so base is the shade between: with 11 the back went near black in a
    # field and a cave, with 13 the front went dull and speckled
    dict(name="ball shell, red", shades=[14, 13, 12, 11, 10, 9], base=2, **BALL),
    # the pale half: gray-lilac where it is in shade (most of it), white along the lit rim
    dict(name="ball shell, white", shades=[3, 2, 1], base=0, **BALL),
    # eye white, its gray corner, the pupil, and the line of a closed eye
    dict(name="eye (line art)", shades=[15, 3, 2, 1], finish=0.9, body=0),
]
def to(name, colors): return {c: name for c in colors}
COLORS = {15: "outline", **to("ball shell, red", [14, 13, 12, 11, 10, 9]), **to("ball shell, white", [3, 2, 1])}
RULES = [
    # the eye drawings: white and black there are the eye; the reds around it stay the shell
    dict(drawings=["part-0*", "eye1*"], colors=to("eye (line art)", [15, 3, 2, 1])),
]
