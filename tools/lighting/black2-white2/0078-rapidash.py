# Rapidash: Ponyta's cream coat, hooves and fire (the same rows and dials), plus a horn and a red eye.
# Colors: 1 black; 2 white (eye catchlight); 3-7 the coat's cream down to its dark brown contour; 8-11 fire
# (8 also the ear insides and the iris); 12-14 the hooves' grays (12 also the eye's white in shade).
SOURCE = "sources/black2-white2/0078-rapidash.spu"
MATERIALS = [
    # black line; the shut eye's lid line is drawn partly in the coat's brown (6); two contour pixels on the
    # head and ear tip are drawn red (8) where the mane burns behind them
    dict(name="outline", shades=[1, 6, 8], finish=0.1, body=0),
    # the cream coat: its brown contour colors are its darkest shades. Front is painted in 3 and 4, back in 4 and 5
    dict(name="short fur", shades=[7, 6, 5, 4, 3], base=3, finish=-0.2, body=0.05),
    # the legs on the far side are painted a step darker all over (tan): the same coat in the body's shadow
    dict(name="short fur, far legs", shades=[7, 6, 5, 4], base=2, finish=-0.2, body=0.05),
    # inside the ears: red, orange at the base
    dict(name="short fur, ear inside", shades=[8, 9], base=0, finish=-0.2, body=0.05),
    # the forehead horn, painted in the coat's own colors: a hide-colored horn (Spines), solid
    dict(name="spines, horn", shades=[7, 6, 5, 4, 3], base=3, finish=0.4, body=0),
    # mane, tail, and the tufts on the back and legs: fire
    dict(name="flame", shades=[8, 9, 10, 11], base=1, finish=0, body=0),
    # gray hooves with a pale glint: hard horn
    dict(name="hooves", shades=[14, 13, 12], base=0, finish=0.7, body=0.05),
    dict(name="eye (line art)", shades=[1, 7, 8, 12, 2], finish=0.9, body=0),
]
def to(name, colors): return {c: name for c in colors}
COLORS = {1: "outline", **to("short fur", [7, 6, 5, 4, 3]), **to("flame", [8, 9, 10, 11]),
          **to("hooves", [14, 13, 12]), 2: "eye (line art)"}
EYE = to("eye (line art)", [1, 2, 7, 8, 12])
FAR = to("short fur, far legs", [7, 6, 5, 4])
FAR3 = to("short fur, far legs", [7, 6, 5])
EAR = to("short fur, ear inside", [8, 9])
HORN = to("spines, horn", [7, 6, 5, 4, 3])
def rects(drawing, view, colors, *rs): return [dict(view=view, drawings=[drawing], rect=r, colors=colors) for r in rs]
RULES = [
    # front: the raised far foreleg (thigh, shin) and the far hind leg, which is drawn inside the body, with its hoof's fetlock
    dict(view="front", drawings=["asi01", "asi02", "asi02-2", "atama-2"], colors=FAR),
    dict(view="front", drawings=["karada"], rect=[30, 31, 7, 14], colors=FAR3),
    # back: the far hind leg (left) and the far foreleg (right of the belly), both drawn inside the body
    dict(view="back", drawings=["body01"], rect=[1, 27, 12, 21], colors=FAR3),
    dict(view="back", drawings=["body01"], rect=[29, 31, 8, 17], colors=FAR3),
    # the ears' red insides
    *rects("atama", "front", EAR, [16, 8, 2, 5], [4, 12, 3, 3]),
    *rects("head01", "back", EAR, [14, 5, 4, 4]),
    # two contour pixels drawn red against the mane
    *rects("atama", "front", {8: "outline"}, [14, 6, 1, 1], [12, 11, 1, 1]),
    # the horn
    *rects("atama", "front", HORN, [4, 6, 3, 2], [5, 8, 3, 1], [5, 9, 5, 1], [6, 10, 5, 1]),
    *rects("head01", "back", HORN, [15, 1, 2, 1], [14, 2, 3, 1], [12, 3, 4, 1], [12, 4, 3, 1], [11, 5, 3, 1], [11, 6, 2, 1]),
    # the eye: brown lid, red iris, white and its gray shade, pupil
    dict(view="front", drawings=["atama"], rect=[14, 16, 3, 4], colors=EYE),
    dict(view="front", drawings=["atama-eyes-open"], rect=[3, 1, 3, 4], colors=EYE),
    dict(view="front", drawings=["atama-eyes-closed"], rect=[3, 1, 3, 4], colors={6: "outline"}),
    dict(view="back", drawings=["head01"], rect=[14, 11, 2, 4], colors=EYE),
    dict(view="back", drawings=["head01-eyes-open"], rect=[3, 2, 2, 4], colors=EYE),
    dict(view="back", drawings=["head01-eyes-closed"], rect=[3, 2, 2, 4], colors={6: "outline"}),
]
# Black 2: "its blazing mane sparkles"; Legends Arceus: "Fiery mane aglow". Ponyta's values.
GLOW = [
    dict(material="flame", colors=[11], glow=245, intent="the fire's yellow core is the brightest"),
    dict(material="flame", colors=[10], glow=220, intent="the fire's orange middle"),
    dict(material="flame", colors=[9], glow=195, intent="the fire's orange-red body"),
    dict(material="flame", colors=[8], glow=180, intent="the fire's red tongues are the dimmest"),
]
def AFTER(job):
    # as on Ponyta: the drawings differ little in how much fire they draw, so the swing is widened
    job.flicker(["hi0*", "ef0*"], low=0.4)
