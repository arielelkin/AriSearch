# Cross-slot qq-chain pp-center periodic family

Status: **VALID after fresh independent positive-construction review.** This is a sufficient whole positive family on a new fixed eight-face quotient. It includes exact qq data outside the paired family; it does not alone classify all center-pp tilings.

## Exact whole family

Choose real parameters, in degrees,

    0<delta<30, 60+delta<chi<180, 60-delta<psi<180,
    exp(i delta)[exp(i psi)-exp(i(psi-chi))+exp(-i chi)]=-2p,
    p>0, q1.

A has native lengths(p,q,p,q,p,q) and directions

    (0,60+delta,120,180+delta,240,300+delta).

B has lengths(p,p,p,q,q,q) and directions

    (0,60,120,60+delta+psi,
     240+delta+psi-chi,420+delta-chi).

Its native angle list is

    (240+delta-chi,120,120,240-delta-psi,chi,psi).

**Theorem. Every pair in this exact domain admits a doubly periodic plane tiling.** Equal lengths are allowed for this positive theorem; the explicit fixture has p<1/2 and is binary with distinct lengths.

A closes by its threefold symmetry. B's p chain is2p exp(i60) and its q chain is exp(i60) times the left side of the defining relation, so it closes exactly. Its turns are

    60,60,psi+delta-60,180-chi,180-psi,chi-60-delta.

All are strictly between0 and180 on the stated domain and sum360. With positive side lengths and closure, ordered once-around directions give strict supports and strict convexity by the projection argument detailed in the same-slot center-family lemma. This is a direct whole-domain argument, independent of fixture continuity.

## Exact two-root parameterization

Given0<delta<30 and60+delta<chi<180, put

    D=cos(delta-chi)^2-2cos(chi)+1.

Retain both real quadratic candidates

    p=[-cos(delta-chi)+sqrt(D)]/2,
    p=[-cos(delta-chi)-sqrt(D)]/2

when D>=0. Keep exactly those with p>0 and reconstructed

    Z=[-2p exp(-i delta)-exp(-i chi)]/[1-exp(-i chi)]

having positive imaginary part and psi=arg(Z) in(60-delta,180). The denominator is nonzero because0<chi<180. The identity

    |-2p exp(-i delta)-exp(-i chi)|^2
       -|1-exp(-i chi)|^2
      =4p^2+4cos(delta-chi)p+2cos(chi)-1

shows|Z|1 on either root, so Z cannot vanish. Reconstructing exp(i psi)=Z yields exactly the original complex closure relation. Conversely every original-domain member solves this quadratic and occurs on one retained branch. Discriminant-zero coalescence is retained, no positive root is assumed automatically admissible, and there is no tangent or omitted denominator root.

## Actual eight-face carrier and whole-domain flat cover

The raw witness is stored in

    research/certificates/branching-hexagon-two-run-pp-center-cross-eight-face.json.

Faces0,1 are positive A;2,3 reflected A;4,5 positive B;6,7 reflected B. A reflected face uses old native corner(-i mod6) at displayed vertex i and old native side(5-i mod6) at displayed side i. This reverses boundary order while keeping each displayed face counterclockwise.

All48 native side occurrences are paired exactly once in the retained24 whole-side pairings, with equal actual lengths and reversed oriented boundary direction. The face graph is connected. The retained endpoint classes are16 actual three-corner circles: the endpoint adjacency graph has degree2 at every node and is connected on every class, so there is a single circular link in each class. After converting reflected corners back to native indices, each actual link is one of

    A_L+B0+chi=360;
    A_H+B3+psi=360;
    A_H+A_L+B1=360;
    A_H+A_L+B2=360.

All16 sums are symbolic identities in(delta,chi,psi). The reflection choices are material: B's cross-slot q3/q5 seams pair a positive B with a reflected B, avoiding a forbidden qq/qq endpoint match. Same-chirality A copies pair on their remaining q sides. This is an actual native gluing certificate, not an abstract star-frequency balance.

The quotient is connected and orientable, with F8,E24,V16 and Euler characteristic0. Strictly convex closed Euclidean faces, isometric reversed-side gluing and every actual circular link360 make it a complete flat torus. Its universal cover is isometric to the Euclidean plane. The deck group consists of a rank2 lattice of translations: any nontranslation orientation-preserving Euclidean isometry fixes a point, contradicting a free deck action, and compactness gives rank2. Lifted faces have disjoint interiors and cover the plane. This proves the whole periodic family, including all valid special parameter strata, without relying on a fixture or a symbolic period formula.

## Exact new binary fixture and developed lattice

Take delta15,chi90 and

    S=sin15, k=sqrt(1+S^2)>0,
    p=(k-S)/2,
    exp(i psi)=[-2p exp(-i15)+i]/(1+i).

The positive root satisfies0<p<1/2. Its unit Z has

    Re Z=1/2+p(S-cos15)>0,
    Im Z=1/2+p(S+cos15)>0,
    Im Z-Re Z=2p cos15>0.

Thus45<psi<90, satisfying psi>60-delta; chi90>60+delta75. Both qq angles are less120, so every homogeneous qq triple sums less360. The qq pair is not{90,150}. This exact fixture is in the remaining one-arc-center/no-qq-homogeneous family and has a periodic escape.

In Q(zeta24)[k], with zeta24=exp(i15), the p and q unit directions of B are

    (1,z^4,z^8,z^5 Z,z^11 Z,z^23).

Native angle units are(z^11,z^8,z^8,z^15/Z,i,Z). Reflection follows the exact old-index map above. The producer independently checks every new native edge and angle, exact closure,48 strict support inequalities for the two species, every actual edge equality, all16 single circular symbolic360 links and the connected oriented quotient. Direct isometry development verifies24 pure-translation seam holonomies. The full degree16 rational coordinate matrix has rank2; integral Hermite normal form gives the primitive period lattice, whose covolume equals the total area of4A+4B. Exact vertices, face placements, all holonomies, lattice basis and areas are retained.

## Search scope and preserved artifacts

The quotient was found after93 of the1024 two-copy lifts of a retained sparse native-seam primal and its reflected support. The separate four-face search exhausted648 endpoint-filtered matchings only in its precisely stated A+,A-,B+,B- domain. That failed finite search is never an exclusion of periodic or infinite tilings. The positive construction depends on the actual raw witness and geometry, not on the primal or search outcome alone.

Stable prefixes under searches/certificates are

    branching-hexagon-two-run-pp-center-cross-slot-balance;
    branching-hexagon-two-run-pp-center-cross-four-face;
    branching-hexagon-two-run-pp-center-cross-eight-face;
    branching-hexagon-two-run-pp-center-cross-periodic-family.

All producers replay read-only; writes require explicit`--output`. The balance record has96 oriented stars and33 signed seam keys, a rational primal with free species frequencies that returns1/2 each; no negative or global conclusion is asserted from that model. The eight-face raw certificate fixes the actual quotient. The final producer replaces its symbolic angle rows with exact new field geometry and retains the complete developed fixture. Independent review must reconstruct every native orientation, link, strict domain, quadratic branch, fixture embedding and flat cover without producer imports. Whole center necessity is a separate theorem and remains outside this positive statement.

Fresh complete positive-family review is [VALID](../reviews/branching-hexagon-two-run-pp-center-cross-periodic-family-review.md); its no-author-import checker passes both phase branches, all native geometry,16 actual circular links, exact fixture, primitive lattice and flat-cover proof.
