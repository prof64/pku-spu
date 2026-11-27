# Primeape: the same ball of shaggy cream fur as Mankey (Fur) with smooth cream ears (Short fur); the whole arms and
# legs are now bare brown skin over muscle (Hide, as Mankey's hands and feet), the pig snout is bare skin, and each
# wrist and ankle wears a dark metal shackle, the one part the painted art gives a highlight.
SOURCE = "sources/black2-white2/0057-primeape.spu"
F = dict(finish=-0.7, body=0.05)          # Fur: the shaggy ball
SF = dict(finish=-0.2, body=0.05)         # Short fur: the smooth-edged ears
H = dict(finish=0.25, body=0.08)          # Hide: plain bare skin
MATERIALS = [
    dict(name="outline", shades=[11], finish=0.1, body=0),
    # the round head-and-body: front and back together are mostly painted in 14. Its two contour browns (15 on the
    # lit side, 10 on the shadow side) are in the row but are NOT shades of it, as on Mankey: the palette has nothing
    # between cream and those browns, so as shades one step off the light turned the ball dark brown
    dict(name="fur", shades=[14, 13, 12], base=0, **F),
    # the ears' cream fronts, rims and backs: smooth triangles, mostly painted in 13
    dict(name="short fur, ears", shades=[14, 13, 12], base=1, **SF),
    dict(name="short fur, ear insides", shades=[6, 5], base=1, **SF),
    # arms, fists, legs and feet: bare brown skin, painted with soft broad shading and no highlight
    dict(name="hide", shades=[10, 9, 8], base=1, **H),
    # the few palest pixels (7) on top of the fists: the same skin at its most lit, in their own row so they go dark
    # with the limb (as on Machamp)
    dict(name="hide, lit patches", shades=[10, 9, 8, 7], base=1, **H),
    # the pink snout: its red rim on top and brown rim below are its shades
    dict(name="hide, snout", shades=[10, 6, 5], base=2, **H),
    # the shackles on wrists and ankles: dark, dull metal
    dict(name="metal, shackles", shades=[4, 3], base=0, finish=0.6, body=-1),
    # lines drawn on the fur in the limbs' tan and mauve (8, 9): the swollen vein on the brow, the furrows between the
    # eyes, the eyes' lower lids. A marking with the fur's dials, so it goes dark with the fur around it (as tinted
    # lines they stayed orange on a face in shade; a row with "line" in its name is taken for line art, hence "marks")
    dict(name="fur, face marks", shades=[9, 8], base=1, **F),
    # the same two colors along the ears' soft edge and around the ear insides
    dict(name="short fur, ear edges", shades=[9, 8], base=0, **SF),
    # the nostrils: lines drawn on a surface, tinted, never a crease
    dict(name="seams and wrinkles", shades=[], finish=0, body=0),
    dict(name="eye (line art)", shades=[11, 3, 2, 1], finish=0.9, body=0),
]
INNER = "seams and wrinkles"
KEEP_TOP = ["fur", "short fur, ears"]
def to(name, colors): return {c: name for c in colors}
CREAM = [15, 14, 13, 12]
COLORS = {11: "outline", **to("fur", CREAM), **to("hide", [10, 9, 8]), 7: "hide, lit patches",
          **to("metal, shackles", [4, 3]), **to("short fur, ear insides", [6, 5]), **to("eye (line art)", [1, 2])}
RULES = [
    # the ball, both views: its shadow-side contour, and the tan and mauve lines drawn on it
    dict(drawings=["atama", "atama-eyes-*", "head01"], colors={10: "fur", **to("fur, face marks", [8, 9])}),
    # the tuft of body fur drawn over the top of one leg
    dict(view="front", drawings=["asi02"], rect=[0, 6, 24, 3], colors={10: "fur"}),
    # ears, both views
    dict(drawings=["mimi*", "*-ear01"], colors={**to("short fur, ears", CREAM), **to("short fur, ear edges", [8, 9])}),
    # the snout, and its two nostrils
    dict(drawings=["hana"], colors=to("hide, snout", [10, 6, 5]), interior={6: ([5], INNER)}),
    # the eyes: white, its gray upper edge, the black pupil and the gray under it
    dict(drawings=["atama-eyes-open"], colors=to("eye (line art)", [1, 2, 3, 11])),
]
