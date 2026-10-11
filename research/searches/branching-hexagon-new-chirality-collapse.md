# Computation record: fixed-B chirality collapse

Date 2026-10-10. Completion status: exact witness and all specified finite checks PASS. Independent hostile review pending.

Question: Does the alternating-length threefold A with B word (r,p,q,q,q,q) support two physically different same-A mate chiralities, and can those chiralities exclude periodic tilings? The exact fixture supports both whole-tile patches, but both branches force three qq angles whose sum gives B a periodic monohedral escape. The general theorem and conditional private-dimer transport restrictions are in [the proof](../lemmas/branching-hexagon-new-chirality-collapse.md).

Exact domain and representation: one explicit algebraic fixture, with coordinates in Q(g), g^4-10g^2+1=0 and 31/10<g<16/5. The native polygon edge lists are retained in the producer and vertices in the certificate. Transformations allow rotations, reflection S and translations. No symmetry reduction or solver is used; Sage's exact real embedding resolves signs.

Complete finite domains: both closed six-edge sums; each polygon's six supporting edges against every nonadjacent vertex; ten full contacts across two four-face patches; all twelve unordered whole-tile patch pairs; six monohedral reversed-edge pairings and all twelve corners forming four actual circular links; exact area/covolume equality; every ordered pair of two periodic motifs and every integer translation within the complete exact lattice-coordinate bounding-box ranges (sixteen comparisons excluding identity).

There is no random seed, timeout, enlarged periodic-search domain, numerical incidence decision or incomplete search. Replay uses Python 3.12.13, Sage10.9. The exact period translations and all finite comparisons are retained in [the certificate](../certificates/branching-hexagon-new-chirality-collapse.json).

Nondestructive replay:

    conda run --no-capture-output -n arisearch python research/searches/branching-hexagon-new-chirality-collapse.py

Explicit certificate production:

    conda run --no-capture-output -n arisearch python research/searches/branching-hexagon-new-chirality-collapse.py --output research/certificates/branching-hexagon-new-chirality-collapse.json

Expected summary: PASS: 12 whole-branch separations; 6 monohedral seams, 4 links, 16 complete lattice separations.

The general branch-collapse proof is geometric and does not depend on extrapolation from this fixture. The computation does not classify other B words, prove every-tiling periodicity, or establish a hierarchy from private dimers. The first remaining global obligation is explicitly recorded in the proof.
