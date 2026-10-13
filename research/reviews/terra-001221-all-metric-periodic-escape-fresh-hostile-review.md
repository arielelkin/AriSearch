# Fresh hostile review: A001221 mixed rings force an omission escape

Date: 2026-10-13. Independent reviewer: sol, distinct from terra author.
**Verdict: VALID** for the stated complementary ternary five-star language,
actual strictly convex polygons, arbitrary metrics and arbitrary B order.
Its S3 colour orbit also covers A002112 and A011022. No global pair theorem
or extra-star angle coverage is inferred.

## Native B exclusion is metric-independent

NoABB propagation in a genuinely mixed defect-free connected field isolates
every B. Both A neighbours at each B vertex have that B colour. Along an
AB side its endpoints must therefore have the same unordered colour pair
on A and B. For A001221 the only pairs are00,01,12,22; lengths merging does
not create11 or02 native endpoints. Two occurrences of each B colour give
n01+n12=4,2n00+n01=4,2n22+n12=4. Thus n00+n22=2, and each of n00,n22 is
at most1 in the six-cycle. Both equal1. The00 and22 blocks are separated
by the two isolated1 positions, uniquely giving001221 up to dihedral
reindexing. The independent check of all11 bracelets confirms this proof.
No metric or polygon closure is assumed in removing other B orders.

## Complete64/768 necessary ring domain

Every B side has exactly two ordered-endpoint-compatible A placements among
all12 native rotations/reflections: for00/22 there is one native A side and
two endpoint orientations; for01/12 there are two native A sides and one
orientation each. These statements concern colours, so all additional length
coincidences preserve completeness. A B native length may subsequently force
or eliminate one of these options; checking both is a sound enlargement.
There are exactly2^6=64 rings per central placement and12 indexed central
placements, hence768 rings. Native reflections map edge i to r-i-1.

I independently numbered A neighbours by central SIDE i, rather than the
producer's side k-1 convention. Shared A endpoints are i+3,i+4 and shared
side i+3; adjacent neighbours' mandatory AA sides are i+2,i+5. This shifted
reconstruction compares every actual native tuple against the certificate
and its AA equalities, without importing author code. It is consistent with
the reviewed honeycomb cell topology. AAA holes are allowed outside the ring;
a one-B species coset or globally allAAB field is not assumed.

For each of the768 rings, the six necessary AA equalities form an undirected
multigraph on the six native A side positions. Independent BFS reaches all
six vertices, including possible loops and repeated edges. Equality is
transitive, so all six actual lengths must agree. This is a finite COMPLETE
necessary obstruction, not failure of a bounded patch search. No outer
completion, infinite extension or solver result enters the implication.

Both retained checkers also enumerate every Bell(6)=203 equality partition.
Only the all-equal partition retains AA-compatible rings, and it retains all
768. Every other exact partition has zero. Thus further specializations are
explicitly included, not inferred from minimal equality patterns. Positivity,
exact closure and convexity remain assumptions on the actual input shapes;
formal all-equal length words are not promoted to actual polygons.

## Periodic escape and original quantifiers

If a genuinely mixed field exists, its actual A is equilateral. Native
corners1,2,3 carry all three A colours, whose angles sum360; native sides3,0
are equal. Reindexing the polygon to begin at corner1 gives precisely the
SUFFICIENT Reinhardt H1 conditions. The named reviewed source supplies an
actual monohedral periodic tiling by A. No completeness of a monohedral
angle-only filter is required. B may be omitted under the original problem.

Any source tiling first supplies the previously reviewed defect-free limit,
possibly omitting a species. A pure limit has a monohedral periodic escape;
a mixed limit has the H1 escape just proved. Hence every tileable pair in
the stated family admits a periodic tiling, including source reflections and
partial contacts. The original tiling is not asserted edge-to-edge, pure or
periodic. No limit, monohedral or global honeycomb dependency was re-audited
without cause; their applicability is exact here.

## S3 integration and replay

Permuting the three angle names and their complementary B names preserves
all hypotheses and the arbitrary-B quantifier. Independent canonicalization
of all six colour permutations gives exactly the bracelet orbit
001221,002112,011022. The theorem therefore covers all three A words at every
actual metric in its stated angle language. It does not cover unrelated
bracelets merely because they have the same multiset.

    mise exec -- conda run --no-capture-output -n arisearch python research/reviews/verify_terra_001221_equal_length_gate.py
    mise exec -- conda run --no-capture-output -n arisearch python research/reviews/verify_terra_001221_connected_graphs_independent.py

Both outcomes: PASS. Eleven B bracelets,12 central placements,64 choices
each,768 connected equality graphs,203 side partitions and the exact three-word
S3 orbit. Native integer operations and graph reachability only; no solver,
seed, timeout, floating-point threshold, metric rank extrapolation or unproved
patch-to-plane extension. The original research problem remains unresolved.
