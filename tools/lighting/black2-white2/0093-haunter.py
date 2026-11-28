# Haunter: one soft dark body (head, trailing body, loose hands), a wet red mouth, white eyes.
SOURCE = "sources/black2-white2/0093-haunter.spu"
MATERIALS = [
    # black, and the red line the loose hands are outlined in (blue on the shiny): drawn lines, as painted.
    # As a lit row of its own the red stayed bright around the hands in a cave.
    dict(name="outline", shades=[14, 10, 9], finish=0.1, body=0),
    # head, body, hands and the jagged teeth, which are the body's own edge. The Pokedex calls it gaseous
    # ("a gaseous hand", Black 2/White 2; "Its tongue is made of gas", Silver), but the art, the 3D model and
    # the sprite all draw an opaque body with a hard contour, like Gastly's ball: so Gastly's dark core dials,
    # soft like the gas (the art paints broad cloudy streaks on the head, no highlight) and solid. Not named
    # gas, so it keeps its shape. Both views together are mostly the mauve (4); its slate contour (5) is its
    # darkest shade.
    dict(name="ghost body", shades=[5, 4, 3, 2, 1], base=1, finish=-0.1, body=0),
    # the wide open mouth. The standard mouth is 0.8; at that this one, far larger than most, caught the cave's
    # lamp as an orange spot on a body gone dark, as if lit from inside. The art paints it flat pink with no
    # highlight, so it is satin (lit flat) and solid.
    dict(name="mouth", shades=[11, 10, 9], base=1, finish=0.5, body=0),
    # the black lines of the shut eyes: tinted, never a crease
    dict(name="seams and wrinkles", shades=[], finish=0, body=0),
    # whites, their gray shade and the two-pixel pupils
    dict(name="eye (line art)", shades=[12, 15], finish=0.9, body=0),
]
INNER = "seams and wrinkles"
BODY = [1, 2, 3, 4, 5]
def to(name, colors): return {c: name for c in colors}
COLORS = {14: "outline", **to("ghost body", BODY), **to("mouth", [9, 10, 11]), **to("eye (line art)", [12, 15])}
RULES = [
    # the hands' red rim
    dict(drawings=["hand-*", "?-hand01*"], colors=to("outline", [9, 10])),
    # pupils: the black at each eye's inner edge
    dict(view="front", drawings=["head-eyes-open"], rect=[4, 8, 1, 2], colors={14: "eye (line art)"}),
    dict(view="front", drawings=["head-eyes-open"], rect=[15, 8, 1, 2], colors={14: "eye (line art)"}),
    # the shut eyes' black strokes lie on the head: lines on it, not creases
    dict(drawings=["head*-eyes-closed"], interior={14: (BODY, INNER)}),
]
# the palest lilac is the painted light on the hands' knuckles and fingers: left out of the row it stayed
# pale on hands gone dark with the sun behind
KEEP_TOP = ["ghost body"]
