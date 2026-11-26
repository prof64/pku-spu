# The format demo's Charizard, whose parts are rebuilt (the game source's are not): the library's own file
SOURCE = ["black2-white2/0006-charizard.spu", "batches/gen1-first-ten/black2-white2/0006-charizard.spu"]
MATERIALS = [
    dict(name="outline", shades=[1], finish=0.1, body=0),
    dict(name="dragon hide", shades=[9, 8, 7, 6], base=2, finish=0.5, body=0.05),
    dict(name="underbelly", shades=[6, 5], base=1, finish=0.4, body=0.25),
    dict(name="wing membrane", shades=[12, 11, 10], base=0, finish=0.45, body=0.5),
    dict(name="wing membrane, outer side", shades=[9, 8, 7, 6], base=2, finish=0.45, body=0.3),
    dict(name="claws and teeth", shades=[4, 3, 2], base=2, finish=0.7, body=0.05),
    dict(name="mouth", shades=[9, 15], base=1, finish=0.8, body=0),
    dict(name="tail flame", shades=[15, 14, 13], base=1, finish=0, body=0),
    dict(name="seams and wrinkles", shades=[], finish=0, body=0),   # lines drawn inside a surface: tinted, never a crease
    dict(name="eye (line art)", shades=[11, 3, 2], finish=0.9, body=0),
]
INNER = "seams and wrinkles"
def to(name, colors): return {c: name for c in colors}
COLORS = {1: "outline", **to("dragon hide", [9, 8, 7, 6]), 5: "underbelly", **to("wing membrane", [12, 11, 10]),
          **to("claws and teeth", [4, 3, 2]), **to("tail flame", [15, 14, 13])}
RULES = [
    dict(drawings=["karada", "o01", "karada01", "tail0*"], colors={6: "underbelly"}),
    dict(drawings=["ago", "ago01"], colors={15: "mouth"}),
    dict(drawings=["atama-eyes-*", "atama01-eyes-*"], colors={11: "eye (line art)", 3: "eye (line art)", 2: "eye (line art)"}),
    dict(view="back", drawings=["l-wings01", "r-wings01"], colors=to("wing membrane, outer side", [8, 7, 6])),
]
GLOW = [
    dict(material="tail flame", colors=[13], glow=255, intent="the flame's yellow core is the brightest"),
    dict(material="tail flame", colors=[14], glow=225, intent="the flame's orange middle"),
    dict(material="tail flame", colors=[15], glow=200, intent="the flame's red tongues"),
]
def AFTER(job):
    job.flicker(["hi*", "ef01*"])
    job.drop_animation("alternate-1", "Alternate 1 only repeats Idle's flame")
