SOURCE = "sources/black2-white2/0437-bronzong.spu"
# Bronzong, the "Bronze Bell Pokemon": one cast bronze bell, dug up after 2,000 years in the ground.
# Everything teal is the same weathered bronze (Old bronze 0.6 / -1: a broad dull reflection of the
# place, not a mirror). The art paints it as flat fields of lighter and darker patina, so the darker
# fields are their own row with the same dials: light reads them as color, not as dents.
MAIN, DARK, RING, EYE = "old bronze", "old bronze, dark bands", "old bronze, pale ring", "eye (line art)"
INNER = "seams and wrinkles"
MATERIALS = [
    # black, and the dark teal pixels that soften the ends of the arms' outline steps
    dict(name="outline", shades=[15, 6, 5], finish=0.1, body=0),
    # crown, handle, the bell's light bands, the light bands of the arms; the whole plain back.
    # The palest teal (2) is a few painted glints along the top edges (3% of the row): left out of the
    # shades so they stay as painted. Kept in, a lamp spread it over the whole crown and the face washed out.
    dict(name=MAIN, shades=[6, 5, 4, 3], base=1, finish=0.6, body=-1),
    # the darker fields: brow panels, sides and lower band, mouth, the arms' dark bands and stripes;
    # from behind the belt, its medallion and the scalloped skirt. Pattern lines are its dark shades.
    # Its 24 pixels of 4 (light on top of the arms' dark bands) are glints too, and stay as painted:
    # with 4 as a shade the brow panels lit up as pale as the bands around them and the face vanished.
    dict(name=DARK, shades=[13, 6, 5], base=1, finish=0.6, body=-1),
    # the pale ring around the bell's shoulder, and the four pale teeth cast in the mouth
    # (base is its gray underside, which most of it is painted in; with the pale top as base the
    # whole ring faced the ground and went olive in a field)
    dict(name=RING, shades=[9, 8, 7], base=0, finish=0.6, body=-1),
    # black lines engraved inside one surface (belt, medallion, skirt, arm stripes): not creases
    dict(name=INNER, shades=[], finish=0, body=0),
    # red ring, its dull red corners, the teal center; white with pale corners when closed
    dict(name=EYE, shades=[5, 12, 11, 2, 14], finish=0.9, body=0),
]
def to(name, colors): return {c: name for c in colors}
COLORS = {15: "outline", **to(MAIN, [2, 3, 4, 5, 6]), 13: DARK, **to(RING, [7, 8, 9]), **to(EYE, [11, 12, 14])}
RULES = [
    # ---- front body: below the ring's shadow every dark teal is a darker field or a pattern line
    dict(view="front", drawings=["body"], rect=[0, 32, 48, 32], colors=to(DARK, [5, 6])),
    dict(view="front", drawings=["body"], rect=[12, 48, 2, 3], colors={5: EYE}),
    dict(view="front", drawings=["body"], rect=[29, 48, 2, 3], colors={5: EYE}),
    dict(drawings=["body-eyes-*"], colors=to(DARK, [5, 6])),
    dict(drawings=["body-eyes-*"], rect=[6, 7, 2, 3], colors={5: EYE}),
    dict(drawings=["body-eyes-*"], rect=[23, 7, 2, 3], colors={5: EYE}),
    dict(drawings=["body-eyes-closed"], colors={2: EYE}),
    # ---- back body: belt, medallion and skirt are the dark row; their black lines are engraved
    dict(view="back", drawings=["body"], rect=[0, 32, 48, 32], colors={6: DARK}),
    dict(view="back", drawings=["body"], rect=[40, 46, 4, 8], colors={5: DARK}),    # light on the skirt's right edge
    dict(view="back", drawings=["body"], rect=[38, 34, 2, 3], colors={5: DARK}),    # light on the belt's right end
    dict(view="back", drawings=["body"], rect=[40, 36, 1, 3], colors={6: MAIN}),    # the body's own soft contour
    dict(view="back", drawings=["body"], interior={15: ([4, 5, 6, 13], INNER)}),
    # the handle is a separate piece standing on the bell, and the ring overlaps it: creases
    dict(view="back", drawings=["body"], rect=[0, 0, 48, 32], colors={15: "outline"}),
    # ---- arms, front. From the tip: dark band, light band, a dark stripe, the light root
    dict(view="front", drawings=["hnd-r"], rect=[3, 9, 9, 12], colors=to(DARK, [4, 5, 6])),
    dict(view="front", drawings=["hnd-r"], rect=[11, 20, 1, 1], colors={4: MAIN}),
    dict(view="front", drawings=["hnd-r"], rect=[24, 8, 5, 10], colors=to(DARK, [4, 5, 6])),
    dict(view="front", drawings=["hnd-r"], rect=[24, 18, 1, 1], colors={5: "outline"}),
    dict(view="front", drawings=["hnd-r"], rect=[20, 19, 1, 1], colors={5: "outline"}),
    dict(view="front", drawings=["hnd-r"], rect=[17, 20, 1, 1], colors={5: "outline"}),
    dict(view="front", drawings=["hand-l"], rect=[9, 9, 5, 8], colors=to(DARK, [4, 5, 6])),
    dict(view="front", drawings=["hand-l"], rect=[26, 9, 10, 12], colors=to(DARK, [4, 5, 6])),
    dict(view="front", drawings=["hand-l"], rect=[26, 20, 1, 1], colors={4: MAIN}),
    dict(view="front", drawings=["hand-l"], rect=[20, 20, 1, 1], colors={6: "outline"}),
    # ---- arms, back: painted a step darker; the pale line along the top edge is the light band's
    dict(view="back", drawings=["hand-l"], rect=[3, 9, 10, 12], colors={6: DARK}),
    dict(view="back", drawings=["hand-l"], rect=[3, 9, 9, 12], colors={5: DARK}),
    dict(view="back", drawings=["hand-l"], rect=[24, 9, 5, 9], colors={6: DARK}),
    dict(view="back", drawings=["hand-l"], rect=[24, 18, 1, 1], colors={6: "outline"}),
    dict(view="back", drawings=["hand-l"], rect=[20, 19, 1, 1], colors={6: "outline"}),
    dict(view="back", drawings=["hand-l"], rect=[17, 20, 1, 1], colors={6: "outline"}),
    dict(view="back", drawings=["hand-r"], rect=[9, 9, 5, 8], colors=to(DARK, [5, 6])),
    dict(view="back", drawings=["hand-r"], rect=[25, 9, 11, 12], colors=to(DARK, [5, 6])),
    dict(view="back", drawings=["hand-r"], rect=[25, 20, 1, 1], colors={5: MAIN}),
    dict(view="back", drawings=["hand-r"], rect=[20, 20, 1, 1], colors={6: "outline"}),
    # the black line down the middle of each stripe
    dict(view="back", drawings=["hand-*"], interior={15: ([4, 5, 6], INNER)}),
]
