# Exact AA/BB strand seam atlas, 2026-10-19

Status: fixed immediate geometry gate; no plane existence or aperiodicity claim. Independent hostile review remains required for substantive claims. Implements Priority 1 of the 19:22 Astra assessment; no quotient, longer strand word, or corona search is used.

The Sage source reconstructs each isolated metric over K=Q(z), z=exp(2 pi i/180), with its distinguished complex embedding. The JSON contains every Q vertex, QQ length, rigid-motion matrix and translation, and all endpoint pentagon vertices, as exact polynomials in z. This finite data specifies the embedding and arithmetic without reliance on the previous approximate metric certificate.

## Complete fixed domain

For each root seam e in {1,3,5}, every neighbor seam f in {1,3,5} and both orientation parities is considered. Opposite interiors require reversed endpoints for orientation-preserving maps and equal endpoint ordering for orientation-reversing maps. Reject unequal lengths and endpoint angle sums other than 252. This enumerates every whole-edge native isometry: an ordered endpoint correspondence and parity uniquely determine a plane isometry. For equal AA/BB endpoints both parities survive; a mixed AB seam has only the orientation-preserving correspondence (AB includes BA).

Write a=Q_e, b=Q_(e+1), u=Q_j, v=Q_k, where j,k are the mapped neighbor endpoints. For parity r=0, c=(b-a)/(v-u), t=a-cu, F(x)=cx+t. For r=1, c=(b-a)/(conj(v)-conj(u)), t=a-c conj(u), F(x)=c conj(x)+t. For c=A+iB the real matrices are [[A,-B],[B,A]] and [[A,B],[B,-A]], respectively. The retained tables give their exact entries.

A regular P on an exterior unit edge [a,b] has vertices b+(a-b)p_j, where p_0=0 and p_(j+1)-p_j=z^(36j). It is unique as a geometric polygon even with reflections. Thus its placement is forced by the Q side. At each seam endpoint the pentagon forced from the root Q and from the other Q must coincide as a complete vertex set; the script asserts both coincidences. It also checks that the two P at Q144 share exactly two vertices.

The strict-interior separating-axis test checks every pair in each fixed neighborhood. Exact coincident pentagons are first identified as one tile; any other coincident polygons intersect. For two convex polygons, their interiors are disjoint exactly when an edge supporting line of either polygon separates their open interiors. Cross products live in K. Zero is decided in K; nonzero real signs use outward interval evaluation of the specified root with precision doubling. No floating-point tolerance is used.

A seam neighborhood includes both Q tiles and all four P neighbors of each. The strand neighborhood includes the root Q, its AA neighbor, its BB neighbor and all their forced P neighbors. These are fixed tests, with no growth depth parameter.

## Outcome and missing global lemma

Each metric has five directed seam entries: two AA-to-BB, two BB-to-AA, and one mixed-to-mixed. All five seam neighborhoods and all four incoming/outgoing AA/BB combinations survive. The four P around an isolated Q are interior disjoint, including their required PP edge at Q144. In particular the reflection choice is not intrinsically forced by these immediate tests.

For each of the four metrics the unreflected forward step has order five (its fifth power has zero translation), while the reflected forward step squared has nonzero translation. The JSON additionally composes the two forward strand isometries formally: an orientation-preserving step has finite rotation order; a reflected step squared is the exact translation t+c conj(t). These are compositions in the Euclidean group, without an assertion that the resulting repeated placements form an embedded strand. Finite rotation order neither bounds strand length nor proves return, and a nonzero drift is compatible with an unbounded embedded strand. No monotone obstruction, completely determined transverse ribbon, or return constraint has been established.

**Blocked under protocol §5.** The missing lemma is an unbounded restriction on sequences of the two allowed AA/BB seam parities which either excludes every plane extension or forces a geometrically repeatable ribbon with proved transverse completion. The immediate atlas does not supply that restriction. Plane existence for each of the four exact pairs and periodic escape versus universal nonperiodicity remain unresolved. The ratio P:Q=1:1 and PP edge density Q/2 on a torus remain necessary balances, with no extension implication. Stop this route absent a materially new invariant or construction; do not authorize a 4Q or larger carrier from the degree-two graph alone.

Replay:

    mise exec -- conda run --no-capture-output -n arisearch sage research/searches/aa-bb-strand-atlas-sol-2026-10-19.sage

Retained certificate: neighboring JSON. Deterministic fixed finite domain, no solver, seed or timeout. No novelty claim.
