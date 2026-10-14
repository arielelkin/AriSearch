# Repeatable strip interfaces force a periodic escape

Date: 2026-10-14. Status: independently hostile-reviewed VALID on the stated conditional strip domain; see the [fresh review](../reviews/two-hexagon-strip-cycle-independent-2026-10-14.md).
This is a construction mechanism and conditional structural theorem, not a
classification of two hexagons. No novelty claim is made.

## Explicit scheme and exact geometry

For p,q,h > 0 define the six-corner convex polygon

    H(p,q,h) = [(0,0),(1/2,-p),(1,0),(1,h),(1/2,h+q),(0,h)].

Its consecutive turn cross products are p,h/2,h/2,q,h/2,h/2,
all strictly positive. Its area is h+(p+q)/2. Horizontal translates
H+(n,0), n in Z, tile the strip between two triangular-wave graphs.
Let tau be the continuous 1-periodic function with tau(0)=0,
tau(1/2)=1, linear between those points. The lower graph is -p tau(x)
and the upper graph is h+q tau(x). Since

    tau(x-1/2) = 1-tau(x),

write the upper graph as h+q-q tau(x-1/2). Thus the strip transports
boundary state p to state q by displacement (1/2,h+q). These are
complete boundary identities, including adjoining-side far endpoints;
matching merely a corner angle is not being substituted for geometry.

A half-turn about (1/2,h/2) takes H(p,q,h) to H(q,p,h).
Consequently every single H(p,q,h) has a repeatable reverse strip.
Alternating the two orientations gives a plane tiling, horizontal period
(1,0) and two-row period (1,2h+p+q). The vertical component is positive,
so these periods are independent. This already defeats omission-sensitive
aperiodicity for every pair drawn from this entire three-parameter family.
No monohedral classification theorem is imported for this conclusion.

For a genuinely noncongruent two-species fixture, use

    A = H(1/8,1/4,1),
    B = H(1/4,1/8,3/2).

Their areas differ (19/16 and 27/16). A transports p to q and B transports
q to p. Alternating A and B therefore covers the whole plane with periods
(1,0) and (1,23/8). The A-only and B-only omission constructions have
periods (1,19/8) and (1,27/8), respectively. These covers are exact and
immediate; no bounded patch extension inference is needed.

## Branching strip-interface theorem

Suppose a finite directed graph supplies independently constructed strip
tilings from a given finite prototile set. Every strip has the same nonzero
horizontal period u>0. Each state s specifies a bounded continuous
u-periodic graph f_s. For an edge e:s->t its strip tiling occupies precisely

    f_s(x) <= y <= d_e + f_t(x-delta_e),

with disjoint tile interiors, with period (u,0), and with strictly positive
pointwise gap. Whole boundaries match exactly as sets. The strip is usable
independently of other rows: there are no unrecorded neighboring-row,
orientation, or hierarchical restrictions on the graph transitions.

If this graph has a directed cycle, the original prototiles admit a doubly
periodic plane tiling. In particular, any admitted bi-infinite strip path
in a finite such graph supplies a periodic escape, even when transitions
branch and their horizontal phase displacements are irrational relative
to u. No neighbor determinism is assumed.

Proof. Choose one directed cycle e_1,...,e_m. Stack its independently valid
strip tilings, translating each next strip by the displacement prescribed
by the preceding interface. Boundary identities guarantee exact union and
interior disjointness. Its net displacement is (Delta,D), the sum of the
edge displacements. Average each positive gap over one horizontal period:

    d_e + mean(f_t)-mean(f_s) > 0.

Summing around the cycle telescopes the means, hence D>0. Repeat the cycle
for every integer n, translating it by n(Delta,D). The boundary graphs at
cycle joints are nD+f_s(x-nDelta), which go uniformly to positive/negative
infinity as n goes to positive/negative infinity because f_s is bounded.
The strips therefore cover the entire plane. Translations (u,0) and
(Delta,D) preserve all tiles, and D>0 makes them independent. A bi-infinite
path in a finite graph contains a directed cycle by vertex repetition.
QED.

This argument does NOT conclude rank-two periodicity merely from a horizontal
period or from one repeatable row. Positive strip gap, bounded periodic
boundary graphs, independently valid row interiors, and a complete interface
state are the hypotheses producing the transverse plane extension. It does
not assert that arbitrary two-hexagon tilings admit these states.

## Bounded experiment and stopping condition

Run:

    mise exec -- conda run --no-capture-output -n arisearch python research/searches/two-hexagon-sawtooth-strip-cycle.py

The bounded rational certificate checks all six turns for each fixture,
actual half-turn congruence, exact seam endpoints, noncongruence by area,
the mixed and both omission period vectors, and fundamental-domain area.
The theorem itself supplies covering, rather than a large patch experiment.

Stopping condition: one admissible periodic or omission cycle closes the
candidate immediately. This fixture stops at both. Do not enlarge a row
census or seek an aperiodic word within the same strip graph: the theorem
already allows arbitrary branching words and still constructs a periodic
word. Restarting requires changing the mathematical assumption that strips
are independently reusable with a finite complete interface state (for
example, intrinsically forced unbounded context across rows), or leaving
this sawtooth family. Changing the chosen nonperiodic source word alone
cannot help.

## Existence and recognition milestones

Existence: exact mixed infinite plane covering proved, with explicit periods.
Omission: exact monohedral periodic covering proved for each fixture member
and indeed each polygon in the full H(p,q,h) family.
Recognition: no universal row recognition or hierarchy is claimed. A visible
row construction does not establish that every admitted tiling has rows.
That missing recognition cannot rescue the candidate, since one periodic
cover already exists. General two-hexagon pairs remain globally unclassified.
