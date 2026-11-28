# Magmar: matte red and yellow hide, fire on the tail tip and on the two lumps of the head, a duck-like bill,
# white claws, hide-colored spikes down the back, black bands at the neck and ankles.
# "Its body always burns with an orange glow that enables it to hide perfectly among flames" (Red/Blue);
# "The fiery surface of its body gives off a wavering, rippling glare that is similar to the sun" (Silver).
SOURCE = "sources/black2-white2/0126-magmar.spu"
HIDE = dict(finish=0.25, body=0.08)
RED, YELLOW = [6, 5, 4, 3], [11, 10, 9, 8, 7]
MATERIALS = [
    # black line; the dark tail tip under the fire and the brown contour of the head's flames are drawn line
    dict(name="outline", shades=[1, 6, 11], finish=0.1, body=0),
    # the red hide: its maroon contour is its darkest shade. Both views are painted mostly in the crimson (5)
    dict(name="hide", shades=RED, base=1, **HIDE),
    # belly, thighs, shoulders and tail: the same hide in yellow, its brown contour its darkest shade
    dict(name="hide, yellow", shades=YELLOW, base=2, **HIDE),
    # the spikes down the back: hardened, hide-colored
    dict(name="spines", shades=[6, 5, 4], base=1, finish=0.4, body=0),
    dict(name="beak", shades=[6, 3, 2], base=1, finish=0.4, body=0.05),
    dict(name="claws and teeth", shades=[14, 13, 12], base=2, finish=0.7, body=0.05),
    # the black bands at the neck and ankles with their painted gray glint: light only tints them
    dict(name="neck and ankle bands", shades=[], finish=0.2, body=0),
    dict(name="mouth", shades=[5, 4], base=0, finish=0.8, body=0),
    dict(name="tail flame", shades=[5, 4, 8], base=1, finish=0, body=0),
    dict(name="head flames", shades=[10, 9, 8], base=2, finish=0, body=0),
    dict(name="eye (line art)", shades=[1, 14, 13, 12], finish=0.9, body=0),
]
def to(name, colors): return {c: name for c in colors}
COLORS = {1: "outline", **to("beak", [3, 2]), **to("hide", [6, 5, 4]), **to("hide, yellow", YELLOW),
          **to("claws and teeth", [14, 13, 12])}
BAND = to("neck and ankle bands", [1, 14])
EYE = to("eye (line art)", [1, 14, 13, 12])
SPINE = to("spines", [6, 5, 4])
RULES = [
    # the fire on the tail: only its own colors; the dark tail tip drawn under it is line
    dict(drawings=["hi*", "ef01*"], colors={**to("tail flame", [8, 4, 5]), 6: "outline", 11: "outline"}),
    # the two flames on the head, with their brown contour as line; the pale spot on the lump behind them is the hide's glint
    dict(drawings=["part-4", "head02"], colors={**to("head flames", [10, 9, 8]), 11: "outline", 3: "hide"}),
    # the neck band
    dict(view="front", drawings=["body"], rect=[6, 8, 9, 5], colors=BAND),
    dict(view="back", drawings=["body01"], rect=[22, 7, 9, 4], colors=BAND),
    # the ankle bands
    dict(view="front", drawings=["foot"], rect=[6, 14, 7, 2], colors=BAND),
    dict(view="front", drawings=["foot-l"], rect=[4, 12, 6, 3], colors=BAND),
    dict(view="back", drawings=["r-leg01"], rect=[5, 16, 6, 4], colors=BAND),
    dict(view="back", drawings=["l-leg01"], rect=[5, 17, 5, 3], colors=BAND),
    # the spikes seen from the front: one behind the neck, two behind the arm
    dict(view="front", drawings=["body"], rect=[16, 1, 8, 7], colors=SPINE),
    dict(view="front", drawings=["body"], rect=[23, 12, 9, 12], colors=SPINE),
    # the dark edges of the three blades seen from behind (their faces are picked below)
    *[dict(view="back", drawings=["body01"], rect=r, colors=SPINE) for r in
      ([11, 5, 4, 1], [15, 6, 1, 1], [18, 7, 1, 1], [17, 10, 1, 1], [7, 11, 4, 1], [11, 12, 2, 1], [6, 19, 5, 1], [13, 20, 2, 1])],
    # the bill: its maroon contour is its darkest shade; the red inside the open bill is the mouth
    dict(view="front", drawings=["head"], rect=[2, 16, 13, 6], colors={6: "beak"}),
    dict(view="front", drawings=["head-eyes-*"], rect=[2, 4, 8, 2], colors={6: "beak"}),
    dict(view="front", drawings=["head-eyes-*"], rect=[12, 5, 1, 1], colors={6: "beak"}),
    dict(view="back", drawings=["head01"], rect=[20, 9, 8, 5], colors={6: "beak"}),
    dict(view="back", drawings=["head01-eyes-*"], rect=[1, 4, 5, 2], colors={6: "beak"}),
    dict(view="front", drawings=["mouse"], colors={6: "beak"}),
    dict(view="front", drawings=["mouse"], rect=[6, 5, 2, 3], colors=to("mouth", [5, 4])),
    dict(view="back", drawings=["mouth01"], rect=[4, 8, 7, 3], colors={6: "beak"}),
    # the eyes: white, gray edge and pupil
    dict(view="front", drawings=["head"], rect=[3, 14, 1, 2], colors=EYE),
    dict(view="front", drawings=["head-eyes-open"], rect=[2, 2, 5, 3], colors=EYE),
    dict(view="front", drawings=["head-eyes-open"], rect=[8, 3, 6, 2], colors=EYE),
    dict(view="back", drawings=["head01"], rect=[21, 8, 4, 2], colors=EYE),
    dict(view="back", drawings=["head01-eyes-open"], rect=[1, 3, 4, 2], colors=EYE),
    # the ridges drawn across the arms: one scale over the next
    dict(drawings=["hand-l", "hand-r", "r-arm01", "l-arm01"], interior={6: ([4, 5], "outline")}),
]
# the faces of the three blades on the back, each closed off by black line
FLOODS = [dict(view="back", drawing="body01", seeds=[[11, 6], [8, 12], [8, 20]], through=[4, 5], colors=to("spines", [4, 5]))]
# The whole body glows by the text, but faintly: the fire is the light. At 0 the feet went dark in the cave beside
# the flames; at 20 the hide lost its shading and lit the cave by itself.
BODY_GLOW = 8
GLOW = [
    dict(material="tail flame", colors=[8], glow=245, intent="the flame's yellow core is the brightest"),
    dict(material="tail flame", colors=[4], glow=215, intent="the flame's orange middle"),
    dict(material="tail flame", colors=[5], glow=180, intent="the flame's red tongues are the dimmest"),
    dict(material="head flames", colors=[8], glow=245, intent="the head flames' yellow core"),
    dict(material="head flames", colors=[9], glow=215, intent="the head flames' darker yellow"),
    dict(material="head flames", colors=[10], glow=180, intent="the head flames' orange edge is the dimmest"),
    dict(material="hide", glow=BODY_GLOW, intent="its body always burns with an orange glow"),
    dict(material="hide, yellow", glow=BODY_GLOW, intent="its body always burns with an orange glow"),
    dict(material="spines", glow=BODY_GLOW, intent="its body always burns with an orange glow"),
]
def AFTER(job):
    job.flicker(["hi", "ef01"])
