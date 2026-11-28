SOURCE = "sources/black2-white2/0144-articuno.spu"
# Articuno: blue plumage all over, a pale chest tuft, a darker blue crest and long tail streamers, a horn-brown
# beak, bare brown legs, pale claws, red eyes. The painted art shades all of it softly with no highlight: matte.
# Colors: 1 black; 7 6 the navy and dark teal (contours and the lines between feathers; on the tail 6 is also
# the streamers' shadow side); 5 the tail's and crest's blue; 2 4 3 the plumage blues; 12 the chest's pale blue;
# 15 14 13 the browns; 10 9 8 dark gray, gray, white (claws, eye); 11 red (eye, mouth).
FEATHERS = dict(finish=-0.2, body=0.05)
MATERIALS = [
    # black; and the navy, dark teal and (around the chest tuft) blue contours of the plumage. The palette has no
    # step between the plumage blues and those dark contours: as the plumage's darkest shades the body and wings
    # speckled dark teal in the field and the cave.
    dict(name="outline", shades=[1, 7, 6, 5], finish=0.1, body=0),
    # head, body, belly, thighs
    dict(name="feathers", shades=[2, 4], base=0, **FEATHERS),
    # the wings: the same matte plumage, but light comes through it. Gold/HeartGold: "The magnificent, seemingly
    # translucent wings of this legendary bird Pokémon are said to be made of ice." The art paints them as
    # opaque soft plumage with no highlight, so not glass: the value thin wings have elsewhere (0.3).
    dict(name="feathers, wings", shades=[2, 4, 3], base=1, finish=-0.2, body=0.3),
    # the pale tuft down the chest; its soft edge and feather strokes are the light blues
    dict(name="feathers, chest", shades=[4, 3, 12], base=2, **FEATHERS),
    # the crest and the long tail streamers: one darker blue. Most of it, both views together, is the dark teal.
    # Four pale pixels on the crest (color 3) are painted glints and stay as painted.
    dict(name="feathers, crest and tail", shades=[7, 6, 5, 4], base=1, **FEATHERS),
    dict(name="beak", shades=[15, 14, 13], base=2, finish=0.4, body=0.05),
    dict(name="dry hide, legs", shades=[15, 14, 13], base=1, finish=0.05, body=0.03),
    dict(name="claws and teeth", shades=[10, 9, 8], base=2, finish=0.7, body=0.05),
    dict(name="mouth", shades=[11], base=0, finish=0.8, body=0),
    dict(name="eye (line art)", shades=[1, 11, 9, 8], finish=0.9, body=0),
]
def to(name, colors): return {c: name for c in colors}
BODY, WINGS, CHEST, TAIL, BEAK, LEGS, CLAWS, LINE, EYE = (
    "feathers", "feathers, wings", "feathers, chest", "feathers, crest and tail", "beak", "dry hide, legs",
    "claws and teeth", "outline", "eye (line art)")
COLORS = {**to(LINE, [1, 7, 6, 5]), **to(BODY, [2, 4]), 12: CHEST, **to(LEGS, [15, 14, 13]),
          **to(CLAWS, [10, 9, 8]), 11: "mouth"}
WING_DRAWINGS = ["wing-*", "part-1*", "l-wings*", "r-wings*"]
TAIL_DRAWINGS = ["uneune2", "tail1a", "tail01", "tail02"]
KEEP_TOP = [TAIL]       # the light blue on top of the tail's bend is broad shading, not a glint
RULES = [
    # wings: layers of feathers; the dark lines between them are creases (the outline row, by COLORS)
    dict(drawings=WING_DRAWINGS, colors=to(WINGS, [2, 4, 3])),
    # tail streamers: long feathers side by side; the navy lines between them are creases. The dark teal is
    # the streamers' shadow side as well as their streaks, so it stays a shade. (The patch of body blue the
    # back view's tail drawing carries is the rump: body plumage.)
    dict(drawings=TAIL_DRAWINGS, colors=to(TAIL, [7, 6, 5, 4]), thin_all={7: LINE}),
    # crest
    dict(view="front", drawings=["hear"], colors=to(TAIL, [7, 6, 5, 4, 3])),
    dict(view="back", drawings=["body01"], rect=[5, 2, 17, 9], colors=to(TAIL, [7, 6, 5, 4])),
    dict(view="back", drawings=["body01-eyes-*"], rect=[0, 0, 8, 1], colors=to(TAIL, [7, 6])),
    # chest tuft, front: all of the drawing but the body blue at its top
    dict(view="front", drawings=["mune"], colors=to(CHEST, [4, 3])),
    # chest tuft, back: the pale part (FLOODS) and its far edge
    dict(view="back", drawings=["body01"], rect=[27, 28, 2, 9], colors=to(CHEST, [4])),
    # beak
    dict(view="front", drawings=["mouse1", "mouse2"], colors=to(BEAK, [15, 14, 13])),
    dict(view="back", drawings=["body01"], rect=[19, 13, 4, 5], colors=to(BEAK, [15, 14, 13])),
    dict(view="back", drawings=["body01-eyes-*"], rect=[5, 3, 3, 5], colors=to(BEAK, [15, 14, 13])),
    # eyes: black rim, white, gray, red iris
    dict(view="front", drawings=["body-eyes-open"], rect=[2, 2, 4, 3], colors=to(EYE, [1, 8, 11])),
    dict(view="back", drawings=["body01-eyes-open"], rect=[3, 1, 3, 4], colors=to(EYE, [1, 8, 9, 11])),
]
FLOODS = [
    dict(view="back", drawing="body01", seeds=[[23, 24]], through=[12, 3], colors=to(CHEST, [12, 3])),
]
