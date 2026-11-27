# Geodude: one stone all over (head and both arms), a wet mouth when it opens, eyes.
SOURCE = "sources/black2-white2/0074-geodude.spu"
ROCK = [2, 3, 4, 5, 6]
MATERIALS = [
    dict(name="outline", shades=[1], finish=0.1, body=0),
    # "At rest, it looks just like a rock" (Black 2/White 2): plain stone, dead matte and solid, the same row
    # as Onix. 2 is its contour on the lit side and the cracks and muscle lines drawn in it; base is the mid
    # gray (4), which most of the head and arms is painted in, both views
    dict(name="rock", shades=ROCK, base=2, finish=0, body=0),
    # the inside of the open mouth (dark red) and the tongue (the two lighter reds)
    dict(name="mouth", shades=[7, 8, 9], base=0, finish=0.8, body=0),
    dict(name="eye (line art)", shades=[1, 12, 11, 10], finish=0.9, body=0),
]
# the pale edge light (6) on the top of the head and fists is few pixels; kept in the row so it goes dark
# with the stone around it
KEEP_TOP = ["rock"]
def to(name, colors): return {c: name for c in colors}
EYE = to("eye (line art)", [10, 11, 12])
PUPIL = {1: "eye (line art)"}
COLORS = {1: "outline", **to("rock", ROCK), **to("mouth", [7, 8, 9]), **EYE}
RULES = [
    # pupils (black); the brow and lid lines around them stay lines
    dict(view="front", drawings=["head-eyes-open"], rect=[4, 4, 1, 2], colors=PUPIL),
    dict(view="front", drawings=["head-eyes-open"], rect=[11, 5, 1, 1], colors=PUPIL),
    dict(view="back", drawings=["head-eyes-open"], rect=[4, 4, 1, 1], colors=PUPIL),
    dict(view="back", drawings=["head"], rect=[26, 13, 1, 1], colors=PUPIL),
]
