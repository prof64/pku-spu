SOURCE = "sources/black2-white2/0029-nidoran.spu"
MATERIALS = [
    # black, and the whiskers where they lie over the cheek (drawn as dark strokes, fading while they twitch)
    dict(name="outline", shades=[15, 5, 4], finish=0.1, body=0),
    dict(name="hide", shades=[5, 4, 3, 2, 1], base=2, finish=0.25, body=0.08),
    dict(name="hide, spots", shades=[5, 4], base=0, finish=0.25, body=0.08),
    dict(name="hide, ear ring", shades=[5, 4], base=0, finish=0.25, body=0.08),
    dict(name="hide, ear center", shades=[10, 8], base=1, finish=0.25, body=0.08),
    dict(name="whiskers", shades=[5, 4, 2], base=2, finish=0.1, body=0.05),
    dict(name="spines", shades=[5, 4, 3, 2], base=2, finish=0.4, body=0),          # the forehead horn and the back barbs
    dict(name="claws and teeth", shades=[14, 13], base=1, finish=0.7, body=0.05),
    dict(name="mouth", shades=[7, 6], base=0, finish=0.8, body=0),
    dict(name="eye (line art)", shades=[7, 6, 13, 14], finish=0.9, body=0),
]
def to(name, colors): return {c: name for c in colors}
COLORS = {15: "outline", **to("hide", [1, 2, 3, 4, 5]), **to("mouth", [7, 6]), **to("hide, ear center", [10, 8]),
          **to("claws and teeth", [14, 13])}
EYE = to("eye (line art)", [7, 6, 13, 14])
SPINE = to("spines", [2, 3, 4, 5])
SPOT = to("hide, spots", [4, 5])
WHISKER = to("whiskers", [1, 2, 3, 4, 5])
STROKE = {5: "outline", 4: "outline"}
def rects(drawing, view, colors, *boxes):
    return [dict(view=view, drawings=[drawing], rect=list(b), colors=colors) for b in boxes]
RULES = [
    # the eye sits beside the mouth and the teeth, in the same reds and white
    dict(view="front", drawings=["ata", "ata-[2345]"], rect=[13, 3, 7, 5], colors=EYE),
    dict(drawings=["ata*-eyes-*", "head-eyes-*"], colors=EYE),
    dict(view="back", drawings=["head"], rect=[12, 6, 6, 3], colors=EYE),
    dict(view="back", drawings=["head-eyes-closed"], rect=[0, 5, 8, 1], colors={5: "outline"}),    # the shut eye's line
    # the horn
    *rects("ata", "front", SPINE, [15, 0, 3, 3]), *rects("ata-2", "front", SPINE, [15, 0, 3, 3]),
    *rects("ata-3", "front", SPINE, [15, 1, 3, 3]), *rects("ata-4", "front", SPINE, [15, 1, 3, 3]),
    *rects("ata-5", "front", SPINE, [15, 1, 3, 3]),
    dict(view="front", drawings=["ata*-eyes-*"], rect=[2, 1, 3, 1], colors=SPINE),
    *rects("head", "back", SPINE, [9, 1, 4, 3]),
    # the barbs on the back
    *rects("kara", "front", SPINE, [23, 10, 6, 3], [24, 13, 5, 2], [27, 16, 3, 2]),
    *rects("body", "back", SPINE, [5, 7, 2, 1], [5, 8, 4, 4], [4, 11, 1, 1], [5, 12, 3, 1], [5, 13, 3, 2], [5, 15, 1, 1]),
    # whiskers: free of the head they are pale strands; over the cheek they are drawn strokes
    *rects("ata", "front", WHISKER, [0, 10, 6, 4], [0, 14, 7, 3]), *rects("ata", "front", STROKE, [13, 9, 10, 8]),
    *rects("ata-2", "front", WHISKER, [0, 10, 6, 4], [0, 14, 7, 3]), *rects("ata-2", "front", STROKE, [13, 9, 10, 8]),
    *rects("ata-3", "front", WHISKER, [0, 11, 6, 4], [0, 15, 7, 3]), *rects("ata-3", "front", STROKE, [13, 10, 10, 8]),
    *rects("ata-4", "front", WHISKER, [0, 10, 5, 2], [0, 12, 6, 2], [0, 14, 7, 2]), *rects("ata-4", "front", STROKE, [13, 9, 10, 6]),
    *rects("ata-5", "front", WHISKER, [0, 8, 5, 1], [0, 9, 6, 1], [0, 10, 5, 2], [0, 12, 6, 2], [0, 14, 5, 1]),
    *rects("ata-5", "front", STROKE, [13, 8, 10, 7]),
    dict(view="back", drawings=["hige*"], colors=WHISKER),
    # the dark spots on the body
    *rects("kara", "front", SPOT, [20, 14, 4, 4], [25, 19, 1, 3], [21, 23, 3, 3]),
    *rects("asi2", "front", SPOT, [2, 7, 2, 2]),
    *rects("body", "back", SPOT, [16, 8, 4, 4], [22, 12, 3, 4], [11, 13, 4, 5], [18, 18, 2, 3]),
]
FLOODS = [
    # inside the ear: a dark ring around a teal center; the ring shares its color with the hide's contour
    dict(view="front", drawing="mimi", seeds=[[5, 7]], through=[5, 8, 10], colors={5: "hide, ear ring"}),
    dict(view="back", drawing="ear-r", seeds=[[12, 8]], through=[5, 4, 8, 10], colors={5: "hide, ear ring", 4: "hide, ear ring"}),
]
