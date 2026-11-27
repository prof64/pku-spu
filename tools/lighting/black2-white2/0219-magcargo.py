# Magcargo: a body of magma under a shell of its own cooled crust, with a flame out of a gap in the shell.
# "The shell on its back is made of hardened magma. Tens of thousands of years spent living in volcanic
# craters have turned MAGCARGO's bodies into magma" (Emerald); "Its body is as hot as lava and is always
# billowing" (Crystal); "Flames spout from gaps in its hardened shell" (Black 2/White 2).
SOURCE = "sources/black2-white2/0219-magcargo.spu"
MAGMA = [5, 4, 3, 2]       # dark red contour and bubble rims, the body's red-orange, its lighter flow, the pale hot patches
ROCK = [14, 13, 12, 11]    # the shell's grays; the darkest also draws its lit-side contour and soft plate lines
MATERIALS = [
    dict(name="outline", shades=[15], finish=0.1, body=0),
    # head, jaw, neck, the spread foot and the drips: molten. Base is the red-orange (4) nearly all of both views
    # is painted in. The dark arcs on it are bubble rims in the magma's own darkest shade.
    dict(name="magma", shades=MAGMA, base=1, finish=0.5, body=0.5),
    # the same magma seen through the gaps between the shell's plates, and the seam where shell meets body
    dict(name="magma, shell cracks", shades=[5, 4], base=1, finish=0.5, body=0.5),
    # the dusky pink (10) where a gap narrows and at its rim: the dim end of the same glow
    dict(name="magma, crack edges", shades=[10], base=0, finish=0.5, body=0.5),
    # the shell: cooled, hardened crust. Plain stone, dead matte and solid. Base is the mid-dark gray (13)
    dict(name="rock", shades=ROCK, base=1, finish=0, body=0),
    # the fire out of the top of the shell
    dict(name="flame", shades=[5, 4, 3, 9, 7], base=1, finish=0, body=0),
    dict(name="seams and wrinkles", shades=[], finish=0, body=0),   # plate lines drawn in black inside the shell: tinted, never a crease
    # yellow eyeball, pale catchlight, dark pupil (and lid line when shut), the gray edge of the near eye
    dict(name="eye (line art)", shades=[14, 12, 10, 9, 7], finish=0.9, body=0),
]
INNER = "seams and wrinkles"
def to(name, colors): return {c: name for c in colors}
COLORS = {15: "outline", **to("magma", MAGMA), **to("rock", ROCK), 10: "magma, crack edges",
          **to("eye (line art)", [9, 7])}
RULES = [
    # in the shell pictures the reds are the gaps; black wholly inside the gray is a line on the one shell
    dict(drawings=["shell*"], colors=to("magma, shell cracks", [5, 4]), interior={15: (ROCK, INNER)}),
    dict(drawings=["fire*"], colors=to("flame", [5, 4, 3, 9, 7])),
    # the head has no rock: its grays and the one dusky pixel are the eyes' pupils and edges
    dict(drawings=["head", "head-eyes-*"], colors=to("eye (line art)", [14, 12, 10])),
]
# the shell's palest gray (11) is on few pixels, one lit plate at the top; left out of the row it stayed pale on a
# shell gone dark with the sun behind, so it stays a shade. The magma's pale patches (2) are left as painted: hot spots.
KEEP_TOP = ["rock"]
GLOW = [
    dict(material="flame", colors=[7], glow=245, intent="the flame's pale core is the brightest"),
    dict(material="flame", colors=[9], glow=230, intent="the flame's yellow"),
    dict(material="flame", colors=[3], glow=210, intent="the flame's orange middle"),
    dict(material="flame", colors=[4], glow=190, intent="the flame's red-orange body"),
    dict(material="flame", colors=[5], glow=180, intent="the flame's dark red edge is the dimmest"),
    dict(material="magma, shell cracks", colors=[4], glow=200, intent="magma in the gaps of the shell: the brightest part after the flame"),
    dict(material="magma, shell cracks", colors=[5], glow=130, intent="the gaps' dark rim"),
    dict(material="magma, crack edges", colors=[10], glow=90, intent="where a gap narrows the glow dims"),
    dict(material="magma", colors=[2], glow=34, intent="the body's hottest patches"),
    dict(material="magma", colors=[3], glow=24, intent="the body's lighter flow"),
    dict(material="magma", colors=[4], glow=16, intent="the body: as hot as lava, a dull red heat"),
    dict(material="magma", colors=[5], glow=8, intent="the body's dark contour and bubble rims"),
]
def AFTER(job):
    # the four flame drawings draw nearly the same amount of fire (131, 110, 110, 111 pixels), so the swing
    # is widened: the three smaller ones shine 0.86 of the biggest
    job.flicker(["fire"], low=0.1)
