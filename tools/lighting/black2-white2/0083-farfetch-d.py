# Farfetch'd: a wild duck. Brown plumage above, cream below and inside the wings (matte Feathers), a black
# brow mark, a horny bill, bare webbed feet, and the plant stalk it carries (a green onion: "The sprig of
# green onions it holds is its weapon", Red/Blue; "The plant stalk it holds is its weapon", LeafGreen/X).
# Colors: 15 black; 14 13 12 11 the browns; 4 3 the creams; 7 6 5 the bill's and feet's oranges;
# 10 9 8 the stalk's greens; 2 1 gray and white (the eyes, the stalk's white end).
SOURCE = "sources/black2-white2/0083-farfetch-d.spu"
F = dict(finish=-0.2, body=0.05)          # Feathers
STALK = dict(finish=0.1, body=0.1)       # Bud and bulb: matte, a little light through
MATERIALS = [
    # black, and the brown lines between feathers
    dict(name="outline", shades=[15, 14, 13], finish=0.1, body=0),
    # the brown plumage: head, crest, back, tail, the outside of the wings. Base is the mid brown (13)
    # nearly all of it is painted in, both views.
    dict(name="feathers", shades=[14, 13, 12, 11], base=1, **F),
    # the cream belly and the inside of the wings, drawn with the browns as its contour and its edge
    dict(name="feathers, cream", shades=[14, 13, 12, 4, 3], base=3, **F),
    # the black V over the eyes: pigment in the plumage, drawn black, so light only tints it
    dict(name="feathers, brow mark", shades=[], **F),
    dict(name="beak", shades=[14, 7, 6, 5], base=2, finish=0.4, body=0.05),
    dict(name="dry hide, legs", shades=[14, 7, 6, 5], base=1, finish=0.05, body=0.03),
    # the stalk's green blades (dark at the tips, mid green below)
    dict(name="leaves", shades=[10, 9], base=1, finish=0.15, body=0.1),
    # the stalk's pale sheath under the blades, with the greens as its contour
    dict(name="stalk", shades=[10, 9, 8], base=2, **STALK),
    # its white end, and the tan root plate at the very bottom
    dict(name="stalk, white end", shades=[2, 1], base=0, **STALK),
    dict(name="stalk, root", shades=[11], base=0, **STALK),
    dict(name="eye (line art)", shades=[15, 2, 1], finish=0.9, body=0),
]
def to(name, colors): return {c: name for c in colors}
LINE, CREAM, BEAK, LEGS = "outline", "feathers, cream", "beak", "dry hide, legs"
COLORS = {15: LINE, **to("feathers", [14, 13, 12, 11]), **to(CREAM, [4, 3]), **to(BEAK, [7, 6, 5]),
          **to("leaves", [10, 9]), 8: "stalk", **to("stalk, white end", [2, 1])}
EYE = to("eye (line art)", [15, 2, 1])
BROW = {15: "feathers, brow mark"}
# the dark green drawn around the white end is the stalk's own contour shade: as line art it stayed bright in the cave
WHITE_END = {**to("stalk, white end", [2, 1]), 11: "stalk, root", 10: "stalk"}
RULES = [
    # wings are layers of feathers: the dark lines between them and around them are creases
    dict(drawings=["hane01", "hane02", "hane03", "hand-*"], thin_all={14: LINE}),
    # the wing seen from inside (front view) is all cream; its mid-brown strokes are softer lines between feathers
    dict(drawings=["hane01"], colors={12: CREAM}, thin_all={13: LINE}),
    dict(drawings=["hane02"], rect=[8, 24, 9, 2], colors={13: CREAM}),          # the cream's bottom contour
    # the crest is three feathers side by side
    dict(view="front", drawings=["atama"], rect=[11, 4, 12, 9], colors={14: LINE}),
    dict(view="back", drawings=["head"], rect=[11, 3, 12, 8], colors={14: LINE}),
    # front body: the cream belly's contour down the left and along the bottom, and its soft edge to the brown
    dict(view="front", drawings=["karada"], colors={12: CREAM}),
    dict(view="front", drawings=["karada"], rect=[0, 12, 9, 16], colors=to(CREAM, [13, 14])),
    dict(view="front", drawings=["karada"], rect=[15, 27, 3, 1], colors=to(CREAM, [13, 14])),
    # back body: the belly shows at the lower right
    dict(view="back", drawings=["body"], rect=[10, 17, 20, 11], colors={14: CREAM}),
    # bill: its brown contour is its darkest shade; the line between its halves is line
    dict(view="front", drawings=["atama"], rect=[6, 20, 13, 7], colors={14: BEAK}),
    dict(view="front", drawings=["atama"], rect=[16, 24, 1, 1], colors={14: LINE}),
    dict(view="front", drawings=["atama"], rect=[13, 25, 1, 1], colors={14: LINE}),
    dict(drawings=["atama-eyes-*"], rect=[7, 10, 8, 2], colors={14: BEAK}),
    dict(drawings=["atama-eyes-*"], rect=[5, 12, 10, 1], colors={14: BEAK}),
    dict(view="back", drawings=["head"], rect=[24, 18, 5, 6], colors={14: BEAK}),
    # the brow mark
    dict(view="front", drawings=["atama"], rect=[12, 15, 5, 4], colors=BROW),
    dict(drawings=["atama-eyes-*"], rect=[8, 5, 5, 4], colors=BROW),
    # eyes (open): white, gray and pupil
    dict(drawings=["atama-eyes-open"], rect=[6, 7, 2, 5], colors=EYE),
    dict(drawings=["atama-eyes-open"], rect=[13, 6, 4, 6], colors=EYE),
    # legs and webbed feet: bare skin
    dict(drawings=["asi0*", "foot-*"], colors=to(LEGS, [14, 7, 6, 5])),
    # the stalk: blades above, pale sheath below, the white end under the wing that grips it
    dict(view="front", drawings=["hane03"], rect=[0, 18, 16, 10], colors=to("stalk", [10, 9, 8])),
    dict(view="front", drawings=["hane03"], rect=[0, 38, 16, 8], colors=WHITE_END),
    dict(view="back", drawings=["hand-l"], rect=[0, 17, 24, 8], colors=to("stalk", [10, 9, 8])),
    dict(view="back", drawings=["hand-l"], rect=[0, 35, 24, 10], colors=WHITE_END),
]
# the palest brown is on a few pixels at the wings' edge and the neck: kept in the row, so it darkens with
# the plumage (left out, those pixels stayed pale on a wing gone dark with the sun behind)
KEEP_TOP = ["feathers"]
FLOODS = [
    # back body: the soft edge between the cream and the brown belongs to the cream
    dict(view="back", drawing="body", seeds=[[24, 21]], through=[3, 4, 12], colors={12: CREAM}),
]
