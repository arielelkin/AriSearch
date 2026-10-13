# A001122: every used AA22 cross seam forces a periodic escape

Date: 2026-10-13. Internally proved with complete exact finite certificate and independent checker PASS; fresh hostile review assigned to luna. This is a native spatial lemma on the full strictly convex B5+1 resonance interval, not the original global problem.

## Statement and precise support hypothesis

Let108<x<126, x!=120, y=720-5x, z=4x-360, r=360-2x, s=360-2y. Actual strictly convex A has native corner word(x,x,y,y,z,z), and B has(s,r,r,r,r,r). The complete trivalent allowed star language is AAAxyz,AABxxr,AAByys,ABBzrr. Assume an actual defect-free whole-side field contains an AA seam using native A side4, whose two endpoints are z,z. Then actual A belongs to a sufficient periodic monohedral family. Therefore the original pair admits a periodic A-only tiling.

Equivalently, if A has no periodic monohedral escape, every actual defect-free field has native A side4 always AB, even when its length equals one or more other native A side lengths. The conclusion is about a USED cross seam; equalitya4=a0/a1/a2 alone does not establish a seam or invoke this theorem. A no-cross support theorem may use the resulting actual-field condition, but a no-cross metric theorem requires its hypothesis to be broadened and reviewed before synthesis.

The open interval is the full strict-convexity domain of this line: y in(90,180),z in(72,144),r in(108,144),s in(0,180). All angle names are distinct except at excluded x=120. The new closure argument below holds on this entire interval, including x<112.5 where z is acute. The extraction/honeycomb extension to this interval is an imported dependency whose review is managed by root; the local lemma itself explicitly assumes the stated trivalent field.

Dependencies: settled actual native honeycomb development and complete angle-star palette, and the Reinhardt H2 sufficient periodic family. In the indexing where sidei joins corneri,i+1, H2 is

    angle0+angle1+angle3=360, side1=side3, side2=side5,

after some cyclic/reflected relabelling. This is the reviewed H2 dependency retained in `terra-001122-all-metric-periodic-escape.md`, from refreshed primary source https://arxiv.org/html/2508.01404v2. It is a sufficient family for actual convex hexagons; no angle>90 hypothesis is imposed by the criterion.

## Complete two-ended native domain

Both endpoints of a used AA22 seam contain an A z corner. Such a vertex cannot be AAB, since the only two-A stars are xxr,yys. Hence both vertices are AAAxyz. The neighbour A has neither endpoint colour z, so its opposite seam is exactly one of native sides0(00),1(01),2(11). Sides3,4,5 all have a z endpoint and are impossible on that neighbour. This is why enumerating only22↔01 would be incomplete.

For each partner sidej in{0,1,2}, both endpoint alignments are allowed. At each end the third A corner has the remaining colour; there are two such native corners, each in two arm orders, for four possibilities. The full necessary domain is thus3*2*4*4=96 cases. Each requires a4=aj and the two exposed-arm equalities at each endpoint. The third A copies are allowed independent choices; no extra overlap/extension assumption is used. The producer also constructs all64 native AAA cycles (two corners of each colour and eight arm reversals) and checks that both endpoints of every case belong to that complete star list.

To make the exact equalities explicit, put the central seam endpoints at native corners4,5. If partner corner at an endpoint is j, its other arm is sidej-1; if it is j+1, its other arm is sidej+1. Central exposed arms are side3 at corner4 and side5 at corner5. For a third A native cornerc, its two possible ordered arms are(c-1,c) and(c,c-1). Matching these to the central/partner exposed arms derives all five equalities without choosing any lengths or angles numerically.

The mathematical question declared before computation was whether any complete two-ended cross pattern avoids every sufficient H2 family. If none did, metric closure would be unnecessary. If any remained, actual positive closure would be tested before larger B/patch enumeration. Exactly one formal actual partition remains, and it fails positive closure by the analytic separator below.

## Equality classification including every specialization

The96 cases yield26 distinct required equality partitions. Their four inclusion-minimal partitions, expressed as restricted-growth words for native sides0,...,5, are:

| Minimal required partition | Consequence |
|---|---|
| 010213 | a0=a2 and a1=a4: H2 |
| 012023 | a0=a3 and a2=a4: H2 |
| 012302 | a0=a4 and a2=a5: H2 |
| 012012 | a0=a3,a1=a4,a2=a5: residual closure obligation |

The H2 statements follow from exact native relabellings of the criterion above. For C001122 the complete H2 conditions reduce to these three sufficient patterns; no H1 rainbow consecutive triple exists for this native word.

All203 actual equality partitions of six side lengths are checked against all96 cases. Exactly41 actual partitions admit at least one case. Forty satisfy one of the three H2 patterns. The sole non-H2 partition is012012 itself. Its further specializations are not ignored: they occur among the forty H2 cases already checked. Among the96 raw cases only one has this non-H2 required pattern: partner side1, endpoints reversed, third A corners0 (reversed arms) and3 (forward arms). Its equalities are a4=a1,a0=a3,a5=a2. These count statements are exact finite certificate results, not low-rank extrapolations or joint geometric-realizability claims.

## The residual partition has no positive closed polygon

Set u=180-x, so54<u<72 andu!=60. Then exterior turns are u,u,v,v,w,w withv=360-5u,w=4u-180. Put U=exp(iu). Starting from native side0 direction1, the exact six unit edge directions are

    (1,U,U^-4,U^-9,-U^-5,U^-1).

For sideword(a,b,c,a,b,c), positive closure requires

    a(1+U^-9)+b(U-U^-5)+c(U^-4+U^-1)=0,

witha,b,c>0. The factor1+U^3 is nonzero: within54<u<72 it vanishes onlyatu60, excluded. Multiply the closure byU^6/(1+U^3). It becomes

    a(2cos(3u)-1)+b(U^4-U)+cU^2=0.

Every coefficient has strictly negative real part throughout this open interval:

- 3u in(162,216), so2cos(3u)-1<0;
- cos(4u)-cos(u)=-2sin(5u/2)sin(3u/2)<0, because5u/2 in(135,180) and3u/2 in(81,108);
- 2u in(108,144), socos(2u)<0.

Taking real parts gives a strictly negative left side for any positive a,b,c, contradicting zero. Thus the residual cannot even be a positive closed polygon. Convexity, B closure and global extension need not be tested. The same separator also excludes merged opposite-length patterns whenever they satisfy this grouped closure, but the complete finite ledger already accounts for all merges through the actual partitions.

## Conclusion and exact replay

Every used AA22 seam therefore forces actual A into H2. It has a periodic monohedral tiling, admitted by the original pair because omission is allowed. If the original actual A is nonmonohedral, native side4 must be AB in every extracted trivalent field, independently of whether lengthspermit an otherwise formal cross match. This support-level implication is stronger than a metric noncollision assumption and is the appropriate input for a no-cross counting theorem.

Producer, certificate, independent checker:

- research/searches/terra-five-one-001122-cross-22-gate.py
- research/certificates/terra-five-one-001122-cross-22-gate.json
- research/reviews/verify_terra_five_one_001122_cross_22_gate.py

    MISE_AUTO_INSTALL=0 mise exec -- conda run --no-capture-output -n arisearch python research/searches/terra-five-one-001122-cross-22-gate.py
    MISE_AUTO_INSTALL=0 mise exec -- conda run --no-capture-output -n arisearch python research/reviews/verify_terra_five_one_001122_cross_22_gate.py

Both PASS. The independent checker imports no producer code: it rebuilds equivalence partitions by graph-component traversal, the full96 native cases and64 stars, all203 actual partitions, the exact four minimal ancestors and three H2 alternatives, and the residual Laurent transformation overQ(U). The angular sign domains use exact rational degree inequalities. No sample angle, floating geometry, solver, search bound, timeout or global extension conjecture appears. MISE_AUTO_INSTALL=0 only avoids installation of unrelated tooling and does not waive provenance checks.

Remaining obligation for complete A001122 coverage: combine with a freshly reviewed no-cross theorem whose hypothesis is UNUSED AA22 in the actual field, not merely distinct side lengths. This lemma does not classify A010122 or other angle families, and does not resolve the original two-convex-tile problem.
