SOURCE = "sources/black2-white2/0095-onix.spu"
ROCK = [14, 13, 12, 11]
MATERIALS = [
    # black, and the soft black (9) the back view draws its lit-side contour and facet lines in
    # (it is the same dark gray in the shiny palette, where the rock turns olive: a line, not a shade)
    dict(name="outline", shades=[15, 9], finish=0.1, body=0),
    # every boulder, the head, the jaw and the horn: plain stone, dead matte and solid. Base is the mid gray
    # (13): of what shows at rest in both views it and the dark gray are level once contour strokes are left out,
    # and the dark gray is the facets' shadow side
    dict(name="rock", shades=ROCK, base=1, finish=0, body=0),
    # the ten near-white pixels (10) on the snout's top edge and tip: the same stone at its most lit. In their
    # own row so they darken with the snout; left as a painted glint they stayed white on a head in shade
    dict(name="rock, snout light", shades=ROCK + [10], base=1, finish=0, body=0),
    dict(name="seams and wrinkles", shades=[], finish=0, body=0),   # facet edges and cracks drawn inside one boulder: tinted, never a crease
    dict(name="eye (line art)", shades=[15, 1], finish=0.9, body=0),
]
INNER = "seams and wrinkles"
def to(name, colors): return {c: name for c in colors}
COLORS = {15: "outline", 9: "outline", **to("rock", ROCK), 10: "rock, snout light", 1: "eye (line art)"}
EYE = {1: "eye (line art)", 15: "eye (line art)"}
RULES = [
    # facet edges and cracks drawn in the soft black wholly inside one boulder are lines on that one stone
    dict(view="back", interior={9: (ROCK, INNER)}),
    # the same in black: the head's ridges (both views) and one facet edge on the second boulder. Not the
    # pictures that draw two or more boulders (body91, body c1): black between boulders is a crease.
    dict(view="front", drawings=["head1", "body21"], interior={15: (ROCK, INNER)}),
    dict(view="back", drawings=["head1"], interior={15: (ROCK + [9], INNER), 9: (ROCK + [15], INNER)}),
    # the black gap under the head, seen from behind, is a hole with its own edge, not a seam
    dict(view="back", drawings=["head1"], rect=[24, 39, 11, 7], colors={15: "outline", 9: "outline"}),
    # brow and lid lines around the eyes stay lines, the same in the head and in the eye pictures
    dict(view="front", drawings=["head1"], rect=[3, 29, 18, 7], colors={15: "outline"}),
    dict(view="back", drawings=["head1-eyes-closed"], colors={9: "outline"}),
    # pupils (the whites are the only use of color 1)
    dict(view="front", drawings=["head1"], rect=[6, 33, 1, 1], colors=EYE),
    dict(view="front", drawings=["head1"], rect=[16, 33, 1, 1], colors=EYE),
    dict(view="front", drawings=["head1-eyes-open"], rect=[3, 5, 1, 1], colors=EYE),
    dict(view="front", drawings=["head1-eyes-open"], rect=[13, 5, 1, 1], colors=EYE),
    dict(view="back", drawings=["head1"], rect=[33, 33, 1, 1], colors=EYE),
    dict(view="back", drawings=["head1-eyes-open"], rect=[4, 3, 1, 1], colors=EYE),
]
