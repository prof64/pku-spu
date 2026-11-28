# Muk: one body of wet, opaque goo, like Grimer. "Thickly covered with a filthy, vile sludge" (Red/Blue);
# "From MUK's body seeps a foul fluid" (Ruby); "A toxic fluid seeps from its body" (Diamond/Pearl, Black/White).
SOURCE = "sources/black2-white2/0089-muk.spu"
# dark contour and the thin dark folds (11), the darker wavy bands (10), the soft step between band and
# body (12), the body (9), its lit side (8), the pale wet patches on head and hands (7), and the palette's
# next paler step (6), which no pixel uses: the glint of a wet surface (as on Grimer)
SLUDGE = [11, 10, 12, 9, 8, 7, 6]
MATERIALS = [
    # black: the line around every blob and the closed eyes' lid lines
    dict(name="outline", shades=[15], finish=0.1, body=0),
    # the whole body, arms and the strands across the mouth. Base is the mid purple (9), as on Grimer.
    # The wavy darker bands are folds of the goo as it sags (the 3D model has none), so they stay its shades.
    dict(name="sludge", shades=SLUDGE, base=3, finish=0.7, body=0.2),
    # the gray tongue in the black mouth
    dict(name="mouth", shades=[5, 4, 3], base=1, finish=0.8, body=0),
    # the dark inside of the open mouth, drawn black: part of the mouth, only tinted by light. Not line art,
    # so the lips are not creased around it.
    dict(name="mouth, dark inside", shades=[], finish=0.8, body=0),
    dict(name="eye (line art)", shades=[15, 3, 1], finish=0.9, body=0),
]
def to(name, colors): return {c: name for c in colors}
COLORS = {15: "outline", **to("sludge", SLUDGE), **to("mouth", [5, 4, 3]), 1: "eye (line art)"}
EYE = to("eye (line art)", [15, 3, 1])
RULES = [
    # eyes: the shaded white, the white and the pupil; the lid line above stays line
    dict(view="front", drawings=["head-eyes-open"], rect=[5, 2, 6, 2], colors=EYE),
    dict(view="back", drawings=["head-eyes-open"], rect=[4, 3, 4, 2], colors=EYE),
    dict(view="back", drawings=["head"], rect=[45, 12, 4, 2], colors=EYE),
]
FLOODS = [
    # the black that fills the open mouth, from a pixel inside it (the body's part, and the part under the
    # upper lip that the head draws); the line under the tongue stays line
    dict(view="front", drawing="body", seeds=[[35, 10]], through=[15], colors={15: "mouth, dark inside"}),
    dict(view="front", drawing="head", seeds=[[15, 27], [30, 25]], through=[15], colors={15: "mouth, dark inside"}),
    dict(view="back", drawing="body", seeds=[[56, 3]], through=[15], colors={15: "mouth, dark inside"}),
]

# The eyes are a small drawing laid over the head (open or closed). A wet surface is lit round, and
# Smeargle rounds every drawing on its own, so the patch around the eye came out as a little pillow on
# the head: a pale box around the eye under a lamp. After facing is worked out, each sludge pixel of the
# eye drawings that is painted the same color as the head pixel under it takes that pixel's facing, so
# the head is one surface again. Light still gives the art back: same shade, same facing.
def lie_on_head(job, view, drawing, under="head"):
    top = job.s.read_picture(drawing=drawing, view=view, layer="facing")
    low = job.s.read_picture(drawing=under, view=view, layer="facing")
    dx, dy = int(top["x"]) - int(low["x"]), int(top["y"]) - int(low["y"])
    g, mg = job.grids[(view, drawing)], job.mgrids[(view, drawing)]
    G, MG = job.grids[(view, under)], job.mgrids[(view, under)]
    lowrows = [r.split() for r in low["rows"]]
    pixels = []
    for y, row in enumerate(top["rows"]):
        for x, cell in enumerate(row.split()):
            if cell == "." or mg[y][x] != "sludge": continue
            X, Y = x + dx, y + dy
            if not (0 <= Y < len(G) and 0 <= X < len(G[0])): continue
            if G[Y][X] != g[y][x] or MG[Y][X] != "sludge" or lowrows[Y][X] == ".": continue
            fx, fy = (int(v) for v in lowrows[Y][X].split(","))
            pixels.append([int(top["x"]) + x, int(top["y"]) + y, [fx/127, fy/127]])
    if pixels:
        job.s.paint_light(drawing=drawing, view=view, layer="facing", pixels=pixels,
                          intent="the patch around the eye lies on the head: it takes the head's facing")
    print(f"  {view}/{drawing}: {len(pixels)} pixels take the head's facing")

def AFTER(job):
    bake = job.bake
    def bake_then_lie():
        r = bake()
        for view in job.views:
            for d in ("head-eyes-open", "head-eyes-closed"):
                lie_on_head(job, view, d)
        return r
    job.bake = bake_then_lie
