# Persian: a sleek cat in one short tan coat, six whiskers, and a red jewel in its forehead (Black 2/White 2:
# "Among fans, the size of the jewel in its forehead is a topic of much talk"), which gives off light
# (Yellow: "The gem in its forehead glows on its own!"). The jewel is the one unusual surface; the rest is matte.
SOURCE = "sources/black2-white2/0053-persian.spu"
FUR = [15, 14, 13, 12]
MATERIALS = [
    # black: the line, the ears' black rims, the nose, the lines of the tail's curl
    dict(name="outline", shades=[3], finish=0.1, body=0),
    # the coat: its brown contour (15) is its darkest shade; nearly all of it is painted in 13
    dict(name="short fur", shades=FUR, base=2, finish=-0.2, body=0.05),
    dict(name="short fur, ear insides", shades=[9, 8, 7], base=1, finish=-0.2, body=0.05),
    # "six bold whiskers": one stiff hair each
    dict(name="whiskers", shades=FUR, base=3, finish=0.1, body=0.05),
    # the jewel: a polished red stone with a white catchlight
    dict(name="gem, red", shades=[6, 5, 4, 1], base=1, finish=1, body=0.6),
    # the one fang showing at the mouth: white, with the palette's gray as its shade
    dict(name="claws and teeth", shades=[2, 1], base=1, finish=0.7, body=0.05),
    # white, its gray, the red slit, and the brown line the eye is drawn with (closed: the lid's line)
    dict(name="eye (line art)", shades=[15, 6, 5, 2, 1], finish=0.9, body=0),
]
def to(name, colors): return {c: name for c in colors}
COLORS = {3: "outline", **to("short fur", FUR), **to("short fur, ear insides", [9, 8, 7]),
          **to("gem, red", [6, 5, 4, 1]), 2: "eye (line art)"}
RULES = [
    dict(drawings=["hige01", "hige02", "hige-l", "hige-r"], colors=to("whiskers", FUR)),
    # the eyes are drawn only on the strips that lie over the head
    dict(drawings=["atanma-eyes-open"], colors=to("eye (line art)", [15, 6, 5, 2, 1])),
    dict(drawings=["atanma-eyes-closed"], colors={15: "eye (line art)"}),
    # the fang
    dict(view="front", drawings=["atanma"], rect=[15, 25, 1, 1], colors={1: "claws and teeth"}),
]
# Only the jewel gives off light: enough to show in a cave and tint the brow, not to light the cave.
GLOW = [
    dict(material="gem, red", colors=[5, 4, 1], glow=80, intent="the gem in its forehead glows on its own: its bright faces"),
    dict(material="gem, red", colors=[6], glow=30, intent="the gem's faces in shade glow less"),
]
