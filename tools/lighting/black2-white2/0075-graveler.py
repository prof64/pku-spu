# Graveler: one craggy stone (body, four arms, feet), bared teeth, eyes.
SOURCE = "sources/black2-white2/0075-graveler.spu"
ROCK = [2, 3, 4, 5, 6]
MATERIALS = [
    dict(name="outline", shades=[1], finish=0.1, body=0),
    # "it doesn't mind if pieces break off while it rolls down mountains" (Gold): plain stone, dead matte and
    # solid, the same row as Geodude and Onix. 2 is the contour on the lit side and the underside's shadow.
    # Base is the darker mid shade (3): the whole back, the arms and the feet are painted in it (the front of
    # the body two steps lighter). With the mid shade (4) the back fell to its darkest shade in a field
    dict(name="rock", shades=ROCK, base=1, finish=0, body=0),
    # the clenched teeth: white below, a step darker under the lip, gray between them
    dict(name="claws and teeth", shades=[7, 8, 9], base=2, finish=0.7, body=0.05),
    dict(name="eye (line art)", shades=[1, 8, 9], finish=0.9, body=0),
]
# the pale light (6) on the crags' top edges is few pixels; kept in the row so it goes dark with the stone
KEEP_TOP = ["rock"]
def to(name, colors): return {c: name for c in colors}
COLORS = {1: "outline", **to("rock", ROCK), **to("claws and teeth", [7, 8, 9])}
PUPIL = {1: "eye (line art)"}
RULES = [
    dict(drawings=["body-eyes-*"], colors=to("eye (line art)", [8, 9])),
    # pupils (black); the brow and lid lines around them stay lines
    dict(view="front", drawings=["body-eyes-open"], rect=[4, 4, 1, 1], colors=PUPIL),
    dict(view="front", drawings=["body-eyes-open"], rect=[10, 5, 1, 1], colors=PUPIL),
]
