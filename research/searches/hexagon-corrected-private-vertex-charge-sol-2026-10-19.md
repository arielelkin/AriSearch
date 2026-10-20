# Corrected pair: vertex and edge charge design cycle

2026-10-19. Status: **blocked at global incidence consistency**.
An exact feasible ledger defeats this specified additive balance mechanism;
no plane tiling, untileability theorem, or aperiodicity result is established.
No patch growth, larger periodic quotients, log edits, or Git operations.

## Exact setting and corner inventory

A=(5,3,3,4,4,2), B=(1,3,3,2,2,4), with closure imbalances +1,-1.
The full-edge/trivalent/common-heading structural reduction is a reviewed
dependency. A_i means native corner between sides i-1 and i, modulo six.
All rotations and reflections are allowed. Unordered corner pairs are:

|i|A_i|B_i|
|---|---|---|
|0|25|14|
|1|35|13|
|2|33|33|
|3|34|23|
|4|44|22|
|5|24|24|

A vertex with ray lengths x,y,z has corners xy,yz,zx. Enumerating
1<=x<=y<=z<=5 and all native corners realizing those three unordered pairs
gives exactly 28 unordered native-corner multisets. This includes repeated
corner indices belonging to different copies of the same species. It does
not force three corners to belong to the same tile. Because reflections
are unrestricted, every listed triple can be placed as three 120-degree
corner sectors locally. This assertion concerns sectors, not global completion.

## Stronger endpoint balance from the private sides

Every side 5 mates A to A along each A's unique side 0; similarly every
side 1 mates B to B along each B's unique side 0. At their endpoints,
an AA private-edge dimer either has two stars containing (A_0,A_1),
or one star with (A_0,A_0) and one with (A_1,A_1). Thus the total
number of doubled-A_0 stars equals doubled-A_1 stars. For B the same
identity holds. This uses endpoint wiring of the private edge and is
stronger than independent corner balance alone. It does not prescribe
the other four sides of a tile or a dimer boundary recursion.

## An exact feasible ledger

Take formal tile counts N_A=6,N_B=18 and the following vertex counts:

|native corner multiset|count|ray lengths|
|---|---:|---|
|A_0,A_1,B_3|6|2,3,5|
|A_2,B_1,B_1|6|1,3,3|
|A_3,B_0,B_1|6|1,3,4|
|A_4,B_0,B_0|6|1,4,4|
|A_5,A_5,B_4|3|2,2,4|
|B_2,B_2,B_2|4|3,3,3|
|B_2,B_3,B_3|6|2,3,3|
|B_4,B_4,B_4|2|2,2,2|
|B_4,B_5,B_5|9|2,4,4|

Each A_i occurs exactly six times and each B_i exactly eighteen times.
There are 48 vertices. Private A dimers can have their six mixed endpoint
stars paired into three dimers. Private B dimers can pair their six
mixed stars into three dimers and their six doubled-B_0 stars with the
six doubled-B_1 stars into six more dimers. Hence both private endpoint
equalities and the private-edge matching totals are satisfied.

The full side counts give formal undirected edge counts by length

    length 1:9, 2:21, 3:24, 4:15, 5:3.

There are 72 edges, and 48-72+24=0. The ray counts in the displayed
vertices agree with the same edge counts (each edge has two endpoints).
Thus adding Euler balance and unsigned length-edge conservation does
not expose a contradiction in this ledger.

These are formal counts, not a claimed cell decomposition of a torus.
In particular no torus or plane can be inferred merely because Euler
characteristic vanishes. The six occurrences of a native corner class
are not yet grouped into actual globally oriented copies of a tile.

## Finite calculation and verification

The adjacent `.py` enumerates all 28 corner multisets, puts a nonnegative
rational frequency on each, requires every native corner i of species t
to have frequency N_t, normalizes N_A+N_B=1 with both positive, and adds
the two doubled-private-endpoint equalities. Z3 4.16.0 reports SAT,
N_A=1/4,N_B=3/4. Multiplying the retained rational witness by 24 gives
the displayed table. The script separately checks all corner counts
using Python Fraction arithmetic; the table permits direct inspection
without trusting the solver. No seed, numerical tolerance, search
timeout, or stochastic choice is used. The finite domain is exactly
the 28 multisets and their linear frequencies, not finite patches.

Replay:

    mise exec -- conda run --no-capture-output -n arisearch python research/searches/hexagon-corrected-private-vertex-charge-sol-2026-10-19.py

The adjacent `.json` retains native inventory and exact witness weights.
Initial implementation failures (string quoting, symbolic Boolean extraction)
were corrected before the retained SAT result; they support no claim.

## What failed and the exact remaining obligation

Any contradiction obtained solely by a linear combination of these
corner-conservation equations, nonnegative local-star frequencies,
private-endpoint equalities, and unsigned edge/Euler counts would also
contradict the explicit feasible vector. Thus this particular scalar
balance mechanism cannot prove untileability. This statement does not
exclude charges depending on heading, chirality, paths, or larger motifs.

The precise missing extension lemma is: assign all six native corners
simultaneously to each face of the complete honeycomb, with a single
phase and reflection for that face, so that every across-edge endpoint
identification and length match holds. The ledger only identifies how
many corners and stars may occur; it supplies no such simultaneous
assignment and does not even claim its particular frequencies are realizable.
Conversely an obstruction would have to rule out every such assignment,
not just this ledger. No heading-dependent conserved charge or explicit
row transfer satisfying that obligation emerged in this design cycle.
The existing local counts and the separate index<=6 negative carrier
test establish neither implication. Under protocol section 5 this
balance route stops here unless a materially new global invariant or
explicit consistent wiring construction is supplied. The parallel
private-dimer boundary investigation is outside this artifact's claims.
