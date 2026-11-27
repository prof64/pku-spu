SOURCE = "sources/black2-white2/0026-raichu.spu"
MATERIALS = [
    # black line; the nose, the mouth line and the lines between the toes are drawn in the dark browns
    dict(name="outline", shades=[1, 8, 7, 6, 12, 11, 9], finish=0.1, body=0),
    # the orange coat: its dark red-brown contour colors are its darkest shades
    dict(name="short fur", shades=[8, 7, 6, 5, 4], base=3, finish=-0.2, body=0.05),
    dict(name="short fur, belly", shades=[3, 2], base=1, finish=-0.2, body=0.05),
    # the soles seen from behind are painted in the belly's shade alone; the cream above it is its lighter step
    dict(name="short fur, soles", shades=[3, 2], base=0, finish=-0.2, body=0.05),
    dict(name="short fur, sole spots", shades=[6, 5], base=0, finish=-0.2, body=0.05),
    dict(name="short fur, cheeks", shades=[12, 11, 10, 9], base=3, finish=-0.2, body=0.05),
    dict(name="short fur, tail and ear insides", shades=[8, 12, 11, 10, 9], base=3, finish=-0.2, body=0.05),
    dict(name="short fur, paws and ears", shades=[8, 12, 11], base=2, finish=-0.2, body=0.05),
    dict(name="short fur, stripes", shades=[12, 6], base=0, finish=-0.2, body=0.05),
    dict(name="short fur, tail cord", shades=[15, 14], base=0, finish=-0.2, body=0.05),
    # the red inside of the open mouth is one color; the dark line around it is its shade
    dict(name="mouth", shades=[8, 13], base=1, finish=0.8, body=0),
    dict(name="eye (line art)", shades=[1, 7, 2], finish=0.9, body=0),
]
def to(name, colors): return {c: name for c in colors}
YELLOW, BROWN, LINE = "short fur, tail and ear insides", "short fur, paws and ears", "outline"
COLORS = {1: LINE, **to("short fur", [8, 7, 6, 5, 4]), **to("short fur, belly", [3, 2]), **to(YELLOW, [10, 9]),
          **to(BROWN, [12, 11]), 13: "mouth", **to("short fur, tail cord", [15, 14])}
RULES = [
    # ears (brown outside and rim, yellow inside) and the brown feet: their dark contour is the brown's
    dict(drawings=["mimi*", "ear-*", "foot01", "foot02"], colors={8: BROWN}),
    # the brown paws at the end of the orange arms
    dict(view="front", drawings=["te01"], rect=[4, 2, 5, 3], colors={8: BROWN}),
    dict(view="front", drawings=["te02"], rect=[6, 3, 7, 7], colors={8: BROWN}),
    dict(view="back", drawings=["hand-l"], rect=[3, 3, 6, 6], colors={8: BROWN}),
    dict(view="back", drawings=["hand-r"], rect=[6, 2, 10, 6], colors={8: BROWN}),
    # the lightning-bolt tail (male and female): yellow, with its olive and brown contour as its shades
    dict(drawings=["o01*", "tail-a*"], colors=to(YELLOW, [8, 12, 11])),
    # the head: yellow cheek patches with their dark contour, nose, mouth line, open mouth
    dict(drawings=["atama", "head"], colors=to("short fur, cheeks", [10, 9])),
    dict(view="front", drawings=["atama"], rect=[0, 8, 3, 6], colors=to("short fur, cheeks", [12, 11])),
    dict(view="front", drawings=["atama"], rect=[4, 10, 9, 7], colors=to(LINE, [8, 7, 6])),
    dict(drawings=["atama-eyes-*"], colors=to("eye (line art)", [1, 2])),
    dict(drawings=["atama-eyes-*"], rect=[11, 5, 1, 1], colors={7: "eye (line art)"}),
    dict(drawings=["atama-eyes-*"], rect=[9, 9, 9, 3], colors=to(LINE, [8, 7, 6])),
    # the two brown stripes across the back (they run on over the left leg); the pale edge is the belly showing
    dict(view="back", drawings=["body", "leg-l"], colors={12: "short fur, stripes"}),
    dict(view="back", drawings=["body"], rect=[0, 9, 32, 12], colors={6: "short fur, stripes"}),
    dict(view="back", drawings=["leg-l"], rect=[0, 9, 16, 5], colors={6: "short fur, stripes"}),
    dict(view="back", drawings=["body"], colors={9: LINE}),
    # the soles seen from behind, their orange spots, and the lines between the toes
    dict(view="back", drawings=["leg-*", "foot-*"], colors={3: "short fur, soles"}),
    dict(view="back", drawings=["leg-l"], rect=[6, 28, 2, 3], colors=to("short fur, sole spots", [6, 5])),
    dict(view="back", drawings=["leg-r"], rect=[2, 20, 3, 3], colors=to("short fur, sole spots", [6, 5])),
    dict(view="back", drawings=["leg-l"], rect=[11, 33, 1, 1], colors={11: LINE}),
    dict(view="back", drawings=["leg-r"], rect=[9, 23, 1, 1], colors={11: LINE}),
    dict(view="back", drawings=["foot-l"], colors=to(LINE, [8, 12, 11])),
    dict(view="back", drawings=["foot-r"], rect=[0, 7, 16, 3], colors={8: BROWN}),
    dict(view="back", drawings=["foot-r"], rect=[0, 10, 16, 3], colors=to(LINE, [8, 11])),
]

# Sapphire: "This POKéMON exudes a weak electrical charge from all over its body that makes it take on a
# slight glow in darkness." Yellow: "It also glows in the dark." A faint glow on the whole coat.
GLOW = [dict(material=m["name"], glow=4, intent="its body takes on a slight glow in darkness")
        for m in MATERIALS if m["name"].startswith("short fur")]
