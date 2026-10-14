# Independent review of the fixed Ammann cross-source resections

Date: 2026-10-14. Reviewer did not develop the four source records.
**Verdict: VALID for the fixed local boundary gates, corrected J-star 5/7
witness, source-cover count obstruction, and stated omission conclusions.**
No mixed 5/7 plane tiling, decoder, aperiodicity, or arbitrary-resection
exclusion is established. The root independently rereviewed the new pentagon
omission argument and lattice comparison/coverage argument.

Reviewed records: `contact-structure-ammann-{corner-triad-gate,
double-corner-gate,double-corner-six-six-escape,j-star-resection}.{py,md}`
(the 6/6 escape is documented in the double-corner note).
The [independent checker](verify_ammann_cross_source_resections_independent.py)
imports no producer. It reconstructs the exact J=1/2+(4/5)ζ fixture in
Q(ζ), ζ⁴−ζ³+ζ²−ζ+1=0, with the specified embedding ζ=exp(iπ/5).
Conjugation is the field homomorphism ζ↦ζ⁻¹. Cross products divided by
positive sin(π/5) lie in the real subfield; exact algebraic signs decide
supports, separation, turns, and lattice bounds. No decimal display decides
a branch, and no source genericity or infinite tiling is inferred from local
coordinates alone.

For each patch the check proves strict convexity of its constituent source
faces, pairwise disjoint interiors, uniqueness of directed edges, complete
reversed-edge cancellation, a single simple outer boundary, nonflat turns,
and exact signed-area conservation. Thus omitted components, boundary holes,
overlaps, and accidental collinear corners are checked independently.

The single K-corner triad has 10 outer sides and reflex endpoints 1,ζ⁻²L.
Their boundary arcs have 3/7 edges. For any partition into two convex bodies,
the separating line contains their common interface. Each reflex boundary
corner must be shared: a convex body containing the whole local reflex
neighborhood would contain points outside the patch. A reflex point cannot
lie inside the interface, since then both bodies occupy opposite half-discs
and their union fills a full neighborhood. The reflex points must therefore
be the seam endpoints. The forced arc boundaries have at most 4/8 genuine
sides, excluding two outputs both with at least five sides. This is a
necessary-side-count gate; convexity of both forced arc polygons is not
asserted or needed.

All four double-corner alternatives were retained. Their (outer sides,
reflex corners) are respectively (12,3),(11,2),(11,3),(10,2), for (H,H),
(H,P2),(P1,H),(P1,P2). The three reflex points are noncollinear in the two
three-reflex branches. In the other branches the forced arc boundaries have
6/7 and 6/6 sides, with exact nonzero endpoint cross products. Hence a
convex two-piece partition cannot conceal a pentagon through a flat seam
endpoint. This fails only the pentagon preference. The 6/7 branch’s tileability remains
unclassified, but any convex realization is excluded from aperiodicity by
the reviewed [hexagon/higher-side theorem](../lemmas/hexagon-limit-and-periodicity.md).
This conclusion imports that theorem’s unrestricted monohedral hexagon
classification and was independently checked during root integration.

The J-star patch also has 10 outer sides, with exactly two reflex corners
1,ζ and 4/6 boundary arcs. Both forced halves are strictly convex and have
5/7 genuine sides, disjoint interiors and exactly the total source area.
**Defect found:** the original note interchanged heptagon labels B1,B0.
The correct order is (1,A3,A4,1+ζ,B0,B1,ζ). The original producer's boundary
slice already used the correct order, so its exact witness is unchanged.
The repaired producer defines both halves by named corners and asserts
agreement with the traced boundary. This prevents the documentation error
from silently changing the retained geometry.

## Omission and whole-plane checks

For the J-star pentagon C=(ζ,J″,0,J′,1), set
ρᵢ=(Cᵢ₋₁−Cᵢ)/(Cᵢ₊₁−Cᵢ). Its argument is the interior angle θᵢ in (0,π).
Exact cross products prove θᵢ≥2π/5 for all i; θ₂=2π/5, and the other four
inequalities are strict. A 2π native-corner multiset has at most five
corners, while a π multiset has at most two. The checker examines every one
of the 251 nonempty multisets of size at most five. A 2π sum necessarily
makes ∏ρᵢ^mᵢ positive real. The only positive-real product is
m=(0,0,5,0,0), which indeed sums to2π. No multiset of size at most two has
negative-real product, excluding every π sum. These implications use exact
field identities and real signs, without inverse trigonometric evaluation
or a classification of known pentagon families.

At a T-junction the native corners on the opposite side of a straight tile
edge sum toπ; this is excluded. At every remaining vertex native corners
sum to2π. The only available vertex consists of five copies of C₂, so the
other four corners of each placed pentagon cannot be surrounded. Therefore
this pentagon admits no monohedral plane tiling, including reflections and
partial contacts. The heptagon alone is untileable by the independently
reviewed [global >=7-side theorem](../lemmas/side-count-and-monohedral-obstructions.md).
These conclusions remove omission only; mixed periodic tilings are open.

For the 6/6 pair, the second hexagon has equal opposite edge vectors with
opposite directions. The independent check derives the two congruent
representatives f,g=t−f and periods a,b from this identity, rather than
trusting the producer's endpoint gluing alone. It computes exact bounding
boxes in lattice coordinates. Every translate whose box can intersect a
motif box lies in the finite integer ranges obtained by exact ceilings and
floors of box differences. All such nonidentity comparisons have disjoint
interiors by exact supports. The two motif areas equal the positive lattice
covolume. Hence periodization fills a fundamental cell almost everywhere;
the locally finite union of compact polygons is closed, so an uncovered
point would have an open positive-area neighborhood, a contradiction.
This proves an actual rank-two Q-only periodic omission escape, without
assuming a finite patch extends.

A global cover solely by disjoint bounded whole H/P1/P2 triads would give
h(R)=p1(R)=p2(R)+O(R). For a source in the reviewed generic Ammann class,
the [anchored-count theorem](../lemmas/ammann-anchored-count-split-fixed-cluster-obstruction.md),
Lemmas1–2, gives p1/h,p2/h→φ and h=Θ(R²). Thus that particular global cover
is impossible. This imports the reviewed reconstruction and hierarchy;
local patch geometry alone gives no frequency theorem. It does not exclude
fractional transfers, different macro contents, or a mixed 5/7 tiling not
obtained from that whole-triad cover.

## Repairs, replay, and limits

Besides the B0/B1 label repair, the 6/6 producer now selects its named
(P1,P2) fixture explicitly instead of inheriting the final loop state.
Each double-corner branch asserts its expected side/reflex counts, and the
J-star asserts both the exact 10-side boundary and the two seam endpoints.
No original output polygon changed. The root independently rereviewed these repairs, including the exposed
B4,B0,B1,B2 native boundary and explicit fixture selection, as recorded in
the [checkpoint audit](checkpoint-diff-audit-2026-10-14.md).

Replay from the repository root:

```text
mise exec -- conda run --no-capture-output -n arisearch python research/reviews/verify_ammann_cross_source_resections_independent.py
```

All four producers and the independent checker pass. There is no solver,
random seed, timeout-based negative conclusion, or unexhausted enumeration.
Sage number-field and real-algebraic arithmetic remain shared trusted
dependencies. The mixed 5/7 pair still requires full-plane existence and
universal source reconstruction/periodic-escape exclusion. The broader
two-convex-tile target remains unresolved.
