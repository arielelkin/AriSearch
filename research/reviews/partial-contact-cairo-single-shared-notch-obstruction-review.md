# Fresh hostile audit of the single-shared Cairo notch obstruction

**Reviewer:** branching_hexagons, freshly assigned by root. This reviewer did not develop or repair the notch obstruction or the canonical-cluster reduction. No author code was executed or imported. The exact author lemma and reviewed geometric dependencies were read, and a separate checker was built from raw macro boundary rays and exact convex intersections.

**Artifact:** [notch obstruction](../lemmas/partial-contact-cairo-single-shared-notch-obstruction.md).
**Verdict:** **VALID** for the exact r=4/5,t=6/5 pair under unrestricted contacts and all isometries. No unresolved substantive defect was found. The result is exact-fixture untileability, not a symbolic-family classification, existence claim, or original target-wide result.

## Proof obligations attacked

The [reviewed canonical-cluster reduction](../lemmas/partial-contact-cairo-single-shared-fourfold-clusters.md) partitions any hypothetical tiling into complete reflected four-pentagon clusters S(r),S(t), with unique native central corners. Its converse equivalence is not used as an existence assertion. Since either individual pentagon is excluded by its reviewed private-arm obstruction, a hypothetical tiling contains an S(r) host; alternatively the absence of P already contradicts Q-only tiling.

At a reflex240 host notch the uncovered sector is120. Every possible incident macrotile boundary sector is90,120,180,240. Side-interior contacts contribute180, including original native vertices that become internal points of a macro side. Thus the gap cannot split into several allowed sectors and must be exactly one native macro E120 corner. This remains valid for arbitrary macro orientation and partial contacts; convexity of the whole macro is not assumed.

The reviewer independently enumerated all four E corners and both assignments of their two boundary rays to the host's directions300 and60 for each species. The resulting16 exact orthogonal placements reduce, by equality of complete transformed macro boundary sets, to exactly four physical possibilities: species z in {r,t} and centers(d_r+d_z+1, plus/minus sqrt3). Therefore the author does not secretly restrict to a common orientation or leave out a chirality choice. All four initial fillers are interior-disjoint from the host.

For either sign the unit endpoint is X=(sqrt3*r/2, minus/plus sqrt3/2), exactly the midpoint of a native host e side. It is a genuine T with one straight180 sector and two original90 sectors. The [reviewed two-T theorem](../lemmas/partial-contact-cairo-two-t-switch.md) forces the perpendicular90-to120 arm to be a complete seam: an earlier endpoint would be120 inside the other native arm. The private length z=r or t occurs only in its corresponding native slot. The mate is the reflection across that full seam, since preserving equal90 endpoints is required; the half-turn would exchange90 and120. This argument applies at this particular T and does not presume every exceptional r/t bank elsewhere is wholly matched.

The raw filler boundary gives the vector from X to its axis notch as (sqrt3*z/2, plus/minus z/2). It has length z and is perpendicular to the hosted e side. Its reflection matrix is exactly the author's Fplus/minus30. Reflecting the actual original tile also reflects its native canonical cluster center and forces the entire reflected cluster by the reviewed private-arm cluster rules. The reflected center differs from the filler center. Hence they are distinct canonical clusters and must be interior-disjoint; they cannot be two descriptions of the same cluster or share an original occurrence.

Finally the reviewer avoided the author's point witnesses entirely. A separate exact half-plane clipping algorithm constructs the intersections of actual constituent convex pentagons in B and its forced reflection C. For each species/sign at least one intersection has strictly positive area, directly proving interior overlap. This contradicts the original tiling's interior-disjointness.

## Independent exact checker

[Independent verifier](verify_partial_contact_cairo_single_shared_notch_independent.py) uses Q(sqrt3), raw quarter-pentagon vertices and raw12-gon boundaries only. It imports no author module and contains none of the author's W formulas. It checks strict convexity of each quarter face,16 raw E/ray placement matrices and their physical deduplication,64 initial host/filler exact intersection areas equal to zero, the native e midpoint, full bank length and orthogonality, both reflection matrices, distinct canonical centers, and positive-area actual pentagon intersections.

The largest constituent intersection area for z=r is6/5-9sqrt3/100 for either sign. For z=t it is9/5+11sqrt3/100 for either sign. Both are strictly positive in the specified positive embedding.

Replay:

    conda run --no-capture-output -n arisearch python research/reviews/verify_partial_contact_cairo_single_shared_notch_independent.py

Completed output: PASS, with the stated exact areas. No solver, numerical tolerance, bounded extension search or failure-to-find is used. The only imported mathematical dependencies are the already reviewed canonical-cluster and two-T geometric theorems and single-pentagon omission obstruction.

## Remaining scope

The argument has not independently classified every r in the symbolic interval or reviewed the privacy/event identities away from4/5. Its valid consequence is that this exact exceptional fixture cannot tile; it invalidates attempts to promote its macro reduction into a construction. It does not settle the original two-convex-polygon task.
