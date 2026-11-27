# Psyduck: a duck in flat yellow down, a broad cream bill, bare cream webbed feet, three black hairs on its head.
# Colors: 15 black; 14 13 12 11 the yellows (14 their brown contour); 4 3 2 1 the creams of bill and feet (4 their
# brown contour; 3 is also the ring drawn round each eye); 5 the eyes' white; 7 the gray lit side of the hairs.
SOURCE = "sources/black2-white2/0054-psyduck.spu"
MATERIALS = [
    # black, and three stray brown pixels (4) on the edge of a back-view arm
    dict(name="outline", shades=[15, 4], finish=0.1, body=0),
    # the yellow body, head, arms and tail: down, painted flat with soft shading and no highlight. Both views
    # together are mostly painted in 13 (the back wholly)
    dict(name="feathers", shades=[14, 13, 12], base=1, finish=-0.2, body=0.05),
    # the palest yellow (11): the soft lit patch on the top of the head, the same down at its most lit. In its own
    # row so it goes dark with the head; left as a painted glint it stayed pale on a head in shade, and kept in
    # the main row it speckled the belly in a field
    dict(name="feathers, lit patches", shades=[14, 13, 12, 11], base=1, finish=-0.2, body=0.05),
    # the bill: smooth horn, cream with a soft lighter top
    dict(name="beak", shades=[4, 3, 2, 1], base=3, finish=0.4, body=0.05),
    # the webbed feet: bare skin, painted flat. From behind their contour is partly drawn in the body's brown (14)
    dict(name="dry hide, feet", shades=[4, 14, 3, 1], base=2, finish=0.05, body=0.03),
    # the three hairs: single stiff black strands with a gray lit side, painted flat
    dict(name="whiskers, head hairs", shades=[15, 7], base=0, finish=0.1, body=0.05),
    # white, pupil, the tan ring round each eye, and the brown ends of the closed lids
    dict(name="eye (line art)", shades=[15, 4, 3, 5], finish=0.9, body=0),
]
def to(name, colors): return {c: name for c in colors}
BEAK, FEET, HAIR, EYE = "beak", "dry hide, feet", "whiskers, head hairs", "eye (line art)"
COLORS = {15: "outline", **to("feathers", [14, 13, 12]), 11: "feathers, lit patches", **to(BEAK, [4, 3, 2, 1]), 5: EYE, 7: HAIR}
RULES = [
    dict(drawings=["foot*", "?-foot01"], colors=to(FEET, [4, 14, 3, 1])),
    dict(view="back", drawings=["r-arm01"], colors={4: "outline"}),
    # the hairs, where they stand above the head and where their roots lie on it
    dict(view="front", drawings=["head2"], rect=[18, 0, 9, 8], colors=to(HAIR, [15, 7])),
    dict(view="front", drawings=["head2-2"], rect=[14, 0, 12, 9], colors=to(HAIR, [15, 7])),
    dict(view="back", drawings=["head01"], rect=[7, 4, 7, 7], colors=to(HAIR, [15, 7])),
    # eye-ring pixels drawn on the head itself, under and beside the eye pictures
    dict(view="front", drawings=["head2"], rect=[5, 15, 4, 2], colors={3: EYE}),
    dict(view="front", drawings=["head2-2"], rect=[23, 16, 1, 2], colors={3: EYE}),
    # eyes open, first head: the rings; the bill's own shade under them; the two pupils
    dict(drawings=["head2-eyes-open"], colors={3: EYE}),
    dict(drawings=["head2-eyes-open"], rect=[5, 7, 5, 1], colors={3: BEAK}),
    dict(drawings=["head2-eyes-open"], rect=[1, 2, 6, 4], colors={15: EYE}),
    dict(drawings=["head2-eyes-open"], rect=[11, 2, 9, 5], colors={15: EYE}),
    # eyes closed, first head: one brown pixel at the end of the right lid
    dict(drawings=["head2-eyes-closed"], rect=[12, 4, 8, 3], colors={4: EYE}),
    # second head (tilted): the same
    dict(drawings=["head2-2-eyes-*"], colors={3: EYE}),
    dict(drawings=["head2-2-eyes-*"], rect=[12, 12, 12, 2], colors={3: BEAK}),
    dict(drawings=["head2-2-eyes-open"], rect=[6, 10, 6, 3], colors={15: EYE}),
    dict(drawings=["head2-2-eyes-open"], rect=[16, 6, 8, 5], colors={15: EYE}),
    dict(drawings=["head2-2-eyes-closed"], rect=[16, 8, 8, 2], colors={4: EYE}),
    dict(drawings=["head2-2-eyes-closed"], rect=[6, 12, 2, 2], colors={4: EYE}),
]
