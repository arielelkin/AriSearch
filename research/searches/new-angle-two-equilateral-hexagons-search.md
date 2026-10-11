# Exact symbolic two-equilateral-hexagon check

**Status:** Exact verifier passed; theorem fresh hostile review requested.

## Question and declared domain

This check supports the restricted theorem in
`research/lemmas/new-angle-two-equilateral-hexagons.md`. Both prototiles are
convex equilateral rational-angle hexagons. Arithmetic root classification
and the independently re-reviewed defect-free limit are proof dependencies,
not inferred from this search.

The finite search domains are exhaustive symbolic domains:

1. All 20 unordered triples with replacement from A+,A-,B+,B-. Angles are
   120 plus coefficients (1,0),(-1,0),(0,1),(0,-1) of parameters a,b>0.
   Solve the affine equation exactly for positive ratio b/a. No upper
   rational denominator bound is imposed. Ratios are exactly 1/2 and 2.
2. All 15 unordered triples containing the sporadic 168 category from
   H+,H-,S60,S108,S168. Their angles are affine pairs
   (120,1),(120,-1),(60,0),(108,0),(168,0). Solve for 0<a<60. Roots are
   exactly 12,24,36.
3. All 35 unordered triples from those same five named categories at each
   of the three exact parameter roots. Equal numerical angles remain distinct
   type categories. Every case misses a native S category.
4. All 10 triples from angles60,108,168, none sums to360.
5. A fixed nine-edge-pair gluing of three CCW six-sided faces. Each paired
   native endpoint is identified in reverse order by union-find. The check
   finds six three-corner classes, verifies each three-sector link, one
   corner from each face per class, common index parity, angle coefficient0,
   connected face graph, and Euler characteristic0.

There are no random seeds, numerical tolerances, solver packages, finite
patch searches, backtracking caps, timeout truncations or rational-angle
sweeps. Arithmetic uses Python integers and fractions.Fraction.

## Reproduction and retained output

From repository root:

    conda run --no-capture-output -n arisearch python3 research/searches/new-angle-two-equilateral-hexagons-verify.py

The JSON output is retained at
`research/certificates/new-angle-two-equilateral-hexagons-certificate.json`.
The successful run on 2026-10-09 used Python3.12.13,
Linux6.8.0-142-generic-x86_64, glibc2.41, conda environment arisearch.
The final captured subprocess exited with status0 in0.04855646099895239s.
The certificate records every affine row, all legal exceptional triples,
each endpoint pair, and all six flat vertex classes.

## Consequence and limits

Finite checks validate exact angular implications and the combinatorial flat
torus; the lemma supplies complete global proofs. The torus is not accepted
merely because it has formal legal stars: its endpoint identifications,
vertex links, orientability, topology and metric development are all stated.
The source/root-order classification is the previously checked primary
Lam--Leung theorem use, with no new literature-completeness claim.

The result closes only the rational-angle equilateral (6,6) family. It does
not classify arbitrary equilateral irrational-angle hexagons or any unequal-
side-length hexagons. No unrestricted impossibility or construction follows.

Exact retained file versions (SHA-256):

    279d5dc6881aceb593770ca6240cd90b5ff89200485d154a826d5f4aca5c9699  research/searches/new-angle-two-equilateral-hexagons-verify.py
    e67fca37fee36727fdcf0c0aa8e3530651d66188a1496784b7fdd02d332b299f  research/certificates/new-angle-two-equilateral-hexagons-certificate.json
