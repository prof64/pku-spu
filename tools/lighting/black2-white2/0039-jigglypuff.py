SOURCE = "sources/black2-white2/0039-jigglypuff.spu"
MATERIALS = [
    # black line; the mouth line, the shut eyes' lash line and the crease where the curl wraps over itself are
    # drawn in the coat's dark reds; the gray softens the line along the far ear seen from behind
    dict(name="outline", shades=[11, 6, 15, 14], finish=0.1, body=0),
    # the pink coat (body, curl, ears, arms, feet): the front is painted in 13, the back in 14; 14 is most of it.
    # Its dark red contour is its darkest shade
    dict(name="short fur", shades=[15, 14, 13, 12], base=2, finish=-0.2, body=0.05),
    # inside the ears: black, with a gray patch of light
    dict(name="short fur, ear insides", shades=[11, 6], base=0, finish=-0.2, body=0.05),
    dict(name="mouth", shades=[9, 10], base=0, finish=0.8, body=0),
    dict(name="eye (line art)", shades=[5, 4, 3, 2, 8, 1], finish=0.9, body=0),
]
def to(name, colors): return {c: name for c in colors}
EAR = to("short fur, ear insides", [11, 6])
LINE = to("outline", [15, 14])
COLORS = {11: "outline", 6: "outline", **to("short fur", [15, 14, 13, 12]), **to("mouth", [9, 10]),
          **to("eye (line art)", [5, 4, 3, 2, 8, 1])}
RULES = [
    # the ears from the front: the near ear's drawing has no other black; the far ear's black edge stays line
    dict(view="front", drawings=["r-ear01*"], colors=EAR),
    dict(view="front", drawings=["l-ear01*"], rect=[6, 3, 5, 7], colors=EAR),
    # the mouth line (shut, and around the open mouth) and the shut eyes' lash line
    dict(drawings=["mouth01*", "image-18"], colors=LINE),
    dict(drawings=["head01-eyes-closed"], colors=LINE),
    # the curl wraps over itself: the dark stroke inside it is a crease
    dict(view="front", drawings=["parts01*"], interior={15: ([11, 12, 13, 14], "outline")}),
]
