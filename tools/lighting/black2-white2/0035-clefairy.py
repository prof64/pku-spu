SOURCE = "sources/black2-white2/0035-clefairy.spu"
MATERIALS = [
    # black line, the mouth line, and the black back of each ear
    dict(name="outline", shades=[15], finish=0.1, body=0),
    # the pink coat everywhere (body, curl, tail, hands, feet, the small wings): painted flat and soft in the
    # official art, smooth-edged with no tufts. Its dark pink contour is its darkest shade; front and back
    # together are mostly painted in 12
    dict(name="short fur", shades=[14, 13, 12, 11], base=2, finish=-0.2, body=0.05),
    dict(name="short fur, ear tips", shades=[8, 7, 6], base=1, finish=-0.2, body=0.05),
    # the two blush marks under the eyes: the coat's ramp one step down
    dict(name="short fur, cheeks", shades=[14, 13], base=1, finish=-0.2, body=0.05),
    # one claw on each hand and foot (white with the palette's gray), and the one tooth
    dict(name="claws and teeth", shades=[3, 1], base=1, finish=0.7, body=0.05),
    dict(name="mouth", shades=[5, 4], base=0, finish=0.8, body=0),
    dict(name="eye (line art)", shades=[15, 3, 1], finish=0.9, body=0),
]
def to(name, colors): return {c: name for c in colors}
COLORS = {15: "outline", **to("short fur", [14, 13, 12, 11]), **to("short fur, ear tips", [8, 7, 6]),
          **to("claws and teeth", [3, 1]), **to("mouth", [5, 4])}
EYE = to("eye (line art)", [15, 3, 1])
RULES = [
    # the eyes: catchlight, pupil and gray foot, one pixel wide (the dark pink marks beside them are the coat's)
    dict(view="front", drawings=["body"], rect=[11, 8, 1, 4], colors=EYE),
    dict(view="front", drawings=["body"], rect=[17, 8, 1, 4], colors=EYE),
    dict(drawings=["body-eyes-open"], colors=EYE),
    # the blush marks
    dict(view="front", drawings=["body"], rect=[6, 11, 3, 2], colors={13: "short fur, cheeks"}),
    dict(view="front", drawings=["body"], rect=[21, 11, 3, 2], colors={13: "short fur, cheeks"}),
]
