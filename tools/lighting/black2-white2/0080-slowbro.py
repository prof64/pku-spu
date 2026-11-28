# Slowbro: the same plain bare skin as Slowpoke, a ribbed cream belly, and a Shellder biting its tail:
# "The SHELLDER that is latched onto SLOWPOKE's tail" (Red/Blue); "Shellder ... has metamorphosed into a
# spiral-shaped shell" (Ultra Moon). The official art paints skin, belly and shell flat, with no highlight.
SOURCE = "sources/black2-white2/0080-slowbro.spu"
# Palette: 1 white (claws, teeth, eye whites); 2 3 4 5 cream (muzzle and belly); 6 the white's pale gray;
# 7 8 9 the shell's grays (9 is also the back view's claw contour and one pupil); 10 the tongue;
# 11 12 13 14 the pink skin (14 is also the dark inside of both mouths); 15 black.
PINK = [14, 13, 12, 11]
CREAM = [5, 4, 3, 2]
SHELL = [9, 8, 7]
MATERIALS = [
    dict(name="outline", shades=[15], finish=0.1, body=0),
    # the body, arms, legs and tail: the maroon contour is its darkest shade; nearly all of it is painted in 13
    dict(name="hide", shades=PINK, base=1, finish=0.25, body=0.08),
    # the cream muzzle: the same skin, paler
    dict(name="hide, muzzle", shades=CREAM, base=2, finish=0.25, body=0.08),
    # the cream belly; its ribs are drawn a step darker than the skin around them and stay its own shades
    # (grooves in it, not lines on it)
    dict(name="hide, belly", shades=[5, 4, 3], base=2, finish=0.25, body=0.08),
    # the Shellder: a spiral shell with spikes. The black lines between its whorls stay outline: each whorl
    # bulges on its own
    dict(name="hard shell", shades=SHELL, base=1, finish=0.2, body=0),
    # the darker blotches on the shell, drawn one step darker than the shell around them
    dict(name="hard shell, spots", shades=[9, 8], base=0, finish=0.2, body=0),
    # Slowbro's claws and teeth and the Shellder's teeth; the back view draws the claws' contour in dark gray
    dict(name="claws and teeth", shades=[9, 6, 1], base=2, finish=0.7, body=0.05),
    # Slowbro's open mouth: dark inside, the orange tongue
    dict(name="mouth", shades=[14, 10], base=0, finish=0.8, body=0),
    # the dark inside of the Shellder's mouth around the tail: only tinted by light
    dict(name="mouth, dark inside", shades=[], finish=0.8, body=0),
    dict(name="eye (line art)", shades=[15, 9, 6, 1], finish=0.9, body=0),
]
def to(name, colors): return {c: name for c in colors}
COLORS = {15: "outline", **to("hide", PINK), **to("hide, belly", CREAM), **to("hard shell", SHELL),
          **to("claws and teeth", [6, 1]), 10: "mouth"}
EYE = to("eye (line art)", [15, 9, 6, 1])
RULES = [
    # the head: its cream is the muzzle
    dict(drawings=["atama", "atama-eyes-*", "head", "head-eyes-*"], colors=to("hide, muzzle", CREAM)),
    # the open mouth (front view): its dark inside shares the skin's contour color
    dict(view="front", drawings=["atama"], rect=[7, 20, 13, 7], colors={14: "mouth"}),
    # Slowbro's eyes: whites, their gray edge, one dark gray and one black pupil
    dict(drawings=["atama-eyes-open"], colors=to("eye (line art)", [9, 6, 1])),
    dict(drawings=["atama-eyes-open"], rect=[16, 7, 1, 1], colors=EYE),
    dict(view="back", drawings=["head"], rect=[24, 12, 2, 4], colors=EYE),
    dict(drawings=["head-eyes-open"], rect=[2, 2, 2, 4], colors=EYE),
    # the back view draws the claws' contour in the shell's dark gray
    dict(view="back", drawings=["hand-r", "foot-r"], colors={9: "claws and teeth"}),
    # the Shellder's eye (its other whites are teeth) and the pupil between the whites
    dict(view="front", drawings=["o1"], rect=[21, 25, 6, 3], colors={1: "eye (line art)"}),
    dict(view="front", drawings=["o1"], rect=[23, 26, 1, 1], colors=EYE),
    dict(drawings=["o1-eyes-open"], colors={1: "eye (line art)"}),
    dict(drawings=["o1-eyes-open"], rect=[7, 5, 1, 1], colors=EYE),
    # the inside of the Shellder's mouth, between its teeth and beside the tail
    dict(view="front", drawings=["o1"], rect=[20, 31, 10, 6], colors={14: "mouth, dark inside"}),
]
MARKS = [
    # the shell's blotches: a darker patch wholly inside the lighter shell (four pixels and up: the shorter
    # dark strokes are ribs of the whorls, and stay the shell's own shade)
    dict(drawings=["o1", "shell"], color=9, on=[8], to="hard shell, spots", max=30, min=4),
    dict(drawings=["o1", "shell"], color=8, on=[7], to="hard shell, spots", max=6, min=2),
]
# The palest pink is few of the skin's pixels overall but three broad soft patches (forehead and both knees):
# a shade, not a glint. Left out of the row they stayed as gray blots under the studio lamp and in the cave.
KEEP_TOP = ["hide"]
