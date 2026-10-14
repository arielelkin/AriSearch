# Fresh review of the mandatory P5/Q14 patch palette audit

Date: 2026-10-14. **Verdict: VALID for the same364 geometrically disjoint
mandatory-dimer patches.** This review concerns the adversary's newly
developed T-contact/native-star test, not independent review of the
reviewer's original P/Q metric producer. It introduces no larger patch
domain or periodic quotient.

Reviewed [adversary checker](construction-adversary-2026-10-14-p5q14-palette.py)
and [frozen pointed certificate](../certificates/construction-adversary-2026-10-14-p5q14-palette.json).
The fresh [witness verifier](verify_p5q14_mandatory_palette_witnesses.py)
imports neither adversary module. It reconstructs every patch from the
author's separately frozen exact guest rotations/translations, reflected
P placements and mandatory α–α mates. The two guest-hand enumerations
have complementary cycle bits; all actual native vertices agree. Full
native indexing is preserved even for clockwise reflected placements:
P vertex0 is α and vertices1–4 are β. Q's native corners are allγ.
Coincident actual tiles are identified by their vertex sets before counts.

Every native angle exceedsπ/2. At a genuine corner in a tile-side interior,
the host occupiesπ and the other half-disc must contain at least two
native corners (one is strictly less thanπ), whose sum exceedsπ. Thus
such a T-contact cannot occur in any admitted plane tiling. The exact
segment test cross(end−start,point−start)=0 with
(point−start)·(point−end)<0 correctly distinguishes an interior contact
from a native endpoint. The independent verifier checks all336 pointed
defects: the exact face pair, subject corner, host edge, point and both
host endpoints match its own reconstruction and satisfy the strict test.

At every remaining native vertex the full star is either PPP=(2α,β) or
PPQ=(2β,γ). A native-corner multiset already in the patch must therefore
be componentwise contained in (2,1,0) or(0,2,1); added tiles cannot remove
an existing corner. The adversary's group test uses exactly those bounds.
For each of the28 reported positive states, the independent verifier
exhausts every actual corner/edge comparison between distinct patch faces
and all coincident native-corner groups. It verifies no T-contact and
the stated componentwise compatibility. This necessary condition does
not construct the missing tiles or prove extension.

Results:364 geometric patches divide into336 forbidden T-contact states
and28 states with no T or native-star defect in this domain. There are no
states rejected solely by the star-group test. **Distribution correction:**
the adversary initially reported “two per14 words” in a message by dividing
the total28 by the earlier14 geometric-word count. The certificate itself
was correct. Fresh verification finds four states per each of seven
split-v-run periods:

    vvuvvuu, vvuuvvu, vuvvuuv, vuuvvuv,
    uvvuvvu, uvvuuvv, uuvvuvv.

The seven single-four-v-run periods have no surviving state. No congruence
quotient was used for these indexed counts. The correction was supplied
to the adversary and root before final synthesis; no witness or geometric
computation changed.

All364 patch/cycle keys match the original mandatory-completion domain.
The verifier proves all336 negative pointed incidences and independently
exhausts the absence checks for all28 positives. No native-index,
reflection, duplicate-face or segment-endpoint defect was found. Exact
Sage field/real-algebraic arithmetic remains trusted. The separate
one-Q translation-orbit attack and straight-side hierarchy restriction
have distinct scopes; neither positive patch status nor a restricted
periodic-model failure proves aperiodicity or a plane tiling.

Replay:

```text
mise exec -- conda run --no-capture-output -n arisearch python research/reviews/verify_p5q14_mandatory_palette_witnesses.py
```

The broader two-convex-tile problem remains unresolved. Future work must
address actual extension/compatibility among differently oriented Q
copies or a changed construction mechanism; this review performs no
further search.
