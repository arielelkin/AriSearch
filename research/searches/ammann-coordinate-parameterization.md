# Ammann convex recomposition: exact parameterization and conditional counts

**Status:** Coordinate formulas proved and adversarially checked.  Aggregate
frequency calculation is conditional on the explicitly listed graph and
ergodic hypotheses.  This is not an exact two-tile candidate.

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

Let \(t,T\) count thin and thick source rhombi in a van-Hove patch.  Reading
the intended marking graph gives three internal segments per thin rhombus and
five per thick rhombus, hence

\[
E=3t+5T+O(\partial).
\]

If the recomposition is edge-to-edge, every graph edge is exactly one native
side of a final pentagon or hexagon, no straight vertex is suppressed, and
boundary-crossing faces contribute only \(O(\partial)\), write \(h,p\) for
the final hexagon and total-pentagon counts.  Then

\[
h+p=t+2T+O(\partial),\qquad
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
