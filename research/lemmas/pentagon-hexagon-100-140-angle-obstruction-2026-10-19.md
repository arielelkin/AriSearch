# An exact pentagon-containing angle obstruction

Status: proved internally; awaiting independent hostile review. This is a narrow no-tiling gate, not an unrestricted impossibility theorem or a novelty claim.

## Statement

There exist an exact strictly convex pentagon P and strictly convex hexagon H, with respective interior-angle lists (100,100,100,100,140) and (100,100,100,140,140,140) degrees. No tiling by isometric copies of P and H exists, even allowing reflections, omission of either type, and arbitrary partial-edge contacts. More generally no finite set of polygons all of whose interior angles belong to {100,140} degrees tiles the plane.

## Exact polygons

Let z = exp(2 pi i/18), the root of x^6-x^3+1 with argument 20 degrees (this argument selection fixes its complex embedding). Write n(k) = (Re(z^k),Im(z^k)). For P use normal indices (0,4,8,12,16); for H use (0,4,8,12,14,16). For either cyclic list k_0,...,k_(m-1), define the polygon as the intersection n(k_j) dot x <= 1. Its vertex v_j is the intersection of lines j and j+1, indices cyclically; explicitly for n(k_j)=(a,b), n(k_(j+1))=(c,d), v_j=((d-b)/(ad-bc),(a-c)/(ad-bc)). These are finite algebraic coordinates with specified embedding.

Successive normal gaps are 80,80,80,80,40 degrees for P and 80,80,80,40,40,40 for H. Each is strictly between zero and 180. Thus the tangent lines to the unit circle form bounded strictly convex polygons, with one genuine edge per line and interior angles 180 degrees minus the corresponding gaps. The two polygons have distinct numbers of vertices and therefore distinct congruence classes.

## Local obstruction with unrestricted contacts

Any tiling by a finite collection of compact polygon shapes is locally finite: each tile intersecting a compact set K lies within distance D of K, where D is the largest tile diameter. Each such tile contains a disk of a common positive radius r, and these disks have disjoint interiors. The bounded neighborhood of K can contain only finitely many such disks.

Choose any vertex v of any tile. Local finiteness permits a sufficiently small disk around v in which every incident tile occupies a sector. A tile whose boundary contains v contributes either its genuine interior corner angle, or 180 degrees when v lies in the relative interior of an edge. No tile can contain v in its interior because that would intersect the interior of the chosen tile near v. The sectors sum to 360 degrees. There is at least one genuine corner and at most one straight sector, since genuine corner angles are positive.

Writing a,b for numbers of 100- and 140-degree corners and c for straight sectors gives 5a+7b+9c=18, with a,b,c nonnegative integers and a+b>=1. Necessarily c=0 or 1. For c=0, b belongs to {0,1,2}, leaving 18,11,4 for 5a, none divisible by 5. For c=1, b belongs to {0,1}, leaving 9,2, again impossible. This contradicts the existence of v and proves the claim.

## First-gate interpretation and limits

For any proposed pentagon/hexagon pair with these two angle values, the first necessary gate is the full or straight-sector vertex equation. It fails before side-length compatibility or plane extension is considered. This is one exact angle palette killed, independent of any hexagon dimer fixture, bounded patch search, or torus bound. It excludes no pair using another angle palette and supplies no aperiodic pair. No literature priority is asserted; the proof is elementary.

## Reproducibility

The small independent Sage checker research/searches/pentagon-hexagon-100-140-angle-obstruction-2026-10-19.sage reconstructs the exact coordinates in the real algebraic field, checks every supporting half-plane, strict turns, nonzero edges, and exhausts the complete local equation domain. Run:

    mise exec -- conda run --no-capture-output -n arisearch sage research/searches/pentagon-hexagon-100-140-angle-obstruction-2026-10-19.sage

Dependencies: elementary Euclidean geometry and local finiteness proof above. No external classification theorem or solver result is used.
