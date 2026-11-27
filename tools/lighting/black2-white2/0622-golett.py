# Golett: unglazed clay all over, leather-like straps, and the energy that burns inside it showing
# through the eye slits, the spiral cut in the chest seal and the gaps between the slabs.
SOURCE = "sources/black2-white2/0622-golett.spu"
CLAY = dict(finish=0, body=0)                 # Clay: matte and solid (the painted art has no highlight anywhere)
ENERGY = dict(finish=0.5, body=0.5)           # Light organ
MATERIALS = [
    # black, and the dark brown lines where one strap lies over another
    dict(name="outline", shades=[15, 13], finish=0.1, body=0),
    # the pale slabs: fists and forearms, feet, face, the peak of the head, the chest seal, patches on the ball.
    # 4 is their contour on the lit side, 3 the grooves cut in them. Base is the mid shade (2): the palest (1)
    # and it are near level over both views, and with the palest as base the fists and feet fell two
    # shades in a field
    dict(name="clay", shades=[4, 3, 2, 1], base=2, **CLAY),
    # the darker ball of the body, the cap and sides of the head, the hands, arms and legs: the same clay
    dict(name="clay, body", shades=[7, 6, 5], base=1, **CLAY),
    # the two brown bands that hold the seal: flat brown in the art, no sheen. Their streaks (12) are shading
    dict(name="straps", shades=[13, 12, 11], base=1, finish=0.1, body=0),
    # "The energy that burns inside it" (Black): the sprite pulses it through three yellows, bright to dim.
    # They are how strongly it burns, not shading, so each is its own row of one shade with the same dials
    dict(name="inner energy", shades=[8], base=0, **ENERGY),
    dict(name="inner energy, dimmer", shades=[9], base=0, **ENERGY),
    dict(name="inner energy, dimmest", shades=[10], base=0, **ENERGY),
    # the two eye slits (front view; they pulse with the body): the same energy, kept as drawn
    dict(name="eye (line art)", shades=[10, 9, 8], finish=0.9, body=0),
]
def to(name, colors): return {c: name for c in colors}
COLORS = {15: "outline", **to("clay", [4, 3, 2, 1]), **to("clay, body", [7, 6, 5]), **to("straps", [13, 12, 11]),
          8: "inner energy", 9: "inner energy, dimmer", 10: "inner energy, dimmest"}
RULES = [
    dict(view="front", drawings=["b-atama01*"], colors=to("eye (line art)", [8, 9, 10])),
    # dark brown lines wholly inside the brown are where the straps cross: one piece over another, a crease.
    # The same brown along the straps' outer edge stays their darkest shade
    dict(drawings=["b-karada0[12]"], interior={13: ([11, 12], "outline")}),
]
GLOW = [
    dict(colors=[8], glow=170, intent="the energy that burns inside it, at its brightest"),
    dict(colors=[9], glow=145, intent="the same energy, a step dimmer"),
    dict(colors=[10], glow=120, intent="the same energy at the low point of its pulse"),
    # the spiral is drawn in the two brighter yellows mixed and does not pulse; at the gaps' strength its
    # light whitened the mark and the seal around it
    dict(colors=[8, 9], drawings=["b-karada02"], views=["front"], glow=120,
         intent="the spiral cut in the seal: the same energy through a narrow groove"),
]
