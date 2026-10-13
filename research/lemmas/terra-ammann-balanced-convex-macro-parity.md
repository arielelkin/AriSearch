# Balanced convex whole-Ammann supports have even side count

Date: 2026-10-13. Status: [fresh independent hostile review VALID](../reviews/terra-ammann-balanced-convex-macro-parity-fresh-hostile-review.md).
No finite search is needed. This eliminates the pentagon-containing whole-source
compiler throughout G*, not arbitrary two convex polygons or fractional cuts.

## General no-flat-dissection lemma

Let S be a finite collection of genuine compact convex polygons of positive
area. Assume NO nonempty finite multiset of their native interior angles sums
to180 degrees. Reflected/rotated copies have the same angle values. Let M be
a compact convex polygon of nonempty interior that is EXACTLY the union of
finitely many whole isometric copies of S, with pairwise disjoint interiors.
No edge-to-edge convention is imposed on this finite dissection and it need
not extend to a source plane tiling.

Then:

1. No source native vertex lies in the relative interior of another source
   edge; all positive-length source edge contacts are whole native sides.
2. Every source edge is wholly an internal shared edge or a boundary edge.
3. Every boundary source vertex is a genuine strict macro corner. Thus each
   genuine native side of M is exactly one whole source side.
4. If source tile i has n_i sides and I internal shared edges, M has

       n(M)=sum_i n_i-2I,
       n(M) congruent to sum_i n_i modulo2.

Collinear subdivisions of M are removed when defining its genuine side count.
The lemma proves none exist at source boundary vertices under its hypothesis.

## Proof, including partial contacts

Suppose a native corner of tile T lies at p in an edge interior of tile H.
H occupies a half-disc sector of angle180 at p. If p is on the boundary of
convex M, M has sector angle at most180, so H already fills all available
sector and the positive-angle native corner of T cannot fit without overlap.
If p lies in the interior of M, the other half-disc is completely covered by
incident source tiles. A second flat host filling that half-disc would leave
no room for T. Therefore every remaining incident tile contributes a genuine
native corner, and their angles sum exactly180. This contradicts the assumed
absence of180 native-angle sums. This argument uses only the finite dissection,
not source-plane extension or an intended vertex atlas.

Consequently no T-junction exists. Positive-length overlap of two source edges
has endpoints native for at least one edge; unequal overlapping segments would
place such an endpoint inside the other, so their native sides must coincide
completely. Convex source tiles sharing a whole side lie on its opposite sides;
three tiles cannot share its relative interior because their interiors would
overlap. Transverse source-edge crossings are likewise impossible by disjoint
interiors. Hence the source dissection is a planar whole-side face complex.

If any relative interior point of a source side lies inside M, the opposite
half-neighbourhood must be covered by another source tile. Their positive
edge overlap is therefore a whole-side match, making that entire open side
internal. Otherwise the whole source side is on the macro boundary. An edge
cannot be partly internal and partly boundary without an excluded T-junction.

Every macro turn is a source vertex, because the boundary is a finite union
of source sides. At such a source boundary vertex no flat host occurs by the
first result. The incident source native-corner sectors exactly fill the
macro interior angle. If that macro angle were180, their positive native
angles would sum180, impossible. Convexity bounds it above by180, so it is
strictly less than180. Thus adjacent boundary source sides never merge into
a longer collinear macro side, and every boundary edge contributes exactly
one genuine macro side. Counting source side incidences gives one for each
boundary edge and two for each internal edge. This proves the formula and
parity. Convex M has one simple boundary and no holes; a disconnected patch,
vertex-only join or hole that fails this exact-support hypothesis cannot
supply a counterexample. QED.

## Application to the generic Ammann source

Fix any J in the reviewed G* domain of
[Ammann forcing](ammann-forcing-aperiodicity.md). Its three actual unmarked
source polygons are H6 (six sides), P1 and P2 (five sides each). The reviewed
Lemma3 proves no native-angle sum180, under G2′; rotations, reflections
and arbitrary original contacts are already covered. Therefore the preceding
finite-support lemma applies before any source-patch enumeration.

If a convex whole-source macro support has balanced source contents(h,k,k),
its total source side incidences are

    6h+5k+5k=6h+10k,

which is even. Its genuine side count is therefore even. In particular NO
such support is a pentagon, for ANY finite h,k, including all k>=1 and all
parameter specializations inside G*. This is not an area-rank condition.

The genericity hypothesis is consequential: a parameter outside G* may admit
native180 relations, permitting collinear boundary mergers and changing the
parity of the genuine side count. Fractional cuts, new source polygons or new
boundary nodes likewise change the theorem's used hypotheses.

## Minimal proposed balanced macros and why geometry searches are unnecessary

A P1+P2 dissection has total ten source sides. Two convex polygons with disjoint
interiors share at most one whole side: two noncollinear common boundary
segments would have a convex intersection of positive area. Thus a convex
connected two-tile support has eight genuine sides; it cannot give a pentagon.
If they fail convexity, that is already outside the support hypothesis.

An H6+P1+P2 dissection has sixteen source sides and at most three pairwise
shared sides among its three source tiles. Hence any convex support has at
least ten genuine sides (twelve for a two-edge contact tree, ten for a
three-edge contact cycle). Neither connected placement can be a pentagon.
No vertex-valence3 fusion assumption or restricted contact atlas is used;
the reviewed source includes higher-valence stars and the proof allows them.
The universal parity statement makes enumeration of these2/3-tile contacts
uninformative for the requested pentagon partner.

## Combining with uniform unmarked resection

The independently reviewed
[uniform-resection theorem](ammann-supported-pair-uniform-resection-obstruction.md)
states that if two convex unmarked supports each have whole-source dissections
and admit a tiling, every such support dissection has fixed BALANCED contents
(h,k,k), throughout G*. That theorem explicitly includes reflections, omitted
macro types and arbitrary unmarked resection; no area independence is required.
Applying parity to each support shows both have even genuine side counts.

If a support has four sides, it admits a periodic monohedral quadrilateral
tiling, so the pair cannot be aperiodic by omission. Convex polygons have at
least three genuine sides; even count therefore gives minimum four.
If both counts are at least six and one exceeds six, the reviewed
[side-count/hexagon limit reduction](hexagon-limit-and-periodicity.md) excludes
aperiodicity (both above six are untileable; a hexagon-plus-higher polygon has
a monohedral periodic escape when tileable). Thus the ONLY remaining potentially
aperiodic two-convex-support whole-Ammann compiler in this domain has two
hexagons. No such compiler is constructed or excluded here.

Consequently the balanced whole-source route does not provide a distinct
pentagon-containing construction track. That track requires a concrete change
such as fractional source cuts/resections, new points/source types or a source
parameter outside G*. Reopening with bigger balanced whole-source clusters
would preserve the parity obstruction and is not justified.

## Dependencies, verification and status

Analytic proof; no search, solver, numerical coordinates or enumeration domain.
Dependencies are the reviewed no180 source-angle result, uniform unmarked
resection and global side-count/periodic quadrilateral facts. The core
no-flat-dissection lemma is self-contained and does not assume a plane source
atlas, simple cluster tree, source trivalence, prescribed chirality, fixed
area rank or an extendable finite patch. Fresh independent hostile review is
required before this becomes stable programme coverage.
