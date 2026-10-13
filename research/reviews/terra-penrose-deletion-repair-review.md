# Hostile review of Penrose dual deletion repairs

Date: 2026-10-13. Reviewer: terra, independent of local deformation author.
Scope: only the proposed graph/density repairs to
research/lemmas/penrose-dual-single-fusion-deformation-gate.md;
not the retained algebraic polygon or infinite construction.
Verdict: VALID conditional repairs, with two literal corrections required.

## Density

Assume all original rhomb points remain intrinsic degree3/4 network vertices,
final faces are only pentagons/hexagons, and boundary counts are O(R).
Then V=N+O(R), E=2N-M+O(R), F=N-M+O(R). Combining
5F5+6F6=2E and F5+F6=F gives

    F5=2N-4M+O(R), F6=3M-N+O(R).

Nonnegative face counts yield N/3-O(R)<=M<=N/2+O(R).
The lower boundary error cannot be omitted: finite-window errors can have
either sign. At review time the displayed lower bound still omitted it;
the announced repair is mathematically correct once installed.
Under the same degree3/4 premise every removed edge lowers the degree of its
two endpoints from4 to3, so V4=N-2M+O(R)=F5/2+O(R), consistent with curvature.

## Matching

At degree2, the two final convex sectors add to2pi and each is at mostpi;
therefore both equalpi and the remaining rays are opposite. A degree1
vertex would give a2pi face sector and cannot be an intrinsic vertex of a
convex final face. Degree0 disappears into a face interior; it is not an
intrinsic network vertex. Thus if every original rhomb point remains an
intrinsic network vertex, and no surviving pair of rays can be opposite,
remaining degree is at least3. Since original degree is4, at most one edge
is deleted per original vertex: deleted edges form a matching.

The intrinsic-vertex hypothesis is indispensable: deleting all4 edges at a
point removes that point and is not excluded by the degree2 argument alone.
The current prose needs to include this hypothesis at the matching statement,
not only later at the density target. With it added the proposed repair is
VALID. Straight degree2 exceptions remain outside this simplified matching
case and must be retained separately, as the artifact already acknowledges.

Under matching, each triangular face has at most one deleted boundary edge;
removing every triangle requires exactly one. A quadrilateral has at most two
and, if two, they are disjoint along its boundary. These conclusions are valid
conditional necessary requirements, not existence of a global deletion rule.

No computations or searches were used. No unrestricted shape-forcing or
infinite-covering conclusion follows from these repairs.
