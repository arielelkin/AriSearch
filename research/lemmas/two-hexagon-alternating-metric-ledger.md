# Complete necessary side-length alphabet for alternating/alternating hexagons

Date: 2026-10-12. Status: [independently reviewed VALID as part of the complete ALT/ALT chain](../reviews/two-hexagon-alternating-all-metric-chain-review.md).
This component retains its stated restricted domain; the full family conclusion
is in [the all-metric theorem](../lemmas/two-hexagon-alternating-all-metric-escape.md).

Use the same-colour AAB angle family with native A=ALT=(p,q,p,q,p,q) and
B=ALT=(r,s,r,s,r,s), q=240-p, r=360-2p, s=2p-120,
90<p<150, p!=120. Reflections and arbitrary positive side coincidences are
permitted. The reviewed [global encoding](two-hexagon-global-sft-encoding.md)
and admitted trivalent hexagon limit give one B species phase and two A phases.
There are no BB seams, and each A has three AB and three AA seams alternating
around its sides. Every native placement, including reflections, preserves
the even/odd side-index partition. Thus a copy of A exposes either its three
even or its three odd native sides to B.

Every actual B side length is among the six actual A side lengths. Partition
the six native A side indices0,...,5 by equality of actual positive lengths;
let U be a block and let m_e(U),m_o(U) count its even and odd indices. Let
n(U) count B native sides with that actual value.

## Exact seam ledger without a tiling frequency hypothesis

Average translates of an admitted full-state lattice field over increasingly
large squares and take a weak limit on its compact finite-alphabet orbit
closure. The resulting measure is translation invariant and supported on legal
fields. The one-B species phase gives species probabilities2/3 for A and1/3
for B. Let h in[0,1] be the conditional probability, given species A, that
its AB native side parity is even. Counting the same U-valued AB seams from
the A and B ends gives

    n(U) = 2 [h*m_e(U)+(1-h)*m_o(U)].                  (1)

Every B copy contributes the same n(U), and every A copy of either parity
contributes its fixed m_e(U) or m_o(U). This does not assume any frequency limit
exists in the original Euclidean tiling. Lattice invariant averaging is enough.
It also does not impose a rational value on h unless the ledger forces one.

If some block has d=m_e-m_o!=0, then1<=|d|<=3 and equation(1) implies

    2*h*d = n(U)-2*m_o(U) is an integer.

Hence h lies in the union of the denominator2,4,6 grids in[0,1], exactly

    0, 1/6, 1/4, 1/3, 1/2, 2/3, 3/4, 5/6, 1.

Conversely these are merely the universal candidate values: every block must
still give an integer n(U). Nonnegativity and sum_U n(U)=6 follow automatically
from h in[0,1] and sum_U m_e=sum_U m_o=3. If all blocks satisfy m_e=m_o,
equation(1) instead gives n(U)=2*m_e(U) for every real h in[0,1]; no discretization
of the actual h is asserted in this balanced case.

## Complete finite native domain

Write the A equality partition as a restricted-growth word of length6: the
first value is0 and each subsequent value is at most one greater than the
largest prior value. This gives every unlabeled actual-length partition once,
while retaining all native positions. There are Bell(6)=203 such partitions.
For each partition and each unbalanced candidate h, keep its integer
multiplicity vector n. In the balanced case keep its one fixed vector. Deduplicate
identical vectors, preserving their admissible h list or continuous balanced
interval. For each vector, every native B word with those class multiplicities
is in the necessary domain; its exact count is6!/product_U n(U)!. A class may
have n(U)=0, for example when its A side parity never meets B. The class labels
always remain those of the fixed A partition, so this causes no re-labeling.

The [producer](../searches/two-hexagon-alternating-metric-ledger.py) and
[certificate](../certificates/two-hexagon-alternating-metric-ledger.json) retain
all203 partition rows and deduplicated multiplicity vectors. Exact totals:

* 16 parity-balanced A partitions: one with one class, nine with two classes,
  and six with three classes. In the two-class case one block contains one
  even and one odd index, selected in3*3 ways. In the three-class case the
  blocks form a bijection between the three even and three odd indices, in3!
  ways. Larger numbers of balanced nonempty blocks are impossible.
* 611 distinct pairs (native A partition, B multiplicity vector).
* 39628 distinct pairs (native A partition, native B side word), before any
  native dihedral quotient, local matching or polygon closure gate.

For the all-distinct A partition012345 the only ledgers are h=0,1/2,1,
yielding B multiplicities(0,2,0,2,0,2), (1,1,1,1,1,1), (2,0,2,0,2,0).
Their native word counts are90,720,90, summing to900. For the all-balanced
partitions the continuous h interval produces no duplicate metric words.

This domain is exhaustive as a necessary condition for every actual metric
pair in this ALT/ALT family, including reflected copies and arbitrary side
coincidences. It deliberately contains many geometrically impossible or
globally incompatible words. The already reviewed native-side-period-two A
[metric escape](two-hexagon-rank-nine-colour-transport.md) covers the two
partitions with constant even and constant odd lengths; it does not settle
the other201 partitions. No larger generic ring search, sample-angle rejection,
or bounded periodic absence is part of this ledger result.
