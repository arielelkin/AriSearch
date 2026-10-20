# Adjacent AA, two-octagon carrier gate

Date: 2026-10-19. Scope: exactly four regular unit pentagons and two congruent octagons in an orientable translation quotient, with the stipulated saturated side coloring. No larger quotient or arbitrary patch search was used.

**Result.** AAABCABC has a periodic carrier for every 108° < α < 126°. AAABBACC has no carrier in this inventory. The latter is only a finite-inventory obstruction.

## Exact orientation reduction

Index octagon vertices and sides from 0, with side i going from vertex i to i+1. Starting the first side at angle 0°, the direction lists are

- AAABBACC: (0,36,72,252−α,432−2α,468−2α,396−α,324).
- AAABCABC: (0,36,72,252−α,180,216,396−α,324).

Sides 3 and 6 are QQ; all others have length one. Their direction difference is 144°, which rules out pairing the two sides of one Q to itself. Thus both QQ contacts join the two Q faces. Fix the first Q orientation. Enumerating the two bijections and the two chiralities gives: equal chirality can pair corresponding sides with a relative half-turn; opposite chirality can only use the swapped pairing, with relative rotation 648−2α modulo 360°.

Normalize every P so its AA-facing side is side 1, and its PP sides are 0 and 2. Each Q supplies two P orientations separated by 36°. At most one PP edge can join those two P faces: the other PP sides cannot pair to each other. Therefore a PP contact crosses between the two anchored P pairs. Because pentagon side turns are 72°, this requires the relative Q rotation to be a multiple of 36°. The opposite-chirality rotation lies strictly between 36° and 72° modulo 360°, so it is impossible. This includes both reflected placements, up to global reflection.

For AAABBACC in the remaining half-turn case, all P directions are multiples of 36°. Q side 4 has direction 432−2α and must face P. Hence α must be a multiple of 18°, with none strictly between 108° and126°. This rejects the complete AAABBACC gate before metric tests.

For AAABCABC all six public directions are constant. The companion Python enumeration checks all 8 QQ cases and 420 remaining PP pairings exactly using rational affine angle equations. Its four survivors are only PP-orientation survivors. The companion Sage program then exhausts the remaining PQ bijections and vertex stars for AAABCABC at α=117°: 1152 PQ bijections, one direction-compatible PQ assignment, two direction-compatible PP assignments, and exactly one correct-star contact map.

## Metric family and contact map

Put u(t)=exp(iπt/180), and let s=2 cos54°. The six public unit edge vectors sum to S=s u(18°). Set

    θ=252°−α,  φ=396°−α,
    x=s sin(φ−198°)/sin144°,
    y=s sin(198°−θ)/sin144°.

Take QQ side lengths x on side 3 and y on side 6. Then x u(θ)+y u(φ)=−S exactly. Both sine numerators are positive throughout the stated interval, so x,y>0. All exterior turns are positive and sum to360°; the closed polygon with these positive lengths is strictly convex. The Sage witness additionally verifies every vertex lies strictly to the left of every nonincident directed side, in the exact real algebraic embedding at α=117°.

Number darts 0–19 by five successive darts of P0,P1,P2,P3, and 20–27,28–35 by eight successive darts of Q0,Q1. The exact edge pairs are

    (0,7) (2,12) (5,15) (10,17)
    (1,20) (3,35) (4,25) (6,21) (8,24) (9,30)
    (11,28) (13,27) (14,33) (16,29) (18,32) (19,22)
    (23,31) (26,34).

Face rotations in degrees are (108,144,288,324,0,180). Every paired directed side is opposite, with equal length. The twelve vertex cycles, computed by successor-after-pairing, are

    (0,8,25) (1,21,7) (2,13,20) (3,28,12)
    (4,26,35) (5,16,30) (6,22,15) (9,31,24)
    (10,18,33) (11,29,17) (14,34,27) (19,23,32).

Every star is APP or PBC, with angle sum360°. The connected oriented quotient has F=6,E=18,V=12, hence genus one. These edge directions, pairings, and stars are independent of α; the only changing lengths are corresponding x/x and y/y QQ matches. Thus the same gluing is a nonsingular compact flat torus throughout the open interval. Its universal cover is the Euclidean plane, and its deck group is a rank-two translation lattice. Development is an isometry of the universal cover, establishing degree-one coverage and disjoint tile interiors, rather than merely an area coincidence.

## Independently inspectable exact witness

The Sage computation uses ζ40=exp(2πi/40) at α=117°. Its JSON stores all placed polygon coordinates, all edge shift coefficients, the vertex cycles, and a lattice basis. Every edge endpoint equality is checked exactly. The basis generates every contact shift with integer coefficients, and its determinant equals the sum of the six positive face areas up to sign. This separately certifies degree one for that explicit member. One exact correct-star map and one lattice certificate survive.

Reproduce with the repository tool wrapper:

    mise exec -- conda run --no-capture-output -n arisearch python research/searches/adjacent-aa-qdimer-carrier-sol-2026-10-19.py
    mise exec -- conda run --no-capture-output -n arisearch sage research/searches/adjacent-aa-qdimer-carrier-sol-2026-10-19.sage

Files: the .py/.json pair contains the finite angle screen; the .sage and -witness.json contain the exact metric contact-map certificate. No discovery log or Git operations were performed.
