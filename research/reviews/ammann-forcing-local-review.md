# Hostile review: local part (Lemmas 1–4, genericity) of `ammann-forcing-aperiodicity.md`

**Status update (2026-10-12):** this is the original review and defect record.
The repairs are complete and have a [VALID fresh rereview](ammann-forcing-repair-rereview.md).
Read the [current lemma](../lemmas/ammann-forcing-aperiodicity.md) for its G* hypotheses.


Reviewer: independent, adversarial. I did not develop this work. Scope: claims L1–L5
below. Lemma 5 (rhomb reconstruction) and Lemma 6 (Penrose composition) are **out of scope**
and were not reviewed.

Independent checkers. They are written from the lemma's statements and import nothing from
`research/searches/`:

* `research/reviews/verify_ammann_forcing_local_stars.py` [s t] checks L1, L2, L3, L4 and L5
  at one point.
* `research/reviews/verify_ammann_forcing_local_genericity.py` checks the genericity
  statement.

Replay:

```
C="conda run --no-capture-output -n arisearch python3"
$C research/reviews/verify_ammann_forcing_local_stars.py            # J0 = 1/2 + 4/5 w
$C research/reviews/verify_ammann_forcing_local_stars.py 9/20 3/4   # also run: 11/20 17/20, 3/7 5/6, 5/11 7/9
$C research/reviews/verify_ammann_forcing_local_genericity.py
```

Each run takes about 30 s. Every decision is exact: arithmetic is done in
\(K(x)\), \(K=\mathbb Q(\zeta_{10})\), or in \(\mathbb Q(\zeta_{30})\) and QQbar/AA for the
genericity script. The multiplicity bound is exact rational arithmetic (see L2). The only
floats are printed sanity values.

## Claims under review

* **L1.** The 16 corner angles are fixed integer combinations of 36°, χ, ψ and κ, for all
  \(J\in D\).
* **L2.** At \(J\in\mathcal G\) no non-negative integer combination of corner angles equals
  180°. Hence there are no T-junctions and every tiling is edge-to-edge.
* **L3.** There are 74 identical 360°-relations. They give 162 edge-compatible stars up to
  rotation and reflection. Pruning leaves 14 stars, all of one handedness.
* **L4.** The hand facts (i) hold, and the flipped-\(P_1\) c-edge contact dies one edge away.
* **L5.** (G2) at \(J_0\) has valuation rank 3, with primes above 11, 41, 181, 251 and 1031.
  (G1) holds exactly.
* **Implicit claim (header and Lemma 2(c)).** \(D\setminus\mathcal G\) is contained in a
  locally finite union of real algebraic curves.

## Checks performed

### L1: angle identities

I rebuilt the tiles from the task-statement formulas and labelled the edges. A label is
assigned when the ratio to \(x-C\), \(x-B\), \(x-D\) or \(K-L\) is a unimodular constant in
\(K(x)\). The side cycles came out as \((a,b,b,r,r,a)\), \((a,b,a,c,a)\) and \((c,r,r,a,b)\).

I did not copy the coefficient table. For each corner I **searched** all
\(c\in\{0..9\}\) and \(p,q,r\in\{-2..2\}\) for which
\(\rho_j/(\omega^c\rho_\chi^p\rho_\psi^q\rho_\kappa^r)\) is a positive real constant. I then
pinned the representative by interval counting, using only \(0<\theta,\chi,\psi,\kappa<180\).
For every corner the result was a **unique** pinned identity, and it equals the lemma's table
entry. The (cw, ccw) edge pairs also match the table. **No defect.**

Reflection bookkeeping: a mirror corner has the same angle with its two rays swapped. Both
the authors' code and mine do exactly this.

### L2: no 180° relation, and the edge-to-edge implication

*Computation.* I avoided the authors' float bound entirely. An identical relation has zero
χ, ψ and κ coefficients. So for **any** rational "dummy" values \(\chi',\psi',\kappa'\) that
make all 16 corner values positive, it satisfies \(\sum m_j\theta'_j=180\) (resp. 360)
exactly. That gives the rigorous rational bound \(m_j\le 360/\theta'_j\). I took
\(\chi',\psi',\kappa'\) to be 3-decimal rationals near the true angles at each test point.
Result at all five listed points: **0** identical 180-relations and **74** identical
360-relations. This agrees with the certificate.

*Implication.* I attacked it case by case:

* **One tile with \(p\) in an edge interior.** Suppose \(p\) is a vertex of tile \(S\) and lies
  in the relative interior of an edge of \(T\). Then \(T\) locally fills a closed half-disc. Any
  other tile \(U\) with \(p\) in the relative interior of one of its edges also fills a
  half-disc. Disjoint interiors force it to be the complementary one, which leaves no room
  for \(S\). So every other tile at \(p\) has \(p\) as a vertex. Their corners fill exactly
  180°, which is a non-negative relation. Only finitely many tiles meet \(p\), because angles
  are bounded below. **Sound.**
* **Mirror copies.** They have the same angles, so they are covered by the same relation
  set. **Sound.**
* **Overlapping collinear edges.** Suppose edges \(e\subset T\) and \(f\subset U\) overlap in
  a segment of positive length. An endpoint of \(e\) strictly inside \(f\) would be a
  T-junction. So the endpoints coincide and \(e=f\). At every vertex, consecutive tiles share
  their full edge from that vertex. With (G1), equal length means equal label. **Sound.**
* **Corner-meets-corner with the rest filled by an edge interior.** This is exactly the
  180° case above. **Covered.**
* **Strict convexity.** No corner is 180°, so no degenerate "vertex" lies on a straight
  boundary.

**L2 is valid for \(J\in\mathcal G\).**

### L3: stars and pruning

**Stars.** I wrote my own DFS, which differs from the authors' permutation × orientation
product. It enumerates cyclic sequences of (corner, d/m) whose consecutive rays have equal
labels, and canonicalises them under rotation and global reflection. A global reflection
reverses the order and flips every orientation. Result: **162** stars. **134** of them mix
handedness, so mixed stars are genuinely enumerated.

**Pruning.** I implemented it independently, keeping both chiral copies explicitly. For
consecutive \(X\) then \(Y\) (ccw) at \(v\), sharing \(X\)'s ccw ray and \(Y\)'s cw ray:

* the far corners are \(X'=\) far(\(X\), ccw) and \(Y'=\) far(\(Y\), cw);
* for a direct tile the ccw ray goes to vertex \(i-1\) and the cw ray to \(i+1\); a mirror
  tile is swapped;
* \((Y',X')\) must be consecutive in some live star.

I re-derived the order \((Y',X')\) at \(w\) from a coordinate picture. The checker also
asserts that the shared edge has the same label seen from both ends.

Result: 284 then 12 oriented stars removed, which is 142 and 6 up to reflection. The
survivors are **14** stars, all single-handed, and they are exactly the 14 listed in
Lemma 4. The six round-2 kills are the \(H_6\)-A-heavy stars, for example \([H6\text{-}A]^5\).

**Soundness of pruning.** A star is removed only if some consecutive pair has **no**
consecutive far pair in any surviving star. If a star occurs at \(v\) in a tiling, the star
actually present at \(w\) contains that far pair. So by induction no star that occurs in a
tiling is ever removed. This is a "no completion exists" test, not a "one completion fails"
test. **Sound.**

**Points not missed:**

* *Both orientations of an edge pair.* Edges carry no direction. The gluing is fully fixed
  by the two corners at \(v\), and both orientations of every corner are enumerated.
* *Equal lengths across labels.* Excluded by (G1), which I verified exactly at all five
  points.
* *Corners with equal labels on both rays* (\(H6\)-A, \(P1\)-E, \(P2\)-G, \(H6\)-B,
  \(H6\)-D). Both orientations were tried, and their far corners differ.
* *Same corner type twice*, for example two \(P_1\)-K corners at one vertex. This is
  allowed by the DFS.

**Single handedness globally.** All 14 stars are monochiral, and in an edge-to-edge tiling
two edge-adjacent tiles share a vertex. Suppose two handedness domains met. Their common
boundary would contain an edge between a d-tile and an m-tile, and its endpoint would carry
a mixed star, which is not viable. So this is **impossible**. A whole tiling made only of
mirror copies is the global mirror image of a direct tiling, and is fine.

**"Matching Ammann patches."** I did **not** independently verify the lower bound, that every
one of the 14 stars occurs in a genuine Ammann tiling (`patchcheck`). It is **not
load-bearing**: the theorem needs only the upper bound.

### L4: hand facts

* (i) I checked this against my relation list:
  * \(H6\)-J appears only in \(\{H6\text{-}J,\chi,\psi\}\), 4 relations.
  * \(P2\)-K appears only with \(\{P1\text{-}K,\chi\}\).
  * \(P2\)-L appears only with \(\{P1\text{-}L,\psi\}\).
  * Every χ-corner and every ψ-corner lies in an \(H6\)-J or \(P2\)-K / \(P2\)-L relation.
  * The edge pattern inside K-type and L-type relations forces a single orientation. I
    checked this by hand from the ray table.

  **Valid.**
* (ii) **Valid.** The P1-K and P1-L relations not involving P2-K or P2-L are
  \(\{P1\text{-}K,P1\text{-}L\}\cup X\), with \(X\in\{H6\text{-}B,\ H6\text{-}D\}\) or a pair
  of 72° corners. Within such a relation, only \(P1\)-K and \(P1\)-L carry a c-ray, so they
  share the c-edge. Their remaining a-rays force \(X\) to be two (a,a) corners, \(H6\)-A or
  \(P1\)-E. A d/m mixture of the two \(P_1\) corners is ray-incompatible, so the two \(P_1\)
  tiles have equal handedness.

  Follow the second \(P_1\)'s a-edge from L. It ends at that tile's F (index 2). The
  neighbouring (a,a) corner \(V\) ends, in either orientation, at
  \(H6\)-J′, \(H6\)-J″, \(P1\)-J′ or \(P1\)-K. Every relation containing \(P1\)-F is
  \(\{P1\text{-}F,P2\text{-}H\}\) plus 72°/144° constants (8 relations, listed by the
  checker), and none contains a χ, ψ or κ corner. So the hand kill is **correct**. It is also
  subsumed by the computer pruning.

### L5: (G1) and (G2) at the listed points

I used my own code path. The candidate rational primes are taken from \(N(\rho_\theta)\),
because \(N(w_\theta)=1\) is useless. I then used `primes_above` and element valuations.

| point | primes | rank | (G1) | strictly convex |
|---|---|---|---|---|
| \(J_0\) | 11, 41, 181, 251, 1031 | 3 | yes | yes |
| (9/20, 3/4) | 4441, 26321, 35401, 116461 | 3 | yes | yes |
| (11/20, 17/20) | 3, 11, 41, 131, 281, 911, 5171 | 3 | yes | yes |
| (3/7, 5/6) | 5, 11, 61, 101, 151, 37021, 42491, 1025161 | 3 | yes | yes |
| (5/11, 7/9) | 2, 61, 271, 46411, 258871, 886741, 24167551 | 3 | yes | yes |

(G1) and convexity are exact; convexity means all three tiles strictly convex and ccw.

The logic also holds. \(n_0\pi+\sum n_j\theta_j=0\) implies \(\prod w_j^{n_j}=1\). A rank-3
integer valuation matrix forces \(n=0\), and then \(n_0=0\). Under (G2), any relation
\(\sum m_j\theta_j\in\{180,360\}\) must have zero χ, ψ and κ coefficients, so it is
identical. **Valid.**

L1–L4 were also fully recomputed at all four other points, not just one. The counts were
identical everywhere: 0 / 74 / 162 / 14, all single-handed.

## Defects

| # | severity | defect |
|---|---|---|
| D1 | **Major (statement), repairable** | The header ("\(D\setminus\mathcal G\) is contained in a locally finite union of real algebraic curves"), Lemma 2(c) and "Gaps" are **false as stated**. See the argument below. The fix is to replace (G2) by the weaker (G2′); see Repairs. |
| D2 | Minor | The relation enumeration's completeness rests on a float bound, `floor(360/θ+1e-6)`, plus float partial-sum pruning. It is correct in practice, but it is not "exact" as the Gaps section claims. **Repair:** use the dummy-rational-angle bound, implemented in my checker, which needs no floats. |
| D3 | Minor (reproducibility) | "Cross-checked at two other points and by CP-SAT" (line 125; line 347 says "three points") is recorded in **no** script or certificate. The authors' script enumerates relations only at the first passing point. My runs supply the multi-point cross-check, but the CP-SAT claim is unverifiable and should be removed or archived. |
| D4 | Minor | Lemma 2(b) says the valuation rank is 3 "at all five points". This is true (reproduced), but the certificate stores the matrix only for \(J_0\). |

**D1 argument.** \(\rho_\chi=(J-C)/(J-B)\) (verified exactly) is a non-constant holomorphic
function of \(J\), so \(\chi=\arg\rho_\chi\) is a non-constant harmonic function. Its image
on any ball is therefore an open interval, so \(\{J:\chi/\pi\in\mathbb Q\}\subset D\setminus
\mathcal G\) is **dense** in \(D\). A locally finite union of curves is closed and nowhere
dense, so it cannot contain this set.

Explicit witness, checked exactly in AA: on \(s=1/2\), at \(t^*\approx0.6434805\), we have
\(\chi=108^\circ\) exactly and all tiles are strictly convex. Other witnesses:
\(\chi=108^\circ\) on \(s=9/20, 11/20, 2/5\), and \(\chi=120^\circ\) on \(s=11/20\).

This does **not** affect \(J_0\) or the other four listed points. It does mean that
"theorem for all \(J\in\mathcal G\)" is a statement about a dense, non-open, meagre set, and
that the "locally finite curves" conclusion is not justified for \(\mathcal G\) as defined.

No defect found in the mathematics of L1–L4 at the listed points.

## Counterexamples attempted (all failed)

* A 180° relation with mirrors, or with several copies of one corner: exhaustive exact
  enumeration found none.
* A vertex in the interiors of two edges, partial collinear overlap, or a corner plus an
  edge interior: all excluded by the half-disc argument above.
* Mixed-handedness stars: 134 of 162 stars are mixed, and all die by round 1 or 2.
* A handedness domain wall: impossible because no mixed star is viable.
* A flipped \(P_1\) pair with the c-edge K↔K (reflected partner): ray-incompatible at the
  vertex.
* A flipped \(P_1\) pair with K↔L, same handedness: killed one edge away, by both the hand
  argument and the pruning.
* Unsound pruning, such as killing a star because one completion fails: the rule tests
  existence over all live stars, so it is sound.
* A wrong far-corner direction for mirror tiles: re-derived independently, and the
  label-consistency assertion at the far end passes.

## Repairs needed

1. **Define (G2′).** Every non-negative integer relation \(\sum m_j\theta_j\in\{180^\circ,
   360^\circ\}\) among the 16 corner angles is identical, meaning its χ, ψ and κ coefficients
   are zero. Then:
   * set \(\mathcal G^*=\{\text{(G1)},\text{(G2′)}\}\supseteq\mathcal G\);
   * Lemmas 3–4 use exactly (G2′);
   * Lemma 2(c)'s argument (finitely many relations on compacts) shows that
     \(D\setminus\mathcal G^*\) is a locally finite union of algebraic curves;
   * restate the header, Lemma 2(c), the Theorem and "Gaps" for \(\mathcal G^*\), keeping
     (G2) as a sufficient condition certified at \(J_0\).

   Note that \(\mathcal G\subseteq\mathcal G^*\), so nothing already proved for points
   of \(\mathcal G\) (such as \(J_0\)) changes. Most points of \(\mathcal G^*\setminus
   \mathcal G\) are gained.
2. Replace the float multiplicity bound with the exact dummy-angle bound (D2).
3. Remove or archive the CP-SAT and multi-point cross-check claims (D3, D4).

## Remaining uncertainty

* My star and pruning code is independent, but it applies the **same mathematical model**
  as the authors' code: vertex star = cyclic word, plus a far-endpoint pair test. A modelling
  error shared by both would be common-mode. I attacked the model by hand (see L2 and L3) and
  found no gap.
* I trust Sage/PARI ideal arithmetic (`primes_above`, valuations) and QQbar/AA sign
  decisions.
* The lower bound "all 14 stars occur in genuine Ammann tilings" (patchcheck) is not
  reviewed. It is not needed for aperiodicity.
* Lemmas 5–6 and the final theorem assembly are not reviewed here.
* Behaviour on the exceptional curves is unknown and not claimed. For example, on
  \(\chi=108^\circ\), P1-F becomes 144° and P2-H becomes 72°.

## Verdicts

| claim | verdict |
|---|---|
| L1 (angle identities, all \(J\in D\)) | **VALID** |
| L2 (no 180-relation; no T-junctions; edge-to-edge) for \(J\in\mathcal G\), in particular \(J_0\) | **VALID** |
| L3 (74 relations, 162 stars, 14 survivors, single handedness), the counts at \(J_0\) and at the 4 other points | **VALID** (the "matching Ammann patches" sub-claim was not reviewed and is not load-bearing) |
| L4 (hand facts (i), flipped-\(P_1\) kill (ii)) | **VALID** |
| L5 ((G2) certificate rank 3 with primes 11/41/181/251/1031; (G1) exact) | **VALID** (also at the 4 other points) |
| Header and Lemma 2(c) "\(D\setminus\mathcal G\) ⊂ locally finite union of curves" | **INVALID** as stated (D1); repairable via (G2′) |
| "All proof-relevant decisions exact" (relation completeness) | **INVALID as worded** (D2): float bound; the result is correct, confirmed by an exact rational bound |
