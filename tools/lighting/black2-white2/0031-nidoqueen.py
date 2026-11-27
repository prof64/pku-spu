SOURCE = "sources/black2-white2/0031-nidoqueen.spu"
MATERIALS = [
    # black, and the dark line around the tongue
    dict(name="outline", shades=[15, 14], finish=0.1, body=0),
    # "armored with hard scales" (Diamond), painted flat and matte: the line's own hide
    dict(name="hide", shades=[14, 13, 12, 11], base=1, finish=0.25, body=0.08),
    # the cream lower jaw, chest and belly band
    dict(name="hide, belly", shades=[6, 5, 4, 3], base=1, finish=0.25, body=0.08),
    dict(name="hide, ear center", shades=[6, 5], base=0, finish=0.25, body=0.08),
    dict(name="spines", shades=[14, 13, 12, 11], base=1, finish=0.4, body=0),      # the horn, the back spines, the tail spine
    dict(name="claws and teeth", shades=[2, 1], base=1, finish=0.7, body=0.05),
    dict(name="mouth", shades=[9, 8, 7], base=0, finish=0.8, body=0),
    dict(name="eye (line art)", shades=[6, 2, 1], finish=0.9, body=0),
]
def to(name, colors): return {c: name for c in colors}
COLORS = {15: "outline", **to("hide", [14, 13, 12, 11]), **to("hide, belly", [6, 5, 4, 3]),
          **to("claws and teeth", [2, 1]), **to("mouth", [9, 8, 7])}
SPINE = to("spines", [11, 12, 13, 14])
def rects(drawings, view, colors, *boxes):
    return [dict(view=view, drawings=drawings, rect=list(b), colors=colors) for b in boxes]
RULES = [
    # the eyes are drawn only in the eye drawings: white, its gray, and the brown iris
    dict(drawings=["*-eyes-*"], colors=to("eye (line art)", [6, 2, 1])),
    # inside the ears, in the belly's browns
    dict(drawings=["mimi", "mimi2"], colors=to("hide, ear center", [6, 5])),
    # the open mouth: the tongue is outlined in the hide's dark color
    dict(view="front", drawings=["atama-[456]"], colors={14: "outline"}),
    # the spines down the back
    dict(view="back", drawings=["toge*"], colors=SPINE),
    # the horn at the front of the head
    *rects(["atama", "asi01-2"], "front", SPINE, [7, 6, 6, 4]),
    *rects(["atama", "mimi1-2"], "back", SPINE, [24, 8, 3, 1], [22, 9, 5, 1], [22, 10, 4, 1]),
    # the spine on the tail
    *rects(["o"], "front", SPINE, [15, 3, 2, 1], [14, 4, 5, 1], [14, 5, 7, 1], [15, 6, 5, 1], [15, 7, 2, 1]),
    *rects(["shippo"], "back", SPINE, [17, 2, 7, 6], [18, 8, 7, 1], [19, 9, 6, 1], [19, 10, 5, 1]),
]
# the lightest blue is a broad painted highlight (forehead, horn, thigh), not a glint
KEEP_TOP = ["hide", "spines"]
