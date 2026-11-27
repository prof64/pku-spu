SOURCE = "sources/black2-white2/0582-vanillite.spu"
# Palette: 6 white, 10 7 8 9 the snow's lilac grays (9 its contour); 1 2 3 4 the ice blues; 5 4 11 the breath
# puffs; 12 13 14 the eyes and mouth; 15 black. The unused first color is pink, so no white takes it.
SNOW = [9, 8, 7, 10, 6]
ICE = [1, 2, 3, 4, 6]
# Gas (the standard row). Smeargle gives a row named gas no shape, so each of the puffs' three blues is
# its own row with the same dials (as on Gastly): how thick the frozen breath is, not shading.
GAS = dict(finish=-0.5, body=0.75)
MATERIALS = [
    # black; and one dark blue pixel on the collar's edge in each view (a softened line)
    dict(name="outline", shades=[15, 1, 2], finish=0.1, body=0),
    # the swirl, the ring under it, the round head and the lobed collar under the head: a coat of snow
    # (the standard Snow row). Its slate and blue-gray contour colors are its darkest shades. Base is white:
    # white and the lilac 7 tie at 363 pixels each (front is painted white, the back lilac); with the lilac
    # as base the front went gray under the studio lamp.
    dict(name="snow", shades=SNOW, base=4, finish=-0.5, body=0.5),
    # the cone it stands in: faceted clear ice (the standard Ice row); the white facets the art and the
    # sprite paint are its top shade, so they move with the light
    dict(name="ice", shades=ICE, base=2, finish=0.8, body=0.8),
    dict(name="ice, hands", shades=ICE, base=3, finish=0.8, body=0.8),
    dict(name="ice, cheek crystals", shades=[2, 3, 4], base=1, finish=0.8, body=0.8),
    dict(name="gas", shades=[4], base=0, **GAS),
    dict(name="gas, thin edge", shades=[5], base=0, **GAS),
    dict(name="gas, dense", shades=[11], base=0, **GAS),
    dict(name="mouth", shades=[13, 12], base=0, finish=0.8, body=0),
    dict(name="eye (line art)", shades=[14, 13, 12, 5, 4], finish=0.9, body=0),
]
def to(name, colors): return {c: name for c in colors}
COLORS = {15: "outline", **to("snow", SNOW), **to("ice", [1, 2, 3, 4]),
          5: "gas, thin edge", 11: "gas, dense", **to("mouth", [13, 12]), 14: "eye (line art)"}
EYE = to("eye (line art)", [14, 13, 12, 5, 4])
FACES = ["face", "lhand-3", "rhand-3"]          # the head, its second front drawing (another mouth) and its back twin
RULES = [
    dict(drawings=["body*"], colors={6: "ice"}),
    dict(drawings=["rhand", "rhand-2", "lhand", "lhand-2"], colors=to("ice, hands", ICE)),
    dict(drawings=FACES, colors=to("ice, cheek crystals", [2, 3, 4])),
    # the eyes painted on the head itself (under the eye drawings): pale ring, iris, pupil
    dict(view="front", drawings=FACES, rect=[7, 8, 5, 7], colors=EYE),
    dict(view="front", drawings=FACES, rect=[17, 9, 5, 7], colors=EYE),
    # one dark blue pixel on the collar's edge, front and back: a softened outline, not a speck of ice
    dict(view="front", drawings=FACES, rect=[9, 21, 1, 1], colors={2: "outline"}),
    dict(view="back", drawings=FACES, colors={1: "outline"}),
    # the eye drawings: the white and lilac around the eyes are snow; closed, the lid lines and their soft ends
    dict(drawings=["*-eyes-*"], colors=EYE),
    # the breath puffs
    dict(drawings=["head-a-3", "head-a-4", "head-b-2", "head-b-3", "smoke-*"], colors={4: "gas"}),
]
