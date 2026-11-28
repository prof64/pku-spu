# Gyarados: Magikarp grown into a sea serpent. Blue fish skin (body, head, the three-pronged crest, the male's
# barbels), a cream belly of overlapping segments, cream ovals along the flanks, a cream jaw rim, white fins
# (back, face, tail) on blue ribs, fangs, a wide open mouth. The female's barbels are white. No Pokédex entry
# describes any surface; the painted art shades everything flat and soft, with no highlight anywhere.
# Palette: 1 black; 2 3 4 5 6 the blues (2 the navy contour and deep shade, 6 the painted pale patches);
# 7 8 9 gray, pale lavender, white (fins, fangs, eye, the female's barbels); a b c the reds (mouth, eye);
# d e f brown, cream, pale cream (belly, flank ovals, jaw rim).
SOURCE = "sources/black2-white2/0130-gyarados.spu"
BLUE, WHITE, CREAM = [2, 3, 4, 5, 6], [7, 8, 9], [13, 14, 15]
MATERIALS = [
    # black; the belly's brown edge and the lines between its segments (one segment overlaps the next); and the
    # fins' gray edge. Neither pale surface has a step between its color and that dark line.
    dict(name="outline", shades=[1, 13, 7], finish=0.1, body=0),
    # the same matte skin as Magikarp's: the art paints the coils flat blue with soft broad shading
    dict(name="fish skin", shades=BLUE, base=2, finish=0.15, body=0.08),
    dict(name="fish skin, barbels", shades=BLUE, base=2, finish=0.15, body=0.08),
    dict(name="fish skin, barbels (female)", shades=WHITE, base=1, finish=0.15, body=0.08),
    dict(name="fish skin, belly", shades=[14, 15], base=0, finish=0.15, body=0.08),
    # the cream ovals along the flanks: pigment in the blue skin
    dict(name="fish skin, flank spots", shades=[14, 15], base=1, finish=0.15, body=0.08),
    # the cream rim of the jaws, shaded in the brown
    dict(name="fish skin, jaw", shades=CREAM, base=1, finish=0.15, body=0.08),
    # the white webbing of the back, face and tail fins: thin skin, painted flat
    dict(name="fin", shades=[8, 9], base=0, finish=0.3, body=0.15),
    dict(name="claws and teeth", shades=WHITE, base=2, finish=0.7, body=0.05),
    dict(name="mouth", shades=[10, 11, 12], base=1, finish=0.8, body=0),
    # the throat, drawn black: part of the mouth, only tinted by light
    dict(name="mouth, dark inside", shades=[], finish=0.8, body=0),
    dict(name="seams and wrinkles", shades=[], finish=0, body=0),   # fin rays, closed eyelids: lines, not creases
    dict(name="eye (line art)", shades=[1, 8, 9, 10, 11, 12], finish=0.9, body=0),
]
INNER = "seams and wrinkles"
def to(name, colors): return {c: name for c in colors}
def dots(view, drawings, points, colors):
    return [dict(view=view, drawings=drawings, rect=[x, y, 1, 1], colors=colors) for x, y in points]
COLORS = {1: "outline", 13: "outline", 7: "outline", **to("fish skin", BLUE), **to("fin", [8, 9]),
          **to("fish skin, belly", [14, 15]), **to("mouth", [10, 11, 12])}
F, B = "front", "back"
HEADS, EYES = ["atama", "atama-female"], ["atama-eyes-open", "atama-female-eyes-open"]
SHUT = ["atama-eyes-closed", "atama-female-eyes-closed"]
EYE, TOOTH = to("eye (line art)", [8, 9, 10, 11, 12]), to("claws and teeth", WHITE)
MALE, FEMALE = to("fish skin, barbels", BLUE), to("fish skin, barbels (female)", WHITE)
RULES = [
    # fin rays: gray lines wholly inside the one flat sheet
    dict(drawings=["karada0*", "mimi0*", "o", "hire", "body*"], interior={7: ([8, 9], INNER)}),
    # the head and lower jaw: the cream is the jaw rim, brown its shade
    dict(drawings=["atama*", "ago"], colors=to("fish skin, jaw", CREAM)),
    # fangs: two in the upper jaw (on the head), the lower ones on the jaw
    dict(view=F, drawings=HEADS, rect=[11, 28, 3, 5], colors=TOOTH),
    dict(view=F, drawings=HEADS, rect=[20, 28, 2, 3], colors=TOOTH),
    dict(drawings=["ago"], colors=TOOTH),
    dict(view=F, drawings=["ago"], rect=[7, 5, 9, 5], colors={1: "mouth, dark inside"}),
    # the barbels: on the head in front, their own drawings behind
    dict(view=F, drawings=["atama"], rect=[9, 34, 8, 13], colors=MALE),
    dict(view=F, drawings=["atama"], rect=[32, 24, 15, 22], colors=MALE),
    dict(view=F, drawings=["atama-female"], rect=[9, 34, 8, 13], colors=FEMALE),
    dict(view=F, drawings=["atama-female"], rect=[32, 24, 15, 22], colors=FEMALE),
    dict(view=B, drawings=["hige-r", "hige-l"], colors=MALE),
    dict(view=B, drawings=["hige-r-female", "hige-l-female"], colors=FEMALE),
    # the eyes (front only): white, red iris, pupil; on the head and again on the eyes drawings, 7 left and 14 up
    dict(view=F, drawings=HEADS, rect=[19, 17, 5, 5], colors=EYE),
    dict(view=F, drawings=HEADS, rect=[10, 22, 2, 2], colors=EYE),
    *dots(F, HEADS, [(20, 21)], {1: "eye (line art)"}),
    dict(view=F, drawings=EYES, rect=[12, 3, 5, 5], colors=EYE),
    dict(view=F, drawings=EYES, rect=[3, 8, 2, 2], colors=EYE),
    *dots(F, EYES, [(13, 7)], {1: "eye (line art)"}),
    *dots(F, SHUT, [(16, 5), (16, 6), (15, 7), (13, 8), (14, 8), (2, 8), (2, 9), (3, 10)], {1: INNER}),
]
# a cream patch wholly inside the blue (or cut off by the black outline) is a flank oval, pale cream where lit
# and cream in shade; the belly is the cream that touches its brown edge
BODY, SKIN = ["karada0*", "body*"], [2, 3, 4, 5, 6]
SPOT = "fish skin, flank spots"
MARKS = [
    dict(drawings=BODY, color=15, on=[1, 14] + SKIN, to=SPOT, max=30, min=1),
    dict(drawings=BODY, color=14, on=[1, 15] + SKIN, to=SPOT, max=16, min=2),
    dict(drawings=BODY, color=14, on=[15] + SKIN, to=SPOT, max=1, min=1),
    # single pixels of ovals that run along the outline
    dict(drawings=["karada05", "body"], color=14, on=[1, 15] + SKIN, to=SPOT, max=1, min=1),
]
# the pale blue patches on the coils and the barbels are broad painted light, not glints: left out of the row
# they stayed pale on a body gone dark
KEEP_TOP = ["fish skin", "fish skin, barbels"]
