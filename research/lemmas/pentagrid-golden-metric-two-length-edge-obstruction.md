# A two-length pentagrid pentagon pair requires partial contacts

**Status:** adversarially reviewed as valid in the
[fresh audit](../reviews/pentagrid-two-length-edge-obstruction-review.md),
with an independently checked exact finite signature certificate. This excludes edge-to-edge tilings of one fixed pair. It does not exclude unrestricted tilings and does not establish aperiodicity.

## Pair and theorem

Let z=exp(pi*i/5), defined exactly as the root of z^4-z^3+z^2-z+1 with Im(z)>0 and 4/5<Re(z)<81/100, and let phi=z+z^(-1). Use the exact U from [the periodic counterexample](../counterexamples/pentagrid-golden-metric-periodic-pair.md). Let V have edge vectors with directions

    (1,z^3,z^6,z^7,z^9)

and respective positive lengths

    (phi^3,phi^3,phi^3,1,1).

Taking cumulative sums from0 defines its five vertices; closure and genuine strict convexity are in [the metric certificate](../certificates/pentagrid-golden-metric-closure.json), V exponent vector (3,3,3,0,0). Its angles after its sides are (2,2,4,3,4) in units pi/5. U angles after sides are (1,3,4,4,3) and lengths (phi^3,phi^3,1,1,1). They are distinct congruence classes.

**Theorem.** The pair {U,V} has no edge-to-edge plane tiling, including reflected copies and tilings omitting either type.

## Native-corner length cycles

Write L=phi^3 and S=1, which are distinct positive lengths. Each corner has two incident side lengths, giving six corner classes:

    U36: LL; U108: LS; U144: SS;
    V72: LL; V144: LS; V108: SS.

The two U108 and the two U144 occurrences, and corresponding repeated V occurrences, have identical angle/length classes. At any full edge-to-edge vertex, read the numerical lengths of the incident rays cyclically. Each LL or SS corner preserves the length symbol; each LS corner switches it. Thus the number of LS corners is even. If there are no switches, all sectors must use the same length symbol. Equivalently, the corner multigraph on {L,S} must be connected and Eulerian. This is a necessary condition for an actual full vertex; no global extension is inferred.

Every full vertex has angle sum10 in units pi/5. The [enumerator](../searches/pentagrid-golden-metric-two-length-stars.py) checks all 9504 integer vectors 0<=n_i<=floor(10/angle_i), retaining only angle sum10 and the necessary cycle condition. It gives precisely17 signatures in [the certificate](../certificates/pentagrid-golden-metric-two-length-stars.json). This tiny domain is complete because the minimum angle is pi/5. No reflection or orientation restriction is used.

The only two signatures containing U144 are

    U144+U108+U108,
    U144+V108+V108.                               (1)

This also has a short direct check. After removing a U144_SS sector, the remaining angle budget is6. If the budget uses an LS sector, the even-switch condition forces two U108_LS corners, each with angle3. A V144_LS angle4 would need another switch of angle at least3, exceeding the budget. If it uses no LS sector, the cycle must stay entirely at S, where the only available remaining corners have angles4 (U144) or3 (V108); only two V108 corners fill6. Hence (1).

## Opposite-edge endpoint contradiction

U side3 has a U144 corner at both endpoints. In an edge-to-edge tiling a whole side of another tile must match it. At either endpoint, (1) requires that the corner of the neighboring tile adjacent to this seam is108 degrees. Hence the matched tile side must join two108-degree corners.

Neither U nor V has such a side: U angles cyclically are (108,36,108,144,144) at vertices0..4, and V angles are (144,72,72,144,108). Their respective108 corners are nonadjacent or unique. Therefore no U tile can occur in an edge-to-edge tiling of the pair.

If U is omitted, a V108_SS corner still has no possible full vertex. With only V corners, angle sum10 involving an angle3 can only be 3+3+4 or 3+3+2+2. The former has one LS switch; the latter has LL and SS loops with no switch, so is disconnected. Both violate the necessary length cycle condition. Thus V alone has no edge-to-edge tiling. This proves the theorem and handles either omitted type.

A supplementary observation from the same17 signatures is

    N_V(R) >= 2*N_U(R)-O(R)

for any hypothetical edge-to-edge tiling: at each vertex n_U108+n_V108>=2*n_U144; native counts are2N_U+N_V and2N_U. The opposite-edge contradiction is stronger, so this inequality is not used in the proof. It explains why a two-U/two-V torus could never pass for this metric.

## Exact scope and next obligation

Partial contacts break the whole-side length cycle. The legal half stars U144+U36=pi and V108+V72=pi can terminate sides partway; the neighboring ray segment lengths then need not equal the whole native lengths L or S. Applying the parity or endpoint argument to these situations would be an invalid quantifier change. The theorem therefore says that any unrestricted tiling of this fixed pair, if one exists, must use partial contacts.

This is a specific remaining construction test: determine whether the half-star contacts can form a globally extendable strip or substitution while prohibiting periodic alternatives. No such extension is presently given. The exact coordinates, closure, and contact avenues make it concrete, but finite four-face search failure is not evidence of aperiodicity. A source theorem or exact propagation invariant addressing partial lengths is needed before upgrading its status.

Replay:

    conda run --no-capture-output -n arisearch python3 research/searches/pentagrid-golden-metric-two-length-stars.py

The generator prints nondestructive JSON by default; use --output explicitly only to save a certificate. The certificate supports an elementary necessary-star calculation, not a solver-derived global existence assertion.
