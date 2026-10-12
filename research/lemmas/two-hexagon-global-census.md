# Two convex hexagons: census of the generic angle strata

**Status:** computer-assisted. It rests on three things:

* exact torus certificates, independently re-checked;
* CP-SAT infeasibility verdicts, each obtained twice with two independent
  encodings;
* no DRAT/LRAT proof logs. The UNSAT verdicts are not formally certified.

The [independent reduction/census audit](../reviews/two-hexagon-reduction-and-census-audit.md)
and [fresh repaired-reduction rereview](../reviews/two-hexagon-global-repaired-reduction-rereview.md)
are complete within their stated scopes. Stored-data and final-query checks
are distinct from exhaustive regeneration of the flat enumeration. The original certificate
is a **restricted-class theorem** covering the 100 exact partition-generated
types. A later census has now completed all 316 stored covering types of
rank at most three; its checks and exact remaining scope are recorded in
Section 5. Neither result covers the higher-rank exact angle types.

**Dependencies:** [two-hexagon-global-sft-encoding.md](two-hexagon-global-sft-encoding.md)
(Corollary 1, Theorem 3 and its fixed-angle specialisation, conventions);
[hexagon-limit-and-periodicity.md](hexagon-limit-and-periodicity.md) via
that file.

## 1. Statement

Number the corners \(0..5\) (of \(A\)) and \(6..11\) (of \(B\)) as in the
encoding lemma. For a partition \(\Pi\) of the twelve corners into four
3-element blocks, let \(T(\Pi)\) be its *rational closure*: all 3-multisets
of corners whose angle-sum equation \(\sum=2\pi\) is a rational linear
consequence of

* the four block equations, and
* the two equations \(\sum_A=\sum_B=4\pi\).

Up to the 288 relabellings (\(D_6\) on each hexagon and swapping \(A,B\))
there are exactly 100 partition classes.

**Theorem C (generic partition strata).** Let \(A,B\) be convex hexagons
whose exact set of \(2\pi\)-triples equals \(T(\Pi)\) for some partition
\(\Pi\). Equivalently, the angle vector lies on the flat cut out by
\(\Pi\) and on none of the additional triple hyperplanes. This is the
meaning of “generic” here. Then \(\{A,B\}\) is not aperiodic. More precisely, for every
equivalence relation \(\sim\) on the twelve sides, realisable or not:

* **(C1)** For the 42 classes in which all four blocks contain corners of
  both hexagons, \(X(T(\Pi),\sim)\) has no legal patch of hex-radius 3. Such
  pairs do not tile.
* **(C2)** For each of the other 58 classes, either \(X(T(\Pi),\sim)\) has
  no legal radius-3 patch, or it contains one of the recorded tori (or a
  symmetry image of one). There are 101 escape records in total, made from
  24 distinct labelled tori. The period lattices have index 1 (15 records),
  2 (47), 4 (37) or 8 (2).

Of the 101 records, 93 are monohedral tori and 8 use both tiles.

In both cases Corollary 1 of the encoding lemma gives tiling-emptiness or a
periodic tiling.

Rank remark:

* The six classes with no mixed block, \((S_A,S_A^c,S_B,S_B^c)\), are
  exactly the covering flats of rank 2 (modulo the two \(4\pi\) sums). They
  are the most generic angle data compatible with both hexagons occurring.
  The enumeration found 504 rank-2 flats, of which exactly 6 cover all
  corners.
* The remaining 94 classes have rank 3.

**Why covering suffices.** If some corner of \(A\) lies in no triple of
\(T\), then \(A\) cannot occur in any configuration. Every tiling then uses
\(B\) alone, and the imported monohedral classification gives a periodic
tiling. So the only angle types that can carry an aperiodic pair are those
whose triples cover all 12 corners. The partition strata are the generic
members of this family.

## 2. Method and proof

For fixed \(T=T(\Pi)\), apply Theorem 3 of the encoding lemma with the
triple variables frozen to \(T\).

The query asks for an equivalence \(e\) on the sides and a legal radius-3
patch of \(X(T,e)\) avoiding every learned clause. The learned clauses are
of three kinds:

1. A torus clause \(\neg(E(x)\subseteq e)\) for each recorded torus \(x\),
   together with all its images under the stabiliser of \(T\). Here
   \(E(x)\) is the set of glued side pairs of \(x\). The clause is sound
   because \(x\) is legal in \(X(T,e)\) iff \(E(x)\subseteq e\). The census
   also adds weaker clauses \(\neg(F\subseteq e)\), with
   \(\mathrm{eqcl}(F)\supseteq E(x)\); these are implied by the torus
   clauses.
2. An empty clause \(e\not\subseteq\sim_0\), whenever \(X(T,\sim_0)\) has no
   legal radius-6 patch. This is sound by monotonicity. No such clause was
   needed.
3. A candidate clause, recorded for later treatment. None arose.

Each proposal is processed in turn. The script searches every period lattice
of index \(\le 8\) for a torus (CP-SAT), then tests a radius-6 patch. When
the query is infeasible for a class, every \(\sim\) admitting a radius-3
patch contains the image of some \(E(x)\), so \(X(T,\sim)\) contains a torus.
Every other \(\sim\) gives an empty SFT. Theorem C follows from Corollary 1.
\(\square\)

**Independence of the checks.**

* [two-hexagon-global-check.py](../searches/two-hexagon-global-check.py)
  re-implements the conventions from scratch. For all 101 records it
  recomputes the corner triples and glued side pairs from the labelling. It
  checks rational membership of every triple in \(T\) by its own exact
  elimination, and checks the side identifications against the recorded
  class assignment. Result: 101 checked, 0 failures.
* [two-hexagon-global-strata-verify.py](../searches/two-hexagon-global-strata-verify.py)
  reads only the certificate. It recomputes the stabilisers and re-encodes
  the final query differently: one-hot symbols, explicit side-identification
  clauses, single worker, fixed seed. Result: all 100 classes INFEASIBLE.
* A separate concrete run fixes exact rational generic angles for each
  class and uses the original SFT code with all twelve sides equal. Its
  patch-emptiness verdicts (radius 4) agree class by class with the 42
  classes of (C1).

## 3. Replay

```
conda run --no-capture-output -n arisearch python research/searches/two-hexagon-global-stratum.py partitions 3 6 8 OUTDIR 0 100
conda run --no-capture-output -n arisearch python research/searches/two-hexagon-global-check.py research/certificates/two-hexagon-global-partition-strata.json
conda run --no-capture-output -n arisearch python research/searches/two-hexagon-global-strata-verify.py research/certificates/two-hexagon-global-partition-strata.json 3
```

The additional independent partition reviewer now reconstructs its closure
input directly from the retained partitions rather than requiring the old
agent-specific `combin.json`. Its 2026-10-12 targeted replay checks all 101
original torus records, including stabilizer images, with zero failures:

    conda run --no-capture-output -n arisearch python research/reviews/verify_two_hexagon_global_strata.py tori

The census took 2641 s of solver wall time in total. Certificate:
[two-hexagon-global-partition-strata.json](../certificates/two-hexagon-global-partition-strata.json).
It records, per class, the partition, \(T\), the status, and every torus
(lattice \((n,s,m)\), meaning periods \((n,0)\) and \((s,m)\); labelling with
symbol index \(12q+6[s=-1]+r\); \(E\), \(F\) and the class vector).

## 4. Exact remaining registry

Rank means the rank of the corner-triple equations **modulo** the two
polygon angle-sum equations. For an exact triple set \(T\), form its affine
angle flat \(F_T\) using those equations. Its rank is
\(12-\dim F_T-2\), between zero and ten. The exact triple sets are
rationally closed: they include every triple equation implied on \(F_T\).
The twelve angles lie in the open box \((0,\pi)^{12}\). A point on
\(F_T\) has exact type \(T\) precisely when it avoids every triple
hyperplane not already in \(T\).

Noncovering types need no further aperiodicity census: a missing corner
prevents its entire species from occurring in an edge-to-edge trivalent
tiling. The nonempty SFT would then give a monohedral tiling, and the
imported unrestricted hexagon classification supplies a periodic escape.

After the rank-at-most-three census in Section 5, the remaining registry is
**every rationally closed covering exact triple set of rank
\(4,\dots,10\), modulo \(D_6\times D_6\) and exchange of the two tiles**.
For each such \(T\), one must handle every side-equality equivalence \(e\),
or decide joint polygon realisability to remove impossible \((T,e)\).
There is no current enumerated complete list of these higher-rank types.
The registry includes higher-rank types having no covering lower-rank
ancestor. Continuing a breadth-first flat enumeration must retain
**noncovering** parent flats too; extending only the 316 known covering
types has no proved completeness justification. The original all-flat
enumerator retains those noncovering parents.

“Non-generic points of partition flats” are not a separate extra bucket.
Taking a point with an additional triple replaces \(T\) by its larger full
closure and strictly increases the rank. A proper specialization of a
rank-two flat having rank three is covered by Section 5; all remaining
proper specializations appear once among the higher-rank exact types.

Learned periodic escapes do propagate upward: a torus using triples \(S\)
and side pairs \(F\) remains legal whenever
\(S\subseteq T\) and \(\operatorname{eqcl}(F)\subseteq e\).
Empty-type conclusions propagate downward, as
\(X(T,e)\subseteq X(T_0,e_0)\) when \(T\subseteq T_0,e\subseteq e_0\).
The full result for a generic type does **not** automatically propagate
upward: extra triples can revive a formerly empty SFT for length data
which supported no learned torus.

Angle-box feasibility is weaker than joint polygon realisability. In fact,
the all-\(120^\circ\) vector lies in every flat generated by corner-triple
equations and the two polygon sums, so the open angle box alone excludes
none of these flats. Exact generic points exist by avoidance of finitely
many additional proper hyperplanes, but that observation imposes no
side-length constraints. The explicit polynomial realisability formula in
the encoding lemma supplies the correct geometric test.

The unrestricted (6,6) statement remains open.

## 5. Status of the higher covering flats

The latest stored flat enumeration contains 11 rank-one flats, 504
rank-two flats, and 26,858 rank-three flats. Exactly 6 rank-two and 310
rank-three flats cover every corner.

The [complete low-rank flat registry](../certificates/two-hexagon-global-angle-flats-rank3.json)
is retained in the repository, including all noncovering parents needed
for complete higher-rank continuation. The
[raw census logs](../certificates/two-hexagon-global-covering-rank3-raw-logs.tar.gz)
are retained in a small compressed archive. The independent registry
verifier defaults to these repository inputs and reads archive members
without extracting paths. Replay no longer depends on temporary files.

The [independent exact registry check](../reviews/verify_two_hexagon_low_rank_registry.py)
recomputes all 27,373 stored ranks, exact closure and symmetry-normalization
of all 316 covering flats, and the closures of all 100 partitions. It
confirms:

* the six rank-two covering classes are exactly the no-mixed partitions;
* all 94 partition-generated rank-three classes occur among the 310
  rank-three covering classes;
* the additional rank-three classes number 216.

The census has completed **all 316 stored covering flats**, with a final
UNSAT query for each, zero empty records, zero candidate records, and
695 torus escape records in total. The
[aggregated certificate](../certificates/two-hexagon-global-covering-rank3-strata.json)
stores every record. Running the independent torus checker on it checks
all 695 records with zero failures. Final-query re-verification uses the
separate one-hot encoding of the original partition census; its output is
preserved in
[the verification log](../certificates/two-hexagon-global-covering-rank3-verification.log).
The completed log has all 316 queries INFEASIBLE and ends with
“non-INFEASIBLE: 0”. This is a second solver encoding, not a formally
checkable infeasibility proof.

The original flat enumeration script labels angle-feasible flats
“realisable”; here that word means only linear angle feasibility.
The registry checker does not independently regenerate every symmetry
class or certify completeness of the original flat enumeration. Its
complete stored-data checks, the solver verdicts, and the repaired
geometric reduction remain distinct verification obligations. The
solver verdicts have no proof logs. The linked audit and repaired-proof
rereview are complete; independent regeneration of the exhaustive flat
enumeration remains outstanding.

An aggregation defect was repaired in this certificate: partition closures
must be symmetry-normalized before matching them with flat closures.
Comparing the raw labelled closures had falsely matched only 58 of the
100 partition types. This affected classification metadata, not the torus
labellings or queries.

Replay:

    conda run --no-capture-output -n arisearch python research/reviews/verify_two_hexagon_low_rank_registry.py --check
    conda run --no-capture-output -n arisearch python research/searches/two-hexagon-global-check.py research/certificates/two-hexagon-global-covering-rank3-strata.json
    conda run --no-capture-output -n arisearch python research/searches/two-hexagon-global-strata-verify.py research/certificates/two-hexagon-global-covering-rank3-strata.json 3
