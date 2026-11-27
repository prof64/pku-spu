# Grimer: one body of wet, opaque goo. "It constantly leaks a horribly germ-infested fluid from all over
# its body" (Sapphire); "sludgy and rubbery body" (Ruby); "Made of hardened sludge" (Yellow).
SOURCE = "sources/black2-white2/0088-grimer.spu"
# dark contour (11), the darker wavy bands (10), the body (9), its lit side (8), the pale wet patches on
# head and hands (7), and the palette's next paler step (6), which no pixel uses: the glint of a wet surface
SLUDGE = [11, 10, 9, 8, 7, 6]
MATERIALS = [
    # black: the line around every blob and the closed eyes' lid lines
    dict(name="outline", shades=[15], finish=0.1, body=0),
    # the whole body. Base is the mid purple (9) most of both views is painted in. The wavy darker bands
    # are folds of the goo as it sags (the 3D model has no stripes at all), so they stay its own shades.
    # Finish 0.7, not the starting 0.6: at exactly 0.6 Smeargle still lights a surface flat, and the
    # roundness and moving highlights of a wet surface only start above it.
    dict(name="sludge", shades=SLUDGE, base=2, finish=0.7, body=0.2),
    # the gray tongue in the black mouth (front view only)
    dict(name="mouth", shades=[5, 4, 3], base=1, finish=0.8, body=0),
    # the dark inside of the open mouth, drawn black: part of the mouth, only tinted by light. Not line
    # art, so the chin is not creased around it.
    dict(name="mouth, dark inside", shades=[], finish=0.8, body=0),
    dict(name="eye (line art)", shades=[15, 2, 1], finish=0.9, body=0),
]
def to(name, colors): return {c: name for c in colors}
COLORS = {15: "outline", **to("sludge", SLUDGE), **to("mouth", [5, 4, 3]), **to("eye (line art)", [2, 1])}
EYE = to("eye (line art)", [15, 2, 1])
RULES = [
    # the pupils are the only black inside these: every other black is the line or the mouth
    dict(view="front", drawings=["atama"], rect=[11, 5, 6, 5], colors=EYE),
    dict(drawings=["atama-eyes-open"], rect=[4, 6, 14, 5], colors=EYE),
    dict(drawings=["body3-eyes-open"], colors=EYE),
]
FLOODS = [
    # the black that fills the open mouth, from a pixel inside it; the line under the tongue stays line
    dict(view="front", drawing="ago", seeds=[[8, 2]], through=[15], colors={15: "mouth, dark inside"}),
]

# The chin (front view) swings: the idle animation holds it turned 20 degrees at rest and brings it
# upright and back. Facing is worked out in a drawing's own upright frame, so on the turned chin the
# light fell 20 degrees off and nine pixels at its edge came out a shade away from the art at rest.
# After facing is worked out, each chin pixel that leaves its painted shade anywhere in the swing is
# turned to the nearest facing that keeps it, so light gives the art back at rest and all through.
import math
_L = [-0.5, 0.6, 0.62]; _k = math.sqrt(sum(a*a for a in _L)); _L = [a/_k for a in _L]

def _shade(n, shades, body, base):
    """Where on its row of shades the art's own light puts a pixel facing n (Smeargle's rule), unrounded."""
    t = min(1.0, max(0.0, (shades - 3)/6)); cl = max(body, 0.0)
    ss = 1 - abs(2*cl - 1) if cl > 0 else 0.0
    g = max(2.0, (shades - 1)*(1 - 0.55*t*t*(3 - 2*t)))*(1 - 0.45*ss)
    up, dn = max(g, (shades - 0.5 - base)/0.32), max(g, (base + 0.5)/1.2)
    e = sum(a*b for a, b in zip(n, _L)) - 0.6
    return base + e*(up if e > 0 else dn)

def _posed(bx, by, m):
    """A stored facing as it stands once its part is turned by m (Smeargle's rule)."""
    nx, ny = (bx - 128)/127, -(by - 128)/127
    rx, ry = m[0]*nx + m[2]*ny, -(m[1]*nx + m[3]*ny)
    return [rx, ry, math.sqrt(1 - min(rx*rx + ry*ry, 0.999))]

def hold_through_swing(job, view, part, drawing, reach=48):
    an = job.s.read_animation(animation="idle")
    track = next(t for t in an["views"][view]["tracks"] if t["part"] == part)
    rest = track["rotation"][0][1]
    angles = sorted({round(k[1], 3) for k in track["rotation"]} | {rest}, key=lambda a: abs(a - rest))   # rest first
    turns = [[math.cos(a), math.sin(a), -math.sin(a), math.cos(a)] for a in map(math.radians, angles)]
    mats = {x["name"]: x for x in job.s.overview()["materials"]}
    g, mg = job.grids[(view, drawing)], job.mgrids[(view, drawing)]
    pic = job.s.read_picture(drawing=drawing, view=view, layer="facing")
    ox, oy = int(pic["x"]), int(pic["y"])      # pixel tools count from the part's origin
    pixels = []; partly = 0
    for y, row in enumerate(pic["rows"]):
        for x, cell in enumerate(row.split()):
            if cell == ".": continue
            mat = mats[mg[y][x]]; sh = mat["shades"]
            if mat["line"] or len(sh) < 2 or g[y][x] not in sh: continue
            want = sh.index(g[y][x])
            # on its shade with room to spare (a shade is one wide; stay within 0.35 of its middle)
            on = lambda bx, by, m: abs(_shade(_posed(bx, by, m), len(sh), mat["body"], mat["base"]) - want) <= 0.35
            holds = lambda bx, by: sum(on(bx, by, m) for m in turns)
            fx, fy = (int(v) for v in cell.split(","))
            bx, by = fx + 128, fy + 128
            if holds(bx, by) == len(turns): continue
            n = _posed(bx, by, [1, 0, 0, 1]); best = None
            for cy in range(max(0, by - reach), min(255, by + reach) + 1):
                for cx in range(max(0, bx - reach), min(255, bx + reach) + 1):
                    if (cx - 128)**2 + (cy - 128)**2 > 126**2: continue
                    if not on(cx, cy, turns[0]): continue   # at rest, always
                    c = _posed(cx, cy, [1, 0, 0, 1])
                    score = (holds(cx, cy), sum(p*q for p, q in zip(c, n)))
                    if best is None or score > best[0]: best = (score, cx, cy)
            if best is None: partly += 1; continue
            if best[0][0] < len(turns): partly += 1
            pixels.append([ox + x, oy + y, [(best[1] - 128)/127, (best[2] - 128)/127]])
    if pixels:
        job.s.paint_light(drawing=drawing, view=view, layer="facing", pixels=pixels,
                          intent="the chin swings 20 degrees: keep each pixel on its painted shade through the swing")
    print(f"  {view}/{drawing}: {len(pixels)} pixels turned to hold their shade through the swing"
          + (f", {partly} of them not at every angle" if partly else ""))

def AFTER(job):
    bake = job.bake
    def bake_then_hold():
        r = bake()
        hold_through_swing(job, "front", "ago", "ago")
        return r
    job.bake = bake_then_hold
