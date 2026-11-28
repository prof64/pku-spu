# Zapdos: spiky yellow plumage all over, a second layer of black feathers behind the wings and tail, gray-brown
# tufts where the legs leave the body (all matte Feathers: the painted art shades them flat and soft), a long horn
# beak, bare orange legs, white talons. Nothing on it gives off light at rest.
# Colors: 1 black; 6 and 5 the dark and the softer brown line drawn around every warm surface; 4 3 the yellows;
# 8 7 the tufts' olive browns; 11 10 the oranges (beak and legs); 15 the talons' gray contour, 13 white,
# 14 a pale gray (one pixel of the eye; also the talons' shade).
# The brown line is outline, not each surface's darkest shade: the palette has no step between the yellow or the
# orange and that brown (5 is only ever a softened line), and as shades they spread olive and brown blotches over
# the wings and legs under a lamp and in the field.
SOURCE = "sources/black2-white2/0145-zapdos.spu"
F = dict(finish=-0.2, body=0.05)          # Feathers
MATERIALS = [
    dict(name="outline", shades=[1, 6, 5, 15], finish=0.1, body=0),
    # the yellow plumage: mid yellow (4) is what most of it is painted in, both views
    dict(name="feathers", shades=[4, 3], base=0, **F),
    # the black layer behind the wings and tail: painted flat black, so light only tints it
    dict(name="feathers, black", shades=[], **F),
    dict(name="feathers, thighs", shades=[8, 7], base=0, **F),
    dict(name="beak", shades=[11, 10], base=1, finish=0.4, body=0.05),
    dict(name="dry hide, legs", shades=[11, 10], base=0, finish=0.05, body=0.03),
    # white talons: the palette's pale gray is their shade (their dark gray contour is line)
    dict(name="claws and teeth", shades=[14, 13], base=1, finish=0.7, body=0.05),
    dict(name="eye (line art)", shades=[1, 14, 13], finish=0.9, body=0),
]
def to(name, colors): return {c: name for c in colors}
LINE, YELLOW, BLACK, THIGH, BEAK, LEGS, CLAW, EYE = (
    "outline", "feathers", "feathers, black", "feathers, thighs", "beak", "dry hide, legs", "claws and teeth", "eye (line art)")
COLORS = {**to(LINE, [1, 5, 6, 15]), **to(YELLOW, [3, 4]), **to(THIGH, [7, 8]), **to(LEGS, [10, 11]), 13: CLAW}

UNDER = ["hane02", "hane03", "hane-l2", "hane-r2"]       # the black feathers behind the wings: whole drawings
RULES = [
    # black feathers behind the wings and between the tail's yellow ones; one-pixel tips and strokes stay the line
    dict(drawings=UNDER + ["o"], colors={1: BLACK}, thin_all={1: LINE}),
    # beak: everything orange on the head
    dict(drawings=["atama", "atama-eyes-*"], colors=to(BEAK, [10, 11])),
    # the eye: a black wedge with a white glint (open), a black lid (closed)
    dict(view="front", drawings=["atama-eyes-*"], rect=[11, 0, 5, 6], colors=to(EYE, [1, 13, 14])),
]
