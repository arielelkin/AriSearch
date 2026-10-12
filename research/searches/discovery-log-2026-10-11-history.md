# Superseded discovery-log snapshot: 2026-10-11

**Historical record only.** Preserved during the 2026-10-12 checkpoint.
Use [the current discovery log](../../discovery-log.md) for status and restart.
The snapshot contains obsolete running-job and review statuses, the retracted
Ammann novelty claim, and the unsupported Lemma S reduction. Its later entries
correct some earlier entries; none is an authority for current status.
It is not a proof or an instruction to resume research.

# Current research state for two convex tiles

**Problem status: unresolved.** No exact aperiodic pair or complete unrestricted
impossibility theorem meets the acceptance gates in [research-problem.md](../../research-problem.md).
**Checkpoint: 2026-10-11, resumed for user-authorized consolidation and one bounded research cycle.** The unrestricted target remains unresolved. All four-distinct Cairo pairs sharing zero or one arm length are excluded. Exactly two shared-arm pairs have a reviewed complete13-orbit/7,830-flat reduction and493 exact seam exclusions; a new full periodic cone and actual-order duals reduce136 necessary survivors to6 still-open targets. All distinct-length alternating/two-run hexagon pairs with at least one nonhomogeneous B arc are now classified into reviewed periodic escapes up to exact length swap/reflection. A full two-parameter single120 resonance slice is independently classified: tileable exactly on the periodic beta120 curve. The entire paired-qq hexagon family is now classified into the two periodic cones. The remaining pure homogeneous hexagon categories and six Cairo targets are the current bounded research obligations.
The user narrowed actual new research to two mechanisms: partial-contact
pentagons and genuinely branching repeated-length hexagons. Other work is
review, verification and preservation of completed results.

Follow [main_prompt.md](../../main_prompt.md) and [research-protocol.md](../../research-protocol.md).
Run every shell command in Conda arisearch. Rotations, reflections, partial
contacts and omission of a species remain allowed. No novelty claim is made;
[the current literature boundary](../literature/2026-10-10-search.md) and earlier
source audits record closest matches and imported classifications.

## Established structural constraints

| Result | Status and scope | Proof and review |
|---|---|---|
| Monohedral escape; exclusion of triangles and quadrilaterals; rank-two side-count inequality | Internally checked. The torus inequality does not exclude rank-one periods. | [Side-count proofs](../lemmas/side-count-and-monohedral-obstructions.md) |
| Every tileable finite convex protoset has a member with at most six sides | Fresh independent re-review VALID (2026-10-10). Includes partial contacts and T-junctions. | [Proof](../lemmas/side-count-and-monohedral-obstructions.md), [review](../reviews/global-side-count-review.md) |
| A hexagon paired with a polygon of more than six sides cannot be aperiodic | Fresh independent re-review VALID (2026-10-10). Depends on the cited unrestricted monohedral hexagon classification. | [Proof](../lemmas/hexagon-limit-and-periodicity.md), [review](../reviews/hexagon-higher-side-review.md) |
| A tileable two-hexagon pair admits an edge-to-edge, trivalent limit tiling | Defect-free limit adversarially re-reviewed after the uniform sector-disk repair. Honeycomb combinatorics and at least one-third same-type contacts follow; arbitrary periodicity does not. Fresh uniform vertex-separation re-review is valid. | [Proofs and review links](../lemmas/hexagon-limit-and-periodicity.md) |
| Pentagon curvature and relative density constraints | Reviewed. An aperiodic (5,6) pair requires positive-density subdivision or excess-valence defects. | [Proof](../lemmas/pentagon-curvature.md), [review](../reviews/pentagon-curvature-review.md) |
| Uniform density when a subfamily cannot tile | Fresh independent review VALID. Every fixed-radius disk meets the complementary types; area/count lower bounds follow. Hypothetical aperiodic two-hexagon pairs require both types at positive lower density in every admitted tiling. | [Density theorem](../lemmas/two-type-uniform-density.md), [review](../reviews/two-type-uniform-density-review.md) |
| No angle multiset summing to pi forces edge-to-edge contacts | Proved internally; repaired after hostile review; independent re-review pending. Permits higher valence. | [Proof](../lemmas/angle-nonresonance-edge-forcing.md), [review](../reviews/angle-nonresonance-review.md) |
| All angles strictly between pi/2 and pi force edge-to-edge trivalence | Proved and reviewed; excludes all-obtuse (5,5) and aperiodic (5,6) pairs. | [Proof](../lemmas/obtuse-edge-forcing.md), [review](../reviews/obtuse-edge-forcing-review.md) |
| Convex fusion transfers strong aperiodicity under explicit source/partition hypotheses | Conditional lemma proved internally; repaired after hostile review; independent re-review pending. No usable source partition certified. | [Proof](../lemmas/convex-cluster-fusion.md), [review](../reviews/convex-cluster-fusion-review.md) |
| Finite convex multitile clusters cannot occur in everywhere-trivalent edge-to-edge convex tilings | Proved internally; extended during hostile review; independent re-review pending. Fusion must use a source with combinatorial defects. | [Proof](../lemmas/convex-cluster-fusion.md), [review](../reviews/trivalent-fusion-review.md) |
| Real corner/edge frequency balance | Proved necessary conditions; repaired after hostile review; independent re-review pending. Not a global realization theorem. | [Proof](../lemmas/frequency-balance.md), [review](../reviews/frequency-balance-review.md) |

Thus the surviving side-count possibilities are a pair containing a pentagon,
or two hexagons. These constraints do not resolve either general case.

## Current mechanism registry

This is the single current route registry. Earlier round-by-round pending
entries have been replaced by the strongest saved result. Details and exact
finite domains live in the linked subject artifacts. A proved periodic witness
kills only its stated family; it never establishes periodicity of an unrelated
pair. An every-original-tiling theorem is labeled separately.

| Mechanism / current status | Strongest result and hypotheses | First remaining global obligation | Reopening condition / exact restart artifact |
| --- | --- | --- | --- |
| **Reciprocal partial-contact mirror V/V — completed reviewed milestone, selected mechanism 1** | Exact A=(a,phi*k+a/phi,a,k,k), B=(k,phi*a+k/phi,k,a,a), a,k>0,a!=k. Four actual convex motifs with six full seams and two directed interval cancellations yield a periodic tiling throughout the positive cone. Partial native contacts persist in all five ratio cases, including coalescence boundaries. Full-cone independent review is VALID;292 complete coordinate comparisons pass. | No unresolved global lemma remains in this cone. Arbitrary independently chosen mirror metrics remain unclassified and are blocked without a new necessity invariant. At a=k the same construction is monohedral. | [Theorem](../lemmas/pentagrid-v-v-reciprocal-partial-periodic.md), [VALID fresh review](../reviews/pentagrid-v-v-reciprocal-partial-periodic-review.md), [exact producer](../searches/pentagrid-v-v-reciprocal-partial-periodic.py). Reopen only changed exact data outside this cone with a new global mechanism. Periodic existence does not assert every tiling periodic. |
| **Branching repeated-length120-degree hexagons — completed reviewed milestone, selected mechanism 2** | New full 4D closed cone A=(p,a,q,p+a-c,c,q+a-c), B=(p+2(a-c),c,q+2(a-c),p+a-c,a,q+a-c), all eight values positive. A four-face periodic torus throughout the cone is independently reviewed VALID. Special p=a,q=c has a>0,0<c<3a/2,c!=a, adjacent repeats and no monohedral escape. | No unresolved global lemma remains in this full cone. Other repeated-length shapes and global extension of the second local branch are unclassified.24 complete fixture and12 local-branch comparisons independently pass. | [Full-cone theorem](../lemmas/hexagon-adjacent-repeat-periodic-cone.md), [VALID fresh review](../reviews/hexagon-adjacent-repeat-periodic-cone-fresh-review.md), [exact producer](../searches/hexagon-adjacent-repeat-periodic-cone.py). Reopen only changed exact geometry outside the cone, with a new global mechanism; longer branch words do not remove the existing periodic escape. |
| **Non-affine repeated hexagons — completed reviewed cone** | Rational3D deformation outside affine120-degree families has two actual local branches and a four-face periodic torus; full cone independently reviewed VALID. | No gap inside this cone; other repeated shapes remain. | [Theorem](../lemmas/branching-hexagon-rational-deformation.md). Existing periodic escape cannot be removed by longer branch words. |
| **Binary alternating/two-run hexagons — no-homogeneous branch complete, resonance slices active** | All0<delta<30,p!=q,Aalternating/Bpppqqq with no homogeneous stars are untileable or have direct/length-swapped positive periodic-cone escape. Complete72mixed-cover hyperplanes necessary for every member. Single120/qq-low-high fullslice tiles iff beta120 after34exact duals/14exact phase filters; whole-proof synthesis VALID. | The entire unordered paired-qq family is now VALID, including all homogeneous pp planes and both native orders. One noncentral homogeneous arc with the other nonhomogeneous arc now has a VALID complete paired-or-untileable count theorem. The central120/120 case with the other arc nonhomogeneous is now VALID, with same/cross-slot positive families derived from actual contact saturation. Both noncentral mixed homogeneous arcs are now independently excluded in both relative orders. Center/mixed and center/pure are independently classified. Pure/mixed and pure/pure categories remain open. | [No-homogeneous theorem](../lemmas/branching-hexagon-two-run-no-homogeneous-star-classification.md), [72planes](../lemmas/branching-hexagon-two-run-mixed-cover-hyperplanes.md), [single120 slice](../lemmas/branching-hexagon-two-run-single-120-complete-slice.md). No fixed frequency or original edge-to-edge rule is assumed. |
| **Fixed-B alternating hexagon transport — completed full family** | A threefold alternating(p,q), B=(r,p,q,q,q,q), all3 lengths distinct. Every tileable pair admits a period, including qq resonances. Fresh two-review audit VALID after explicit omission ledger. Required-angle multiplicity handles repeats; unique-target injection gives a saturated admitted limit, with j3periodic and j4/j5 native-parity contradictions. | No global gap inside the stated family. Other A geometries, B words or length coincidences remain. | [Full theorem](../lemmas/branching-hexagon-new-fixed-b-classification.md), [independent review](../reviews/branching-hexagon-new-fixed-b-classification-review.md), [root review](../reviews/branching-hexagon-new-fixed-b-classification-root-review.md). Reopen only changed hypotheses and a concrete new mechanism. |
| **Fixed unit Robinson U/V compiler — closed** | Proper Penrose, all regular generalized sources at the fixed slope, and the stated local matching closure exclude every mandatory V boundary independently of residual filling. All 409 generalized objects independently certified; two full U objects occur in infinite generalized sources. | Arbitrary singular selections outside the closure are unclassified. This is not unrestricted U/V untileability. | No intercept-only or additional residual search. Require exact changed cuts, macro metric/scale, slope or another used assumption plus the obstruction removed. [Closure theorem and checklist](../lemmas/pentagrid-robinson-generalized-source-gate.md), [VALID review](../reviews/pentagrid-robinson-generalized-window-review.md). |
| **General V/V central-hexagon partner — completed reviewed theorem** | Every positive V-angle pentagon has a continuum of explicitly chosen noncongruent V partners with a periodic four-face dissection. Full4-parameter positive cone and56 complete fixture comparisons pass two independent reviews. | Arbitrary independently specified V/V pairs remain unclassified. | A new necessity/compatibility mechanism, rather than another supportive example, is needed. [Theorem](../lemmas/pentagrid-v-v-general-double-y-partners.md), [fresh second review](../reviews/pentagrid-v-v-general-partner-fresh-review.md). The older mirror theorem is a subfamily. |
| **General Y periodic partner — completed reviewed theorem** | Every positive Y=(R,theta,R,theta,2pi-2theta) pentagon, pi/2<theta<3pi/4, has an explicit distinct periodic Y partner. A given pair with Q2=P0,Q4=P1 also has a periodic carrier. Reflections and partial carrier contacts included. | Arbitrary given Y/Y pairs and other equal-multiplicity words are unclassified. | Need a new necessary edge relation or different global construction. [Theorem](../lemmas/general-y-pentagon-periodic-partner.md), [fresh second review](../reviews/general-y-pentagon-partner-fresh-review.md). |
| **V/W and U/W periodic partners — completed reviewed families** | Every genuine equiangular W has a selected V partner in a full 3D metric cone. U/W has the earlier explicit b>0,0<c<phi*b cone. Each has four-face periodic coverage for every stated parameter. | Unrelated independently specified U/W or V/W pairs remain unclassified. | Exact changed compatibility data or an independent necessity argument. [General V/W](../lemmas/pentagrid-v-w-general-metric.md), [VALID fresh review](../reviews/pentagrid-v-w-general-metric-fresh-review.md), [U/W](../lemmas/pentagrid-u-w-periodic-continuum.md). |
| **Unique-private octagon chains — completed every-tiling theorem** | ANY equiangular108 P has adjacent-corner rigidity: a repeated side forces an actual reflection symmetry. Q with two nonadjacent108/six144 corners and two distinct unique lengths absent P forces a common nonzero period in EVERY original tiling, including extra Q contacts. | Other private multiplicities and broader Q data are unclassified. | Need exact changed private matching data. [Universal theorem](../lemmas/private-octagon-adjacent-corner-rigidity.md), [VALID review](../reviews/private-octagon-adjacent-rigidity-review.md). Supersedes the distinct-P good-limit proof. |
| **Equal-private octagon branches — completed reviewed restrictions** | Nonsymmetric Q3 with P=(2phi-2,phi,1,phi,2phi-2), Q=(phi^2,2phi-2,phi,phi^2,1,2phi-2,phi,phi) has a certified2Q+4P periodic torus,36 independent complete clips. An actual Q symmetry exchanging its two L slots implies every tiling periodic;12-case regular-unit closure and all actual symmetries independently reviewed VALID. | Arbitrary nonsymmetric equal-private metrics or mixed private choices remain unclassified; no every-tiling claim for Q3. | Inactive research under current portfolio. [Exact Q3 escape](../counterexamples/new-octagon-q3-equal-private-periodic.md), [VALID independent review](../reviews/octagon-q3-equal-private-periodic-review.md), [symmetry theorem](../lemmas/private-octagon-equal-private-symmetric-periodicity.md), [VALID review](../reviews/private-octagon-equal-private-symmetric-review.md). |
| **All-obtuse internally distinct(5,n) — completed restricted exclusion** | n>=8 untileable; n7 has a four-face periodic witness. New direct theorem proves a nonzero period in EVERY original tiling using two selected Q-private midpoint chains and unique P corners, without counting limits or graph enumeration. | Repeated native lengths or nonobtuse angles remain outside. | Exact changed metric coincidences/contact data. [General theorem](../lemmas/distinct-length-obtuse-pentagon-higher.md), [direct strengthening](../lemmas/distinct-length-obtuse-direct-common-period.md), both reviewed VALID. |
| **Two-angle(5,7) metric family — completed reviewed restrictions** | alpha4pi/7,beta5pi/7: full 4D positive cone has periodic coverage, even with coincidences. Internally distinct P/H implies EVERY original tiling periodic for all shared orders. Equal-private H=(L,a,L,b,c,d,e), five-distinct P, reduces to a complete2D positive cone with a periodic escape throughout. | Other repeated lengths/positions remain unclassified. | No longer private-chain words in the closed cone. Need exact changed coincidence pattern. [Full theorem](../lemmas/two-angle-5-7-metric-continuum.md), [VALID second review](../reviews/two-angle-5-7-metric-continuum-second-review.md), [equal-private theorem](../lemmas/two-angle-5-7-equal-private-scaffold.md), [VALID review](../reviews/two-angle-5-7-equal-private-scaffold-review.md). |
| **Regular higher-polygon partners — completed all-obtuse classification** | Strictly obtuse P with regular Q: n7 exact periodic family, n12 exact2D periodic family; other n>=7 excluded by reviewed angle/contact counts. Regular-Q7/four-alpha-one-beta is untileable. | Irregular Q or nonobtuse P remain outside. | Changed exact angle/metric data, not the same regular family. [Q7](../lemmas/all-obtuse-pentagon-regular-heptagon-classification.md), [Q12](../lemmas/all-obtuse-pentagon-regular-dodecagon-classification.md), [n>=13](../lemmas/all-obtuse-pentagon-regular-large-polygon-obstruction.md), all reviewed. |
| **Pentagrid angular/metric reduction — reviewed necessary constraints** |101 words/13 classes leave U,V,W; ALL U/U metrics are untileable with unrestricted partial contacts. Conditional Rao filter: U/W monohedrally untileable; V mono iff L2=L4 or L3=L0 in the after-side convention. U/V,U/W,V/V,V/W general metric pairs remain open. | Unrestricted geometric forcing for surviving pairs. | New metric/contact invariant. [Two-U proof](../lemmas/pentagrid-two-asymmetric-u-obstruction.md), [angular reduction](../lemmas/pentagrid-pentagon-angular-reduction.md), [explicit Rao dependency](../lemmas/pentagrid-pentagon-monohedral-filter.md). |
| **Area-compatible U/V partial-contact family — inactive; global mechanism blocked** | U=(phi^2*b+phi*c twice,b,c,b), V=(b,2phi*b+phi^2*c,b,phi*(b+c) twice), b,c>0, closed/convex and areaV=phi*areaU. EVERY metric lacks an ETE tiling. If c/b outside Q(sqrt5), no homothetic U/V substitution exists; inside, scale lies in Z[phi]. | Nonhomothetic infinite existence and unrestricted forcing lack a concrete mechanism. | New nonhomothetic mechanism or exact changed family; no larger old substitution search. [Area/source record](../searches/pentagrid-golden-metric-area-compatible.md), [ETE obstruction](../lemmas/pentagrid-area-family-edge-obstruction.md), [unbounded substitution theorem](../lemmas/pentagrid-generic-metric-substitution-obstruction.md). Old phi^3 trial was UNKNOWN at120.205638s, never UNSAT. |
| **Cairo/right-angle partial contacts — generic, monohedral, zero/one-sharing complete; exact two-sharing reduction reviewed** | Complete738generic patterns and monohedral classification. All zero/one-sharing metrics excluded, across every event resonance. Exact two-sharing:72patterns/13orbits,7,830flats,629necessary local strata,493exact seam duals; new reversed-right-pair fullperiodic cone removes one of136 relaxed primals. Known swapped/Y cones remain periodic throughout. |6 necessary targets remain (3 dimension2,3 dimension1; flat239 restricted to its low-ratio subcone), with additional reviewed order restrictions. All four dimension3 parents have reviewed periodic escapes. Internally repeated pairs and three/four shared-arm nongeneric metrics remain outside these complete reductions. | [Zero/one master](../lemmas/partial-contact-cairo-one-shared-classification.md), [two-cross reduction](../lemmas/partial-contact-cairo-two-cross-native-reduction.md), [new periodic cone](../lemmas/partial-contact-cairo-reversed-right-pair-periodic.md), [fresh flat audit](../reviews/partial-contact-cairo-two-cross-event-flats-review.md). No primal implies existence. |
| **Three-angle multiplicity and irrational witness — completed audit** | Different multiplicity rows for three combined angle values force rational angles. Equal rows admit periodic irrational theta/pi with cos(theta)=-2/5. Scaling the independently checked witness by sqrt2 gives private lengths sqrt2,sqrt10, both irrational and irrational ratio.52/48/48 complete comparisons pass. | Other equal-row metric pairs and four-angle families remain outside. | Exact changed compatibility data. [Rationality lemma](../lemmas/three-angle-pentagon-multiplicity-rationality.md), [witness](../lemmas/new-angle-three-pentagon-private-length-counterexample.md), [VALID review](../reviews/new-angle-three-pentagon-periodic-review.md). Mixed X/Y finite ansatz967680 cases/8models is exhausted infeasible, not a full X/Y classification. |
| **Distinct/five-length hexagon graph selection — completed restricted exclusions** | Both internally distinct hexagons admit a periodic torus if tileable. Five-symbol/separation2 repeats: <=2 shared untileable,3 shared periodic; one private-repeat six-symbol order has periodic escape in both generic/doubled-angle cases. Unique complete intrinsic neighbors force a crystallographic group, conditionally. | Other repeated orders and genuinely branching physical neighbors remain outside determinism. | Exact changed repeated order with positive closure and two-ended contacts. [Distinct theorem](../lemmas/hexagon-holonomy-distinct-lengths.md), [sparse repeats](../lemmas/hexagon-five-length-sparse-sharing.md), [private repeats](../lemmas/hexagon-five-length-private-repeat-periodicity.md), [conditional determinism](../lemmas/hexagon-five-length-intrinsic-determinism.md), all reviewed. |
| **Equilateral rational-angle root classification — completed restricted exclusions** | Rational-angle equilateral(5,5),(5,6) cannot be aperiodic even at different scales. Two equilateral rational-angle hexagons are untileable or have a monohedral/three-face periodic escape. Imported root-sum theorem explicit. | Irrational-angle equilateral hexagons outside root classification. | Changed angle hypothesis and concrete geometry; denominator/scale enlargement does not repair closed cases. [Pentagons](../lemmas/new-angle-equilateral-rational-obstruction.md), [hexagons](../lemmas/new-angle-two-equilateral-hexagons.md), both reviewed. |
| **Affine-mirror repeated hexagons — completed periodic counterexample** | Two repeated-length irrational-angle noncentral hexagons have an exact periodic escape, with no monohedral escape; an affine image of mirror shapes needs a commuting affine map to keep exactly two classes. | General branching non-affine family remains outside. | New non-affine contact data. [Exact theorem/witness](../lemmas/hexagon-affine-mirror-periodic-escape.md), [VALID review](../reviews/hexagon-affine-mirror-escape-review.md). |
| **Convex source fusion/Ammann — blocked** | Conditional fusion lemma and exact coordinate reconstruction retained. Trivalent ETE sources cannot support finite convex multitile fusion. Aggregate H:P=1:2phi is conditional; species split and unrestricted forcing unproved. | Certified strongly aperiodic source, all exact tiles and a global convex two-class partition are missing. | New source or exact primary forcing and partition data. [Audit](../reviews/ammann-convex-source-audit.md), [coordinates](../lemmas/ammann-coordinate-parameterization.md), [fusion](../lemmas/convex-cluster-fusion.md). |
| **Walton two-hexagon rule compiler — falsified recorded family** | Natural transcription and all24 relabelings collapse to regular hexagons;4094 state assignments leave4 angular branches, all fail equilateral closure. The one-block obstruction is narrower than the general target. | A different certified geometry compiler and shape-only global forcing are missing. | New source, extendible strict sublanguage or neighborhood-dependent geometry. [Exact domain](../searches/walton-encoding-reconnaissance.md), [one-block lemma](../lemmas/walton-one-block-obstruction.md). Do not repeat completed assignments. |
| **Nonresonant(5,6) scaffolds — falsified exact candidates** | Both recorded exact pairs are untileable. Original full-edge stars omit required corners; joint pair's94 ordered/chiral endpoint cases reduce12 then0. | No survivor exists in the recorded fixed data. | Change side/angle partition and apply cheap two-endpoint filters before global work. [Original](../searches/nonresonant-5-6-angle-scaffold.md), [joint](../searches/joint-5-6-synthesis.md), [endpoint review](../reviews/joint-5-6-two-ended-review.md). |

## Current hexagon obligation ledger

For B with native side word `pppqqq`, use four arc categories: N has no legal
homogeneous triple; C has both native angles120; P has one120 angle and one
other angle; M has a noncentral mixed2+1 homogeneous triple. The four
homogeneous lines intersect only at C. Distinct p,q and `0<delta<30` remain
explicit hypotheses. Reflection may swap both native arc orders; exchanging
length names requires the reviewed A normalization and never changes the
aperiodicity definition.

| Domain | Strongest current result | Exact artifact / remaining obligation |
| --- | --- | --- |
| At least one N arc | Every tileable member has a reviewed periodic escape | [No-homogeneous](../lemmas/branching-hexagon-two-run-no-homogeneous-star-classification.md), [one-noncentral](../lemmas/branching-hexagon-two-run-one-noncentral-homogeneous-arc.md), [center/N necessity](../lemmas/branching-hexagon-two-run-pp-center-no-qq-homogeneous-classification.md) |
| M/M, both relative native orders | Untileable; forward and complete reverse obstruction independently VALID | [Forward](../lemmas/two-homogeneous-forward-mixed-arcs-obstruction.md), [complete reverse](../lemmas/two-homogeneous-opposite-mixed-arcs-full-obstruction.md), [fresh whole reverse review](../reviews/two-homogeneous-opposite-mixed-arcs-full-obstruction-review.md) |
| C/M, up to length normalization | Complete periodic-escape classification, independently VALID | [Center/mixed](../lemmas/two-homogeneous-center-mixed-qq-classification.md) |
| C/P, up to length normalization | Complete periodic-escape classification, independently VALID | [Center/pure](../lemmas/two-homogeneous-center-pure-qq-classification.md), [fresh whole-proof review](../reviews/two-homogeneous-center-pure-qq-classification-review.md); all four phase/domain/native-metric transfers checked |
| C/C | Closure requires p=q, outside distinct-binary scope | Both equal120 arcs have unit chain norm2; closed positive p and q chains therefore require2p=2q |
| P/M and P/P | OPEN; no actual necessity/realization theorem retained | Both-end native contacts, allowable AA seams and actual phase must be handled. Old no-qq-homogeneity exclusion and center-slot arguments do not apply |

The [same-slot](../lemmas/branching-hexagon-two-run-pp-center-periodic-family.md)
and [cross-slot](../lemmas/branching-hexagon-two-run-pp-center-cross-periodic-family.md)
positive carriers are independently VALID on their full exact domains, both
admissible quadratic branches and their coalescence. They provide sufficiency,
not arbitrary-pair necessity. Equal lengths and arbitrary A remain outside the
negative binary-family classifications. No whole parent-family closure or
unrestricted impossibility theorem is claimed.

## Current Cairo obligation ledger

[The native master reduction](../lemmas/partial-contact-cairo-two-cross-native-reduction.md)
retains the complete72-pattern/13-orbit/7830-flat domain and493 exact seam
exclusions. Actual-order refinements and native Euclidean carriers replace
local feasible balances by reviewed periodic witnesses where proved. The
[seven-target signed native map](../lemmas/partial-contact-cairo-mixed-quotient-seven-stratum-reduction.md)
is independently VALID. The [ray459 theorem](../lemmas/partial-contact-cairo-mixed-quotient-fixed-ray459-periodic.md)
now has a fresh full native-geometry/links/holonomy/coverage VALID review.
[The six-target synthesis](../lemmas/partial-contact-cairo-mixed-quotient-six-stratum-reduction.md)
removes that entire1D ray and is independently VALID after its separate synthesis review.

The conservative necessary residual targets are:

- dimension2: separated46, separated49, orbit6 flat239 only on
  `sqrt(3)*a/4 < b < a/sqrt(3)` with a=Pa,b=Pb;
- dimension1: orbit1 flat759, orbit6 flat906, orbit7 flat575.

All original positive/private active-event and actual-order domains remain
in force. Internally repeated arms and three/four shared-arm coincidences are
outside this full two-sharing reduction. No remaining primal establishes
tilability. No claim is made that every original tiling of a killed metric
is periodic; one admitted periodic witness suffices to kill aperiodicity.

Preserved bounded negatives: ray759 selected10-face proposal reached its
1,000,000-node cap; ray575 selected8-face proposal exhausted909,775 nodes;
ray906 selected10-face proposal exhausted8,995 nodes; low239 selected20-face
proposal reached its2,000,000-node cap. These are finite-model results only,
not unrestricted untileability. Exact domains and certificates remain in
[the native search](../searches/partial-contact-cairo-mixed-quotient-native-search.py)
and corresponding subject records. Full residual-color models retained only
necessary primals. Further quotient-size or balance-model expansion is blocked
without a new geometric constraint or proved finite-model property.

## Dependency gates and closed-route restart rules

Retain the status in the structural table above. Repaired angle-nonresonance,
convex fusion/trivalent fusion and real frequency balance are not silently
promoted by successful finite replays. Intrinsic deterministic-state arguments
require their explicitly stated neighbor uniqueness; their repaired review
obligation is not replaced by broader periodic examples.

The fixed-unit Robinson source compiler remains closed inside the regular
fixed-slope/local-matching boundary. Its generalized audit covered409 objects,
with all mandatory V boundaries excluded; singular selections outside that
boundary are unclassified. Reopen only changed exact cuts, scale, slope or
another used assumption that removes the actual obstruction; do not rerun
intercept/residual filling searches. [Source gate and checklist](../lemmas/pentagrid-robinson-generalized-source-gate.md).

Arbitrary V/V and Y/Y compatibility needs a new necessity invariant; selected
periodic partners are not arbitrary-pair classification. Area-compatible U/V
nonhomothetic existence and forcing remain blocked; the retained phi3 SMT
trial was UNKNOWN at120.205638s, never UNSAT. [Exact trial](../searches/pentagrid-golden-metric-phi3-macro.md).
Convex fusion/Ammann needs a certified source, two-class convex partition and
unrestricted forcing; [source audit](../reviews/ammann-convex-source-audit.md).

## Consolidation and verification (2026-10-11)

The current restart index replaces the long chronological log; subject proofs,
counterexamples, computation records and certificates remain retained. Status
corrections require explicit review provenance. Historical progression is not
used as mathematical evidence. [Preservation snapshot](../searches/consolidation-2026-10-11-inventory.json)
retains file hashes/sizes, Git index digest and status inventory at its stated
concurrent snapshot. Existing index changes are preserved: root has not
staged, committed or pushed during this cycle. The earlier prepared319-path
checkpoint is not a new commit or a final mathematical report.

Six targeted existing carrier/count/necessity checkers passed this cycle;
the new complete reverse and reverse-phase checkers passed through the
nondestructive runner. Ray459 registered replay passed. The consolidation
snapshot parsed276 Python sources, found all43 registered producer/certificate
pairs and131 verifier paths, and found no missing Markdown targets;
`git diff --check` passed at that snapshot. Counts are not the final-cycle
portfolio, and syntax/path checks are not mathematical evidence.

    conda run --no-capture-output -n arisearch python research/searches/verify.py

Use repeated `--only SCRIPT` for dependency-affected replay; certificate writes
require explicit author `--output`. Do not disable assertions. No full historical
suite rerun is claimed from targeted passes. Final-cycle check counts and baseline certificate/index preservation are
recorded below and in the inventory artifact.

[Current narrow primary-source boundary](../literature/2026-10-11-search.md)
and [earlier source boundary](../literature/2026-10-10-search.md) retain
exact queries, sections and imported theorem scope. No novelty claim is made.

## Bounded cycle authorization and acceptance test

The user resumed the prior explicit pause on2026-10-11 and authorized
consolidation followed by one bounded research cycle. The cycle consists of
one necessity/geometry synthesis pass and one fresh independent review/repair
round on the selected routes. Construction, audit and root integration have
separate file ownership; every shell command uses Conda arisearch.

The test distinguishes closure of the entire selected A(delta)/Bpppqqq or
Cairo domain from closure of an exact subfamily. New reviewed slices and
witnesses are retained partial progress. If neither parent route closes nor
a new global forcing mechanism survives, record exact blockers and suggest
substantially different mechanisms with concrete first falsification tests.
No larger capped quotient search, repeated feasible local balance or renamed
theorem-strength gap counts as success. This explicit bounded authorization
is the stopping boundary; elapsed time or difficulty alone is not a limit.

Current pass: center/pure synthesis and full reverse/ray459 audits are independently VALID.
The Cairo geometric first-corona pass is complete and independently VALID
within its stated finite scope: all391 variants have relaxed exact neighbor
assignments, with no new exclusion. Fixed-ray feasibility scales; the three
dimension2 outcomes are exact fixtures only.
[Experiment and exact domains](../searches/partial-contact-cairo-first-corona-geometry.md),
[fresh finite review](../reviews/partial-contact-cairo-first-corona-geometry-review.md).
Neither feasibility nor a finite collar is a plane-extension proof.

**Cycle complete: neither selected parent family closed, and no new global
forcing mechanism for the residual cases emerged.** The user-authorized bound
is reached after the one synthesis pass and fresh review round; no resource
exhaustion or mathematical impossibility is inferred. Scoped results remain
retained. The parent gaps above are blocked with the current methods and must
not receive another larger local-balance/quotient search without a materially
new actual invariant or construction.

[Mechanism reset and exact next falsification gates](../reviews/bounded-cycle-mechanism-reset.md)
proposes three different directions: rank1 strip construction; actual Euclidean
cycle transport beyond marginal balance; and direct inverse design of a
recognizable expansive hierarchy using acute pentagons/T-junctions outside
the current templates. These are suggestions, not executed extra cycles or
proved theorems. No final mathematical report exists; the unrestricted target
remains unresolved.

## Final preservation and replay checkpoint

All twelve targeted registered checks passed this cycle, including the new
reverse phase/full count, ray459, center/pure and two first-corona checks.
The full historical suite was not rerun. Final syntax/path/link consistency
checks pass 280 research Python sources, 137 registered verifier paths and
43 registered producer/certificate pairs; `git diff --check` passes. All
182 baseline certificates have unchanged SHA256 hashes; the 381 pre-existing
index entries remain byte-for-byte identical as the recorded Git index
manifest. Seven newly retained first-corona certificates are additional
evidence with finite-only scope. No index, commit or push mutation occurred.
All delegated work and bounded searches are complete; no extra research round
is pending. Dormant repaired review gates retain their status above.

## Open-ended cycle (2026-10-11, user-authorized; in progress)

The user authorized continuing until an impossibility proof or a new
construction, with subagents, prioritizing the lowest-hanging route.
Slice classification of the residual hexagon/Cairo families is paused: even
complete closure is a restricted-family exclusion, a stated non-result.

Portfolio (independent; root integrates; agents own disjoint `research/` files):

1. **Ammann two-class collapse (construction, lead route).** Reconstruct the
   Penrose-rhomb recomposition into two convex pentagons and a hexagon
   exactly, as a function of its free interior point J and circle branches.
   Find every parameter where the set collapses to two congruence classes
   (mirror images identified), including hexagon straight-angle degeneration.
   Forcing for all tilings is a separate later gate.
2. **Literature/verification.** Ammann convex set status and reflections;
   post-2024 two-convex results; Grunbaum-Shephard one-translation theorem.
3. **Global two-hexagon impossibility.** Use the reviewed edge-to-edge
   trivalent limit (honeycomb combinatorics) for a whole-class argument, not
   word-by-word classification.
4. **Convex two-tile substitution design (falsification first).** Seek an
   exact self-similar dissection of a pentagon/hexagon pair with irrational
   inflation; kill immediately by periodic-torus or monohedral escape.

### Checkpoint 2026-10-11 19:25 UTC (session resumed; no jobs relaunched)

Two-hexagon route: [SFT encoding lemma](../lemmas/two-hexagon-global-sft-encoding.md)
(not yet independently reviewed) reduces the (6,6) case to finitely many
vertex-star SFTs X(T,~) and gives a sound covering certificate (Theorem 3).
Generic partition-strata census (`two-hexagon-global-stratum.py partitions
3 6 8`) is COMPLETE over its stated domain: all 100 classes UNSAT, 0
candidates, 101 tori. Scope: only types whose angle set T is the closure of
a 4-block corner partition; non-generic flats are not covered. The census
record and retained tori are still in scratch and must be moved under
`research/` with an independent check before use. Covering-flat
enumeration (`two-hexagon-global-flats.py 3`) is running: ranks 1-2 done
(11 and 504 flats; 0 and 6 covering), rank 3 in progress. The interrupted
agents were resumed with their saved context.

### Ammann three-to-two collapse — falsified within stated domain (2026-10-11)

[Reconstruction](../lemmas/ammann-two-class-reconstruction.md) of
Ammann's Penrose recomposition: K, L are forced (no real circle branch);
tiles H6=[0,J',1,J,w,J''], P1=[0,J',1,L,K], P2=[K,L,1+w^2,J2,w^2] over
Q(zeta10) with J=s+tw. Exact collapse classification
([record](../searches/ammann-two-class-search.md)): the only two-class
point in the admissible region is J = circumcentre of BCD
(s=t=(5+sqrt5)/10), where P1=P2 but H6 is equilateral and centrally
symmetric, so it tiles alone by translations: **Falsified**. Root
independently re-checked that point exactly
([check](../reviews/verify_ammann_two_class_collapse_point_root.sage)).
Generalized decorations (<=2 interior points per arrow-marked rhomb, 9604
rhomb pairs, Robinson half-rhombs with <=1 point) give no other convex
two-class point. Not covered: more points, points on rhomb edges,
neighbour-dependent decorations, kite/dart sources, other aperiodic sources.
Status: computational evidence with exact decisions; completeness of the
"only collapse point" claim awaits independent hostile review.

### Literature boundary update (2026-10-11)

[Boundary record](../literature/2026-10-11-convex-aperiodic-boundary.md):
no aperiodic set of unmarked convex polygons of ANY size has a located
proof. Ammann's three convex tiles (Tilings and Patterns §10.3,
Fig. 10.3.28, pp. 547-548) are asserted without proof; by the book's
conventions reflections are implicitly allowed. No two-convex construction or
impossibility proof found; undecidability results (Demaine-Langerman,
Stade, Yang-Zhang) use non-convex tiles. Grunbaum-Shephard Statement 3.7.1
(one translation implies a periodic tiling) is proved only for
EDGE-TO-EDGE polygon tilings; the general case is an exercise and treated
as open by Klee-Wagon. Consequence: outside edge-to-edge settings, an
aperiodicity proof must exclude singly periodic tilings directly, and a
singly periodic witness is a genuinely weaker kill (this corrects the root's
earlier objection to the reset note's strip proposal). Within the
two-hexagon route the edge-to-edge limit makes 3.7.1 applicable.

New stepping-stone route: **forcing for Ammann's three convex tiles** with
reflections and partial contacts. A proof would be the first rigorous convex
aperiodic set and supplies the forcing method any two-tile construction needs.

### Route decisions (2026-10-11 ~19:55 UTC)

| Route | Decision |
|---|---|
| Cairo pentagons, binary hexagon slices | Paused unless a new geometric invariant appears. |
| Ammann three-to-two collapse | Closed on its recorded domain. Hat/spectre/other-source decoration enlargement stopped (no specific justification; does not address forcing); partial work recorded in `research/searches/source-decoration-search.md`. |
| Convex substitution search | No candidate passed the exact dissection gate ([record](../searches/convex-substitution-search.md)). No further alphabet enlargement; reopen only for a new angle system or a parametric mechanism with a concrete first gate. |
| Global two-hexagon analysis | Lead route. [Census](../lemmas/two-hexagon-global-census.md) closes the 100 generic partition strata (internal, unreviewed). Gates: independent hostile review (running) and explicit coverage. Flats rank<=3 enumerated: 11 / 504 / 26,858 flats; 0 / 6 / 310 cover all corners. Ranks >=4 unenumerated. |
| Ammann three-tile forcing | Stepping stone, running: decide whether Ammann's three convex tiles force aperiodicity with reflections and partial contacts. |

### Ammann three-tile forcing — internally proved, under hostile review (2026-10-11)

[Lemma](../lemmas/ammann-forcing-aperiodicity.md) (computer-assisted,
exact): for every strictly convex J with (G1) a,b,r,c pairwise distinct and
(G2) 1, chi/pi, psi/pi, kappa/pi Q-independent (explicit certified points
include J0 = 1/2 + (4/5)w), Ammann's three unmarked convex tiles admit
tilings, every tiling is edge-to-edge (no angle combination sums to 180 deg),
uses one handedness, has vertex stars among 14 types (74 combinations to
360 deg, 162 edge-compatible stars, far-endpoint pruning), reconstructs to an
arrow-legal Penrose rhomb tiling, and has no nonzero translation (unique
composition proved directly: 8 stars, 85 patches, 564 parent cases). One
unintended P1-P1 c-edge contact dies one edge away (hand argument).
Status: **Proved internally; not yet reviewed.** Two independent hostile
reviews running (local geometry; reconstruction/Penrose composition).
Non-generic J open. Root float triage at J0 (reconnaissance only): 11
distinct angles, no multiset summing to 180, six summing to 360.
If it survives review this is, within the literature boundary, the first
proved aperiodic set of unmarked convex polygons. It has three tiles and does
not resolve the two-tile target.

### Convex substitution — closed (2026-10-11)

[Final record](../searches/convex-substitution-search.md): no pair
passed the exact homothetic dissection gate. Families killed: (6,6) and
(6,n>=7) by a dissection Euler identity; lambda=phi; pi/4 angles; pi/5 words
except U,V,W; the golden b=c U/V pair for all lambda (corner test); the
repo's phi^3 5U+8V question (5-node exhaustion; previously a Z3 timeout);
bounded Z[phi] U/V/W alphabets. Unfinished and not claimed: the
pentagon-hexagon corner classification, pi/6 pentagon-hexagon runs. Proposed
only: a parametric-length corner LP over Q(w). Internal; not reviewed.
Local review ([record](../reviews/ammann-forcing-local-review.md)):
L1-L5 VALID at all five listed points (74/162/14 reproduced independently,
exact; single handedness global). Defects: D1 major statement defect — the
(G2) exceptional set is dense (chi/pi rational on a dense set), so "locally
finite union of curves" is false; repair: replace (G2) by (G2'): no 180/360
relation among corner angles has nonzero chi, psi, kappa coefficients. D2
float multiplicity bound (exact repair in reviewer checker); D3 undocumented
CP-SAT/point cross-checks; D4 valuation matrix stored only for J0. Repairs
pending with the author after the reconstruction review; repaired statement
needs a fresh independent re-review.
Reconstruction review ([record](../reviews/ammann-forcing-reconstruction-review.md)):
R1 regrouping, R2 unique composition/no translations, R3 existence all VALID
(independent brute-force parents 564/564, exact non-overlap of 85 patches,
closure at scale phi, 2-SAT pentagrid test identifies the arrow set with
Penrose's computationally). Minor defects: Lemma 6 twin-role case, missing
whole-plane existence of a legal rhomb tiling, an identification overclaim,
an unexplained orientation fact in Lemma 5. All eight repairs sent to the
author; the repaired lemma then needs a fresh independent re-review.

### Novelty revision and Ammann reclassification (2026-10-11)

User-supplied benchmarks (see the
[literature correction](../literature/2026-10-11-convex-aperiodic-boundary.md)):
Healey, RHUMJ 12(2) (2011), Thm 4.5 / Cor 4.7 already proves Ammann's three
convex tiles aperiodic (MLD with Penrose; complete-edge convention, length-
only allowability, reflections not discussed). Ammann-Grunbaum-Shephard,
DCG 8 (1992) is the rigorous composition-technique benchmark (reflections
included) for A2-A5. **Retracted:** every earlier statement in this log that
the repo's Ammann proof would be "the first proved aperiodic set of unmarked
convex polygons". The three-tile theorem is **not a research objective**.
The repo lemma is retained only as an exact verification and strengthening
of Healey: no edge-to-edge convention, explicit reflections, exact atlas,
explicit genericity on G* = D ∩ (G1) ∩ (G2'). Its (G2') exceptional set is a
locally finite union of curves; the dense set is where the stronger (G2)
fails. Both review-defect lists are repaired; a narrow independent
re-review of the repairs is running. Root replay: composition certificate
identical; angles certificate substantively identical (74 relations, 162
stars, 142+6 pruned, 14 viable), with witness representatives varying run to
run (reproducibility remark only).

[Mechanism survival analysis](../reviews/ammann-mechanism-two-shape-survival.md):
these layers are independent of the number of shapes and survive with two
convex shapes:

* source unique composition;
* length coding;
* angle-genericity edge forcing;
* atlas pruning;
* inverse derivation;
* handedness.

What must change is the shape economy. Collapsing face orbits by congruence
spends the free parameters genericity needs (C1). AGS-style self-similar
composition and notch markings are unavailable to convex tiles. Lemma S
(root, unreviewed): a per-rhomb Penrose decoration with one face per rhomb
and strictly convex faces yields only quadrilaterals or trivalent hexagons.
That sub-route therefore lies inside the two-hexagon census.
Ammann verification documentation complete: [repair re-review](../reviews/ammann-forcing-repair-rereview.md)
VALID on G* (all eight repairs); wording points W1-W3 applied by root; the
angles script is now deterministic and its regenerated certificate is
byte-identical across hash seeds and equal in content to the previous one;
patch check passes. Lemma status: **Adversarially reviewed**, as a
verification/strengthening of Healey 2011 (not a discovery; the parameter
range is narrower than Healey's).

### Kite/dart recomposition campaign (started 2026-10-11, user-approved)

Best current construction bet. Topology-led recompositions of Penrose
kite/dart tilings, then (only if exhausted) rhomb recompositions with segment
endpoints inside source edges. Gates, in order:

1. final tiles cross and erase source boundaries;
2. the domain is new relative to the 9,604 exhausted rhomb decorations;
3. two shapes by construction (shared congruence rules; merging along a
   curve allowed);
4. a parameter that changes angles, with strict convexity on an open set
   and the identical angle relations computed exactly;
5. periodic escapes first (each shape alone, then mixed tori).

Only survivors get vertex-star analysis and source reconstruction. Forcing
(every tiling recovers the source, with reflections and partial contacts)
remains the decisive obligation; existence alone is not a result.


### Kite/dart recomposition campaign — first bounded phase completed (2026-10-11)

User authorized this agent to take over after the other agent exhausted its
context. The prior campaign was only a log entry: no P2 search script,
checkpoint, or running P2 job existed. Separate two-hexagon jobs were left
alone. All commands below run through the `arisearch` Conda environment.

[Campaign manifest](../certificates/penrose-kite-dart-campaign.json)
retains exact domain, versions, script hashes, replay/resume commands and
remaining gaps. Source builder:
`research/searches/penrose-kite-dart-patch.py`, using Lang--Hayes (2013)
equation (1) and Figure 3; reference shapes [0,1,w,w^2] (kite) and
[0,1,w/phi,w^2] (dart). Exact source patches: 95 tiles at P2 deflation 3,
265 at deflation 4. A numerical number-field `abs` in the initial area
check was corrected to exact algebraic-sign normalization; corrected
patch3 replay is byte-identical. No proof relies on the numerical check.

New finite domain: the 98 abstract plane-graph decorations independently
on each labelled kite/dart, <=2 distinct strictly interior nodes, spokes,
PQ and source diagonals, all source edges erased; 9,604 pairs. Abstract
embeddings are a geometric superset, particularly on the nonconvex dart.
Screen completed: 8,096 triangle/quadrilateral escapes, 832 slit faces,
364 pinches, 277 multiple boundary cycles, 17 fixed reflex corners; 18
remaining rows. Four have no bounded interior face: (0,0), (0,54), (0,1),
(0,3), on BOTH retained patch sizes. These four are NOT classified globally.
The other 14 have 4--7 generic classes; none has two identically for free
independent point coordinates. Larger-patch replay adds a fifth class to
(15,0)/(27,0), illustrating why finite patch class lists are lower bounds.

Congruence checks do not stop at generic class counts. All cyclic shifts
and reflections, initially w^k rotations, then arbitrary rotations through
full squared-distance polynomials over Q(sqrt(5)). Metric pass: 660 options
completed. Necessary strict-convexity conditions leave only (15,27) and
(27,15), each seven pentagons. Their 128 partitions into <=2 blocks were
checked jointly by exact Groebner bases, with positive dimension, nonzero
edges, distinct nodes and fixed-source-interior pruning. No admissible
positive-dimensional locus remains. Zero-dimensional loci are outside
this free-parameter campaign and were not classified fully.

Straight-vertex cases were checked with weak turns, positive areas,
nonzero edges, strictly interior source points and >=5 genuine corners
(otherwise a convex tile gives a monohedral periodic escape). The only
remaining hexagon patterns are (1,3)/(3,1). Each has three forced flat
turns, a polynomial and its negative among the required nonnegative turns.
For (3,1), zero-turn pattern enumeration completed, with one realizable
necessary-condition cell and no positive-dimensional two-class locus.
The direct (1,3) enumeration timed out after one cell, recorded as
incomplete. An exact involution s_j -> -s_j,
t_j -> phi*s_j+t_j (z_j -> w^2 conjugate(z_j)) preserves both source
polygons and bijects all five full face-distance matrices. Thus the
completed mirror case transfers its negative result. Certificate:
`research/certificates/penrose-kite-dart-flat-mirror-map.json`.
Pentagon straight-vertex cases reduce to <=4 genuine corners and die by
the monohedral gate. Other bounded-face survivors fail necessary weak
convexity with strict source-interior constraints; timeout records are
retained separately from successful stronger/weak checks.

Status: **computational evidence, not independently adversarially reviewed**.
No free-angle two-shape candidate was found in the checked bounded-face
branches. No candidate reached the remaining monohedral/mixed-torus or
shape-only reconstruction tests. This does NOT exclude the entire P2
recomposition route or solve the main problem.

Encoding controls (`research/reviews/verify_penrose_kite_dart_recomposition.py`):
360 exact source frames, 1,960 full symbolic distance identities against
independent conjugate-product expressions over Q(w), 200 exact algebraic
sign controls, full 9,604 checkpoint coverage and the mirror transfer.
These controls are not an independent review of exhaustive enumeration or
ideal pruning. The retained SMT formulas make all solver claims replayable;
UNSAT proof certificates are not provided.

Restart obligations: classify the four no-bounded-face templates; audit
this finite-domain exclusion independently. Next construction enlargement
should introduce matched endpoints inside source edges with a small shared
parameter family, rather than unrestricted extra interior nodes. Edge
endpoints, neighbour dependence, >2 points and full shape-only forcing
remain outside the completed phase. All P2 jobs launched here finished;
check process state before resuming any checkpoint.


### Matched-endpoint P2 attachments — bounded exclusions (2026-10-11)

[Edge campaign](../certificates/penrose-kite-dart-edge-campaign.json)
records exact domains, commands, hashes and limits. One-centre stars: all706
recipes checked;522 small-polygon periodic escapes,181 slits,1 holed face,
2 remaining recipes. Both fail weak convexity even without a minimum-corner
requirement, with strict source-interior points and nonzero edges. Independent
rotation-system face tracing agrees with both136-face source-piece quotients;
495 shared edge-endpoint instances match exactly and patch3/4 edge constraints
agree. These are encoding controls, not solver proof certificates.

At a degree-two internal endpoint convexity forces the two segments to be
straight through it. The subsequent bounded enlargement adds at most one
endpoint-to-nonadjacent-corner chord per source type, lying in one fan face.
Centre degree remains >=3. Each single active orbit has35 local types/source,
including15 unchorded, hence35^2-15^2=1000 new pairs;2,000 total. Activating
all four endpoints leaves no eligible single chord, so adds no recipes.
All2,000 completed in27s:1,262 triangle/quadrilateral escapes,604 slits,
34 multiple boundary cycles,100 degenerate faces after conditional interior
degree-two deletion. No survivors. Chord screening has not yet had independent
review; this is a bounded-domain computational result, not an exclusion of
arbitrary boundary attachments.

User now prioritizes (1) audit/repair the hexagon reduction and exact census
scope, (2) finish original P2 exclusion audit and four no-bounded-face templates,
then (3) specify a small exactly-two-shape angle-varying attachment family and
apply periodic escapes before reconstruction. User explicitly authorized
subagents. Three reviewers/preparers active; no further enlarged enumeration
will start before the audits clear it. Restart paths are the edge campaign,
original P2 campaign, two-hexagon encoding/census and new audit artifacts.


### Completed audit priorities and exact restart scope (2026-10-11)

User authorized three subagents; work was divided into hexagon reduction/census,
original P2 exclusion audit, and preparation of a small two-shape attachment
family. Construction execution waited for the audits. Crossreviews were then
assigned to different authors; root integrates manifests and preserves the
restart state. This section supersedes earlier open-template and unreviewed
status statements for the original bounded P2 campaign, without altering its
historical checkpoints.

**Hexagon reduction.** The previous Theorem1(d) incorrectly promoted a single
physical translation to a rank-two period lattice. The repaired argument takes
defect-free local limits using translations only, preserves that same nonzero
period in the limit, and transfers it to a honeycomb symbolic period. It does
not assert that the original periodic tiling is defect-free. Metric completeness
and exact convex-polygon/noncongruence realizability were also repaired. The
[fresh repaired-proof rereview](../reviews/two-hexagon-global-repaired-reduction-rereview.md)
is VALID within its stated dependencies and scope; ancillary flux claims are
outside that review and are not used in the census.

[Reduction/census audit](../reviews/two-hexagon-reduction-and-census-audit.md):
the stored rank<=3 registry has27,373 flats:11 rank1,504 rank2,26,858 rank3.
Covering types are exactly6 rank2 plus310 rank3. The6 are precisely the
no-mixed partition closures; all94 rank3 partition closures occur among the310.
The216 additional covering classes are already checked, not still pending.
All316 final coverage queries are UNSAT; all695 retained torus escapes pass
an independent exact checker. A second one-hot encoding independently returns
INFEASIBLE on all316 final queries. The stored ranks and covering closures were
independently checked, but exhaustive regeneration of the original flat BFS
was not part of this audit. Solver proof logs are not supplied.

Remaining census domain: every rationally closed covering triple type of
rank4..10 modulo D6 x D6 and species exchange, with every side-length
equivalence structure, unless discharged by inherited escapes, an applicable
empty-supertype certificate, or exact polygon nonrealizability. Proper
specializations count once by their full higher-rank closure; generic negative
cells do not exclude all specializations. Continue from ALL retained flats,
including noncovering parents: higher-rank minimal covering roots need not
descend through covering parents. Linear angle-box feasibility is only a
superset of joint polygon/side realizability. No rank4 enumeration has started
in this phase.

**Original P2 exclusion.**
[Independent audit](../reviews/kite-dart-exclusion-audit.md) closes the
98-type/9,604-pair strictly-interior, source-edge-erased varying-angle domain.
All9,586 negative primal witnesses and1,194 retained bounded faces were
independently reconstructed,660 metric ideals and128 joint partitions checked,
and both flat hexagon cases closed including their exact mirror transfer.
The four previously unresolved templates are closed: (0,0) has no boundary
network; (0,54),(0,1),(0,3) each has a degree-one boundary vertex in a closed
native dart/kite star. The legal sun occurs strictly inside a half-tile
supertile; primitive substitution recurrence makes the witness relevant to
the marked substitution-language hull, not arbitrary bare kite/dart tilings.
The old [campaign manifest](../certificates/penrose-kite-dart-campaign.json)
now records completion rather than repeating these open obligations. Shared
Z3/Singular trust and isolated specializations outside the varying-angle
scope remain explicit. No further P2 graph enlargement has been started.

**Construction gate.** Preparation includes an exact two-pentagon family
whose angle varies with0<t<1/4, and an explicit lattice tiling by their union
hexagon. This [periodic control](../searches/boundary-attachment-periodic-control.md)
is killed for every parameter by a mixed periodic escape; it is a verifier
control, not a promising candidate. A narrowly scoped two-donor notch transfer
leaves a <=4-corner member and similarly fails the monohedral gate.

The actual next attempt prescribes Ammann P1(J),P2(J) as the two final shapes
and seeks a convex two-piece dissection of H(J). Necessary area/perimeter
gates are retained in [the construction record](../searches/boundary-attachment-ammann-h-gate.md).
The [fresh independent review](../reviews/boundary-attachment-ammann-h-gate-review.md)
passes the repaired all-orientations gate. A signed-area convention gap found
in review was removed: the mixed pair is impossible for every real J since
|A1|+|A2| >= |A1+A2| = 1+sqrt5 > 2 = |AH|. The same-shape cases include
both signed areas Ai=+1 and Ai=-1; all ten necessary ideals are
zero-dimensional. Together with the two original mixed unit-ideal controls,
all twelve rows were independently reconstructed, their Groebner bases
matched, and a pure-power leading monomial checked for each variable.
Thus no continuous varying-angle family survives any two-piece convex
dissection into these prescribed shapes, including arbitrary reflections
and rotations. Exact strict-convex uncut samples confirm the original
prescribed shapes have angle freedom before the dissection equations.
Isolated necessary points remain unclassified; shared Singular engine
trust is explicit. No candidate reached reconstruction. This is a bounded
family exclusion, not a global impossibility theorem.

Main problem remains **Unresolved**: no new aperiodic two-shape pair or
whole-class impossibility proof has been established. Highest-information
next steps are the rank4 exact-type census from all parents, and a genuinely
different pair of final boundary words, subjected to periodic escapes before
source-forcing work.


Final restart checkpoint for this batch: all three agents' work and crossreviews
finished. No computational search from this batch remains running. The full
27,373-flat input is retained at
`research/certificates/two-hexagon-global-angle-flats-rank3.json`; all316 raw
census logs and three summaries are preserved in
`research/certificates/two-hexagon-global-covering-rank3-raw-logs.tar.gz`.
The independent registry verifier defaults to these repository inputs. SHA
and archive-member integrity checks passed. Original P2 manifest points to
its audit and fresh rereview; matched-endpoint screening remains separately
labelled unaudited. The current requested audit/construction batch is complete;
its bounded domains and absence of a surviving free-angle construction are
the stopping boundary, not a resolution of the research problem.

Next construction work needs different prescribed final boundary words or
a cluster involving neighboring shapes, with an exact convex varying-angle
family before forcing work. For the hexagon branch, first measure inherited
escape coverage on new rank4 types before committing to expensive whole-census
queries; retain noncovering parents and distinguish enumeration completeness
from solver verification. Neither larger search was launched in this batch.
