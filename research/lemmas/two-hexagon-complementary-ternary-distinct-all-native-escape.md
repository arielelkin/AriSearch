# Complementary ternary hexagons: all native words and actual metrics

Date:2026-10-13. Status: root synthesis of independently reviewed results;
[fresh synthesis review VALID](../reviews/two-hexagon-complementary-ternary-distinct-all-native-escape-synthesis-review.md). Restricted angle-family theorem, not the
original unrestricted two-convex-polygon problem.

## Theorem

Let A,B be actual strictly convex hexagons with angle multisets

    A: two copies each of x,y,z,
    B: two copies each of 360-2x,360-2y,360-2z,

where x+y+z=360 degrees,90<x,y,z<180, the three A values are pairwise
distinct and none is120. Native cyclic orders and all actual side metrics
are arbitrary. Reflected copies, original partial contacts and omission of
either shape are permitted. If {A,B} admits a plane tiling, it admits a
plane tiling with a nonzero translation symmetry. Hence no pair in this
complete angle/native/metric stratum is aperiodic.

The two congruence classes are automatically distinct here: equality of an
A angle and a complementary B angle would force either an A value120 or
two A values equal. All six angle values are therefore distinct.

## Independently reviewed native zero-core coverage

Define the five type stars

    AAA=(x,y,z), BBB=(r,s,t),
    AAB=(x,x,r),(y,y,s),(z,z,t),
    (r,s,t)=(360-2x,360-2y,360-2z).

Each native proof below establishes the following USED-star-core statement:
if an actual connected defect-free field for its native A word has all its
vertices among these five stars, the pair admits a periodic escape. The
proofs do not need other algebraically allowed stars to be absent when those
stars are unused. Fresh native reviews explicitly check this conditional form.

The11 dihedral native A bracelets fall into five colour-permutation orbits.
Colour permutation reparameterizes x,y,z and their complements simultaneously;
it transports every native side word and never permutes corners of a fixed
polygon without transporting its geometry. B is arbitrary in every proof.

| Native representative | Orbit size | Reviewed zero-core mechanism |
| --- | --- | --- |
|012012|1|Every legal AAA ray cycle forces central A by the positive sine closure kernel; noAAA makes the mixed B ring impossible|
|001122|1|All203 side partitions; residual outerAAB rings force an index3 Bcoset and periodic full-native quotient actions|
|001221|3|Only Bsameword can occur; all768 ring AA-equality graphs force equilateral A and an H1 omission escape|
|001212|3|All203 partitions;23 functional outerAAB fibres plus one AAA fibre whose positive closure forces equal A angles, outside this stratum|
|010212|3|All203 partitions; every outer-completable native metric fibre has a sufficient H1/H2 monohedral escape|

Proofs and fresh hostile reviews:

- [012012](terra-ternary-opposite-a-all-metric-escape.md),
  [review](../reviews/terra-ternary-opposite-a-all-metric-fresh-hostile-review.md);
- [001122](terra-001122-all-metric-periodic-escape.md),
  [review](../reviews/terra-001122-all-metric-periodic-escape-fresh-hostile-review.md);
- [001221](terra-001221-all-metric-periodic-escape.md),
  [review](../reviews/terra-001221-all-metric-periodic-escape-fresh-hostile-review.md);
- [001212](terra-001212-all-metric-periodic-escape.md),
  [review](../reviews/terra-001212-all-metric-periodic-escape-fresh-hostile-review.md);
- [010212](terra-010212-all-metric-periodic-escape.md),
  [review](../reviews/terra-010212-all-metric-periodic-escape-fresh-hostile-review.md).

The [independent orbit checker](../reviews/verify_ternary_native_word_coverage_independent.py)
reconstructs all11 bracelets and their disjoint orbit sizes1,3,3,1,3.
Actual-metric specialization is included through all203 equality relations
in each native ring reduction, or the complete closure/equality graph
argument. Formal nonrealizable partitions are retained as necessary tests;
no angle grid or low-rank ancestor is used as polygon realization.

## All permitted angle points reduce to that core

The reviewed [56-triple resonance ledger](two-hexagon-opposite-a-resonance-removal.md)
and [independent checker](../reviews/verify_ternary_resonance_ledger_independent.py)
classify every three-angle type equation after x+y+z=360. There are five
identity stars and twelve nonidentity line directions, all passing through
the all120 point. Three lines impose equal A values, three impose an A
value120, and six ordered lines impose Ai=4Aj-360 for i unequal to j.
At a noncentral point on one of those last six lines, the sole extra type
star is Ai Bj Bj. Distinct non120 A values place a point either outside all
nonidentity lines, or on exactly one of these six soleABB lines.

Start with any original admitted tiling. The reviewed
[defect-free hexagon limit](hexagon-limit-and-periodicity.md) supplies an
admitted whole-side trivalent field, possibly pure. If its angle point is
outside those six lines, every vertex already belongs to the five-star core.
If on one line, assign type-constant A weights p_i=1,p_j=-1,p_k=0 and B
weights -2p. Every full A or B tile has weight sum0 because each colour
occurs twice. Every core star has score0, and the one extra star has score5.
The independently reviewed nonnegative-potential argument therefore gives
an admitted defect-free translated limit with no extra stars. It keeps the
same actual shapes and angles; it does NOT alter their complete algebraic
triple language. A species may disappear harmlessly. Whole-side contacts and
trivalence persist by the reviewed uniform vertex separation proof.

Apply the appropriate reviewed native used-core theorem, selected by its
orbit. It supplies an admitted periodic tiling. Pure limits instead give a
monohedral periodic tiling by the named unrestricted convex-hexagon theorem.
Every case yields a periodic escape, proving the theorem.

## Geometric and computational scope

The result covers the complete distinct/non120 complementary ternary
stratum, all121 fixed-colour native A/B bracelet pairs, arbitrary positive
side metrics of ACTUAL closed strictly convex polygons, and every further
length equality. It does not claim every formal metric partition is feasible
or that every admitted source tiling is itself periodic.

The remaining angle points WITHIN the same multiset family are exactly the
three equal-angle lines and three A-angle120 lines, including their all120
intersection. Type-constant potentials preserving the full five-star core
cannot remove their extra stars; those cases need a new geometric/native
mechanism. Other angle multisets and general pentagon-containing pairs remain
outside this theorem. A complete solution to research-problem.md is not
claimed and no final research report is warranted.

Stable proof dependencies are the reviewed defect-free/monohedral theorems,
the exact native finite certificates and periodic full-A quotient lifting,
and the reviewed resonance reduction. Native data are replayed through
research/searches/verify.py. No search bounds, solver timeout or numerical
angle agreement establish this synthesis.

[Primary-literature boundary](../literature/2026-10-13-opposite-angle-coverage-boundary.md)
is limited and documented; no priority or unrestricted impossibility claim.
