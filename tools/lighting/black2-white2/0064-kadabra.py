SOURCE = "sources/black2-white2/0064-kadabra.spu"
MATERIALS = [
    # black, and the softened brown line (9, 8, 7) the art draws around the yellow parts on their lit sides
    dict(name="outline", shades=[15, 9, 8, 7], finish=0.1, body=0),
    # the yellow coat: its olive contour colors are its darkest shades; the pale patch on the brow is its own top shade
    dict(name="short fur", shades=[14, 13, 12, 11, 10], base=2, finish=-0.2, body=0.05),
    # the red star on the forehead and the three red waves on the belly
    dict(name="short fur, star and belly marks", shades=[5], base=0, finish=-0.2, body=0.05),
    # the brown band around the tail
    dict(name="short fur, tail band", shades=[8, 7, 6], base=0, finish=-0.2, body=0.05),
    # the brown chest and shoulder pieces: dry plates standing off the body; their dark contour is their darkest shade
    dict(name="plated hide", shades=[9, 8, 7], base=1, finish=0.2, body=0.03),
    # the mustache: yellow at the root, pale at the tips, its strands drawn in the darker yellows
    dict(name="whiskers", shades=[14, 13, 12, 11, 10], base=4, finish=0.1, body=0.05),
    # "KADABRA holds a silver spoon in its hand" (Sapphire): polished metal, its white highlight kept so it can move
    dict(name="metal", shades=[4, 3, 2, 1], base=1, finish=0.9, body=-1),
    # white claws; from behind the art paints them in the grays
    dict(name="claws and teeth", shades=[4, 3, 2, 1], base=3, finish=0.7, body=0.05),
    dict(name="eye (line art)", shades=[15, 3, 2, 1], finish=0.9, body=0),
]
def to(name, colors): return {c: name for c in colors}
COLORS = {15: "outline", **to("outline", [9, 8, 7]), **to("short fur", [14, 13, 12, 11, 10]),
          5: "short fur, star and belly marks", 6: "short fur, tail band", **to("claws and teeth", [4, 3, 2, 1])}
METAL = to("metal", [4, 3, 2, 1])
def rects(drawing, view, colors, *boxes):
    return [dict(view=view, drawings=[drawing], rect=list(b), colors=colors) for b in boxes]
RULES = [
    # the brown pieces
    dict(drawings=["karada01", "body", "kata1", "kata2"], colors=to("plated hide", [9, 8, 7])),
    # the tail band (the browns at the tail's edge stay its softened line)
    dict(view="front", drawings=["o01"], colors=to("short fur, tail band", [8, 7])),
    *rects("o01", "front", {8: "outline"}, [3, 6, 1, 1]),
    dict(view="back", drawings=["tail1"], colors=to("short fur, tail band", [8, 7])),
    # the mustache
    dict(drawings=["hige*"], colors=to("whiskers", [14, 13, 12, 11, 10])),
    # the spoon: the bowl and neck above the fist, and the handle below it (the white between the fingers is their claws)
    *rects("te03", "front", METAL, [4, 3, 8, 12], [6, 21, 6, 5]),
    *rects("r-arm1", "back", METAL, [4, 5, 8, 6], [10, 11, 2, 2], [14, 21, 7, 5]),
    # the eyes: white, their gray corners and the black pupil
    *rects("atama-eyes-open", "front", to("eye (line art)", [1, 15]), [1, 2, 3, 3]),
    *rects("atama-eyes-open", "front", to("eye (line art)", [1, 2, 3, 15]), [9, 2, 6, 4]),
]
# the pale patch on the brow is the coat's own top shade: left out, it stays pale on a body gone dark
KEEP_TOP = ["short fur"]
