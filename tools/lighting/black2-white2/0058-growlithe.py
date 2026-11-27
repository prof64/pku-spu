SOURCE = "sources/black2-white2/0058-growlithe.spu"
# Growlithe: an orange coat with black stripes, a cream muzzle, and long cream fur on the crest, the chest
# ruff and the tail. Nothing glows. The painted art shades every part flat and soft (no highlight but the
# nose, the eye and the claws), so the coat is matte: the smooth-edged orange and muzzle are the sleek coat
# (Short fur), the ragged cream tufts the long one (Fur), as on Munchlax.
SHORT = dict(finish=-0.2, body=0.05)
MATERIALS = [
    # black line; the mouth line and the lines between clumps of the long fur are drawn in the cream's dark brown
    dict(name="outline", shades=[15, 10], finish=0.1, body=0),
    # the orange coat: its dark-brown contour is its darkest shade. Body and legs, front and back, are painted
    # in 13; the head is a step or two lighter
    dict(name="short fur", shades=[14, 13, 12, 11], base=1, **SHORT),
    # the black stripes: black in shade, gray where the art lights them (the top of the back)
    dict(name="short fur, stripes", shades=[15, 3], base=0, **SHORT),
    # the cream muzzle and jaw: drawn smooth-edged like the coat
    dict(name="short fur, muzzle", shades=[10, 9, 8, 7], base=3, **SHORT),
    # inside the ear: tan, painted dark
    dict(name="short fur, ear inside", shades=[10, 9], base=0, **SHORT),
    # the crest, the chest ruff and the tail: long ragged fur. The front paints it in 7 and 8, the back in 9 and 7
    dict(name="fur", shades=[10, 9, 8, 7], base=2, finish=-0.7, body=0.05),
    # the black nose and its one painted glint: light only tints it
    dict(name="nose", shades=[], finish=0.25, body=0.08),
    # white claws, their gray shade and dark-gray edge; the two fangs of the open mouth
    dict(name="claws and teeth", shades=[3, 2, 1], base=1, finish=0.7, body=0.05),
    dict(name="mouth", shades=[6, 5, 4], base=1, finish=0.8, body=0),
    dict(name="eye (line art)", shades=[15, 3, 2, 1], finish=0.9, body=0),
]
# The lightest orange is few of the coat's pixels overall but a broad painted band across the face:
# a shade, not a glint (as on Electrike's crest).
KEEP_TOP = ["short fur"]
def to(name, colors): return {c: name for c in colors}
MUZZLE, STRIPES = "short fur, muzzle", "short fur, stripes"
COLORS = {15: "outline", **to("short fur", [14, 13, 12, 11]), **to("fur", [10, 9, 8, 7]), 3: STRIPES,
          **to("claws and teeth", [2, 1]), **to("mouth", [6, 5, 4])}
EYE = to("eye (line art)", [15, 3, 2, 1])
TUFTS = {10: ([7, 8, 9, 15], "outline")}          # a dark stroke wholly inside the cream: one clump over the next
RULES = [
    # the head: the cream below the eye is the muzzle, the cream above it the crest
    dict(view="front", drawings=["atam", "atam-2"], rect=[0, 19, 32, 13], colors=to(MUZZLE, [10, 9, 8, 7])),
    dict(view="front", drawings=["atam*-eyes-*"], colors=to(MUZZLE, [10, 8, 7])),
    # the mouth line (upper lip over the jaw) is a drawn line
    dict(view="front", drawings=["atam", "atam-2"], interior=TUFTS),
    # the ear seen from the front: its tan inside
    dict(view="front", drawings=["atam", "atam-2"], rect=[20, 11, 7, 7], colors=to("short fur, ear inside", [10, 9])),
    # the eye: pupil, gray iris, white and its shade
    dict(view="front", drawings=["atam", "atam-2"], rect=[13, 15, 6, 5], colors=EYE),
    dict(view="front", drawings=["atam*-eyes-open"], rect=[6, 6, 6, 4], colors=EYE),
    # the nose: a black blob with one white glint
    dict(view="front", drawings=["atam", "atam-2"], rect=[5, 18, 5, 3], colors={15: "nose", 1: "nose"}),
    # the stripes: black wider than a line is stripe, one-pixel strokes stay the drawn line
    dict(drawings=["karada", "asi01", "asi02", "r-asi1b-2", "r-asi2", "r-asi1a", "r-asi1a-2", "p-u-foot-l1"],
         colors={15: STRIPES}, thin_all={15: "outline"}),
    # the claws
    dict(view="front", drawings=["asi01"], rect=[0, 12, 32, 5], colors={3: "claws and teeth"}),
    dict(view="back", drawings=["karada2b"], colors={3: "claws and teeth"}),
    # clumps of the long fur
    dict(drawings=["munage", "o01", "o01-2", "shippo", "p-u-foot-l2-2", "l-asi2", "l-asi2-2"], interior=TUFTS),
]
