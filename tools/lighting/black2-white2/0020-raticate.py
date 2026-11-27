SOURCE = "sources/black2-white2/0020-raticate.spu"
MATERIALS = [
    dict(name="outline", shades=[15, 12, 8, 7], finish=0.1, body=0),
    # the tawny coat: head, back, arms, the backs of the ears. The back view and the front's side are painted in 11
    dict(name="short fur", shades=[12, 11, 10, 9], base=1, finish=-0.2, body=0.05),
    # the cream muzzle, chin, chest ruff and belly: the same coat, paler
    dict(name="short fur, cream", shades=[8, 7, 6, 5], base=2, finish=-0.2, body=0.05),
    # one stiff hair each: smooth, painted flat
    dict(name="whiskers", shades=[8, 7, 6, 5], base=3, finish=0.1, body=0.05),
    # bare skin: the ringed tail, hands and feet
    dict(name="hide", shades=[4, 3, 2], base=1, finish=0.25, body=0.08),
    dict(name="hide, ear insides", shades=[4, 3], base=0, finish=0.25, body=0.08),
    dict(name="claws and teeth", shades=[14, 13, 1], base=2, finish=0.7, body=0.05),
    dict(name="eye (line art)", shades=[15, 13, 1], finish=0.9, body=0),
]
def to(name, colors): return {c: name for c in colors}
EYE = to("eye (line art)", [15, 13, 1])
COLORS = {15: "outline", **to("short fur", [12, 11, 10, 9]), **to("short fur, cream", [8, 7, 6, 5]),
          **to("hide", [4, 3, 2]), **to("claws and teeth", [14, 13, 1])}
RULES = [
    dict(drawings=["hige*"], colors=to("whiskers", [8, 7, 6, 5])),
    dict(drawings=["mimi-*", "ear-*"], colors={4: "hide, ear insides"}),
    # the chest ruff hangs over the belly: the lines of its points are creases
    dict(drawings=["fusafusa"], thin_all={8: "outline", 7: "outline"}),
    # tufts drawn on the coat in its dark color (the back view): clumps of fur, so creases
    dict(view="back", drawings=["head", "body"], interior={12: ([11, 10, 9, 15], "outline")}),
    dict(view="front", drawings=["body"], rect=[15, 11, 4, 2], colors=EYE),
    dict(view="front", drawings=["body-eyes-open"], rect=[3, 3, 4, 2], colors=EYE),
    dict(view="back", drawings=["head"], rect=[36, 17, 3, 2], colors=EYE),
    dict(view="back", drawings=["head-eyes-open"], rect=[2, 3, 3, 2], colors=EYE),
]
