# Flareon: an orange-red coat, and long cream fur on the head tuft, the ruff and the tail ("Flareon's fluffy
# fur ... releases heat into the air", Ruby/Sapphire; "It fluffs out its fur collar to cool down", Silver).
# The painted art shades every part flat and soft, with no highlight but the eye, so all of it is matte: the
# smooth-edged coat is the sleek one (Short fur, as on Growlithe and Ponyta), the ragged cream the long one
# (Fur at -0.1: at -0.7 anything bigger than a tuft goes grainy). Its fire is inside ("It has a flame sac in
# its body"), and no entry says the body shines, so nothing glows.
SOURCE = "sources/black2-white2/0136-flareon.spu"
SHORT = dict(finish=-0.2, body=0.05)
LONG = dict(finish=-0.1, body=0.05)
MATERIALS = [
    # black line; the nose's edge and the shut eyes' lid lines in the coat's dark reds; the lines between
    # clumps of the long fur in its dark brown
    dict(name="outline", shades=[1, 6, 5, 10], finish=0.1, body=0),
    # the orange-red coat: its dark red-brown contour is its darkest shade. Legs and the whole back view are
    # painted in 4, the face and the near flank a step lighter
    dict(name="short fur", shades=[6, 5, 4, 3], base=2, **SHORT),
    # the leg on the far side, painted flat in the coat's dark red: the same coat in the body's shadow
    dict(name="short fur, far legs", shades=[6, 5], base=1, **SHORT),
    # inside the ear (front view): black and navy
    dict(name="short fur, ear insides", shades=[1, 12], base=0, **SHORT),
    # the head tuft, the ruff and the tail: long cream fur, edged in dark brown. Most of it, and nearly all
    # of the back view, is painted in 9
    dict(name="fur", shades=[10, 9, 8, 7], base=1, **LONG),
    # black pupil, navy iris, white catchlight and the dark red line round the near eye
    dict(name="eye (line art)", shades=[1, 6, 5, 12, 11], finish=0.9, body=0),
]
# the pale cream and the lighter orange are broad lit areas, not glints
KEEP_TOP = ["short fur", "fur"]
def to(name, colors): return {c: name for c in colors}
FAR, EAR, EYE = "short fur, far legs", "short fur, ear insides", "eye (line art)"
COLORS = {1: "outline", **to("short fur", [6, 5, 4, 3]), **to("fur", [10, 9, 8, 7]), 12: EAR, 11: EYE}
RULES = [
    # a dark brown stroke wholly inside the long fur is one clump lying over the next
    dict(drawings=["head", "image-3", "neck", "tail2*", "atama-ke", "ke", "o", "o-2"],
         interior={10: ([1, 7, 8, 9], "outline")}),
    # the far foreleg
    dict(view="front", drawings=["foot31"], colors=to(FAR, [6, 5])),
    # the eyes, on the head and on the strip that lies over it (1 right and 12 down of it): the far one at
    # the head's edge, the near one with its dark red rim
    dict(view="front", drawings=["head"], rect=[2, 19, 2, 3], colors=to(EYE, [11, 1, 12])),
    dict(view="front", drawings=["head"], rect=[9, 19, 5, 4], colors=to(EYE, [11, 1, 12])),
    dict(view="front", drawings=["head"], rect=[9, 19, 2, 4], colors=to(EYE, [6, 5])),
    dict(view="front", drawings=["head-eyes-open"], rect=[1, 7, 2, 3], colors=to(EYE, [11, 1, 12])),
    dict(view="front", drawings=["head-eyes-open"], rect=[8, 7, 5, 4], colors=to(EYE, [11, 1, 12])),
    dict(view="front", drawings=["head-eyes-open"], rect=[8, 7, 2, 4], colors=to(EYE, [6, 5])),
    # shut, they are drawn lines
    dict(view="front", drawings=["head-eyes-closed"], rect=[2, 8, 1, 1], colors={5: "outline"}),
    dict(view="front", drawings=["head-eyes-closed"], rect=[8, 8, 5, 3], colors=to("outline", [6, 5])),
    # the nose's edge
    dict(view="front", drawings=["head"], rect=[5, 23, 1, 1], colors={6: "outline"}),
    dict(view="front", drawings=["head-eyes-*"], rect=[4, 11, 1, 1], colors={6: "outline"}),
]
FLOODS = [
    # the black of the ear's inside, from the navy outward
    dict(view="front", drawing="mimi", seeds=[[14, 10]], through=[1, 12], colors=to(EAR, [1, 12])),
]
