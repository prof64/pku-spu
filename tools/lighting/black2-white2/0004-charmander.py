SOURCE = "sources/black2-white2/0004-charmander.spu"
MATERIALS = [
    dict(name="outline", shades=[1], finish=0.1, body=0),
    dict(name="lizard skin", shades=[9, 8, 7, 6], base=2, finish=0.35, body=0.1),
    dict(name="belly", shades=[5, 4], base=1, finish=0.4, body=0.25),
    dict(name="claws and teeth", shades=[2, 3], base=1, finish=0.7, body=0.05),
    dict(name="mouth", shades=[9, 15], base=1, finish=0.8, body=0),
    dict(name="tail flame", shades=[15, 14, 13], base=1, finish=0, body=0),
    dict(name="seams and wrinkles", shades=[], finish=0, body=0),   # lines drawn inside a surface: tinted, never a crease
    dict(name="eye (line art)", shades=[12, 11, 10, 2, 3], finish=0.9, body=0),
]
INNER = "seams and wrinkles"
def to(name, colors): return {c: name for c in colors}
COLORS = {1: "outline", **to("lizard skin", [9, 8, 7, 6]), **to("belly", [5, 4]), **to("claws and teeth", [2, 3]),
          **to("tail flame", [15, 14, 13]), **to("eye (line art)", [12, 11, 10])}
FLAMES = ["hi*", "ef01*"]
RULES = [
    dict(drawings=FLAMES, colors={9: "outline"}),
    dict(drawings=["atama"], colors={15: "mouth"}),
    dict(drawings=["atama-eyes-*", "head01-eyes-*"], colors=to("eye (line art)", [2, 3])),
]
GLOW = [
    dict(material="tail flame", colors=[13], glow=245, intent="the flame's yellow core is the brightest"),
    dict(material="tail flame", colors=[14], glow=215, intent="the flame's orange middle"),
    dict(material="tail flame", colors=[15], glow=180, intent="the flame's red tongues are the dimmest"),
]
def AFTER(job):
    job.flicker(["hi", "ef01"])
    job.drop_animation("alternate-1", "Alternate 1 is a 4-tick still, not an animation")
