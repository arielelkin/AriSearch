#!/usr/bin/env python3
"""Exact finite construction gates for nonconvex P/P two-hexagon parents."""
import argparse
import json
from itertools import combinations_with_replacement, product
from pathlib import Path
import sys

from sage.all import AA, CyclotomicField

K = CyclotomicField(36)
z = K.gen()
roots = [z**j for j in range(36)]


def direction(degrees):
    assert degrees % 10 == 0
    return roots[(degrees//10) % 36]


def coeffs(value):
    return [str(c) for c in K(value).polynomial().list()] + ["0"]*(12-len(K(value).polynomial().list()))


def vertices(lengths, directions):
    out = [K(0)]
    for length, angle in zip(lengths, directions):
        out.append(out[-1]+length*direction(angle))
    assert out[-1] == 0
    return out[:-1]


def cyclic_binary(types):
    """Exact compatibility of all three native radial labels, allowing mirrors."""
    for flips in product((False, True), repeat=3):
        oriented = [pair[::-1] if flip else pair for pair, flip in zip(types, flips)]
        if all(oriented[j][1] == oriented[(j+1)%3][0] for j in range(3)):
            return True
    return False


def native_stars(delta, u, beta, v, eta):
    # A H/L aggregate multiplicity3 each; B native slots remain distinct.
    angles = (120+delta,120-delta,u,120,beta,v,120,eta)
    tags = ((1,0),(0,1),(1,0),(0,0),(0,0),(0,1),(1,1),(1,1))
    triples = [list(t) for t in combinations_with_replacement(range(8),3)
               if sum(angles[j] for j in t) == 360
               and cyclic_binary([tags[j] for j in t])]
    missing = [j for j in range(8) if not any(j in t for t in triples)]
    return angles, triples, missing


def main():
    if sys.flags.optimize:
        raise RuntimeError("Assertions must be enabled.")
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--output", type=Path)
    args = parser.parse_args()
    grid = tuple(range(10,180,10))
    arc_grid = tuple(a for a in grid if a != 120)
    raw = 0
    geometric = []
    for beta, eta, u in product(arc_grid, arc_grid, grid):
        v = 480-beta-eta-u
        if v not in grid:
            continue
        raw += 1
        pp = 1+direction(60)+direction(240-beta)
        qq = direction(u+eta-60)+direction(u+eta)+direction(u+180)
        assert pp != 0
        p = -qq/pp
        if p != p.conjugate() or AA(p) <= 0 or p == 1:
            continue
        Bdirections = (0,60,240-beta,u+eta-60,u+eta,u+180)
        B = vertices((p,p,p,K(1),K(1),K(1)),Bdirections)
        geometric.append((beta,eta,u,v,p,B,Bdirections))
    records = []
    survivors = []
    for beta,eta,u,v,p,B,Bdirections in geometric:
        for delta in (10,20):
            Adirections = (0,60+delta,120,180+delta,240,300+delta)
            A = vertices((p,K(1),p,K(1),p,K(1)),Adirections)
            angles, stars, missing = native_stars(delta,u,beta,v,eta)
            angles_only = sorted(set(angles))
            # Boundary-flat existence is a deliberately generous necessary
            # condition: ignore labels and allow at most8 incident child corners.
            flat = [list(t) for n in range(2,9)
                    for t in combinations_with_replacement(angles_only,n)
                    if sum(t) == 180]
            status = "MISSING_NATIVE_360_STAR" if missing else (
                "NO_180_BOUNDARY_STAR" if not flat else "ATOMIC_GATE_SURVIVOR")
            record = {"delta":delta,"B_angles":[u,120,beta,v,120,eta],
                      "p":coeffs(p),"A_vertices":[coeffs(a) for a in A],
                      "B_vertices":[coeffs(b) for b in B],
                      "A_directions":list(Adirections),"B_directions":list(Bdirections),
                      "native_360_stars":stars,"missing_native_slots":missing,
                      "flat_180_angle_multisets":flat,"status":status}
            records.append(record)
            if status == "ATOMIC_GATE_SURVIVOR":
                survivors.append(record)
    result = {"field":{"cyclotomic_order":36,"minimal_polynomial":"x^12-x^6+1",
                       "embedding":"z=exp(i*pi/18)","coefficient_order":"1,z,...,z^11"},
              "domain":{"delta_degrees":[10,20],"B_angle_grid_degrees":list(grid),
                        "B_arc_grid_degrees":list(arc_grid),"q":1,
                        "parent_atomic_counts":[1,1],"inflation":2,"inflated_children":8},
              "counts":{"angle_signatures":raw,"positive_distinct_closed_B":len(geometric),
                        "atomic_pairs":len(records),"atomic_gate_survivors":len(survivors)},
              "records":records,
              "completion":"ATOMIC_PREFILTER_COMPLETE"}
    output = json.dumps(result,sort_keys=True,indent=2)+"\n"
    if args.output:
        args.output.write_text(output)
    else:
        print(output,end="")


if __name__ == "__main__":
    main()
