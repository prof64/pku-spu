# Machoke: bare gray-purple skin over muscle (Hide) everywhere, as on Machamp; the crest on its head, the red
# stripes on its arms and the dark "briefs" are that same skin in other colors; the power-save belt it wears is a
# dark strap with a golden plate and studs.
SOURCE = "sources/black2-white2/0067-machoke.spu"
H = dict(finish=0.25, body=0.08)          # Hide: plain bare skin
GOLD = [8, 9, 10, 11]
MATERIALS = [
    dict(name="outline", shades=[1], finish=0.1, body=0),
    # the skin: its dark purple contour and muscle lines (3) are its darkest shade
    dict(name="hide", shades=[3, 4, 5, 6], base=1, **H),
    # the few palest pixels (7) on the snout, shoulders, knees, knuckles and toes: the same skin at its most lit.
    # In their own row so they go dark with the body (Machamp's file says why)
    dict(name="hide, lit patches", shades=[3, 4, 5, 6, 7], base=1, **H),
    # the crest on its head: the same skin, painted in the yellow-browns
    dict(name="hide, head ridges", shades=GOLD, base=1, **H),
    # the red stripes on its forearms: pigment in the skin; the purple-red (12) is their edge
    dict(name="hide, arm stripes", shades=[12, 13], base=1, **H),
    # the dark "briefs": pigment in the skin, painted dark gray with black where it turns under
    dict(name="hide, briefs marking", shades=[1, 2], base=1, **H),
    # the belt's strap: dark, dull leather
    dict(name="belt strap", shades=[2], base=0, finish=0.1, body=0),
    # the golden plate of the belt and the studs along the strap: hard and dull. The art paints them flat pale
    # yellow with no highlight (on Machamp, as metal, the plate mirrored the grass and went green in a field)
    dict(name="belt plate", shades=GOLD, base=2, finish=0.2, body=0),
    # the red letter on the plate: color on the same plate
    dict(name="belt plate, emblem", shades=[13], base=0, finish=0.2, body=0),
    dict(name="eye (line art)", shades=[13, 12, 14, 15], finish=0.9, body=0),
]
def to(name, colors): return {c: name for c in colors}
COLORS = {1: "outline", 2: "hide, briefs marking", **to("hide", [3, 4, 5, 6]), 7: "hide, lit patches",
          **to("hide, head ridges", GOLD), **to("hide, arm stripes", [12, 13]), **to("eye (line art)", [14, 15])}
BRIEFS = "hide, briefs marking"
BELT = {**to("belt plate", GOLD), 13: "belt plate, emblem"}
RULES = [
    # the eye pictures: the eye and the sliver of the far eye; the crest above them stays crest
    dict(drawings=["atama-eyes-*"], colors=to("eye (line art)", [12, 13, 14, 15])),
    # waist: the belt's plate, its red letter and its studs
    dict(drawings=["karada2", "body"], colors=BELT),
    # black wholly inside the briefs is the briefs turning under, not line art; their edge stays the outline
    dict(drawings=["karada2", "body"], interior={1: ([2], BRIEFS)}),
    # the strap, above the briefs, and the black lines along it
    dict(view="front", drawings=["karada2"], rect=[0, 0, 24, 7], colors={1: "outline", 2: "belt strap"}),
    dict(view="back", drawings=["body"], rect=[0, 0, 24, 7], colors={1: "outline", 2: "belt strap"}),
    dict(view="back", drawings=["body"], rect=[0, 7, 24, 1], colors={1: "outline"}),
]
