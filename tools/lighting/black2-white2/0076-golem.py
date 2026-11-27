# Golem: a shell of rock slabs, a thick hide on the head, arms and legs, white claws and teeth.
SOURCE = "sources/black2-white2/0076-golem.spu"
ROCK = [9, 8, 7, 6]
HIDE = [13, 12, 11, 10]
CLAW = [3, 2, 1]
MATERIALS = [
    # black: the line, and the deep gaps between the slabs (each slab is its own piece, so they are creases)
    dict(name="outline", shades=[15], finish=0.1, body=0),
    # "enclosed in a hard shell that is as rugged as slabs of rock" (FireRed): plain stone, dead matte and
    # solid, the same row as Geodude, Graveler and Onix. 9 is each slab's contour and the slabs in shadow.
    # Base is the second darkest (8), which most of the shell is painted in, both views
    dict(name="rock", shades=ROCK, base=1, finish=0, body=0),
    # head, arms and legs: "its rugged hide" (Crystal), Blastoise's row for a heavy thick-skinned animal.
    # Base is the darker tan (12): limbs and the back of the head are nearly all painted in it
    dict(name="thick hide", shades=HIDE, base=1, finish=0.4, body=0.06),
    dict(name="claws and teeth", shades=CLAW, base=2, finish=0.7, body=0.05),
    # the open mouth is one dark red; the black around it is its shade, so it goes dark with the head
    # (as a row of the one red it stayed vivid in a cave). No other color is darker in both palettes
    dict(name="mouth", shades=[15, 5], base=1, finish=0.8, body=0),
    dict(name="eye (line art)", shades=[5, 4, 3, 2, 1], finish=0.9, body=0),
]
# the palest tan (10) is only the light on top of the head; kept in the row so it goes dark with the head
KEEP_TOP = ["thick hide"]
def to(name, colors): return {c: name for c in colors}
COLORS = {15: "outline", **to("rock", ROCK), **to("thick hide", HIDE), **to("claws and teeth", CLAW), 5: "mouth"}
RULES = [
    dict(view="front", drawings=["head-eyes-open"], colors=to("eye (line art)", [1, 2, 3, 4])),
    dict(view="back", drawings=["body-eyes-open"], colors=to("eye (line art)", [1, 5])),
]
