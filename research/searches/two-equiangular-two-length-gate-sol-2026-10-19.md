# Two equiangular hexagons with at most two lengths each

Status: proved internally; independent hostile review pending. No novelty claim.

## Statement
Let A and B be strictly convex equiangular 120-degree hexagons. Suppose
EACH has at most two distinct numerical side lengths (their palettes need
not coincide). Then either the pair does not tile the plane, or it admits
a rank-two periodic tiling. More precisely: a centrally symmetric member
supplies a monohedral lattice tiling; if neither is centrally symmetric,
no tiling exists. Isometries, reflections, and unrestricted contacts are allowed.
This does not resolve the general pair problem or the three-length frontier.

## Exact closure and the binary classification
Put e_i=(cos(i*pi/3),sin(i*pi/3)). For consecutive positive side lengths
l_0,...,l_5, closure is exactly

    l_0-l_3 = l_2-l_5 = l_4-l_1 = t.

Indeed e_2=e_1-e_0 and e_{i+3}=-e_i. If t=0 opposite
lengths agree, so opposite edges are equal and opposite, hence the hexagon
is centrally symmetric. Conversely central symmetry implies t=0.
If the palette is {a,b}, a<b, and t is nonzero, every difference above
must be the same one of +(b-a), -(b-a). Consequently the word is exactly
(a,b,a,b,a,b) or its cyclic shift. This is a universal symbolic argument;
no rational-independence or normalization assumption on a,b is needed.
Positive closed words with these ordered headings are strictly convex:
all turns are pi/3 and their convex edge ordering bounds a convex polygon.

## Full-edge trivalent contacts
Every tile corner has angle 120 degrees. A vertex cannot lie in the
relative interior of a side of another tile: that would leave a
180-degree half-plane to be filled by whole 120-degree corner sectors,
which is impossible. Thus contacts are full edges, and exactly three
corners meet at each vertex. Compactness and positive minimum tile size
make the tiling locally finite, justifying this local sector count.

## The two-palette obstruction
If both tiles are noncentral, write their unordered length palettes as
{a,b} and {c,d}, with a!=b and c!=d. Form the simple graph G whose
vertices are actual numerical lengths and whose edges are these two
unordered pairs, identifying equal numerical values. It has at most two
edges and no loops, so it is bipartite (also when the palettes share one
length or coincide). Each corner of either tile has one incident edge
length in each part of a bipartition. At a trivalent tiling vertex let
x,y,z be the three outgoing edge lengths. Its three tile corners require
xy,yz,zx all to be edges of G. This is an odd closed walk, impossible
in a bipartite graph. Equivalently the three corners contribute three
incidences to each part while each physical ray contributes two.
Reflections reverse corner order but do not change an unordered palette.
The contradiction is pointwise, so it proves no infinite tiling exists.

## The central member supplies a lattice escape
Write a central member's consecutive edge vectors as
u,v,w,-u,-v,-w. Its vertices are
0,u,u+v,u+v+w,v+w,w, with all corner angles 120 degrees.
Identify opposite boundary edges by translations. The three pairing
translations are v+w, w-u, and -(u+v); they lie in the rank-two lattice
L=Z(u+v)+Z(v+w). Opposite-edge gluing produces a connected orientable
compact surface with one face, three edges, and two vertex classes.
Each vertex class contains three original 120-degree corners, so there
are no cone singularities. It is a flat torus. Its universal cover is
the Euclidean plane: a complete simply connected flat surface develops
isometrically to the plane (straight geodesics extend for all time, and
local Euclidean charts give the standard covering/developing argument).
The lifted hexagons therefore tile the plane with no overlaps and with
the stated translation lattice. Rank two also follows directly from

    det(u+v,v+w)=det(u,v)+det(u,w)+det(v,w)>0.

This argument permits unequal u,v,w and uses neither the other member
nor any hypothesis that both prototiles occur.

## Finite audit and replay
The companion standard-library Python script enumerates exactly 2^6=64
words over {1,2}, checks exact integer closure, and certifies eight central
words and two alternating words. It checks the three palette-intersection
patterns (equal, one common value, disjoint) for absence of corner triangles.
The universal arbitrary-real conclusion follows from the written proof,
not from replacing real lengths by 1 and 2 in this finite audit.

Replay:

    mise exec -- conda run --no-capture-output -n arisearch python research/searches/two-equiangular-two-length-gate-sol-2026-10-19.py

No solver, seed, timeout, symmetry reduction, or search cutoff is used.
The finite domain is completely exhausted. Dependencies: Python standard
library only; the exact Python version is printed by `python --version`
under the same environment. The audit is supporting arithmetic evidence;
the proof above is independent of its output.
