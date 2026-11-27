SOURCE = "sources/black2-white2/0073-tentacruel.spu"
# Palette: 1 white, 2 pale pink (the orbs' painted highlights; 1 is the eye's white too); 3 4 5 the orbs' reds;
# 6 7 9 10 the tentacles' grays (10 is the eye's shaded white too); 11 12 13 14 the blues; 15 black.
MATERIALS = [
    # black is the line, and the dark hollow under the bell (a hole: it stays dark).
    # One dark gray pixel softens the line at the tip of a beak-like arm.
    dict(name="outline", shades=[15, 9], finish=0.1, body=0),
    # bell, skirt and the two beak-like arms: the same body as Tentacool's ("almost entirely composed of water").
    # The art paints it an opaque blue with soft shading, so it is wet and lets light through, but is not seen through.
    dict(name="jelly, clear body", shades=[14, 13, 12, 11], base=1, finish=0.6, body=0.45),
    # the two big red orbs and the small one between them: Tentacool's "glassy" orbs, grown large.
    # The art paints smooth red glass domes with broad pale reflections. The pink and white painted on the orbs are
    # the art's own highlights: they stay as painted, outside the shades.
    dict(name="crystal, gem", shades=[5, 4, 3], base=1, finish=1.0, body=0.95),
    # the tentacles: painted flat gray, soft shading, no highlight
    dict(name="hide", shades=[9, 7, 6, 10], base=1, finish=0.25, body=0.08),
    dict(name="eye (line art)", shades=[10, 1], finish=0.9, body=0),
]
def to(name, colors): return {c: name for c in colors}
EYE = to("eye (line art)", [10, 1])
COLORS = {15: "outline", **to("jelly, clear body", [14, 13, 12, 11]), **to("crystal, gem", [5, 4, 3, 2, 1]),
          **to("hide", [9, 7, 6, 10])}
RULES = [
    # the same white is the orbs' highlight and the white of the eye; the eyes' gray is the tentacles' pale gray
    dict(drawings=["body2-eyes-*"], rect=[0, 4, 32, 12], colors=EYE),
    # the eyes are drawn on the head itself too (under the eye drawing)
    dict(view="front", drawings=["body2"], rect=[0, 25, 56, 7], colors=EYE),
    dict(view="front", drawings=["body"], colors={9: "outline"}),
]
# The tentacles' palest gray is the soft light on their swollen tips, a twentieth of the tentacles. Left out of
# the row it stays pale on tentacles gone dark with the sun behind, so it is kept as a real shade.
KEEP_TOP = ["hide"]
