# Mankey: a ball of shaggy cream fur (Fur) with smooth cream arms, legs and tail (Short fur); the brown hands,
# two-toed feet and tail tip are bare skin (Hide), and so is the pink pig snout. Nothing glows, nothing is glossy:
# the painted art shades every part softly, with no highlight anywhere but the eyes.
SOURCE = "sources/black2-white2/0056-mankey.spu"
F = dict(finish=-0.7, body=0.05)          # Fur: the shaggy ball
SF = dict(finish=-0.2, body=0.05)         # Short fur: the smooth-edged limbs, tail and ears
H = dict(finish=0.25, body=0.08)          # Hide: plain bare skin
MATERIALS = [
    dict(name="outline", shades=[7], finish=0.1, body=0),
    # the round head-and-body. The front is mostly painted in 13, the back wholly in 14, so both views together are
    # mostly 14; the broad pale forehead (12) is a shade, not a glint. The dark brown contour (15) is in these cream
    # rows but is NOT one of their shades: the palette has nothing between cream and that brown, so as the darkest
    # shade every pixel one step off the light fell to dark brown and the whole ball went dark and speckled in daylight
    dict(name="fur", shades=[14, 13, 12], base=0, **F),
    # arms, thighs, shins and the tail's shaft: the same cream, drawn smooth-edged with no tufts
    dict(name="short fur", shades=[14, 13], base=0, **SF),
    # the ears' cream backs and rims: smooth triangles
    dict(name="short fur, ears", shades=[14, 13, 12], base=1, **SF),
    dict(name="short fur, ear insides", shades=[11, 10], base=1, **SF),
    # hands, feet and the tail's tip: bare brown skin, painted flat
    dict(name="hide", shades=[11, 10, 9, 8], base=1, **H),
    # the pink snout: bare skin with a soft lighter top
    dict(name="hide, snout", shades=[6, 5, 4], base=1, **H),
    # the two furrows between the eyes, drawn on the fur in the hands' browns: a marking with the fur's dials, so it
    # goes dark with the fur around it (as a tinted line it stayed orange on a face in shade)
    dict(name="fur, brow furrows", shades=[11, 10], base=1, **F),
    # the nostrils, and the fur-brown line along the top of the front feet and tail tip: lines drawn on a surface,
    # tinted, never a crease
    dict(name="seams and wrinkles", shades=[], finish=0, body=0),
    dict(name="eye (line art)", shades=[7, 5, 2, 1], finish=0.9, body=0),
]
INNER = "seams and wrinkles"
KEEP_TOP = ["fur", "short fur, ears"]
def to(name, colors): return {c: name for c in colors}
CREAM = [15, 14, 13, 12]
EAR = to("short fur, ears", CREAM)
EYE = to("eye (line art)", [1, 2, 5, 7])
COLORS = {7: "outline", **to("fur", CREAM), **to("hide", [11, 10, 9, 8]), **to("hide, snout", [6, 5, 4]),
          **to("eye (line art)", [1, 2])}
def rects(view, drawings, boxes, colors): return [dict(view=view, drawings=drawings, rect=b, colors=colors) for b in boxes]
RULES = [
    # limbs and tail, both views: smooth cream
    dict(drawings=["ude*", "momo*", "asi*", "o", "arm-*", "hand-*", "leg-*", "foot-*", "tail"],
         colors=to("short fur", [15, 14, 13])),
    # the fur-brown line drawn along the top of the front feet and of the tail's tip
    dict(view="front", drawings=["asi1"], rect=[0, 6, 16, 10], colors={15: INNER}),
    dict(view="front", drawings=["o"], rect=[0, 5, 32, 9], colors={15: INNER}),
    # front head: the brown inside each ear (everything brown above the brow)
    dict(view="front", drawings=["kao", "kao-2"], rect=[0, 0, 32, 11], colors=to("short fur, ear insides", [11, 10])),
    # ... and each ear's cream rim: the left ear, then the right
    *rects("front", ["kao", "kao-2"], [[3, 3, 4, 1], [4, 4, 3, 1], [4, 5, 5, 1], [5, 6, 5, 1], [5, 7, 6, 1], [6, 8, 5, 1],
                                      [6, 9, 4, 1], [21, 3, 4, 4], [20, 7, 5, 1], [19, 8, 6, 2], [20, 10, 4, 1]], EAR),
    # the two furrows between the eyes
    dict(view="front", drawings=["kao", "kao-2"], rect=[9, 14, 5, 4], colors=to("fur, brow furrows", [11, 10])),
    dict(drawings=["kao*-eyes-*"], rect=[4, 3, 5, 4], colors=to("fur, brow furrows", [11, 10])),
    # the nostrils
    dict(view="front", drawings=["kao", "kao-2"], rect=[9, 19, 6, 4], colors={15: INNER}),
    # the eyes: white, its gray corner, the red iris and the black pupil and rim
    dict(view="front", drawings=["kao", "kao-2"], rect=[6, 13, 3, 5], colors=EYE),
    dict(view="front", drawings=["kao", "kao-2"], rect=[14, 14, 6, 4], colors=EYE),
    dict(drawings=["kao*-eyes-open"], rect=[1, 2, 3, 5], colors=EYE),
    dict(drawings=["kao*-eyes-open"], rect=[9, 3, 6, 4], colors=EYE),
    # back head: the two ears (the right one lies flat in the first drawing)
    *rects("back", ["head"], [[5, 3, 5, 4], [6, 7, 3, 1], [6, 8, 2, 2], [24, 5, 4, 1], [24, 6, 3, 1], [22, 7, 5, 1], [20, 8, 6, 1]], EAR),
    *rects("back", ["head-2"], [[6, 2, 6, 4], [7, 6, 3, 1], [6, 7, 3, 1], [6, 8, 2, 2], [21, 3, 5, 4], [20, 7, 6, 1], [20, 8, 5, 1]], EAR),
]
