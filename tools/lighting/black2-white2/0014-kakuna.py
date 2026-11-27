SOURCE = "sources/black2-white2/0014-kakuna.spu"
MATERIALS = [
    dict(name="outline", shades=[12, 7], finish=0.1, body=0),
    dict(name="insect shell", shades=[7, 6, 5, 4, 3, 2], base=3, finish=0.45, body=0),
    dict(name="eye (line art)", shades=[12, 11, 10, 1], finish=0.9, body=0),
]
def to(name, colors): return {c: name for c in colors}
COLORS = {12: "outline", **to("insect shell", [7, 6, 5, 4, 3, 2]), **to("eye (line art)", [11, 10, 1])}
RULES = [
    # the cocoon's plates overlap (shoulder plates, folded arms, the rings of the tail end): the dark
    # lines between them are creases; the same color along the outside stays the shell's darkest shade
    dict(drawings=["body", "hand", "neck"], interior={7: ([6, 5, 4, 3, 2], "outline")}),
    dict(view="front", drawings=["head"], rect=[11, 11, 6, 5], colors={12: "eye (line art)"}),
    dict(view="back", drawings=["head"], rect=[23, 14, 3, 5], colors={12: "eye (line art)"}),
    dict(drawings=["head-eyes-*"], colors={12: "eye (line art)"}),
]
