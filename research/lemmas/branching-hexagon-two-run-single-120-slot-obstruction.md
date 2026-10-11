# A single-120 resonance: exact native-slot global obstruction

Status: **VALID after fresh independent hostile review.** This is a new untileability obstruction on a homogeneous pp resonance, not a target resolution. A feasible corner-count ratio is rejected by actual indexed seam-end balance. The exact fixture and abstract five-type obstruction have passed independent no-producer verification.

## Exact new fixture

Take delta15,q=1 and native pp/qq angles

    (alpha,beta,chi,psi)=(120,105,90,150).

With z=exp(i*pi/12), put

    P=1+z^4+z^9,    Q=1+z^6+z^8,
    p=sqrt((Q conjugate(Q))/(P conjugate(P)))>0,
    R=-pP/Q.

A has precisely lengths(p,q,p,q,p,q) and directions(0,75,120,195,240,315). B has directed edges

    (p,p z^4,p z^9,R,R z^6,R z^8).

Thus its word is(p,p,p,q,q,q). Closure is exact and R has modulus1. The producer verifies strict side supports at every nonincident vertex of both native polygons. Its positive p differs from1; the exact p-squared coefficient vector inQ(zeta24) is retained. A admits no homogeneous corner star; B admits the pp star of three alpha120 corners and no homogeneous qq star.

**Claim:** this pair admits no unrestricted plane tiling, by the global dual below. The reviewed defect-free hexagon limit theorem reduces any putative unrestricted tiling to an actual trivalent edge-to-edge tiling, possibly omitting either species. The strong dual charges both species negatively, so omission does not evade it.

## Abstract star domain, including all orientations

Let alpha120, chi=120-2delta and psi=120+2delta, with0<delta<30. B's beta is arbitrary subject to actual strict convexity and closure. Suppose the complete collection of native length-legal trivalent stars of a given distinct binary pair is contained in these five named types:

    (alpha,alpha,alpha),
    (A_H,A_H,chi),
    (A_L,A_L,psi),
    (A_H,A_L,alpha),
    (B_0,B_3,beta).

Repetition means separate tile occurrences; A_H and A_L each have three indexed native slots. Do not merge those slots. For the concrete fixture the exact angle-unit product enumeration gives precisely these five types, with all cyclic orders/reflections resolved into80 native oriented stars. No extra metric-angle star is silently omitted.

For every geometry meeting this abstract complete-star containment hypothesis, the same rational dual below excludes a plane tiling. This is a scoped generalization from the actual discrete native-star domain, not an inferred extension from one sample's angle feasibility or from a bounded patch failure.

The corner-marginal counts alone have a feasible support. Per3B and2A take one(alpha,alpha,alpha) star, three(B0,B3,beta) stars, three(2AH,chi) stars and three(2AL,psi) stars. All typed native angle multiplicities can be balanced after distributing A's three H/L native labels symmetrically. This does not balance the signed native seams. A five-face periodic quotient would additionally have15 occurrences of each length, impossible to pair; doubling the counts fixes that elementary parity but still fails the stronger global invariant. No quotient search is used in this proof.

## Exact symmetric separating functional

Corner weights W are integer:

    W(A native vertices0,2,4)=-1,
    W(B native vertex4)=-3,
    all other indexed corner weights0.

Each A and each B has total W=-3.

Use the reviewed signed seam key(x,y,parity), where x,y are indexed side slots and parity is the xor of their native endpoint flags at the star. Order x,y lexicographically. The seam sign is+1 at native endpoint0 of the smaller slot and-1 at endpoint1. For x=y and parity1 the feature is0, since no copy is distinguished; for x=y and parity0 the sign is well-defined. Both endpoint flags reverse at the other end of a whole shared seam, so the signed feature cancels exactly between seam ends.

Define seam potentials Y as follows, with all unlisted keys0. Species A precedes B in slot order.

| Indexed slot pair | Parity | Y |
| --- | --- | ---: |
| (A,i even), (B,1) |1 |-3 |
| (A,i even), (B,1) |0 |1 |
| (A,i odd), (B,3) |0 |-7 |

All80 oriented native stars have nonnegative W-corner charge plus signed Y-seam charge. Exact integer replay gives:

| Named star type | Number of oriented native stars | Augmented charge distribution |
| --- | ---: | --- |
| AH,AL,alpha |36 |18 at0;18 at2 |
| AH,AH,chi |18 |18 at2 |
| AL,AL,psi |18 |18 at0 |
| B0,B3,beta |4 |4 at0 |
| alpha,alpha,alpha |4 |4 at0 |

This table resolves each A native slot, every legal cyclic order and both mirror choices. It is not only a five-row unlabelled angle check. The retained certificate includes all80 explicit stars, all12 corner-count columns, all36 seam-feature columns, the symmetric W/Y vectors and the original independently checkable rational solver dual. The symmetric integer functional is checked directly against every exact column; its validity no longer depends on the solver's decision.

## Infinite boundary argument

In an admitted trivalent edge-to-edge tiling select all tiles whose interiors meet a square of radiusR. Their number N isOmega(R^2) by area coverage and fixed maximum tile area. Their total W corner weight is exactly-3N.

At a complete selected vertex its actual oriented star is among the allowed80 and has nonnegative augmented charge. Signed seam terms cancel between the two ends of each whole seam whose endpoint stars are both complete. Every incomplete selected vertex and every seam with an incomplete end is incident to a boundary tile. Fixed tile diameters, positive minimum areas and disjoint interiors give onlyO(R) boundary tiles; each has six corners and sides and all fixed integer weights are bounded. Therefore all incomplete W weights and all uncanceled Y terms have total magnitudeO(R).

It follows that the total selected W charge is at least-O(R), contradicting-3N with N=Omega(R^2). This excludes every actual trivalent tiling covered by the five-type domain. The reviewed compactness theorem excludes the original unrestricted tiling. The proof imposes no translation invariance, species ratio, frequency existence or positive density assumption.

## Real resonant slice and exact scope

The natural metric slice hasalpha120, chi/psi120∓2delta. For beta in(0,180), its unit p-chain is

    P_beta=1+exp(i60)+exp(i(240-beta)),

which never vanishes because the first two terms have magnitude sqrt3 and the last has magnitude1. Closure fixes p=2cos(delta)/|P_beta| and the q-chain phase. Near(delta,beta)=(15,105), strict convexity and p unequal to1 persist. The five displayed star-type angle equalities hold identically on this slice: the two A/qq sums and the AH/AL/alpha sum are360, alpha repeated three times is360, and B0+B3+beta=360 by the hexagon angle sum. Every other finite length-legal native corner triple has angle sum different from360 at the exact fixture. Continuity therefore gives some open neighborhood in this two-parameter resonance slice where the complete allowed-star domain stays exactly these five types. The same global dual excludes that entire neighborhood. This assertion requires no inference that a locally feasible configuration extends; the invariant is negative on each actual tile.

No explicit maximal beta/delta exclusion domain is claimed. Additional star equalities can occur elsewhere on the resonant slice and must be retained and audited before extending the conclusion to those strata. In particular beta120 adds pp corner coincidences and lies on the known periodic first curve; it is outside the five-type obstruction. This is an actual open untileability region on a homogeneous resonance, not a complete classification of that resonance.

## Artifacts

- `research/searches/branching-hexagon-two-run-single-120-slot-obstruction.py`;
- `research/certificates/branching-hexagon-two-run-single-120-slot-obstruction.json`.

Normal replay is read-only; writing requires explicit`--output`. The authoring producer reuses the earlier reviewed catalog producer core for this one NEW exact tuple; fresh independent verification must not import either producer. The producer reconstructs native geometry and strict supports, enumerates the full angle/legal-label domain, checks the UNSAT rational dual and the explicitly stated symmetric integer dual, and retains all raw stars/features. It does not infer untileability from finite assembly failure. No prior artifact or Git history was modified.
