# Machamp: bare bluish-gray skin over muscle (Hide) everywhere; the three head ridges, the lips and the black
# "briefs" are that same skin in other colors; the belt it wears is a dark strap with a golden plate and studs.
SOURCE = "sources/black2-white2/0068-machamp.spu"
H = dict(finish=0.25, body=0.08)          # Hide: plain bare skin
GOLD = [7, 8, 9, 10, 11]
MATERIALS = [
    # black, and one stray dark pixel (2) on a back-view hand
    dict(name="outline", shades=[1, 2], finish=0.1, body=0),
    # the skin: its dark blue-gray contour and shadow (3) is its darkest shade
    dict(name="hide", shades=[3, 4, 5], base=1, **H),
    # the few palest pixels (6) on the chest, fists, arms and thighs: the same skin at its most lit. In their own
    # row so they go dark with the body; left as painted glints they stayed pale on a body in shade and read as shine
    dict(name="hide, lit patches", shades=[3, 4, 5, 6], base=1, **H),
    # "three brown ridges right above its eyes": the same skin, painted in the yellow-browns
    dict(name="hide, head ridges", shades=GOLD, base=2, **H),
    # "large, pale, yellow lips"
    dict(name="hide, lips", shades=GOLD, base=3, **H),
    # "black markings that resemble briefs": pigment in the skin, painted black with a dark gray lighter patch
    dict(name="hide, briefs marking", shades=[1, 2], base=0, **H),
    # the belt's strap: dark, dull leather between two black lines
    dict(name="belt strap", shades=[2], base=0, finish=0.1, body=0),
    # the golden plate of the belt and the studs along the strap: hard and dull. The art paints them flat pale
    # yellow with no highlight; as metal the plate mirrored the grass and went green in a field
    dict(name="belt plate", shades=GOLD, base=3, finish=0.2, body=0),
    # the red letter on the plate: color on the same plate
    dict(name="belt plate, emblem", shades=[13], base=0, finish=0.2, body=0),
    dict(name="mouth", shades=[13, 12], base=1, finish=0.8, body=0),
    dict(name="eye (line art)", shades=[13, 12, 14, 15], finish=0.9, body=0),
]
def to(name, colors): return {c: name for c in colors}
COLORS = {1: "outline", 2: "outline", **to("hide", [3, 4, 5]), 6: "hide, lit patches", **to("hide, head ridges", GOLD),
          **to("mouth", [12, 13]), **to("eye (line art)", [14, 15])}
LIPS = to("hide, lips", GOLD)
RIDGE = to("hide, head ridges", GOLD)
EYE = to("eye (line art)", [12, 13, 14, 15])
BELT = {**to("belt plate", GOLD), 13: "belt plate, emblem"}
RULES = [
    # front head: the ridges run down between the eyes; everything yellow below them is lip
    dict(view="front", drawings=["atama", "atama-2"], rect=[0, 12, 24, 12], colors=LIPS),
    dict(view="front", drawings=["atama", "atama-2"], rect=[17, 11, 2, 1], colors=LIPS),     # the lip's raised corner
    dict(view="front", drawings=["atama", "atama-2"], rect=[8, 12, 1, 1], colors=RIDGE),    # the middle ridge's tip
    # the eye pictures lie over the same place: eyes, the ends of the ridges, the lip under them
    dict(drawings=["atama*-eyes-*"], colors=EYE),
    dict(drawings=["atama*-eyes-*"], rect=[0, 8, 32, 8], colors=LIPS),
    dict(drawings=["atama*-eyes-*"], rect=[16, 8, 1, 1], colors=RIDGE),
    # body: the belt's plate, its red letter and its studs
    dict(drawings=["karada", "body"], colors=BELT),
    # the strap between its two black lines
    dict(view="front", drawings=["karada"], rect=[18, 32, 12, 3], colors={2: "belt strap"}),
    dict(view="back", drawings=["body"], rect=[0, 33, 32, 3], colors={2: "belt strap"}),
    # the briefs below the belt
    dict(view="front", drawings=["karada"], rect=[0, 36, 40, 12], colors=to("hide, briefs marking", [1, 2])),
    dict(view="back", drawings=["body"], rect=[0, 37, 32, 11], colors=to("hide, briefs marking", [1, 2])),
]
