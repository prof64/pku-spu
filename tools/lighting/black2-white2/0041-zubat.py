# Zubat: bare skin all over (Hide), thin wing membrane, fangs. No eyes ("It has no eyes", FireRed).
SOURCE = "sources/black2-white2/0041-zubat.spu"
BLUE, PURPLE = [9, 8, 7, 6], [13, 12, 11]
MATERIALS = [
    # black, and the wing's darkest purple where it is a line one pixel wide: the membrane's drawn edge along the
    # fingers. Left in the membrane row those lines lit up brighter than the membrane itself in the cave.
    dict(name="outline", shades=[4, 13], finish=0.1, body=0),
    # body, ears, the two tails, and the wing's arm and fingers where the purple membrane shows between them
    dict(name="hide", shades=BLUE, base=1, finish=0.25, body=0.08),
    dict(name="hide, ear insides", shades=PURPLE, base=1, finish=0.25, body=0.08),
    # the purple inner side of the wing
    dict(name="wing membrane", shades=PURPLE, base=1, finish=0.3, body=0.3),
    # a wing seen from its blue outer side: arm, fingers and membrane are drawn as one blue sheet
    dict(name="wing membrane, outer side", shades=BLUE, base=1, finish=0.45, body=0.3),
    # fangs: white, a light gray, and the dark gray the art draws their outer edge in
    dict(name="claws and teeth", shades=[3, 2, 1], base=2, finish=0.7, body=0.05),
    # the gray throat in the black mouth (front view only)
    dict(name="mouth", shades=[3], base=0, finish=0.8, body=0),
    # the dark inside of the open mouth, drawn black: part of the mouth, only tinted by light
    dict(name="mouth, dark inside", shades=[], finish=0.8, body=0),
]
def to(name, colors): return {c: name for c in colors}
COLORS = {4: "outline", **to("hide", BLUE), **to("wing membrane", PURPLE), **to("claws and teeth", [3, 2, 1])}
DARK = {4: "mouth, dark inside"}
RULES = [
    # each wing has a raised and a lowered drawing; one of the two shows the blue outer side only
    dict(view="front", drawings=["wing-l", "wing-r-2"], colors=to("wing membrane, outer side", BLUE)),
    dict(view="back", drawings=["wing-l", "wing-r-2"], colors=to("wing membrane, outer side", BLUE)),
    dict(drawings=["wing-*"], thin_all={13: "outline"}),
    dict(view="front", drawings=["mimi", "mimi-r"], colors=to("hide, ear insides", PURPLE)),
    # the open mouth: the black that fills it, the gray throat, the black under the upper lip and between the fangs
    dict(view="front", drawings=["body"], rect=[0, 3, 11, 10], colors={**DARK, 3: "mouth"}),
    dict(view="front", drawings=["mouse2", "mouse2-female"], colors=DARK),
    dict(view="front", drawings=["mouse", "mouse-female"], rect=[0, 0, 9, 3], colors=DARK),
]
# the palest blue is the lit upper lip, ear and wing edge: a tenth of the front view's skin, shading and not a glint
KEEP_TOP = ["hide"]
