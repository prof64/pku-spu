#!/usr/bin/env python3
"""Light a library sprite: say what every pixel is made of, then let Smeargle work out the rest.

    tools/light.py plan  sources/black2-white2/0007-squirtle.spu plan.png   every drawing, each pixel's color number written on it
    tools/light.py apply tools/lighting/black2-white2/0007-squirtle.py out.spu
    tools/light.py check out.spu          pixels light alone gets wrong (must be 0, in every look), rows nothing uses
    tools/light.py sheet out.spu sheet.png    front and back in every place, the material map and its legend

Every change goes through Smeargle's tools (the `smeargle` command must be on PATH), so it is in the
sprite's history and can be watched live. docs/materials.md says how the materials are chosen.

A sprite's lighting is written down as a small Python file in tools/lighting/<collection>/:

  SOURCE      the sprite to start from, relative to this repository (or a list: the first that exists).
              One that already has lighting is stripped of it first.
  MATERIALS   [dict(name, shades, finish, body, base)], the outline first. shades are color numbers,
              darkest first; base is the shade a surface facing the viewer shows (the color most of
              its lit side is painted in, not its shadow).
  COLORS      {color: material}: what each color is, wherever nothing below says otherwise
  THIN        {color: "outline"}: optional, and not used by the first ten (docs/materials.md says
              why a surface's dark contour stays one of its shades). A stroke one pixel wide in
              that color running along the outside or another surface goes in the outline row;
              inside its own surface it goes in the row INNER names.
  INNER       the name of the row with no shades for lines inside a surface (seams drawn in black):
              light only tints it, and it does not crease the shape
  RULES       [dict(view=?, drawings=[patterns]?, rect=[x, y, w, h]?, colors={...}, thin={...},
              thin_all={...}, interior={color: ([surface colors], material)})]: the same, for some
              drawings only; later rules win. thin_all makes every one-pixel stroke a line (petals,
              lobes, a caterpillar's segments: pieces that overlap). interior picks pixels wholly
              inside a surface (seams drawn in black).
  FLOODS      [dict(view, drawing, seeds=[[x, y]], through=[colors], colors={...})]: the touching
              region from a pixel, for two surfaces that share colors in one drawing
  MARKS       [dict(drawings, color, on=[colors around], to=material, max=pixels)]: a patch of a
              darker color wholly inside lighter skin is a marking, with its own row
  KEEP_TOP    [row names] whose lightest shade stays in the row although few pixels use it (see glints)
  AREAS, GLOW lists of arguments for assign_material and set_glow
  AFTER(job)  anything else: job.flicker([parts]) ties a flame's glow to its drawn flicker
"""
import sys, os, json, shutil, fnmatch, io, base64, subprocess, types, collections

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

def _client():
    out = subprocess.run([os.environ.get("SMEARGLE", "smeargle"), "python"], capture_output=True, text=True)
    if out.returncode != 0:
        sys.exit("The `smeargle` command is needed (Smeargle's engine): " + out.stderr.strip())
    mod = types.ModuleType("smeargle"); exec(out.stdout, mod.__dict__); return mod

_smeargle = _client()
Sprite, SmeargleError = _smeargle.Sprite, _smeargle.SmeargleError

def source(spec):
    names = spec.SOURCE if isinstance(spec.SOURCE, (list, tuple)) else [spec.SOURCE]
    for n in names:
        p = n if os.path.isabs(n) else os.path.join(ROOT, n)
        if os.path.exists(p): return p
    sys.exit(f"None of {names} exists")

def grid(rows):
    return [[None if t == "." else int(t) for t in r.split()] for r in rows]

def thin_mask(g, color):
    """Pixels of `color` that are in no 2x2 block of that color: a stroke one pixel wide."""
    h = len(g); w = len(g[0]) if h else 0
    broad = [[False]*w for _ in range(h)]
    for y in range(h-1):
        for x in range(w-1):
            if g[y][x] == color and g[y][x+1] == color and g[y+1][x] == color and g[y+1][x+1] == color:
                broad[y][x] = broad[y][x+1] = broad[y+1][x] = broad[y+1][x+1] = True
    return [[g[y][x] == color and not broad[y][x] for x in range(w)] for y in range(h)]

def regions(g, color):
    h = len(g); w = len(g[0]) if h else 0
    seen = [[False]*w for _ in range(h)]; out = []
    for y in range(h):
        for x in range(w):
            if g[y][x] == color and not seen[y][x]:
                st = [(x, y)]; seen[y][x] = True; reg = []
                while st:
                    a, b = st.pop(); reg.append((a, b))
                    for dx, dy in ((1,0),(-1,0),(0,1),(0,-1)):
                        p, q = a+dx, b+dy
                        if 0 <= p < w and 0 <= q < h and not seen[q][p] and g[q][p] == color:
                            seen[q][p] = True; st.append((p, q))
                out.append(reg)
    return out

class Job:
    def __init__(self, spec, out):
        self.spec = spec
        os.makedirs(os.path.dirname(os.path.abspath(out)), exist_ok=True)
        shutil.copyfile(source(spec), out)
        self.s = Sprite(out, agent="Claude Code"); self.out = out
        self.o = self.s.overview()
        self.views = [v["id"] for v in self.o["views"]]
        self.pal = self.o["palettes"][0]["colors"]

    def per_view(self, d, view):
        if d and all(isinstance(k, str) for k in d): return d.get(view, {})
        return d or {}

    def strip(self):
        s = self.s
        o = s.overview()
        if not o["materials"]: return
        for v in self.views:
            try: s.clear_light(view=v, intent="start the lighting over")
            except SmeargleError as e: print("clear", v, e)
        for m in reversed(s.overview()["materials"]):
            try: s.remove_material(material=m["index"], intent="start the lighting over")
            except SmeargleError as e: print("remove", m["name"], e)

    def materials(self):
        for m in self.spec.MATERIALS:
            kw = dict(name=m["name"], shades=m["shades"], finish=m.get("finish", 0), body=m.get("body", 0), assign=False,
                      intent=m.get("why", f"{m['name']}: its shades and finish"))
            if m.get("base") is not None: kw["base"] = m["base"]
            self.s.add_material(**kw)
        self.index = {m["name"]: m["index"] for m in self.s.overview()["materials"]}

    def paint(self):
        sp = self.spec; calls = []; self.grids = {}; self.mgrids = {}
        for d in self.s.overview()["drawings"]:
            for view in d["pictures"]:
                g = grid(self.s.read_picture(drawing=d["id"], view=view)["rows"])
                self.grids[(view, d["id"])] = g
                h = len(g); w = len(g[0]) if h else 0
                m = [[None]*w for _ in range(h)]
                INNER = getattr(sp, "INNER", None)
                def apply(colors, thin, rect=None):
                    x0, y0, x1, y1 = (0, 0, w, h) if not rect else (rect[0], rect[1], rect[0]+rect[2], rect[1]+rect[3])
                    for y in range(max(0, y0), min(h, y1)):
                        for x in range(max(0, x0), min(w, x1)):
                            c = g[y][x]
                            if c is not None and c in colors: m[y][x] = colors[c]
                    # A stroke one pixel wide in a surface's dark color is its drawn contour where it runs along
                    # something else (the outside, another surface); inside its own surface it is a seam or a
                    # wrinkle, which stays that surface's shade so it does not crease the shape.
                    snap = [r[:] for r in m]
                    for c, name in (thin or {}).items():
                        t = thin_mask(g, c)
                        for y in range(max(0, y0), min(h, y1)):
                            for x in range(max(0, x0), min(w, x1)):
                                if not t[y][x]: continue
                                own = snap[y][x]; foreign = False
                                for dy in (-1, 0, 1):
                                    for dx in (-1, 0, 1):
                                        p, q = x+dx, y+dy
                                        if not (0 <= p < w and 0 <= q < h) or g[q][p] is None: foreign = True
                                        elif snap[q][p] not in (own, name) and not (snap[q][p] or "").startswith("outline"): foreign = True
                                if foreign: m[y][x] = name
                                elif INNER: m[y][x] = INNER
                def snapshot_thin(thin, region):
                    snap = [r[:] for r in m]
                    for c, name in thin.items():
                        tm = thin_mask(g, c)
                        for (x, y) in region:
                            if not tm[y][x]: continue
                            own = snap[y][x]; foreign = False
                            for dy in (-1, 0, 1):
                                for dx in (-1, 0, 1):
                                    p, q = x+dx, y+dy
                                    if not (0 <= p < w and 0 <= q < h) or g[q][p] is None: foreign = True
                                    elif snap[q][p] not in (own, name) and not (snap[q][p] or "").startswith("outline"): foreign = True
                            if foreign: m[y][x] = name
                            elif INNER: m[y][x] = INNER
                def interior(spec_):
                    # a pixel of `color` whose neighbors (all eight) are only that color or the surface's own colors
                    # is a line drawn inside the surface (a seam, a wrinkle), not its contour
                    for c, (inside, name) in (spec_ or {}).items():
                        ok = set(inside) | {c}
                        for y in range(h):
                            for x in range(w):
                                if g[y][x] != c: continue
                                good = True
                                for dy in (-1, 0, 1):
                                    for dx in (-1, 0, 1):
                                        p, q = x+dx, y+dy
                                        if not (0 <= p < w and 0 <= q < h) or g[q][p] not in ok: good = False
                                if good: m[y][x] = name
                apply(self.per_view(sp.COLORS, view), self.per_view(getattr(sp, "THIN", {}), view))
                for r in getattr(sp, "RULES", []):
                    if r.get("view") and r["view"] != view: continue
                    if r.get("drawings") and not any(fnmatch.fnmatch(d["id"], p) for p in r["drawings"]): continue
                    apply(r.get("colors", {}), r.get("thin"), r.get("rect"))
                    interior(r.get("interior"))
                    # lines between overlapping pieces (petals, lobes): every stroke one pixel wide is a drawn line
                    for c, name in (r.get("thin_all") or {}).items():
                        tm = thin_mask(g, c)
                        for y in range(h):
                            for x in range(w):
                                if tm[y][x]: m[y][x] = name
                for fl in getattr(sp, "FLOODS", []):
                    if fl.get("view") and fl["view"] != view: continue
                    if fl["drawing"] != d["id"]: continue
                    thr = set(fl["through"]); st = [tuple(p) for p in fl["seeds"]]; seen = set()
                    while st:
                        a, b = st.pop()
                        if (a, b) in seen or not (0 <= a < w and 0 <= b < h) or g[b][a] not in thr: continue
                        seen.add((a, b))
                        if g[b][a] in fl["colors"]: m[b][a] = fl["colors"][g[b][a]]
                        st += [(a+1, b), (a-1, b), (a, b+1), (a, b-1)] + ([(a+1, b+1), (a-1, b-1), (a+1, b-1), (a-1, b+1)] if fl.get("diagonal") else [])
                    if not seen: print("  flood found nothing:", fl)
                    if fl.get("thin"):
                        snapshot_thin(fl["thin"], seen)
                for k in getattr(sp, "MARKS", []):
                    if k.get("view") and k["view"] != view: continue
                    if k.get("drawings") and not any(fnmatch.fnmatch(d["id"], p) for p in k["drawings"]): continue
                    for reg in regions(g, k["color"]):
                        if len(reg) > k.get("max", 40) or len(reg) < k.get("min", 2): continue
                        ok = True; rs = set(reg)
                        for (a, b) in reg:
                            for dx, dy in ((1,0),(-1,0),(0,1),(0,-1)):
                                p, q = a+dx, b+dy
                                if (p, q) in rs: continue
                                if not (0 <= p < w and 0 <= q < h) or g[q][p] not in k["on"]: ok = False
                        if ok:
                            for (a, b) in reg: m[b][a] = k["to"]
                self.mgrids[(view, d["id"])] = m
                rows = []; any_ = False; missing = set()
                for y in range(h):
                    row = []
                    for x in range(w):
                        if g[y][x] is None: row.append(".")
                        elif m[y][x] is None: missing.add(g[y][x]); row.append(".")
                        else: row.append(str(self.index[m[y][x]])); any_ = True
                    rows.append(" ".join(row))
                if missing: print(f"  no material for colors {sorted(missing)} in {view}/{d['id']}")
                if any_: calls.append({"tool": "paint_light", "args": {"drawing": d["id"], "view": view, "layer": "material", "rows": rows}})
        self.s.batch(calls=calls, intent="say what every pixel is made of")
        for a in getattr(sp, "AREAS", []):
            kw = dict(a); kw.setdefault("intent", f"{a['material']}: the pixels that are it")
            self.s.assign_material(**kw)

    def glow(self):
        for g in getattr(self.spec, "GLOW", []):
            kw = dict(g); kw.setdefault("intent", "what gives off light")
            self.s.set_glow(**kw)

    def flicker(self, parts, low=0.8):
        """A flame's glow follows its drawn flicker: each drawing shines in proportion to how much fire it draws."""
        s = self.s; size = {}
        for (view, d), g in self.grids.items():
            mg = self.mgrids[(view, d)]
            size[d] = sum(1 for y, row in enumerate(g) for x, c in enumerate(row) if c is not None and mg[y][x] and "flame" in mg[y][x])
        for a in s.overview()["animations"]:
            an = s.read_animation(animation=a["id"])
            for view, vd in an["views"].items():
                for t in vd["tracks"]:
                    if not any(fnmatch.fnmatch(t["part"], p) for p in parts): continue
                    keys = [k for k in (t.get("drawings") or []) if k[1]]
                    if len(keys) < 2: continue
                    big = max(size.get(k[1], 0) for k in keys) or 1
                    em = [[k[0], round(low + (1 - low)*size.get(k[1], 0)/big, 2), "step"] for k in keys]
                    s.set_track(animation=a["id"], view=view, part=t["part"], emission=em, intent="the flame's glow flickers with its drawn flicker")

    def drop_animation(self, name, why):
        for a in self.s.overview()["animations"]:
            if a["id"] == name: self.s.remove_animation(animation=name, intent=why)

    def bake(self):
        r = self.s.bake_facing(intent="work out which way every pixel faces from the art")
        return r

    def unused(self):
        """Take out rows no pixel ended up in."""
        used = collections.Counter()
        for d in self.s.overview()["drawings"]:
            for view in d["pictures"]:
                for row in grid(self.s.read_picture(drawing=d["id"], view=view, layer="material")["rows"]):
                    used.update(c for c in row if c is not None)
        for m in reversed(self.s.overview()["materials"]):
            if not used[m["index"]] and m["index"] != 0:
                self.s.remove_material(material=m["index"], intent=f"no pixel is {m['name']}")

    def glints(self, share=0.07):
        """A surface's lightest color that the art uses on only a few of its pixels is a painted glint,
        not a shade: it is taken out of the row (those pixels then stay as painted), so another light
        cannot spread it over a third of the surface. Rows a spec lists in KEEP_TOP, polished rows
        (finish 0.6 and up) and rows of two shades are left alone."""
        keep = set(getattr(self.spec, "KEEP_TOP", []))
        count = collections.Counter()
        for d in self.s.overview()["drawings"]:
            for view in d["pictures"]:
                g = grid(self.s.read_picture(drawing=d["id"], view=view)["rows"])
                mg = grid(self.s.read_picture(drawing=d["id"], view=view, layer="material")["rows"])
                for y, row in enumerate(g):
                    for x, c in enumerate(row):
                        if c is not None: count[(mg[y][x], c)] += 1
        for m in self.s.overview()["materials"]:
            sh = m["shades"]
            if m["line"] or len(sh) < 3 or m["finish"] >= 0.6 or m["name"] in keep or m["base"] >= len(sh) - 1: continue
            total = sum(count[(m["index"], c)] for c in sh)
            if total and count[(m["index"], sh[-1])] / total < share:
                # the base is given again: changing a row's shades alone makes Smeargle pick a new base
                self.s.update_material(material=m["index"], shades=sh[:-1], base=m["base"],
                                       intent=f"{m['name']}: its lightest color is a painted glint, not a shade")

    def run(self):
        self.strip(); self.materials(); self.paint(); self.unused(); self.glints(); self.glow()
        if hasattr(self.spec, "AFTER"): self.spec.AFTER(self)
        r = self.bake()
        c = self.s.check()
        if c.get("problem"): print("  problem:", c["problem"])
        return self

# ---------------------------------------------------------------------------------------------
# Looking: the pictures to plan from and to check with
# ---------------------------------------------------------------------------------------------

def _pil():
    try:
        from PIL import Image, ImageDraw, ImageFont
    except ImportError:
        sys.exit("plan and sheet need Pillow (pip install pillow)")
    return Image, ImageDraw, ImageFont

def _font(size):
    _, _, ImageFont = _pil()
    for p in ("/System/Library/Fonts/Menlo.ttc", "/System/Library/Fonts/Monaco.ttf", "/usr/share/fonts/truetype/dejavu/DejaVuSansMono.ttf"):
        try: return ImageFont.truetype(p, size)
        except Exception: pass
    return ImageFont.load_default()

def _rgb(h): return tuple(int(h[i:i+2], 16) for i in (1, 3, 5))

def plan(spu, out, cell=9):
    """Every drawing of every view as a tile, each pixel in its color with its color number (hex) on it."""
    Image, ImageDraw, _ = _pil()
    s = Sprite(spu); o = s.overview(); pal = [_rgb(c) for c in o["palettes"][0]["colors"]]
    f, small = _font(cell-2), _font(7); tiles = []
    for d in o["drawings"]:
        for v in d["pictures"]:
            g = grid(s.read_picture(drawing=d["id"], view=v)["rows"]); h = len(g); w = len(g[0]) if h else 0
            ys = [y for y in range(h) if any(c is not None for c in g[y])]
            xs = [x for x in range(w) if any(g[y][x] is not None for y in range(h))]
            if not ys: continue
            x0, x1, y0, y1 = min(xs), max(xs)+1, min(ys), max(ys)+1
            im = Image.new("RGB", (max((x1-x0)*cell+22, 150), (y1-y0)*cell+26), (58, 58, 80)); dr = ImageDraw.Draw(im)
            dr.text((2, 1), f"{v}/{d['id']}", fill=(255, 255, 0))
            for y in range(y0, y1):
                if (y-y0) % 2 == 0: dr.text((1, 26+(y-y0)*cell-1), str(y), fill=(200, 200, 120), font=small)
                for x in range(x0, x1):
                    c = g[y][x]
                    if c is None: continue
                    X, Y = 22+(x-x0)*cell, 26+(y-y0)*cell
                    dr.rectangle([X, Y, X+cell-1, Y+cell-1], fill=pal[c])
                    dr.text((X+2, Y-1), "%x" % c if c < 16 else "+", fill=(0, 0, 0) if sum(pal[c]) > 380 else (255, 255, 255), font=f)
            for x in range(x0, x1):
                if (x-x0) % 4 == 0: dr.text((22+(x-x0)*cell, 14), str(x), fill=(200, 200, 120), font=small)
            tiles.append(im)
    width = 1500; x = y = rowh = 0; pos = []
    for t in tiles:
        if x + t.width > width: x = 0; y += rowh + 6; rowh = 0
        pos.append((x, y)); x += t.width + 6; rowh = max(rowh, t.height)
    legend = 16
    img = Image.new("RGB", (width, y + rowh + legend + 4), (30, 30, 34)); dr = ImageDraw.Draw(img)
    for t, p in zip(tiles, pos): img.paste(t, p)
    use = {u["color"]: sum(u["pixels"].values()) for u in s.color_usage()}
    for i, c in enumerate(o["palettes"][0]["colors"]):
        X = 4 + i*92
        if X + 90 > width: break
        dr.rectangle([X, y+rowh+4, X+10, y+rowh+14], fill=_rgb(c)); dr.text((X+13, y+rowh+3), f"{i:x} {c} {use.get(i, 0)}", fill=(230, 230, 230), font=small)
    img.save(out); return out

PLACES = [("art", dict(mode="color", place="studio")), ("field", dict(place="field")), ("studio", dict(place="studio")),
          ("cave", dict(place="cave")), ("rain", dict(place="rain")), ("sun behind", dict(place="field", light=[0.3, 0.4, -1])),
          ("lamp right", dict(place="studio", light=[1, 0.3, 0.6])), ("material", dict(mode="material", place="studio"))]

def _hue(h):
    f = lambda o: min(1, max(0, abs(((h+o) % 1)*6 - 3) - 1))
    return (f(0), f(0.667), f(0.333))

def sheet(spu, out, scale=3):
    """Front and back in every place, the art beside them, then the material map and its legend."""
    Image, ImageDraw, _ = _pil()
    s = Sprite(spu); o = s.overview(); rows = []; tmp = out + ".part.png"
    for v in o["views"]:
        row = []
        for name, kw in PLACES:
            s.render_lit(view=v["id"], scale=scale, png=tmp, **kw); row.append((name, Image.open(tmp).convert("RGB").copy()))
        rows.append(row)
    os.remove(tmp)
    cw = [max(r[i][1].width for r in rows) for i in range(len(PLACES))]; rh = [max(im.height for _, im in r) for r in rows]
    img = Image.new("RGB", (sum(cw) + 4*len(PLACES) + 250, max(sum(rh) + 14*len(rows), 16*len(o["materials"]) + 8)), (40, 40, 44)); d = ImageDraw.Draw(img); y = 0
    for r, h in zip(rows, rh):
        x = 0
        for (name, im), w in zip(r, cw):
            d.text((x+2, y+1), name, fill=(220, 220, 220)); img.paste(im, (x, y+14)); x += w + 4
        y += h + 14
    x = sum(cw) + 4*len(PLACES) + 6
    for m in o["materials"]:
        c = (20, 20, 20) if m["line"] else tuple(int(255*(0.0625 + 0.75*k)) for k in _hue(m["index"]*0.618 + 0.05))
        d.rectangle([x, 4+16*m["index"], x+12, 16+16*m["index"]], fill=c)
        d.text((x+18, 4+16*m["index"]), f"{m['name']} {m['finish']:.2f}/{m['body']:.2f}", fill=(240, 240, 240))
    img.save(out); return out

def check(spu):
    """Pixels where the lighting data alone does not give back the art (every look), and material rows no pixel uses."""
    Image, _, _ = _pil()
    s = Sprite(spu); o = s.overview(); names = [m["name"] for m in o["materials"]]; use = collections.Counter()
    for d in o["drawings"]:
        for v in d["pictures"]:
            g = grid(s.read_picture(drawing=d["id"], view=v)["rows"]); mg = grid(s.read_picture(drawing=d["id"], view=v, layer="material")["rows"])
            for y, row in enumerate(g):
                for x, c in enumerate(row):
                    if c is not None: use[mg[y][x]] += 1
    misses = {}
    for v in o["views"]:
        for look in [[]] + [[x["id"]] for x in o["variants"]]:
            kw = dict(mode="misses", place="studio", background=False, scale=1, view=v["id"])
            if look: kw["variants"] = look
            im = Image.open(io.BytesIO(base64.b64decode(s.render_lit(**kw)["image"].split(",", 1)[1]))).convert("RGB")
            n = sum(1 for p in (im.get_flattened_data() if hasattr(im, "get_flattened_data") else im.getdata()) if p[0] > 220 and p[1] < 80 and p[2] > 170)
            misses[v["id"] + ("+" + look[0] if look else "")] = n
    unused = [names[i] for i in range(len(names)) if use[i] == 0]
    problem = s.check().get("problem")
    ok = not any(misses.values()) and not unused and not problem
    print(os.path.basename(spu), "ok" if ok else "NOT OK", "| misses", {k: v for k, v in misses.items() if v} or 0, "| unused rows", unused or "none", "| problem", problem)
    return ok

def load(path):
    import importlib.util
    spec = importlib.util.spec_from_file_location("lighting_" + os.path.basename(path)[:-3].replace("-", "_"), path)
    m = importlib.util.module_from_spec(spec); spec.loader.exec_module(m); return m

def main():
    a = sys.argv[1:]
    if len(a) >= 3 and a[0] == "plan": print(plan(a[1], a[2]))
    elif len(a) >= 3 and a[0] == "apply":
        Job(load(a[1]), a[2]).run(); sys.exit(0 if check(a[2]) else 1)
    elif len(a) >= 2 and a[0] == "check": sys.exit(0 if all([check(f) for f in a[1:]]) else 1)
    elif len(a) >= 3 and a[0] == "sheet": print(sheet(a[1], a[2]))
    else: sys.exit(__doc__)

if __name__ == "__main__":
    main()
