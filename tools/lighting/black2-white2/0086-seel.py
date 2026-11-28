SOURCE = "sources/black2-white2/0086-seel.spu"
# Seel: a sleek pale coat all over (head, body, flippers, tail), a cream muzzle, a hard fur-colored horn,
# two white tusks, a pink tongue. The painted art shades all of it softly with no highlight: matte.
MATERIALS = [
    dict(name="outline", shades=[14], finish=0.1, body=0),          # black line, the nose, the closed eyelids
    # the coat: its slate contour (4) is its darkest shade; most of it is painted in 2
    dict(name="short fur", shades=[4, 3, 2, 1], base=2, finish=-0.2, body=0.05),
    # the cream muzzle and lower jaw: the same coat, another color
    dict(name="short fur, muzzle", shades=[8, 7, 6, 5], base=2, finish=-0.2, body=0.05),
    # the horn on the forehead: hard, the coat's own color
    dict(name="spines, horn", shades=[4, 3, 2, 1], base=3, finish=0.4, body=0),
    # the tusks: white, shaded with the coat's pale blues, a slate contour
    dict(name="claws and teeth", shades=[4, 3, 2, 15], base=3, finish=0.7, body=0.05),
    # the tongue hangs out, broad and flat. Not the standard wet Mouth (0.8): the art paints it flat pink
    # with no highlight, and at 0.8 so big a tongue went dark maroon under the studio lamp.
    dict(name="hide, tongue", shades=[11, 10, 9], base=2, finish=0.25, body=0.08),
    # the dark inside of the mouth, behind the tongue
    dict(name="mouth", shades=[11], base=0, finish=0.8, body=0),
    dict(name="eye (line art)", shades=[14, 4, 15], finish=0.9, body=0),
]
def to(name, colors): return {c: name for c in colors}
COLORS = {14: "outline", **to("short fur", [4, 3, 2, 1]), **to("short fur, muzzle", [8, 7, 6, 5]),
          **to("hide, tongue", [11, 10, 9]), 15: "claws and teeth"}
EYE = to("eye (line art)", [14, 4, 15])
HORN = to("spines, horn", [4, 3, 2, 1])
TUSK = to("claws and teeth", [4, 3, 2, 15])
RULES = [
    # the horn, above the dome of the head
    dict(view="front", drawings=["atama"], rect=[11, 1, 5, 5], colors=HORN),
    dict(view="front", drawings=["atama"], rect=[12, 6, 4, 1], colors=HORN),
    dict(view="back", drawings=["head"], rect=[15, 2, 5, 5], colors=HORN),
    dict(view="back", drawings=["head"], rect=[16, 7, 3, 1], colors=HORN),
    # the eyes: black, a white catchlight, a slate reflection and rim
    dict(view="front", drawings=["atama-eyes-open"], rect=[2, 3, 3, 4], colors=EYE),
    dict(view="front", drawings=["atama-eyes-open"], rect=[11, 4, 4, 4], colors=EYE),
    dict(view="back", drawings=["head"], rect=[24, 13, 1, 4], colors=EYE),
    dict(view="back", drawings=["head-eyes-open"], rect=[2, 2, 1, 4], colors=EYE),
    # the dark of the open mouth between the muzzle and the tongue
    dict(view="front", drawings=["kuti02"], colors={11: "mouth"}),
    # the tusks, hanging from the muzzle
    dict(view="front", drawings=["kuti02"], rect=[2, 6, 4, 5], colors=TUSK),
    dict(view="front", drawings=["kuti02"], rect=[14, 7, 4, 6], colors=TUSK),
    dict(view="back", drawings=["mouth"], colors=TUSK),
]
