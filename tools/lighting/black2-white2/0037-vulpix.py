SOURCE = "sources/black2-white2/0037-vulpix.spu"
MATERIALS = [
    # black line; lines between overlapping tails and locks (dark red); the dark brown line along the ears and
    # hind leg, and the mouth and nose lines
    dict(name="outline", shades=[4, 15, 11], finish=0.1, body=0),
    # head, ears, body and legs: a sleek coat the art paints flat. Its dark red contour is its darkest shade;
    # the back view is wholly in 14, so that is the base
    dict(name="short fur", shades=[11, 14, 13], base=1, finish=-0.2, body=0.05),
    # the pale brow, muzzle top and ear fronts (front view only, few pixels): the same coat where the art lights
    # it most. Its own row, so it goes dark with the head and the coat's row keeps the body's color as its top
    dict(name="short fur, brow and muzzle", shades=[14, 13, 12], base=2, finish=-0.2, body=0.05),
    # the top edge of each ear, drawn in red-brown: the coat's contour on its lit side
    dict(name="short fur, ear edges", shades=[11, 10], base=1, finish=-0.2, body=0.05),
    # the cream chest and belly: the same coat, paler. Seen from behind it is edged in the coat's dark red,
    # its darkest shade, so it goes dark with the body
    dict(name="short fur, cream", shades=[11, 3, 2], base=1, finish=-0.2, body=0.05),
    # the dark brown socks on all four feet
    dict(name="short fur, paws", shades=[15, 7, 6], base=1, finish=-0.2, body=0.05),
    dict(name="short fur, ear insides", shades=[15, 7, 6], base=1, finish=-0.2, body=0.05),
    # the six tails and the curled locks on the head. Black 2/White 2: "As each tail grows, its fur becomes
    # more lustrous."; the art paints a pale patch on every tail and lock
    dict(name="glossy fur", shades=[11, 10, 9, 8], base=1, finish=0.3, body=0.05),
    dict(name="eye (line art)", shades=[4, 15, 6, 1], finish=0.9, body=0),
]
def to(name, colors): return {c: name for c in colors}
COAT, PAWS, EAR, LOCKS, EYE = "short fur", "short fur, paws", "short fur, ear insides", "glossy fur", "eye (line art)"
EDGE = "short fur, ear edges"
COLORS = {4: "outline", **to(LOCKS, [11, 10, 9, 8]), **to(COAT, [14, 13]), 12: "short fur, brow and muzzle", **to("short fur, cream", [3, 2]),
          **to(PAWS, [15, 7, 6]), 1: EYE}
OVERLAP = {11: ([10, 9, 8], "outline")}        # a dark line wholly inside the tails or locks: one lies over another
RULES = [
    # tails and locks: the lines between them are creases; their outer contour stays their darkest shade
    dict(drawings=["kami", "atama-k", "o01", "o2", "o3", "shippo*"], interior=OVERLAP),
    # body and legs: the dark red contour is the coat's; a line wholly inside (leg over body) is a crease
    dict(drawings=["karada", "b-momo", "b-ashi0*", "r-ashi", "mimi", "usiroasi*", "image-3", "asi2", "maeashi"],
         colors={11: COAT}, interior={11: ([14, 13, 12, 3, 2], "outline")}),
    # the dark brown line on the hind thigh and down the hind leg above the sock
    dict(view="front", drawings=["b-momo"], colors={15: "outline"}),
    dict(view="front", drawings=["b-ashi02"], rect=[0, 1, 16, 4], colors={15: "outline"}),
    # front head: coat contour, the dark brown line around the ears, the mouth and the nose's edge, the ears'
    # red-brown top edge, the brown inside of the right ear
    dict(view="front", drawings=["atama"], colors={11: COAT, 15: "outline", 10: EDGE, 7: EAR, 6: EAR}),
    dict(view="front", drawings=["atama"], rect=[25, 6, 4, 3], colors={15: EAR}),
    dict(view="front", drawings=["atama"], rect=[21, 9, 4, 4], colors={15: EAR}),
    dict(view="front", drawings=["atama"], rect=[20, 13, 1, 1], colors={15: EAR}),
    dict(view="front", drawings=["atama"], rect=[23, 15, 3, 1], colors={15: EAR}),
    # the locks in front of the ears
    dict(view="front", drawings=["atama"], rect=[8, 6, 11, 9], colors=to(LOCKS, [11, 10]), interior=OVERLAP),
    # the eye: black ring, brown iris and its lighter part, white catchlight; shut, it is a drawn line
    dict(drawings=["atama-eyes-open"], colors=to(EYE, [4, 15, 6, 1])),
    dict(drawings=["atama-eyes-closed"], colors={15: "outline"}),
    # back head: coat contour, the line under the ear, the far ear's red-brown edge; then the locks on top
    dict(view="back", drawings=["atama"], colors={11: COAT, 10: EDGE}, interior={11: ([14, 13, 12], "outline")}),
    dict(view="back", drawings=["atama"], rect=[9, 9, 15, 8], colors=to(LOCKS, [11, 10]), interior=OVERLAP),
]
# the pale front of the locks is few pixels: kept in its row so it goes dark with them
KEEP_TOP = ["glossy fur"]
