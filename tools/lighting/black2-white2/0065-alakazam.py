SOURCE = "sources/black2-white2/0065-alakazam.spu"
MATERIALS = [
    # black, and the softened brown line (9, 10, 8) the art draws around the yellow parts on their lit sides
    dict(name="outline", shades=[15, 8, 9, 10], finish=0.1, body=0),
    # the yellow coat: its olive contour color is its darkest shade
    dict(name="short fur", shades=[14, 13, 12], base=1, finish=-0.2, body=0.05),
    # the pale patch the art paints on the brow, one step up from the coat. As the coat's top shade it broke up
    # into pale scribbles over the whole face in daylight; left out of every row it stayed pale in the cave
    dict(name="short fur, brow", shades=[12, 11], base=0, finish=-0.2, body=0.05),
    # the brown chest, forearm and knee pieces: dry plates standing off the body; their dark contour is their darkest shade
    dict(name="plated hide", shades=[8, 7, 6, 5], base=1, finish=0.2, body=0.03),
    # the mustache: yellow at the root, pale at the tufts
    dict(name="whiskers", shades=[14, 13, 12, 11], base=3, finish=0.1, body=0.05),
    # "The spoons clutched in its hands are said to have been created by its psychic powers" (Black 2/White 2);
    # silver like Kadabra's: polished metal, its white highlight kept so it can move
    dict(name="metal", shades=[4, 3, 2, 1], base=1, finish=0.9, body=-1),
    # the white claws on the feet, gray-edged
    dict(name="claws and teeth", shades=[4, 3, 2, 1], base=3, finish=0.7, body=0.05),
    dict(name="eye (line art)", shades=[15, 2, 1], finish=0.9, body=0),
]
def to(name, colors): return {c: name for c in colors}
COLORS = {15: "outline", **to("outline", [9, 10]), **to("short fur", [14, 13, 12]), 11: "short fur, brow",
          **to("plated hide", [8, 7, 6, 5]), **to("claws and teeth", [4, 3, 2, 1])}
def rects(drawing, view, colors, *boxes):
    return [dict(view=view, drawings=[drawing], rect=list(b), colors=colors) for b in boxes]
RULES = [
    # the spoons: every gray in a hand is spoon (the bowl above the fist, the handle's end below it)
    dict(drawings=["hand-r", "hand-l"], colors=to("metal", [4, 3, 2, 1])),
    # the mustache
    dict(drawings=["hige-*"], colors=to("whiskers", [14, 13, 12, 11])),
    # the eyes: white, their gray corners and the black pupils
    dict(view="front", drawings=["head", "head-eyes-open"], colors=to("eye (line art)", [1, 2])),
    *rects("head-eyes-open", "front", {15: "eye (line art)"}, [3, 4, 1, 1], [11, 4, 1, 1]),
    # the plates' dark brown where it is only the softened line around a yellow part
    dict(view="front", drawings=["arm-l"], colors={8: "outline"}),
    dict(view="back", drawings=["foot-l"], colors={8: "outline"}),
    *rects("hand-l", "back", {8: "outline"}, [9, 18, 1, 1]),
]
# the pale patch on the shoulder and knee plates is the plates' own top shade: left out, it stayed pale on a body gone dark
KEEP_TOP = ["plated hide"]
