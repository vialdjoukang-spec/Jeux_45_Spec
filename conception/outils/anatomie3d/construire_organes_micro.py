"""Derniers organes de la Tétrade, un .glb par organe, 0 token, fusionnés dans anatomie3d/index.json.
Deux voies :
  - « bp3d »       : maillages réels BodyParts3D (CC BY-SA 2.1 JP), organes génitaux internes isolés, à but strictement
                     didactique (décision de Vial du 26.11.2026) : modèle d'atlas, jamais placé sur un corps entier ;
  - « procedural » : modèle 3D scientifique reconstruit par code (trimesh) à partir de dimensions publiées et citées
                     (cellules et structures microscopiques que le scanner ne voit pas). Jamais de SVG.
Chaque entrée porte « nature » (réel ou reconstruit), « unite » et « echelle ». Cache : empreinte (dimensions + code) inchangée
et .glb présent → organe sauté. Dépendances : pip install trimesh fast-simplification. Signature : AAI (Anthropic AI)"""
import hashlib, json, os, subprocess

import numpy as np, trimesh
from scipy.sparse.csgraph import minimum_spanning_tree
from scipy.spatial import cKDTree

ICI = os.path.dirname(os.path.abspath(__file__)); RAC = os.path.dirname(os.path.dirname(os.path.dirname(ICI)))
SORTIE = os.path.join(RAC, "conception", "prototypes", "moteur", "anatomie3d"); IDX = os.path.join(SORTIE, "index.json")
BP = "/tmp/bp3d"; D = BP + "/assets/BodyParts3D_data/stl/"
CODE = hashlib.sha256(open(__file__, "rb").read()).hexdigest()[:12]
ROUGE, ROSE, BLEU, VIOLET, JAUNE, BEIGE = [178, 34, 52], [222, 150, 150], [70, 110, 190], [110, 60, 150], [225, 200, 90], [235, 205, 170]


def coul(m, c):
    m.visual = trimesh.visual.ColorVisuals(m, face_colors=list(c) + [255]); return m


def tube(points, r, c, sections=16):
    """Tube lisse le long d'une polyligne (vaisseau, canal) : un cylindre et une sphère par segment."""
    out = []
    for a, b in zip(points[:-1], points[1:]):
        out.append(trimesh.creation.cylinder(radius=r, segment=[a, b], sections=sections))
    out += [trimesh.creation.icosphere(2, radius=r).apply_translation(p) for p in points]
    return coul(trimesh.util.concatenate(out), c)


def stl_bp3d(fmas):
    """Charge des maillages BodyParts3D (repère mm, Z haut, face vers -Y, gauche du patient vers +X), en ne tirant que les STL manquants."""
    manque = [f for f in fmas if not os.path.exists(D + f + ".stl")]
    if manque:
        if not os.path.isdir(BP):
            subprocess.run(["git", "clone", "-q", "--filter=blob:none", "--no-checkout", "https://github.com/Kevin-Mattheus-Moerman/BodyParts3D.git", BP], check=True)
        subprocess.run(["git", "-C", BP, "-c", "gc.auto=0", "checkout", "HEAD", "--"] + [f"assets/BodyParts3D_data/stl/{f}.stl" for f in manque], check=True)
    return [trimesh.load(D + f + ".stl", force="mesh") for f in fmas]


# ---------- voie procédurale : chaque fonction rend (pièces, dimensions de contrôle) ----------
def erythrocyte():
    # Evans E, Fung YC. Microvasc Res 1972;4:335-347 : z(r) = ±½ √(1-ρ²)(C0 + C2 ρ² + C4 ρ⁴), ρ = r/R0,
    # R0 = 3,91 µm, C0 = 0,81 µm, C2 = 7,83 µm, C4 = -4,39 µm → diamètre 7,82 µm, épaisseur ≈ 2,4 µm au bord, 0,81 µm au centre.
    R0, C0, C2, C4 = 3.91, 0.81, 7.83, -4.39
    nr, nt = 60, 96; rho = np.sin(np.linspace(0, np.pi / 2, nr)); th = np.linspace(0, 2 * np.pi, nt, endpoint=False)
    h = 0.5 * np.sqrt(np.clip(1 - rho ** 2, 0, None)) * (C0 + C2 * rho ** 2 + C4 * rho ** 4)
    V, F = [], []
    for s in (1, -1):
        base = len(V)
        for i in range(nr):
            for t in th:
                V.append([R0 * rho[i] * np.cos(t), R0 * rho[i] * np.sin(t), s * h[i]])
        for i in range(nr - 1):
            for j in range(nt):
                a, b = base + i * nt + j, base + i * nt + (j + 1) % nt; c, d = a + nt, b + nt
                F += [[a, c, b], [b, c, d]] if s == 1 else [[a, b, c], [b, d, c]]
    m = trimesh.Trimesh(V, F); m.merge_vertices(merge_tex=True, merge_norm=True)
    return [coul(m, ROUGE)], {"diametre_um": (m.extents[0], 7.82), "epaisseur_max_um": (m.extents[2], 2.4)}


def plaquette():
    # Frojmovic MM, Milton JG. Physiol Rev 1982;62:185-261 : plaquette au repos discoïde, ≈ 3,6 µm × 0,9 µm.
    m = trimesh.creation.icosphere(4, radius=1.0); m.apply_scale([1.8, 1.8, 0.45])
    gr = [trimesh.creation.icosphere(1, radius=0.12).apply_translation(p) for p in [[0.6, 0.3, 0], [-0.5, 0.5, 0], [0.1, -0.7, 0], [-0.4, -0.3, 0]]]
    return [coul(m, [205, 170, 210]), coul(trimesh.util.concatenate(gr), VIOLET)], {"diametre_um": (m.extents[0], 3.6)}


def leucocytes():
    # Ross MH, Pawlina W. Histology, 8e éd. 2020, chap. 10 : neutrophile 10-12 µm, noyau de 3 à 5 lobes ;
    # lymphocyte 7 µm (petit lymphocyte), noyau rond occupant presque toute la cellule.
    neu = trimesh.creation.icosphere(4, radius=5.5)
    lobes = [trimesh.creation.icosphere(3, radius=1.6).apply_translation(p) for p in [[-2.4, 0.6, 0], [-0.8, -1.2, 0.3], [1.0, -0.6, -0.2], [2.4, 0.9, 0]]]
    ponts = tube([[-2.4, 0.6, 0], [-0.8, -1.2, 0.3], [1.0, -0.6, -0.2], [2.4, 0.9, 0]], 0.35, VIOLET)
    lym = trimesh.creation.icosphere(4, radius=3.5).apply_translation([14, 0, 0])
    nl = trimesh.creation.icosphere(3, radius=2.9).apply_translation([14.3, 0, 0])
    return [coul(neu, [230, 225, 240]), coul(trimesh.util.concatenate(lobes), VIOLET), ponts, coul(lym, [215, 225, 245]), coul(nl, [60, 50, 140])], \
        {"neutrophile_um": (neu.extents[0], 11.0), "lymphocyte_um": (lym.extents[0], 7.0)}


def jonction_nm():
    # Ross & Pawlina 2020, chap. 11 : fente synaptique primaire ≈ 50 nm ; plis jonctionnels (fentes secondaires) ≈ 1 µm de profondeur ;
    # vésicules synaptiques ≈ 50 nm (Heuser JE, Reese TS. J Cell Biol 1973;57:315-344). Bouton terminal modélisé à 3 µm de large.
    bouton = trimesh.creation.icosphere(4, radius=1.0); bouton.apply_scale([1.5, 1.0, 0.8]); bouton.apply_translation([0, 0, 0.85])
    axone = tube([[0, 0, 0.9], [0, 0, 3.5]], 0.35, JAUNE)
    ves = [trimesh.creation.icosphere(1, radius=0.025).apply_translation(p) for p in np.random.default_rng(1).uniform([-1, -0.6, 0.15], [1, 0.6, 0.6], (120, 3))]
    fente = 0.05; plaque = []
    for x in np.arange(-2.0, 2.01, 0.25):   # crêtes séparées par les plis jonctionnels (1 µm de profondeur)
        plaque.append(trimesh.creation.box([0.17, 2.4, 1.0]).apply_translation([x, 0, -fente - 0.5]))
    plaque.append(trimesh.creation.box([4.4, 2.4, 1.0]).apply_translation([0, 0, -fente - 1.5]))
    return [coul(bouton, JAUNE), axone, coul(trimesh.util.concatenate(ves), [250, 240, 200]), coul(trimesh.util.concatenate(plaque), ROUGE)], \
        {"pli_um": (1.0, 1.0)}


def peau(glandes):
    # Ross & Pawlina 2020, chap. 15 : épiderme 0,075-0,15 mm (peau fine) ; derme papillaire et réticulaire ≈ 1-2 mm ; papilles dermiques ;
    # glande sudorale eccrine : peloton sécrétoire ≈ 0,4 mm de diamètre au fond du derme ou dans l'hypoderme, canal hélicoïdal vers l'épiderme ;
    # glande sébacée : alvéoles annexées au follicule pileux, ≈ 0,2-2 mm. Unité : mm.
    W = 3.0; morceaux = []
    xs = np.linspace(-W / 2, W / 2, 61); X, Y = np.meshgrid(xs, xs)
    Z = 0.12 * (np.sin(X * 2 * np.pi / 0.3) * np.sin(Y * 2 * np.pi / 0.3)) ** 2   # papilles dermiques (hauteur ≈ 0,1 mm, pas 0,3 mm)
    der = trimesh.creation.box([W, W, 1.8]).apply_translation([0, 0, -0.9])
    pap = [trimesh.creation.cylinder(radius=0.05, height=0.12).apply_translation([x, y, 0.06]) for x in xs[::5] for y in xs[::5]]
    hypo = trimesh.creation.box([W, W, 1.5]).apply_translation([0, 0, -2.55])
    lob = [trimesh.creation.icosphere(2, radius=0.25).apply_translation(p) for p in np.random.default_rng(2).uniform([-1.2, -1.2, -3.1], [1.2, 1.2, -2.1], (25, 3))]
    if not glandes:
        return [coul(der, [235, 175, 160]), coul(trimesh.util.concatenate(pap), [235, 150, 140]), coul(hypo, [245, 225, 150]), coul(trimesh.util.concatenate(lob), [250, 235, 170])], \
            {"derme_mm": (1.8, 1.8)}
    t = np.linspace(0, 8 * np.pi, 160)   # peloton sécrétoire eccrine (diamètre 0,4 mm)
    pel = [[0.2 * np.cos(u) - 0.6, 0.2 * np.sin(u), -1.9 - 0.25 * u / (8 * np.pi)] for u in t[::4]]
    canal = [[-0.6 + 0.04 * np.sin(z * 25), 0.04 * np.cos(z * 25), z] for z in np.linspace(-1.9, 0.1, 40)]
    foll = tube([[0.6, 0, -1.6], [0.6, 0, 0.15]], 0.07, [120, 80, 60])
    seb = [trimesh.creation.icosphere(2, radius=0.12).apply_translation(p) for p in [[0.8, 0, -0.7], [0.85, 0.12, -0.85], [0.78, -0.12, -0.9], [0.9, 0, -1.0]]]
    return [tube(pel, 0.03, BLEU), tube(canal, 0.012, [120, 160, 220]), foll, coul(trimesh.util.concatenate(seb), JAUNE)], \
        {"peloton_mm": (0.4, 0.4)}


def microcirculation():
    # Levick JR. An Introduction to Cardiovascular Physiology, 5e éd. 2010 : artériole 10-100 µm, capillaire 5-8 µm, veinule post-capillaire 10-30 µm.
    art = tube([[-150, 0, 0], [-60, 0, 0]], 15, ROUGE, 24); ven = tube([[60, 0, 0], [150, 0, 0]], 15, BLEU, 24)
    caps = []
    for y in np.linspace(-40, 40, 6):
        pts = [[-60, 0, 0], [-35, y * 0.6, 5], [0, y, -5 * np.sign(y)], [35, y * 0.6, 5], [60, 0, 0]]
        caps.append(tube(pts, 3.5, [200, 80, 120], 12))
    return [art, ven, trimesh.util.concatenate(caps)], {"capillaire_um": (7.0, 7.0)}


def tissu_conduction():
    # Tissu de conduction reconstruit sur le cœur réel BodyParts3D (paroi FMA7274, veine cave supérieure FMA4720, veine cave inférieure
    # FMA10951, sinus coronaire FMA4706, valves tricuspide FMA7234 et mitrale FMA7235, aorte ascendante FMA3736, muscles papillaires
    # FMA7260, FMA7266, FMA9352nsn ; CC BY-SA 2.1 JP). Topologie : Anderson RH, Ho SY. Novartis Found Symp 2003;250:6-17 (nœud sinusal
    # sous-épicardique dans le sillon terminal ; nœud AV à l'apex du triangle de Koch ; faisceau pénétrant entre septum fibreux et
    # musculaire ; branches descendant de part et d'autre du septum) et Anderson RH et al. Clin Anat 2009;22:99-113.
    # Mesures : nœud sinusal en croissant, 13,5 ± 2,5 mm (Sánchez-Quintana D et al. Heart 2005;91:189-194) ; triangle de Koch,
    # His → ostium du sinus coronaire 25,9 ± 7,9 mm (Ueng KC et al. J Cardiovasc Electrophysiol 1996;7:1017-1023). Unité : mm.
    import fast_simplification as fs
    paroi, vcs, vci, sc, tv, mv, aao, pap_vd, pap_vg_p, pap_vg_a = stl_bp3d(
        ["FMA7274", "FMA4720", "FMA10951", "FMA4706", "FMA7234", "FMA7235", "FMA3736", "FMA7260", "FMA7266", "FMA9352nsn"])
    v, f = fs.simplify(paroi.vertices.astype(np.float32), paroi.faces.astype(np.int32), target_reduction=1 - 30000 / len(paroi.faces))
    W = trimesh.Trimesh(v, f); W.fix_normals()
    bas = lambda m, k=3: m.vertices[m.vertices[:, 2] < m.vertices[:, 2].min() + k].mean(0)
    J = bas(vcs); I = vci.vertices[vci.vertices[:, 2] > vci.vertices[:, 2].max() - 3].mean(0)    # jonctions caves – oreillette droite
    racine = bas(aao, 4); H = tv.vertices[np.linalg.norm(tv.vertices - racine, axis=1).argmin()]  # anneau tricuspide au contact de la racine aortique (corps fibreux central)
    O = sc.vertices[sc.vertices[:, 0].argmin()]                                                    # ostium du sinus coronaire (extrémité droite)
    C = (tv.vertices.mean(0) + mv.vertices.mean(0)) / 2; u = np.array([1, -0.6, -1.0]); u /= np.linalg.norm(u)
    A = W.vertices[((W.vertices - C) @ u).argmax()]                                               # apex (en bas, en avant, à gauche)
    ax = (A - H) / np.linalg.norm(A - H); n = mv.vertices.mean(0) - tv.vertices.mean(0); n -= (n @ ax) * ax; n /= np.linalg.norm(n)  # n : du VD vers le VG
    surf = lambda P: trimesh.proximity.closest_point(W, np.atleast_2d(P))[0]

    fc, fn = W.triangles_center, W.face_normals
    rel = fc - H; perp = np.linalg.norm(rel - np.outer(rel @ ax, ax), axis=1)
    sept = {c_: cKDTree(fc[(perp < 14) & (c_ * (fn @ n) > 0.4)]) for c_ in (1, -1)}   # faces endocardiques du septum : côté VG (+1), côté VD (-1)
    sept_n = {c_: fn[(perp < 14) & (c_ * (fn @ n) > 0.4)] for c_ in (1, -1)}
    sept_c = {c_: fc[(perp < 14) & (c_ * (fn @ n) > 0.4)] for c_ in (1, -1)}

    def face_septale(P, cote):   # point de la face endocardique du septum (cote = +1 : VG, -1 : VD), 0,6 mm dans la cavité
        d_, i_ = sept[cote].query(P)
        return None if d_ > 15 else sept_c[cote][i_] + 0.6 * sept_n[cote][i_]

    # 1. nœud sinusal : croissant de 13,5 mm, sous l'épicarde du sillon terminal, de la VCS vers la VCI, face latérale droite
    d = (I - J) / np.linalg.norm(I - J); pts = [J + d * s_ + np.array([-6.0, -4.0, 0]) for s_ in np.linspace(1, 14.5, 10)]
    ps = surf(np.array(pts)); nrm = ps - W.centroid; nrm /= np.linalg.norm(nrm, axis=1, keepdims=True); ps = ps - 1.0 * nrm
    lon_ns = float(np.sum(np.linalg.norm(np.diff(ps, axis=0), axis=1)))
    ns = [trimesh.creation.icosphere(2, radius=r).apply_translation(p) for p, r in zip(ps, np.linspace(2.5, 1.0, len(ps)))]
    ns += [trimesh.creation.cylinder(radius=r, segment=[a, b], sections=12) for a, b, r in zip(ps[:-1], ps[1:], np.linspace(2.4, 1.0, len(ps) - 1))]
    # 2. nœud auriculo-ventriculaire compact : ellipsoïde 5 × 3 × 1,5 mm (ordre de grandeur classique de Tawara, repris par Anderson 2009),
    #    à l'apex du triangle de Koch, 5 mm en arrière du point de His, le long du bord His → ostium du sinus coronaire
    k = (O - H) / np.linalg.norm(O - H); centre = surf(H + 5 * k)[0]
    noeud = trimesh.creation.icosphere(3, radius=1.0); noeud.apply_scale([2.5, 1.5, 0.75])
    z0 = np.cross(k, n); z0 /= np.linalg.norm(z0); R = np.eye(4); R[:3, :3] = np.c_[k, np.cross(z0, k), z0]; noeud.apply_transform(R); noeud.apply_translation(centre)
    # 3. faisceau de His : du nœud AV au point de His puis 8 mm le long de la crête du septum (bifurcation B)
    B = H + 8 * ax; his = tube([centre, H, B], 1.0, [210, 40, 40], 12)
    # 4. branches : droite (cordon unique vers la bande modératrice et le muscle papillaire antérieur du VD) ; gauche en éventail (3 fascicules)
    def branche(cible, cote, r, c):
        chemin = [B]
        for t in np.linspace(0.15, 0.85, 8):
            q = face_septale(B + t * (cible - B), cote) if cote else None
            chemin.append(q if q is not None else surf(B + t * (cible - B))[0])
        chemin.append(cible); return chemin, tube(chemin, r, c, 10)
    pied = lambda m: m.vertices[((m.vertices - C) @ u).argmax()]   # base d'un muscle papillaire (côté apex)
    mi_sept = H + 0.6 * (A - H)
    bd, tbd = branche(pied(pap_vd), -1, 0.6, [40, 150, 60])
    fasc = [branche(pied(pap_vg_a), 1, 0.6, [40, 170, 90]), branche(pied(pap_vg_p), 1, 0.6, [40, 170, 90]), branche(mi_sept, 1, 0.5, [40, 170, 90])]
    # 5. réseau de Purkinje : sous-endocarde des deux tiers apicaux des ventricules ; arbre couvrant minimal (arêtes ≤ 12 mm, collées à la paroi)
    rng = np.random.default_rng(7); cand = W.vertices[rng.choice(len(W.vertices), 6000, replace=False)]
    _, _, tri = trimesh.proximity.closest_point(W, cand); nv = W.face_normals[tri]
    endo = W.ray.intersects_any(cand + 0.3 * nv, nv)                                      # la normale sortante rencontre la paroi : face endocardique
    prof = (cand - C) @ (A - C) / np.linalg.norm(A - C) ** 2
    garde = endo & (prof > 0.33) & (prof < 1.05); P = cand[garde] + 0.6 * nv[garde]
    P = P[cKDTree(P).query(P, k=2)[0][:, 1] > 0]
    sel = [0]; dmin = np.linalg.norm(P - P[0], axis=1)
    for _ in range(min(260, len(P)) - 1):                                                  # échantillonnage le plus éloigné (couverture régulière)
        i = int(dmin.argmax()); sel.append(i); dmin = np.minimum(dmin, np.linalg.norm(P - P[i], axis=1))
    Q = np.vstack([P[sel]] + [np.array(c_[0][-3:]) for c_ in fasc] + [np.array(bd[-3:])])
    dd, ii = cKDTree(Q).query(Q, k=8); rows, cols, vals = [], [], []
    for a_ in range(len(Q)):
        for d_, b_ in zip(dd[a_, 1:], ii[a_, 1:]):
            if d_ <= 12 and np.linalg.norm(surf((Q[a_] + Q[b_]) / 2)[0] - (Q[a_] + Q[b_]) / 2) < 2.0:
                rows.append(a_); cols.append(b_); vals.append(d_)
    from scipy.sparse import coo_matrix
    T_ = minimum_spanning_tree(coo_matrix((vals, (rows, cols)), shape=(len(Q), len(Q)))).tocoo()
    purk = [trimesh.creation.cylinder(radius=0.35, segment=[Q[a_], Q[b_]], sections=6) for a_, b_ in zip(T_.row, T_.col)]
    pieces = [coul(W, [235, 200, 195]), coul(trimesh.util.concatenate(ns), [245, 180, 40]), coul(noeud, [240, 120, 30]), his, tbd] + [t_ for _, t_ in fasc] \
        + [coul(trimesh.util.concatenate(purk), [120, 200, 120])]
    return pieces, {"noeud_sinusal_mm": (lon_ns, 13.5), "koch_his_sinus_coronaire_mm": (float(np.linalg.norm(O - H)), 25.9, 7.9 / 25.9)}


PROC = {
    "he_sang_globules_rouges": ("Sang : globules rouges", erythrocyte, "µm", "Érythrocyte en disque biconcave, forme d'Evans et Fung (Microvasc Res 1972;4:335-347), diamètre 7,82 µm."),
    "he_sang_globules_blancs": ("Sang : globules blancs", leucocytes, "µm", "Neutrophile (11 µm, noyau à 4 lobes) et petit lymphocyte (7 µm), dimensions de Ross et Pawlina, Histology 8e éd. 2020, chap. 10."),
    "he_plaquettes_et_hemostase": ("Plaquettes et hémostase", plaquette, "µm", "Plaquette au repos discoïde 3,6 × 0,9 µm avec granules, d'après Frojmovic et Milton, Physiol Rev 1982;62:185-261."),
    "ne_jonction_neuromusculaire": ("Jonction neuromusculaire", jonction_nm, "µm", "Bouton terminal, vésicules de 50 nm, fente de 50 nm et plaque motrice à plis de 1 µm, d'après Ross et Pawlina 2020 chap. 11 et Heuser et Reese, J Cell Biol 1973."),
    "de_derme_et_hypoderme": ("Derme et hypoderme", lambda: peau(False), "mm", "Bloc de peau de 3 mm : derme de 1,8 mm à papilles et hypoderme à lobules adipeux, d'après Ross et Pawlina 2020 chap. 15."),
    "de_glandes_sudorales_et_sebacees": ("Glandes sudorales et sébacées", lambda: peau(True), "mm", "Glande eccrine (peloton de 0,4 mm et canal hélicoïdal) et glande sébacée annexée au follicule, d'après Ross et Pawlina 2020 chap. 15."),
    "cv_cur_tissu_de_conduction": ("Cœur : tissu de conduction", tissu_conduction, "mm",
                                   "Tissu de conduction reconstruit (procédural) sur le cœur réel BodyParts3D 4.0 (CC BY-SA 2.1 JP) : nœud sinusal en croissant de 13,5 mm "
                                   "sous l'épicarde du sillon terminal (Sánchez-Quintana et al., Heart 2005;91:189-194), nœud AV à l'apex du triangle de Koch "
                                   "(His → ostium du sinus coronaire 25,9 ± 7,9 mm ; Ueng et al., J Cardiovasc Electrophysiol 1996;7:1017-1023), faisceau de His, "
                                   "branche droite vers la bande modératrice, branche gauche en trois fascicules et réseau de Purkinje sous-endocardique, "
                                   "d'après Anderson et Ho, Novartis Found Symp 2003;250:6-17 et Anderson et al., Clin Anat 2009;22:99-113. "
                                   "Épaisseurs du nœud AV (5 × 3 × 1,5 mm), du His (2 mm) et des fibres de Purkinje (0,7 mm) : grossies ou indicatives, pour la lecture."),
    "cv_microcirculation": ("Microcirculation", microcirculation, "µm", "Artériole de 30 µm, réseau de capillaires de 7 µm et veinule de 30 µm, d'après Levick, Introduction to Cardiovascular Physiology 5e éd. 2010."),
}
BP3D = {
    "rn_testicules_epididymes": ("Testicules, épididymes et voies spermatiques", ["FMA7211", "FMA7212", "FMA18256", "FMA18257"],
                                 "Testicules et épididymes droits et gauches, modèle d'atlas isolé (jamais sur le corps entier) ; voies spermatiques absentes de BodyParts3D."),
    "en_gonades": ("Gonades", ["FMA7211", "FMA7212"],
                   "Gonades masculines (testicules) en modèle d'atlas isolé ; l'ovaire manque dans BodyParts3D (modèle masculin) ; les ovaires sont produits à part (org_gyneco_ovaires, Human Reference Atlas, CC BY 4.0)."),
}

index = json.load(open(IDX, encoding="utf-8")); fait = 0
for oid, (nom, fmas, note) in BP3D.items():
    emp = hashlib.sha256(json.dumps([fmas, CODE]).encode()).hexdigest()[:16]
    if index["organes"].get(oid, {}).get("empreinte") == emp and os.path.exists(os.path.join(SORTIE, oid + ".glb")):
        continue
    manque = [f for f in fmas if not os.path.exists(D + f + ".stl")]
    if manque:
        if not os.path.isdir(BP):
            subprocess.run(["git", "clone", "-q", "--filter=blob:none", "--no-checkout", "https://github.com/Kevin-Mattheus-Moerman/BodyParts3D.git", BP], check=True)
        subprocess.run(["git", "-C", BP, "-c", "gc.auto=0", "checkout", "HEAD", "--"] + [f"assets/BodyParts3D_data/stl/{f}.stl" for f in manque], check=True)
    m = trimesh.util.concatenate([trimesh.load(D + f + ".stl", force="mesh") for f in fmas]); m.apply_translation(-m.bounds.mean(axis=0)); coul(m, [215, 170, 160])
    sc = trimesh.Scene(); sc.add_geometry(m, node_name=oid, geom_name=oid); sc.export(os.path.join(SORTIE, oid + ".glb"))
    index["organes"][oid] = {"nom": nom, "statut": "produit", "pieces": len(fmas), "faces": len(m.faces), "taille_mm": [round(x) for x in m.extents],
                             "source": "BodyParts3D 4.0 (" + ", ".join(fmas) + "), Database Center for Life Science, CC BY-SA 2.1 JP",
                             "nature": "maillage réel", "usage": "didactique et anatomique, organe isolé (atlas)", "note": note, "empreinte": emp}
    fait += 1; print(oid, [round(x) for x in m.extents], "mm", flush=True)

for oid, (nom, f, unite, src) in PROC.items():
    emp = hashlib.sha256(json.dumps([oid, unite, src, CODE]).encode()).hexdigest()[:16]
    if index["organes"].get(oid, {}).get("empreinte") == emp and os.path.exists(os.path.join(SORTIE, oid + ".glb")):
        continue
    pieces, ctrl = f(); m = trimesh.util.concatenate(pieces); m.apply_translation(-m.bounds.mean(axis=0))
    for k, (mes, cible, *tol) in ctrl.items():   # contrôle à 10 % des dimensions citées (ou à l'écart-type publié)
        assert abs(mes - cible) / cible <= (tol[0] if tol else 0.10), f"{oid} {k} : {mes:.2f} ≠ {cible}"
    sc = trimesh.Scene(); sc.add_geometry(m, node_name=oid, geom_name=oid); chemin = os.path.join(SORTIE, oid + ".glb"); sc.export(chemin)
    assert os.path.getsize(chemin) < 5e6, oid
    index["organes"][oid] = {"nom": nom, "statut": "produit", "pieces": len(pieces), "faces": len(m.faces), "unite": unite,
                             "taille": [round(float(x), 2) for x in m.extents], "echelle": f"1 unité du maillage = 1 {unite} (échelle réelle)",
                             "nature": "modèle 3D scientifique reconstruit (procédural, dimensions publiées)", "source": src, "empreinte": emp,
                             "controle": {k: round(float(v[0]), 2) for k, v in ctrl.items()}}
    fait += 1; print(oid, [round(float(x), 2) for x in m.extents], unite, flush=True)

sup = index["_meta"].setdefault("sources_supplementaires", [])
for s in ["BodyParts3D 4.0, organes génitaux internes isolés à but didactique (décision de Vial du 26.11.2026), CC BY-SA 2.1 JP",
          "Modèles procéduraux reconstruits (trimesh) : Evans et Fung 1972 ; Frojmovic et Milton 1982 ; Ross et Pawlina, Histology 8e éd. 2020 ; Heuser et Reese 1973 ; Levick 2010",
          "Tissu de conduction reconstruit sur le cœur BodyParts3D : Anderson et Ho 2003 ; Anderson et al. 2009 ; Sánchez-Quintana et al. 2005 ; Ueng et al. 1996"]:
    if s not in sup:
        sup.append(s)
json.dump(index, open(IDX, "w", encoding="utf-8"), ensure_ascii=False, indent=1)
print(f"organes 3D : {sum(1 for x in index['organes'].values() if x['statut'] == 'produit')} produits ; {fait} nouveaux")
