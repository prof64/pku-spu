# Meowth: a cat in a short cream coat with brown feet and tail tip, and a gold coin on its forehead
# (Crystal: "When it sees a shiny object, the gold coin on its head shines too"; Shield: "It washes its face
# regularly to keep the coin on its forehead spotless"). The coin is hard and dull, as the art paints it;
# everything else is a matte coat. Drawing names do not say what a drawing is (the idle reuses them across parts:
# "atama-3" is a foot, "hige02-2" a hand), so the whisker rule names its four drawings exactly.
SOURCE = "sources/black2-white2/0052-meowth.spu"
FUR = [15, 14, 13, 12]
MATERIALS = [
    # black: the line, the ears' black outsides, the lines of the tail's curl and between the toes
    dict(name="outline", shades=[8], finish=0.1, body=0),
    # the cream coat: its brown contour (15) is its darkest shade. The back view and the body are painted in 14,
    # the face in 13 with a pale patch (12) between the eyes; 14 is most of it
    dict(name="short fur", shades=FUR, base=1, finish=-0.2, body=0.05),
    # the brown hind feet and the curled tip of the tail: the same coat in another color
    dict(name="short fur, feet and tail tip", shades=[11, 10, 9], base=1, finish=-0.2, body=0.05),
    dict(name="short fur, ear insides", shades=[7, 6], base=1, finish=-0.2, body=0.05),
    # one stiff hair each: the two long ones on the head and the four on the cheeks
    dict(name="whiskers", shades=[15, 14, 13], base=2, finish=0.1, body=0.05),
    # the pink pads under a raised foot
    dict(name="hide, paw pads", shades=[7, 6], base=1, finish=0.25, body=0.08),
    # the gold coin: hard and dull, like Machamp's belt plate. The painted art draws it flat, with grooves and no
    # highlight; as real metal it mirrored the place, lime green over grass and near black in a cave. From
    # behind, its top edge is drawn in the coat's brown (15)
    dict(name="gold coin", shades=[5, 15, 4, 3], base=3, finish=0.2, body=0),
    # the white bars on its ridges, in their own row so they go dark with the coin; with white as the coin's
    # top shade a lamp spread it over the whole coin
    dict(name="gold coin, ridges", shades=[3, 1], base=1, finish=0.2, body=0),
    # the two small fangs: white, with the palette's gray as their shade
    dict(name="claws and teeth", shades=[2, 1], base=1, finish=0.7, body=0.05),
    dict(name="mouth", shades=[7, 6], base=1, finish=0.8, body=0),
    # white, its gray, the black slit pupil and the brown line the eye is drawn with (closed: the lid's line)
    dict(name="eye (line art)", shades=[8, 15, 2, 1], finish=0.9, body=0),
]
def to(name, colors): return {c: name for c in colors}
COLORS = {8: "outline", **to("short fur", FUR), **to("short fur, feet and tail tip", [11, 10, 9]),
          **to("short fur, ear insides", [7, 6]), **to("gold coin", [5, 4, 3]), **to("eye (line art)", [2, 1])}
EYE = to("eye (line art)", [8, 15, 2, 1])
LID = {15: "eye (line art)"}
WHISKER = to("whiskers", [15, 14, 13])
HEADS = ["atama", "atama-2"]
RULES = [
    # the cheek whiskers
    dict(drawings=["hige01", "hige02", "hige-l", "hige-r"], colors=WHISKER),
    # the two long whiskers standing on the head, down to where the head begins
    dict(view="front", drawings=HEADS, rect=[8, 2, 3, 10], colors=WHISKER),
    dict(view="front", drawings=HEADS, rect=[17, 3, 5, 9], colors=WHISKER),
    dict(view="back", drawings=["atama"], rect=[10, 1, 3, 4], colors=WHISKER),
    dict(view="back", drawings=["atama"], rect=[11, 5, 2, 1], colors=WHISKER),
    dict(view="back", drawings=["atama"], rect=[12, 6, 1, 3], colors=WHISKER),
    dict(view="back", drawings=["atama"], rect=[13, 9, 1, 2], colors=WHISKER),
    dict(view="back", drawings=["atama"], rect=[20, 1, 3, 4], colors=WHISKER),
    dict(view="back", drawings=["atama"], rect=[19, 5, 2, 3], colors=WHISKER),
    # the coin's white bars; from behind, its top showing over the head and its brown edge
    dict(view="front", drawings=HEADS, rect=[10, 7, 7, 10], colors={1: "gold coin, ridges"}),
    dict(view="back", drawings=["atama"], rect=[14, 6, 5, 3], colors={1: "gold coin, ridges", 15: "gold coin"}),
    dict(view="back", drawings=["atama"], rect=[19, 8, 1, 1], colors={15: "gold coin"}),
    # the eyes, on the head and on the strips that lie over it
    dict(view="front", drawings=HEADS, rect=[7, 17, 4, 5], colors=EYE),
    dict(view="front", drawings=HEADS, rect=[16, 17, 7, 6], colors=EYE),
    dict(drawings=["atama*-eyes-open"], rect=[7, 1, 4, 5], colors=EYE),
    dict(drawings=["atama*-eyes-open"], rect=[16, 1, 7, 6], colors=EYE),
    dict(drawings=["atama*-eyes-closed"], rect=[6, 4, 4, 3], colors=LID),
    dict(drawings=["atama*-eyes-closed"], rect=[17, 4, 6, 3], colors=LID),
    # the mouth: its pink inside, and a fang at each corner
    dict(view="front", drawings=HEADS, rect=[10, 24, 9, 5], colors={**to("mouth", [7, 6]), 1: "claws and teeth"}),
    # the pads under the raised foot
    dict(drawings=["asi-3", "image-14"], colors={6: "hide, paw pads", 7: "hide, paw pads"}),
]
# the pale patch between the eyes is the face's lit shade, not a glint
KEEP_TOP = ["short fur"]
