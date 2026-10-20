# Last B orbit: bounded negative four-face carrier gate

Date: 2026-10-19. Exact finite enumeration and [independent Sol hostile review](../reviews/hexagon-five-four-last-b-four-face-negative-hostile-sol-2026-10-19.md) PASS: no carrier in the domain below.

Words are A=(0,1,2,0,3,4), B=(0,1,2,0,3,1). Corner i is the interior corner at the end of native side i. The required unsigned circular vertex links are each of

    (a0,a1,b2), (a2,b1,b5), (a3,b0,b4), (a4,a5,b3)

exactly twice. These are the four independent angle rows supplied for signed-star support [2,5,13,15,17,20,22,23]; their geometric value is 2pi. The gate does not infer these rows independently from that atlas.

## Complete declared domain

Faces 0,1 are labeled A copies and faces 2,3 are labeled B copies. Every native side is paired exactly once, exclusively with a side of the same color. Self face pairs and same type pairs are allowed. Every face may be ordinary or reflected; global reflection fixes face 0 positive without loss, leaving eight assignments. Thus this includes the narrower domain with both A faces ordinary. The oriented boundary gluing reverses endpoints in oriented face coordinates: in native coordinates this identifies opposite native endpoints for equal handedness and equal native endpoints for opposite handedness. There is exactly one such endpoint rule for each pair and handedness assignment.

Native color populations are 8,6,4,4,2. Their perfect matching counts are respectively 105,15,3,3,1. The Cartesian product has 14,175 complete pairings, and all eight handedness assignments give 113,400 candidates. This enumeration retains labeled duplicates and therefore does not rely on an isomorphism reduction.

For each candidate the checker constructs all native corner endpoint identifications exactly with a disjoint set calculation. It requires exactly eight classes, each of size three; their native angle multisets must be the four required rows each twice. It then requires connected face adjacency. None of the 113,400 candidates passes. A valid requested torus would necessarily pass these conditions, so their failure is a complete obstruction in this declared domain. No metric realization or development argument is needed for a negative result. The code also constructs corner adjacency; its use of corner equivalence classes gives a necessary test sufficient for this exhaustive negative conclusion even without a separate circular-link test.

## Replay

    mise exec -- conda run --no-capture-output -n arisearch python research/searches/hexagon-five-four-last-b-four-face-carrier-sol-2026-10-19.py

Output:

    EXHAUSTED: 113400 labeled pairing/handedness candidates; no requested four-face carrier

This contrasts with the positive four-face carriers for masks33416 and41032, which use B=(0,1,1,0,2,3) and different angle triples. Their side and corner incidences were not transferred. The new word and four supplied identities were enumerated directly.

Scope ends here: no larger torus search, no exclusion of larger periodic carriers, and no conclusion about plane tilability or aperiodicity.
