# Golbat: bare skin all over (Hide), thin purple wing membrane on blue arms, four fangs, a huge open mouth.
SOURCE = "sources/black2-white2/0042-golbat.spu"
BLUE, PURPLE = [8, 7, 6, 5], [11, 10, 9]
MATERIALS = [
    # black, and the darkest purple, which the wings use only for lines one pixel wide: the finger bones under the
    # membrane and its drawn edge. The wing is panels of skin stretched between the fingers, so they are creases.
    # Left in the membrane row they lit up brighter than the membrane itself in the cave.
    dict(name="outline", shades=[4, 12], finish=0.1, body=0),
    # body, ears, feet, and the wing's arm along the membrane's leading edge
    dict(name="hide", shades=BLUE, base=1, finish=0.25, body=0.08),
    dict(name="hide, ear insides", shades=[12, 9], base=0, finish=0.25, body=0.08),
    dict(name="wing membrane", shades=PURPLE, base=1, finish=0.3, body=0.3),
    # fangs: white, a light gray, and the dark gray the art draws their shaded edge in
    dict(name="claws and teeth", shades=[3, 2, 1], base=2, finish=0.7, body=0.05),
    # the gray tongue in the black mouth (front view only)
    dict(name="mouth", shades=[3], base=0, finish=0.8, body=0),
    # the dark inside of the open mouth, drawn black: part of the mouth, only tinted by light
    dict(name="mouth, dark inside", shades=[], finish=0.8, body=0),
    # whites, their grays and the black slit pupils
    dict(name="eye (line art)", shades=[4, 3, 2, 1], finish=0.9, body=0),
]
def to(name, colors): return {c: name for c in colors}
COLORS = {4: "outline", 12: "outline", **to("hide", BLUE), **to("wing membrane", PURPLE), **to("claws and teeth", [3, 2, 1])}
EYE = to("eye (line art)", [4, 3, 2, 1])
RULES = [
    dict(view="front", drawings=["body", "body-female"], colors=to("hide, ear insides", [12, 9])),
    # the eyes, painted on the head and again on the blink overlay
    dict(view="front", drawings=["body", "body-female"], rect=[3, 12, 3, 2], colors=EYE),
    dict(view="front", drawings=["body", "body-female"], rect=[13, 12, 3, 2], colors=EYE),
    dict(view="front", drawings=["body-eyes-open", "body-female-eyes-open"], rect=[1, 3, 3, 2], colors=EYE),
    dict(view="front", drawings=["body-eyes-open", "body-female-eyes-open"], rect=[11, 3, 3, 2], colors=EYE),
    # shut, the eye keeps the gray pixel at its outer corner
    dict(view="front", drawings=["body-eyes-closed", "body-female-eyes-closed"], rect=[1, 3, 1, 1], colors=EYE),
    # the tongue
    dict(view="front", drawings=["mouse", "mouse-female"], rect=[5, 14, 5, 10], colors={3: "mouth"}),
]
FLOODS = [
    # the black that fills the open mouth, from a pixel inside it
    dict(view="front", drawing="mouse", seeds=[[8, 8]], through=[4], colors={4: "mouth, dark inside"}),
    dict(view="front", drawing="mouse-female", seeds=[[8, 8]], through=[4], colors={4: "mouth, dark inside"}),
]
# the palest blue is the lit brow between the ears and the top of the wing arms: shading, not a glint
KEEP_TOP = ["hide"]
