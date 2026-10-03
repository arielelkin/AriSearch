# Pentagon curvature and density constraints

**Status:** adversarially reviewed necessary conditions. These constrain
possible tilings and do not prove their existence or universal nonperiodicity.

**Dependencies and shared definitions:** use the square-window patch from
[side-count and monohedral obstructions](side-count-and-monohedral-obstructions.md).
N is its tile count, E and V its planarized graph counts, B its boundary-edge
count, V_b its boundary-vertex count, H its hole count, and q the sum of
boundary-vertex degrees. These boundary quantities are O(R), uniformly in the
window centre. The pentagon–hexagon consequence also uses the imported
monohedral classification in [hexagon limits](hexagon-limit-and-periodicity.md).

**Review:** [pentagon curvature review](../reviews/pentagon-curvature-review.md).

## Exact combinatorial curvature and pentagon backbones

For the general square-window patch, put

\[
S=\sum_T n(T),\quad
\delta=(2E-B)-S,\quad
D=\sum_{v\ \mathrm{interior}}(\deg v-3).
\]

The same Euler calculation gives the exact identity

\[
\boxed{
\delta+2D=
\sum_T(6-n(T))+6V_b-2q-B-6+6H.}             \tag{5}
\]

All terms have the meanings used above.  The final boundary expression is
\(O(R)\), uniformly for translated squares.  For a pentagon \(P\) and an
\(n\)-gon \(Q\), this becomes

\[
\delta+2D=N_P-(n-6)N_Q+O(R),
\qquad
(n-6)N_Q\leq N_P+O(R).                       \tag{6}
\]

### Pentagon syndeticity

If \(n\geq7\) and \(\{P,Q\}\) tiles, there is a constant \(L\), depending
only on the pair, such that every radius-\(L\) disk in every admitted tiling
meets a pentagon.  Otherwise, recenter a sequence of pentagon-free disks with
radii tending to infinity and take a compactness limit.  The limit is a
monohedral tiling by the \(n\)-gon, contradicting the global side-count
theorem.  A separated-grid count then gives
\(N_P(x,R)\geq cR^2-O(R)\) uniformly in the tiling and centre.

For a \((5,6)\) pair claimed to be aperiodic, the same conclusion is
necessary.  Failure of syndeticity produces a monohedral hexagon tiling in a
limit; the unrestricted convex-hexagon classification then supplies a periodic
monohedral tiling admitted by the pair.

Consequently an aperiodic \((5,6)\) pair would have
\(\delta+2D\geq cR^2-O(R)\): it must force a positive density of native-side
subdivisions/T-junctions or excess-valence vertices.  For a \((5,5)\) pair,
(5) directly gives \(\delta+2D=N+O(R)=\Theta(R^2)\).  Thus neither surviving
case can be resolved by an everywhere edge-to-edge trivalent construction.

If edge-to-edge contact is forced separately (for example by angle
nonresonance), then $\delta=0$ and the $(5,6)$ identity sharpens to

\[
  2\sum_{v\ {\rm interior}}(\deg v-3)=N_5+O(R).
\]

Thus total excess valence has asymptotic density exactly half the pentagon
density.  If every nontrivalent vertex is 4-valent, their count is
$N_5/2+O(R)$.  This supplies a precise incidence target for a prospective
nonresonant-angle compiler; it does not prove that the required vertex stars
extend globally.
