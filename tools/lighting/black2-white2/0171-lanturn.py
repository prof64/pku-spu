# Lanturn: smooth fish skin, a yellow face mask, pale thin fins, and the two orbs on its antenna, which give off
# light (Emerald: "The light-emitting orbs on its back are very bright").
SOURCE = "sources/black2-white2/0171-lanturn.spu"
MATERIALS = [
    dict(name="outline", shades=[15], finish=0.1, body=0),
    # the blue body, head and tail blade: the navy contour is its darkest shade. The art paints one soft pale band
    # along the back and no hard highlight: a soft sheen, not wet
    dict(name="fish skin", shades=[1, 2, 3, 4, 5], base=1, finish=0.15, body=0.08),
    # the antenna stalks, painted a step lighter than the body
    dict(name="fish skin, antenna", shades=[1, 2, 3, 4, 5], base=3, finish=0.4, body=0.08),
    # the yellow mask round the eye and mouth: pigment in the same skin
    dict(name="fish skin, mask", shades=[8, 9, 10, 11, 12], base=4, finish=0.4, body=0.08),
    # the pale pectoral fins: thin skin, painted flat and soft. Body 0.15, not more: at 0.3 they stayed near white
    # in the cave and washed out with the sun behind
    dict(name="fin", shades=[1, 2, 3, 4, 5], base=4, finish=0.3, body=0.15),
    # the yellow lobe of the tail fin, painted in ochre (no pale yellow)
    dict(name="fin, tail", shades=[8, 9, 10, 11], base=2, finish=0.3, body=0.15),
    # the big orb at the antenna's tip: the light itself, white at its core
    dict(name="light organ", shades=[8, 9, 10, 11, 12, 14], base=4, finish=0.5, body=0.5),
    # the small orb, painted dimmer (ochre, no white core)
    dict(name="light organ, small", shades=[8, 9, 10, 11, 12], base=2, finish=0.5, body=0.5),
    # the rings of light the orbs throw off when they twinkle: light only, no surface
    dict(name="light organ, flare", shades=[12, 14], base=0, finish=0, body=0),
    dict(name="mouth", shades=[8, 6, 7], base=1, finish=0.8, body=0),
    dict(name="eye (line art)", shades=[15, 8, 9, 10, 6, 7, 13, 14], finish=0.9, body=0),
]
def to(name, colors): return {c: name for c in colors}
BLUE, YELLOW = [1, 2, 3, 4, 5], [8, 9, 10, 11, 12]
COLORS = {15: "outline", **to("fish skin", BLUE), **to("fish skin, mask", YELLOW),
          **to("eye (line art)", [6, 7, 13, 14])}

# the eye, pixel row by pixel row: white, red iris, black pupil and the rim drawn round it in the mask's browns
# (the same places hold the lid lines of the closed eye)
EYE = to("eye (line art)", [15, 8, 9, 10, 6, 7, 13, 14])
FRONT_EYE = [[9, 1, 3, 1], [8, 2, 5, 1], [7, 3, 6, 1], [7, 4, 6, 1], [6, 5, 7, 1], [6, 6, 7, 1], [6, 7, 5, 1]]
BACK_EYE = [[24, 15, 2, 1], [23, 16, 4, 1], [23, 17, 4, 1], [24, 18, 4, 1], [24, 19, 4, 1], [25, 20, 3, 1],
            [25, 21, 3, 1], [28, 20, 1, 1]]      # in the head drawing; the eye drawings sit 17 right, 10 down of it
RULES = [
    dict(drawings=["parts0*"], colors=to("fish skin, antenna", BLUE)),
    dict(drawings=["r-arm", "l-arm"], colors=to("fin", BLUE)),
    dict(drawings=["tail"], colors=to("fin, tail", [8, 9, 10, 11])),
    dict(drawings=["ball01*"], colors=to("light organ", YELLOW + [14])),
    dict(drawings=["ball02*"], colors=to("light organ, small", YELLOW + [14])),
    # the open mouth (front only): dark red inside, pink tongue, and the brown line round it as its shade
    dict(view="front", drawings=["head"], colors=to("mouth", [6, 7])),
    dict(view="front", drawings=["head"], rect=[7, 24, 10, 2], colors={8: "mouth"}),
] + [dict(view="front", drawings=["head-eyes-*"], rect=r, colors=EYE) for r in FRONT_EYE] \
  + [dict(view="back", drawings=["head"], rect=r, colors=EYE) for r in BACK_EYE] \
  + [dict(view="back", drawings=["head-eyes-*"], rect=[r[0] - 17, r[1] - 10, r[2], r[3]], colors=EYE) for r in BACK_EYE]

# the twinkle drawings hold the orb and, apart from it, the ring of light round it
RING = to("light organ, flare", [12, 14])
FLOODS = [
    dict(drawing="ball01-2", seeds=[[9, 2]], through=[12, 14], colors=RING, diagonal=True),
    dict(view="back", drawing="ball02-2", seeds=[[9, 5]], through=[12, 14], colors=RING, diagonal=True),
    dict(view="front", drawing="ball02-2", seeds=[[5, 2]], through=[12, 14], colors=RING, diagonal=True),
]
# the big orb's white core is the heart of the light, not a glint
KEEP_TOP = ["light organ", "light organ, small"]

# Emerald: "The light-emitting orbs on its back are very bright." Gold: "The light it emits is so bright that it
# can illuminate the sea's surface from a depth of over three miles." Only the orbs and their rings of light glow.
GLOW = [
    dict(material="light organ", colors=[14], glow=255, intent="the big orb's white core is the brightest"),
    dict(material="light organ", colors=[12], glow=235, intent="the big orb's pale yellow"),
    dict(material="light organ", colors=[11], glow=205, intent="the big orb's yellow"),
    dict(material="light organ", colors=[10], glow=175, intent="the big orb's ochre edge"),
    dict(material="light organ", colors=[8, 9], glow=120, intent="the big orb's rim shines least"),
    dict(material="light organ, small", colors=[12], glow=235, intent="the small orb's pale yellow"),
    dict(material="light organ, small", colors=[11], glow=205, intent="the small orb's yellow"),
    dict(material="light organ, small", colors=[10], glow=175, intent="the small orb's ochre"),
    dict(material="light organ, small", colors=[8, 9], glow=120, intent="the small orb's rim shines least"),
    dict(material="light organ, flare", colors=[14], glow=255, intent="the white ring of light"),
    dict(material="light organ, flare", colors=[12], glow=220, intent="the yellow ring of light"),
]

def AFTER(job):
    # the orbs twinkle (the plain orb and the orb with its ring take turns): the glow follows, as a flame's does
    s = job.s
    for a in s.overview()["animations"]:
        an = s.read_animation(animation=a["id"])
        for view, vd in an["views"].items():
            for t in vd["tracks"]:
                keys = [k for k in (t.get("drawings") or []) if k[1]]
                if not t["part"].startswith("ball") or len({k[1] for k in keys}) < 2: continue
                em = [[k[0], 1 if k[1].endswith("-2") else 0.8, "step"] for k in keys]
                s.set_track(animation=a["id"], view=view, part=t["part"], emission=em,
                            intent="the orb's glow twinkles with its drawn twinkle")
