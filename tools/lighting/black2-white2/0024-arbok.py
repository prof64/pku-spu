SOURCE = "sources/black2-white2/0024-arbok.spu"
PURPLE = [12, 11, 10, 9]
MATERIALS = [
    dict(name="outline", shades=[8], finish=0.1, body=0),
    dict(name="snake scales", shades=PURPLE, base=1, finish=0.15, body=0.05),
    # the face pattern on the spread chest is pigment in the same scales: one row per color, the scales' dials
    dict(name="snake scales, pattern black", shades=[], finish=0.15, body=0.05),
    dict(name="snake scales, pattern red", shades=[7, 6, 5], base=1, finish=0.15, body=0.05),
    dict(name="snake scales, pattern yellow", shades=[2, 1], base=1, finish=0.15, body=0.05),
    dict(name="mouth", shades=[13, 4, 3], base=1, finish=0.8, body=0),
    dict(name="claws and teeth", shades=[14, 15], base=1, finish=0.7, body=0.05),
    dict(name="eye (line art)", shades=[8, 15], finish=0.9, body=0),
]
def to(name, colors): return {c: name for c in colors}
COLORS = {8: "outline", **to("snake scales", PURPLE), **to("snake scales, pattern red", [7, 6, 5]),
          **to("snake scales, pattern yellow", [2, 1]), **to("mouth", [13, 4, 3]), **to("claws and teeth", [14, 15])}
EYE = to("eye (line art)", [8, 15])
RULES = [
    # black wholly inside the hood is the pattern's black, not line art: it must not crease the hood
    dict(drawings=["karada1"], interior={8: ([1, 5, 6, 7, 9, 10, 11, 12], "snake scales, pattern black")}),
    dict(drawings=["atama-eyes-open"], rect=[6, 8, 4, 2], colors=EYE),
    dict(view="back", drawings=["head01"], rect=[15, 9, 4, 2], colors=EYE),
    dict(drawings=["head01-eyes-open"], colors=EYE),
]
