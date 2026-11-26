SOURCE = "sources/black2-white2/0007-squirtle.spu"
MATERIALS = [
    dict(name="outline", shades=[15], finish=0.1, body=0),
    dict(name="turtle skin", shades=[14, 13, 12, 11], base=2, finish=0.5, body=0.08),
    dict(name="shell", shades=[5, 4, 3], base=1, finish=0.2, body=0),
    dict(name="shell rim", shades=[2, 1], base=0, finish=0.2, body=0),
    dict(name="belly plate", shades=[9, 8, 7, 6], base=2, finish=0.15, body=0),
    dict(name="mouth", shades=[10, 9], base=1, finish=0.8, body=0),
    dict(name="seams and wrinkles", shades=[], finish=0, body=0),   # lines drawn inside a surface: tinted, never a crease
    dict(name="eye (line art)", shades=[10, 9, 5, 2, 1], finish=0.9, body=0),
]
INNER = "seams and wrinkles"
COLORS = {15: "outline", 14: "turtle skin", 13: "turtle skin", 12: "turtle skin", 11: "turtle skin",
          5: "shell", 4: "shell", 3: "shell", 2: "shell rim", 1: "shell rim",
          10: "belly plate", 9: "belly plate", 8: "belly plate", 7: "belly plate", 6: "belly plate"}
RULES = [
    dict(drawings=["atama*", "head01*"], colors={2: "eye (line art)", 1: "eye (line art)", 10: "eye (line art)", 9: "mouth"}),
    dict(view="back", drawings=["head01*"], colors={9: "eye (line art)", 5: "eye (line art)"}),
    # seams drawn in black are lines on the one dome, not creases
    dict(drawings=["body01"], interior={15: ([5, 4, 3], INNER)}),
    dict(drawings=["karada"], interior={15: ([10, 9, 8, 7, 6], INNER)}),
]
AREAS = [
    # the mouth line and the dark of the open mouth are drawn line, the tongue is the mouth
    dict(material="outline", colors=[10], area=dict(view="front", rect=[30, 36, 12, 6])),
]
