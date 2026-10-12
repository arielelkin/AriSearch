# Ammann's three convex tiles: exact verification and strengthening of Healey's aperiodicity theorem (generic J; reflections and arbitrary contacts allowed)

**Status: Adversarially reviewed (computer-assisted, exact arithmetic).** Local review, reconstruction review and an independent re-review of all repairs are VALID ([local](../reviews/ammann-forcing-local-review.md), [reconstruction](../reviews/ammann-forcing-reconstruction-review.md), [re-review](../reviews/ammann-forcing-repair-rereview.md)). This is
an independent exact **verification and strengthening** of a known theorem,
V. O. Healey (2011), Thm 4.5 and Cor. 4.7. It is not a discovery; see
"Relation to the literature". The claim covers every \(J\) in the open, dense, full-measure set
\(\mathcal G^*\subset D\) defined below. In particular it covers the explicit
point \(J_0=\tfrac12+\tfrac45\omega\) and the four further points
\((s,t)=(\tfrac{9}{20},\tfrac34),(\tfrac{11}{20},\tfrac{17}{20}),(\tfrac37,\tfrac56),(\tfrac5{11},\tfrac79)\).
\(D\setminus\mathcal G^*\) is closed and contained in a locally finite union of
real algebraic curves, and the theorem is **not** claimed there (see "Gaps").
Two hostile reviews exist (see Changelog). Their defects are repaired here,
and the repairs were independently re-reviewed VALID
([re-review](../reviews/ammann-forcing-repair-rereview.md)); its three wording
points are applied.

Inputs: exact data from `ammann-two-class-reconstruction.md`.
Earlier literature note:
`research/literature/2026-10-11-convex-aperiodic-boundary.md`. That search did
not find Healey (2011); see the next section.

## Relation to the literature

* **Ammann's set.** Grünbaum–Shephard, *Tilings and Patterns* (1987),
  Fig. 10.3.28, assert aperiodicity, with Ammann's condition that the four
  segment lengths be distinct.
* **Healey 2011.** V. O. Healey, "A Family of Recompositions of the Penrose
  Aperiodic Protoset and its Dynamic Properties", *Rose-Hulman Undergraduate
  Mathematics Journal* 12(2) (2011).
  * Thm 4.5 and Cor. 4.7 prove that every tiling by the three tiles is
    mutually locally derivable with a Penrose tiling. Hence the protoset is
    aperiodic.
  * Hypotheses as reported to us:
    * adjacent tiles share complete edges (a stated convention, p. 97);
    * the free point is "allowable", meaning \(|AQ|,|BQ|,|CQ|,|RS|\) are
      pairwise distinct (our (G1));
    * the edge/angle relations of its Prop. 4.3 are treated as exhaustive;
    * reflections are not discussed.
  * The aperiodicity of Ammann's three tiles is therefore **established in the
    literature**.
* **Ammann–Grünbaum–Shephard**, "Aperiodic tiles", *Discrete Comput. Geom.*
  8 (1992) 1–25. Its composition technique, with congruence taken directly or
  oppositely, is the rigorous benchmark for Ammann's other sets (A2–A5). It
  does not treat the three convex polygons.

**What this proof adds to Healey's theorem:**

1. **No edge-to-edge convention is assumed.** Arbitrary partial contacts are
   allowed. T-junctions are *excluded* by proof (Lemma 3), under the explicit
   hypothesis (G2′).
2. **Reflections are handled explicitly.** Mirror copies are enumerated in the
   atlas, and every tiling is shown to be single-handed (Lemma 4).
3. **The vertex atlas is exact and computer-checked.** The relation list is
   complete by an exact enumeration (74 identical 360° relations, none at
   180°). The 162 edge-compatible stars are pruned to 14. The one unintended
   local configuration, the flipped \(P_1\) pair, is shown to die one edge
   away.
4. **The genericity hypothesis is explicit.** It is (G1)+(G2′), with exact
   certificates at five points and a proof that the exceptional set is closed
   and contained in a locally finite union of real algebraic curves.
5. **The Penrose step is self-contained.** An exact unique-composition proof
   for the induced arrow marking (Lemma 6) and an existence proof (Lemma 7)
   replace the citation to Penrose.

**A question, not a claim.** Healey's allowability condition is length-only.
By itself it does not exclude the extra angle relations that hold on the
(G2′) exceptional curves. For example, on the curve \(\chi=108^\circ\), the
corners P1-F and P2-H become 144° and 72°, and new 360° relations appear such
as P1-F + H6-B + P1-E. On those curves Prop. 4.3's relations may fail to be
exhaustive. We have not determined whether any allowable \(J\) on such a curve
admits a non-Penrose or periodic tiling.

(The set where the stronger certificate (G2) fails is dense. The (G2′)
exceptional set itself is closed and contained in a locally finite union of
curves, Lemma 2(c).)

**Scope relative to Healey.** The parameter range here is narrower than
Healey's: allowable \(J\) outside \(\mathcal G^*\) are not re-derived.

## Scripts and certificates

| step | script | certificate |
|---|---|---|
| angle identities, (G1)/(G2) certificates, exact relation enumeration, vertex stars, pruning | `research/searches/ammann-forcing-angles.py` | `research/certificates/ammann-forcing-angles.json` |
| cross-check against genuine Ammann tilings (not load-bearing) | `research/searches/ammann-forcing-patchcheck.py` | `research/certificates/ammann-forcing-patchcheck.json` |
| marked rhombs: unique composition (R1–R3), closure (R5), deflation legality (R6) | `research/searches/ammann-forcing-penrose-composition.py` | `research/certificates/ammann-forcing-penrose-composition.json` |

Replay (about 2 + 10 + 0.5 minutes):
```
C="conda run --no-capture-output -n arisearch python3"
$C research/searches/ammann-forcing-angles.py research/certificates/ammann-forcing-angles.json
$C research/searches/ammann-forcing-patchcheck.py research/certificates/ammann-forcing-angles.json 6 research/certificates/ammann-forcing-patchcheck.json
$C research/searches/ammann-forcing-penrose-composition.py research/certificates/ammann-forcing-penrose-composition.json
```

## Setting

\(\omega=e^{i\pi/5}\), \(K=\mathbb Q(\omega)\), \(J=s+t\omega\). The tiles are
\(H_6=[0,J',1,J,\omega,J'']\), \(P_1=[0,J',1,L,K]\) and
\(P_2=[K,L,1+\omega^2,J_2,\omega^2]\) (counter-clockwise), with
\(J',J'',K,L,J_2\) as in the reconstruction lemma. Every vertex is a
complex-affine function of \(J\). Corners are named by tile and vertex label:
H6-{A, J', B, J, D, J''}, P1-{E, J', F, L, K}, P2-{K, L, G, J2, H}.

**Domain.**
\(D=\{J: 0<s<1,\ 0<t<1,\ H_6,P_1,P_2 \text{ strictly convex and positively oriented}\}\).
\(D\) is open and contains \(J_0\). Sampling suggests
\(D=\{0<s,t<1,\ |J|^2>s+t\}\), but nothing below uses this.

**Tiling.** A countable family of closed sets, each congruent to
\(H_6,P_1\) or \(P_2\) by an isometry (reflections allowed). The sets cover
\(\mathbb R^2\) and have pairwise disjoint interiors. No contact condition is
imposed.

**Basic angles.** \(\chi\) = corner H6-J', \(\psi\) = corner H6-J'',
\(\kappa\) = corner P1-K.

**Genericity.**

* **(G1)** \(a=|J-C|\), \(b=|J-B|\), \(r=|J-D|\), \(c=|K-L|\) are pairwise
  distinct.
* **(G2′)** Every relation \(\sum_j m_j\theta_j(J)\in\{180^\circ,360^\circ\}\),
  with \(m_j\in\mathbb Z_{\ge0}\) over the 16 corner angles, is **identical**.
  That is, after substituting Lemma 1 its \(\chi,\psi,\kappa\) coefficients
  vanish.
* \(\mathcal G^*:=\{J\in D:\text{(G1) and (G2′)}\}\).
* A sufficient certificate for (G2′) is
  **(G2)**: \(1,\chi/\pi,\psi/\pi,\kappa/\pi\) are linearly independent over
  \(\mathbb Q\). The set where (G2) holds is **not** open; its complement is
  dense, since \(\chi/\pi\in\mathbb Q\) on a dense set. So (G2) is used only as a
  certificate at the listed points and to prove Lemma 2(c).

## Lemma 1 (edge labels and angle identities; exact, all \(J\in D\))

Every edge vector of every tile equals a unimodular constant times one of
\(J-C\), \(J-B\), \(J-D\) or \(K-L\), identically in \(J\). Hence the side
cycles are \((a,b,b,r,r,a)\), \((a,b,a,c,a)\) and \((c,r,r,a,b)\).

For every \(J\in D\) the 16 corner angles, in degrees, are:

| corner | angle | edges (cw ray, ccw ray) |
|---|---|---|
| H6-A, P1-E, P2-G | 72 | (a,a), (a,a), (r,r) |
| H6-B, H6-D | 144 | (b,b), (r,r) |
| H6-J', P1-J' | \(\chi\) | (b,a) |
| H6-J'', P2-J2 | \(\psi\) | (a,r) |
| H6-J | \(360-\chi-\psi\) | (r,b) |
| P1-F | \(252-\chi\) | (a,b) |
| P2-H | \(\chi-36\) | (b,a) |
| P1-K | \(\kappa\) | (a,c) |
| P1-L | \(216-\kappa\) | (c,a) |
| P2-K | \(360-\chi-\kappa\) | (c,b) |
| P2-L | \(144-\psi+\kappa\) | (r,c) |

*Proof.* Let \(\rho=(v_{i-1}-v_i)/(v_{i+1}-v_i)\in K(J)\). For a strictly
convex positively oriented polygon the interior angle is
\(\operatorname{Arg}\rho\in(0,\pi)\). For each corner with claimed angle
\(36c+p\chi+q\psi+r\kappa\), the script checks in \(K(J)\) that
\(\rho/(\omega^{c}\rho_\chi^{p}\rho_\psi^{q}\rho_\kappa^{r})\) is a constant
\(\lambda\in K\) with \(\lambda=\bar\lambda>0\). This gives the identity modulo
\(360^\circ\). The representative is then forced: all angles lie in
\((0,180)\), so \(\theta-p\chi-q\psi-r\kappa\) lies in an explicit open interval
containing exactly one admissible value (checked by the script). ∎

## Lemma 2 (the listed points are in \(\mathcal G^*\); \(\mathcal G^*\) is open, dense and of full measure)

**(a)** At all five listed points the tiles are strictly convex, and
\(a^2,b^2,r^2,c^2\in\mathbb Q(\sqrt5)\) are pairwise distinct (exact).

**(b)** Put \(w_\theta=\rho_\theta/\bar\rho_\theta\in K\). A relation
\(n_0\pi+n_1\chi+n_2\psi+n_3\kappa=0\) implies
\(w_\chi^{n_1}w_\psi^{n_2}w_\kappa^{n_3}=1\). At each listed point, the
3-row matrix of valuations of \(w_\chi,w_\psi,w_\kappa\) at the prime ideals of
\(K\) has rank 3. All five matrices are stored in the certificate. The primes
involved lie above:

| point | primes |
|---|---|
| \(J_0\) | 11, 41, 181, 251, 1031 |
| (9/20, 3/4) | 4441, 26321, 35401, 116461 |
| (11/20, 17/20) | 11, 41, 131, 281, 911, 5171 |
| (3/7, 5/6) | 11, 61, 101, 151, 37021, 42491, 1025161 |
| (5/11, 7/9) | 61, 271, 46411, 258871, 886741, 24167551 |

Hence (G2) holds at these points.

(G2) implies (G2′). Write the relation via Lemma 1 as
\(n_0\cdot36^\circ+n_1\chi+n_2\psi+n_3\kappa=0\); then
\(n_1=n_2=n_3=0\). So all five points lie in \(\mathcal G^*\).

**(c)** Fix a non-identical non-negative vector \(m\), with target
\(T\in\{180,360\}\) and \((n_1,n_2,n_3)\neq0\). Let
\(Z_m=\{J\in D:\sum m_j\theta_j(J)=T\}\). On \(Z_m\) we have
\(\prod_j(\rho_j/\bar\rho_j)^{m_j}=e^{2iT^\circ}=1\). By Lemma 1 the left side
equals \(\omega^{2\sum m_jc_j}\,w_\chi^{n_1}w_\psi^{n_2}w_\kappa^{n_3}\), a
rational function of \((s,t)\).

At \(J_0\) it is \(\neq1\). Otherwise \(w_\chi^{n_1}w_\psi^{n_2}w_\kappa^{n_3}\)
would be a root of unity, with zero valuation vector, contradicting rank 3.
So the numerator \(N_m(s,t)\) of "product \(-1\)" is a nonzero polynomial,
and \(Z_m\subset\{N_m=0\}\), a real algebraic set of dimension at most 1. The
six equalities excluded by (G1) are likewise nonzero polynomials, nonzero at
\(J_0\).

On a compact \(C\subset D\), every corner angle is at least some
\(\varepsilon_C>0\), so only the finitely many \(m\) with
\(\sum m_j\le 360/\varepsilon_C\) matter. Hence \(D\setminus\mathcal G^*\) is closed
and contained in a locally finite union of closed real algebraic sets of
dimension at most 1.
\(\mathcal G^*\) is therefore open, dense and of full measure in \(D\). ∎

(Lemmas 3–6 use **only** (G1) and (G2′).)

## Lemma 3 (no T-junctions; every tiling is edge-to-edge; \(J\in\mathcal G^*\))

There is **no** identical relation with sum 180. There are exactly **74**
identical relations with sum 360.

*Exact enumeration (no floats).* An identical relation has vanishing
\(\chi,\psi,\kappa\) coefficients. So it takes the value \(T\) for **any**
substituted values \(\chi',\psi',\kappa'\). Choose rationals making all 16 corner
values positive; the script checks this exactly. Then \(m_j\le T/\theta'_j\),
and partial sums never exceed \(T\), in exact Fraction arithmetic.

The enumeration was run with five such triples: the true angles at the five
listed points, rounded to 3 decimals. All five give the same set, 0 and 74
(`relation_enumeration_cross_check` in the certificate). Floats are used
only to *choose* the dummy values; correctness needs only the exact
positivity check.

Suppose a vertex \(p\) of some tile lies in the relative interior of an edge
of a tile \(T\). Then the tiles meeting \(p\) on the other side of that edge
have corners at \(p\) summing to exactly \(180^\circ\). A second tile with
\(p\) in an edge interior would fill that half-disc alone. By (G2′) such a
relation would have to be identical, and there is none.

Hence no tile vertex lies in the interior of another tile's edge. Edges that
overlap in positive length therefore coincide. At every vertex, consecutive
corners share a full edge, and by (G1) that edge carries the same label.
Every tiling is **edge-to-edge**. ∎

## Lemma 4 (vertex atlas; \(J\in\mathcal G^*\))

Every vertex star of every tiling is one of the following 14 stars, all of
one orientation (shown here as direct; ccw order):

```
J-type:  [H6-J, P1-J', P2-J2]   [H6-J, P1-J', H6-J'']
K-type:  [P1-J', P1-K, P2-K]    [H6-J', P1-K, P2-K]
L-type:  [P1-L, P2-J2, P2-L]    [H6-J'', P2-L, P1-L]
Penrose-vertex type:
 [P2-G]x5   [P1-E]x5   [H6-D, P2-G, P2-G, P2-G]   [H6-D, H6-D, P2-G]
 [H6-B, P2-H, P1-F]   [H6-A, P1-F, P2-H, P1-E]
 [H6-A, P1-E, P1-E, P1-E, P1-E]   [H6-A, P1-E, H6-A, P1-E, P1-E]
```

Consequently **every tiling uses copies of a single handedness only**.
Tiles sharing a vertex have equal handedness, and the adjacency graph is
connected.

*Proof (script).* By (G2′), every star realises one of the 74 identical
relations. These give 162 cyclic, edge-length-compatible stars, counted up
to rotation and global reflection.

The stars are pruned to a fixed point by the necessary **edge-consistency
condition**. Let \(X\) (tile \(T\)) and \(Y\) (tile \(U\)) be consecutive
corners at \(v\) sharing the edge \(vw\), with \(U\) after \(T\) in ccw order.
Then the far corners of \(U\) and \(T\) must be consecutive, in that order, in
some surviving star.

142 stars are removed in round 1 and 6 in round 2, leaving 14. The
`patchcheck` cross-check is not load-bearing. In exact decorated deflation
patches, every observed star is viable and every viable star occurs (2726
complete vertices at 6-fold deflation).

The facts used below can be checked by hand from the relation list:

* **(i)** The relations containing H6-J are \(\{\)H6-J, \(\chi\), \(\psi\}\).
  Those containing P2-K are \(\{\)P2-K, P1-K, \(\chi\}\), and those containing
  P2-L are \(\{\)P2-L, P1-L, \(\psi\}\). Every \(\chi\)-corner (H6-J', P1-J')
  lies in an H6-J or P2-K relation, and every \(\psi\)-corner (H6-J'', P2-J2)
  in an H6-J or P2-L relation.
* **(ii)** The other relations containing P1-K or P1-L are
  \(\{\)P1-K, P1-L\(\}\cup X\), where \(X\) is one 144° corner or two 72°
  corners. Edge lengths force P1-K and P1-L to share their c-edge and \(X\) to
  be two (a,a) corners (H6-A or P1-E). This is the **flipped \(P_1\) pair**.

  It dies one edge away. The (a,a) corner \(V\) adjacent to the second
  \(P_1\)'s a-edge ends at that \(P_1\)'s F corner (\(252-\chi\)), next to a
  far corner of \(V\) in \(\{\)H6-J', H6-J'', P1-J', P1-K\(\}\). The relations
  containing P1-F are \(\{\)P1-F, P2-H\(\}\) plus 72°/144° corners only. So no
  star accommodates them.

  Hence P1-K occurs only in K-type stars and P1-L only in L-type stars. The
  edge patterns are forced: (a,c) | (c,b) | (b,a) at K, and
  (c,a) | (a,r) | (r,c) at L. ∎

## Lemma 5 (reconstruction of a marked rhomb tiling; \(J\in\mathcal G^*\))

Cut each tile along its **chords**: \(H_6\) along \(0\!-\!1\) and
\(0\!-\!\omega\); \(P_1\) along \(0\!-\!1\); \(P_2\) along
\(\omega^2\!-\!(1+\omega^2)\). The pieces are:

* \(H_6\): quad \(ABJD\), an X-triangle (sides a, b; apex J'), and a
  Y-triangle (sides r, a; apex J'');
* \(P_1\): quad \(EFLK\) and an X-triangle;
* \(P_2\): quad \(KLGH\) and a Y-triangle.

By (G1), the side cycles admit no symmetry, so the pieces of a placed tile
are well defined.

Let \(\mathcal T\) be any tiling. Group the pieces as follows:

* **Thin.** For each \(H_6\): its quad, the X-triangle of the
  \(\chi\)-corner tile at its J-vertex, and the Y-triangle of the
  \(\psi\)-corner tile there.
* **Thick.** For each \(P_1\): its quad, the quad of the unique \(P_2\)
  sharing its c-edge with \(K\leftrightarrow K\), the X-triangle at \(K\), and
  the Y-triangle at \(L\).

Then:

1. Each group is a unit thin, resp. thick, rhomb. Around \(J\) (resp. \(K\)
   and \(L\)) the pieces fill \(360^\circ\) with the forced edge pattern, so
   their union is a disc bounded by the image of \(ABCD\) (resp. \(EFGH\))
   under the placing isometry. The \(P_2\) shares \(K\), \(L\) and the
   handedness, hence also the placement.
2. Every piece lies in exactly one group (Lemma 4(i)). So the rhombs tile the
   plane.
3. Every rhomb edge is a chord of exactly one tile, with that tile's quad and
   triangle on opposite sides. So the rhomb tiling is edge-to-edge.
4. Mark each rhomb edge by the triangle type (X or Y) on it, oriented from the
   triangle's a-end:

   \[
   \text{thin } A\!\to\!B,\ C\!\to\!B \ (X),\quad A\!\to\!D,\ C\!\to\!D\ (Y);\qquad
   \text{thick } E\!\to\!F,\ E\!\to\!H\ (X),\quad F\!\to\!G,\ H\!\to\!G\ (Y).
   \]

   Both rhombs at an edge read the same triangle, so the marks agree: this is
   a **legal marked-rhomb tiling**.

**Orientation rule** (needed for the converse). In both rhombs:

* for an X edge, the quad lies on the **left** of the arrow and the triangle
  on the right;
* for a Y edge, the quad lies on the **right** and the triangle on the left.

Check: thin AB (A→B) has the rhomb interior on its left and is a receiving
edge (quad side). Thin BC (arrow C→B) has the interior on its right and
gives its triangle. The same check works for CD, DA, EF, FG, GH and HE.

Two rhombs sharing an edge with equal marks lie on opposite sides of the
arrow. So **exactly one** of them has its quad on that edge and the other
its triangle.

The construction is canonical, so any isometry preserving \(\mathcal T\)
preserves the rhomb tiling.

**Converse (decoration).** Let a legal marked-rhomb tiling be given and
\(J\in D\). By the orientation rule, every triangle lies across exactly one
receiving edge, from exactly one quad. Each quad together with the triangles
across its receiving edges is a congruent copy of \(H_6\), \(P_1\) or \(P_2\).
The pieces partition the plane, so this is a tiling by the three shapes. ∎

## Lemma 6 (marked rhombs: unique composition; no translations)

**Statement.** Let \(T\) be any legal tiling by the marked unit rhombs. Then
there is a legal tiling \(C(T)\) by the same marked rhombs scaled by
\(\varphi\), with these properties:

* its Robinson deflation (Preshing's rule \(\sigma\)) is the half-rhomb
  tiling of \(T\);
* \(C(T+x)=C(T)+x\) for every translation \(x\).

Consequently **no legal tiling has a nonzero translational symmetry**.

*Proof (script, exact in \(\mathbb Z[\omega]\), no floats).*

* **R1 (stars).** 14 raw rhomb vertex stars; after edge-consistency pruning, 8
  remain.
* **R2 (patches).** For each of the 8 stars at the origin, enumerate all
  consistent choices of stars at every neighbouring vertex. This gives 85
  patches, a superset of the real radius-1 patches.
* **R3 (uniqueness).** For every patch and every half \(t\) at the origin,
  call a parent hypothesis \(H\) **valid** if every \(\sigma\)-child of \(H\)
  and of its mirror twin \(H^*\) is a half of the patch. Of the 5 algebraic
  hypotheses, exactly one is valid in every case: 564 cases, 0 failures.

  Locality is asserted in code: the pivot of \(H\) (\(C\) for red, \(R\) for
  blue) is a vertex of \(t\), and every child of \(H\) and \(H^*\) contains it.
  So validity in the tiling equals validity in the patch.

Let \(P(t)\) be the valid \(H\). Validity of \(H\) depends on \(T\) only and is
shared by all children of \(H\); for \(H^*\), whose twin is \(H\), the same
holds. So siblings get the same parent, and the halves are partitioned into
the children of valid twin pairs. Distinct valid parents share no child,
hence have disjoint interiors. The \(\varphi\)-rhombs \(R=H\cup H^*\) tile the
plane.

**Edge-to-edge with matching marks (closure).** Let \(R\) be a valid
\(\varphi\)-rhomb, \(e\) one of its edges, and \(h\) the child of \(R\) whose
base lies on \(e\). From the substitution, these are:

* a blue whose base is the whole Y-leg (labels B = head, C = tail), or
* a red whose base is the head-end segment of length \(1/\varphi\) of an X-leg
  (B = split point, C = head).

(Children whose base lies on a parent *diagonal*, namely blue\((Q,R,B)\), have
their twin inside the same parent rhomb.)

The twin \(h^*\) lies across \(e\), outside \(R\), and belongs to some valid
\(R'\). Each of \(h^*\)'s parent hypotheses is one of two kinds:

* **(α)** a rhomb having \(h\) itself among its children. This is impossible
  for \(R'\): \(h\) would then have two valid parents, contradicting the
  disjointness above. This is the case where \(h^*\) would play a "diagonal"
  or other interior role in \(R'\).
* **(β)** a rhomb having \(e\) as a full edge with the same type and direction.
  This follows by hand because twins share their B and C labels, and those
  labels determine the leg as above.

Check R5 enumerates every outward child of both big rhombs and every parent
hypothesis of its twin: 20 cases, 4 of type (α), 16 of type (β), 0 of
neither.

So \(R'\) shares the full edge \(e\) with \(R\), with equal marks. Hence
\(C(T)\) is edge-to-edge and legal, and \(C(T)/\varphi\) is again legal.

**No translations.** If \(T+x=T\) with \(x\ne0\), then \(C^k(T)+x=C^k(T)\) for
all \(k\). Once the inradius \(\varphi^k r_0\) exceeds \(|x|\), a tile \(\Pi\)
and \(\Pi+x\) overlap in interior. So \(\Pi=\Pi+x\), which is impossible.

**Sanity check** (not used): on a 5-fold Preshing patch, all 2250 children
with interior parent rhombs recover their true parent. ∎

This lemma is self-contained and needs no identification of the marking with
Grünbaum–Shephard's P3 arrows.

**Remark (not used).** That identification is supported only as
computational evidence, by the reconstruction review
(`research/reviews/ammann-forcing-reconstruction-review.md`). There:

* Robinson P3 patches obey the marking;
* the 8 surviving stars are exactly the P3 stars;
* exact 2-SAT shows that pentagrid tilings with \(\Sigma\gamma=0\) are markable,
  while generalized ones with \(\Sigma\gamma=1/2,1/5\) are not.

## Lemma 7 (existence of a legal marked-rhomb tiling of the plane)

Call a finite set of halves (marked Robinson triangles) with disjoint
interiors a **legal half-patch** if any two halves meeting along a boundary
segment of positive length share a full edge, either:

* legs with equal mark (type and head), or
* bases, between twins (same colour, same B and C labels).

**(a)** If \(\mathcal Q\) is a legal half-patch at scale \(\varphi\), then
\(\sigma(\mathcal Q)\) (all children) is a legal half-patch.

*Proof.* Take two children meeting in a segment of positive length.

* If they have the same parent, check R6(a) applies: the internal edges of
  the children of each big half are each shared by exactly two children,
  compatibly.
* Otherwise the segment lies on the boundaries of both parents. Parents
  meeting only in a point cannot contain it, so by legality of \(\mathcal Q\)
  the parents share a full edge \(E\) legally.

Check R6(b) covers every legal contact of two big halves along a full edge,
up to rotation: twin bases and equal-mark legs, both rhomb types, all 10
rotations of the partner, interiors on opposite sides (exact sign test).
In each case the children lying on \(E\) induce the same partition of \(E\)
from both sides, with compatible kinds. Totals: 4 single halves, 20
contacts, 30 child-edge matches, 0 failures. ∎

**(b)** A legal marked-rhomb tiling of the plane exists.

*Proof.* Start from the two halves of one rhomb, a legal half-patch. By (a),
\(\mathcal Q_n=\sigma^n(\mathcal Q_0)\), scaled to unit legs, is a legal
half-patch covering the rhomb scaled by \(\varphi^n\). A half whose base is not
on the outer boundary is paired with its twin. So \(\mathcal Q_n\) contains a
legal rhomb patch covering a disc of radius
\(\varphi^n r_0-1\to\infty\).

Translate so that a vertex near the centre is at the origin. All edge vectors
lie in the finite set \(\{\pm\omega^k,\pm\omega^k/\varphi,\pm\omega^k\varphi\}\),
and the edge graph of the rhombs meeting the disc \(B(m+4)\) is connected with a
bounded number of edges. Hence only finitely many configurations of the rhombs
meeting \(B(m)\) can occur (finite local complexity).

By König's lemma (diagonal extraction) there is a nested sequence of legal
patches whose union is a tiling of the plane. Legality is a pairwise local
condition, so the union is legal. ∎

## Theorem (\(J\in\mathcal G^*\); in particular the five listed points)

1. \(\{H_6,P_1,P_2\}\) admits tilings (Lemmas 7 and 5, converse).
2. Every tiling, with reflections and arbitrary contacts allowed, has the
   following properties:
   * it is edge-to-edge;
   * it uses one handedness only;
   * its vertex stars are among the 14 stars of Lemma 4;
   * it is the Ammann recomposition of a legal marked-rhomb tiling.
3. No tiling has a nonzero translational symmetry; singly periodic tilings
   are excluded.

So, for these \(J\), the set is **aperiodic in the strong sense**: three
unmarked convex polygons, with reflections and arbitrary contacts allowed.

*Proof.* Lemmas 3–5 give the structure, and Lemmas 7 and 5 give existence.
A translation of the tiling is a translation of the rhomb tiling (Lemma 5),
which Lemma 6 excludes. ∎

## Gaps and limits (stated precisely)

* **Non-generic \(J\).** The theorem is not claimed on
  \(D\setminus\mathcal G^*\). This set is closed and contained in a locally
  finite union of real algebraic curves, on which some non-identical 180°/360° relation holds or two side
  lengths coincide; it was not computed explicitly. There, new stars or
  T-junctions may appear. Example from the local review: on \(\chi=108^\circ\),
  P1-F = 144° and P2-H = 72°. The circumcentre point
  \(s=t=(5+\sqrt5)/10\) is periodic (two-class lemma). Whether other
  exceptional \(J\) admit non-Ammann or periodic tilings is not determined here.
* **Ammann's condition.** Distinct lengths (G1) alone is not shown to suffice;
  the proof uses (G2′) as well.
* **Computer assistance.** Every proof-relevant decision is exact:
  * symbolic identities in \(K(J)\);
  * exact signs in \(\mathbb Q(\omega)\);
  * ideal factorisation (Sage/PARI);
  * Fraction arithmetic for the relation enumeration;
  * integer \(\mathbb Z[\omega]\) geometry with exact signs in
    \(\mathbb Z[\varphi]\) for the rhomb part.

  Floats are used only to *choose* dummy rationals and in the optional patch
  cross-check's face tracing, which is guarded by an exact area identity.
* **Shared modelling.** The local reviewer's independent checker uses the
  same mathematical model: vertex star = cyclic word, plus the far-endpoint
  pair test. The model was attacked by hand and found sound, but a shared
  modelling error would be common-mode.
* **Compactness step** (Lemma 7(b)) is the standard extension argument,
  written out but not formalised.
* **Domain description.** \(D=\{|J|^2>s+t\}\) remains sampling evidence and is
  not used.

## Changelog

Repairs after the reviews `research/reviews/ammann-forcing-local-review.md`
(L1–L5 valid) and `research/reviews/ammann-forcing-reconstruction-review.md`
(R1–R3 valid):

* **Local D1 (statement).** "\(D\setminus\mathcal G\) ⊂ locally finite union of
  curves" was false: the (G2) failure set is dense. The theorem is now stated
  for \(\mathcal G^*\), defined by (G1) and the new condition (G2′). (G2) is
  kept only as a pointwise certificate. Lemma 2(c) now proves that
  \(D\setminus\mathcal G^*\) is a locally finite union of algebraic curves.
  Lemmas 3–6 were checked to use only (G1) and (G2′).
* **Local D2.** The float multiplicity bound and float partial-sum pruning
  were replaced by exact Fraction enumeration with positive rational dummy
  angles (`identical_relations` in `ammann-forcing-angles.py`).
* **Local D3.** The unrecorded CP-SAT cross-check claim was removed. The
  multi-point cross-check is now real: exact enumeration at five dummy
  triples, recorded in `relation_enumeration_cross_check` in the
  certificate.
* **Local D4.** Valuation matrices and prime lists for all five points are
  stored (`points_tested[*].valuation_matrix_rows_chi_psi_kappa`).
* **Reconstruction D1.** Added the twin-role analysis, cases (α)/(β), to
  Lemma 6, with the exact check R5 (20 cases, 0 failures).
* **Reconstruction D2.** Added Lemma 7: existence of a legal rhomb tiling
  through the exact check R6 (deflation preserves legal half-patches) plus
  compactness.
* **Reconstruction D3.** Deleted the overclaim that the star count and the
  deflation sanity check identify the marking with P3. The reviewer's 2-SAT
  evidence is cited as a non-load-bearing remark.
* **Reconstruction D4.** Added the orientation rule to Lemma 5 (X: quad on
  the left of the arrow; Y: on the right), which shows each edge has a quad
  on exactly one side.
* Status reworded to "Proved internally"; not marked reviewed.
* **Literature reframing** (coordinator update). Retitled as an independent
  exact verification and strengthening of Healey (2011), Thm 4.5 and
  Cor. 4.7. Added "Relation to the literature", citing Healey and
  Ammann–Grünbaum–Shephard (DCG 8, 1992), and stated what is added. Removed
  the "no prior proof located" phrase. Posed the length-only allowability
  issue on the (G2′) exceptional curves as an open question.

* **Root (after re-review).** Applied re-review wording points W1 (exceptional
  set "closed and contained in" a locally finite union of curves), W2 (finite
  local complexity phrased for the rhombs meeting B(m)) and W3 (scope narrower
  than Healey's; "not determined here"). Made `ammann-forcing-angles.py`
  deterministic (sorted permutation iteration); the regenerated certificate is
  byte-identical across hash seeds and equal in content to the previous one.
