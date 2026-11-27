SOURCE = "sources/black2-white2/0351-castform.spu"
# Castform, normal form: one smooth gray body (head, horn, the two lobes it rests on, tail) and a white
# face mask. The painted art shades it softly with broad pale patches and no hard highlight: plain hide.
MATERIALS = [
    dict(name="outline", shades=[14, 13], finish=0.1, body=0),
    dict(name="hide", shades=[5, 4, 3, 2, 1], base=2, finish=0.25, body=0.08),
    # the mask is a marking on the same skin: its gray rim (8) and soft edge (12) are its shades
    dict(name="hide, face mask", shades=[8, 12, 7], base=2, finish=0.25, body=0.08),
    dict(name="eye (line art)", shades=[14, 13, 15], finish=0.9, body=0),
]
def to(name, colors): return {c: name for c in colors}
COLORS = {14: "outline", 13: "outline",            # black line; dark gray = the mouth line and the mask's edge at the silhouette
          **to("hide", [5, 4, 3, 2, 1]),
          **to("hide, face mask", [8, 12, 7]),
          15: "eye (line art)"}                      # the catchlight
RULES = [
    # the eye drawings: pupil (14), its gray edge (13), catchlight (15); closed, the lid line
    dict(drawings=["*-eyes-*"], colors=to("eye (line art)", [14, 13, 15])),
]
# The art paints one soft pale patch (1) on the head, the horn and each lobe. Left out of the row it
# stays put as a gray blot under the studio lamp and in the cave; kept, it moves with the light.
KEEP_TOP = ["hide"]
