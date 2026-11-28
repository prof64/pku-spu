SOURCE = "sources/black2-white2/0087-dewgong.spu"
# Dewgong: a snowy white coat all over (head, long body, flippers, tail fins), a hard horn of the coat's
# own color, two small fangs, an open red mouth (front view). The painted art shades all of it softly
# with no highlight: matte.
MATERIALS = [
    dict(name="outline", shades=[14], finish=0.1, body=0),          # black line, the nose, the closed eyelids
    # the coat: its slate contour (5) and the fin rays (4, 3) are its dark shades; most of it is painted in 2.
    # The sprite paints one white patch (15) on the forehead: a glint, which the tool leaves as painted.
    dict(name="short fur", shades=[5, 4, 3, 2, 1, 15], base=4, finish=-0.1, body=0.05),
    # the horn on the forehead: hard, the coat's own color
    dict(name="spines, horn", shades=[5, 4, 3, 2, 1], base=4, finish=0.4, body=0),
    # the fangs: white, with their own two grays
    dict(name="claws and teeth", shades=[13, 12, 15], base=2, finish=0.7, body=0.05),
    # the open mouth: dark red inside, the tongue the lighter red
    dict(name="mouth", shades=[7, 6], base=0, finish=0.8, body=0),
    dict(name="eye (line art)", shades=[14, 13, 15], finish=0.9, body=0),
]
def to(name, colors): return {c: name for c in colors}
COLORS = {14: "outline", **to("short fur", [5, 4, 3, 2, 1]), **to("mouth", [7, 6]),
          **to("claws and teeth", [13, 12, 15])}
EYE = to("eye (line art)", [14, 13, 15])
HORN = to("spines, horn", [5, 4, 3, 2, 1])
RULES = [
    # the white patch on the forehead
    dict(view="front", drawings=["atama"], rect=[12, 7, 5, 3], colors={15: "short fur"}),
    # the horn, above the dome of the head
    dict(view="front", drawings=["atama"], rect=[18, 2, 5, 5], colors=HORN),
    dict(view="back", drawings=["body01-2"], rect=[11, 1, 6, 5], colors=HORN),
    dict(view="back", drawings=["body01-2"], rect=[12, 6, 5, 1], colors=HORN),
    # the eyes: black, a white catchlight, a gray edge; closed, one gray pixel of the lid
    dict(view="front", drawings=["atama-eyes-open"], rect=[4, 3, 4, 4], colors=EYE),
    dict(view="front", drawings=["atama-eyes-open"], rect=[14, 6, 5, 5], colors=EYE),
    dict(view="front", drawings=["atama-eyes-closed"], colors={13: "eye (line art)"}),
    dict(view="back", drawings=["body01-2", "body01-2-eyes-closed"], colors={13: "eye (line art)"}),
    dict(view="back", drawings=["body01-2-eyes-open"], rect=[4, 2, 2, 5], colors=EYE),
]
# Left out of the row, the forehead patch stayed white on a head gone gray with the sun behind; kept, it
# darkens with the coat.
KEEP_TOP = ["short fur"]
