# Exact nonresonant angle scaffold for a pentagon--hexagon route

**Status:** the angle/incidence relaxation is feasible and both monohedral
escapes are excluded, but the displayed exact side-length choice is locally
untileable.  It is therefore a falsified candidate, not a solution.

The later [joint side-partition replacement](joint-5-6-restart.md) is also
falsified, by a two-ended-edge check. Use [the current log](../../discovery-log.md)
for restart decisions; the calculations below retain the original failure.

## Angle data

In cyclic order, take angles (in degrees)

\[
 P=(66,162,66,96,150),\qquad
 H=(102,111,99,147,117,144).
\]

They sum to $540^\circ$ and $720^\circ$, respectively.  Every angle is at
least $66^\circ$, so a multiset summing to $180^\circ$ could contain at
most two angles.  Direct exact enumeration finds no complementary pair.
The angle-nonresonance theorem therefore makes every tiling by polygons with
these angles edge-to-edge, while still permitting the required 4-valent
vertices.

Index the five pentagon corners by 0--4 and the six hexagon corners by 5--10.
The following vertex stars all sum to $360^\circ$.  Assign them the listed
formal frequencies:

| corner multiset | valence | weight |
|---|---:|---:|
| `(1,3,5)` | 3 | 1 |
| `(2,4,10)` | 3 | 1 |
| `(3,8,9)` | 3 | 1 |
| `(4,6,7)` | 3 | 1 |
| `(0,0,0,1)` | 4 | 2/3 |
| `(1,2,2,2)` | 4 | 1/3 |

Every labelled pentagon corner then has marginal 2 and every labelled
hexagon corner marginal 1.  Thus the formal tile-frequency ratio is $2:1$.
The total 4-valent weight is 1 and the total excess valence is 1, exactly
satisfying $2D=N_5$ at pentagon weight 2.  Hence angle nonresonance,
corner balance, and curvature balance are simultaneously feasible; they do
not by themselves make a plane tiling.

## Exact polygon closure is feasible

The angle lists are geometrically realizable as strictly convex polygons.
For $P$, choose successive edge directions

\[
  0^\circ,18^\circ,132^\circ,216^\circ,246^\circ
\]

and lengths $(1,p_1,p_2,1,1)$, where

\[
 p_1=\frac{\sin84^\circ+\sin114^\circ-\sin132^\circ}{\sin114^\circ},
 \qquad
 p_2=\frac{2\sin18^\circ+\sin48^\circ}{\sin114^\circ}.
\]

For $H$, choose directions

\[
  0^\circ,69^\circ,150^\circ,183^\circ,246^\circ,282^\circ
\]

and lengths $(h_0,h_1,1,1,1,1)$, where

\[
 h_0=\frac{\sin81^\circ+\sin114^\circ+\sin177^\circ-\sin147^\circ}
            {\sin69^\circ},
 \qquad
 h_1=\frac{\sin3^\circ+\sin66^\circ+\sin78^\circ-\sin150^\circ}
            {\sin69^\circ}.
\]

Resolving the two coordinate closure equations gives these formulas.
Numerically, only as a positivity diagnostic,
$(p_1,p_2)\approx(1.2752,1.4900)$ and
$(h_0,h_1)\approx(1.5092,1.5468)$.  The displayed sine expressions and
standard first-quadrant comparisons prove all four are positive.  Successive
turns are strictly between 0 and $180^\circ$, so closure with positive
lengths gives strict convexity.  All coordinates lie in a real cyclotomic
field.

The hexagon avoids the unrestricted monohedral classification: it is not H1
because its first three angles sum to $312^\circ$; it satisfies the H2
angle sum $102+111+147=360$, but violates the required corresponding side
equality since $h_1\ne1$; and it is not H3 because alternating angles are
not all $120^\circ$.  Thus this exact hexagon does not tile monohedrally.
Here $h_1>1$ follows without decimals: $\sin78^\circ>\sin69^\circ$
and $\sin66^\circ+\sin3^\circ>\sin150^\circ$, so the numerator defining
$h_1$ is greater than its denominator.
The pentagon also fails an angle condition for every one of the fifteen known
monohedral families, under every cyclic or reflected labeling.  It has no
three distinct corners summing to $360^\circ$ (Types 1, 2, and 6), no
relation $2x+y=360^\circ$ (Types 7--9), no $90^\circ$ angle (Types 4 and
10--15), and no $120^\circ$ angle (Types 3 and 5).  The exact script checks
these coarse gates.  This is not a proof of monohedral escape because the
completeness of the fifteen-family classification remains unconfirmed in the
current literature boundary.
The family equations checked here are those tabulated in Figure 1 of
Sugimoto, *Convex pentagonal monotiles in the 15 Type families*,
arXiv:2501.07090v2; this use does not adopt that paper's unconfirmed
completeness premise.

In fact the pentagon monohedral gate can be closed without assuming that
classification.  Angle nonresonance makes any hypothetical pentagon tiling
edge-to-edge.  Since the minimum angle is $66^\circ$, a tiling vertex has
at most five sectors.  The certificate enumerates every 3-, 4-, and 5-sector
pentagon-only sum of $360^\circ$; none contains corner 4, whose angle is
$150^\circ$.  Every copy of the pentagon has such a corner, so no
monohedral tiling exists.  Together with the Reinhardt exclusion for $H$,
neither member has a monohedral escape.

## Full-edge compatibility falsifies the displayed shapes

The closure choice has five length symbols.  Around corners 0--10 their
unordered adjacent-side pairs are

```text
uu, ua, ab, bu, uu, uc, cd, du, uu, uu, uu.
```

Here $u=1$, $a=p_1$, $b=p_2$, $c=h_0$, and $d=h_1$.  These five values are
distinct.  Rational interval evaluation of the displayed sine formulas gives

\[
 1.275<a<1.276,\quad 1.489<b<1.491,\quad
 1.509<c<1.510,\quad 1.546<d<1.548.
\]

The replay script certifies these intervals from
$333/106<\pi<355/113$ and alternating Taylor bounds after range reduction;
they isolate exact algebraic values rather than serving as floating-point
branch decisions.

At a full-edge vertex, the adjacent-side pairs of its corner sectors must be
cyclically joined at equal lengths.  Equivalently, they form a connected
Eulerian multigraph on the length symbols.  Exact enumeration leaves only
two angle-legal rows for the distinct-symbol partition: `(0,4,10)` and
`(0,8,8)`.  Together they use only corner labels 0, 4, 8, and 10.  Since
every polygon copy also brings the other labelled corners, no tiling by the
displayed exact shapes exists.

The same enumeration shows that making all six selected certificate rows
edge-compatible within this five-symbol closure family forces
$u=a=b=c$ (while $d$ may remain separate).  In particular it would make the
pentagon equilateral.  That pentagon cannot close: the imaginary part of the
sum of its unit edge vectors is

\[
 \sin18^\circ+\sin48^\circ-\sin36^\circ-\sin66^\circ
 =-2\sin9^\circ(\cos27^\circ+\cos57^\circ)<0.
\]

Thus neither coarsening the five existing length symbols nor using the
displayed distinct values rescues this incidence support.  A new search must
solve angle incidence, cyclic side matching, and polygon closure jointly;
changing arbitrary closure lengths after the angle search is unsound.

## Replay and exact boundary

```text
conda run --no-capture-output -n arisearch python3 research/verify.py
```

The script uses integer angle units and rational incidence weights.  It
enumerates every possible half-plane sum, every 3--5-valent full-angle sum,
and verifies all eleven labelled marginals and curvature.  It does not use
floating point and does not search for a global tiling.

## Remaining obligations

1. Redesign the side-length equality pattern jointly with the incidence
   rows; the displayed exact polygons admit no tiling.
2. Restrict the many extra $360^\circ$ multisets listed in the certificate;
   the six selected rows are not the full geometry-admitted vertex language.
3. Prove every tiling in the resulting unrestricted geometric language is
   nonperiodic.  The present incidence certificate says nothing about that.
