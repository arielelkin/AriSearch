# Exact two-P, two-Q resonant periodic carrier

The derived minimal gate succeeds. Let H=1+2cos36°, and take Q side lengths, starting at its AA side, to be

(1,1,1,H sin36°/sin60°,H sin24°/sin60°,1,1).

Its angle word is (144,144,120,120,120,120,132) degrees. P is the unit regular pentagon. These shapes have an exact periodic tiling with two copies each per fundamental cell. This is an existence result for this metric, not a statement for all metrics of this angle word or all saturated tilings.

## Exhaustive quotient gate

Label P0 darts 0..4, P1 darts 5..9, Q0 darts 10..16, Q1 darts 17..23. A dart starts at the correspondingly indexed corner and follows the counterclockwise boundary. Normalize each P's AA-facing side to local side0. Then its PP sides are local1,4; the remaining PQ sides are local2,3. Each Q has PQ sides local0,1,6 and QQ sides local2,3,4,5. Fix Q0 chirality, and enumerate both Q1 chiralities. Regular P has no additional chirality choice.

The enumerator exhausts 15,120 pairings in each chirality case, permitting same-face side pairings. The angle-sum/three-corner vertex condition leaves two maps in each case. Direction consistency rejects both opposite-chirality maps. The two same-chirality maps are exchanged by relabelling Q0,Q1. This leaves the following representative edge involution:

(1,6), (4,9), (0,10), (2,23), (3,18), (5,17),
(7,16), (8,11), (12,15), (13,20), (14,21), (19,22).

Its vertex cycles, computed by alpha composed with predecessor, are

(0,9,11), (1,10,7), (2,6,17), (3,23,19),
(4,18,5), (8,16,12), (13,15,21), (14,20,22).

There are eight vertices, twelve edges, four faces, giving Euler characteristic zero. The face adjacency graph is connected. Every vertex has angle sum360°. Its orientable polygon gluing is therefore a flat torus.

## Exact geometry and every mate shift

Put z=exp(iπ/15), reducing rational expressions modulo Φ30(z)=z^8+z^7−z^5−z^4−z^3+z+1. The metric script works entirely in this exact field after selecting the lattice basis; floating evaluation selects an independent pair and all subsequent identities are exact.

The face rotations (P0,P1,Q0,Q1) are (0,180,180,0) degrees. Start each face's local vertex0 at zero, follow its prescribed headings and lengths, then translate faces by

T=(0, z^6+2, 1, z^6+1).

The lattice generators are

u=z^7−z^3−z^2−1,

v=z^7−7z^6/3−5z^5/3−5z^4/3−10z^3/3+4z^2/3+7z/3−1/3.

For each ordered pair (a,b) above, the translation applied to face(b) to mate its directed side against side(a) is m u+n v, with coefficient pairs in the same order:

(0,0), (1,0), (0,0), (0,0), (1,0), (0,0),
(0,0), (−1,0), (1,0), (0,1), (−1,1), (−1,0).

The reverse mate uses the negative shift. All endpoints match exactly and every edge vector is the negative of its mate. The script verifies closure and these identities by polynomial reduction.

All seven lengths are strictly positive by their displayed sine formulas. Every exterior turn is strictly between zero and180°, their sum is360°, and the polygon closes. The standard total-turn convexity criterion consequently proves strict convexity (and simplicity) of Q; P is regular and strictly convex.

The script also verifies the exact shoelace identity

area(P0)+area(P1)+area(Q0)+area(Q1)=det(u,v)>0.

In particular u,v are independent. The polygon gluing maps to R²/(Zu+Zv). Edge interiors and vertex neighborhoods map locally bijectively because paired sides are opposite and each corner cycle turns through exactly360°. Thus this is a covering of flat tori. The exact area identity makes its covering degree one. Its translates therefore tile the plane, with no interior overlap or uncovered regions. This verifies actual coverage rather than only boundary closure.

## Reproduction and scope

Run both scripts with the required environment wrapper:

    mise exec -- conda run --no-capture-output -n arisearch python research/searches/resonance-minimal-carrier-sol-2026-10-19.py
    mise exec -- conda run --no-capture-output -n arisearch python research/searches/resonance-minimal-carrier-sol-2026-10-19-metric.py

They produce the adjacent JSON certificates. The census is complete for the stated saturated, orientable 2P+2Q translational torus model. No larger quotient, arbitrary patch, discovery-log entry, or Git mutation was used. The construction alone does not establish periodicity for all positive metric realizations; it provides a specific exact periodic escape and an independently checkable carrier for this derived gate.
