# Two convex hexagons: exact reduction to finitely many vertex-star SFTs

**Status:** repaired internal proof (2026-10-11). A
[fresh independent rereview](../reviews/two-hexagon-global-repaired-reduction-rereview.md)
finds the repaired Theorem 1(d), completeness, and exact polygon
realisability encoding VALID, conditional on the reviewed L1/L2/L3
dependencies. It does not review census/code correctness or the ancillary
flux claims in Section 4. The original proof of Theorem 1(d) incorrectly treated a single
translation as a rank-two period lattice. Its replacement preserves that
translation in a defect-free limit; it makes no assertion that the original
periodic tiling is defect-free. Whole-class
reduction, not a periodicity theorem. It isolates the entire (6,6) case as a
finite list of explicit two-dimensional SFT questions and says exactly which
finite certificates would settle it.

**Dependencies (cited as stated):**
[hexagon-limit-and-periodicity.md](hexagon-limit-and-periodicity.md):
(L1) a tileable pair of convex hexagons admits an edge-to-edge, everywhere
trivalent tiling; (L2) every such tiling is combinatorially the hexagonal
honeycomb; (L3) the exact identity
\(\delta+2D_v=6V_b-2q-B-6+6H\) with uniformly \(O(R)\) right-hand side in
every translated square window \(Q_R\), valid for an arbitrary tiling by the
two hexagons (here \(\delta\) counts native-side subdivisions and \(D_v\)
excess valence inside the window). Standard facts used: the Killing–Hopf
theorem (a complete simply connected flat surface is isometric to
\(\mathbb E^2\)); a locally finite tiling is preserved by no rotation of
infinite order.

Code: [research/searches/two-hexagon-global-sft.py](../searches/two-hexagon-global-sft.py)
implements exactly the conventions below;
[research/searches/two-hexagon-global-geometry.py](../searches/two-hexagon-global-geometry.py)
independently develops configurations in the plane (numerical replay of
Theorem 1(a), used only as a convention check).

## 1. The SFT

Let \(A=P_0\), \(B=P_1\) be convex hexagons with six actual corners (all
interior angles in \((0,\pi)\)). In \(P_q\) number the corners \(0,\dots,5\)
counter-clockwise; side \(i\) joins corners \(i,i+1\); corner \(i\) has angle
\(\alpha_q(i)\) and lies between sides \(i-1,i\); side \(i\) has length
\(\ell_q(i)\).

Cells are \(z\in\mathbb Z^2\) (triangular lattice, basis at \(60^\circ\));
directions \(D_0,\dots,D_5=(1,0),(0,1),(-1,1),(-1,0),(0,-1),(1,-1)\). In the
abstract honeycomb, *slot* \(k\) of cell \(z\) is the honeycomb vertex shared
by \(z,z+D_k,z+D_{k+1}\); there it is slot \(k+2\) of \(z+D_k\) and slot
\(k+4\) of \(z+D_{k+1}\). *Side-slot* \(k\) joins slots \(k,k+1\) and is the
edge shared with \(z+D_{k+1}\), where it is side-slot \(k+3\).

Alphabet \(\Sigma=\{(q,r,s):q\in\{0,1\},r\in\mathbb Z_6,s=\pm1\}\), 24
symbols. Symbol \(\sigma=(q,r,s)\) puts corner \(\kappa_\sigma(k)=r+sk\) of
\(P_q\) at slot \(k\), hence side \(\lambda_\sigma(k)=r+k\) (\(s=1\)) or
\(r-k-1\) (\(s=-1\)) on side-slot \(k\). Write \(\alpha(\sigma,k)\),
\(\ell(\sigma,k)\) for the corresponding angle and length.

\(X(A,B)\subset\Sigma^{\mathbb Z^2}\) is the set of \(x\) with, for all
\(z\) and \(k\):

* (V) \(\alpha(x_z,k)+\alpha(x_{z+D_k},k+2)+\alpha(x_{z+D_{k+1}},k+4)=2\pi\);
* (E) \(\ell(x_z,k)=\ell(x_{z+D_{k+1}},k+3)\).

It is a nearest-neighbour SFT (all constraints live on elementary triangles
of the lattice = honeycomb vertices; (E) is implied by triangle constraints
since every lattice edge lies in a triangle).

## 2. Faithfulness

**Theorem 1.**
(a) For every \(x\in X(A,B)\) there is an edge-to-edge, everywhere trivalent
tiling \(\mathcal T_x\) by copies of \(A,B\), with tiles \(T_z\) such that
\(T_z\) is a copy of \(P_{q(x_z)}\) (direct iff \(s=1\)), its corner
\(\kappa_{x_z}(k)\) is the common vertex of \(T_z,T_{z+D_k},T_{z+D_{k+1}}\),
and its side \(\lambda_{x_z}(k)\) is the common side of \(T_z,T_{z+D_{k+1}}\).
\(\mathcal T_x\) is unique up to an isometry of the plane.
(b) Every edge-to-edge trivalent tiling by copies of \(A,B\) is
\(\mathcal T_x\) for some \(x\in X(A,B)\).
(c) If \(x_{z+p}=x_z\) for all \(z\) and some \(p\neq0\), then
\(\mathcal T_x\) has a nonzero translational symmetry.
(d) If some tiling by copies of \(A,B\) (arbitrary partial contacts allowed)
has a nonzero translational symmetry, then the same pair admits an
edge-to-edge, everywhere-trivalent tiling with a nonzero translational
symmetry, and \(X(A,B)\) has a point with a nonzero period. The limiting
tiling need not be the original tiling.

**Corollary 1.** The pair \(\{A,B\}\) is aperiodic (tiles, and no tiling has
a nonzero translational symmetry) **iff** \(X(A,B)\neq\emptyset\) and
\(X(A,B)\) has no periodic point. (Tileable \(\Rightarrow X\ne\emptyset\) by
(L1),(L2),(b); \(X\ne\emptyset\Rightarrow\) tileable by (a); periodic tilings
\(\leftrightarrow\) periodic points by (c),(d).) A periodic point in the sense
of one nonzero period suffices; by the standard strip argument a 2D SFT with
a one-periodic point also has a doubly periodic point, so "periodic point"
may be read either way.

### Proof of (a)

Let \(\widetilde P_z\) be \(P_{q}\) if \(s=1\) and its mirror image if
\(s=-1\) (\(x_z=(q,r,s)\)), with corner \(r+sk\) labelled slot \(k\); in both
cases slots increase counter-clockwise. Glue side-slot \(k\) of
\(\widetilde P_z\) to side-slot \(k+3\) of \(\widetilde P_{z+D_{k+1}}\) by
the isometry sending slot \(k\mapsto\) slot \(k+4\) and slot
\(k+1\mapsto\) slot \(k+3\). This is consistent with the honeycomb incidences
of Section 1 and possible because of (E). The quotient \(K_x\) is a cell
complex combinatorially isomorphic to the honeycomb, hence homeomorphic to
\(\mathbb R^2\).

The Euclidean metrics of the tiles give a piecewise-Euclidean length metric.
Interior points of tiles and of glued sides have Euclidean neighbourhoods. A
vertex is surrounded by exactly three corner sectors whose angles sum to
\(2\pi\) by (V), so it too has a Euclidean disk neighbourhood. Thus \(K_x\)
is a flat surface without cone points.

Completeness: the metric has uniform local Euclidean disk charts. To see
this without assuming global injectivity of development, use the finite
set of local models consisting of one tile interior, two tiles glued at a
side, and three corner sectors glued at a vertex. All side lengths are
positive, all corners are genuine, and the vertex models have angle
\(2\pi\). Each point in a closed prototile therefore has a neighbourhood
in its model isometric to an open Euclidean disk, with a smaller disk whose
closure stays in that neighbourhood. There are finitely many model choices
and compact prototiles; a finite subcover yields a common positive radius
\(\rho\) so that each point has such a chart containing its metric
\(\rho\)-ball. A path leaving the chart must first cross the smaller
disk's boundary, so shortcuts outside the chart do not invalidate this
radius. Every Cauchy sequence eventually stays in one such disk and
converges there. Thus \(K_x\) is complete.

By Killing–Hopf, the developing map \(\mathrm{Dev}:K_x\to\mathbb R^2\) is an
isometry. Put \(T_z=\mathrm{Dev}(\widetilde P_z)\). Since Dev is bijective,
the tiles cover the plane with disjoint interiors; glued sides are full
common sides and every vertex has three tiles. Dev is unique up to
post-composition with an isometry. \(\square\)

### Proof of (b)

By (L2) there is a combinatorial isomorphism \(\psi\) from the tiling to the
honeycomb. Compose with a lattice reflection if necessary so that \(\psi\)
preserves the cyclic (counter-clockwise) order of neighbours. For the tile at
cell \(z\) choose an isometry \(g_z\) with \(g_z(P_q)=T_z\). Let \(s=1\) if
\(g_z\) is direct, \(-1\) otherwise. The slot-\(k\) vertex of \(T_z\) is the
image of a corner \(c_k\). Counter-clockwise order of slots and corners gives
\(c_k=r+sk\) for a unique \(r\). Thus \(x_z=(q,r,s)\). (V) holds because
three corners fill a neighbourhood of a trivalent vertex. (E) holds because
the common side is a full side of both tiles. \(\square\)

### Proof of (c)

The shift by \(p\) induces an isometry of \(K_x\) (identical tiles, identical
gluings). So \(g=\mathrm{Dev}\circ\sigma_p\circ\mathrm{Dev}^{-1}\) is an
isometry of the plane preserving \(\mathcal T_x\) and sending \(T_z\) to
\(T_{z+p}\). For \(m\ne0\), \(g^m\) fixes no tile, since \(T_{z+mp}\ne T_z\)
by injectivity of Dev.

* A rotation preserving a locally finite tiling has finite order, and some
  power of it fixes a tile containing its centre. So \(g\) is not a
  rotation.
* \(g\) is not a reflection, because \(g^2=\mathrm{id}\).

Hence \(g\) is a translation or a glide reflection, and \(g^2\) is a nonzero
translational symmetry. \(\square\)

### Proof of (d)

Let translation by the vector \(t\ne0\) preserve the original tiling
\(\mathcal T\). A single translation repeats a defect only \(O(R)\) times
in \(Q_R\), so (L3) does **not** eliminate defects in \(\mathcal T\).
Instead apply the defect-free-limit construction (L1) to this tiling.
For each \(L\), its uniform defect estimate supplies a defect-free disk of
radius \(L\). Translate the disk centre to the origin and take the
placement-convergent diagonal subsequence used in (L1). Its limit
\(\mathcal T_\infty\) is edge-to-edge and everywhere trivalent.

Every translated approximant still has the **same** translational
symmetry \(t\), since translations commute. Preservation by this fixed
translation is closed in the local placement topology: if a tile placement
occurs in the limit, approximating tile placements and their translates by
\(t\) converge to that placement and its translate, both limit tiles.
Apply the same argument to \(-t\) for equality of tile sets. Thus
\(\mathcal T_\infty+t=\mathcal T_\infty\). By (b), this limiting tiling
equals \(\mathcal T_x\) for some legal labelling.

\(t\) induces an orientation-preserving automorphism \(\varphi\) of the
triangular lattice. Such a map is a translation or a rotation about a cell,
a honeycomb vertex or an edge midpoint. In the rotation case, \(t^6\) would
fix a tile, a vertex or an edge, hence \(t^6=\mathrm{id}\), which is
impossible. So \(\varphi\) is translation by some \(p\), and \(p\ne0\)
because \(t\) moves every tile. \(t\) maps slot \(k\) of \(T_z\) to slot
\(k\) of \(T_{z+p}\).

Choose the isometries \(g_z\) of (b) \(t\)-equivariantly: \(g_{z+p}=t\,g_z\).
Do this freely on one cell per \(\langle p\rangle\)-orbit and propagate. The
labels are then equal: \(x_{z+p}=x_z\). (Any choice of \(g_z\) yields a legal
configuration.) \(\square\)

## 3. Finitely many SFTs

The **type** of the pair is \(\tau(A,B)=(T,\sim)\). Here \(T\) is the set of
3-element multisets of the twelve corners whose angles sum to \(2\pi\), and
\(\sim\) is equality of length on the twelve sides. Conditions (V),(E) refer
only to membership in \(T\) and to \(\sim\). So \(X(A,B)=X(\tau(A,B))\), and
there are at most \(2^{364}\cdot\mathrm{Bell}(12)\) distinct SFTs.

A type is *realisable* if it is \(\tau(A,B)\) for some pair. Two properties
of types are used below:

* **Closure.** Realisable \(T\) is closed under rational-linear implication:
  if the equations of \(S\subseteq T\), together with the two \(4\pi\) sums,
  imply \(\sum_{c\in\tau}\alpha_c=2\pi\), then \(\tau\in T\).
* **Monotonicity.** \(T'\subseteq T\) and \(\sim'\subseteq\sim\) imply
  \(X(T',\sim')\subseteq X(T,\sim)\).

**Theorem 2 (exact finite reduction).** There is no aperiodic pair of convex
hexagons iff, for every realisable type \(\tau\), the property
\[P(\tau):\quad X(\tau)=\emptyset\ \text{ or }\ X(\tau)\ \text{has a periodic point}\]
holds. Each true \(P(\tau)\) has a finite certificate:

* emptiness: by compactness, some radius \(R\) admits no legal hexagonal
  patch;
* periodicity: a legal labelling of a finite torus
  \(\mathbb Z^2/\Lambda\).

Realisability of a type is a first-order statement over the reals, hence
decidable; the explicit polynomial encoding is given below. This is
realisability by actual polygons, not just feasibility of the linear angle
equations in the open angle box.

Consequently the (6,6) case is **either false, witnessed by one of finitely
many explicit SFTs, or provable by a finite exact computation**. Its
difficulty is entirely the possible existence of a realisable type whose SFT
is a nonempty aperiodic SFT on 24 symbols. *Proof.* Corollary 1 and
\(X(A,B)=X(\tau(A,B))\). \(\square\)

### Polynomial encoding of realisability

Introduce real coordinates \(v_{q,i}\in\mathbb R^2\) for both polygons,
positive variables \(h_{q,i}\) for side lengths, and corner variables
\(c_{q,i},s_{q,i}\). Indices are cyclic modulo six. Set
\(e_{q,i}=v_{q,i+1}-v_{q,i}\),
\(u_{q,i}=v_{q,i-1}-v_{q,i}\), and
\(f_{q,i}=v_{q,i+1}-v_{q,i}\). Impose

\[
 h_{q,i}>0,\quad h_{q,i}^{\,2}=e_{q,i}\cdot e_{q,i},\qquad
 \det(e_{q,i},v_{q,j}-v_{q,i})>0\quad(j\notin\{i,i+1\}).
\]

The strict half-plane tests make the listed vertices the counter-clockwise
corners of a strictly convex hexagon. Impose also

\[
 h_{q,i-1}h_{q,i}c_{q,i}=u_{q,i}\cdot f_{q,i},\qquad
 h_{q,i-1}h_{q,i}s_{q,i}=-\det(u_{q,i},f_{q,i}),\qquad s_{q,i}>0.
\]

These variables are exactly \(\cos\alpha_{q,i},\sin\alpha_{q,i}\), with
\(0<\alpha_{q,i}<\pi\). For each three-element corner multiset \(t\),
form the real and imaginary polynomial parts of
\(\prod_{a\in t}(c_a+\mathrm i s_a)\), including repeated factors.
The triple has angle sum \(2\pi\) iff these parts are \(1,0\): its
angle sum lies strictly between \(0\) and \(3\pi\), and \(2\pi\) is
the sole multiple of \(2\pi\) in that interval. Impose this equality for
\(t\in T\) and its Boolean negation for every \(t\notin T\). Impose
\(h_a=h_b\) iff \(a\sim b\) for each pair of sides. All these are
polynomial equalities, strict inequalities and finite Boolean combinations,
with rational coefficients.

For exactly two distinct congruence classes, also negate every cyclic or
reversed corner matching between the polygons. Explicitly, for each of the
twelve permutations \(\sigma(i)=r\pm i\pmod6\), require at least one of
the fifteen squared-distance inequalities
\[
 \lVert v_{0,i}-v_{0,j}\rVert^2
 \ne \lVert v_{1,\sigma(i)}-v_{1,\sigma(j)}\rVert^2
 \quad(0\le i<j<6).
\]
Full distance matrices characterize congruence, and any isometry between
convex polygons preserves or reverses their cyclic corner order. With
these finite Boolean inequalities, the existential real formula is
precisely realisability of \((T,\sim)\) by two distinct polygon shapes.

The two angle sums \(4\pi\) follow from the convex-polygon conditions;
they do not need a trigonometric constraint. Quantifier elimination decides
this finite formula. The finite-reduction claim does not supply a decision
procedure for arbitrary two-dimensional SFT emptiness: it says that, if
every realisable type has an empty-patch or torus certificate, this finite
list of certificates together with the unrealised-type checks settles this
particular finite family.

**Theorem 3 (sound covering certificate).** Let \(\mathcal C\) be a finite
set of *escape records* \((S,F)\): \(S\) a set of corner triples and \(F\) a
set of side pairs, each paired with a torus \(x\). The triples used by \(x\)
lie in the rational-linear closure of \(S\). The side identifications used by
\(x\) lie in the equivalence closure of \(F\). Let \(\mathcal E\) be a finite
set of *empty records* \((T_0,\sim_0)\) with no legal patch of radius \(R_0\)
in \(X(T_0,\sim_0)\). Let \(\mathcal K\) be a finite set of *candidate
records* \((T_c,\sim_c)\).

Suppose no \((t,e,y)\) satisfies all of the following:

1. \(t\) is a set of triples whose \(2\pi\)-equations are feasible with
   angles in \((0,\pi)\) and both sums \(4\pi\);
2. \(e\) is an equivalence relation on sides;
3. \(y\) is a legal radius-\(R\) patch of \(X(t,e)\);
4. for every escape record, \(S\not\subseteq t\) or \(F\not\subseteq e\);
5. for every empty or candidate record, \(t\not\subseteq T_0\) or
   \(e\not\subseteq\sim_0\).

Then every aperiodic pair \(\{A,B\}\) has \(\tau(A,B)\le(T_c,\sim_c)\)
(componentwise inclusion) for some candidate record. In particular, if
\(\mathcal K=\emptyset\), no pair of convex hexagons is aperiodic.

*Proof.* Let \(\tau=(T,\sim)\) be the type of an aperiodic pair. By Corollary
1, \(X(\tau)\) has a legal radius-\(R\) patch \(y\), and \(T\) is feasible.
So \((T,\sim,y)\) satisfies items 1–3, and therefore violates item 4 or 5.

* If item 4 fails for an escape record \((S,F)\), then \(S\subseteq T\) and
  \(F\subseteq\sim\). Closure of realisable \(T\) and transitivity of
  \(\sim\) give that the torus \(x\) is legal in \(X(\tau)\). This
  contradicts aperiodicity.
* If item 5 fails for an empty record, then \(\tau\le(T_0,\sim_0)\).
  Monotonicity gives \(X(\tau)=\emptyset\), again a contradiction.

So item 5 fails for a candidate record. \(\square\)

Realisability of the side lengths is *not* imposed. The certificate is
therefore stronger than needed, and is valid for all realisable pairs.
Theorem 3 is implemented by
[research/searches/two-hexagon-global-cegar.py](../searches/two-hexagon-global-cegar.py)
(CP-SAT for the query, z3 for exact angle feasibility, exact rational
linear algebra for closure). Results are reported in
[two-hexagon-global-census.md](two-hexagon-global-census.md).

## 4. A conserved quantity and why frequency arguments cannot decide

Fix the row class of direction \(D_0\). Cells \(z+jD_0\) are consecutive
along a row and share side-slot \(5\)/side-slot \(2\) ("rungs"). For a cell
with symbol \(\sigma\), put
\[\delta(\sigma)=\alpha(\sigma,0)+\alpha(\sigma,1)+\alpha(\sigma,2)-2\pi,\]
the sum of its three upper corners minus \(2\pi\). Then \(\delta(\sigma)\) is
the signed angle from the rung directed upward through the cell's
side-slot 2 to the rung through its side-slot 5.

This follows from the exterior-angle sum: going from the reversed side-slot-2
edge to the side-slot-5 edge across the lower half turns by
\(\pi-\sum_{\text{lower}}(\pi-\alpha)=\sum_{\text{lower}}\alpha-2\pi\), and
\(\sum_{\text{lower}}\alpha=4\pi-\sum_{\text{upper}}\alpha\). In particular
\(\delta=0\) iff the two rungs are parallel.

**Proposition 4 (rung-turning flux).** For a row segment of \(n\) cells and
the segment of the next row above it, let \(\Theta_n(r)\) be the sum of
\(\delta\) over the segment in row \(r\). Then
\(\Theta_n(r)=\sum_{\text{valleys}}\alpha-\sum_{\text{peaks}}\gamma\pm O(1)\)
for both \(r\) and \(r+1\), so \(|\Theta_n(r)-\Theta_n(r+1)|\le C\) with \(C\)
independent of \(n\).

Here a valley is a vertex of the boundary zigzag with one row-\(r\) corner
\(\alpha\). A peak is a vertex with two row-\(r\) corners and one
row-\((r+1)\) corner \(\gamma\).

*Proof.* Sum (V) over the boundary vertices. Row \(r\) gives
\(\sum(S_{\rm up}-2\pi)=\sum_{\rm peaks}(2\pi-\gamma)+\sum_{\rm valleys}\alpha-2\pi n\).
Row \(r+1\) gives
\(\sum(2\pi-S_{\rm down})=2\pi n-\sum\gamma-\sum_{\rm valleys}(2\pi-\alpha)\).
These agree up to the two end vertices. \(\square\)

**Corollary 4a.** In a doubly periodic configuration every row has total rung turning
exactly \(0\) over each of its periods, since cells one period apart are
translates. So for the integer counts \(n_\sigma\) of symbols in a
fundamental domain and each of the three row classes \(c\),
\(\sum_\sigma n_\sigma\,\delta_c(\sigma)=0\) holds exactly in
\(\mathbb R\). Double periodicity is needed here to give each row its own
period and a finite fundamental domain. A configuration having just one
nonzero period need not give every row a period; the strip argument in
Corollary 1 supplies a possibly different doubly periodic point of the
same SFT.

**Corollary 4b (obstruction to a natural aperiodicity proof).** Corollary 4a
suggests proving aperiodicity by forcing irrational frequencies, as in
Kari–Culik: rows with \(\mathbb Q\)-independent turnings. Every *convex*
relaxation of this idea fails:

* Rotating the lattice by \(\pi\) is a symmetry of \(X\), and it negates
  every \(\delta_c\).
* So any vector of local pattern frequencies satisfying the (rational)
  Kirchhoff/balance equations can be symmetrised to one satisfying all
  turning equations.
* The balance cone is rational, so it then contains a nonzero rational
  vector with zero turning.

Hence no linear-programming or frequency-balance certificate, at any finite
pattern radius, can prove that \(X(A,B)\) has no periodic point. An
aperiodicity proof for a hexagon pair must use non-convex information, for
example that a single configuration cannot mix a pattern with its half-turn.

## 5. Scope

The fresh repaired-proof review covers the exact equivalence (Corollary 1),
the faithfulness repair and completeness argument on which it rests, and
the geometric realisability step in the finite reduction (Theorem 2).
Soundness of the covering certificate (Theorem 3) is an internal proof.
The flux identity and its consequences (Section 4) are ancillary internal
claims outside that review; they are not used for the equivalence or
census.

Not proved: that every realisable type satisfies \(P(\tau)\). This is
exactly the remaining (6,6) obligation.

## 6. Reusable ternary native-contact pruning (2026-10-13)

The [single-cross-palette family obstruction](two-hexagon-single-cross-palette-obstruction.md)
adds a spatial gate beyond homogeneous endpoint palettes. For a generic
ternary A012012 with exactly the length partition(0,0,1,2,3,4), the three-colour
corner-arm graph has no closed three-ray AAA cycle, even with reflections.
This deletes all AAA local states without assuming a global colour phase.
Same-colour AAB fans then force equal B arms, their class intersection forces
B=L equilateral, and every B word fails a native AB endpoint test. Thus no
mixed SFT point exists; any realizable tileable type in this stratum has a
pure-B periodic escape by the reviewed monohedral dependency. This is a
conditional analytic reduction, not a newly computed global census record.

Reusable order of operations: enumerate reflected corner-arm cycles before
propagating palettes; derive allowed B arm pairs at native AAB fans; intersect
cyclic B side requirements; only then test polygon closure and successors.
An endpoint-palette coincidence is necessary for a mixed/pure transition but
does not ensure an actual third corner can close its two exposed rays. These
checks preserve parameter families because they use actual length equality
classes, not sampled distances. Extra equalities or extra stars change the
premises and must be checked anew.

## 7. Arbitrary-metric opposite-angle coverage and sparse-star removal

The independently reviewed [A012012 all-metric theorem](terra-ternary-opposite-a-all-metric-escape.md)
supersedes the five-class restriction in Section6 for the generic complementary
ternary angle family. For actual closed polygons, every legal one-of-each-colour
AAA metric cycle forces centrality: the positive sine closure kernel has
strict triangle inequalities, so none of its signed three-term sums vanishes.
Absent AAA, a six-neighbour native B colour contradiction excludes mixed
SFT points. This covers every side-equivalence relation and every B native
word in that angle family. It is a geometric coverage theorem, not an
angle-only empty region: central A has a periodic point, while other A metrics
may be unrealized or untileable. It must not be entered as an unconditional
empty patch certificate for arbitrary angle-only relaxed polygons.

The [resonance-removal extension](two-hexagon-opposite-a-resonance-removal.md)
(independently reviewed VALID) uses a different reusable mechanism.
A corner potential with zero sum on every whole tile and nonnegative sum on
all legal trivalent stars makes its positive stars O(R) in each translated
window. A new compactness limit contains only zero-score stars. Thus a
periodic-extension theorem for that restricted used-star language yields an
escape for the original actual polygons even when their exact angle triple
set contains additional unused resonances. This deletes used stars in a limit;
it does not change the actual polygon's angle equations or prove that its
full SFT is empty. On the six sole-ABB resonance lines, this reduces to the
reviewed exact-star A012012 theorem.

No claim is made that these native/order conditions cover arbitrary
higher-rank types. Do not discard noncovering ancestors of a higher-rank
closure or interpret the complete angle grid as joint polygon realization.
The [fresh independently reviewed all-native synthesis](two-hexagon-complementary-ternary-distinct-all-native-escape.md) now covers all eleven A bracelets, all121 fixed-colour native pairs, every actual metric specialization, and all six soleABB resonance lines. Remaining within complementary ternary angles: the equal-angle/120 lines, including all120. Other angle families and the general
pentagon-containing cases remain outside this reduction.

## 8. Reviewed angular family cuts in the complete global domain

The [full distinct/non120 all-native theorem](two-hexagon-complementary-ternary-distinct-all-native-escape.md) supplies an actual-polygon escape cut independent of side metrics. This is distinct from an abstract SFT empty record. The [fully reified encoder and hostile review](../reviews/two-hexagon-ternary-angular-filter-fresh-hostile-review.md) exclude its angle vectors in either species role using fifteen native pairings each, with exact multiplicity, interval and distinctness guards.

Complete angle-type representation is essential. For a covered vector, its full native triple set contains34 five-core equations; together with polygon sums they have rank10 on12 angles and force paired A values and doubled complements. Its exact type excludes repeated nativeAAA triples that would become legal if an A value were120 or two A values coincided. These exclusions force every representative of THAT EXACT type into the same distinct/non120 family; positive complementary B angles force A>90. Extra soleABB equations reduce dimension but do not change this reasoning. Thus a complete-grid representative cannot silently cover an uncovered realization of the same exact type. The argument does not apply to a partial type or to a necessary noncovering ancestor.

The [retained bounded query](../searches/two-hexagon-ternary-filtered-global-query.md) with this new cut at radius3/grid5394/60seconds returned UNKNOWN. It provides no new coverage of other types, polygon realization, infinite tilability or aperiodicity. The cut itself remains reusable; further global search requires a concrete new pruning mechanism or domain decomposition.
