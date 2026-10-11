# Exact all-shift gate for the fixed Robinson U/V compiler

Question: do the fixed compulsory boundaries or retained complete assemblies
occur as whole coordinate rhomb facets of a regular generalized pentagrid
source with the Penrose slope, allowing all real internal shifts?

The [reviewed theorem and closure checklist](../lemmas/pentagrid-robinson-generalized-source-gate.md)
state source scope, upstream dependencies, positive occurrence, exclusions
and non-consequences. The [independent review](../reviews/pentagrid-robinson-generalized-window-review.md)
returned VALID.

## Exact domain and encoding

The boundary-completion certificate supplies28 mandatory U and185 mandatory
V objects. The residual certificate supplies28 positive full U and168
positive full V objects. These409 objects are fixed; no domain enlargement,
new residual search or new macro is used. Whole source facets have canonical
Z^5 lifts, independently reconstructed by the proper-window checker.
Internal coordinates I annihilate the fixed physical plane and have3 real
coordinates (m,A,T). The zonotope I([0,1]^5) has20 facets over Q(sqrt5).

For each facet normal the minimum of its constants over the object's lifted
vertices compresses the full strict system to20 inequalities. The producer
enumerates all6175 subsets of2,3,4 normals and retains220 positive minimal
kernel dependencies. A selected dependency with nonpositive constant sum
certifies strict infeasibility. A strict layer span must be less than5.
Otherwise a Q(sqrt5) field-backend polyhedron supplies an exact interior
shift, and every original vertex/facet inequality is checked strictly.
No floating-point feasibility decision, stochastic seed or grid of shifts
is used. Canonical lift translation has no effect on existence of a shift.

## Execution and completion

Replay environment: Python3.12.13, SageMath10.9, Linux x86_64, Conda arisearch.
The search uses Sage exact matrices and Polyhedron with the field backend;
there is no SAT/SMT solver. One120-second deadline covered the entire domain.
It completed in5.053148557999521 seconds. The first invocation failed at
Sage-version serialization before testing any object; the same domain was
rerun after correcting that implementation error. Neither domain nor
deadline increased. No timeout, interrupted enumeration or memory failure
is reported as an exclusion.

| Domain | Width rejection | Small dual rejection | Strict witness |
| --- | ---: | ---: | ---: |
| Mandatory U28 |4|20|4|
| Mandatory V185 |145|40|0|
| Full U28 |6|20|2|
| Full V168 |135|33|0|

Thus290 width rejections,113 exact duals and6 strict witnesses certify all409
objects. Full U rows7 and8 have open strict acceptance regions; choosing a
regular shift in such a region establishes infinite generalized-source
occurrence. Every mandatory V fails independently of a residual filling.
Local matching closure transfers that finite-patch exclusion. Arbitrary
singular selections outside that closure remain unclassified.

## Retention and nondestructive replay

Producer and exact certificate:

    conda run --no-capture-output -n arisearch python research/searches/pentagrid-robinson-generalized-window.py

The normal invocation emits JSON to stdout. Only explicit --output writes a
certificate. Its elapsed_seconds field is runtime metadata, so the producer
is not registered as a byte-for-byte or whole-JSON deterministic comparison.
Its certificate is checked instead by the registered independent verifier:

    conda run --no-capture-output -n arisearch python research/searches/verify.py --only verify_pentagrid_robinson_generalized_window_independent.py

The independent checker imports no producer or polyhedron backend; it
reconstructs facets and lifts through the independently reviewed proper-gate
checker and verifies every width, positive dual and all original positive
facet inequalities. Retained source certificates are inputs and are never
overwritten. The result closes this fixed compiler; it does not exclude
other cuts, scales, metrics, slopes or unrestricted U/V plane tilings.
