SOURCE = "sources/black2-white2/0028-sandslash.spu"
MATERIALS = [
    # black, the dark brown soft outline (14), the claws' dark gray edge (10); in the quill drawings also the thin
    # olive edge line (5), and on the body the brown line where the hide meets the quills (13, 12)
    dict(name="outline", shades=[15, 14, 10, 5, 13, 12], finish=0.1, body=0),
    # the palette's lightest yellow (1) is never drawn: it is the hide's own lighter step
    dict(name="plated hide", shades=[5, 4, 3, 2, 1], base=2, finish=0.2, body=0.03),
    # the cream stomach, muzzle and cheek: as dry and matte as the hide, but soft skin
    dict(name="dry hide, belly", shades=[9, 8, 7, 6], base=2, finish=0.05, body=0.08),
    dict(name="spines", shades=[13, 12, 11], base=0, finish=0.4, body=0),
    # white claws; in shade the art paints them cream (7, 8) and gray (9)
    dict(name="claws and teeth", shades=[9, 8, 7, 6], base=3, finish=0.7, body=0.05),
    dict(name="eye (line art)", shades=[9, 7, 6], finish=0.9, body=0),
]
def to(name, colors): return {c: name for c in colors}
COLORS = {**to("outline", [15, 14, 10]), **to("plated hide", [5, 4, 3, 2]), **to("dry hide, belly", [9, 8, 7, 6]),
          **to("spines", [13, 12, 11])}
CLAWS = to("claws and teeth", [9, 8, 7, 6])
EYE = to("eye (line art)", [9, 7, 6])
RULES = [
    # limbs: every white, cream and gray pixel on an arm or a leg is a claw
    dict(drawings=["karada-2", "te02", "asi01", "asi02", "ude", "asi2", "asi1", "asi1-*"], colors=CLAWS),
    # quills overlap: the thin olive line along a quill's edge is a line like the black beside it
    dict(drawings=["hari*"], colors={5: "outline"}),
    # the body's edge against the quills behind it is drawn in the quills' brown: a line, not a quill
    dict(view="front", drawings=["karada"], colors={13: "outline", 12: "outline"}),
    # eyes (front): the right eye's white, its gray and its cream corner; the left eye's one white pixel
    dict(view="front", drawings=["atama"], rect=[17, 19, 4, 4], colors=EYE),
    dict(view="front", drawings=["atama"], rect=[9, 20, 2, 2], colors=EYE),
    dict(view="front", drawings=["atama-eyes-open"], rect=[9, 3, 4, 4], colors=EYE),
    dict(view="front", drawings=["atama-eyes-open"], rect=[1, 4, 2, 2], colors=EYE),
    # eye (back): one cream pixel of eye white
    dict(view="back", drawings=["atama-eyes-open"], rect=[3, 1, 3, 3], colors=EYE),
]
