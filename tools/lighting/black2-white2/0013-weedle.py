SOURCE = "sources/black2-white2/0013-weedle.spu"
MATERIALS = [
    dict(name="outline", shades=[5, 10], finish=0.1, body=0),
    # the brown body: the painted art gives the head and each segment a soft pale patch, not Caterpie's white highlights
    dict(name="larval skin", shades=[10, 9, 8, 7, 6], base=2, finish=0.35, body=0.15),
    # the pink nose and the pink feet: each is painted with its own small highlight
    dict(name="larval skin, nose and feet", shades=[14, 13, 12, 11], base=1, finish=0.45, body=0.15),
    dict(name="claws and teeth, stingers", shades=[4, 3, 2, 1], base=3, finish=0.7, body=0.05),
    dict(name="eye (line art)", shades=[5, 4, 1], finish=0.9, body=0),
]
def to(name, colors): return {c: name for c in colors}
COLORS = {5: "outline", **to("larval skin", [10, 9, 8, 7, 6]), **to("larval skin, nose and feet", [14, 13, 12, 11]),
          **to("claws and teeth, stingers", [4, 3, 2, 1])}
EYE = to("eye (line art)", [5, 4, 1])
RULES = [
    dict(drawings=["head-eyes-open"], colors=EYE),
    dict(view="back", drawings=["head"], rect=[21, 15, 1, 2], colors=EYE),      # the eye drawn on the head itself
    # two segments drawn in one picture: the line between them is a crease
    dict(view="back", drawings=["body4"], rect=[7, 1, 2, 3], colors={10: "outline"}),
    dict(view="front", drawings=["body4"], rect=[9, 2, 1, 2], colors={10: "outline"}),
    dict(view="back", drawings=["body5"], rect=[7, 6, 3, 4], colors={10: "outline"}),
]
