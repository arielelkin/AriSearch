# Root audit: single cross-palette hexagon interface

Date: 2026-10-13. Verdict: VALID within the explicit generic star language,
actual convex A012012, and exactly five distinct side classes(L,L,M,P,Q,V).
This is a root mathematical/code audit with a separate reconstruction,
not a claim of review by another person or agent.

The two seam endpoint bijections exhaust reflection freedom. Each required
third A corner fails equality of both exposed lengths. More strongly, the
colour1 arm cases L,L and P,Q each force the unmatched pair M,V, eliminating
all AAA stars. The disjoint native arm sets at each colour force equal B
arms at an AAB vertex. Their three palettes intersect only at L. A B cycle
with two copies of each colour either has an equal-colour adjacency (already
impossible against A), or contains two02 edges, which cannot match A's L
sides. Thus mixed fields are impossible for the full length stratum.
The pure-A case is impossible as well. Pure B in the reviewed defect-free
limit gives precisely the claimed monohedral periodic escape; the source
tiling is not claimed pure or periodic. The theorem uses the previously
reviewed limit and monohedral dependencies.

The separate checker imports no producer code. It reconstructs1728 triples
of twelve native A placements using actual honeycomb corner slots0,2,4 and
all three shared-side flags. It finds no AAA placement, reconstructs reflected
AAB arm pairs, and checks the02 obstruction on all90 labelled cyclic B words.
It uses Q(zeta720) instead of the producer's Q(zeta360), reconstructs all11
constant-family residues and all171875 sample assignments, and compares
complete retained closure sets. The family closure exclusion relies on a
positive common scale and a nonzero exact residue, not rational independence
of L,M,lambda. Nonconstant fixture exclusions remain sample-only.

For the surviving equilateral012012 B, fresh exact vertices pass closure
and all strict supports. All opposite-side translations reverse both
endpoints. Two generators satisfy the third-neighbour relation and their
positive determinant equals exact shoelace area. Together with the reviewed
central-hexagon translation theorem (or the single-cell SFT faithfulness
result), this verifies an infinite pure-B periodic covering. A finite cycle,
finite patch and mere angle/area ledger would not suffice on their own.

Replay:

    MISE_AUTO_INSTALL=0 mise exec -- conda run --no-capture-output -n arisearch python research/searches/two-hexagon-single-cross-palette-interface.py /tmp/single-cross-palette-replay.json
    MISE_AUTO_INSTALL=0 mise exec -- conda run --no-capture-output -n arisearch python research/reviews/verify_two_hexagon_single_cross_palette_independent.py /tmp/single-cross-palette-replay.json

Outcome: PASS. No larger search or timeout increase was needed. Other A
words, extra length equalities, additional angle stars and the unrestricted
hexagon problem remain outside this audit.
