# Slowpoke: plain bare skin all over, painted flat in the official art (no highlight anywhere on it).
# "It lazes vacantly near water" (Gold); "A sweet sap leaks from its tail's tip" (Silver): nothing says wet or slick.
SOURCE = "sources/black2-white2/0079-slowpoke.spu"
# Palette: 1 black; 2 3 4 white and grays shared by the tail tip, the claws, the teeth and the eyes;
# 5 6 7 8 the cream muzzle; 9 10 11 12 13 the pink skin; 14 15 the inside of the mouth (they stay pink
# when the shiny palette turns the skin pale). The unused first color is a blue, so no white takes it.
PINK = [13, 12, 11, 10, 9]
CREAM = [8, 7, 6, 5]
WHITE = [4, 3, 2]
MATERIALS = [
    dict(name="outline", shades=[1], finish=0.1, body=0),
    # the body: its maroon contour is its darkest shade; both views together are mostly painted in 11
    dict(name="hide", shades=PINK, base=2, finish=0.25, body=0.08),
    # the cream muzzle and lower jaw: the same skin, paler. The front view paints its top in 5, the back view
    # (and the chin) in 7: the base is the step between. With 5 the back view's muzzle fell to brown in the
    # field and near black in the cave.
    dict(name="hide, muzzle", shades=CREAM, base=2, finish=0.25, body=0.08),
    # the white end of the tail: the same skin again; the dark gray is its contour
    dict(name="hide, tail tip", shades=WHITE, base=2, finish=0.25, body=0.08),
    dict(name="claws and teeth", shades=WHITE, base=2, finish=0.7, body=0.05),
    # the open mouth (front view): the tongue is the lighter pink
    dict(name="mouth", shades=[15, 14], base=0, finish=0.8, body=0),
    dict(name="eye (line art)", shades=[1, 3, 2], finish=0.9, body=0),
]
def to(name, colors): return {c: name for c in colors}
COLORS = {1: "outline", **to("hide", PINK), **to("hide, muzzle", CREAM), **to("claws and teeth", WHITE),
          **to("mouth", [15, 14])}
EYE = to("eye (line art)", [1, 3, 2])
RULES = [
    # the tail's white end, both views
    dict(drawings=["o2", "shippo1"], colors=to("hide, tail tip", WHITE)),
    # the eyes: whites and their gray edge; the one black pixel inside each is the pupil
    dict(drawings=["atama-eyes-open"], colors=to("eye (line art)", [3, 2])),
    dict(drawings=["atama-eyes-open"], rect=[6, 5, 4, 4], colors=EYE),
    dict(drawings=["atama-eyes-open"], rect=[17, 5, 6, 6], colors=EYE),
    # from behind the eye is two black pixels on the head itself
    dict(view="back", drawings=["atama"], rect=[20, 12, 2, 1], colors=EYE),
]
# The palest pink is few of the skin's pixels overall but one broad soft band on the forehead and one along
# the back: a shade, not a glint. Left out of the row it stayed as a gray blot on the head under the studio
# lamp and a pale one in the cave.
KEEP_TOP = ["hide"]
