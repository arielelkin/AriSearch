# Internally distinct Cairo-angle pairs have no edge-to-edge tiling

**Status:** adversarially reviewed; [fresh hostile review](../reviews/cairo-distinct-side-edge-obstruction-review.md) valid within the explicit edge-to-edge scope.
This is an explicitly edge-to-edge obstruction. It does not rule out plane
tilings with right-angle T-junctions under the target's unrestricted definition.

## Theorem

Let A and B be convex pentagons. In each polygon the interior angles after
successive native sides are (90,120,90,120,120) degrees. Suppose each separately
has five pairwise distinct native side lengths. Then copies of A and B do
not admit an edge-to-edge plane tiling. Reflections and all rotations remain
permitted within this hypothesis.

No assumption that the joint set of ten side slots has ten distinct lengths
is made. All cross-type equalities are included below. A type disappearing
would give a monohedral edge-to-edge tiling and is separately excluded.

## The 120-degree corner graph

At a tiling vertex containing a120-degree corner, all sectors are120degrees.
Indeed a*90+b*120=360 with b>=1 and integers a,b>=0 has only (a,b)=(0,3).
Full-side matching allows the rays at such a vertex to be labeled by whole
native side lengths. The three labels must be distinct: if two were equal,
the third tile would have two adjacent equal native side lengths, contrary
to internal distinctness.

Write A's cyclic side lengths (a,b,c,d,e). Its120-degree corners correspond
to the three graph edges

    {b,c}, {d,e}, {e,a}.

They form an isolated edge and a two-edge path, hence a forest without a
triangle. B has the same pattern. Thus a monochromatic120-degree vertex
cannot occur. In particular neither type can tile alone edge-to-edge, and
both occur. Every actual120-degree corner occurs at such a trivalent vertex.

A's isolated corner {b,c} cannot be one of two A sectors: its graph edge has
no vertex in common with either of A's other120-degree corner edges. Two
same-type corners in a mixed star must share one ray-length symbol. Therefore
A's isolated corner is the minority in a star with two B corners. B's majority
corners must be its two path corners, because those are the only different B
corner edges sharing a symbol. The same reasoning exchanges A and B.

Writing B's side lengths (A0,A1,A2,A3,f) temporarily, full-edge matching in
these two forced stars gives

    {a,d} = {A1,A2},       {b,c} = {A0,A3}.               (1)

Internal distinctness leaves exactly the following four cyclic B words:

    (b,a,d,c,f), (c,a,d,b,f),
    (b,d,a,c,f), (c,d,a,b,f).                            (2)

This deduction uses actual full sides. It is invalid at arbitrary partial
contacts; the [Cairo finite patch](../counterexamples/cairo-partial-beta-length-graph.md)
shows why.

## Exact vector closure eliminates all four words

Let w=sqrt3. In the indicated native side order, choose the first side vector
at0 degrees. The following vectors have directions0,90,150,240,300degrees.
The two coordinate closure equations for any such pentagon are

    2a = w*c+d-e,        2b = w*(d+e)-c.                 (3)

For a proposed B word (B0,B1,B2,B3,f), the first closure equation determines

    f = w*B2+B3-2B0.

Substitute this into the second closure equation. Set L=d+e-w*c. The residual
2B1-w*(B3+f)+B2 is, in the four cases (2), respectively

| B word | Exact residual |
|---|---|
| (b,a,d,c,f) | 2L |
| (c,a,d,b,f) | -4L |
| (b,d,a,c,f) | 4L |
| (c,d,a,b,f) | -2L |

Every B closure therefore forces L=0. But (3) then gives

    a=d,        b=c,

contradicting A's five distinct side lengths. This finishes the proof.
No special angle choice, numerical tolerance, pentagon classification,
periodicity assumption, or finite torus bound is used.

## Exact replay and non-consequences

```text
conda run --no-capture-output -n arisearch python3 research/reviews/verify_cairo_distinct_side_ete.py
```

A [fresh independent checker](../reviews/verify_cairo_distinct_side_independent.py) also exhausts all1546 internally-injective cross-type equality patterns, including repeated native corner multisets, and rederives the closure matrices. The small author verifier checks the angle equation, the graph's isolated edge/path,
and every one of the four exact closure residuals in Q(sqrt3)[c,d,e]. It is
not a search for plane tilings. The manual derivation above is a full finite
proof; the [execution record](../searches/cairo-distinct-side-edge-obstruction.md)
records the computational check.

If such a pair admits an unrestricted plane tiling, every such tiling has
native side subdivisions/right-angle T-junctions. The theorem does not apply
when one member has repeated side lengths, and does not exclude an unrestricted
aperiodic pair in the surviving right-angle family. No novelty claim is made.

## Short relative-density corollary

**Additional status:** internally proved; fresh review of this corollary pending.
For each fixed pair satisfying the theorem, there is an R>0 such that every
radius-R disk in every admitted unrestricted tiling contains a T-junction.
No explicit numerical R is claimed.

Otherwise translate tilings with T-free disks of radii tending to infinity
to the origin. Positive minimum area and bounded tile diameter bound the
number of tiles meeting each fixed disk. Compactness of rotations/reflections
and a diagonal subsequence give limiting polygon placements. Coverage and
disjoint interiors persist: a missing open disk or an overlapping open disk
would persist under small perturbations.

Within the expanding T-free disks every side contact is a whole-side contact.
Choose r>0 below every reference vertex-to-other-vertex and vertex-to-
nonincident-side distance. At a clean native vertex the incident native
corner sectors cover its radius-r disk; their tiles coincide with those
wedges there. No other native vertex can lie in the disk, since an interior
point of a wedge is in a tile interior and a new vertex on a wedge ray would
be a T-junction. Thus these clean vertices are uniformly separated. Whole-
side neighbours in any fixed disk can be frozen along the subsequence;
positive side lengths and this separation prevent endpoints or vertex stars
from coalescing. Every limiting side retains its whole-side neighbour. The
limit is therefore an edge-to-edge tiling by the same pair, contradicting
the theorem. This proves the uniform radius statement, including sequences
whose original tilings omit or sparsely use a type.
