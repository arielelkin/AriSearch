# Ammann convex recomposition: exact parameterization and conditional counts

**Status:** Proved coordinate formulas and conditional frequency calculation.
Repairs from the recorded hostile review are incorporated; independent
re-review of the repaired artifact is pending. The graph counts below are
explicit hypotheses, not certified diagram data. This is not an exact
two-tile candidate.

**Review:** [coordinate and count review](../reviews/ammann-coordinate-review.md).

**Dependencies:** the source relations in Figure 4 cited below and the
standard Penrose thick:thin ratio; the graph and van-Hove hypotheses for
the count calculation are explicitly conditional.

## Algebraic coordinate parameterization

Normalize the unit thin Penrose rhombus in cyclic order as

\[
A=(0,0),\ B=(1,0),\ D=d=(\cos36^\circ,\sin36^\circ),\ C=B+d,
\]

and the unit thick rhombus as

\[
E=(0,0),\ F=(1,0),\ H=q=(\cos72^\circ,\sin72^\circ),\ G=F+q.
\]

Let \(J=(x,y)\) be an interior point of the thin rhombus and put

\[
a=|C-J|,\qquad b=|B-J|,\qquad r=|D-J|,
\quad q^\perp=(-\sin72^\circ,\cos72^\circ).
\]

The published constraints are

\[
EK=CJ,\quad HK=BJ,\quad FL=CJ,\quad GL=DJ.
\]

Writing \(K=u_Kq+v_Kq^\perp\), the first two constraints give

\[
u_K=\frac{a^2-b^2+1}{2}
    =1+\cos36^\circ-J\mathbin\cdot d,
\qquad
v_K=\pm\sqrt{a^2-u_K^2}.
\]

Writing \(L=F+u_Lq+v_Lq^\perp\), the last two give

\[
u_L=\frac{a^2-r^2+1}{2}
    =1+\cos36^\circ-x,
\qquad
v_L=\pm\sqrt{a^2-u_L^2}.
\]

These follow by subtracting the two circle equations in each case.  If \(J\)
is algebraic, every feasible branch is algebraic in the common real
algebraic extension obtained by adjoining the displayed square roots.

The signs are not determined by the distance equations.  Each point is
normally one of two circle intersections (and may be tangent or infeasible).
The intended branch must be selected by exact inside/incidence inequalities
from the construction.  Moreover, \(J\) remains a two-real-parameter choice.
Thus these formulas parameterize the diagram but do not select exact tiles.

## Conditional aggregate face count

Let \(t,T\) count thin and thick source rhombi in a van-Hove patch.
Assume its recomposition is represented by a connected finite plane marking
graph with edge count \(E\) and vertex count \(V\) satisfying

\[
E=3t+5T+O(\partial),\qquad V=2t+3T+O(\partial).
\]

These are additional incidence-count hypotheses for the intended graph.
The distance equations above do not establish either count. An exact marking
and vertex-incidence table is needed before applying them to a source tiling.
Here \(O(\partial)\) bounds boundary corrections, which must be negligible
relative to \(t+T\) along the chosen van-Hove sequence.

Let \(F\) be the graph's number of bounded faces. Euler's formula for a
connected finite plane graph gives \(V-E+F=1\), hence

\[
F=E-V+1=t+2T+O(\partial).
\]

Assume also that its bounded faces correspond to final pentagons and hexagons
up to \(O(\partial)\) boundary faces; every graph edge is exactly one native
side of an incident final polygon; the recomposition is edge-to-edge; and no
straight vertex is suppressed. Write \(h,p\) for the final hexagon and
total-pentagon counts. Face correspondence and edge-incidence counting then
give

\[
h+p=F+O(\partial)=t+2T+O(\partial),\qquad
6h+5p=2E+O(\partial)=6t+10T+O(\partial).
\]

Solving gives

\[
h=t+O(\partial),\qquad p=2T+O(\partial).
\]

After a van-Hove limit and the standard Penrose thick:thin ratio
\(T:t=\varphi:1\), the conditional aggregate ratio is

\[
H:P=1:2\varphi.
\]

This does **not** determine the two pentagon-class frequencies.  The tempting
split \(P_1:P_2:H=\varphi:\varphi:1\) needs a separate exact incidence or
substitution proof.  No fusion-frequency conclusion is valid without it.

## Replay/source boundary

The source relations and diagram are in Sugimoto,
*Convex Polygons for Aperiodic Tiling*, arXiv:1602.06372v2, Figure 4.  The
coordinate calculation is symbolic and uses no floating-point decision.
The missing data remain an exact \(J\), exact branch inequalities, final
polygon cyclic vertex lists, and a legal vertex-star/substitution table.
