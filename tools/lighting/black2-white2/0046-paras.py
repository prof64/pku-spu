SOURCE = "sources/black2-white2/0046-paras.spu"
SHELL = [14, 13, 12, 11, 10]
MATERIALS = [
    dict(name="outline", shades=[15, 14, 13], finish=0.1, body=0),
    # head, body, pincers and legs: one hard orange shell; its brown contour colors are its darkest shades
    dict(name="insect shell", shades=SHELL, base=2, finish=0.45, body=0),
    # the five dots on the forehead: pigment, drawn one step darker than the shell around them
    dict(name="insect shell, spots", shades=[13, 12, 11], base=0, finish=0.45, body=0),
    # the two mushrooms: painted flat and soft, no highlight
    dict(name="mushroom cap", shades=[8, 7, 6], base=1, finish=0.1, body=0.1),
    dict(name="mushroom cap, spots", shades=[13, 12, 5, 4], base=2, finish=0.1, body=0.1),
    dict(name="mushroom stem", shades=[13, 5], base=1, finish=0.1, body=0.1),
    dict(name="claws and teeth", shades=[3, 9, 2, 1], base=2, finish=0.7, body=0.05),
    dict(name="eye (line art)", shades=[15, 3, 9, 2, 1], finish=0.9, body=0),
]
def to(name, colors): return {c: name for c in colors}
EYE = to("eye (line art)", [15, 3, 9, 2, 1])
COLORS = {15: "outline", **to("insect shell", SHELL), **to("mushroom cap", [8, 7, 6]),
          **to("mushroom cap, spots", [5, 4]), **to("eye (line art)", [3, 9, 2, 1])}
RULES = [
    # the body's segments, the head on the thorax, a pincer's two jaws, a closed eye's slit: the dark
    # lines between them are creases; the same colors along the outside stay the shell's darkest shades
    dict(drawings=["body*", "hand-*", "foot*"],
         interior={14: ([13, 12, 11, 10], "outline"), 13: ([14, 12, 11, 10], "outline")}),
    # eyes (the pupil is black) and the white mandibles under them
    dict(view="front", drawings=["body2"], rect=[1, 15, 6, 7], colors=EYE),
    dict(view="front", drawings=["body2"], rect=[14, 18, 6, 7], colors=EYE),
    dict(drawings=["body2-eyes-open"], colors=EYE),
    dict(view="front", drawings=["body2"], rect=[5, 24, 8, 5], colors=to("claws and teeth", [3, 9, 2, 1])),
    # mushrooms: a yellow spot at the rim is edged in the browns; the short stem under each cap
    dict(drawings=["kinoko*"], colors={13: "mushroom cap, spots", 12: "mushroom cap, spots", 14: "outline"}),
    dict(view="front", drawings=["kinoko1"], rect=[9, 13, 4, 3], colors=to("mushroom stem", [5])),
    dict(view="front", drawings=["kinoko2"], rect=[3, 14, 3, 4], colors=to("mushroom stem", [13, 5])),
    dict(view="front", drawings=["kinoko2"], rect=[6, 17, 1, 1], colors=to("mushroom stem", [13])),
    dict(view="back", drawings=["kinoko-r"], rect=[7, 8, 5, 5], colors=to("mushroom stem", [5])),
    dict(view="back", drawings=["kinoko-l"], rect=[3, 11, 4, 3], colors=to("mushroom stem", [13, 5])),
]
MARKS = [
    dict(view="front", drawings=["body2"], color=11, on=[10], to="insect shell, spots", max=1, min=1),
    dict(view="front", drawings=["body2"], color=12, on=[11, 10], to="insect shell, spots", max=1, min=1),
]
# the pale orange is the broad lit side of the head and pincers in the front view (none in the back view,
# so it is under 7% of the shell overall): left out of the row it stays pale on a body gone dark
KEEP_TOP = ["insect shell"]
