# Staryu: a matte starfish body, a dull gold-colored casing, and the red core: a polished gem that shines.
SOURCE = "sources/black2-white2/0120-staryu.spu"
MATERIALS = [
    dict(name="outline", shades=[1, 5], finish=0.1, body=0),
    # the arms: flat brush-painted planes in the art, no highlight anywhere
    dict(name="starfish skin", shades=[6, 5, 4, 3, 2], base=2, finish=0.1, body=0.05),
    # the gold-colored fitting that holds the core (and its band round the lower arm, seen from behind):
    # hard and dull; the art paints lit faces and an olive shadow, no reflection
    dict(name="gold casing", shades=[11, 10, 9, 8, 7], base=2, finish=0.2, body=0),
    # the core: a polished red gem with a painted catchlight, and it shines (Ruby: "shines bright red").
    # Body 0.6, not the gem row's 0.8: at 0.8 the red washed out to pale pink in the cave and with the sun behind
    dict(name="core gem", shades=[15, 14, 13, 12], base=0, finish=1, body=0.6),
]
def to(name, colors): return {c: name for c in colors}
COLORS = {1: "outline", **to("starfish skin", [6, 5, 4, 3, 2]), **to("gold casing", [11, 10, 9, 8, 7]),
          **to("core gem", [15, 14, 13, 12])}
RULES = [
    # one brown pixel on the core's rim, between gem and casing: part of the line round the core
    dict(drawings=["housaki"], rect=[15, 10, 1, 1], colors={5: "outline"}),
]
# the casing's pale color is the lit face of each bar, not a glint: left out of the row it stayed bright in the dark
KEEP_TOP = ["gold casing"]
GLOW = [
    dict(material="core gem", colors=[14, 13, 12], glow=150, intent="the core shines bright red: its bright middle"),
    dict(material="core gem", colors=[15], glow=40, intent="the core's darker rim shines less"),
]
