# Falsified joint pentagon and hexagon synthesis

**Status:** falsified by the October 3 two-ended-edge review: these exact
shapes admit no plane tiling. Positive closure and the initial local language
remain certified, but their vertex configurations cannot consistently share
whole edges. See [the review](../reviews/joint-5-6-two-ended-review.md).

## Data retained

Keep the rational angle lists from the falsified scaffold:

\[
 P=(66,162,66,96,150)^\circ,\qquad
 H=(102,111,99,147,117,144)^\circ.
\]

Number the five pentagon sides 0--4 and the six hexagon sides 5--10.  A joint
search, rather than an after-the-fact closure choice, found the equality
partition

```text
side slots:  0 1 2 3 4 | 5 6 7 8 9 10
class:       0 2 0 1 2 | 2 3 1 4 0  1
```

Let the edge directions be
$(0,18,132,216,246)^\circ$ for $P$ and
$(0,69,150,183,246,282)^\circ$ for $H$.  Define
$(L_0,\ldots,L_3)$ by the four real closure equations for these two
polygons and normalize $L_4=1$.  Cramer's rule makes these finite exact
elements of the real cyclotomic field.  Rational interval arithmetic proves
the coefficient determinant is nonzero and isolates the positive solution:

```text
(L0,L1,L2,L3,L4)
  ~= (10.62730884, 7.94113192, 5.34292351, 14.52247548, 1).
```

The replay verifier uses $333/106<\pi<355/113$, alternating Taylor bounds
for the required sines and cosines, and interval Cramer determinants.  It
certifies the coarser disjoint intervals
$10.6<L_0<10.7$, $7.9<L_1<8$, $5.3<L_2<5.4$, and
$14.5<L_3<14.6$.  Thus the closure is exact and strictly positive; the
decimals above are diagnostics only.

## Local language

Combining exact angle sums with cyclic full-edge compatibility for the above
partition leaves these rows:

```text
valence 3: (0,4,10), (1,3,5), (2,4,10), (3,8,9), (4,6,7)
valence 4: (0,0,0,1), (0,0,1,2), (0,1,2,2), (1,2,2,2)
valence 5: none
```

The prior balanced incidence support is contained in this language.  One
choice of cyclic corner orders and local flips for its six rows is:

```text
(1,3,5):   order (1,3,5),   flips (1,0,0)
(2,4,10):  order (4,2,10),  flips (0,0,0)
(3,8,9):   order (3,8,9),   flips (0,0,0)
(4,6,7):   order (6,4,7),   flips (1,1,1)
(0,0,0,1): order (0,1,0,0), flips (1,1,1,0)
(1,2,2,2): order (2,2,1,2), flips (0,1,1,1)
```

This is only local.  In a global map, all corners belonging to one reflected
tile occurrence must use the same face chirality; the listed independent
local flips do not prove that consistency.

That first chirality obstruction has nevertheless been passed at the count
level.  At the 12-pentagon/6-hexagon scale, choose the two compatible
order/flip variants of each row with these multiplicities:

```text
row          copies  order       flips
(1,3,5)        4     (1,3,5)     (1,0,0)
               2     (1,5,3)     (0,1,1)
(2,4,10)       4     (10,4,2)    (0,0,0)
               2     (4,10,2)    (1,1,1)
(3,8,9)        4     (9,3,8)     (0,0,0)
               2     (3,9,8)     (1,1,1)
(4,6,7)        4     (7,4,6)     (0,0,0)
               2     (7,6,4)     (1,1,1)
(0,0,0,1)      4     (0,0,0,1)   (0,1,0,0)
(1,2,2,2)      2     (2,2,2,1)   (0,1,0,0)
```

Every pentagon corner label then has four flipped occurrences and every
hexagon corner label has two.  Hence the positions can be assigned to four
reflected pentagon faces and two reflected hexagon faces without a marginal
chirality contradiction.  This is still not an edge pairing: the two
endpoints of each native side must choose the same neighboring side orbit.

Neither type can tile alone in this local language.  Pentagon-only rows omit
corners 3 and 4, while there is no hexagon-only row.  Since angle
nonresonance forces edge-to-edge contact, this closes the monohedral gate for
any exact positive closure with this partition.

## Search provenance and reproduction boundary

The original notes attribute this partition to seeded randomized enumeration
of cyclic orders and flips, followed by a numerical positive-kernel check.
Neither the seed nor the randomized generator was retained. Discovery of the
partition is therefore not reproducible from these artifacts. The retained
fixed partition, exact positive closure, local enumeration, and later
falsification are reproducible; no missing seed should be invented.

The former proposed 12-pentagon/6-hexagon torus search is superseded. The
full nine-row language already fails a necessary two-ended-edge condition,
so expanding the six-row support or searching larger maps cannot rescue
these shapes. A future branch must change the angle data or side partition
and enforce both endpoints of every edge before testing global existence.

The discrete claims above replay without SciPy or floating point:

```text
conda run --no-capture-output -n arisearch python3 research/verify.py
```

The runner replays [the original local verifier](joint_5_6_local_verify.py),
which exhausts angle rows, cyclic orders, and corner flips for the fixed partition, checks the chirality-balanced mixture, rechecks both
monohedral local obstructions, and certifies the exact positive closure
kernel.  It deliberately does not certify a torus map or plane tiling.

## Two-ended-edge falsification

An edge shared by consecutive sectors at one vertex must be shared by the
same two tile occurrences at its other endpoint, with unchanged face
chiralities and reversed sector order. The other endpoint corners are fixed
by their native side slots. Every such pair must occur in some allowed star.

The independent [review verifier](../reviews/verify_joint_5_6_two_ended.py)
enumerates all stars, including the three rows outside the balanced support.
There are initially 94 ordered/chiral configurations. The first compatibility
pass leaves 12 configurations on rows `(2,4,10)` and `(3,8,9)`; the second
leaves none. Every vertex of an actual tiling would survive every pass, so
these polygons cannot tile the plane. Reflections are included.

The earlier periodic-hexagon-chain argument was conditional on a tiling
existing. It is superseded as a restart action by this stronger obstruction;
its original wording is preserved in the [historical checkpoint](../runs/2026-10-02-checkpoint.md).
No torus search or chain-synchronization proof is needed for this pair.
