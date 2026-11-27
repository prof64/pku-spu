SOURCE = "sources/black2-white2/0044-gloom.spu"
# Gloom: the blue root body of Oddish with arms, a closed brown bud of four lobes with pale spots, drooping
# orange leaves, purple lips, and the nectar it drools. The painted art shades everything flat and soft except
# the drool, which is drawn wet.
# Colors: 15 black; 14 13 12 the blues; 9 8 7 6 the bud's browns; 5 4 3 2 the leaves' oranges (3 also the pistil,
# 2 also the spots' shade); 1 cream (spots, nectar); 10 the lips' purple. The eyes are shut: black lines.
ROOT = dict(finish=0.1, body=0.1)      # as Oddish
BUD = dict(finish=0.1, body=0.25)      # Bud and bulb, as Ivysaur's bud
MATERIALS = [
    # black; the bud's darkest brown where it is the line between two lobes; and the bud's browns where they
    # draw a leaf's edge against the bud
    dict(name="outline", shades=[15, 9, 8], finish=0.1, body=0),
    dict(name="plant body", shades=[14, 13, 12], base=1, **ROOT),
    # the lips: color in the same body
    dict(name="plant body, lips", shades=[14, 10], base=1, **ROOT),
    dict(name="leaves", shades=[5, 4, 3, 2], base=1, finish=0.15, body=0.35),
    dict(name="bud", shades=[9, 8, 7, 6], base=1, **BUD),
    dict(name="bud spots", shades=[2, 1], base=1, **BUD),
    # the orange pistil between the four lobes
    dict(name="flower center", shades=[3], base=0, finish=0.2, body=0.25),
    # the honey it drools: wet, sticky and opaque (the dials of sludge). The palette has no gray: its unused
    # first color (a pale gray, in the shiny palette too) is the cream's shade
    dict(name="nectar", shades=[0, 1], base=1, finish=0.7, body=0.2),
    # the dark blue inside the open mouth (the black there is line)
    dict(name="mouth, dark inside", shades=[], finish=0.8, body=0),
]
def to(name, colors): return {c: name for c in colors}
COLORS = {15: "outline", **to("plant body", [14, 13, 12]), 10: "plant body, lips", **to("leaves", [5, 4, 3, 2]),
          **to("bud", [9, 8, 7, 6]), 1: "bud spots"}
INSIDE = {14: "mouth, dark inside"}
RULES = [
    # the bud (the female's has bigger spots): its spots and their yellow shade, the pistil, and the lines
    # between its lobes, which overlap, so they are creases
    dict(drawings=["flower*", "head*"], colors={2: "bud spots", 3: "flower center"}, thin_all={9: "outline"}),
    dict(drawings=["hear*"], colors={8: "outline", 9: "outline"}),
    # the mouth and the drool
    dict(drawings=["mouth*", "yodare*"], colors={1: "nectar"}),
    dict(drawings=["mouth"], rect=[10, 7, 3, 1], colors=INSIDE),
    dict(drawings=["mouth-2"], rect=[10, 7, 3, 1], colors=INSIDE),
    dict(drawings=["mouth-2"], rect=[9, 8, 5, 1], colors=INSIDE),
    dict(drawings=["mouth-2"], rect=[12, 9, 1, 1], colors=INSIDE),
]
# the yellow patches toward the leaves' tips are broad painted light, a shade: left out of the row they went khaki
KEEP_TOP = ["leaves"]
