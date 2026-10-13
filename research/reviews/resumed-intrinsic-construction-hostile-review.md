# Independent hostile review: exact two-class Voronoi construction

Date: 2026-10-13. Verdict: **VALID**. Reviewer did not develop the producer.

Reviewed [construction](../searches/resumed-intrinsic-construction.md),
[producer](../searches/resumed_intrinsic_voronoi_pair.py) and
[retained certificate](../certificates/resumed_intrinsic_voronoi_pair.json).
Independent verifier:
[resumed_higher_voronoi_verify.py](resumed_higher_voronoi_verify.py).

## Exact claims checked

1. The infinite Voronoi tiling from Z²+{0,d,-d}, d=(1/10,49/100), has
   exactly two genuine convex polygon congruence classes, pentagon P and
   octagon Q; both translations by lattice generators preserve the tiling.
2. Neither P nor Q admits a monohedral tiling, including reflections and
   partial-edge contacts.
3. Grouping the three site-orbit cells for each lattice index produces a
   repeatable simple14-gon parent of area1 with four reflex vertices.
4. Moving the single site d by(1/10000,0) creates a new octagonal class
   distinct from both P and Q; the modified site set has no nonzero period.

## Independent exact verification

The verifier never imports or calls the producer. It reconstructs each
Voronoi polygon by intersections of pairs of rational bisector lines and
checks every resulting vertex against every relevant inequality. This is
different from the producer's sequential clipping algorithm. It reconstructs
V(0), V(d)-d, V(-d)+d and the modified V(0), checking the retained coordinates
as unordered sets, strict convexity and positive oriented areas.

The finite-site domain is complete: an omitted index has some local
coordinate magnitude >=101/50. For any real other coordinate v,
v²-|v|>=-1/4, whereas(101/50)²-101/50-1/4>0. Thus the omitted bisector
constraint is strictly redundant on the same-coset unit square. The
unit-square constraints themselves arise from actual four nearest
same-coset integer translates; no arbitrary truncation box is assumed.
The defect-origin cell keeps these same-coset neighbours, so its reconstruction
has the same completeness argument. No sampled distant site check is used.

Interior corner phases are independently reconstructed from the two outgoing
rays at each vertex. Bounds theta_P>60 and theta_Q>90 are decided exactly
by rational dot/cross inequalities. Weak compositions are independently
generated for totals1 through5 (five distinct P phases), and1 through3
(four distinct Q phases). This checks all251+34=285 multisets. Only the
all-five P phases have real product, which is negative; its size5 excludes
the half-star domain size<=2. No Q product is real. Certificate phase order
is separately accounted for when reproducing each retained product.
This is a complete necessary-star test, not just a selected star list.
At a native vertex a monohedral tiling has at least one native corner;
at most one straightpi sector can coexist with it. Thus the complete
native sum is eitherpi or2pi. Reflections leave angle values unchanged.
No edge-to-edge or orientation condition is smuggled into omission exclusion.

For the parent, the verifier translates the P polygon into its actual d
position and inverts it for the -d cell. It splits every boundary segment
at every available collinear vertex, cancels opposite directed subsegments,
and independently reconstructs exactly the14 retained outer boundary
segments. Area1 and four negative turns are independently verified. Interior
disjointness follows from the infinite Voronoi definition, while the two
full shared sides give connected interior. Periodic site triples partition
all cells, proving global parent compatibility rather than a finite patch.

The modified octagon is independently reconstructed; its failure of central
symmetry is checked by all opposite-vertex sums. The original octagon has
central symmetry and P has a different side count, so no reflection or
rotation can identify it with either. Z² supplies a uniform covering radius,
so one site displacement affects cells only in a bounded region; both
original classes survive away from the defect. The site's nonperiodicity
argument is valid: S symmetric-difference(S+t) is Z²-periodic and, if
S' is t-invariant, finite; hence it is empty. The finite nonempty
S symmetric-difference S' would then be t-invariant, impossible for t!=0.
This does not assert tile-set nonperiodicity merely from site nonperiodicity;
the accepted obstruction is the additional congruence class.

## Replay, defects and uncertainty

Executed:

    mise exec -- conda run --no-capture-output -n arisearch python research/reviews/resumed_higher_voronoi_verify.py

Exit0. PASS: independent exact Voronoi cells, finite-domain completeness,
285 corner multisets, parent boundary and defect third class.

No mathematical defect requiring repair was found. The checks use exact
Fractions and integers; angular sorting in reconstruction uses exact cross
products, not floating-point tolerances. No new parameter enumeration was
performed. The shape pair is decisively periodic and hence fails the original
aperiodicity goal. Parent repetition supplies no hierarchy recognition or
aperiodic source decoder. No novelty or unrestricted impossibility claim
is validated.
