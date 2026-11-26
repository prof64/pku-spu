SOURCE = "sources/black2-white2/0005-charmeleon.spu"
MATERIALS = [
    dict(name="outline", shades=[10], finish=0.1, body=0),
    dict(name="scales", shades=[7, 6, 5, 4], base=2, finish=0.45, body=0.06),
    dict(name="belly", shades=[9, 12, 8], base=2, finish=0.4, body=0.25),
    dict(name="claws and teeth", shades=[3, 2, 1], base=2, finish=0.7, body=0.05),
    dict(name="mouth", shades=[10, 7], base=1, finish=0.8, body=0),
    dict(name="tail flame", shades=[15, 14, 13], base=1, finish=0, body=0),
    dict(name="seams and wrinkles", shades=[], finish=0, body=0),   # lines drawn inside a surface: tinted, never a crease
    dict(name="eye (line art)", shades=[11, 2, 1], finish=0.9, body=0),
]
INNER = "seams and wrinkles"
def to(name, colors): return {c: name for c in colors}
COLORS = {10: "outline", **to("scales", [7, 6, 5, 4]), **to("belly", [9, 12, 8]), **to("claws and teeth", [3, 2, 1]),
          **to("tail flame", [15, 14, 13]), 11: "eye (line art)"}
RULES = [
    dict(drawings=["ago", "jaw01"], colors={7: "mouth"}),
    dict(drawings=["atama", "atama-eyes-*", "head01", "head01-eyes-*"], colors=to("eye (line art)", [3, 2, 1])),
]
GLOW = [
    dict(material="tail flame", colors=[13], glow=250, intent="the flame's yellow core is the brightest"),
    dict(material="tail flame", colors=[14], glow=220, intent="the flame's orange middle"),
    dict(material="tail flame", colors=[15], glow=190, intent="the flame's red tongues and embers"),
]
def AFTER(job):
    job.flicker(["h001*", "ef01*"])
    job.drop_animation("alternate-1", "Alternate 1 only repeats Idle's flame over a still body")
