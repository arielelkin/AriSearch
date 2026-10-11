# Two specified two-cross Cairo arm patterns: exhaustive event-flat record

Date: 2026-10-10. Python 3.12.13, SageMath 10.9. Exact Q(sqrt3), positive
embedding1<sqrt3<2. No seed, timeout, numerical decisions, symmetry quotient,
patch bound, or codimension cutoff. Status: completed exact enumeration;
mathematical conclusions are independently reviewed VALID at research/reviews/partial-contact-cairo-two-cross-event-flats-review.md.

Question: which metrics with internally four-distinct arms and exactly
Pa=Qa,Pb=Qb (adjacent) or Pa=Qa,Pc=Qc (separated) retain every native120
corner under the reviewed necessary partial-contact relation?

Domain: the complete13-form adjacent or26-form separated homogeneous
intersection lattice in its4-dimensional native closure kernel. Eight
native arms remain distinct slots, while the two declared cross pairs
identify numerical length labels. There are six numerical arm labels.
Adjacent has six self-bank event totals and no nonself total. Separated
has those six self totals plus cross-bank totals Pb+Qb and Pd+Qd.
Every event-total difference is included except one forcing an undeclared
arm equality: self/self comparisons, or a self total against a cross total
containing that label. Those omitted index pairs are retained explicitly.
All eP/event, eQ/event and eP=eQ forms are included, even when dependent.

Rows are canonical exact RREF. Every proper contact hyperplane is added
recursively, including descendants of native-corner-negative strata.
Only hereditary extra arm identities and certified empty positive cones
prune descendants. Dimension1 has no positive proper descendants. The
field polyhedron solves all ten lengths>=1; homogeneity makes this
strict positivity. Every empty cone retains nonnegative sum1 Gordan
weights annihilating all ten length forms. Every positive cone retains
actual eight-arm/two-e values and kernel coordinates.

The actual native-slot compatibility and all56 unordered120 triples with
8 reflection choices are used. There is no transitive closure, inherited
sole-cross core geometry, or assumption that a local survivor extends.
Both shapes must occur because either four-distinct-arm shape alone
cannot tile by the reviewed private-arm theorem.

Completion:

| Pattern | Full visited domain | Extra arm identity | Exact Gordan empty | Missing120 corner | Local survivor |
|---|---:|---:|---:|---:|---:|
| adjacent | 107 | 77 | 2 | 28 | 0 |
| separated | 547 | 266 | 92 | 151 | 38 |

The separated survivors have twelve dimension2 kernels and twenty-six
dimension1 kernels. Every dimension2 kernel has actual normalized native
sidewords, exact positivity interval, all proper event/privacy ratio cuts,
and actual generic samples in every open arm-order chamber. Dimension1
positive fixtures already avoid every proper form since its only root is
zero. Higher dimensional positive fixtures need not themselves be generic;
strict positivity is open and a finite union of proper hyperplanes cannot
cover it. No metric is discarded merely because its positive witness has
an accidental undeclared equality.

    conda run --no-capture-output -n arisearch python research/searches/partial-contact-cairo-two-cross-event-flats.py --output research/certificates/partial-contact-cairo-two-cross-event-flats.json
    conda run --no-capture-output -n arisearch python research/searches/partial-contact-cairo-two-cross-event-flats.py --pattern adjacent
    conda run --no-capture-output -n arisearch python research/searches/partial-contact-cairo-two-cross-event-flats.py --pattern separated

Retained producer and exact certificate use this stem. The adjacent full
family obstruction follows from complete finite necessary elimination,
subject to fresh independent review. The separated output is only a
38-stratum necessary reduction, with no existence or periodicity claim.
No general two-cross pattern classification or global problem resolution
is implied. An initial producer edit had a Python syntax typo before the
first completed run; it was repaired before any certificate was written.

Fresh root audit found an event-bank metadata name-shadowing defect: the
native event-bank list was overwritten by the local120 star sectors before
serialization. The actual event rows, constraints, BFS, duals, compatibility
and strata were already computed independently of that overwritten name.
Both producers now name those local sectors separately. Native bank metadata
was reconstructed directly from actual declared arm labels and the complement
map and its vectors checked exactly against the original event rows. A full
producer replay then reproduced the entire repaired certificate exactly;
no flat, dual, fixture, star, count, or normalization changed. Fresh independent review is VALID on this repaired version.
