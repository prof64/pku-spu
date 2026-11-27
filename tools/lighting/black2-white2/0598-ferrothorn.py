SOURCE = "sources/black2-white2/0598-ferrothorn.spu"
# Ferrothorn: a dull gray pod ringed by two black bands, steel spikes on its rim, its face and the
# three feeler discs, and green plant parts (the feelers, the discs' undersides, the thorn on its
# head, the patches its eyes sit in). Only the spikes are metal: the Pokedex calls them steel and the
# painted art gives each a hard white edge, while it paints the pod in flat soft grays.
BODY, BANDS, SPIKES, PLANT, EYE = "hard shell, pod", "hard shell, bands and pits", "metal, spikes", "plant body", "eye (line art)"
MATERIALS = [
    dict(name="outline", shades=[1, 5], finish=0.1, body=0),
    dict(name=BODY, shades=[5, 4, 3, 2], base=2, finish=0.2, body=0),
    dict(name=BANDS, shades=[6, 5, 12], base=1, finish=0.2, body=0),
    dict(name=SPIKES, shades=[5, 4, 3, 2], base=2, finish=0.9, body=-1),
    dict(name=PLANT, shades=[8, 9, 7], base=1, finish=0.1, body=0.25),
    dict(name=EYE, shades=[1, 5, 11, 10], finish=0.9, body=0),
]
def to(name, colors): return {c: name for c in colors}
GRAY = [2, 3, 4, 5]
# white (15) is four glint pixels painted on the body: they stay as painted
COLORS = {1: "outline", **to(BODY, GRAY + [15]), **to(BANDS, [6, 12]), **to(PLANT, [7, 8, 9]), **to(EYE, [10, 11])}

def rects(view, drawing, rs, colors):
    return [dict(view=view, drawings=[drawing], rect=r, colors=colors) for r in rs]

RULES = [
    # the feeler discs: a crown of steel spikes on a green cup
    dict(drawings=["te0*"], colors=to(SPIKES, GRAY)),
    # the dark pixels where a feeler meets the body
    dict(drawings=["turu*"], colors={5: "outline"}),
    # the body's spikes, front: rim spikes clockwise from the top left, then the one on the face
    *rects("front", "karada-a", [
        [11, 5, 6, 3], [12, 8, 3, 1],                 # top left
        [5, 14, 9, 3], [8, 17, 4, 1],                 # left
        [6, 18, 4, 1], [6, 19, 2, 1], [7, 20, 2, 1],  # lower left, small
        [9, 24, 4, 3],                                # bottom left
        [15, 27, 1, 3], [16, 28, 2, 1],               # bottom, small
        [24, 31, 5, 4],                               # bottom, large
        [32, 31, 3, 1],                               # bottom, in shadow
        [39, 29, 3, 4],                               # bottom right
        [44, 25, 4, 3],                               # lower right
        [44, 11, 6, 3], [46, 14, 2, 1],               # right
        [41, 22, 7, 2], [41, 24, 1, 1], [44, 24, 2, 1],   # on the face, lower right
    ], to(SPIKES, GRAY)),
    *rects("back", "karada-a", [
        [11, 7, 5, 3], [12, 10, 3, 1],                # top left
        [6, 14, 7, 4], [10, 18, 2, 1],                # left
        [9, 24, 4, 2],                                # bottom left
        [15, 27, 5, 3],                               # bottom, small
        [23, 31, 3, 4], [26, 32, 1, 1],               # bottom, large
        [33, 32, 2, 2],                               # bottom, in shadow
        [40, 30, 4, 4], [39, 31, 1, 1],               # bottom right
        [45, 26, 5, 2],                               # lower right
        [41, 22, 7, 2], [45, 24, 2, 1],               # right, lower
        [43, 16, 8, 2], [42, 17, 1, 1], [44, 18, 6, 1], [45, 19, 4, 1], [46, 20, 2, 1],   # right
        [21, 23, 5, 1], [22, 24, 4, 3], [22, 27, 2, 1],   # on the back's lower half
    ], to(SPIKES, GRAY)),
    # the eyes: iris, pupil, and the line of a closed lid
    dict(view="front", drawings=["karada-a"], rect=[19, 16, 5, 4], colors={1: EYE}),
    dict(view="front", drawings=["karada-a"], rect=[30, 19, 6, 3], colors={1: EYE}),
    dict(drawings=["karada-a-eyes-open"], colors={1: EYE}),
    dict(drawings=["karada-a-eyes-closed"], rect=[4, 7, 3, 2], colors={5: EYE}),
    # band pixels at the edge of the eye drawings (the flood below cannot reach them)
    dict(drawings=["karada-a-eyes-*"], rect=[4, 10, 1, 1], colors={5: BANDS}),
    # the small black pits dotted over the pod: marks, not dents
    *rects("front", "karada-a", [[x, y, 1, 1] for x, y in [(32, 11), (23, 12), (27, 14), (33, 14), (30, 29)]], {5: BANDS}),
    *rects("back", "karada-a", [[x, y, 1, 1] for x, y in [(32, 13), (29, 16), (15, 18), (19, 21), (30, 22), (36, 24), (31, 30)]], {5: BANDS}),
    dict(drawings=["karada-a-eyes-*"], rect=[12, 3, 1, 1], colors={5: BANDS}),
    dict(drawings=["karada-a-eyes-*"], rect=[18, 3, 1, 1], colors={5: BANDS}),
]
# the two black bands: every dark pixel touching a seed. The body's own dark contour does not touch them.
FLOODS = [
    dict(view="front", drawing="karada-a", seeds=[[16, 12], [16, 24]], through=[5], colors={5: BANDS}),
    dict(view="front", drawing="karada-a-eyes-open", seeds=[[3, 4]], through=[5], colors={5: BANDS}),
    dict(view="front", drawing="karada-a-eyes-closed", seeds=[[3, 4]], through=[5], colors={5: BANDS}),
    dict(view="back", drawing="karada-a", seeds=[[17, 10], [10, 19], [30, 27], [21, 27]], through=[5, 6, 12], colors={5: BANDS}),
]
