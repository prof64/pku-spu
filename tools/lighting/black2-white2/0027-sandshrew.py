SOURCE = "sources/black2-white2/0027-sandshrew.spu"
MATERIALS = [
    dict(name="outline", shades=[15], finish=0.1, body=0),
    # the yellow brick-patterned hide: its plate lines (5) and brown contour (7, 6) are its own darker shades
    dict(name="plated hide", shades=[7, 6, 5, 4, 3], base=3, finish=0.2, body=0.03),
    # the cream stomach and muzzle: as dry and matte as the hide, but soft skin (the gray is the muzzle's contour from behind)
    dict(name="dry hide, belly", shades=[13, 10, 11, 12], base=1, finish=0.05, body=0.08),
    dict(name="dry hide, ear insides", shades=[10, 11, 12], base=1, finish=0.05, body=0.03),
    # white claws; in shade the art paints them cream (12) and tan (10), with gray (13) edges
    dict(name="claws and teeth", shades=[13, 10, 12, 1], base=3, finish=0.7, body=0.05),
    dict(name="eye (line art)", shades=[9, 8, 1], finish=0.9, body=0),
]
def to(name, colors): return {c: name for c in colors}
COLORS = {15: "outline", **to("plated hide", [7, 6, 5, 4, 3]), **to("dry hide, belly", [10, 11, 12]),
          **to("claws and teeth", [13, 1]), **to("eye (line art)", [9, 8])}
RULES = [
    # the white in a head drawing is the eye's catchlight
    dict(drawings=["head", "head-2", "head-eyes-*", "head-2-eyes-*", "head01", "head01-eyes-*"], colors={1: "eye (line art)"}),
    # from behind, the muzzle's contour is drawn in the gray
    dict(drawings=["head01", "head01-eyes-*"], colors={13: "dry hide, belly"}),
    # ear insides: the left one in shadow (tan), the right one lit (cream)
    dict(view="front", drawings=["head", "head-2"], rect=[9, 9, 3, 5], colors={10: "dry hide, ear insides"}),
    dict(view="front", drawings=["head", "head-2"], rect=[23, 12, 4, 4], colors={12: "dry hide, ear insides"}),
    # claws in shade
    dict(drawings=["legl2", "legr", "legr2"], colors={10: "claws and teeth"}),
    dict(drawings=["handl"], colors={12: "claws and teeth"}),
]
