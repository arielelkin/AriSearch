# Hostile review: one exact periodic two-angle (5,7) instance

**Date:** 2026-10-09. **Verdict:** **valid mathematical periodic witness**.
The reviewer did not develop the generator, certificate, or checker.
The checker author is the root researcher; the fresh review is independent.

## Claim reviewed and artifacts

[Generator](../searches/two_angle_5_7_periodic_witness.py),
[exact coordinate certificate](../certificates/two_angle_5_7_periodic.json),
and [independent checker](verify_two_angle_5_7_periodic.py).
The claim is that their two convex shapes P,H admit a doubly periodic
plane tiling. P has five genuine corners with cyclic angles
\((5\pi/7,4\pi/7,4\pi/7,4\pi/7,4\pi/7)\);
H has seven corners each \(5\pi/7\).
Two copies of each shape in a rank-two lattice motif realize the tiling.
This refutes aperiodicity of this fixed coordinate instance. It does
not refute the entire family of polygons with this angle signature.

## Exact algebraic definition and embedding

The certificate's number-field polynomial is
\(f(x)=x^{12}-x^{10}+x^8-x^6+x^4-x^2+1=\Phi_{28}(x)\).
It selects the root whose real part lies in \((97/100,98/100)\)
and imaginary part in \((22/100,23/100)\).
The checker finds exactly one QQbar root in that rectangle.
This is the positive small-angle primitive root \(\omega=e^{i\pi/14}\),
so \(\omega^7=i\), \(\omega^{14}=-1\), and \(\omega^{28}=1\).
The geometric embedding is therefore fixed exactly, rather than by a
floating-point choice of a conjugate. Field coefficient lists are rational
and determine all coordinates finitely.

I independently checked all 52 raw motif/lattice coordinate components
are real in this embedding and all seven declared H side lengths are
positive. In the generator this also follows from
\(C(t)=(t+t^{-1})/2\) and
\(S(t)=(t-t^{-1})/(2i)\) for unit roots t: both are real, and real
arithmetic preserves reality. The polygon coordinates are defined by
these formulas before any numerical rendering.

**Checker hardening reported to root and resolved by the author:** reality must be tested directly
for every raw x,y component. Reality checks only on determinants, dot
products, and lattice-basis coordinates are not generally sufficient:
a complex orthogonal coordinate change could preserve those invariants.
This observation does not invalidate the retained real certificate.
The author added explicit raw-coordinate reality assertions for all motif
and lattice components, plus positivity checks for the seven H side lengths.
The strengthened checker was inspected and replayed successfully.

## Convexity and cyclic angle order

Same-signed consecutive turns alone would permit a multiply winding star
polygon. I challenged that sufficiency. Before this review's final replay,
the root strengthened the checker: for every boundary edge, every other
vertex must lie strictly in its interior supporting half-plane. These
exact inequalities ensure all vertices are distinct, each listed segment
is a hull edge, and the cyclic list is a simple strictly convex polygon.
Thus signed shoelace areas equal the actual positive polygon areas.

The angle equations check each consecutive pair of edges using the exact
cosine/sine of powers \(\omega^4\) and \(\omega^6\), together with the
sign of the dot product. This distinguishes an exterior angle from its
supplementary alternative. Since the polygons are convex, their exterior
angles lie in \((0,\pi)\): the encoded values are exactly
\(2\pi/7\) at every H vertex, and \(2\pi/7\) followed by four
\(3\pi/7\) turns at P. The corrected certificate order therefore matches
the actual cyclic order. Earlier different indexing was corrected by the
author before the reviewed run.

The second copy of each polygon is checked coordinate by coordinate as
a half-turn: the sums of paired vertices are a common fixed vector.
This is a direct congruence certificate with no inferred reflection or
cyclic reindexing. The two prototile classes are distinct already because
their numbers of genuine vertices differ; the area comparison is an
additional redundant distinction check. The geometry is unmarked.

## All possible periodic overlaps, not a bounded guess

Let u,v be the two certificate lattice vectors and
\(D=\det(u,v)\ne0\). Their exact determinant gives a rank-two lattice.
For every vertex p, its lattice coordinates are
\(\xi=\det(p,v)/D\) and \(\eta=\det(u,p)/D\).
Extrema of either affine coordinate on a polygon occur at vertices.
Therefore if A and \(B+mu+nv\) can intersect, then necessarily

\[
\min\xi_A-\max\xi_B\le m\le\max\xi_A-\min\xi_B,
\qquad
\min\eta_A-\max\eta_B\le n\le\max\eta_A-\min\eta_B.
\]

Ceiling the lower bounds and flooring the upper bounds gives the full
finite integer domain, including potential boundary-only contacts.
The checker derives those bounds separately for all sixteen ordered
motif pairs. Only comparison of a tile with itself at zero shift is
excluded. Coincident tiles of different motif indices would not be
excluded. The retained instance requires 34 comparisons.

For every comparison, the checker seeks a separating axis perpendicular
to an edge of either polygon. Its projection values are exact
\(\det(e,p)\). Omitting the edge's base point merely adds the same
constant to both intervals and changes no separation decision.
Non-strict interval separation permits edge/vertex contacts while
excluding overlapping interiors. The supporting-edge inequalities
already established convexity, so this standard polygon separation
criterion applies. Every possible lattice translated intersection has
been covered; there is no arbitrary fixed radius or search cutoff.

## Area proves full-plane coverage here

The checker compares doubled shoelace areas and verifies
\(\sum_i 2\operatorname{area}(T_i)=2|D|\).
With disjoint periodic tile interiors this is exactly full area density,
but that phrase requires the following global proof.

Take a lattice fundamental parallelogram F. Let
\(N(x)=\sum_{i,\lambda\in\Lambda}1_{\mathrm{int}(T_i+\lambda)}(x)\).
The periodic set is locally finite: the motif tiles are bounded, u,v
have nonzero determinant, and only finitely many lattice translates can
meet a fixed bounded region. Thus N is locally finite and is 0 or 1
away from tile boundaries. Integrating over F and translating each
summand gives
\(\int_F N=\sum_i\operatorname{area}(T_i)=\operatorname{area}(F)\).
Boundaries have measure zero, so the complement of the closed tile union
has zero measure on F. The tile union is closed by local finiteness.
If any plane point were uncovered, its open complementary neighborhood
would contain a disk of positive area. Periodicity would then give a
positive-measure uncovered portion in F, contradiction. Hence the closed
tile union covers the entire plane. This is an infinite plane tiling,
not just a periodic finite patch with a density estimate.

## Replays and verdict

The strengthened checker was replayed successfully:

    conda run --no-capture-output -n arisearch python3 research/reviews/verify_two_angle_5_7_periodic.py

It reported PASS, 34 overlap comparisons, the corrected angle signature,
and the exact derived shift domains. Its conclusions were also checked
against the proof above. I found no counterexample to the exact fixed
instance, no overlap-domain omission, or area-to-coverage gap once the
closed-union argument is supplied.

Repairs made by the author before review: cyclic P-angle index correction
and full supporting-half-plane convexity checks. Additional raw-coordinate
reality validation was added by the author for checker robustness; the retained
coordinates were independently found real and the strengthened checker passed.
No geometric repair was made
by this reviewer. The result remains a failure witness for one candidate,
with no universality, family-wide exclusion, or novelty assertion.
