SOURCE = "sources/black2-white2/0607-litwick.spu"
MATERIALS = [
    # black line; the flame's own drawn line is dark purple, and the pool's rim is drawn in it where it crosses the flame
    dict(name="outline", shades=[15, 6], finish=0.1, body=0),
    # the whole candle (dome, drips, hands, foot): white where its top faces the flame, lilac gray below; gray contour
    dict(name="wax", shades=[3, 2, 7, 1], base=1, finish=0.3, body=0.5),
    # the lavender pool of melted wax around the wick
    dict(name="wax, melted pool", shades=[4], base=0, finish=0.3, body=0.5),
    dict(name="flame", shades=[5, 11, 4], base=0, finish=0, body=0),
    dict(name="eye (line art)", shades=[9, 8], finish=0.9, body=0),
]
def to(name, colors): return {c: name for c in colors}
COLORS = {15: "outline", 6: "outline", **to("wax", [3, 2, 7, 1]), 4: "wax, melted pool",
          **to("eye (line art)", [9, 8])}
RULES = [
    dict(drawings=["fire*"], colors=to("flame", [5, 11, 4])),
]
GLOW = [
    dict(material="flame", colors=[4], glow=245, intent="the flame's pale core is the brightest"),
    dict(material="flame", colors=[11], glow=225, intent="the edge of the core"),
    dict(material="flame", colors=[5], glow=200, intent="the flame's purple body"),
]
def AFTER(job):
    # the three flame drawings differ little in size, so the swing is widened: the smallest shines 0.83
    job.flicker(["fire"], low=0)
