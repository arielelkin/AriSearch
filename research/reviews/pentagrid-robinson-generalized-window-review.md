# Fresh review: generalized-source window gate

**Verdict: VALID** for the finite generalized regular-source membership gate,
the actual two retained full-U source occurrences, and V exclusion from the
local tiling-space closure of regular generalized sources. No global U/V
macro repartition or shape-only forcing is established.

## Exact claim and independent computation

The domain is all 213 mandatory boundary objects and all 196 retained full
assemblies, reconstructed from the earlier independently checked geometry
certificates. The new producer permits an arbitrary three-dimensional
internal shift, including a noninteger coordinate sum. Its certificate is
`research/certificates/pentagrid-robinson-generalized-window.json`.

The independent verifier is
`research/reviews/verify_pentagrid_robinson_generalized_window_independent.py`.
It imports neither the generalized producer, circuit enumeration, an LP
solver nor a polyhedron backend. It reuses only the independent proper-window
native graph/lift and generator-cross-product facet reconstruction. For every
object it checks the complete source index domain, side words, actual integer
vertex lifts and layer interval. It then verifies either a width failure,
a positive shifted-window slack at every vertex/facet, or a selected 2--4-row
Farkas obstruction whose nonnegative weights annihilate all three internal
normals and give a nonpositive constant sum.

| Domain | Objects | Width failures | Dual failures | Strict witnesses |
|---|---:|---:|---:|---:|
| Mandatory U |28|4|20|4|
| Mandatory V |185|145|40|0|
| Full U |28|6|20|2|
| Full V |168|135|33|0|

All 409 objects were checked. Six positive shifts, 113 exact duals and 290
width failures account for the entire domain. An initial independent replay
had an incorrect hardcoded aggregate count after all object-level assertions
passed; the aggregate was corrected without changing any data or geometric
check. The successful command is:

```text
conda run --no-capture-output -n arisearch python research/reviews/verify_pentagrid_robinson_generalized_window_independent.py
```

## Positive source membership is stronger than a numerical window pass

Each full object consists of genuine unit rhombs. The native integer edge
lift turns each into one complete integer unit 2-facet; the connected graph
has a single translation gauge. All vertices at the certified shift lie
strictly in the strip. Convexity of the strip therefore puts every whole
selected 2-facet inside it. Source membership persists in a nonempty open
neighborhood of that shift. Avoiding the countably many nontrivial affine
hyperplanes where an integer point reaches a strip support facet gives a
regular intercept within this neighborhood. The regular whole-facet
cut-and-project theorem then selects these same facets in an infinite
edge-to-edge generalized rhomb tiling. Thus the two full U positive rows
really occur in regular infinite generalized sources. A mandatory-only
positive result is not asserted to complete the macro interior.

The reference construction and generalized/proper distinction are in
[Fernique--Lutfalla, Section 2.3](https://arxiv.org/html/2211.08239v2#S2.SS3).
Vertex membership is used as a necessary condition for every object and,
only for an already complete collection of actual integer 2-facets, as the
convex-strip sufficiency just explained.

## Closure and singular scope

A finite exact rhomb patch in the local tiling-space closure of regular
sources must occur in one regular approximant. This is the usual local
tiling topology with an arbitrarily small global translation and eventual
agreement on bounded regions. Equivalently, fixed finite source directions
and unit edge lengths give finite local complexity and rigid finite edge
coordinates. A mandatory boundary object inside an alleged limit source can
be included in a finite whole-rhomb patch, and that patch transfers to an
approximant. The V negative certificate would reject it there. Hence no V
boundary object occurs even in this local closure.

This does not assert that an arbitrary all-facets selection at a singular
closed-window intercept is a tiling, nor that every such selection belongs
to that local closure. The claim does not need either assertion. Ordinary
proper Penrose sources are an independently excluded subfamily; positive
U generalized shifts do not repair the proper-source compiler.

## Remaining uncertainty

None remains in the stated finite/source conclusions. The 28/185 mandatory
word completeness is an explicit upstream dependency. Alternate V residual
fillings cannot escape a mandatory-boundary rejection. No source containing
only the U clusters supplies a two-class macro repartition, and no unrestricted
U/V untileability or aperiodicity conclusion follows.
