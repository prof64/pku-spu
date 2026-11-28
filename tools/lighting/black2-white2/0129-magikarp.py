# Magikarp: a carp. Red-orange fish skin with drawn scale lines, peach lips round an open mouth, white fins
# (tail, pectoral) on red rays, a stiff yellow crown fin and belly fin, and two long barbels (yellow on the male,
# white on the female). No Pokédex entry describes any surface; the painted art shades everything flat and soft.
# Palette: 1 black; 7 6 5 4 3 the body (7 and 6 its contour and scale lines); 2 the lips' pale top;
# b a 9 8 the yellows; f e d c the grays and white (fins, eye, the female's barbels).
SOURCE = "sources/black2-white2/0129-magikarp.spu"
RED, YELLOW, GRAY = [7, 6, 5, 4, 3], [11, 10, 9, 8], [15, 14, 13, 12]
MATERIALS = [
    dict(name="outline", shades=[1], finish=0.1, body=0),
    # body, tail stalk and the red rays that carry the white fins; the scale lines are its own dark shades
    dict(name="fish skin", shades=RED, base=2, finish=0.15, body=0.08),
    dict(name="fish skin, lips", shades=[7, 6, 5, 3, 2], base=3, finish=0.25, body=0.08),
    dict(name="fish skin, barbels", shades=YELLOW, base=3, finish=0.15, body=0.08),
    dict(name="fish skin, barbels (female)", shades=GRAY, base=3, finish=0.15, body=0.08),
    # the white webbing of the tail and pectoral fins: thin skin, painted flat white with soft gray shading
    dict(name="fin", shades=GRAY, base=3, finish=0.3, body=0.15),
    # the yellow crown fin on the back and the fin under the belly: the same thin skin, opaque yellow
    dict(name="fin, yellow", shades=YELLOW, base=1, finish=0.3, body=0.15),
    # the red floor of the open mouth
    dict(name="mouth", shades=[6, 5], base=1, finish=0.8, body=0),
    # the dark inside of the open mouth, drawn black: part of the mouth, only tinted by light
    dict(name="mouth, dark inside", shades=[], finish=0.8, body=0),
    dict(name="seams and wrinkles", shades=[], finish=0, body=0),   # black notches where scale lines meet: not creases
    dict(name="eye (line art)", shades=[1, 13, 12], finish=0.9, body=0),
]
INNER = "seams and wrinkles"
def to(name, colors): return {c: name for c in colors}
def dots(view, drawing, points, colors):
    return [dict(view=view, drawings=[drawing], rect=[x, y, 1, 1], colors=colors) for x, y in points]
COLORS = {1: "outline", **to("fish skin", RED), **to("fin, yellow", YELLOW), **to("fin", GRAY)}
EYE = to("eye (line art)", [1, 13, 12])
RULES = [
    dict(drawings=["hige2*", "r-parts02*"], colors=to("fish skin, barbels", YELLOW)),
    dict(drawings=["hige2*-female", "r-parts02*-female"], colors=to("fish skin, barbels (female)", GRAY)),
    # the lips; the one orange pixel at their edge stays body
    dict(drawings=["kuti2"], colors=to("fish skin, lips", [7, 6, 5, 3, 2])),
    dict(drawings=["kuti2"], rect=[8, 9, 3, 3], colors=to("mouth", [6, 5])),
    *dots("front", "kuti2", [(5, 6), (6, 6), (7, 6), (8, 6), (6, 7), (7, 7), (8, 7), (9, 7), (7, 8), (8, 8), (9, 8), (7, 9)],
          {1: "mouth, dark inside"}),
    # the eye: white, its gray edge and the pupil, on the body and again on the eyes drawings
    dict(view="front", drawings=["karada2"], rect=[13, 9, 6, 8], colors=EYE),
    dict(view="back", drawings=["body02"], rect=[27, 10, 6, 7], colors=EYE),
    dict(drawings=["karada2-eyes-*", "body02-eyes-*"], colors=EYE),
    # one gray pixel on the body's edge where the tail fin starts
    dict(view="front", drawings=["karada2"], rect=[34, 20, 1, 1], colors={15: "outline"}),
    # black notches where scale lines cross, wholly inside the body
    dict(drawings=["karada2", "body02"], interior={1: (RED, INNER)}),
]
# the crown's pale yellow is the lit side of its tall spike (a block of pixels, not a glint): left out of the
# row it would stay pale on a crown gone dark
KEEP_TOP = ["fin, yellow"]
