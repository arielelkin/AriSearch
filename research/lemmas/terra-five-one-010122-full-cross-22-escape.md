# A010122: every used AA22 seam forces a periodic omission escape

Date: 2026-10-13. Status: [independent hostile review VALID](../reviews/five-one-010122-cross22-fresh-hostile-review.md); producer and independent exact checkers PASS. This is a restricted B5+1-family result, not a solution of the unrestricted two-convex-polygon problem.

## Exact statement and imported dependencies

Let 108<x<126, x!=120, with y=720-5x, z=4x-360, r=360-2x, s=360-2y. Let actual strictly convex A and B have native corner words A=(x,y,x,y,z,z) and B=(s,r,r,r,r,r). Native side i joins corners i and i+1 modulo six. Suppose an actual defect-free whole-side trivalent field has complete star language AAAxyz, AABxxr, AAByys, ABBzrr and contains an AA seam using native A side4 (the zz side). Then A admits a periodic monohedral tiling. Consequently the original pair admits a periodic tiling by omission of B.

Equivalently, if A has no such monohedral escape, its native side4 is AB in every field of this kind. This conclusion concerns seams actually USED in the field. Equalities a4=a0, a4=a1, a4=a2 alone do not assert the existence of such a seam, and all other metric aliases remain allowed.

The settled full strict-convex-angle-line extraction and star-language results are imported when this lemma is applied to unrestricted tilings; the present local proof explicitly assumes the stated field. Reinhardt's sufficient periodic monohedral criteria are imported in the native indexing already reviewed in [the all-metric A001122 escape lemma](terra-001122-all-metric-periodic-escape.md):

    H1: angle0+angle1+angle2=360 and side2=side5;
    H2: angle0+angle1+angle3=360, side1=side3, side2=side5.

Each criterion may be applied after any cyclic or reflected native relabelling. They are sufficient criteria for actual convex hexagons; this proof needs no necessity claim. Since x+y+z=360, any indicated rainbow angle triple meets the angle requirement throughout the complete interval.

## Finite questions declared before enumeration

The exact first question is whether a complete two-ended USED AA22 pattern can avoid all sufficient H1/H2 relabellings. Its domain is three possible partner sides, both endpoint alignments, and the four native third-A offers at EACH end: 3*2*4*4=96. To retain all metric specializations, every one of the 203 equality partitions of the six actual A side lengths is also tested. If any non-H1/H2 patterns survive, actual positive polygon closure must be addressed before enlarging the local or global search. Here none survive, so no extra positive-closure obligation remains.

At each endpoint of an AA22 seam the central A contributes z. A two-A/one-B star would require the A colours xx or yy, so each endpoint must instead be AAAxyz. Thus the partner's two endpoint colours both avoid z. For A010122 the possible partner sides are precisely0,1,2, each a mixed xy side. Native sides3,4,5 have at least one z endpoint and cannot partner the seam. Both endpoint correspondences are retained, including reflection.

At a given end the third A supplies the unique remaining colour. It has two native corners of that colour, and its arms may occur in either order, yielding four offers. These are independent necessary choices at the two endpoints; no extension or nonoverlap premise is inferred. Matching the central/partner seam and the two remaining rays at both endpoints yields exactly five side equalities per case.

Explicitly, the central endpoint corners are4 and5 and their exposed arms are side3 and side5. If partner side j presents corner j, its exposed arm is j-1; if it presents corner j+1, its exposed arm is j+1. A third corner c presents arms (c-1,c) or (c,c-1). This determines every equality without chosen lengths, angle samples, or solver bounds. The certificate separately retains all64 native AAA cycles (two corners per colour, eight arm orders) and verifies each generated endpoint has compatible native AAA incidence.

## Exhaustive equality result and explicit sufficient witnesses

The96 raw cases yield36 distinct required equality partitions. Their three inclusion-minimal ancestors are as follows. A partition word names equality classes of a0,...,a5; differently named classes are unconstrained at this stage and may merge.

| Minimal ancestor | Forced side equalities | Sufficient relabelling |
|---|---|---|
| 012023 | a0=a3 and a2=a4 | H2 starting at corner1, forward |
| 012302 | a0=a4 and a2=a5 | H2 starting at corner3, forward |
| 012314 | a1=a4 | H1 starting at corner2, forward |

For the first row, relabelled corners0,1,3 are original1,2,4, with colours y,x,z; relabelled side1=side3 becomes a2=a4, and side2=side5 becomes a3=a0. For the second row, corners3,4,0 have colours y,z,x, and the two equalities are a4=a0 and a5=a2. For the last row, consecutive corners2,3,4 are x,y,z and relabelled side2=side5 is a4=a1. Thus each row gives a direct sufficient periodic family on the actual polygon.

All203 actual side-equality partitions are included. Exactly71 admit one or more of the96 patterns, and EVERY one satisfies H1 or H2. Each of the96 raw cases already satisfies such a criterion before further identifications. The certificate retains explicit cyclic/reflected witnesses for every case and compatible actual partition. Specializations cannot undo a sufficient equality, and the203-partition check explicitly confirms them rather than leaving alias cases implicit.

There is no positive-closure residual: some of these formal patterns may fail actual polygon closure, which can only remove cases. Every actual polygon satisfying any remaining pattern already meets the sufficient monohedral criterion. Unlike the companion A001122 argument, no separating functional or sampling of the angular parameter is needed here.

## Actual-field conclusion and replay

A USED AA22 seam in an actual field supplies one of the96 necessary patterns. Its actual A metric therefore satisfies an H1/H2 witness and has a periodic monohedral tiling. This is an existence consequence of a known sufficient polygon family, not an inference from finite local consistency to an infinite mixed field. Omission is permitted in the original problem, so that tiling is an escape for the original pair.

If no AA22 seam is used, the field satisfies exactly the support premise required by the support-strengthened [no-cross periodic-lift theorem](five-one-all-mask-no-cross-periodic-escape.md). Once that strengthening is independently reviewed, the used/unused dichotomy closes A010122 for the full B5+1 strict-convexity interval and arbitrary actual metrics. This lemma itself neither asserts the support theorem's review status nor covers different angle multiplicities.

Artifacts:

- [Producer](../searches/terra-five-one-010122-cross-22-gate.py)
- [Complete finite certificate](../certificates/terra-five-one-010122-cross-22-gate.json)

Replay without modifying the certificate:

    mise exec -- conda run --no-capture-output -n arisearch python research/searches/terra-five-one-010122-cross-22-gate.py --check research/certificates/terra-five-one-010122-cross-22-gate.json

Producer and [independent checker](../reviews/verify_five_one_010122_cross22_independent.py): PASS. Counts and explicit witnesses are exact; no floating-point computation, timeout, sampled metric, positive-density assumption, or finite-to-global extension conjecture enters the result. [Independent hostile review](../reviews/five-one-010122-cross22-fresh-hostile-review.md) is VALID. The complete all-native composition is retained in [the B5+1 synthesis](five-one-complete-native-all-metric-periodic-escape.md).
