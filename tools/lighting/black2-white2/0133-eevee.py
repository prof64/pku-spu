# Eevee: a brown coat the painted art shades flat and soft, a big cream ruff and a bushy tail with a cream tip.
# No Pokédex entry describes a surface (they are all about its genes), so every part is set from the art:
# nothing has a highlight but the eyes, so everything is matte. The smooth-edged coat is the sleek one
# (Short fur, as on Pikachu and Growlithe); the ragged ruff and the brush of the tail are long fur
# (Fur at -0.1, as on Arcanine's mane: at -0.7 anything bigger than a tuft goes grainy). Nothing glows.
SOURCE = "sources/black2-white2/0133-eevee.spu"
SHORT = dict(finish=-0.2, body=0.05)
LONG = dict(finish=-0.1, body=0.05)
MATERIALS = [
    # black line; the nose, the mouth line and the shut eyes' lid lines are drawn in the coat's dark browns
    dict(name="outline", shades=[1, 6, 5], finish=0.1, body=0),
    # the brown coat: its dark-brown contour is its darkest shade. Body, legs and the whole back view are
    # painted in 4; the face is a step lighter
    dict(name="short fur", shades=[6, 5, 4, 3], base=2, **SHORT),
    # inside the ears (front view): black with a dark brown patch
    dict(name="short fur, ear insides", shades=[1, 6], base=0, **SHORT),
    # the cream ruff and the cream tip of the tail: long ragged fur, edged in the coat's dark browns
    dict(name="fur", shades=[6, 5, 9, 8, 7], base=3, **LONG),
    # the brown brush of the tail
    dict(name="fur, tail", shades=[6, 5, 4, 3], base=2, **LONG),
    # black pupil, brown iris, white catchlight
    dict(name="eye (line art)", shades=[1, 6, 10], finish=0.9, body=0),
]
# the lightest brown is the whole face: a shade, not a glint
KEEP_TOP = ["short fur", "fur", "fur, tail"]
def to(name, colors): return {c: name for c in colors}
EAR, EYE, TAIL = "short fur, ear insides", "eye (line art)", "fur, tail"
COLORS = {1: "outline", **to("short fur", [6, 5, 4, 3]), **to("fur", [9, 8, 7]), 10: EYE}
RULES = [
    # the ruff, front and back: its dark edge is its own darkest shade
    dict(drawings=["neck-*", "ke", "ke-2", "ke-3"], colors=to("fur", [6, 5, 9, 8, 7])),
    # the tail: brown brush, cream tip (the dark edge beside the cream is the cream's)
    dict(drawings=["tail", "o"], colors=to(TAIL, [6, 5, 4, 3])),
    dict(view="front", drawings=["tail"], rect=[0, 6, 24, 8], colors=to("fur", [5])),
    dict(view="back", drawings=["o"], rect=[0, 2, 14, 8], colors=to("fur", [6, 5])),
    # the ear insides seen from the front
    dict(view="front", drawings=["mimi-l"], rect=[7, 6, 3, 9], colors=to(EAR, [1, 6])),
    dict(view="front", drawings=["mimi-l"], rect=[7, 15, 1, 3], colors=to(EAR, [1, 6])),
    # the nose and the mouth line
    dict(view="front", drawings=["head"], rect=[4, 12, 1, 1], colors={6: "outline"}),
    dict(view="front", drawings=["head"], rect=[4, 14, 5, 2], colors={5: "outline"}),
    # the eyes: pupil, iris, catchlight; shut, they are drawn lines
    dict(view="front", drawings=["head-eyes-open"], rect=[2, 4, 3, 5], colors=to(EYE, [1, 6, 10])),
    dict(view="front", drawings=["head-eyes-open"], rect=[11, 6, 3, 5], colors=to(EYE, [1, 6, 10])),
    dict(view="front", drawings=["head-eyes-closed"], colors=to("outline", [6, 1])),
]
FLOODS = [
    dict(view="front", drawing="mimi-r", seeds=[[12, 10]], through=[1, 6], colors=to(EAR, [1, 6])),
]
