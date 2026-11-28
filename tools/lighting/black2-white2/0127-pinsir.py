SOURCE = "sources/black2-white2/0127-pinsir.spu"
SHELL = [6, 5, 4, 3, 2]
HORN = [12, 11, 10, 9, 8]
MATERIALS = [
    dict(name="outline", shades=[1, 6, 11], finish=0.1, body=0),
    # head-and-body, arms and legs: one hard brown shell; the dark brown contour is its darkest shade
    dict(name="insect shell", shades=SHELL, base=1, finish=0.45, body=0),
    # the two pincer horns and their thorns: hard horn, painted paler than the body with a broad soft light band
    dict(name="spines, horn", shades=HORN, base=2, finish=0.4, body=0),
    # the claws of the hands and feet
    dict(name="claws and teeth", shades=[11, 9, 7], base=2, finish=0.7, body=0.05),
    # the long flat teeth across the mouth
    dict(name="claws and teeth, mouth", shades=[10, 9, 8, 7], base=3, finish=0.7, body=0.05),
    dict(name="eye (line art)", shades=[1, 9, 7], finish=0.9, body=0),
]
def to(name, colors): return {c: name for c in colors}
COLORS = {1: "outline", **to("insect shell", SHELL), **to("spines, horn", HORN), 7: "claws and teeth"}
RULES = [
    # the body's segments and the joints of the limbs overlap: the dark lines between them are creases;
    # the same color along the outside stays the shell's darkest shade
    dict(interior={6: ([5, 4, 3, 2], "outline")}),
    # hands and feet: the claws, with their gray shade and contour
    dict(drawings=["hand-l2", "hand-r2", "te-*", "ashi-*", "tume*"], colors=to("claws and teeth", [11, 9, 7])),
    dict(drawings=["tume*"], colors={6: "outline"}),         # the dark line where a toe claw meets the foot
    dict(drawings=["foot"], colors={11: "outline"}),         # one stray gray pixel: stays as drawn
    # mouth: the teeth; the black between them stays the outline
    dict(drawings=["mouse*"], colors=to("claws and teeth, mouth", [10, 9, 8, 7])),
    # eyes: white, its gray shade, the black pupil and brow
    dict(drawings=["body-eyes-open"], rect=[0, 1, 16, 4], colors=to("eye (line art)", [1, 9, 7])),
]
# the palest brown is the broad lit top of the head and of each limb (about 4% of the shell): left out of
# the row it stays pale on a body gone dark with the sun behind
KEEP_TOP = ["insect shell"]
