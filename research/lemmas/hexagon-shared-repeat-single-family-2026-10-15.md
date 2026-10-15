# A shared repeated-length hexagon family cannot tile

Date:2026-10-15. Status: independently hostile-reviewed VALID;
[review](../reviews/hexagon-shared-repeat-single-family-hostile-2026-10-15.md).
This is one exact numerical-word family, not a classification of two
hexagons or a solution of research-problem.md.

## Statement

Let A,B be genuine convex hexagons whose cyclic native side-length words
are

    A=(r,x,r,y,z,t), B=(r,y,r,z,x,t),

where r,x,y,z,t are five pairwise distinct positive real numbers. Then the
unmarked pair admits NO plane tiling, even allowing all rotations,
reflections and partial contacts. This holds for every geometrically
realizable metric and angle choice satisfying these length words.

## Complete native endpoint proof

Use the reviewed [defect-free limit theorem](hexagon-limit-and-periodicity.md).
Any unrestricted tiling would supply a full-side everywhere-trivalent
tiling, possibly using one type only. Give its occurrences native reference
indices. Number each side0,...,5; corner i is AFTER side i, between sides i
and i+1. Denote the B corners by6,...,11.

At a trivalent vertex the three ray lengths are distinct. Otherwise two
of the rays would have equal lengths and the sector between them would
be a native corner with equal adjacent side lengths; neither polygon has
one. A vertex therefore corresponds to a triangle in the union graph
whose vertices are the five length values and whose edges are native
corner arm pairs. Neither individual word graph contains a triangle:
each is a four-cycle with a pendant edge. Thus neither type alone can
supply the limit; both types occur, and in particular corner A1 occurs.

At A1 the native arms are x and r. The third ray can only have length z
or t: the graph has the corner pair x-y absent, and no equal arms. For z,
the other two native corners must be B2=(r,z) and B3=(z,x). For t, they
must be B4=(x,t) and either A5=(t,r) or B5=(t,r). These are all choices,
including reflections. The complete possibilities and their far-end
requirements across the r ray are:

| Star containing A1 | Same two tiles at far end of their r seam |
|---|---|
| (A1,A5,B4) | (A2,A0) |
| (A1,B2,B3) | (A2,B1) |
| (A1,B4,B5) | (A2,B0) |

The first far pair has arms (r,y) and (r,x), requiring an absent x-y
corner to close its three distinct rays. Each of the second and third
has TWO copies of arm pair(r,y). Such duplicate pairs cannot coexist in
a three-distinct-ray star: the three ray-pair sectors must be the three
DIFFERENT edges of its triangle. All three possibilities are impossible.
Following a full native seam preserves its two actual incident tiles, so
these far-end requirements are mandatory, regardless of absolute tile
orientations. Hence A1 cannot occur, contradiction. QED.

## Exact finite check

[Producer](../searches/hexagon-shared-repeat-single-family-2026-10-15.py)
constructs the full twelve-star native atlas, isolates all three A1 stars,
and checks each forbidden far pair. Its
[certificate](../certificates/hexagon-shared-repeat-single-family-2026-10-15.json)
retains the atlas and endpoint obstructions. It uses only integer label
equality, finite products and native indices; no angles, solver, floating
point, geometry search, period bound or finite-patch inference appears.
The proof above is also directly human-checkable without trusting code.

Exact replay command:

    mise exec -- conda run --no-capture-output -n arisearch python research/searches/hexagon-shared-repeat-single-family-2026-10-15.py

This closes the09:30adviser's first declared shared-repeat word pair at a
cheaper endpoint gate. Its2112seam-tree records need not be enumerated.
Changing only metrics or increasing a torus search cannot reopen it. A
materially different cyclic length word or repeat arrangement is required.
