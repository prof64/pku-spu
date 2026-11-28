# Mr. Mime: bare matte skin (Hide) everywhere: the pink head and limbs, the white torso, hands and knee caps, the
# red balls at shoulders and hips, the red cheeks, belly spot and finger pads, the blue curled feet. The blue
# tufts on the head are hair with a smooth edge (a short coat). No Pokédex entry names any surface; all from the art.
SOURCE = "sources/black2-white2/0122-mr-mime.spu"
H = dict(finish=0.25, body=0.08)          # Hide: plain bare skin
MATERIALS = [
    # black; the lines between fingers and round the knee caps (navy 3, blue 2); the pink skin's brown contour (12)
    # and the white's blue one (2): the palette has no step between those pale surfaces and their contours, and
    # as their darkest shades they spread over the back of the head and the torso in brown and blue wedges
    dict(name="outline", shades=[14, 3, 4, 8, 12, 2], finish=0.1, body=0),
    # pink skin: head, arms, shins; both views together are mostly 11
    dict(name="hide", shades=[11, 10], base=0, **H),
    # the palest pixels on the forehead: the same skin at its most lit, in their own row so they go dark with the head
    dict(name="hide, lit patches", shades=[11, 10, 9], base=0, **H),
    # the red cheeks: color in the same skin
    dict(name="hide, cheeks", shades=[7, 6], base=1, **H),
    # white torso, hands and knee caps: mostly painted in the light gray, white where lit
    dict(name="hide, white", shades=[1, 15], base=0, **H),
    # the red spot on the belly: color in the torso's skin
    dict(name="hide, belly spot", shades=[7, 6, 5], base=1, **H),
    # the red balls at shoulders and hips; the maroon contour is its darkest shade
    dict(name="hide, joints", shades=[8, 7, 6], base=1, **H),
    # the red pad on each fingertip
    dict(name="hide, finger pads", shades=[7, 6], base=1, **H),
    # the blue curled feet
    dict(name="hide, feet", shades=[4, 3, 2], base=1, **H),
    # the two blue tufts: hair, drawn smooth-edged and flat
    dict(name="short fur, hair", shades=[4, 3, 2], base=1, finish=-0.2, body=0.05),
    dict(name="mouth", shades=[13], base=0, finish=0.8, body=0),
    dict(name="eye (line art)", shades=[12, 14, 15], finish=0.9, body=0),
]
def to(name, colors): return {c: name for c in colors}
COLORS = {**to("outline", [14, 3, 4, 12, 2]), **to("hide", [11, 10]), 9: "hide, lit patches",
          **to("hide, white", [1, 15]), **to("hide, joints", [8, 7, 6]), 5: "hide, belly spot", 13: "mouth"}
RULES = [
    # head, both views: the tufts, the cheeks; the chin's contour is drawn in maroon
    dict(drawings=["haed", "head"], colors={**to("short fur, hair", [4, 3, 2]), 6: "hide, cheeks", 8: "outline"}),
    # the open mouth lies over the cheek's edge
    dict(drawings=["mouse-2"], colors={7: "hide, cheeks"}),
    # torso: the belly spot; one maroon contour pixel by the shoulder
    dict(drawings=["body"], colors={**to("hide, belly spot", [7, 6, 5]), 8: "outline"}),
    # arms and one shin: their contour beside a red ball is drawn in the ball's maroon
    dict(drawings=["ude", "ude-r"], colors={8: "outline"}),
    dict(view="front", drawings=["leg-r2"], rect=[12, 14, 1, 1], colors={8: "outline"}),
    # hands: the fingertip pads
    dict(drawings=["hand*"], colors={6: "hide, finger pads"}),
    # feet; the navy at the top of the ankle is the knee cap's line
    dict(drawings=["foot-*"], colors=to("hide, feet", [4, 3, 2])),
    dict(view="back", drawings=["foot-r"], rect=[7, 4, 1, 1], colors={3: "outline"}),
    dict(view="back", drawings=["foot-l"], rect=[7, 3, 4, 2], colors={3: "outline"}),
    # eyes: white, pupil and the brown rim
    dict(drawings=["haed-eyes-open"], colors=to("eye (line art)", [15, 14, 12])),
]
KEEP_TOP = ["hide, belly spot"]
