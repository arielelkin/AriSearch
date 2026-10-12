# Hostile re-review: repairs to `ammann-forcing-aperiodicity.md`

**Date:** 2026-10-11
**Reviewer:** independent hostile re-reviewer. I did not write the lemma or
either earlier review.
**Scope (narrow).** Only the repairs made after
[ammann-forcing-local-review.md](ammann-forcing-local-review.md) (D1–D4) and
[ammann-forcing-reconstruction-review.md](ammann-forcing-reconstruction-review.md)
(D1–D4), plus the new "Relation to the literature" section. The rest of the
proof was not re-reviewed. It was found valid by those reviews.

## Verdicts

| repair | verdict |
|---|---|
| Local D1: restatement on \(\mathcal G^*\), (G2′), Lemma 2(c) | **VALID** (one wording point, W1) |
| Local D2: exact dummy-angle enumeration | **VALID** |
| Local D3: CP-SAT claim removed; five-triple cross-check recorded | **VALID** |
| Local D4: all five valuation matrices stored | **VALID** |
| Reconstruction D1: twin roles (α)/(β), check R5 | **VALID** |
| Reconstruction D2: Lemma 7, R6 plus compactness | **VALID** (compactness is terse but correct; W2) |
| Reconstruction D3: overclaim deleted | **VALID** |
| Reconstruction D4: orientation rule in Lemma 5 | **VALID** |
| "Relation to the literature" | **VALID** (one framing point, W3) |
| **Repaired lemma overall** | **VALID on \(\mathcal G^*\)**. No blocking defect. W1–W3 are wording only. |

## Independent checker

`research/reviews/verify_ammann_forcing_repair_rereview.py` uses Sage with
exact arithmetic in \(\mathbb Q(\zeta_{10})\), AA signs and Fractions. It
imports no author code and runs in about 40 s:

```
conda run --no-capture-output -n arisearch python3 research/reviews/verify_ammann_forcing_repair_rereview.py
```

| part | what it checks | result |
|---|---|---|
| A1 | Identical relations, enumerated from the lemma's **printed** angle table. Uses four reviewer-chosen dummy triples, none from the certificate: (100,100,100), (130,110,70), (90,90,60), (109.1,150.65,151.7). Uses a different branching order. Compares with the certificate's relation set. | 0 / 74 for every triple. The set equals the certificate's set. |
| A2 | Exact rank of every stored matrix. Recomputes \(w_\chi,w_\psi,w_\kappa\) from the tile formulas of the reconstruction lemma, factors the ideals, and compares the columns and rational primes. | Rank 3 at all 5 points. Stored columns equal the recomputed ones, up to order. Prime lists equal the lemma's table. |
| A3 | The lemma's example relation P1-F + H6-B + P1-E | Linear form \(468-\chi\), so it is non-identical and equals 360 iff \(\chi=108\). |
| B1 | Orientation rule at \(J_0\). J lies inside the thin rhomb; K and L lie inside the thick one; J′, J″ and J2 lie outside. | The rule holds on all 8 marked edges. |
| B2 | Closure. Parents are found by **brute force** over all 40 big halves (both types, both chiralities, 10 rotations) and translations, not by inverse formulas. | 80 outward children and 200 cases: 40 (α), 160 (β), 0 neither. Every edge of R carries exactly one outward base. |
| B3 | Deflation legality, checked **directly**. Over every legal full-edge contact of two big halves (all rotations), every pair of children is interior-disjoint and every positive-length edge overlap is an equal full edge of compatible kind. For one half: the children's areas sum to the parent's, the children are contained in the parent, and they are pairwise legal. | 40 single halves, 200 contacts, 1340 child pairs, 0 failures. |

I also replayed both author scripts:

* `penrose-composition` reproduced the committed JSON exactly.
* `angles` was run twice, with `PYTHONHASHSEED=1` and `2`. See the reproducibility remark below.

## 1. Local D1: \(\mathcal G^*\), (G2′) and Lemma 2(c)

**Lemma 2(c), step by step.**

* *The product identity.* \(\rho/\bar\rho=e^{2i\arg\rho}\). So on \(Z_m\),
  \(\prod(\rho_j/\bar\rho_j)^{m_j}=e^{2iT}=1\) for \(T\in\{180^\circ,360^\circ\}\).
* *Reduction via Lemma 1.* Lemma 1 gives
  \(\rho_j=\lambda_j\omega^{c_j}\rho_\chi^{p_j}\rho_\psi^{q_j}\rho_\kappa^{r_j}\)
  with \(\lambda_j>0\). Hence the product equals
  \(\omega^{2\sum m_jc_j}w_\chi^{n_1}w_\psi^{n_2}w_\kappa^{n_3}\). Correct.
* *The product is not 1 at \(J_0\).* Suppose it were. Then
  \(w^{n}\) would be a root of unity, so \(n\cdot M=0\) for the valuation
  matrix \(M\). Rank 3 then forces \(n=0\), a contradiction. Correct.
* *The numerator is a nonzero polynomial.* \(N_m\) has coefficients in
  \(K\) as a polynomial in real \((s,t)\). Its real zero set is
  \(Z(\operatorname{Re}N_m)\cap Z(\operatorname{Im}N_m)\). One of these
  polynomials is nonzero at \(J_0\), so the set has dimension at most 1.
  Denominators are products of \(\rho\) and \(\bar\rho\), which are nonzero on
  \(D\). Correct.
* *The (G1) equalities.* These are differences of quadratics in \(s,t\) and
  are nonzero at \(J_0\). Correct.

**Finiteness near \(\partial D\) (the question asked).** The argument is
correct. Local finiteness is meant *in \(D\)*.

* Every \(J\in D\) has a compact neighbourhood \(C\subset D\), since \(D\) is
  open.
* On \(C\) the 16 angles are continuous and positive, so their minimum
  \(\varepsilon_C\) is positive.
* \(Z_m\cap C\neq\emptyset\) forces \(\sum m_j\le T/\varepsilon_C\), so only
  finitely many \(m\) are relevant.
* As \(J\to\partial D\) some angle tends to 0, and infinitely many curves
  \(Z_m\) may accumulate there. That is harmless, because \(\partial D\) is
  not in \(D\) and nothing is claimed there.

Each \(Z_m\) is closed in \(D\), since the angles are continuous. So
\(D\setminus\mathcal G^*\) is closed in \(D\), nowhere dense and null.
Therefore \(\mathcal G^*\) is open, dense and of full measure. **Valid.**

**W1 (wording, non-blocking).** The header, Lemma 2(c) and "Gaps" say that
\(D\setminus\mathcal G^*\) **is** a locally finite union of (closed) real
algebraic curves or sets. What is proved is weaker:

* each \(Z_m\) is a closed *semialgebraic* subset of \(\{N_m=0\}\cap D\);
* \(\{N_m=0\}\) also contains points where the same \(m\) sums to 180·k for
  other k, and such points can lie in \(\mathcal G^*\).

So the correct statement is "is closed and contained in a locally finite union
of real algebraic curves", or "is a locally finite union of closed
semialgebraic sets of dimension ≤ 1". The conclusions (open, dense, full
measure) are unaffected.

**Do later lemmas use only (G1) and (G2′)?** Yes. "(G2)" occurs only in the
definitions, in Lemma 2 and in the changelog.

* Lemma 3 (T-junction) needs only that a 180° corner relation is identical.
* Lemma 4 needs only that each star's 360° relation is identical, plus (G1)
  for edge labels.
* Lemma 5 uses Lemma 4 together with (G1). (G1) gives the asymmetry of the
  side cycles (a,b,b,r,r,a), (a,b,a,c,a) and (c,r,r,a,b), which I checked by
  hand: none has a rotation or reflection symmetry when a, b, r, c are
  distinct.
* Lemmas 6 and 7 do not depend on \(J\).

**Supporting check (exact).** The question in the literature section is
well-posed. On \(s=1/2\), at \(t^*\approx0.643480\), \(\chi=108^\circ\)
exactly. All three tiles are strictly convex there, and
\(a^2,b^2,r^2,c^2\) are pairwise distinct (exact AA). So there are points
that are allowable in Healey's length-only sense but lie outside
\(\mathcal G^*\).

## 2. Local D2: exact enumeration

**Why the dummy values give every identical relation.** Write the relation as
\(\sum m_j\ell_j\), where each \(\ell_j\) is an affine form in
\((\chi,\psi,\kappa)\) taken from Lemma 1.

* A relation is *identical* when \(\sum m_j\ell_j\equiv T\) as a form: the
  χ, ψ and κ coefficients are 0 and the constant is T.
* So it evaluates to exactly T at **any** substituted
  \((\chi',\psi',\kappa')\).

**Why the multiplicity bound is valid.**

* If every \(\theta'_j=\ell_j(\chi',\psi',\kappa')\) is positive, then each
  term satisfies \(m_j\theta'_j\le T\), which gives the bound.
* Every partial sum is at most T, so pruning by partial sums is sound.

Hence every identical relation lies in the searched box. This is
completeness. The final test
`acc == (T/36, 0, 0, 0)` keeps exactly the identical relations, which is
soundness. Float rounding only chooses the dummy values, and
`assert all(v > 0)` is exact. The dummy values need not be close to the true
angles; my (100,100,100) gives the same 0/74.

## 3. Local D3 and D4: the records exist and match the text

* `relation_enumeration_cross_check` holds the five dummy triples, all with
  `n180 = 0` and `n360 = 74`. The script asserts that the five sets are equal.
* Each entry of `points_tested[*]` stores
  `valuation_matrix_rows_chi_psi_kappa` (rank 3) and `valuation_primes`. The
  rational primes match the table in Lemma 2(b) at all five points. The
  earlier local review listed extra primes 2, 3 and 5; those come from norms
  of \(\rho\) and have zero valuation in \(w\), so this is not a discrepancy.
* No CP-SAT or "two/three points" claim remains in the lemma; I searched for
  it.

## 4. Reconstruction repairs

**D1, twin roles (Lemma 6).** The parent hypotheses of \(h^*\) are complete:
brute force finds exactly 2 parents for a red child and 3 for a blue child.

* *Case (α).* Suppose \(R'\ni h\) as a child and \(R'\) is valid. Then
  \(R'\neq R\), because \(h^*\notin R\). So \(h\) would have two valid
  parents, contradicting R3's uniqueness. Sound.
* *Case (β).* \(R'\) has the full edge \(e\) with the same mark.
* *Coverage.* Every edge of R carries exactly one outward child's base. This
  is needed for "every edge" and was implicit in the text; B2 confirms it.

My brute force over all 10 rotations gives 200 cases: 40 (α) and 160 (β).
This equals the authors' R5 count of 20/4/16 (one rotation) times 10, and the
first reviewer's 40/160. In all 40 (α) cases \(R'\) also overlaps R in
interior. **Valid.**

**D2, existence (Lemma 7).**

*Part (a).* The proof that legality passes to children is sound:

* children of one parent meet only inside that parent;
* children of different parents can meet in positive length only on a common
  parent edge E;
* R6(b), or my direct pairwise B3, covers every legal contact along E.

*Part (b), compactness, checked as written.*

* *Uncovered margin.* An unpaired half has its base on the outer boundary.
  Its apex is within height < 1 of that base: about 0.951 for the 36-72-72
  half and 0.588 for the 36-36-108 half. So "radius \(\varphi^nr_0-1\)" is
  right.
* *Finite local complexity.* Restrict to the rhombs meeting B(m). They lie in
  B(m+2), and their union is connected because each rhomb meets the connected
  disc that they cover. So their edge graph is connected and has boundedly
  many edges, by an area bound. Each vertex is then a bounded sum of unit
  vectors \(\omega^k\), so finitely many configurations occur.
* *Extraction.* Diagonal extraction gives nested restrictions. Their union
  covers the plane, has disjoint interiors and is legal pairwise.

**Valid.**

**W2 (wording).** "the edge graph inside a disc of radius m+4 is connected"
should read "the edge graph of the rhombs meeting B(m) (contained in B(m+2))
is connected". "Configurations inside the disc" should mean the rhombs
*meeting* B(m). The Gaps section already flags this step as written out but
not formalised. That is accurate.

**D3, overclaim.** The overclaim has been deleted. The P3 identification is
now a remark marked "(not used)", citing the reviewer's 2-SAT evidence. Lemma
6 states that it needs no identification. **Valid.**

**D4, orientation rule (Lemma 5).** By hand, with ccw rhombs ABCD and EFGH:

* *X edges, quad on the left:*
  * A→B and E→F: the interior is on the left, and these are quad edges;
  * C→B and E→H: the interior is on the right, and the triangle is inside.
* *Y edges, quad on the right:*
  * A→D and H→G: the interior is on the right, and these are quad edges;
  * C→D and F→G: the interior is on the left, and the triangle is inside.

B1 confirms this exactly at \(J_0\). It holds for all \(J\in D\), because the
quad/triangle side of each rhomb edge is combinatorial. Two rhombs with equal
mark on a shared edge lie on opposite sides of the arrow, so exactly one
supplies the quad. **Valid.**

## 5. Relation to the literature

Each requirement is met:

* **Framing.** The title and Status present the result as an "independent
  exact verification and strengthening" of Healey, *RHUMJ* 12(2) (2011), Thm
  4.5 and Cor. 4.7. The Status says "not a discovery".
* **Healey's hypotheses.** They are stated as reported:
  * complete-edge convention (p. 97);
  * length-only allowability;
  * Prop. 4.3 treated as exhaustive;
  * reflections not discussed.
* **Ammann–Grünbaum–Shephard**, *DCG* 8 (1992) 1–25, is cited.
* **No novelty claim.** The words "first", "novel" and "discovery" occur only
  in the disclaimer and the changelog. "No prior proof located" is gone.
* **The question.** The exceptional-curve question is posed explicitly as "A
  question, not a claim": "We have not determined whether…". My exact check
  in §1 shows the question is non-vacuous.

**W3 (framing, non-blocking).** The "strengthening" is in conventions:
arbitrary contacts and reflections. The parameter range is **narrower** than
Healey's: \(\mathcal G^*\) is a proper subset of the allowable set. "Gaps"
says this ("(G1) alone is not shown to suffice"), and item 4 implies it. One
sentence in the literature section itself would prevent misreading, for
example: "On allowable J outside \(\mathcal G^*\), Healey's claim is not
re-derived here." Also, "Whether other exceptional J admit … is open" in Gaps
would read better as "is not determined here". As written, it could be read as
a claim about the state of the literature.

## Reproducibility remark (confirmed, with a correction)

The root's observation is confirmed in part. Three runs of
`ammann-forcing-angles.py` were compared: hash seeds 1 and 2, and the
committed certificate. All three agree on:

* the relations, the 162 stars, the 14 viable stars, the killed sets (142, 6);
* every other certificate field.

They differ only in **list order**:

* stars within 10 of the relation entries are listed in a different order;
* the pruning-round records are ordered differently. Compared by position,
  only 27 of 142 and 4 of 6 records coincide.

The cause is iteration over `set(itertools.permutations(...))` under Python
hash randomisation.

The witness pair recorded **for a given star** is identical in all three runs.
Keyed by the canonical star, there are 0 of 148 differences. This is expected,
because stars are stored in canonical (minimal) form and the first failing
pair is then deterministic. So the run-to-run differences are in which record
appears at which position, not in the witnesses themselves.

**Recommendation:** sort the star lists and kill records, or pin
`PYTHONHASHSEED`, so that the certificate is byte-reproducible. This does not
affect correctness.

## Remaining uncertainty

* Healey's paper was not consulted. The literature section's account of its
  hypotheses ("as reported to us") is taken as given.
* The B2 and B3 checks use the half labels and deflation formulas stated in the
  composition script's docstring. The marks are derived independently from the
  lemma's rhomb arrows, and their consistency with the half labels is asserted.
  A wrong labelling would have made B3 fail.
* I trust Sage, PARI and AA for exact ideal factorisation and signs.
