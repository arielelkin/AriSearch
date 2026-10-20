# Hostile Sol review: last-B four-face negative gate

Date: 2026-10-19. Verdict: **PASS**, within the explicitly bounded domain.

Reviewed lemma: `research/lemmas/hexagon-five-four-last-b-four-face-negative-sol-2026-10-19.md`.
Exact producer: `research/searches/hexagon-five-four-last-b-four-face-carrier-sol-2026-10-19.py`.
This is an independent Sol review, not an Astra review. The author artifact was not edited.

## Enumeration and completeness

The two labeled A copies and two labeled B copies have color populations 8,6,4,4,2. Pairing a population of size 2k gives (2k-1)!! matchings. The producer's recursive first-element pairing visits each matching exactly once, so its factors 105,15,3,3,1 give 14,175 pairings. All native sides, including same-face and same-type pairs, participate without restriction beyond equal color.

Each face independently has two handedness choices. Simultaneous reversal changes neither the native endpoint equivalence relation nor unsigned angle rows. Fixing face 0 positive therefore retains a representative of all possibilities and leaves eight choices. No rotation or copy symmetry reduction is used. All 113,400 labeled candidates are covered.

For a native side i, its start and end corners are i-1 and i. Equal handedness requires opposite native endpoint identifications; different handedness requires equal native endpoint identifications. The producer implements exactly these rules, including self-face pairings. Its union-find is correct despite omitting rank and path compression. Angle conversion `6*(x//12)+x%6` maps the two A copies to a0..a5 and the two B copies to b0..b5. Its target integer triples match all four declared rows, and its multiplicity check demands each twice.

## Independent reconstruction and replay

I ran the exact producer through the prescribed environment wrapper:

    mise exec -- conda run --no-capture-output -n arisearch python research/searches/hexagon-five-four-last-b-four-face-carrier-sol-2026-10-19.py

It exited successfully with:

    EXHAUSTED: 113400 labeled pairing/handedness candidates; no requested four-face carrier

I also independently enumerated all matchings in an inline Python program through the same wrapper, using vertex cycles of a permutation instead of union-find. If tau exchanges paired oriented side darts, the vertex permutation is `previous_on_oriented_face(tau(d))`. For native dart i on face f, previous is i-h[f] modulo 6; its oriented end angle is native i for positive handedness and i-1 for negative handedness. This reconstructs actual circular links and handles reflections and self-pairs directly.

Independent output:

    matching factors [105, 15, 3, 3, 1]
    total 113400 counts {'eight_trivalent': 8}

Thus eight candidates have exactly eight length-three vertex cycles, and zero have the prescribed angle-row multiset, even before a connectedness filter. The independent permutation calculation agrees with the negative producer result.

## Link and scope audit

The producer constructs but does not separately inspect its corner adjacency lists. This is not a gap in a negative result: every requested circular trivalent link necessarily produces a size-three corner equivalence class with the prescribed angle multiset. Failure of that necessary condition excludes the requested carrier. Independently checking the full vertex-cycle permutation corroborates this point. Its face-connectivity closure is also sufficient, though no target-row candidate reaches that check.

The result assumes the supplied four angle identities; it does not establish their derivation from the signed-star atlas. It excludes only complete equal-color side pairings of exactly two A and two B hexagons under orientable endpoint reversal. Larger carriers, other angle rows, nonorientable gluings, partial-side subdivisions, metric realizations outside this combinatorial domain, plane tilability, and aperiodicity are not decided. A connected orientable requested carrier would have V=8,E=12,F=4 and Euler characteristic zero, consistent with the intended torus scope.
