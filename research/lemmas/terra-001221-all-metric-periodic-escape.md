# Generic ternary A001221: a mixed ring forces equilateral A

Date: 2026-10-13. Status: internally proved with separate native certificate
checker PASS; independent hostile review VALID. Restricted family theorem.

## Theorem

Let A,B be actual strictly convex hexagons with angles respectively two copies
of each x,y,z and of r=360-2x,s=360-2y,t=360-2z, where x+y+z=360 and90<x,y,z<180.
Assume six distinct angle values and exactly the five trivalent star types
AAA=(x,y,z), BBB=(r,s,t), AAB=(x,x,r),(y,y,s),(z,z,t).
A has native cyclic angle word001221. B has arbitrary native order and metric;
A has arbitrary actual side lengths, including all additional equalities.
Every tileable pair admits a periodic tiling with omission permitted,
including reflections and original partial contacts.

Dependencies: reviewed defect-free hexagon limit and unrestricted monohedral
periodic escape in [hexagon-limit-and-periodicity.md](hexagon-limit-and-periodicity.md),
reviewed no-ABB propagation in [ternary stars](two-hexagon-ternary-angle-star-balance.md),
reviewed honeycomb/native indexing in [one-B rings](two-hexagon-one-b-ring-spatial-reduction.md),
and the sufficient Reinhardt H1 periodic family in the refreshed primary
[source](https://arxiv.org/html/2508.01404v2).

## Only one B native word can occur in a mixed field

The reviewed limit supplies a connected defect-free field. A pure field gives
a monohedral periodic escape, so consider a genuinely mixed field. Its B cells
have no B neighbours; every B vertex is same-colour AAB. Every AB edge therefore
matches A colours to B colours at each spatial endpoint. A001221 has unordered
native side endpoint pairs

    00,01,12,22,12,01.

Thus B has neither11 nor02 edges, regardless of side-length coincidences.
Let n_ij count B edges of pairij. Its two occurrences of colour1 give degree4,
so n_01+n_12=4. Its two colour0 and two colour2 corners give
2n_00+n_01=4 and2n_22+n_12=4. Hence n_00+n_22=2.
Each of n_00,n_22 is at most1, since two positions of a colour have at most
one joining cycle edge in a six-cycle with all three colours present.
Therefore n_00=n_22=1 and n_01=n_12=2. The00 and22 consecutive blocks must
be joined by the two isolated1 corners. This uniquely gives B001221 up to
rotation/reflection. The exact checker also tests all11 bracelets directly.

## Complete native ring gate

Use standard honeycomb slots: a B centre has A neighbours A_k, k modulo6.
The AB side compares B side-slot k-1 with A_k side-slot k+2. Its endpoint
colour constraints are

    A_k.corner(k+2)=B.corner(k),
    A_k.corner(k+3)=B.corner(k-1).

For A001221 and B001221, every B side has exactly TWO native A placements
satisfying those ordered endpoint conditions, among all12 rotations/reflections.
For00/22 this is the two endpoint orientations of a unique native side;
for01/12 it is the two possible native A sides of that pair. Hence each
indexed B placement has2^6=64 complete AB colour rings. Retaining all12
indexed B placements gives768. This contains all actual mixed B rings,
without assuming a B side metric or geometric realization of every formal ring.

Consecutive A neighbours share an AA side. Its native length equality is

    A_k.side(k+1)=A_(k+1).side(k+4).

For EACH of the768 rings, regard these six equalities as undirected edges
on the six native A side indices. The exact finite checker proves this
six-vertex graph CONNECTED in every case. Therefore any metrically legal
ring forces all six actual A side lengths equal. No positivity, closure,
outer AAA completion, spatial successor or torus search is needed for this
necessary equality implication.

The retained producer also projects these graphs through all203 equality
partitions of six A sides, including all further specializations. Exactly the
single all-equal partition retains any AA-compatible ring. It retains all768;
every other partition retains zero. This confirms all-metric coverage rather
than inferring further specializations from a few minimal patterns.

## Immediate omission escape

If any genuinely mixed field exists, A is equilateral. Its native corners
1,2,3 have colours0,1,2 and angles summing360. Its native side3 equals side0.
After cyclic relabelling starting at corner1, these are exactly Reinhardt H1:

    angle0+angle1+angle2=360, side2=side5.

An ACTUAL convex polygon satisfying this sufficient family has a periodic
monohedral tiling. Its existence is already part of the actual-field hypothesis;
no formal equality partition is promoted to a polygon. Omitting B gives an
admitted periodic tiling of the pair. Together with the pure-limit case,
this proves the theorem at every actual metric in the stated angle stratum.

## Exact certificate, replay and scope

[Producer](../searches/terra-001221-all-metric-native-rings.py),
[certificate](../certificates/terra-001221-all-metric-native-rings.json),
[independent checker](../reviews/verify_terra_001221_equal_length_gate.py).
The checker imports no producer and uses graph reachability for the equality
closure. Its finite domain is11 B bracelets,12 native B placements,64 native
A tuples per surviving B placement, and203 actual A equality partitions.
Native side/corner reflection maps are included explicitly. Only standard
library integer operations are used; there is no solver, seed, timeout,
floating-point geometric decision or bounded tiling inference.

    mise exec -- conda run --no-capture-output -n arisearch python research/reviews/verify_terra_001221_equal_length_gate.py

Output PASS. The native record contains outer corner and B-metric diagnostics,
but the theorem needs only the earlier connected-AA-graph gate; these further
diagnostics are not assumptions. No infinite mixed tilability or universal
nonperiodicity is asserted. Extra-angle-star strata and other A native words
remain outside this theorem. Next obligation is fresh hostile review, then
another genuinely uncovered native/angle mechanism rather than enlarging the
completed768-case domain.

Fresh independent review: [VALID](../reviews/terra-001221-all-metric-periodic-escape-fresh-hostile-review.md).
