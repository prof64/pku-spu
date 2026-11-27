SOURCE = "sources/black2-white2/0025-pikachu.spu"
MATERIALS = [
    # black line; the mouth line and the nose are drawn in the fur's browns
    dict(name="outline", shades=[1, 7, 6, 5], finish=0.1, body=0),
    # the yellow coat: its brown contour colors are its darkest shades
    dict(name="short fur", shades=[7, 6, 5, 4, 3, 2], base=4, finish=-0.2, body=0.05),
    dict(name="short fur, ear tips", shades=[14, 13, 12], base=1, finish=-0.2, body=0.05),
    dict(name="short fur, cheeks", shades=[10, 9], base=0, finish=-0.2, body=0.05),
    # the two brown stripes on the back and the brown base of the tail
    dict(name="short fur, stripes and tail base", shades=[7, 6, 5], base=1, finish=-0.2, body=0.05),
    dict(name="mouth", shades=[10, 9], base=0, finish=0.8, body=0),
    dict(name="eye (line art)", shades=[1, 14, 13, 15], finish=0.9, body=0),
]
def to(name, colors): return {c: name for c in colors}
COLORS = {1: "outline", **to("short fur", [7, 6, 5, 4, 3, 2]), **to("short fur, ear tips", [14, 13, 12]),
          **to("short fur, cheeks", [10, 9])}
EYE = to("eye (line art)", [1, 13, 14, 15])
BROWN = to("short fur, stripes and tail base", [7, 6, 5])
RULES = [
    # the head: both eyes (black, their gray reflections and white catchlight) and the one-pixel nose
    dict(view="front", drawings=["atama"], colors=to("eye (line art)", [13, 14, 15])),
    dict(view="front", drawings=["atama"], rect=[4, 9, 2, 4], colors=EYE),
    dict(view="front", drawings=["atama"], rect=[13, 8, 4, 4], colors=EYE),
    dict(view="front", drawings=["atama"], rect=[8, 11, 1, 1], colors={7: "outline"}),
    dict(drawings=["atama-eyes-*"], colors=EYE),
    dict(drawings=["atama-eyes-*"], rect=[5, 4, 1, 1], colors={7: "outline"}),
    # the mouth: its brown line is drawn line, the red inside and the tongue are the mouth
    dict(drawings=["kuti*"], colors={**to("outline", [7, 6, 5]), **to("mouth", [10, 9])}),
    # the two stripes across the back
    dict(view="back", drawings=["karada"], rect=[5, 7, 18, 9], colors=to("short fur, stripes and tail base", [6, 5])),
    # the brown base of the tail (male and female tails end the same way)
    dict(view="front", drawings=["o", "o-female"], rect=[0, 25, 24, 7], colors=BROWN),
    dict(view="back", drawings=["o", "o-female"], rect=[0, 26, 24, 5], colors=BROWN),
]
