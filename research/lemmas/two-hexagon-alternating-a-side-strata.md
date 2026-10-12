# Exact native side strata of an alternating-angle hexagon

Date: 2026-10-12. Status: [independently reviewed VALID as part of the complete ALT/ALT chain](../reviews/two-hexagon-alternating-all-metric-chain-review.md).
This component retains its stated restricted domain; the full family conclusion
is in [the all-metric theorem](../lemmas/two-hexagon-alternating-all-metric-escape.md).

Let A have alternating native angles(p,q,p,q,p,q), with p+q=240 degrees,
90<p<150 and p!=120. Among the203 native side equality partitions,137 are
impossible at every admitted angle. The remaining66 are a necessary superset:
one one-class, one two-class, three three-class,45 four-class,15 five-class,
and one six-class partition. Generic feasibility of this superset is not an
assertion that every retained partition is feasible at every angle.

The exact [producer](../searches/two-hexagon-alternating-a-side-strata.py) and
[certificate](../certificates/two-hexagon-alternating-a-side-strata.json) retain
all203 matrices, generic kernels, class-pair equalities and exact rank-drop
gcds. No gcd has an admissible real root. Weighted by the complete
[ALT metric ledger](two-hexagon-alternating-metric-ledger.md), the137 impossible
partitions remove18323 of39628 native B word cases, leaving21305.

## Two actual side values force native period two

Write alpha=180-q=p-60 in(30,90) degrees with alpha!=60. Native side directions are

    0, alpha, 120, 120+alpha, 240, 240+alpha.

Each parity's three unit vectors sum to zero. If native lengths take precisely
two positive actual values x!=y, let U be the nonempty proper subset carrying x.
Closure reduces to(x-y) times the unit direction sum over U being zero.
Put omega=exp(2pi*i/3). The sum over U is E+exp(i alpha)O, where E,O are subset
sums of1,omega,omega^2 for even and odd native indices respectively.

Each of these eight subset sums is either zero or one of the six unit sixth
roots: the empty and full subset have zero sum, a singleton is a third root,
and a two-element subset is the negative of the omitted third root. If exactly
one of E,O vanishes, their combination cannot vanish. If neither vanishes,
exp(i alpha)=-E/O is a sixth root. The only sixth-root angle strictly between30
and90 is60, which is excluded. Both E and O must therefore vanish. Since U is
proper and nonempty, it is exactly the even or exactly the odd native indices.
Thus the length word is E0,O0,E0,O0,E0,O0. The64 exact subset records in the
certificate verify these possibilities using integer coefficients in the basis
1,omega; proper zero subsets have masks21 and42 only.

This independently excludes30 of31 two-class native partitions. The remaining
one, and the all-equal partition, are covered by the reviewed
[alternating side-period-two metric escape](two-hexagon-rank-nine-colour-transport.md).

## All203 class-coordinate closure matrices

Put theta=120-p and t=tan(theta/2), with sqrt(3)-2<t<2-sqrt(3), t!=0.
Using the exact rationalized sine and cosine, the direction list is

    (j,m)=(0,0),(1,-1),(2,0),(3,-1),(4,0),(5,-1),

meaning j*60+m*theta. For a native side partition with k actual classes,
sum direction vectors within each class to form a2-by-k matrix M over
Q(sqrt(3))(t). M times its positive class-length vector must vanish. The
all-ones class vector is always in the kernel because all six unit vectors sum
to zero, but using that vector would merge all actual classes when k>1.

For every generic kernel, list all pairs of class coordinates that agree in
every kernel vector. Any such pair makes the asserted actual equality partition
impossible: its two different classes would have equal positive lengths.
This test excludes30 two-class,87 three-class and20 four-class partitions.
For each M, the exact gcd of its generic-rank minor numerators has no admitted
real root, so its rank is constant throughout the parameter domain. The forced
coordinate relations therefore persist even at a pole of a chosen rational
kernel basis: nullspaces vary continuously locally at constant matrix rank.
Equivalently, use a nonzero rank minor as a local basis chart at each point.

The three retained three-class partitions are

    001221, 011022, 012210.

Each has generic rank1 and no forced class-pair equality. They are reflection
palindromes with one even and one odd side in each class. Every other
three-class partition has a forced merge, at all admitted angles.

For generic kernels with no forced pair, there are generic positive vectors
with all class coordinates distinct: choose a kernel vector outside the finite
union of coordinate-equality hyperplanes and perturb the all-ones vector by a
small scalar multiple. This observation explains the retained generic label;
it is not needed for the137 universal exclusions. Isolated angles where
additional coordinate relations arise without a rank drop could further shrink
the retained positive domain, and are not asserted absent here.

No conclusion about B geometry, global compatibility or periodicity follows
merely from membership in the66-partition necessary superset.
