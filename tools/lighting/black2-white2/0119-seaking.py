# Seaking: an orange-red fish with a white belly, black markings over its head and back (pigment in the same
# skin), white fins with drawn rays and black spots, a cream horn, pink lips with two small fangs. The painted art
# shades the body softly with no hard highlight, and the fins flat: matte.
SOURCE = "sources/black2-white2/0119-seaking.spu"
# Palette: 7 black; 6 dark gray (the lit side of the black markings, the fin spots, the eye); 5 4 the grays of
# contours and fin rays; 3 2 1 pale gray to white; 8 cream (the horn); 12 11 10 9 the orange-reds; 15 14 13 the
# lips. In the shiny palette 5 4 3 2 are greens.
ORANGE, FINW = [12, 11, 10, 9], [5, 4, 3, 2, 1]
MATERIALS = [
    # black; and the gray edge of the belly and of the horn (no step in between on those: as a shade it speckles)
    dict(name="outline", shades=[7, 5, 4, 6], finish=0.1, body=0),
    dict(name="fish skin", shades=ORANGE, base=1, finish=0.15, body=0.08),
    dict(name="fish skin, belly", shades=[2, 1], base=0, finish=0.15, body=0.08),
    # the black over the head and back, the stripes and spots on the side: painted black with a dark gray lit side
    dict(name="fish skin, black markings", shades=[7, 6], base=0, finish=0.15, body=0.08),
    dict(name="fish skin, lips", shades=[12, 15, 14, 13], base=2, finish=0.25, body=0.08),
    # dorsal, pectoral and tail fins: thin skin, painted flat and soft
    dict(name="fin", shades=FINW, base=3, finish=0.3, body=0.15),
    dict(name="fin, spots", shades=[], finish=0.3, body=0.15),      # flat dark gray flecks: light only tints them
    # the horn: hard and solid, cream with a white tip, painted without a highlight
    dict(name="spines, horn", shades=[8, 1], base=0, finish=0.4, body=0),
    dict(name="claws and teeth", shades=[2, 1], base=1, finish=0.7, body=0.05),      # the two fangs
    dict(name="seams and wrinkles", shades=[], finish=0, body=0),   # fin rays: lines on the one sheet, not creases
    dict(name="eye (line art)", shades=[7, 6, 2, 1], finish=0.9, body=0),
]
INNER = "seams and wrinkles"
def to(name, colors): return {c: name for c in colors}
COLORS = {7: "outline", 5: "outline", 4: "outline", **to("fish skin", ORANGE), **to("fish skin, belly", [2, 1]),
          6: "fish skin, black markings", 8: "spines, horn", **to("fish skin, lips", [15, 14, 13]), 3: "fin"}
HORN = {4: "outline", 5: "outline", **to("spines, horn", [8, 1])}
BODY = ["body", "body-female"]
FINS = ["sebire", "hand*", "tail*"]
RULES = [
    # black wholly inside the body is the marking, not line art; black along the silhouette stays the outline
    dict(drawings=BODY, interior={7: ([6, 9, 10, 11, 12], "fish skin, black markings")}),
    # the horn
    dict(view="front", drawings=BODY, rect=[2, 10, 14, 11], colors=HORN),
    dict(view="back", drawings=BODY, rect=[35, 5, 13, 8], colors=HORN),
    # the eye: white ring, black pupil, gray catchlights
    dict(view="front", drawings=BODY, rect=[19, 16, 8, 8], colors=to("eye (line art)", [7, 6, 1])),
    dict(view="back", drawings=BODY, rect=[32, 13, 7, 9], colors=to("eye (line art)", [7, 6, 2, 1])),
    # the mouth: lips with their dark red edge, the fangs, the skin around them; the open mouth is black
    dict(drawings=["mouth*"], colors={12: "fish skin, lips", 1: "claws and teeth", 6: "outline"}),
    # fins: white with gray contours; the drawn rays are lines on the sheet; the flecks
    dict(drawings=FINS, colors={**to("fin", FINW), 6: "fin, spots"}),
    dict(drawings=FINS, interior={4: ([1, 2, 3, 6], INNER)}),
]
