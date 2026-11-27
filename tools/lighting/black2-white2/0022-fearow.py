# Fearow: plumage all over (matte Feathers), cream tips and a cream ruff as their own rows; the comb and feet are
# bare skin, the beak and claws horn.
SOURCE = "sources/black2-white2/0022-fearow.spu"
F = dict(finish=-0.2, body=0.05)          # Feathers
MATERIALS = [
    dict(name="outline", shades=[1, 6, 5, 15, 11], finish=0.1, body=0),
    dict(name="feathers", shades=[6, 5, 4, 3], base=1, **F),                     # brown body, neck, head, wings, tail
    dict(name="feathers, wing tips", shades=[4, 3, 2], base=1, **F),             # the cream ends of the flight feathers
    dict(name="feathers, ruff", shades=[15, 14, 13, 12], base=2, **F),           # the shaggy cream ruff at the base of the neck
    # the red comb on the head is bare skin, painted flat: matte, solid
    dict(name="comb", shades=[11, 10, 9], base=2, finish=0.1, body=0.08),
    dict(name="dry hide, feet", shades=[11, 10, 9, 8], base=3, finish=0.05, body=0.03),
    # the palette's unused pale pink (7) is the beak's own lighter step. Its dark red contour (11) is left out of the
    # shades, so it is only tinted: the beak is two or three pixels thick, and shaded by direction the contour
    # (two steps down, on the lit side) made the whole beak blotchy under any light but the art's
    dict(name="beak", shades=[9, 8, 7], base=1, finish=0.4, body=0.05),
    dict(name="claws and teeth", shades=[15, 13, 12], base=1, finish=0.7, body=0.05),
    dict(name="eye (line art)", shades=[1, 2, 12], finish=0.9, body=0),
]
def to(name, colors): return {c: name for c in colors}
COLORS = {1: "outline", 2: "feathers, wing tips", **to("feathers", [3, 4, 5, 6]), **to("dry hide, feet", [8, 9, 10, 11]),
          **to("feathers, ruff", [12, 13, 14, 15])}
WINGS = ["hane*", "wing-*"]
COMB = to("comb", [9, 10, 11])
EYE = to("eye (line art)", [1, 2, 12])
RULES = [
    # head: beak below, comb above
    dict(drawings=["atama", "atama-eyes-*"], colors=to("beak", [8, 9, 11])),
    dict(drawings=["atama"], rect=[0, 0, 40, 17], colors=COMB),
    dict(view="front", drawings=["atama"], rect=[20, 17, 11, 1], colors=COMB),
    dict(drawings=["atama-eyes-*"], rect=[0, 0, 8, 3], colors=COMB),
    dict(drawings=["karada"], colors={11: "comb", 15: "outline"}),
    dict(view="front", drawings=["atama-eyes-*"], rect=[2, 2, 5, 3], colors=EYE),
    dict(view="back", drawings=["atama-eyes-*"], rect=[3, 3, 3, 3], colors=EYE),
    # feet: white claws, the feathered thigh stays plumage
    dict(drawings=["asi*"], colors=to("claws and teeth", [12, 13, 15])),
    dict(drawings=["asi02"], rect=[12, 0, 12, 24], colors={11: "outline", 15: "outline"}),
    # wings: which colors are the cream tips differs by drawing (the back view paints them a step darker)
    dict(drawings=["hane01", "hane04-2"], colors={3: "feathers, wing tips"}),
    dict(drawings=["hane01"], rect=[10, 13, 7, 9], colors={3: "feathers"}),      # the lit leading edge, not a tip
    dict(drawings=["wing-r*"], colors=to("feathers, wing tips", [3, 4])),
    dict(drawings=["wing-l*"], colors={4: "feathers, wing tips"}),
    dict(drawings=WINGS, colors={11: "outline"}),
    # flight feathers overlap: the lines between them are creases; so are the lines between the ruff's tufts
    dict(drawings=WINGS, thin_all={6: "outline", 15: "outline"}),
    dict(drawings=["hane04", "hane04-3", "hane01-2", "hane01-3"], thin_all={5: "outline"}),
    dict(drawings=["body"], thin_all={15: "outline"}),
]
