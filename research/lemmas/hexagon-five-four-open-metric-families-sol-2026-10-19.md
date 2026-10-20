# Two remaining supports contain open seven-dimensional metric families

Date:2026-10-19. Status: proved with exact replay and [independent Sol hostile review](../reviews/hexagon-five-four-open-metric-families-hostile-sol-2026-10-19.md) PASS. This is separate from the universal mask41032 periodicity theorem.

## Statement

For each mask33416 and41032, its affine native-angle support F has dimension7. There is a nonempty relatively open subset U of F such that every angle assignment in U determines closed strictly convex A,B with five distinct positive common lengths, normalized l0=1. The resulting normalized metric family is a graph over U and has dimension7. In particular nonequangular closure does not collapse these supports to a lower-dimensional angle resonance locus.

## Exact base point and determinant

Use interior angles in degrees

    A=(90,150,90,120,150,120),
    B=(150,120,120,90,150,90)

and lengths, with r=sqrt(3)>0,

    (l0,l1,l2,l3,l4)=(1,4-2r,-4+3r,2-r,-6+4r).

The replay script checks positive distinct lengths, both polygon vector closures, total turn360 degrees, and all strict supporting halfplanes algebraically in Q(r). It also checks both support equations and augmented rank5 independently. Angle index i is the end of native side i.

For arbitrary angles with each polygon total4pi, start each side0 in direction(1,0). Successive directions are obtained by adding exterior turns pi-alpha_i. Closure is the four-row linear system M(alpha)l=0. At the displayed point its matrix is

    [1-r/2, 0,   -1/2, 0,  1/2]
    [-1/2,  1,    r/2,-1, -r/2]
    [1-r/2, r/2, -1/2, 0,  0  ]
    [1/2,   3/2, -r/2,-1,  0  ].

The determinant after deleting column0 is exactly -1/4, nonzero.

## Analytic proof of open metric feasibility

The matrix entries are real analytic trigonometric functions of the native angles. Its final four columns remain invertible throughout a neighborhood of the base point. With l0=1, define explicitly

    (l1,l2,l3,l4)^T = -M(alpha)[:,1:]^(-1) M(alpha)[:,0].

This is analytic and enforces both exact polygon closure vectors at every angle in the neighborhood. Restrict the angles to either affine support F. Both native polygon angle totals remain4pi, so each constructed direction sequence has total turn2pi. Strict positivity, pairwise distinctness of lengths, and each of the finitely many strict supporting halfplane determinants hold at the base point and are continuous. Shrinking the neighborhood preserves them all. The supporting halfplanes certify simplicity and strict convexity; no mere angle criterion substitutes for them. Thus the asserted U exists. Its dimension is7 since F has dimension7 and U is relatively open. The graph retains its full angle coordinates and therefore cannot have smaller dimension.

This proof uses an exact invertible linear solve and continuity, rather than an unverified numerical Jacobian or nonlinear solver. Scale and independent polygon placements have been removed by l0=1 and the two independent side0 direction choices.

## What generic angles do establish

Each F contains the equiangular point e=(2pi/3,...,2pi/3). For a nonempty finite multiset n of corners, the relation n dot alpha=pi cannot be an identity on F: evaluation at e would require2 sum(n)=3. Similarly n dot alpha=2pi can be an identity only when sum(n)=3. The replay exhausts the364 unordered corner triples with repetition. The only identities are, in native corner indices0..5 for A and6..11 for B:

    33416: (0,6,7), (1,8,9), (2,3,10), (4,5,11).
    41032: (0,6,7), (1,2,8), (3,9,10), (4,5,11).

Shrink U so every angle exceeds pi/3, possible because the displayed base point has minimum pi/2. Any multiset with sum2pi then has at most5 members, and any multiset with sum pi has at most2. Therefore only finitely many candidate local angle relations need be considered throughout this U. Every nonidentity relation cuts out a proper affine hyperplane in F. Their finite union cannot cover the relatively open U. The complement is open and dense in U, excludes all pi-sum multisets, and has exactly the listed four2pi corner multisets. This is a genuine generic statement for realizable metrics, not merely formal angles.

For an edge-to-edge tiling of a generic pair, every vertex must therefore be one of those four unsigned triples. A periodic mixed torus carrier using only these four triples would have the same number N of A and B faces and N occurrences of each triple, by counting the incidence of each native corner. These necessary counts are consistent: V=4N,E=6N,F=2N gives Euler characteristic0. Thus angle genericity alone does not obstruct periodic topology.

For41032 the companion theorem supplies just such a four-face torus, with N=2, for EVERY feasible metric. Hence generic metrics on41032 certainly do not exclude periodic tilings. This generic-angle gate alone neither established nor excluded a torus carrier using only the four33416 identities; the [subsequent universal carrier theorem](hexagon-five-four-mask33416-universal-periodicity-sol-2026-10-19.md) supplies one.

## Precise generic-periodicity boundary

A fixed finite edge-to-edge torus carrier containing a vertex angle equation not identical on F is excluded by the generic choices above. This excludes all such carriers simultaneously because the candidate local equations on U are finite, even though the number of possible carriers is unbounded. A carrier whose every vertex uses one of the four identity triples survives this entire angle argument. Equal edge lengths and flat development make any valid closed oriented torus carrier of that kind periodic for every feasible metric; it cannot be excluded by choosing generic lengths within this family. The subsequent33416 carrier construction shows this generic-angle exclusion cannot produce a candidate in either support.

Even exclusion of every periodic carrier would establish only absence of periodic tilings. It would not establish existence of any plane tiling. Conversely the open metric theorem establishes only feasible polygon pairs. It does not establish that any of their retained stars or finite coronas occur geometrically, let alone extend to a plane tiling. These three gates remain separate.

## Evidence and replay

    mise exec -- conda run --no-capture-output -n arisearch python research/searches/hexagon-five-four-open-metric-gate-sol-2026-10-19.py

Certificate: `research/certificates/hexagon-five-four-open-metric-gate-sol-2026-10-19.json`. Exact arithmetic uses SageMath Q(sqrt(3)) and QQ. Finite domains: one specified fixture, two specified support rowspaces,364 unordered triples, and one literal12-pair carrier. No randomized seeds, solver timeouts, or expanded collar searches are involved. Replay completed and passed. The unsigned identity enumeration does not classify signed local vertex geometry or global tiling extension.
