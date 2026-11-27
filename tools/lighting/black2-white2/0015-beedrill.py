SOURCE = "sources/black2-white2/0015-beedrill.spu"
YELLOW = [6, 5, 4, 3, 2]
PALE = [10, 9, 8, 7, 1]
MATERIALS = [
    dict(name="outline", shades=[15, 10], finish=0.1, body=0),
    dict(name="insect shell", shades=YELLOW, base=2, finish=0.45, body=0),
    # the black bands of the abdomen: pigment in the same shell, drawn black with a blue-gray sheen
    dict(name="insect shell, stripes", shades=[15, 14], base=0, finish=0.45, body=0),
    # legs, arms and antennae: the same hard shell, drawn black with a blue-gray lit side
    dict(name="insect shell, limbs", shades=[15, 14], base=0, finish=0.45, body=0),
    # body 0.3, not the starting 0.6: at 0.6 the wings sparkle and stay bright in the cave and lose their contour
    # in the field; at 0.3 they are as bright next to the body in the cave as the art paints them, and still
    # light up when the sun is behind them
    dict(name="insect wing", shades=PALE, base=4, finish=0.4, body=0.3),
    dict(name="claws and teeth, stingers", shades=PALE, base=1, finish=0.7, body=0.05),
    dict(name="claws and teeth, tail stinger", shades=YELLOW, base=2, finish=0.7, body=0.05),
    dict(name="seams and wrinkles", shades=[], finish=0, body=0),   # wing veins: lines inside one sheet, never a crease
    dict(name="eye (line art)", shades=[13, 12, 11, 1], finish=0.9, body=0),
]
INNER = "seams and wrinkles"
def to(name, colors): return {c: name for c in colors}
LIMB = to("insect shell, limbs", [15, 14])
STRIPE = to("insect shell, stripes", [15, 14])
COLORS = {15: "outline", 14: "insect shell, limbs", **to("insect shell", YELLOW), **to("insect wing", PALE),
          **to("eye (line art)", [13, 12, 11])}
RULES = [
    # wings: the veins are lines inside one flat sheet
    dict(drawings=["wing-*", "*-wings0*", "part-0"], interior={9: ([1, 7, 8, 10], INNER), 10: ([1, 7, 8, 9], INNER)}),
    # legs and the loose antenna pictures are all limb
    dict(drawings=["foot-*", "*-leg01", "image-7", "image-8"], colors=LIMB),
    # head: the antennae above it; the eye's catchlight
    dict(view="front", drawings=["head"], rect=[0, 0, 32, 12], colors=LIMB),
    dict(view="front", drawings=["head"], rect=[0, 12, 12, 4], colors=LIMB),
    dict(view="back", drawings=["head01"], rect=[11, 0, 21, 13], colors=LIMB),
    dict(view="back", drawings=["head01"], rect=[24, 13, 8, 3], colors=LIMB),
    dict(view="back", drawings=["head01"], colors={10: "outline"}),        # one lilac pixel on an antenna: stays as drawn
    dict(drawings=["head", "head-eyes-*"], colors={1: "eye (line art)"}),
    # arms: the stinger, and the arm that holds it
    dict(drawings=["hand-l", "hand-r", "l-arm01", "r-arm01"], colors=to("claws and teeth, stingers", PALE)),
    dict(view="front", drawings=["hand-l"], rect=[20, 2, 20, 8], colors=LIMB),
    dict(view="front", drawings=["hand-r"], rect=[14, 21, 10, 1], colors=LIMB),
    dict(view="front", drawings=["hand-r"], rect=[0, 22, 24, 9], colors=LIMB),
    dict(view="back", drawings=["l-arm01"], rect=[0, 21, 24, 10], colors=LIMB),
    dict(view="back", drawings=["r-arm01"], rect=[0, 3, 21, 8], colors=LIMB),
    # abdomen: the black bands are stripes; the black along the silhouette stays the outline
    dict(drawings=["body", "body02"], colors=STRIPE),
    dict(view="front", drawings=["body"], rect=[19, 9, 2, 10], colors={15: "outline"}),
    dict(view="front", drawings=["body"], rect=[18, 19, 3, 1], colors={15: "outline"}),
    dict(view="front", drawings=["body"], rect=[4, 18, 1, 2], colors={15: "outline"}),
    dict(view="front", drawings=["body"], rect=[0, 20, 24, 8], colors={15: "outline"}),
    dict(view="back", drawings=["body02"], rect=[0, 5, 24, 5], colors={15: "outline"}),
    dict(view="back", drawings=["body02"], rect=[3, 13, 2, 4], colors={15: "outline"}),
    dict(view="back", drawings=["body02"], rect=[0, 20, 9, 2], colors={15: "outline"}),
    dict(view="back", drawings=["body02"], rect=[0, 22, 24, 6], colors={15: "outline"}),
    # the point of the abdomen is the tail stinger
    dict(view="front", drawings=["body"], rect=[0, 22, 24, 6], colors=to("claws and teeth, tail stinger", YELLOW)),
    dict(view="back", drawings=["body02"], rect=[0, 24, 24, 4], colors=to("claws and teeth, tail stinger", YELLOW)),
]
