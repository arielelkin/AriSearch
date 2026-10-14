# Independent audit: finite nonconvex parents made from convex hexagonal atoms

Date: 2026-10-14. Reviewer: construction-adversary agent, independent of the root proposal. Verdict: VALID for the corrected sector-count formulation below. The initial native-corner interpretation of the reflex term needed repair.

## Claim and exact hypotheses

The [root perimeter theorem](../lemmas/nonconvex-parent-hexagon-perimeter-bound.md) concerns a finite partition of a simple polygonal disk with p genuine boundary corners into t genuine convex polygons, each with at least six native sides. Native child lengths are bounded by L. Arbitrary reflections, partial seams, straight subdivisions and isolated contacts are allowed; holes, unbounded parents and nonpolygonal boundaries are outside the claim.

The conclusion is perimeter(parent) <= (2p-6)L. Consequently no fixed finite set of such simple polygonal parents can have compatible scalar inflation iterates of unbounded scale, each partitioned into the same fixed convex atoms. Nonconvex finite parents do not rescue this particular all-hexagon substitution mechanism. This is not a theorem about every tiling by two hexagons or every possible hierarchy.

## Independent derivation and defect found

Planarize every child boundary and the parent boundary, retaining genuine parent corners and all seam junctions; remove irrelevant degree-two collinear points. Let Vb be non-native junctions on straight parent boundary, Vi interior junctions, E edges, S the sum of incident child sectors at all vertices, N the total native child-corner count, and F the number of child-flat incidences. Thus S=N+F. A child flat incidence at a reflex parent corner MUST be included in F, not silently excluded.

Euler for a disk gives E=t+p+Vb+Vi-1. Every boundary edge has one incident child and every interior edge two, so 2E=S+p+Vb. Minimum child-sector incidences are one at a genuine parent corner, two at a straight boundary junction and three at an interior junction. Write S=p+2Vb+3Vi+X for the total nonnegative sector excess. Eliminating E, S and Vi gives

    6t-N = 6-p+Vb+2X+F.

Since N>=6t, Vb+2X+F<=p-6. In particular Vb<=p-6. Every planarized boundary segment is contained in one native child side, so has length at most L. There are p+Vb such segments, proving the bound.

The original proposal's statement that a reflex corner necessarily has at least two NATIVE child corners was too strong: a convex child can contribute a flat sector there. Counting incident child sectors instead repairs the argument. Every reflex corner does have at least two incident sectors, because one convex child cannot fill a reflex sector. Therefore X is at least the number of reflex parent corners, and the strengthened Vb<=p-6-2r bound follows without excluding flat child incidences at those corners.

## Counterexample attempts and scope checks

The audit targeted a child flat at a reflex parent corner, T junctions on the parent boundary, collinear child-edge subdivisions, isolated boundary touches, disconnected positive-length child adjacency, and nonconvex parent angles. Sector counts and planarized disk Euler handle these; the proof never assumes a convex parent or connected positive-length adjacency graph. Finite polygon partitions give a finite connected planar boundary complex because the covered domain is a disk. Nonconvexity only increases sector requirements at reflex corners.

For a scalar factor lambda>1, a fixed parent's perimeter grows by lambda^k while p and the fixed atom bound L remain constant. This contradicts the same finite bound for sufficiently large k. A finite family of parent shapes has bounded p, so choosing another parent in that family does not evade the contradiction. A single finite dissection, a hierarchy with growing corner counts, a nonpolygonal parent, a parent with holes, or a scheme using pentagonal/nonconvex atoms is not excluded by this argument.

## Application to the actual construction loop

The attempted mixed-two-hexagon nonconvex-parent route uses fixed convex six-sided atoms. Its proposed iterable scalar-eight-child compiler is excluded before another packing enumeration. The construction agent changed the atom domain to a pentagon/hexagon pair. The separate exact adversary check for that new pair is recorded in [the loop note](../searches/construction-adversary-2026-10-14.md); this theorem is not applied to its pentagon atom.
