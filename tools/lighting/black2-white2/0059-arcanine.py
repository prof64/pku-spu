SOURCE = "sources/black2-white2/0059-arcanine.spu"
# Arcanine: an orange coat with black stripes, and long cream fur everywhere else: the mane around the head
# and chest ("its grand mane", Gold), the tail, the tufts behind each leg. Nothing glows: the fire of the
# Pokédex entries is "within this POKéMON's body" (Ruby). The painted art shades every part flat and soft,
# so all of it is matte: the smooth-edged orange is the sleek coat (Short fur), the ragged cream the long one
# (Fur), as on Growlithe.
SHORT = dict(finish=-0.2, body=0.05)
MATERIALS = [
    # black line; the lines between clumps of the long fur and the mouth line are drawn in the two dark browns
    dict(name="outline", shades=[15, 14, 10], finish=0.1, body=0),
    # the orange coat: its dark-brown contour is its darkest shade. Both views are painted in 13
    dict(name="short fur", shades=[14, 13, 12, 11], base=1, **SHORT),
    # the black stripes: black in shade, gray-brown where the art lights them
    dict(name="short fur, stripes", shades=[15, 3], base=0, **SHORT),
    # inside the ear (front view): tan and cream
    dict(name="short fur, ear inside", shades=[10, 9, 8], base=1, **SHORT),
    # mane, tail and leg tufts: long ragged fur. Two dark browns for its contour, a mid brown on its lit tips
    dict(name="fur", shades=[14, 10, 7, 9, 8], base=3, finish=-0.1, body=0.05),
    # the nose, drawn in the stripes' gray-brown with one pale glint: light only tints it
    dict(name="nose", shades=[], finish=0.25, body=0.08),
    # the red pads under the hind feet (back view): bare skin, painted in one flat color
    dict(name="dry hide, paw pads", shades=[5], base=0, finish=0.05, body=0.03),
    # the one fang; the palette's pale gray (drawn in the eye and on the nose) is its shade
    dict(name="claws and teeth", shades=[2, 1], base=1, finish=0.7, body=0.05),
    dict(name="eye (line art)", shades=[15, 2, 1], finish=0.9, body=0),
]
# The lightest orange is few of the coat's pixels overall but a broad painted patch on the thigh, the paws
# and the ears: a shade, not a glint (as on Growlithe's face).
KEEP_TOP = ["short fur"]
def to(name, colors): return {c: name for c in colors}
STRIPES = "short fur, stripes"
COLORS = {15: "outline", **to("short fur", [14, 13, 12, 11]), **to("fur", [10, 7, 9, 8]), 3: STRIPES,
          5: "dry hide, paw pads", **to("claws and teeth", [2, 1])}
EYE = to("eye (line art)", [15, 2, 1])
# a dark stroke wholly inside the cream: one clump of fur over the next (and the mouth line)
TUFTS = {10: ([7, 8, 9, 14, 15], "outline"), 14: ([7, 8, 9, 10, 15], "outline")}
RULES = [
    # drawings that are cream fur: the darker brown is the fur's contour too
    dict(drawings=["atama", "munage", "kakato", "o1", "o2", "usiroiagmi", "asige", "fur-*", "tail-*", "head-a", "head-b"],
         colors={14: "fur"}, interior=TUFTS),
    # the orange mask around the eye (front) and the orange cheek and ear seen from behind
    dict(view="front", drawings=["atama"], rect=[10, 21, 8, 5], colors={14: "short fur"}),
    dict(view="back", drawings=["head-b"], rect=[21, 14, 6, 8], colors={14: "short fur"}),
    # the belly fur under the body (back view)
    dict(view="back", drawings=["body"], rect=[13, 29, 21, 8], colors={14: "fur"}),
    # the ear seen from the front: its tan inside
    dict(view="front", drawings=["mimi1"], colors=to("short fur, ear inside", [10, 9, 8])),
    # the eye: pupil, white and its shade
    dict(view="front", drawings=["atama-eyes-open"], rect=[5, 3, 4, 3], colors=EYE),
    # the nose, front and seen from behind
    dict(view="front", drawings=["atama"], rect=[2, 29, 4, 3], colors=to("nose", [3, 2])),
    dict(view="back", drawings=["head-a"], rect=[33, 7, 4, 4], colors=to("nose", [3, 2])),
    # the stripes: black wider than a line is stripe, one-pixel strokes stay the drawn line
    dict(drawings=["karada", "asi", "asi2", "body", "foot-b", "foot-f"], colors={15: STRIPES}, thin_all={15: "outline"}),
]
