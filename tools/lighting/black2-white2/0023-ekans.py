SOURCE = "sources/black2-white2/0023-ekans.spu"
PURPLE = [15, 14, 13, 12, 11]
YELLOW = [9, 8, 7, 6, 5]
MATERIALS = [
    dict(name="outline", shades=[10], finish=0.1, body=0),
    dict(name="snake scales", shades=PURPLE, base=2, finish=0.15, body=0.05),
    # the yellow neck band and the yellow underside it joins: the same scales in another color
    dict(name="snake scales, band and belly", shades=YELLOW, base=2, finish=0.15, body=0.05),
    # the rattle: hard, dry, hollow beads; the painted art gives them soft shading and no highlight
    dict(name="rattle", shades=YELLOW, base=2, finish=0.2, body=0.05),
    dict(name="mouth", shades=[4, 3, 2], base=1, finish=0.8, body=0),
    dict(name="eye (line art)", shades=[10, 9, 7, 6, 1], finish=0.9, body=0),
]
def to(name, colors): return {c: name for c in colors}
COLORS = {10: "outline", **to("snake scales", PURPLE), **to("snake scales, band and belly", YELLOW), **to("mouth", [4, 3, 2])}
EYE = to("eye (line art)", [10, 9, 7, 6, 1])
RULES = [
    dict(drawings=["o", "tail"], colors=to("rattle", YELLOW)),
    dict(view="front", drawings=["atama"], rect=[11, 6, 6, 4], colors=EYE),
    dict(drawings=["atama-eyes-open"], rect=[2, 1, 6, 4], colors=EYE),
    dict(view="back", drawings=["head"], rect=[17, 9, 5, 4], colors=EYE),
    dict(drawings=["head-eyes-open"], rect=[1, 2, 5, 4], colors=EYE),
]
