# Moltres: a yellow-feathered bird whose crest, tail and flight feathers are fire (Yellow: "flaming wings";
# FireRed: "orange wings that seem to be on fire"). Body, head and wing arms are plain matte plumage.
# Colors: 1 black; 5 4 3 2 the plumage, dark brown contour up to pale yellow; 6 7 8 9 fire, red to its yellow core;
# 12 11 10 the pink-brown beak and legs (12 is also the near-black line round the head and the brow);
# 13 white (eye, claws), 14 the eye white's gray, 15 the claws' gray.
SOURCE = "sources/black2-white2/0146-moltres.spu"
F = dict(finish=-0.2, body=0.05)
MATERIALS = [
    # black line; the head's contour and brow are drawn in the darkest brown (12); in the wings the brown
    # strokes (5) between feather layers, and between the feathers and the fire, are lines
    dict(name="outline", shades=[1, 12, 5], finish=0.1, body=0),
    # plumage: front is painted in 3 and 4, back almost all in 4
    dict(name="feathers", shades=[5, 4, 3, 2], base=1, **F),
    # crest, tail and the wings' flight feathers: fire
    dict(name="flame", shades=[6, 7, 8, 9], base=0, finish=0, body=0),
    dict(name="beak", shades=[12, 11, 10], base=2, finish=0.4, body=0.05),
    dict(name="dry hide, legs", shades=[12, 11, 10], base=1, finish=0.05, body=0.03),
    dict(name="claws and teeth", shades=[15, 13], base=1, finish=0.7, body=0.05),
    dict(name="eye (line art)", shades=[1, 12, 11, 14, 13], finish=0.9, body=0),
]
# the pale yellow (2) is the plumage's lit top (a broad patch on the body, a band along each wing), not a glint:
# left out of the row it stayed pale on a body gone dark in the cave
KEEP_TOP = ["feathers"]
def to(name, colors): return {c: name for c in colors}
LINE, EYE, BEAK, LEGS = "outline", "eye (line art)", "beak", "dry hide, legs"
COLORS = {1: LINE, 12: LINE, **to("feathers", [5, 4, 3, 2]), **to("flame", [6, 7, 8, 9]),
          **to(BEAK, [11, 10]), **to("claws and teeth", [15, 13]), 14: EYE}

HEAD = {"front": ("atama", 11, 7), "back": ("head", 13, 5)}     # the head drawing, and where the eye drawings sit on it
def head(view, rect, colors, eyes="*"):
    """A rule for a region of the head, given once for the head and for the eye drawings laid over it."""
    name, ox, oy = HEAD[view]
    return [dict(view=view, drawings=[name], rect=rect, colors=colors),
            dict(view=view, drawings=[name + "-eyes-" + eyes], rect=[rect[0]-ox, rect[1]-oy, rect[2], rect[3]], colors=colors)]

WINGS = ["hane01", "hane01-[234]", "hane02", "hane02-2", "wing-l", "wing-l-[234]", "wing-r", "wing-r-[234]"]
RULES = [
    # wings: layers of feathers over fire; the brown strokes between them are creases
    dict(drawings=WINGS, thin_all={5: LINE}),
    # legs and feet: bare skin with dark scutes; the brown stroke where a thigh meets the body is a line
    dict(drawings=["asi0*", "foot-*"], colors={**to(LEGS, [12, 11, 10]), 5: LINE}),
    # front head: the beak with its dark contour, then the eye (brow, white, its gray, pupil)
    *head("front", [5, 13, 9, 10], to(BEAK, [12, 11, 10])),
    *head("front", [12, 8, 5, 5], to(EYE, [1, 12, 11, 13, 14]), eyes="open"),
    # back head: the beak (the line between its halves, drawn in 12, stays a line), then the eye;
    # the brown pixel behind the eye is the end of the lid line and is there with the eye shut too
    *head("back", [17, 8, 7, 6], to(BEAK, [11, 10])),
    *head("back", [15, 7, 3, 3], to(EYE, [1, 12, 11, 13, 14]), eyes="open"),
    *head("back", [15, 8, 1, 1], to(EYE, [11]), eyes="closed"),
]
# Yellow: "As it flaps its flaming wings, even the night sky will turn red." Ponyta's values.
GLOW = [
    dict(material="flame", colors=[9], glow=245, intent="the fire's yellow core is the brightest"),
    dict(material="flame", colors=[8], glow=220, intent="the fire's orange middle"),
    dict(material="flame", colors=[7], glow=195, intent="the fire's orange-red body"),
    dict(material="flame", colors=[6], glow=180, intent="the fire's red tongues are the dimmest"),
]
def AFTER(job):
    # as on Ponyta: the drawings differ little in how much fire they draw, so the swing is widened
    job.flicker(["hane01", "hane02", "hi01", "o", "tosaka", "tail", "wing-l", "wing-r"], low=0.4)
