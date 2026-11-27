SOURCE = "sources/black2-white2/0040-wigglytuff.spu"
MATERIALS = [
    # black line; the mouth line is drawn in the browns, the shut eyes' lash line and the crease where the
    # curl wraps over itself in the coat's dark pinks
    dict(name="outline", shades=[15, 9, 8, 14, 13, 12], finish=0.1, body=0),
    # the pink coat (body, curl, ears, arms, feet): the front is painted in 11, the back in 12; 12 is most of it.
    # Its dark contour colors are its darkest shades
    dict(name="short fur", shades=[14, 13, 12, 11], base=2, finish=-0.2, body=0.05),
    # the white belly: the same coat
    dict(name="short fur, belly", shades=[2, 1], base=1, finish=-0.2, body=0.05),
    # the white ear tips; their gray contour is their darkest shade
    dict(name="short fur, ear tips", shades=[3, 2, 1], base=2, finish=-0.2, body=0.05),
    # inside the ears: black, with brown patches of light
    dict(name="short fur, ear insides", shades=[15, 9, 8], base=0, finish=-0.2, body=0.05),
    # the red inside of the open mouth is one color; the brown line over it is its shade
    dict(name="mouth", shades=[8, 7], base=1, finish=0.8, body=0),
    dict(name="eye (line art)", shades=[6, 5, 2, 1], finish=0.9, body=0),
]
def to(name, colors): return {c: name for c in colors}
FUR = [11, 12, 13, 14]
EAR = to("short fur, ear insides", [15, 9, 8])
COLORS = {15: "outline", 9: "outline", 8: "outline", **to("short fur", FUR), **to("short fur, belly", [2, 1]),
          3: "short fur, ear tips", 7: "mouth", **to("eye (line art)", [6, 5])}
RULES = [
    dict(drawings=["mimi-?-b", "?-mimi-b"], colors=to("short fur, ear tips", [3, 2, 1])),
    dict(drawings=["body-b-eyes-open"], colors=to("eye (line art)", [6, 5, 2, 1])),
    # the shut eyes: the lids are the coat, every darker pixel is the lash line
    dict(drawings=["body-b-eyes-closed"], colors=to("outline", [12, 13, 14])),
    dict(drawings=["mouse-b"], colors={8: "mouth"}),
    # the curl wraps over itself: the dark stroke inside it is a crease
    dict(drawings=["hear-b", "kami-b"], interior={13: (FUR, "outline"), 14: (FUR, "outline")}),
]
FLOODS = [
    # inside the ears, seen from the front: the black band shares its color with the line around the ear
    dict(view="front", drawing="mimi-l-b", seeds=[[6, 10]], through=[15, 9, 8], colors=EAR),
    dict(view="front", drawing="mimi-r-b", seeds=[[8, 13]], through=[15, 9, 8], colors=EAR),
]
