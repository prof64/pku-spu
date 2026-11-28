# Vaporeon: smooth aquatic skin, a dark blue ridge down the back and tail, cream fins on the head and a white
# frill round the neck. The painted art shades all of it flat and soft, with broad pale patches and no hard
# highlight, so nothing is wet or polished: the same Fish skin and Fin as Lanturn. The Pokédex says its cells
# are "similar to water molecules" and that it "can melt away into water", but at rest both the art and the
# sprite paint an opaque body, so it is skin, not a clear body. Nothing glows.
SOURCE = "sources/black2-white2/0134-vaporeon.spu"
SKIN = dict(finish=0.15, body=0.08)
FIN = dict(finish=0.3, body=0.15)
MATERIALS = [
    # black line; lines drawn in dark blue where a leg lies over the body; the one-pixel nose
    dict(name="outline", shades=[1, 7, 6], finish=0.1, body=0),
    # the light blue body, legs and tail: its navy contour is its darkest shade. The back view is wholly in 4,
    # the front body in 3 and 4, the face a step or two lighter
    dict(name="fish skin", shades=[7, 6, 4, 3, 2], base=2, **SKIN),
    # the dark blue ridge along the back and tail, the cap on the forehead and the arms of the three head
    # fins: pigment in the same skin
    dict(name="fish skin, ridge and fin arms", shades=[7, 6], base=1, **SKIN),
    # the cream webs of the ear fins and the crest: thin skin, painted flat; olive contour
    dict(name="fin", shades=[13, 12, 11], base=2, **FIN),
    # the white frill: the same thin skin, its folds drawn in gray
    dict(name="fin, frill", shades=[10, 9, 8], base=2, **FIN),
    # the frill seen from behind, which the sprite paints in the body's blue with fold lines
    dict(name="fin, frill from behind", shades=[7, 6, 4, 3], base=2, **FIN),
    dict(name="mouth", shades=[15, 14], base=0, finish=0.8, body=0),
    # black, the purple iris, the white catchlight and the blue pixel that rounds each eye's corner
    dict(name="eye (line art)", shades=[1, 5, 8, 4, 6], finish=0.9, body=0),
]
def to(name, colors): return {c: name for c in colors}
RIDGE, EYE, BACKFRILL = "fish skin, ridge and fin arms", "eye (line art)", "fin, frill from behind"
COLORS = {1: "outline", **to("fish skin", [7, 6, 4, 3, 2]), **to("fin", [13, 12, 11]), **to("fin, frill", [10, 9, 8]),
          **to("mouth", [15, 14]), 5: EYE}
CREASE = {7: ([1, 2, 3, 4, 6], "outline"), 6: ([1, 2, 3, 4, 7], "outline")}
RULES = [
    # a dark blue line wholly inside the skin is one piece lying over another (leg over body, haunch over tail)
    dict(view="front", drawings=["karada", "sippo"], interior=CREASE),
    dict(view="back", drawings=["body", "foot"], interior=CREASE),
    # the head: everything dark blue above the eyes is the cap and the fin arms; the cap's point between the eyes
    dict(view="front", drawings=["atama"], rect=[0, 0, 40, 19], colors=to(RIDGE, [7, 6])),
    dict(view="front", drawings=["atama"], rect=[14, 19, 1, 1], colors={6: RIDGE}),
    # the nose
    dict(view="front", drawings=["atama"], rect=[14, 23, 1, 1], colors={6: "outline"}),
    # the fins seen from behind
    dict(view="back", drawings=["ear-l", "ear-r", "tosaka"], colors=to(RIDGE, [7, 6])),
    # the frill seen from behind
    dict(view="back", drawings=["head"], colors=to(BACKFRILL, [7, 6, 4, 3])),
    # the eyes; shut, they are drawn lines
    dict(view="front", drawings=["atama-eyes-open"], rect=[1, 3, 3, 4], colors=to(EYE, [1, 8, 5, 4])),
    dict(view="front", drawings=["atama-eyes-open"], rect=[9, 3, 4, 4], colors=to(EYE, [1, 8, 5, 6])),
    dict(view="front", drawings=["atama-eyes-closed"], rect=[2, 5, 2, 2], colors={7: "outline"}),
    dict(view="front", drawings=["atama-eyes-closed"], rect=[9, 5, 4, 2], colors={7: "outline"}),
]
# the ridge: its dark blue and the navy that edges it, from a pixel of it outward
BAND = to(RIDGE, [7, 6])
FLOODS = [
    dict(view="front", drawing="karada", seeds=[[16, 9], [16, 30]], through=[6, 7], colors=BAND),
    dict(view="front", drawing="sippo", seeds=[[11, 9]], through=[6, 7], colors=BAND),
    dict(view="front", drawing="sippo2", seeds=[[10, 9]], through=[6, 7], colors=BAND),
    dict(view="back", drawing="body", seeds=[[11, 4]], through=[6, 7], colors=BAND, diagonal=True),
    # the far foreleg seen from behind, painted in the skin's two darkest blues: skin in shadow, not a line
    dict(view="back", drawing="foot", seeds=[[9, 3]], through=[6, 7], colors=to("fish skin", [6, 7])),
]
