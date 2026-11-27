SOURCE = "sources/black2-white2/0036-clefable.spu"
MATERIALS = [
    # black line, and the near-black purple (9) drawn around the wings and the tail: it is the drawn line
    # there (pure black in the shiny palette), so it is never a shade
    dict(name="outline", shades=[15, 9], finish=0.1, body=0),
    # the pink coat (body, curl, ears, arms, legs, feet): painted flat and soft in the official art, smooth-edged
    # with no tufts. Its dark pink contour is its darkest shade; front and back together are mostly painted in 6
    dict(name="short fur", shades=[8, 7, 6, 4], base=2, finish=-0.2, body=0.05),
    # the tail seen from the front, behind the body: the same coat, painted wholly in a shadow pink (14) no
    # other part uses, so it has its own ramp (from the back the tail is painted in the body's own colors)
    dict(name="short fur, tail", shades=[8, 14], base=1, finish=-0.2, body=0.05),
    dict(name="short fur, ear tips", shades=[13, 12], base=0, finish=-0.2, body=0.05),
    # the three-pointed wings: darker pink, painted as flat and soft as the body
    dict(name="short fur, wings", shades=[8, 10, 5], base=1, finish=-0.2, body=0.05),
    # the two white toes of each foot, with the palette's gray
    dict(name="claws and teeth", shades=[3, 1], base=1, finish=0.7, body=0.05),
    dict(name="mouth", shades=[8, 11], base=1, finish=0.8, body=0),
    dict(name="eye (line art)", shades=[15, 1], finish=0.9, body=0),
]
def to(name, colors): return {c: name for c in colors}
TAIL, WING = "short fur, tail", "short fur, wings"
COLORS = {15: "outline", 9: "outline", **to("short fur", [8, 7, 6, 4]), **to("short fur, ear tips", [13, 12]),
          **to(WING, [10, 5]), **to("claws and teeth", [3, 1]), 11: "mouth", 14: TAIL}
RULES = [
    dict(drawings=["tail"], colors=to(TAIL, [8, 14, 5])),      # one stray pixel of the wings' pink (5) is the tail's
    dict(drawings=["wing", "wing1", "l-wings01", "r-wings01"], colors=to(WING, [8, 10, 5])),
    # the open mouth: red inside and its dark rim (the black line above stays line)
    dict(drawings=["mouth01"], colors=to("mouth", [8, 11])),
    # the eyes: pupil and catchlight (the pink marks beside them are the coat's)
    dict(drawings=["body-eyes-open"], colors=to("eye (line art)", [15, 1])),
]
