# Ammann's convex recomposition: exact tiles and complete collapse classification

**Status.**
* Reconstruction (tile formulas, branch choice, three direct classes): **Proved**
  for the formulas, with the face structure **checked by exact computation** on
  Penrose patches (4- and 6-fold deflated suns).
* Collapse classification inside the closed admissible region: **Computational
  evidence from exact decisions** (certificate below); independent hostile
  review of exhaustiveness remains outstanding. The unique collapse point is **Falsified**
  as an aperiodic candidate (monohedral escape).
* The description of the admissible region by two inequalities is
  **computational evidence** (redundancy of the other 13 inequalities was
  checked on 400 000 random samples only). The classification itself does not
  depend on it: admissibility was decided exactly at every algebraic solution.

**Scripts / certificates.**
`research/searches/ammann-two-class-reconstruct.py`,
`research/searches/ammann-two-class-collapse.py`,
`research/certificates/ammann-two-class-reconstruction.json`,
`research/certificates/ammann-two-class-collapse.json`.
Search record: `research/searches/ammann-two-class-search.md`.

## Coordinates

Work in \(\mathbb C\) with \(\omega=e^{i\pi/5}\), \(K=\mathbb Q(\omega)\).
Thin rhomb \(A=0,\ B=1,\ D=\omega,\ C=1+\omega\); thick rhomb
\(E=0,\ F=1,\ H=\omega^2,\ G=1+\omega^2\). Write \(J=s+t\omega\) with
\(s,t\) real (rhomb coordinates of \(J\)).

The Sugimoto/Grünbaum–Shephard figure marks the arrows \(A\to B\), \(C\to B\)
(thin) and \(E\to F\), \(E\to H\) (thick). Gluing across rhomb edges then
forces the decoration triangles to match as follows:

* the thick triangle \(HEK\) is the image of the thin triangle \(BCJ\) under
  the rotation sending \(B\mapsto H,\ C\mapsto E\);
* the thick triangle \(FGL\) is the image of \(CDJ\) under the rotation
  sending \(C\mapsto F,\ D\mapsto G\).

Hence

\[
K=\omega^2+\omega^6(J-1),\qquad L=1+\omega^7(J-1-\omega).
\]

These satisfy \(EK=CJ,\ HK=BJ,\ FL=CJ,\ GL=DJ\). The two circles defining
\(K\) meet at \(K\) and at its mirror image in line \(EH\). That second point
lies outside the thick rhomb when \(K\) is inside, and likewise for \(L\) and
line \(FG\). So **there is no branch choice** in the admissible region. The
earlier parameterization's \(v_K=\pm\sqrt{\cdot}\) must take the sign that puts
\(K\) on the \(F\) side of \(EH\).

Auxiliary points (rotated copies of \(J\) carried across rhomb edges):

\[
J'=1+\omega^4(J-1),\quad J''=\omega+\omega^6(J-\omega),\quad J_2=1+\omega+\omega^2-J .
\]

## The three tiles (counter-clockwise vertex lists)

\[
\begin{aligned}
H_6&=[\,0,\ J',\ 1,\ J,\ \omega,\ J''\,] &&\text{(thin quad }ABJD\text{ + triangle on }AB\text{ + triangle on }DA)\\
P_1&=[\,0,\ J',\ 1,\ L,\ K\,] &&\text{(thick quad }EFLK\text{ + triangle on }EF)\\
P_2&=[\,K,\ L,\ 1+\omega^2,\ J_2,\ \omega^2\,] &&\text{(thick quad }KLGH\text{ + triangle on }GH)
\end{aligned}
\]

With \(a=|J-C|,\ b=|J-B|,\ r=|J-D|,\ c=|K-L|\), the side cycles are
\(H_6:(a,b,b,r,r,a)\), \(P_1:(a,b,a,c,a)\), \(P_2:(c,r,r,a,b)\).
Every vertex is a complex-affine function of \(J\), because only rotations are
used.

**Patch check.** Penrose patches come from exact Robinson deflation in \(K\).
Each rhomb gets an orientation-preserving copy of the decoration, anchored on
its Robinson "B" or "C" label (4 options). The rhomb edges are erased and the
faces of the resulting plane graph are traced. The face areas sum exactly to
the patch area. Exactly one anchor option, which is the arrow convention of
the figure, gives three classes for the generic samples
\(J\in\{(1/2,4/5),(9/20,3/4),(11/20,17/20)\}\). Those classes are directly
congruent to \(H_6,P_1,P_2\), with no mirror copies and all faces strictly
convex. On the 6-fold patch the counts are 415 hexagons, 680 \(P_1\) and
675 \(P_2\). The other three options give 5 or 6 classes, including
quadrilaterals or non-convex faces.

## Admissible region

The closed admissible region is defined by: all three tiles weakly convex with
nonzero edges, and all seven rhomb pieces weakly positively oriented. There
are 40 listed corner inequalities, which reduce to 17 distinct polynomials.
Sampling shows that the strict region is

\[
0<s<1,\quad 0<t<1,\quad |J|^2=s^2+\varphi st+t^2> s+t .
\]

That is, \(J\) lies inside the thin rhomb and outside the circumcircle of
\(A,B,D\). The binding circle is the corner of \(P_2\) (and of the thick
quad \(KLGH\)) at \(L\). The region covers about 42.8% of the parameter
square. The Figure 4 sample \(J\approx(0.495,0.779)\) lies inside it.

## Collapse classification (mirror images identified)

**Proposition (exact computation).** In the closed admissible region, the set
\(\{H_6,P_1,P_2\}\) has at most two congruence classes **only** at

\[
s=t=\tfrac{5+\sqrt5}{10},\qquad J=\text{circumcentre of }BCD,
\]

where \(P_1\cong P_2\) directly. At that point \(a=b=r=\sqrt{(5-\sqrt5)/10}\),
\(c^2=(25-9\sqrt5)/10\), and every tile is strictly convex.

*Proof sketch.*
1. **(a) \(P_1\sim P_2\), direct.** For each cyclic shift \(k\), the conditions
   \(f_{k+i}e_0=f_ke_i\) are polynomials in the single complex variable \(J\),
   because both edge lists are affine in \(J\). The gcd of these polynomials has
   at most two roots. Only one root has a unimodular rotation factor: shift 2,
   at the point above.
2. **(a) mirror.** Write the equations over \(K[s,t]\) and close them under
   complex conjugation. The Groebner basis is \((1)\) for shifts 1–4. For
   shift 0 the only real point is \((1,-\varphi^{-1})\), which fails
   unimodularity.
3. **(b) \(H_6\) with one straight angle, congruent to \(P_1\) or \(P_2\).**
   Delete each vertex \(m\in\{0,\dots,5\}\) in turn and repeat steps 1–2. The
   only unimodular solutions are \((1,\varphi^{-2})\) and \((\varphi^{-2},1)\).
   At both, \(J\) is on a rhomb edge and the deleted vertex is *not* straight,
   so neither is a genuine solution.
4. **(c) other degenerations.** A straight angle in \(P_1\) or \(P_2\), or two
   in \(H_6\), produces a quadrilateral. Every quadrilateral tiles periodically,
   so these strata are discarded without solving.

**Kill (exact).** At the collapse point \(H_6\) is equilateral with angles
\(72,144,144,72,144,144\) degrees and satisfies \(e_i=-e_{i+3}\). It is
therefore a centrally symmetric hexagon and tiles the plane by translations.
The pair \(\{H_6,P\}\) admits a periodic tiling, so it is **not aperiodic**.

**Dimension count.** There are 2 real parameters. Congruence of two pentagons
imposes 7 real conditions, and a straight angle imposes 1 more. No collapse is
expected generically. The isolated solution exists because of the symmetry
\(b=r\) when \(J\) lies on the diagonal \(AC\).

## What this does not show

It says nothing about aperiodicity of Ammann's generic three-tile set under
reflections and partial contacts; that question stays open, as recorded in the
source audit. It also does not cover recompositions other than the
generalization recorded in the search file.
