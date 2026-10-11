# A broader pp-center periodic family on the indexed four-face carrier

Status: **VALID after fresh independent positive-construction review.** This is a complete positive family for a fixed four-face quotient, not a classification of every pp-center pair. It includes actual qq angles outside120±2delta. No periodicity is inferred from local angle balance or continuation of a single fixture.

## Full exact family

Angles are in degrees. Choose real parameters satisfying

    0<delta<30, 60-delta<chi<180, 60+delta<psi<180,
    Im[exp(i delta)(exp(i chi)-1+exp(-i psi))]=0,
    p=-Re[exp(i delta)(exp(i chi)-1+exp(-i psi))]/2>0.

Set q1. A has lengths(p,q,p,q,p,q) and directions

    (0,60+delta,120,180+delta,240,300+delta).

B has lengths(p,p,p,q,q,q) and directions

    (0,60,120,60+delta+chi,240+delta,420+delta-psi).

Its native angles are

    (240+delta-psi,120,120,240-delta-chi,chi,psi).

**Theorem. Every pair in this exact domain admits a doubly periodic plane tiling.** Equal lengths p1 are allowed in this positive construction; distinct lengths hold in the new explicit fixture below. There is no negative assertion outside the domain.

A closes by threefold symmetry. B's p chain is2p exp(i60), while its q chain is

    exp(i60) exp(i delta)(exp(i chi)-1+exp(-i psi)).

The domain therefore gives exact closure. Every side is positive. B's six turns are

    60,60,chi+delta-60,180-chi,180-psi,psi-60-delta.

They are strictly between0 and180 by the stated bounds and sum360. Thus its edge directions increase once around the circle; the same holds for A. Closure and ordered strict turns give a strictly convex polygon: the projection of successive edges on the interior normal of any selected side has its positive entries followed by its negative entries and sums0, with partial sums strictly positive at other vertices. Therefore every nonadjacent vertex lies strictly on the interior side of that side's line. The full domain has strict convexity directly; no sample-continuity argument is used.

The defining metric equation is a real phase condition. Below is an explicit quadratic parametrization preserving both roots, so the implicit domain hides no denominator or branch omission.

## Exact indexed four-face quotient, unchanged pairings with new geometry

Use only species, mirror bits, native labels, side pairs and endpoint classes from

    research/certificates/branching-hexagon-new-two-run-four-face-periodic.json.

Its old numeric native angle metadata is not used for this new family. The new faces are0,1 copies of A and2,3 copies of B, all in positive native orientation. The12 oppositely oriented whole-side pairings are

    (0,0)-(2,0); (1,0)-(3,0);
    (0,1)-(3,4); (1,1)-(2,4);
    (0,2)-(2,2); (1,2)-(3,2);
    (0,4)-(3,1); (1,4)-(2,1);
    (0,3)-(1,3); (0,5)-(1,5);
    (2,3)-(3,3); (2,5)-(3,5).

Every one of24 native side occurrences is used exactly once and shares its actual length. The face adjacency graph is connected. The actual endpoint-identification components are the following eight classes:

    (0,1),(2,0),(3,5);
    (0,2),(2,3),(3,4);
    (0,4),(1,3),(3,2);
    (0,5),(1,0),(3,1);
    (1,1),(2,5),(3,0);
    (1,2),(2,4),(3,3);
    (0,3),(1,4),(2,2);
    (0,0),(1,5),(2,1).

At each class the side-pair endpoint graph is connected and every node has degree2. It is therefore a single circular three-corner link, not several angle cycles accidentally collapsed into one class. The new native angle sums are, twice each,

    A_L+B0+psi = (120-delta)+(240+delta-psi)+psi=360;
    A_H+B3+chi = (120+delta)+(240-delta-chi)+chi=360;
    A_H+A_L+B1=360;
    A_H+A_L+B2=360.

All eight sums are identically360 in the three raw variables(delta,chi,psi). They impose neither chi+psi240 nor the paired qq values. Extra legal star types at special parameters do not damage this fixed construction.

The quotient is connected, orientable, compact and has F4,E12,V8, hence Euler characteristic0 and torus topology. Each face interior is Euclidean, each paired side has an isometric Euclidean neighborhood, and each actual circular vertex link totals360. It is a complete flat Euclidean torus. Its universal cover develops isometrically onto the Euclidean plane. The deck group acts freely, so its orientation-preserving Euclidean isometries are translations; compactness supplies a rank2 lattice. Lifted polygon interiors are disjoint and cover the plane, giving the claimed doubly periodic tiling for every stipulated parameter. This proves the whole family independently of a formula for its periods.

## Explicit quadratic parameterization, including both branches

Let

    K=cos(delta)-cos(delta+chi),
    D=K^2-1+2cos(chi).

Choose0<delta<30 and60-delta<chi<180. Retain **both** candidates

    p=(K+sqrt(D))/2, p=(K-sqrt(D))/2

when D>=0. Keep precisely candidates with p>0 for which

    Z=1-exp(i chi)-2p exp(-i delta)

has negative imaginary part and psi=-arg(Z) lies in(60+delta,180). Then use that psi in the displayed family. If D0 the roots coalesce and the single value is retained; no hypothesis of distinct roots is required.

Indeed

    |Z|^2-1=4p^2-4Kp+1-2cos(chi).

The quadratic makes|Z|1, so Z never vanishes. The branch condition selects its unique principal phase(-180,0) and enforces the strict native-angle bound on psi. Rearranging Z=exp(-i psi) gives

    exp(i delta)(exp(i chi)-1+exp(-i psi))=-2p.

Conversely every member of the original domain has this reconstruction and solves that quadratic, so it appears in one of the two retained branches. There is no tangent division, principal-phase ambiguity, zero-unit root or omitted discriminant-zero case. This is an algebraic/trigonometric parametrization of the same positive family, not a claim that both roots are always positive or admissible.

## Exact new fixture outside the paired qq case

Choose delta15,chi105 and put

    C=cos15, S=sin15, r=sqrt3/2-S,
    k=sqrt(1-r^2)>0,
    psi=195-arcsin(r), p=(1/2+C+k)/2.

Here1/2<r<1/sqrt2 implies30<arcsin(r)<45 and150<psi<165. Thus every strict family bound holds and qq is not the paired{90,150} arc. None of its four homogeneous qq triples is legal:3chi315,2chi+psi>360,chi+2psi>405,3psi>450. The exact producer proves p>1, so the new fixture has distinct lengths.

The metric relation is exact because

    exp(i(delta+chi))-exp(i delta)+exp(i(delta-psi))
      =exp(i120)-exp(i15)-k-ir
      =-1/2-C-k=-2p.

This fixture therefore belongs to the remaining pp-center/no-qq-homogeneous family after the reviewed one-noncentral reduction, and has an explicit periodic escape beyond the paired-qq cone.

The retained geometry uses the exact degree16 field

    Q(zeta24)[k], k^2=1-(sqrt3/2-sin15)^2,
    zeta24=exp(i15), k positive.

A's unit edge vectors are z^(0,5,8,13,16,21). B's are

    (1,z^4,z^8,z^12,z^17,z^4(-k-ir)).

The producer checks exact closure, all native angle-unit ratios, all48 strict support inequalities across the two species, every whole-side equality, all eight actual circular links and their symbolic360 rows. It independently develops the four faces by direct Euclidean side isometries, checks every cycle holonomy has trivial rotational part, computes the full primitive rank2 period lattice by exact rational Hermite normal form and proves lattice covolume equals the four-face area. All field coordinates, face placements,12 translation holonomies, primitive lattice basis, tile areas and covolume are retained. This fixture validates actual geometry; the preceding flat-torus proof, not fixture continuity, establishes the whole family.

## Stable retained artifacts and limitations

- `research/searches/branching-hexagon-two-run-pp-center-periodic-family.py`;
- `research/certificates/branching-hexagon-two-run-pp-center-periodic-family.json`.

Replay is read-only by default; an explicit`--output` is required for writes. The raw original quotient is read as fixed combinatorial data, and its former numeric geometry is replaced throughout by the new exact field and symbolic angle rows. Independent review should reconstruct native geometry, every actual circular link, full strict parameter domain, quadratic roots, exact fixture embedding, period lattice and flat-cover argument without importing the producer.

This is a positive sufficient family for the fixed indexed four-face carrier. It does not prove every tileable pp-center pair uses that carrier, does not exclude a cross-slot qq-chain branch or a tiling with different angle relations, and does not settle both-arc homogeneous or unrestricted-target cases.

Fresh full-domain independent review is [VALID](../reviews/branching-hexagon-two-run-pp-center-periodic-family-review.md), with a no-author-import checker for all native geometry, circular links, phase branches, exact fixture and period lattice.
