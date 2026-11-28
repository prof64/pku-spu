# Jynx: a purple face and hands of bare matte skin (Hide), big pink lips, long straight blonde hair, and what the
# sprite's own drawing names call cloth ("nuno") and a bra ("bura"): a red gown with a yellow band round the bust
# and white sleeves. No Pokédex entry names any surface; all from the art, which paints everything flat.
SOURCE = "sources/black2-white2/0124-jynx.spu"
H = dict(finish=0.25, body=0.08)          # Hide: plain bare skin
CLOTH = dict(finish=-0.2, body=0)         # woven cloth: matte, a faint soft edge; solid
MATERIALS = [
    # black; the hair's brown lines (15): strands lying over one another, and its contour. The palette has no step
    # between the gold and that brown: as the hair's darkest shade it turned the whole head of hair muddy tan in
    # a field. Stray contour pixels (8, 4)
    dict(name="outline", shades=[1, 15, 8, 4], finish=0.1, body=0),
    # the long hair: a big mass, so the big-coat fur value; mostly painted in the deep gold (14)
    dict(name="fur, hair", shades=[14, 13, 12], base=0, finish=-0.1, body=0.05),
    # face and hands
    dict(name="hide", shades=[11, 10, 9], base=1, **H),
    dict(name="hide, lips", shades=[5, 2], base=1, **H),
    # the one white pixel on the upper lip: the lip at its most lit, in its own row so it goes dark with the lips
    dict(name="hide, lips, lit patch", shades=[5, 2, 6], base=1, **H),
    dict(name="mouth", shades=[4], base=0, finish=0.8, body=0),
    # the red gown; its darkest red is its contour and the shadow under the hair
    dict(name="cloth", shades=[5, 4, 3, 2], base=1, **CLOTH),
    # the yellow band round the bust: painted flat, no highlight, so cloth and not gold
    dict(name="cloth, trim", shades=[15, 14, 13], base=1, **CLOTH),
    # the white sleeves, drawn with fold lines at the elbow
    dict(name="cloth, sleeves", shades=[8, 7, 6], base=1, **CLOTH),
    dict(name="eye (line art)", shades=[1, 7, 6], finish=0.9, body=0),
]
def to(name, colors): return {c: name for c in colors}
COLORS = {1: "outline", 15: "outline", **to("fur, hair", [14, 13, 12]), **to("hide", [11, 10, 9]), **to("cloth", [5, 4, 3, 2]),
          **to("cloth, sleeves", [8, 7, 6])}
RULES = [
    # head and locks: stray contour pixels
    dict(drawings=["atama", "kami*"], colors={8: "outline", 4: "outline"}),
    dict(drawings=["bura"], colors=to("cloth, trim", [15, 14, 13])),
    dict(drawings=["kuti"], colors={5: "hide, lips", 2: "hide, lips", 6: "hide, lips, lit patch", 4: "mouth"}),
    dict(drawings=["atama-eyes-open"], colors=to("eye (line art)", [6, 7, 1])),
]
