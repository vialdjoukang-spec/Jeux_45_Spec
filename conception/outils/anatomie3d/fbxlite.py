"""Lecteur FBX binaire minimal : renvoie {nom: (sommets Nx3, triangles Mx3)} pour chaque Model portant une Geometry."""
import struct, zlib, numpy as np

def _val(b, p):
    t = chr(b[p]); p += 1
    if t in "YCFDLI":
        f = {"Y": "<h", "C": "<b", "F": "<f", "D": "<d", "L": "<q", "I": "<i"}[t]
        v = struct.unpack_from(f, b, p)[0]; return v, p + struct.calcsize(f)
    if t in "fdlib":
        n, enc, cl = struct.unpack_from("<III", b, p); p += 12
        raw = b[p:p + cl]; p += cl
        if enc: raw = zlib.decompress(raw)
        dt = {"f": "<f4", "d": "<f8", "l": "<i8", "i": "<i4", "b": "u1"}[t]
        return np.frombuffer(raw, dt, n), p
    if t in "SR":
        n = struct.unpack_from("<I", b, p)[0]; p += 4
        return bytes(b[p:p + n]), p + n
    raise ValueError(t)

def _node(b, p, v7):
    if v7: end, na, nl, ln = struct.unpack_from("<QQQB", b, p); p += 25
    else: end, na, nl, ln = struct.unpack_from("<IIIB", b, p); p += 13
    if end == 0: return None, p
    name = b[p:p + ln].decode(); p += ln
    props = []
    for _ in range(na):
        v, p = _val(b, p); props.append(v)
    kids = []
    while p < end:
        k, p = _node(b, p, v7)
        if k is None: break
        kids.append(k)
    return (name, props, kids), end

def lire(chemin):
    b = open(chemin, "rb").read(); ver = struct.unpack_from("<I", b, 23)[0]; v7 = ver >= 7500
    p = 27; top = []
    while p < len(b) - 100:
        n, p = _node(b, p, v7)
        if n is None: break
        top.append(n)
    obj = [x for x in top if x[0] == "Objects"][0][2]
    cons = [x for x in top if x[0] == "Connections"][0][2]
    geo, mod = {}, {}
    for name, pr, kids in obj:
        if name == "Geometry":
            d = {k[0]: k[1][0] for k in kids if k[0] in ("Vertices", "PolygonVertexIndex")}
            if "Vertices" in d: geo[pr[0]] = d
        elif name == "Model":
            mod[pr[0]] = pr[1].split(b"\x00")[0].decode("utf8", "replace")
    out = {}
    for c in cons:
        if c[0] == "C" and c[1][0] == b"OO":
            a, bb = c[1][1], c[1][2]
            if a in geo and bb in mod:
                d = geo[a]; V = d["Vertices"].reshape(-1, 3); idx = d["PolygonVertexIndex"].astype(np.int64)
                tris = []; cur = []
                for i in idx:
                    if i < 0: cur.append(~i); tris += [(cur[0], cur[j], cur[j + 1]) for j in range(1, len(cur) - 1)]; cur = []
                    else: cur.append(i)
                out[mod[bb]] = (V, np.array(tris, dtype=np.int64).reshape(-1, 3))
    return out


def _euler(rx, ry, rz):
    a, b, c = np.radians([rx, ry, rz])
    X = np.array([[1, 0, 0], [0, np.cos(a), -np.sin(a)], [0, np.sin(a), np.cos(a)]])
    Y = np.array([[np.cos(b), 0, np.sin(b)], [0, 1, 0], [-np.sin(b), 0, np.cos(b)]])
    Z = np.array([[np.cos(c), -np.sin(c), 0], [np.sin(c), np.cos(c), 0], [0, 0, 1]])
    return Z @ Y @ X   # ordre XYZ par défaut de FBX


def lire_monde(chemin):
    """Comme lire(), mais applique la hiérarchie Lcl (translation, rotation, échelle, pré-rotation) : coordonnées monde en mètres, Y vers le haut."""
    b = open(chemin, "rb").read(); v7 = struct.unpack_from("<I", b, 23)[0] >= 7500
    p = 27; top = []
    while p < len(b) - 100:
        n, p = _node(b, p, v7)
        if n is None: break
        top.append(n)
    obj = [x for x in top if x[0] == "Objects"][0][2]; cons = [x for x in top if x[0] == "Connections"][0][2]
    geo, mod, loc = {}, {}, {}
    for name, pr, kids in obj:
        if name == "Geometry":
            d = {k[0]: k[1][0] for k in kids if k[0] in ("Vertices", "PolygonVertexIndex")}
            if "Vertices" in d: geo[pr[0]] = d
        elif name == "Model":
            mod[pr[0]] = pr[1].split(b"\x00")[0].decode("utf8", "replace")
            t, r, s, pre = np.zeros(3), np.zeros(3), np.ones(3), np.zeros(3)
            for k in kids:
                if k[0] == "Properties70":
                    for q in k[2]:
                        nm = q[1][0]
                        if nm == b"Lcl Translation": t = np.array(q[1][4:7], float)
                        elif nm == b"Lcl Rotation": r = np.array(q[1][4:7], float)
                        elif nm == b"Lcl Scaling": s = np.array(q[1][4:7], float)
                        elif nm == b"PreRotation": pre = np.array(q[1][4:7], float)
            M = np.eye(4); M[:3, :3] = _euler(*pre) @ _euler(*r) @ np.diag(s); M[:3, 3] = t
            loc[pr[0]] = M
    parent = {}; gm = {}
    for c in cons:
        if c[0] == "C" and c[1][0] == b"OO":
            a, bb = c[1][1], c[1][2]
            if a in mod and bb in mod: parent[a] = bb
            if a in geo and bb in mod: gm[bb] = a
    cache = {}
    def monde(i):
        if i not in cache:
            cache[i] = (monde(parent[i]) if i in parent else np.eye(4)) @ loc[i]
        return cache[i]
    out = {}
    for mid, gid in gm.items():
        d = geo[gid]; V = d["Vertices"].reshape(-1, 3); idx = d["PolygonVertexIndex"].astype(np.int64)
        tris = []; cur = []
        for i in idx:
            if i < 0:
                cur.append(~i); tris += [(cur[0], cur[j], cur[j + 1]) for j in range(1, len(cur) - 1)]; cur = []
            else: cur.append(i)
        W = monde(mid); Vw = (np.c_[V, np.ones(len(V))] @ W.T)[:, :3]
        out[mod[mid]] = (Vw, np.array(tris, dtype=np.int64).reshape(-1, 3))
    return out
