SOURCE = "sources/black2-white2/0003-venusaur.spu"
MATERIALS = [
    dict(name="outline", shades=[11, 7], finish=0.1, body=0),
    dict(name="bumpy hide", shades=[1, 2, 3, 4], base=2, finish=0.15, body=0.06),
    dict(name="bumpy hide, patches", shades=[1, 2, 3], base=1, finish=0.15, body=0.06),
    dict(name="bumpy hide, ear insides", shades=[7, 5, 6], base=1, finish=0.15, body=0.06),
    dict(name="leaves", shades=[13, 14], base=0, finish=0.15, body=0.35),
    dict(name="petals", shades=[7, 5, 6], base=2, finish=0.2, body=0.25),
    dict(name="petal spots", shades=[6, 12], base=1, finish=0.2, body=0.25),
    dict(name="trunk", shades=[7, 8], base=1, finish=-0.45, body=0.05),
    dict(name="flower center", shades=[7, 8, 9, 10], base=3, finish=0.2, body=0.25),
    # the palette has no gray: its unused first color (a pale gray) is the white's shade
    dict(name="claws and teeth", shades=[0, 15], base=1, finish=0.7, body=0.05),
    dict(name="mouth", shades=[7, 6], base=1, finish=0.8, body=0),
    dict(name="seams and wrinkles", shades=[], finish=0, body=0),   # lines drawn inside a surface: tinted, never a crease
    dict(name="eye (line art)", shades=[7, 5, 6, 12, 15], finish=0.9, body=0),
]
INNER = "seams and wrinkles"
def to(name, colors): return {c: name for c in colors}
COLORS = {11: "outline", **to("bumpy hide", [1, 2, 3, 4]), **to("petals", [7, 5, 6]), 12: "petal spots", 8: "trunk",
          **to("flower center", [9, 10]), **to("leaves", [13, 14]), 15: "claws and teeth"}
EYE = {**to("eye (line art)", [7, 5, 6, 12]), 15: "eye (line art)"}
RULES = [
    dict(drawings=["flower-*", "flowe-*"], thin_all={7: "outline"}),          # petals overlap: their lines are creases
    dict(drawings=["miki"], colors=to("trunk", [7, 8])),
    dict(drawings=["kannmuri*", "meshibe*"], colors=to("flower center", [7, 8, 9, 10])),
    dict(drawings=["leaf-*"], colors={1: INNER}),        # leaf veins and the dark between leaflets
    dict(view="front", drawings=["head2"], rect=[0, 0, 60, 13], colors=to("bumpy hide, ear insides", [7, 5, 6])),
    dict(view="front", drawings=["head2"], rect=[0, 13, 60, 12], colors=EYE),
    dict(drawings=["head2-eyes-*"], colors=EYE),
    dict(view="back", drawings=["head"], colors=to("bumpy hide, ear insides", [7, 5, 6])),
    dict(drawings=["head-2"], colors=to("mouth", [7, 6])),
]
MARKS = [
    dict(drawings=["head*", "body", "leg-*", "foot-*"], color=2, on=[3, 4], to="bumpy hide, patches", max=12, min=2),
]
