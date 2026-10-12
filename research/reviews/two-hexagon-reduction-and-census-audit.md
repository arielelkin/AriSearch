# Audit: two-hexagon reduction and remaining census

Date: 2026-10-11.

## Verdict and repaired claim

The original proof of SFT Theorem 1(d) was invalid. A nonzero translation
replicates a defect only linearly in square radius, consistent with the
linear defect estimate. It does not prove that the original tiling is
edge-to-edge or trivalent.

The repaired claim is sufficient for the exact aperiodicity equivalence:
from any tiling invariant under a nonzero translation \(t\), construct
the reviewed defect-free limit by translating increasingly large clean
disks to the origin. Every approximant is still invariant under the same
\(t\). Tile-placement convergence preserves this fixed symmetry; the limit
is an admitted edge-to-edge trivalent tiling with period \(t\).
Honeycomb rigidity and an equivariant choice of polygon labels give a
nonzero period of the symbolic configuration.

The proof uses the existing defect-density, compactness, uniform vertex
separation, and honeycomb results. It does not assert that defects in the
original periodic tiling disappear. This distinction is now in the
[encoding lemma](../lemmas/two-hexagon-global-sft-encoding.md). A
[fresh independent rereview](two-hexagon-global-repaired-reduction-rereview.md)
finds the repaired converse, metric completeness and exact realisability
formula VALID, conditional on the reviewed structural dependencies. That
review excludes census/code correctness and the ancillary flux claims.

The same file now proves completeness using finitely many local metric
models, and supplies the actual existential polynomial formula for type
realisability. Angle-triple membership is encoded by the product of three
unit corner-angle complex numbers: each corner angle lies in \((0,\pi)\),
so product one means sum \(2\pi\). Positive side-length variables and strict
convexity inequalities tie those angles to genuine polygons. Exact side
equalities and inequalities are included. Negating all twelve cyclic or
reversed full-distance-matrix matches enforces two distinct congruence
classes. Linear angle-box feasibility alone would not establish this
joint geometric realisability.

The unrelated turning-flux corollary now explicitly assumes a doubly
periodic configuration. A single symbolic period need not make every row
periodic or give a finite fundamental domain. The SFT strip argument gives
existence of a possibly different doubly periodic point and suffices for
the reduction.

## Current low-rank data, checked independently

The stored enumeration has 11 rank-one, 504 rank-two, and 26,858 rank-three
flats. Only 6 rank-two and 310 rank-three flats cover all twelve corners.
All 27,373 flats, including noncovering parents, are now retained in
[the repository registry](../certificates/two-hexagon-global-angle-flats-rank3.json).
The 316 raw census logs and three summaries are retained in
[a compressed archive](../certificates/two-hexagon-global-covering-rank3-raw-logs.tar.gz).
The independent verifier defaults to these retained inputs.
The [independent registry script](verify_two_hexagon_low_rank_registry.py)
imports neither the enumerator nor census code. It checks all 27,373 stored
ranks, and the full 364-triple closure and symmetry-normalization of all
316 covering flats. It also independently computes the 100 partition
closures and confirms:

* all six rank-two covering classes are the no-mixed partitions;
* all 94 partition rank-three classes belong to the 310 covering classes;
* 216 rank-three covering classes are additional to the partition census.

The latest raw census is complete for these 316 stored covering classes:
all queries ended UNSAT, with no empty or candidate records. Every one of
the additional 216 classes obtained torus escape records; the 42 types
empty before any escape learning are partition-generated types.

The [aggregated certificate](../certificates/two-hexagon-global-covering-rank3-strata.json)
contains 695 torus records. The independent exact torus checker verified
all 695 with zero failures. The separate one-hot final-query verifier
finished all 316 queries INFEASIBLE, with zero other outcomes; its
[complete log](../certificates/two-hexagon-global-covering-rank3-verification.log)
is retained. These are solver checks without infeasibility proof logs.

The original temporary aggregator had a metadata defect: raw labelled
partition closures were compared with canonical flat closures. It falsely
matched only 58 of the 100 partition types. The new independent aggregation
canonicalizes both sides and matches all 100. The original torus records
and constraint queries are unaffected.

## Precisely what remains

The remaining angle-type census consists of every covering, rationally
closed exact triple set \(T\) of rank \(4,\ldots,10\), modulo
\(D_6\times D_6\) and species exchange. Rank is relative to the two hexagon
angle sums. Each exact type must be tested for every side-length
equivalence \(e\), except combinations already covered by inherited
escapes, empty-supertype certificates, or impossibility of actual polygon
realisability.

Proper specializations are counted by their full exact closure. They are
not a second independent bucket: rank-three specializations have been
treated, and all unhandled ones have rank at least four.

Existing torus records propagate upward in allowed triples and side
equalities. Emptiness propagates downward. The whole generic-type census
does not propagate upward because newly available triples can turn an
old empty SFT into a nonempty one with no already learned periodic escape.

Do not enumerate only descendants of the 316 covering low-rank types.
A minimal covering root could have higher rank. Continue from **all**
lower-rank flats, including noncovering parents, unless a separate
covering-root completeness theorem is proved.

There is no stored complete enumeration of the remaining higher-rank
types. The exact registry check verifies the stored data and subset
identities; it does not independently regenerate all low-rank symmetry
classes. Enumeration completeness, the repaired geometric proof,
constraint-encoding soundness, and solver infeasibility are separate
obligations. Fresh review of the repaired geometric proof is recorded
separately; the finite census still lacks formal infeasibility certificates
and an independent regeneration of the flat enumeration.

The two-hexagon case is unresolved.
