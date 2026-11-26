SOURCE = "sources/black2-white2/0009-blastoise.spu"
GRAY = [5, 4, 3, 2]
MATERIALS = [
    dict(name="outline", shades=[1], finish=0.1, body=0),
    dict(name="thick hide", shades=[9, 8, 7, 6], base=1, finish=0.4, body=0.06),
    dict(name="thick hide, jaw", shades=[14, 13, 12, 11], base=1, finish=0.4, body=0.06),
    dict(name="shell", shades=[15, 14], base=0, finish=0.6, body=0),
    dict(name="shell rim", shades=GRAY, base=2, finish=0.6, body=0),
    dict(name="belly plate", shades=[15, 14, 13, 12, 11], base=2, finish=0.5, body=0),
    dict(name="cannons", shades=GRAY, base=2, finish=0.85, body=0),
    dict(name="claws and teeth", shades=[4, 3, 2], base=2, finish=0.7, body=0.05),
    dict(name="mouth", shades=[15, 10], base=1, finish=0.8, body=0),
    dict(name="seams and wrinkles", shades=[], finish=0, body=0),   # lines drawn inside a surface: tinted, never a crease
    dict(name="eye (line art)", shades=[14, 15, 3, 2], finish=0.9, body=0),
]
INNER = "seams and wrinkles"
def to(name, colors): return {c: name for c in colors}
COLORS = {1: "outline", **to("thick hide", [9, 8, 7, 6]), **to("belly plate", [15, 14, 13, 12, 11]), **to("shell rim", GRAY), 10: "mouth"}
RULES = [
    dict(view="back", drawings=["body01"], colors=to("shell", [15, 14, 13]),
         interior={1: ([15, 14, 13], INNER)}),   # seams drawn in black: lines on the one dome, not creases
    dict(drawings=["ago*", "jaw01"], colors={**to("thick hide, jaw", [14, 13, 12, 11]), 15: "outline", **to("claws and teeth", GRAY)}),
    dict(drawings=["head02"], colors=to("claws and teeth", GRAY)),
    dict(drawings=["taihou1", "taihou2", "l-parts01", "r-parts01"], colors=to("cannons", GRAY)),
    dict(drawings=["ude2", "taihou1-2", "*foot*", "r-arm", "asi*", "*leg*"], colors=to("claws and teeth", GRAY)),
    dict(drawings=["atama"], colors=to("outline", GRAY)),
    dict(drawings=["atama-eyes-*", "head01-eyes-*"], colors={3: "eye (line art)", 2: "eye (line art)", 14: "eye (line art)", 15: "eye (line art)"}),
]
FLOODS = [
    dict(view="front", drawing="karada", seeds=[[30, 6], [40, 25], [40, 30], [38, 33]], through=[15, 14, 13], colors=to("shell", [15, 14, 13])),
]
