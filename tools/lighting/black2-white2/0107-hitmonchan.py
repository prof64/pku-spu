# Hitmonchan: bare tan skin (Hide), head crest and shoulder guards included; it wears a lilac tunic and pleated
# kilt with a black belt, lilac boxing shoes and red boxing gloves.
SOURCE = "sources/black2-white2/0107-hitmonchan.spu"
H = dict(finish=0.25, body=0.08)          # Hide: plain bare skin
CLOTH = dict(finish=-0.2, body=0)         # woven cloth: matte, a faint soft edge; solid
SHOE = dict(finish=0.1, body=0)          # soft dull shoe
GLOVE = dict(finish=0.2, body=0)          # padded glove: the art paints a broad soft light patch, no hard highlight
MATERIALS = [
    # black (also the dark underside of the raised shoulder guard), and the dark purple lines between the kilt's pleats
    dict(name="outline", shades=[15, 5], finish=0.1, body=0),
    # the skin: its dark brown contour (14) is its darkest shade
    dict(name="hide", shades=[14, 13, 12, 11], base=1, **H),
    # tunic and kilt. The palette has no step between the lilac and its dark purple contour (5), so the contour
    # is outline: as the cloth's darkest shade the tunic speckled dark purple in the cave
    dict(name="cloth", shades=[4, 3], base=0, **CLOTH),
    # the black belt: drawn in flat black
    dict(name="cloth, belt", shades=[15], base=0, **CLOTH),
    # boxing shoes: soft and dull
    dict(name="shoes", shades=[5, 4, 3], base=1, **SHOE),
    # the few palest pixels (2) on each toe cap: the same shoe at its most lit, in their own row so they go dark
    # with the shoe
    dict(name="shoes, lit patches", shades=[5, 4, 3, 2], base=1, **SHOE),
    dict(name="boxing gloves", shades=[10, 9, 8], base=1, **GLOVE),
    # the few orange pixels (7) on top of each glove: the same glove at its most lit. In their own row so they go
    # dark with the glove instead of staying bright as painted glints
    dict(name="boxing gloves, lit patches", shades=[10, 9, 8, 7], base=1, **GLOVE),
    dict(name="eye (line art)", shades=[5, 2, 1], finish=0.9, body=0),
]
def to(name, colors): return {c: name for c in colors}
COLORS = {15: "outline", **to("hide", [14, 13, 12, 11]), 5: "outline", **to("cloth", [4, 3]), 2: "shoes, lit patches",
          **to("boxing gloves", [10, 9, 8]), 7: "boxing gloves, lit patches"}
RULES = [
    # the eyes: white, its gray and the dark purple iris
    dict(drawings=["atama", "atama-eyes-*"], colors=to("eye (line art)", [5, 2, 1])),
    # the shoes share the tunic's lilacs
    dict(drawings=["asi", "leg-*", "foot-*"], colors={**to("shoes", [5, 4, 3]), 2: "shoes, lit patches"}),
    # the kilt's pleats lie one over the next: the lines between them are creases
    dict(drawings=["kahansin", "body-b"], thin_all={5: "outline"}),
    # the black belt
    dict(view="front", drawings=["kata"], rect=[12, 18, 13, 3], colors={15: "cloth, belt"}),
    dict(view="front", drawings=["kahansin"], rect=[6, 3, 11, 2], colors={15: "cloth, belt"}),
    dict(view="back", drawings=["body-a"], rect=[6, 19, 12, 2], colors={15: "cloth, belt"}),
    dict(view="back", drawings=["body-b"], rect=[5, 2, 12, 4], colors={15: "cloth, belt"}),
]
