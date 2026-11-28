SOURCE = "sources/black2-white2/0131-lapras.spu"
# Lapras: smooth blue skin with darker spots, a cream underside (throat, chest, the underside of every
# flipper), a small skin-colored horn, and a knobby gray shell on its back.
# Palette: 1 black; 2 3 5 6 the blue skin (6 is its contour and the spots); 4 a gray-green that softens the
# line where blue meets cream; 7 8 cream, 10 its brown contour; 11 13 14 the shell's grays; 12 white (the
# shell's knob tips and the eye whites); 15 the brown iris. The unused first color is a pink, so no white
# takes it as a shade.
SKIN = dict(finish=0.5, body=0.08)        # smooth aquatic skin: Turtle skin's dials (as Golduck)
BLUE = [6, 5, 3]
MATERIALS = [
    dict(name="outline", shades=[1, 4], finish=0.1, body=0),
    # head, ears, neck, body, flippers: the dark blue contour is its darkest shade; both views are mostly 5
    dict(name="aquatic skin", shades=BLUE, base=1, **SKIN),
    # the palest blue (2, under 5%): broad soft patches on the head, ear curls and flippers, the same skin at
    # its most lit. In their own row so they go dark with the body instead of staying pale as painted glints
    dict(name="aquatic skin, lit patches", shades=BLUE + [2], base=1, **SKIN),
    # the darker spots on the cheek, neck and flank: pigment, painted in one color, so light only tints them
    dict(name="aquatic skin, spots", shades=[6], base=0, **SKIN),
    # throat, chest and the underside of the flippers: the same skin, painted flat with no pale patch
    dict(name="aquatic skin, underside", shades=[10, 8, 7], base=1, finish=0.2, body=0.08),
    # the small horn on the forehead: hard, the skin's own color
    dict(name="spines, horn", shades=BLUE, base=1, finish=0.4, body=0),
    # the shell: dull and rough. Its slate lines (11) are its darkest shade; the black lines around the knobs
    # stay outline, since each knob stands out from the dome
    dict(name="hard shell", shades=[11, 14, 13], base=1, finish=0.2, body=0),
    # the few white pixels on the knob tips: the same shell at its most lit, in their own row so they darken
    # with the shell
    dict(name="hard shell, knob tips", shades=[11, 14, 13, 12], base=1, finish=0.2, body=0),
    dict(name="eye (line art)", shades=[1, 15, 13, 12], finish=0.9, body=0),
]
def to(name, colors): return {c: name for c in colors}
SPOT, HORN, EYE = "aquatic skin, spots", "spines, horn", "eye (line art)"
COLORS = {1: "outline", 4: "outline", **to("aquatic skin", BLUE), 2: "aquatic skin, lit patches",
          **to("aquatic skin, underside", [10, 8, 7]), **to("hard shell", [11, 14, 13]), 12: "hard shell, knob tips"}
RULES = [
    # the horn, front view: everything above the black line across the forehead
    dict(view="front", drawings=["atama"], rect=[8, 6, 9, 4], colors=to(HORN, BLUE)),
    dict(view="front", drawings=["atama"], rect=[8, 10, 5, 1], colors=to(HORN, BLUE)),
    dict(view="front", drawings=["atama"], rect=[8, 11, 3, 1], colors=to(HORN, BLUE)),
    dict(view="front", drawings=["atama"], rect=[8, 12, 2, 1], colors=to(HORN, BLUE)),
    # the horn, back view: the bump on the far side of the head, above the eye
    dict(view="back", drawings=["head"], rect=[25, 8, 5, 2], colors=to(HORN, BLUE)),
    dict(view="back", drawings=["head"], rect=[26, 10, 4, 1], colors=to(HORN, BLUE)),
    dict(view="back", drawings=["head"], rect=[27, 11, 2, 2], colors=to(HORN, BLUE)),
    # the eyes: white, brown iris, the gray of the far eye's white, and the pupil
    dict(drawings=["atama", "atama-eyes-open", "head-eyes-open"], colors=to(EYE, [12, 13, 15])),
    dict(view="front", drawings=["atama"], rect=[16, 20, 1, 1], colors={1: EYE}),
    dict(view="front", drawings=["atama-eyes-open"], rect=[8, 5, 1, 1], colors={1: EYE}),
    # the cheek spot where the eye's own drawings repeat it (cut by their edge), and the flank spots at the
    # edge of the body's drawing
    dict(view="front", drawings=["atama-eyes-*"], rect=[13, 4, 3, 3], colors={6: SPOT}),
    dict(view="front", drawings=["koura"], rect=[9, 24, 4, 2], colors={6: SPOT}),
]
MARKS = [
    # a patch of the dark blue wholly inside the skin is a spot (the ears' curl lines are not)
    dict(drawings=["atama", "kubi", "head", "neck", "body"], color=6, on=[5, 3], to=SPOT, max=16, min=2),
]
