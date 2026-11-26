# Already in the library with its parts rebuilt; only its lighting is redone
SOURCE = ["black2-white2/0001-bulbasaur.spu", "batches/gen1-first-ten/black2-white2/0001-bulbasaur.spu"]
MATERIALS = [
    dict(name="outline", shades=[10, 14], finish=0.1, body=0),
    dict(name="frog skin", shades=[5, 15, 4, 3, 2], base=3, finish=0.3, body=0.1),
    dict(name="frog skin, spots", shades=[5, 4, 3], base=1, finish=0.3, body=0.1),
    dict(name="bulb", shades=[14, 13, 12, 11], base=1, finish=0.1, body=0.25),
    dict(name="claws and teeth", shades=[9, 1], base=1, finish=0.7, body=0.05),
    dict(name="mouth", shades=[8, 7, 6], base=0, finish=0.8, body=0),
    dict(name="seams and wrinkles", shades=[], finish=0, body=0),   # lines drawn inside a surface: tinted, never a crease
    dict(name="eye (line art)", shades=[8, 7, 6, 9, 1], finish=0.9, body=0),
]
INNER = "seams and wrinkles"
def to(name, colors): return {c: name for c in colors}
COLORS = {10: "outline", **to("frog skin", [5, 15, 4, 3, 2]), **to("bulb", [14, 13, 12, 11]),
          **to("claws and teeth", [9, 1]), **to("mouth", [8, 7, 6])}
SKIN = ["head*", "body*", "leg*", "foot*", "hand"]
RULES = [
    dict(drawings=["tane"], thin_all={14: "outline"}),    # the bulb's lobes overlap: their lines are creases
    dict(drawings=["head-eyes-*", "head-2-eyes-*"], colors={**to("eye (line art)", [9, 1]), **to("eye (line art)", [8, 7, 6])}),
]
MARKS = [
    # darker patches of the skin: a dark patch wholly inside lighter skin
    dict(drawings=SKIN, color=5, on=[4, 3, 2, 15], to="frog skin, spots", max=30, min=2),
    dict(drawings=SKIN, color=4, on=[3, 2], to="frog skin, spots", max=40, min=2),
]
