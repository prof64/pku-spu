SOURCE = "sources/black2-white2/0102-exeggcute.spu"
# Six eggs. Gold: "The shell is very durable. Even if it cracks, it can survive without spilling the contents."
# FireRed: "it was discovered to be a life-form more like plant seeds." The painted art shades every egg softly,
# with one broad pale patch and no small hard highlight: a dull hard shell (Hard shell, like a turtle's), solid.
SHELL = dict(finish=0.2, body=0)
MATERIALS = [
    dict(name="outline", shades=[5, 15], finish=0.1, body=0),
    # the dark red contour (15) is in the outline row: the palette has no step between the peach and it, so as
    # the shell's darkest shade it turned the whole back view dark crimson in a field
    dict(name="shell", shades=[14, 13, 12, 11], base=0, **SHELL),
    # the contents showing in the cracked egg: painted flat yellow with an orange shade, no highlight
    dict(name="yolk", shades=[4, 3], base=1, finish=0.2, body=0.1),
    # one egg's open mouth, painted in the contour's dark red
    dict(name="mouth", shades=[15], base=0, finish=0.8, body=0),
    # cracks, brows, closed eyes and mouth lines: drawn inside the one shell, tinted, never a crease
    dict(name="seams and wrinkles", shades=[], finish=0, body=0),
    dict(name="eye (line art)", shades=[5, 2, 1], finish=0.9, body=0),
]
INNER = "seams and wrinkles"
def to(name, colors): return {c: name for c in colors}
COLORS = {5: "outline", 15: "outline", **to("shell", [11, 12, 13, 14]), **to("yolk", [3, 4]), **to("eye (line art)", [1, 2])}
PUPIL = {5: "eye (line art)"}
def pupils(drawing, *rects): return [dict(drawings=[drawing], rect=list(r), colors=PUPIL) for r in rects]
RULES = [
    # dark red wholly inside an egg (next to shell, eye or black only) is a crack or a face line, not the contour
    dict(interior={15: ([11, 12, 13, 14, 1, 2, 5], INNER)}),
    # the shouting egg's open mouth, and its top row on the eye drawings
    dict(drawings=["t05"], rect=[11, 13, 5, 3], colors={15: "mouth"}),
    dict(drawings=["t05-eyes-*"], rect=[6, 7, 4, 1], colors={15: "mouth"}),
    # black inside a shell: the end of a crack, the back egg's frown and its closed eyes
    dict(drawings=["t05"], rect=[15, 19, 1, 1], colors={5: INNER}),
    dict(view="back", drawings=["parts03"], rect=[6, 22, 7, 2], colors={5: INNER, 15: INNER}),
    dict(drawings=["parts03-eyes-closed"], colors={5: INNER, 15: INNER}),
    # pupils: black inside each eye
    *pupils("t01", [11, 14, 1, 2], [17, 14, 1, 2]), *pupils("t01-eyes-open", [8, 8, 1, 2], [14, 8, 1, 2]),
    *pupils("t02", [6, 9, 1, 1], [11, 10, 1, 1]), *pupils("t02-eyes-open", [4, 3, 1, 1], [9, 4, 1, 1]),
    *pupils("t04", [9, 10, 1, 2], [4, 13, 1, 1]), *pupils("t04-eyes-open", [9, 2, 1, 2], [4, 5, 1, 1]),
    *pupils("t05", [12, 8, 2, 1], [18, 11, 1, 1]), *pupils("t05-eyes-open", [7, 2, 2, 1], [13, 5, 1, 1]),
    *pupils("t06", [14, 6, 1, 1], [9, 10, 1, 1]), *pupils("t06-eyes-open", [12, 2, 1, 1], [7, 6, 1, 1]),
    *pupils("parts03-eyes-open", [4, 4, 1, 2], [10, 4, 1, 2]),
]
KEEP_TOP = ["shell"]    # the broad pale patch on each egg is its lit top: left out, it stayed pale on eggs gone dark in the cave
