#!/usr/bin/env python3
"""Geometry helpers: tile coordinates, developing map, and numerical replay.

Used to check the SFT conventions of two-hexagon-global-sft.py against the
actual plane: every configuration is developed cell by cell and every
honeycomb vertex must receive the same point from all three cells.
"""
import math, importlib.util, os
import numpy as np

_here = os.path.dirname(os.path.abspath(__file__))
_spec = importlib.util.spec_from_file_location("thg_sft", os.path.join(_here, "two-hexagon-global-sft.py"))
sft = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(sft)


def tile_points(angles, lengths):
    """corner positions; side i from corner i to i+1 with direction phi_i."""
    pts = [np.zeros(2)]
    phi = 0.0
    for i in range(6):
        if i > 0:
            phi += math.pi - math.radians(float(angles[i]))
        pts.append(pts[-1] + lengths[i] * np.array([math.cos(phi), math.sin(phi)]))
    return pts[:6], np.linalg.norm(pts[6])


def closure_matrix(angles):
    phi = 0.0
    M = np.zeros((2, 6))
    for i in range(6):
        if i > 0:
            phi += math.pi - math.radians(float(angles[i]))
        M[0, i] = math.cos(phi); M[1, i] = math.sin(phi)
    return M


def develop(S, angles, lengths, config, start=None):
    """config: dict cell->symbol index.  Returns dict (cell,slot)->point and
    max discrepancy over all vertices shared by cells in config."""
    syms = S.syms
    tp = [tile_points(angles[t], lengths[t])[0] for t in range(len(angles))]
    cells = list(config)
    start = start or cells[0]
    placed = {}

    def slotpts_local(sym):
        t, r, s = sym
        return [tp[t][(r + s * k) % 6] * np.array([1, s]) for k in range(6)]

    # place start
    placed[start] = slotpts_local(syms[config[start]])
    queue = [start]
    while queue:
        z = queue.pop()
        P = placed[z]
        for k in range(6):
            w = sft.add(z, sft.D[(k + 1) % 6])
            if w not in config or w in placed:
                continue
            loc = slotpts_local(syms[config[w]])
            # w slot k+4 = P[k], w slot k+3 = P[k+1]
            a0, a1 = loc[(k + 4) % 6], loc[(k + 3) % 6]
            b0, b1 = P[k], P[(k + 1) % 6]
            va, vb = a1 - a0, b1 - b0
            th = math.atan2(vb[1], vb[0]) - math.atan2(va[1], va[0])
            R = np.array([[math.cos(th), -math.sin(th)], [math.sin(th), math.cos(th)]])
            placed[w] = [R @ (q - a0) + b0 for q in loc]
            queue.append(w)
    # discrepancy at every vertex
    err = 0.0
    for z in placed:
        for k in range(6):
            p = placed[z][k]
            for (w, kk) in ((sft.add(z, sft.D[k]), (k + 2) % 6), (sft.add(z, sft.D[(k + 1) % 6]), (k + 4) % 6)):
                if w in placed:
                    err = max(err, float(np.linalg.norm(placed[w][kk] - p)))
    # orientation sanity: every placed hexagon positively oriented in slot order
    for z in placed:
        P = placed[z]
        area = 0.0
        for k in range(6):
            area += P[k][0] * P[(k + 1) % 6][1] - P[(k + 1) % 6][0] * P[k][1]
        if area <= 0:
            err = max(err, 1e9)
    return placed, err


def unwrap(lat, sol, R):
    n, s, mm = lat
    def wrap(z):
        x, y = z
        q = y // mm
        return ((x - s * q) % n, y - mm * q)
    return {(x, y): sol[wrap((x, y))] for x in range(-R, R + 1) for y in range(-R, R + 1)
            if max(abs(x), abs(y), abs(x + y)) <= R}
