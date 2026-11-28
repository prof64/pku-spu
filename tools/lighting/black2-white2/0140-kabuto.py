SOURCE = "sources/black2-white2/0140-kabuto.spu"
# Palette: 1 black (the line, and the whole soft body under the shell); 2 3 4 5 6 the brown shell, light to dark;
# 8 9 10 the yellow legs (10 their dark contour, back view); 11 white (the catchlight of the small eyes on the
# shell); 12 the navy the art paints low on the black body; 14 15 the red eyes. 7 and 13 are not used.
SHELL = [6, 5, 4, 3, 2]
MATERIALS = [
    dict(name="outline", shades=[1], finish=0.1, body=0),
    # the dome: "It is protected by a stiff shell." The art paints it flat brown with one soft broad paler wash
    # on top and no highlight: dull. Cloyster's row.
    dict(name="hard shell", shades=SHELL, base=2, finish=0.2, body=0),
    # the soft body under the shell: painted flat black with a navy wash low on it, so light only tints it
    # (as a shade, the navy broke out in specks beside the eyes under a lamp). Shellder's row.
    dict(name="hide, black body", shades=[], finish=0.25, body=0.08),
    # the four legs: jointed shell ending in a point, painted flat yellow with soft shading. Kingler's row.
    dict(name="hard shell, legs", shades=[10, 9, 8], base=1, finish=0.2, body=0),
    dict(name="eye (line art)", shades=[1, 6, 11, 14, 15], finish=0.9, body=0),
]
def to(name, colors): return {c: name for c in colors}
EYE = to("eye (line art)", [14, 15])
DOT = to("eye (line art)", [1, 6, 11])
COLORS = {1: "outline", **to("hard shell", SHELL), **to("hard shell, legs", [10, 9, 8]), 12: "hide, black body", **EYE}
RULES = [
    # front: the broad black is the body; one-pixel strokes of it stay the line
    dict(view="front", drawings=["body"], colors={1: "hide, black body"}, thin_all={1: "outline"}),
    # the small black eyes on top of the shell, each with a white catchlight and a dark brown edge
    dict(view="front", drawings=["body"], rect=[18, 2, 3, 2], colors=DOT),
    dict(view="back", drawings=["body"], rect=[17, 3, 2, 2], colors=DOT),
    dict(view="back", drawings=["body"], rect=[27, 5, 2, 2], colors=DOT),
    # one black pixel beside the navy is body, not a stroke of the line
    dict(view="front", drawings=["body"], rect=[23, 27, 1, 1], colors={1: "hide, black body"}),
]
KEEP_TOP = ["hard shell"]
GLOW = [
    dict(material="eye (line art)", colors=[15], glow=80, intent="the red eyes glow: their hot middle"),
    dict(material="eye (line art)", colors=[14], glow=30, intent="the red eyes' paler ring glows less"),
]
