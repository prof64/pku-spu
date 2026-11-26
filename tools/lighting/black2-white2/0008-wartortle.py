SOURCE = "sources/black2-white2/0008-wartortle.spu"
MATERIALS = [
    dict(name="outline", shades=[15, 4, 14, 13, 12, 11], finish=0.1, body=0),
    dict(name="turtle skin", shades=[14, 13, 12, 11], base=2, finish=0.5, body=0.08),
    dict(name="fur", shades=[3, 2, 1], base=0, finish=-0.7, body=0.05),
    dict(name="shell", shades=[7, 6, 5], base=1, finish=0.6, body=0),
    dict(name="shell rim", shades=[3, 1], base=0, finish=0.6, body=0),
    dict(name="belly plate", shades=[7, 10, 9, 8], base=3, finish=0.5, body=0),
    dict(name="claws and teeth", shades=[3, 1], base=1, finish=0.7, body=0.05),
    dict(name="seams and wrinkles", shades=[], finish=0, body=0),   # lines drawn inside a surface: tinted, never a crease
    dict(name="eye (line art)", shades=[7, 6, 3, 1], finish=0.9, body=0),
]
INNER = "seams and wrinkles"
COLORS = {15: "outline", 4: "outline", 14: "turtle skin", 13: "turtle skin", 12: "turtle skin", 11: "turtle skin",
          3: "fur", 2: "fur", 1: "fur", 7: "shell", 6: "shell", 5: "shell",
          10: "belly plate", 9: "belly plate", 8: "belly plate"}
FURLINES = {11: "outline", 12: "outline", 13: "outline", 14: "outline"}
RULES = [
    dict(drawings=["o", "o2", "mimi*", "tail0*", "*-ear01", "image-*"], colors=FURLINES),
    dict(drawings=["karada", "body01"], colors={3: "shell rim", 1: "shell rim"}),
    dict(drawings=["karada", "body02"], colors={7: "belly plate"}),
    dict(drawings=["te*", "l-arm01", "asi*", "*foot*", "*leg*"], colors={3: "claws and teeth", 1: "claws and teeth"}),
    dict(drawings=["atama"], colors={3: "claws and teeth", 1: "claws and teeth"}),
    dict(drawings=["atama-eyes-*", "head01-eyes-*"], colors={3: "eye (line art)", 1: "eye (line art)", 7: "eye (line art)", 6: "eye (line art)"}),
    # seams drawn in black are lines on the one dome, not creases
    dict(drawings=["body01"], interior={15: ([7, 6, 5], INNER)}),
    dict(drawings=["karada"], interior={15: ([7, 10, 9, 8], INNER)}),
]
