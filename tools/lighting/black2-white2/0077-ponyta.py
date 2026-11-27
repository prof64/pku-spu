SOURCE = "sources/black2-white2/0077-ponyta.spu"
MATERIALS = [
    # black line; the shut eye's lid line is drawn partly in the coat's dark brown
    dict(name="outline", shades=[1, 7], finish=0.1, body=0),
    # the cream coat: its brown contour colors are its darkest shades. Front is painted in 3 and 4, back in 4
    dict(name="short fur", shades=[7, 6, 5, 4, 3], base=3, finish=-0.2, body=0.05),
    # the two legs on the far side are painted a step darker all over (tan, brown thigh): the same coat in the body's shadow
    dict(name="short fur, far legs", shades=[7, 6, 5], base=2, finish=-0.2, body=0.05),
    # inside the ear (front view): red with a dark rim
    dict(name="short fur, ear inside", shades=[7, 8], base=1, finish=-0.2, body=0.05),
    # mane, tail, and the tufts on the back and legs: fire
    dict(name="flame", shades=[8, 9, 10, 11], base=1, finish=0, body=0),
    # navy hooves with a pale glint: hard horn
    dict(name="hooves", shades=[14, 13, 12], base=0, finish=0.7, body=0.05),
    dict(name="eye (line art)", shades=[1, 7, 2], finish=0.9, body=0),
]
def to(name, colors): return {c: name for c in colors}
COLORS = {1: "outline", **to("short fur", [7, 6, 5, 4, 3]), **to("flame", [8, 9, 10, 11]),
          **to("hooves", [14, 13, 12]), 2: "eye (line art)"}
EYE = to("eye (line art)", [1, 2, 7])
FAR = to("short fur, far legs", [7, 6, 5])
RULES = [
    # far-side legs (their top rows painted in the body's cream stay coat)
    dict(view="front", drawings=["usiro02", "mae01", "mae01-2"], colors=FAR),
    dict(view="back", drawings=["leg-fl", "leg-bl", "foot-fl", "foot-bl"], colors=FAR),
    # the ear seen from the front: its red inside and that inside's dark rim
    dict(view="front", drawings=["mimi"], rect=[3, 2, 3, 5], colors=to("short fur, ear inside", [7, 8])),
    # the eye: pupil, catchlight and dark brown iris ring
    dict(view="front", drawings=["atama", "atama-[23]"], rect=[10, 20, 5, 4], colors=EYE),
    dict(view="front", drawings=["atama*-eyes-open"], rect=[2, 4, 5, 4], colors=EYE),
    dict(view="front", drawings=["atama*-eyes-closed"], rect=[2, 4, 5, 4], colors={7: "outline"}),
    dict(view="back", drawings=["head", "head-[23]"], rect=[25, 21, 4, 4], colors=EYE),
    dict(view="back", drawings=["head*-eyes-open"], rect=[2, 2, 4, 4], colors=EYE),
    dict(view="back", drawings=["head*-eyes-closed"], rect=[2, 2, 4, 4], colors={7: "outline"}),
]
GLOW = [
    dict(material="flame", colors=[11], glow=245, intent="the fire's yellow core is the brightest"),
    dict(material="flame", colors=[10], glow=220, intent="the fire's orange middle"),
    dict(material="flame", colors=[9], glow=195, intent="the fire's orange-red body"),
    dict(material="flame", colors=[8], glow=180, intent="the fire's red tongues are the dimmest"),
]
def AFTER(job):
    # the drawings differ little in how much fire they draw, so the swing is widened: the smallest tail drawing shines 0.85
    job.flicker(["atama", "kubi", "sipo", "senaka", "asinohi", "head", "neck", "tail", "fire-senaka", "fire-ashi"], low=0.4)
