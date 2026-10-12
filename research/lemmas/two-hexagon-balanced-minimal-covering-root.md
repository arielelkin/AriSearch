# A positive corner-balanced minimal covering rank-five root

Date: 2026-10-12. **Adversarially reviewed:** [fresh hostile review](../reviews/two-hexagon-balanced-minimal-covering-root-review.md).
This answers a structural coverage question negatively. It is not an
aperiodic pair or a higher-rank census. The explicit native corner order
also has an exact local spatial obstruction.

## Exact closed type and positive balance

Native A corners are 0,...,5 and B corners are 6,...,11. Set

    T = {(0,1,6), (1,2,7), (0,2,8),
         (3,4,9), (4,5,10), (3,5,11)}.

Every A corner occurs twice and every B corner once. Thus the strictly
positive weights w_t=1/3 on all six triples give

    sum_t w_t m_t = (2/3) 1_A + (1/3) 1_B.

Both species have positive normalized weights and sum_t w_t=2.
This is a positive primal balance certificate, unlike the earlier
unbalanced rank-five example.

## Exact closure and rank

Write the angle deviations from 120 degrees as x_0,...,x_11. All defining
equations become homogeneous. The polygon equations are sum_A x=sum_B x=0.
The triple equations give

    x_6=-x_0-x_1, x_7=-x_1-x_2, x_8=-x_0-x_2,
    x_9=-x_3-x_4, x_10=-x_4-x_5, x_11=-x_3-x_5.

The B polygon sum follows from the A sum and these equations. The six
triple rows are independent before adjoining polygon sums, because each
B column occurs in exactly one row. A linear combination of those rows
lies in the span of the two polygon rows only when all six coefficients
are equal: the B entries force this, and each A entry is then twice that
coefficient. This one-dimensional relation is

    sum_t m_t = 2 1_A + 1_B.

Consequently the triple rank modulo the two polygon sums is 6-1=5.

To prove full rational closure, let an implied triple contain k B corners,
with multiplicities. Let n_A(i) and n_B(j) denote its incidence counts.
The displayed formulae imply that for some common constant c,

    n_A(i) = c + sum_(j whose defining pair contains i) n_B(j).

Summing over A gives 3-k=6c+2k, hence c=(1-k)/2.

* For k=0 or k=2, c is a half-integer and cannot equal integer incidence
  counts after subtracting integer terms.
* For k=1, c=0; the two A entries are exactly the defining pair of that
  single B corner. The triple is one of the six in T.
* For k=3, c=-1 and all A entries vanish. The three B pairs would have
  to cover each A corner exactly once. But those pairs form two disjoint
  3-cycles, on {0,1,2} and {3,4,5}, which have no perfect matching.
  Repeated B corners cannot repair this, since repeating an edge already
  repeats its endpoints.

Thus **T is its entire rational closure**.

Each B corner occurs in a unique triple of T. A covering subset of T
must therefore include all six triples. Every rationally closed ancestor
is a subset of T; if it covers all corners it is T itself. Hence there
is **no proper covering ancestor at any rank**, in particular none of
rank at most three. Positive corner balance does not repair the
coverage gap caused by extending only the stored low-rank covering types.

## Exact generic angle point

An explicit point with exactly this triple type has degree angles

    angle_i = 120 + d_i/1000,
    d = (1,10,100,1000,10000,-11111,
         -11,-110,-101,-11000,1111,10111).

Both six-angle sums equal 720 degrees, all angles lie strictly between
0 and 180 degrees, and checking all 364 corner 3-multisets gives exactly T.
This is angle feasibility. It asserts neither a simultaneous side-equality
realisation nor an equilateral polygon realisation.

## Angle-only SFT: an exact local obstruction for this native order

The native cyclic orders are A=(0,1,2,3,4,5) and B=(6,7,8,9,10,11).
Use the reviewed honeycomb slot conventions: directions D_k are the six
triangular-lattice neighbours; a placement (r,s) carries native corner
r+s k at slot k, with s=+1 or -1. At the vertex of slot k of a cell, the
other two cells are D_k and D_(k+1), at their slots k+2 and k+4.

Every triple of T contains exactly one B corner. Around a B cell all
six neighbours are therefore A. For each fixed B placement, enumerate
the twelve A placements in the six neighbour positions. Consecutive
positions are allowed precisely when their two indicated native corners
are the A pair assigned to that B corner. This is a six-position cyclic
binary constraint problem, with eight allowed pairs per position. Exact
enumeration gives **one** neighbour ring for each of the twelve B placements.
The retained certificate lists all binary relations and the unique rings.

The two adjacent A neighbours at D_k and D_(k+1) share an edge. The
third cell on the other end of that edge, at D_k+D_(k+1), must be B,
because its vertex triple otherwise contains no B. Its unique neighbour
ring must agree with the first ring on those same A placements.

For k=0, compatibility is possible only for first-B placements

    (r,s) in {(0,+1),(3,+1),(0,-1),(3,-1)}.

For k=1, it is possible only for

    (r,s) in {(2,+1),(5,+1),(1,-1),(4,-1)}.

These sets are disjoint. Every B cell needs successors in both directions,
so no B cell can occur in an infinite legal configuration. Since every
allowed vertex requires a B corner, the angle-only SFT is **empty**.

The finite verifier calculates this directly by rational corner labels
and twelve-state cycle enumeration, without any SAT/LP infeasibility
verdict. Side equalities can only remove configurations, so emptiness
holds for every side-equivalence relation e for this fixed native order.
Arbitrary non-dihedral permutations of native corners define other types
and were not tested or excluded.

## Bounded solver controls

As separate controls with all side classes equal, deterministic CP-SAT
reported a legal radius-one patch and an **INFEASIBLE radius-two patch**.
All 56 Hermite-form tori of lattice index at most eight also returned
INFEASIBLE. Patch queries had a 30-second timeout; torus queries had
5 seconds each; seed zero and one worker were used. No timeout occurred.
No formal solver UNSAT logs are retained, but the analytic local argument
above supplies an independent empty-SFT mechanism. Larger radii do not
require repeated tests once radius two is empty.

## Artifacts and replay

`research/reviews/verify_two_hexagon_balanced_rank_five_root.py` independently
checks rank, all 364 closure memberships, the positive rational balance,
all 41 generating subsets of at most three triples, the generic rational
angle point, and the exact local cycle obstruction. It also runs the narrow
solver controls. Output is retained in
`research/certificates/two-hexagon-balanced-minimal-covering-root.json`.

    MISE_AUTO_INSTALL=0 mise exec -- conda run --no-capture-output -n arisearch python3 research/reviews/verify_two_hexagon_balanced_rank_five_root.py

The command passed on 2026-10-12. No low-rank registry or discovery log was
modified. No complete higher-rank enumeration, novelty claim, geometric
construction or unrestricted impossibility theorem follows from this example.

The fresh [solver-free independent checker](../reviews/check_two_hexagon_balanced_rank_five_ring.py)
derives ring incidences and neighbour indices directly from lattice coordinates,
without importing the producer, SFT implementation, CP-SAT or Sage. Its
[hostile review](../reviews/two-hexagon-balanced-minimal-covering-root-review.md)
validates all twelve unique rings and the disjoint successor-placement sets.
Use that checker for nondestructive replay; the original script also reruns
secondary solver controls and writes its output certificate.
