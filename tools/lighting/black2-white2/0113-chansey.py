SOURCE = "sources/black2-white2/0113-chansey.spu"
MATERIALS = [
    # black line. The pale coat's contour (14, 15) and the egg's olive contour (4, 3) are drawn line too: the
    # palette has no step between the pale pinks and their dark contour, and with the contour as the coat's
    # darkest shade the whole body speckled dark in the field and the cave
    dict(name="outline", shades=[7, 15, 14, 4, 3], finish=0.1, body=0),
    # the pink coat (body, head, arms, tail, the hair-like growths): painted flat and soft in the official art,
    # smooth-edged with no tufts. The front is painted in 12, the back in 13; 13 is most of it
    dict(name="short fur", shades=[13, 12, 11], base=0, finish=-0.2, body=0.05),
    # the darker ends of the six growths at the sides of the head
    dict(name="short fur, ear tips", shades=[15, 10, 9], base=1, finish=-0.2, body=0.05),
    # the pouch that holds the egg: the same coat in the darker pink
    dict(name="short fur, pouch", shades=[15, 10, 9, 8], base=2, finish=-0.2, body=0.05),
    # the feet, painted in the shadow under the body
    dict(name="short fur, feet", shades=[15, 10, 13], base=0, finish=-0.2, body=0.05),
    # the egg: white with a soft cream shade; painted dull, no highlight (Hard shell)
    dict(name="hard shell, egg", shades=[2, 1], base=1, finish=0.2, body=0),
    dict(name="mouth", shades=[10], base=0, finish=0.8, body=0),
    dict(name="eye (line art)", shades=[7, 1], finish=0.9, body=0),
]
def to(name, colors): return {c: name for c in colors}
TIPS, POUCH, FEET = "short fur, ear tips", "short fur, pouch", "short fur, feet"
COLORS = {**to("outline", [7, 15, 14, 4, 3]), **to("short fur", [13, 12, 11]), **to(TIPS, [10, 9]), 8: POUCH,
          **to("hard shell, egg", [2, 1])}
def runs(drawing, view, *spans):
    return [dict(view=view, drawings=[drawing], rect=[x, y, w, 1], colors={15: TIPS}) for x, y, w in spans]
RULES = [
    dict(drawings=["egg"], colors=to(POUCH, [15, 10, 9, 8])),
    dict(drawings=["foot-*"], colors=to(FEET, [15, 10, 13])),
    # the open mouth's red inside; its line and the shut mouth's smile are drawn line
    dict(drawings=["mouth", "mouth-2"], colors={15: "outline", 10: "mouth"}),
    dict(drawings=["eye-eyes-open"], colors=to("eye (line art)", [7, 1])),
    # the dark contour around each darker tip belongs to the tip, the rest of it to the pink strand
    *runs("ear-rc", "back", [8, 4, 3], [11, 5, 2], [13, 6, 1], [8, 7, 1], [13, 7, 1], [9, 8, 4]),
    *runs("ear-rb", "back", [15, 6, 1], [9, 7, 1], [16, 7, 1], [10, 8, 3], [16, 8, 1], [13, 9, 3]),
    *runs("ear-rb", "front", [9, 9, 2], [7, 10, 2], [6, 11, 1], [6, 12, 1], [11, 12, 1], [7, 13, 4]),
    *runs("ear-ra", "front", [5, 7, 1], [4, 8, 1], [3, 9, 1], [3, 10, 1], [6, 10, 2], [4, 11, 2]),
    *runs("ear-lc", "back", [6, 3, 2], [5, 4, 1], [4, 5, 1], [4, 6, 1], [7, 6, 2], [5, 7, 2]),
    *runs("ear-lb", "back", [5, 6, 2], [3, 7, 2], [2, 8, 1], [2, 9, 1], [6, 9, 2], [3, 10, 3]),
    *runs("ear-lb", "front", [13, 9, 1], [7, 10, 1], [14, 10, 1], [8, 11, 2], [14, 11, 1], [10, 12, 4]),
    *runs("ear-la", "front", [8, 5, 3], [11, 6, 2], [13, 7, 1], [13, 8, 1], [8, 9, 5]),
]
# the pale patch on the forehead is broad soft light, not a glint (left out, it went gray under the lamp)
KEEP_TOP = ["short fur"]
