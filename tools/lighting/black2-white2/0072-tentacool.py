SOURCE = "sources/black2-white2/0072-tentacool.spu"
MATERIALS = [
    # black is the line, and the dark hollow under the bell (a hole: it stays dark)
    dict(name="outline", shades=[1], finish=0.1, body=0),
    # head, bell and skirt: "almost entirely composed of water", "refracts [sunlight] using water inside its body".
    # The art paints it an opaque blue with soft shading, so it is wet and lets light through, but is not seen through.
    # Body 0.55 to 0.95 sprinkled it with white specks (yellow ones in the cave); 1.0 turned it white with the sun behind.
    dict(name="jelly, clear body", shades=[4, 5, 6, 7], base=1, finish=0.6, body=0.45),
    # the two big red orbs and the small one between them: "glassy", "as transparent as crystals".
    # The art paints a smooth glass ball with one highlight, so clear, not frosted: at 0.8 it was sprinkled with
    # specks that shone orange in the cave. The pink and white painted on the orbs are the art's own highlights:
    # they stay as painted, outside the shades (in the shades, a lamp turned the whole orb pink).
    dict(name="crystal, gem", shades=[8, 9, 10], base=1, finish=1.0, body=0.95),
    # the two feelers: painted flat gray-brown, no highlight
    dict(name="hide", shades=[12, 13, 14, 15], base=1, finish=0.25, body=0.08),
    dict(name="eye (line art)", shades=[3, 2], finish=0.9, body=0),
]
def to(name, colors): return {c: name for c in colors}
EYE = to("eye (line art)", [3, 2])
COLORS = {1: "outline", **to("jelly, clear body", [4, 5, 6, 7]), **to("crystal, gem", [8, 9, 10, 11, 2]),
          **to("hide", [12, 13, 14, 15]), 3: "eye (line art)"}
RULES = [
    # the same white is the orbs' highlight and the white of the eye
    dict(drawings=["head01-eyes-*"], colors=EYE),
    # from behind the eye is drawn on the head itself too (under the eye drawing)
    dict(view="back", drawings=["head01"], rect=[20, 28, 5, 6], colors=EYE),
]
