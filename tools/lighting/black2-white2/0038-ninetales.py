SOURCE = "sources/black2-white2/0038-ninetales.spu"
MATERIALS = [
    # black line; brown lines drawn inside the coat (one tail over another, a leg over the body, the mouth)
    dict(name="outline", shades=[15, 14], finish=0.1, body=0),
    # the whole golden coat: head, crest, ruff, body, legs, nine tails. FireRed, X, Violet: "It has nine long
    # tails and fur that gleams gold."; the art paints pale streaks along every tail, the crest and the chest.
    # Its brown contour is its darkest shade
    dict(name="glossy fur", shades=[14, 13, 12, 11], base=2, finish=0.3, body=0.05),
    # the orange tips of the tails: the same fur
    dict(name="glossy fur, tail tips", shades=[14, 7, 6], base=1, finish=0.3, body=0.05),
    dict(name="eye (line art)", shades=[15, 14, 4, 3, 2, 1], finish=0.9, body=0),
]
def to(name, colors): return {c: name for c in colors}
EYE = "eye (line art)"
COLORS = {15: "outline", **to("glossy fur", [14, 13, 12, 11]), **to("glossy fur, tail tips", [7, 6]), **to(EYE, [4, 3, 2, 1])}
RULES = [
    # a brown line wholly inside the coat is where one piece lies over another: a crease
    dict(interior={14: ([13, 12, 11, 7, 6], "outline")}),
    # the eye: red iris, white catchlight, its black and brown rim
    dict(view="front", drawings=["atama"], rect=[12, 13, 4, 3], colors=to(EYE, [14, 15])),
    dict(drawings=["atama-eyes-open"], colors=to(EYE, [14, 15])),
    # shut, the eye is a drawn line
    dict(drawings=["atama-eyes-closed"], colors={14: "outline"}),
]
# the pale orange on two tips is few pixels: kept in the row so it goes dark with the tip
KEEP_TOP = ["glossy fur, tail tips"]
