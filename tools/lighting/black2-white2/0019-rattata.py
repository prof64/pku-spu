SOURCE = "sources/black2-white2/0019-rattata.spu"
MATERIALS = [
    dict(name="outline", shades=[15, 7], finish=0.1, body=0),
    # the purple coat: head, back, legs, tail. Front is painted in 5, back in 6; 6 is most of it
    dict(name="short fur", shades=[7, 6, 5, 4], base=1, finish=-0.2, body=0.05),
    # the cream muzzle, lower jaw, belly and paws: the same coat, paler
    dict(name="short fur, cream", shades=[12, 11, 10, 8], base=2, finish=-0.2, body=0.05),
    dict(name="short fur, ear insides", shades=[11, 9], base=1, finish=-0.2, body=0.05),
    # one stiff hair each: smooth, painted flat
    dict(name="whiskers", shades=[12, 11, 10, 8], base=3, finish=0.1, body=0.05),
    dict(name="hide, paw pads", shades=[3, 2], base=1, finish=0.25, body=0.08),
    dict(name="claws and teeth", shades=[14, 13, 1], base=2, finish=0.7, body=0.05),
    dict(name="mouth", shades=[3, 2], base=1, finish=0.8, body=0),
    dict(name="eye (line art)", shades=[3, 2, 13, 1], finish=0.9, body=0),
]
def to(name, colors): return {c: name for c in colors}
COLORS = {15: "outline", **to("short fur", [7, 6, 5, 4]), **to("short fur, cream", [12, 11, 10, 8]),
          9: "short fur, ear insides", **to("claws and teeth", [14, 13, 1]), 2: "mouth", 3: "eye (line art)"}
RULES = [
    dict(drawings=["hige*"], colors=to("whiskers", [12, 11, 10, 8])),
    dict(view="front", drawings=["mimi-*"], colors={11: "short fur, ear insides"}),
    # the pink on the raised hind feet, seen from behind
    dict(view="back", drawings=["b-foot-*"], colors={2: "hide, paw pads"}),
    dict(drawings=["head-eyes-*"], colors=to("eye (line art)", [3, 2, 13, 1])),
    # the curled tail lies over itself: the dark line of the spiral is a crease
    dict(drawings=["tail*"], interior={7: ([6, 5, 4, 15], "outline")}),
]
