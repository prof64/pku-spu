SOURCE = "sources/black2-white2/0045-vileplume.spu"
# Vileplume: the blue root body under one huge five-petaled flower, red with pale spots (bigger on the female),
# and an orange cup at its center. The painted art shades all of it flat and soft: matte.
# Colors: 15 black; 14 13 12 11 the blues; 8 6 7 1 5 the petals' reds, dark to light; 10 9 the spots' pinks;
# 4 3 2 the cup's oranges. The eyes are one petal-red pixel in a dark ring.
ROOT = dict(finish=0.1, body=0.1)        # as Oddish
PETAL = dict(finish=0.2, body=0.25)
MATERIALS = [
    # black; the petals' darkest red where it is the line between two petals; the body's dark blues where they
    # draw the mouth line, the shut eyes and the dark hollow of the cup
    dict(name="outline", shades=[15, 8, 14, 13], finish=0.1, body=0),
    dict(name="plant body", shades=[14, 13, 12, 11], base=1, **ROOT),
    dict(name="petals", shades=[8, 6, 7, 1, 5], base=2, **PETAL),
    dict(name="petal spots", shades=[10, 9], base=1, **PETAL),
    # the orange cup in the middle of the flower
    dict(name="flower center", shades=[4, 3, 2], base=2, **PETAL),
    dict(name="eye (line art)", shades=[14, 7], finish=0.9, body=0),
]
def to(name, colors): return {c: name for c in colors}
COLORS = {15: "outline", **to("plant body", [14, 13, 12, 11]), **to("petals", [8, 6, 7, 1, 5]),
          **to("petal spots", [10, 9]), **to("flower center", [4, 3, 2])}
EYE = to("eye (line art)", [14, 7])
LINE = {14: "outline"}
RULES = [
    # the flower: the petals overlap, so the lines between them are creases; the blues inside the cup are its hollow
    dict(drawings=["flower1*", "parts01*"], colors={14: "outline", 13: "outline"}, thin_all={8: "outline"}),
    # the eyes, drawn on the body and again on the eye drawing: a red pixel and the dark ring around it
    dict(view="front", drawings=["body1"], rect=[20, 7, 3, 3], colors=EYE),
    dict(view="front", drawings=["body1"], rect=[10, 8, 3, 3], colors=EYE),
    dict(drawings=["body1-eyes-open"], rect=[12, 7, 3, 3], colors=EYE),
    dict(drawings=["body1-eyes-open"], rect=[2, 8, 3, 3], colors=EYE),
    # shut, they are lines; so is the smile
    dict(drawings=["body1-eyes-closed"], colors=LINE),
    dict(view="front", drawings=["body1"], rect=[14, 11, 6, 2], colors=LINE),
]
