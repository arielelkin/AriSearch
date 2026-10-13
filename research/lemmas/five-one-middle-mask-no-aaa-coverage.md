# Seven middle-mask B5+1 native words: unusedAAA coverage

Date:2026-10-13. [Fresh independent hostile review VALID](../reviews/five-one-middle-mask-no-aaa-coverage-fresh-hostile-review.md); root3072-wheel and independent12288-wheel checkersPASS. Conditional actual-field coverage, not a full changed-multiplicity theorem.

## Statement and scope

Use the reviewed B5+1 angle family x in(112.5,126),x!=120,y=720-5x,z=4x-360,r=360-2x,s=360-2y. Actual A has one of the native words001212,002112,010212,011202,012012,012021,012102; B has native(s,r,r,r,r,r). Suppose an actual mixed defect-free field has every B degree2 and uses NO AAA vertices. Then the actual pair admits a periodic tiling. For four words such a mixed field is impossible; for three, a periodic full-native lift exists at every actual metric specialization.

The original unrestricted tiling is not assumed already in this form. The reviewed saturation extraction supplies a degree2 limit or a pureA periodic escape, but does not generally remove AAA. Thus actual fields USING AAA remain the separate obligation. Pure limits and omissions keep their reviewed unrestricted scopes.

## Private-seam exclusion covers four words

The [reviewed saturated palette](terra-five-one-b-saturated-chain-reduction.md) forces these seven A words to the middle B maskBB{1,4}. Every AB side then has endpoint pair02 or12. Hence every A side with neither endpoint2 is necessarilyAA. In a noAAA field each A0/A1 corner has exactly one AA arm; two would give an AAA vertex. Each A2 corner has no AA arm.

For001212,010212,011202,012021 there is a native0/1 corner incident to TWO privateAA sides. Their noAAA mixed fields are therefore empty, independently of lengths and geometry. This is a complete local native obstruction, not a finite extension failure.

For the remaining002112,012012,012102 the privateAA sides are exactly0 and3. Every A has precisely these two oppositeAA neighbours. As in the independently reviewed [adjacent-pair row lemma](five-one-adjacent-pair-no-aaa-binary-row-escape.md), primitive triangular-lattice line intersections force allA components parallel; entire rows alternate A/B using exact degree2 of both species. Choose the common directionD0 and label A rows byy=2j.

## Complete periodic angle bases with binary full-native fibres

A native state(r,s) places corner r+s*k in slotk, side r+k in side-slotk for s=+, or r-k-1 for s=-. Exactly four A row states have native0/3 on side-slots5/2. Group them into two angle profiles, each containing two full native states:

| A word | profile0 states | profile1 states | horizontal flip h | A-row vertical flip v | B offset o |
|---|---|---|---|---|---|
|002112|(1,+),(0,-)|(4,+),(3,-)|1|0|0|
|012012|(1,+),(4,+)|(0,-),(3,-)|1|1|1|
|012102|(1,+),(3,-)|(0,-),(4,+)|0|0|1|

The two states in every listed profile have IDENTICAL all-six angle profiles; their native side metrics can differ. B profile0 has states(1,-),(5,+), with s at upperAAB slot1; profile1 has(4,-),(2,+), with s at lower slot4. Each B profile again has two states with identical angles.

AA endpoint-colour matching forces each A row's angle profile to change byh perD0 step. Its two adjacent A rows interact through the central B's upper/lower AAB vertices: native x/x needs B_r, y/y needs B_s, exactly one each. This forces profileupper=profilelower XORv and profileB=profilelower XORo. These are exact native-angle relations, independent of side lengths.

The [independent finite checker](../reviews/verify_five_one_middle_mask_no_aaa_phase_coverage.py) derives the four row states from all12 direct/reflected placements, checks every AA endpoint pairing, and enumerates all3072 centre/row phase and chirality wheels. Wheel legality holds exactly under the table's two phase conditions; no additional chirality restriction comes from angles. The other four words are independently rejected by their private-side corner incidence.

Consequently A at column i,row2j has profile p0 XORh*(i mod2) XORv*(j mod2), and B between that row and the next has profile pA XORo. Both choices of initial profile p0 are included, including the constant-profile012102 case. Species/angle profiles have common periods2D0 and4D1. No actual metric period has been asserted yet.

## Metric lift, including every side merge

Each cell now has exactly two remaining full native states. Give it one bit. Every side-length constraint is equality of two binary-valued functions, each depending on its own cell bit. Their possible tables are full, empty, pins, equality, or inequality; this is the independently reviewed classification used in the adjacent-pair row proof, and includes every coincidence of lengths. No arbitrary binary SFT or multi-state fibre theorem is used.

The assumed actual field supplies a solution to this periodic binary equality network. The [reviewed finite-cover theorem](periodic-binary-equality-fibre-lifting.md) produces a solution on a finite-index periodic cover. Its full native field satisfies every angle and seam constraint. Reviewed metric development gives an admitted plane tiling with a nonzero translation, after squaring a glide if needed. This develops a new tiling, not a reinsertion at source coordinates.

The three successful words thus have periodic escapes whenever the assumed noAAA field exists; the four empty words cannot supply that field. This proves the conditional seven-word coverage theorem.

## Replay and programme consequence

    MISE_AUTO_INSTALL=0 mise exec -- conda run --no-capture-output -n arisearch python research/reviews/verify_five_one_middle_mask_no_aaa_phase_coverage.py

Finite domain: seven middle-mask words; twelve native states per species; four row states for the three survivors;3072 exact phase/chirality wheels. No geometry sample, solver or timeout. The auto-install environment flag skips installation of an unrelated unavailable browser tool; it does not bypass its trust policy or alter the installed research environment.

The two all-mask words001122,010122 remain outside this middle-mask theorem. The two impossible saturated words001221,011022 are independently covered by the reviewed capacity/pureA theorem. A012012's usedAAA branch already forces centralA, hence its complete coverage is independently reviewed. Other usedAAA branches need actual closure plus compatible B neighbourhoods; positive local geometry still does not imply infinite tilability. This coverage theorem does not complete the original problem.
