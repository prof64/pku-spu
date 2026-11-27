SOURCE = "sources/black2-white2/0050-diglett.spu"
ROCK = [9, 8, 7]
MATERIALS = [
    # black, and the dark brown the shut eyes are drawn in
    dict(name="outline", shades=[11, 15], finish=0.1, body=0),
    # the brown skin: plain bare skin, painted with flat soft shading (the pale patch on the crown is the
    # dome catching light, not a sheen). Its dark-brown contour (15) is its darkest shade
    dict(name="hide", shades=[15, 14, 13, 12], base=2, finish=0.25, body=0.08),
    # the column under the head, which the art paints in the one shadow brown (14): the same hide with that
    # brown as its base (see AFTER)
    dict(name="hide, lower body", shades=[15, 14, 13], base=1, finish=0.25, body=0.08),
    # the nose: the painted art gives it, and nothing else, a crisp pale highlight
    dict(name="nose", shades=[5, 4, 3, 2], base=1, finish=0.45, body=0.08),
    # the dug-up earth and stones around it: dead matte and solid
    # (base is the mid olive: the light one is a little ahead in what shows, but as base it dropped every
    # shaded face to the darkest olive in the field and the cave, and the stones went blotchy)
    dict(name="rock", shades=ROCK, base=1, finish=0, body=0),
    # the pale tops (6) of the two biggest stones: the same stone at its most lit, in their own row so they
    # darken with the rest
    dict(name="rock, lit faces", shades=ROCK + [6], base=1, finish=0, body=0),
    dict(name="eye (line art)", shades=[11, 1], finish=0.9, body=0),
]
def to(name, colors): return {c: name for c in colors}
COLORS = {11: "outline", **to("hide", [15, 14, 13, 12]), **to("nose", [5, 4, 3, 2]), **to("rock", ROCK),
          6: "rock, lit faces", 1: "eye (line art)"}
KEEP_TOP = ["hide", "nose"]
RULES = [
    dict(drawings=["body", "body-2"], colors={14: "hide, lower body"}),
    # the eyes: black ovals with a white catchlight; shut, they are two short drawn lines
    dict(drawings=["head-eyes-open"], colors={11: "eye (line art)", 1: "eye (line art)"}),
    dict(drawings=["head-eyes-closed"], colors={15: "outline", 11: "outline"}),
]

# The column under the head is one flat brown, and the idle animation holds it squashed to half its height at
# rest and stretches it as Diglett bobs. Facing is worked out in a drawing's own unsquashed frame, so on the
# squashed column the pixels along its edge came out a shade away from the art. After facing is worked out,
# the column is laid flat (facing the viewer): it shows its base brown at rest and at every stretch.
def lie_flat(job, drawings):
    for (view, d), g in job.grids.items():
        if d not in drawings: continue
        mg = job.mgrids[(view, d)]
        pic = job.s.read_picture(drawing=d, view=view, layer="facing")
        ox, oy = int(pic["x"]), int(pic["y"])      # pixel tools count from the part's origin
        pixels = [[ox + x, oy + y, [0, 0]] for y, row in enumerate(g) for x, c in enumerate(row)
                  if c is not None and mg[y][x] == "hide, lower body"]
        job.s.paint_light(drawing=d, view=view, layer="facing", pixels=pixels,
                          intent="the squashed column lies flat, so it keeps its shade at any stretch")

def AFTER(job):
    bake = job.bake
    def bake_then_flatten():
        r = bake()
        lie_flat(job, ["body", "body-2"])
        return r
    job.bake = bake_then_flatten
