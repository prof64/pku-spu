# Jolteon: a yellow coat that bristles into spikes on the rump, and a spiky white ruff. The Pokédex calls it
# fur throughout ("its bristlelike fur", Black 2/White 2; "The bristling fur is made of electrically charged
# needles", Ruby/Sapphire), hard only when it is charged or angry. The painted art shades all of it flat and
# soft with no highlight, so it is matte fur: the smooth-edged head, ears, body and legs the sleek coat
# (Short fur, as on Pikachu), the spikes and the ruff long fur (Fur at -0.1: at -0.7 anything bigger than a
# tuft goes grainy). Nothing glows at rest: no entry says it does.
SOURCE = "sources/black2-white2/0135-jolteon.spu"
SHORT = dict(finish=-0.2, body=0.05)
LONG = dict(finish=-0.1, body=0.05)
YELLOW = [7, 6, 5, 4, 3, 2]
MATERIALS = [
    # black line; the mouth line and the lid of the shut eye in the coat's browns; the lines between spikes
    # (brown in the yellow, dark gray in the ruff)
    dict(name="outline", shades=[1, 7, 6, 5, 11], finish=0.1, body=0),
    # the yellow coat: its brown contour colors are its darkest shades. The whole back view and the body are
    # painted in 4, the face a step lighter
    dict(name="short fur", shades=YELLOW, base=3, **SHORT),
    # the two legs on the far side, painted flat in the coat's brown: the same coat in the body's shadow
    dict(name="short fur, far legs", shades=[7, 6], base=1, **SHORT),
    # inside the ears: black and dark purple
    dict(name="short fur, ear insides", shades=[1, 15], base=0, **SHORT),
    # the spikes on the rump and back: the same yellow, standing up
    dict(name="fur", shades=[7, 6, 4, 3, 2], base=2, **LONG),
    # the white ruff: white and light gray, edged in dark gray
    dict(name="fur, ruff", shades=[11, 10, 9, 8], base=2, **LONG),
    # black pupil, purple iris, white catchlight and the brown line round the eye
    dict(name="eye (line art)", shades=[1, 7, 15, 8], finish=0.9, body=0),
]
# the pale patch on the forehead and the ear's pale rim are broad lit patches, not glints
KEEP_TOP = ["short fur", "fur", "fur, ruff"]
def to(name, colors): return {c: name for c in colors}
FAR, EAR, EYE, RUFF = "short fur, far legs", "short fur, ear insides", "eye (line art)", "fur, ruff"
COLORS = {1: "outline", **to("short fur", YELLOW), **to(RUFF, [11, 10, 9, 8]), 15: EAR}
RULES = [
    # the spikes; a brown stroke wholly inside them is one spike lying over the next
    dict(drawings=["ke02", "parts02", "parts03"], colors=to("fur", [7, 6, 4, 3, 2]),
         interior={6: ([1, 2, 3, 4], "outline")}),
    # the ruff; a dark gray stroke wholly inside it is one tuft over the next
    dict(drawings=["ke01", "parts01"], interior={11: ([1, 8, 9, 10], "outline")}),
    # the far legs
    dict(view="front", drawings=["br-leg01", "br-foot01"], colors=to(FAR, [7, 6])),
    dict(view="front", drawings=["karada2"], rect=[8, 15, 5, 3], colors=to(FAR, [6])),
    dict(view="back", drawings=["pr-leg01", "pr-foot01"], colors=to(FAR, [7, 6])),
    dict(view="back", drawings=["body01"], rect=[5, 17, 6, 3], colors=to(FAR, [7, 6])),
    dict(view="back", drawings=["image-2"], rect=[2, 2, 6, 8], colors=to(FAR, [7, 6])),
    # the mouth line and the nose's edge
    dict(view="front", drawings=["atama"], rect=[5, 15, 1, 1], colors={7: "outline"}),
    dict(view="front", drawings=["atama"], rect=[6, 17, 2, 1], colors=to("outline", [7, 6])),
    dict(view="front", drawings=["atama"], rect=[8, 18, 3, 1], colors={7: "outline"}),
    dict(view="front", drawings=["atama-eyes-*"], rect=[3, 10, 1, 1], colors={7: "outline"}),
    # the eyes, front: the far one at the head's edge, the near one with its brown rim; shut, a drawn line
    dict(view="front", drawings=["atama-eyes-open"], rect=[3, 6, 1, 3], colors=to(EYE, [8, 1, 15])),
    dict(view="front", drawings=["atama-eyes-open"], rect=[8, 7, 5, 4], colors=to(EYE, [7, 8, 1, 15])),
    dict(view="front", drawings=["atama-eyes-closed"], rect=[8, 9, 5, 2], colors=to("outline", [7, 5])),
    # the eye seen from behind, on the head and on the strip that lies over it
    dict(view="back", drawings=["body01-2"], rect=[16, 9, 3, 4], colors=to(EYE, [8, 1, 15])),
    dict(view="back", drawings=["body01-2-eyes-open"], rect=[0, 1, 3, 4], colors=to(EYE, [8, 1, 15])),
]
INSIDE = to(EAR, [1, 15])
FLOODS = [
    # the black of the ear insides, from the purple outward
    dict(view="front", drawing="l-ear01", seeds=[[14, 6]], through=[1, 15], colors=INSIDE),
    dict(view="back", drawing="body02-2", seeds=[[7, 11]], through=[1, 15], colors=INSIDE),
]
