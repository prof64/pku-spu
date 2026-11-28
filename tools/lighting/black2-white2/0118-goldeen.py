# Goldeen: a white fish with orange-red patches (pigment in the same skin), long thin billowing fins that carry
# the same patches, a cream horn, pink lips. The painted art shades all of it flat and soft, with no highlight
# anywhere: matte.
SOURCE = "sources/black2-white2/0118-goldeen.spu"
# Palette: 14 black; 4 3 the grays of the white's contour; 1 2 15 the white; 9 7 6 5 the orange-red; 8 tan (the
# horn, and in the fins the edge where a patch fades into white); 10 11 the lips; 12 13 the iris.
WHITE, ORANGE = [4, 3, 1, 2, 15], [9, 7, 6, 5]
MATERIALS = [
    # black; the dark red line where the two lips meet; the horn's gray edge (the palette has no step between
    # that gray and the horn's tan, so as a shade the whole horn fell to gray in daylight)
    dict(name="outline", shades=[14, 9, 4], finish=0.1, body=0),
    dict(name="fish skin", shades=WHITE, base=2, finish=0.15, body=0.08),
    # the orange-red patches and the eyelid: pigment in the same skin
    dict(name="fish skin, patches", shades=ORANGE, base=2, finish=0.15, body=0.08),
    dict(name="fish skin, lips", shades=[10, 11], base=1, finish=0.25, body=0.08),
    # dorsal, pectoral and tail fins: thin skin, painted flat and soft
    dict(name="fin", shades=WHITE, base=2, finish=0.3, body=0.15),
    dict(name="fin, patches", shades=[9, 7, 6, 8, 5], base=1, finish=0.3, body=0.15),
    # "its sharp horn": hard and solid, painted flat tan with a pale tip
    dict(name="spines, horn", shades=[8, 15], base=0, finish=0.4, body=0),
    dict(name="seams and wrinkles", shades=[], finish=0, body=0),   # fin rays inside a patch, the closed eye's line
    dict(name="eye (line art)", shades=[14, 13, 12, 9, 3, 1, 15], finish=0.9, body=0),
]
INNER = "seams and wrinkles"
def to(name, colors): return {c: name for c in colors}
COLORS = {14: "outline", **to("fish skin", WHITE), **to("fish skin, patches", ORANGE), 8: "spines, horn",
          **to("fish skin, lips", [10, 11]), **to("eye (line art)", [12, 13])}
EYE = to("eye (line art)", [14, 13, 12, 9, 3, 1, 15])
HORN = {4: "outline", **to("spines, horn", [8, 15])}
FRONT_EYE = [[8, 7, 3, 1], [5, 8, 7, 1], [6, 9, 6, 1], [6, 10, 5, 1], [7, 11, 3, 1]]
BACK_EYE = [[2, 4, 1, 1], [4, 4, 3, 1], [2, 5, 5, 1], [3, 6, 4, 1], [4, 7, 2, 1]]   # in the eye drawings; the body has it 22 right, 18 down
FINS = ["sebire*", "hand-*", "hire", "tail*", "obire*"]
RULES = [
    dict(drawings=FINS, colors={**to("fin", WHITE), **to("fin, patches", [9, 7, 6, 8, 5])}),
    # the fin rays drawn in dark red inside a patch: lines on the one sheet
    dict(drawings=FINS, interior={9: ([7, 6, 5, 8], INNER)}),
    # the horn
    dict(view="front", drawings=["body", "body-female"], rect=[4, 5, 9, 10], colors=HORN),
    dict(view="back", drawings=["karada", "karada-female"], rect=[17, 8, 6, 10], colors=HORN),
    # the dark red line between the lips
    dict(drawings=["mouse*"], colors={9: "outline"}),
    # closed eyes: the lid is the orange patch, its black line a line on the skin
    dict(drawings=["*-eyes-closed"], colors={14: INNER}),
] + [dict(view="front", drawings=["*-eyes-open"], rect=r, colors=EYE) for r in FRONT_EYE] \
  + [dict(view="back", drawings=["*-eyes-open"], rect=r, colors=EYE) for r in BACK_EYE] \
  + [dict(view="back", drawings=["karada", "karada-female"], rect=[r[0] + 22, r[1] + 18, r[2], r[3]], colors=EYE) for r in BACK_EYE]
