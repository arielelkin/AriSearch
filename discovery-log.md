# Current research state for two convex tiles

**Problem status: unresolved.** No exact aperiodic pair or complete unrestricted
impossibility theorem meets [the acceptance criteria](research-problem.md).
**Checkpoint: 2026-10-12. All research agents and routes are paused.** The last
bounded audit/construction batch is complete; no research search was found
running at this checkpoint. Verification below does not resume the research.

Follow [main_prompt.md](main_prompt.md) and [research-protocol.md](research-protocol.md).
Run shell tools through Conda `arisearch`. Rotations, reflections, partial
contacts and omission of a species remain allowed. The
[corrected literature boundary](research/literature/2026-10-11-convex-aperiodic-boundary.md)
recognizes Healey 2011 as the three-convex-tile benchmark under its stated
conventions. The repository's Ammann proof is a verification/strengthening,
not a new three-tile discovery. No fresh literature search is claimed here.

## Current portfolio and restart gates

| Mechanism / status | Strongest retained result | Remaining obligation / exact restart |
| --- | --- | --- |
| **Global two-hexagon route — paused, incomplete whole-class analysis** | The repaired SFT reduction has a [VALID fresh rereview](research/reviews/two-hexagon-global-repaired-reduction-rereview.md), conditional on reviewed structural dependencies. A single physical translation is preserved in a defect-free translated limit; the original tiling is not asserted defect-free. All **316 stored covering types of rank ≤3** have final UNSAT queries, **695 independently checked torus records**, and a second one-hot encoding giving 316 INFEASIBLE outcomes. The 100 partition types are a subset; the 216 extra rank-three types are already checked. | Rank **4..10** remains unenumerated. Continue from **all 27,373 stored flats**, including noncovering parents; minimal covering roots need not have a covering ancestor. First measure inherited escape coverage. Stored ranks/closures were independently checked, but exhaustive regeneration of the flat enumeration was not. Solver infeasibility proof logs are absent. Angle-box feasibility is not joint polygon/side realizability. [Census and replay](research/lemmas/two-hexagon-global-census.md), [audit](research/reviews/two-hexagon-reduction-and-census-audit.md). |
| **Ammann three-to-two collapse — closed on the recorded domain** | Exact reconstruction has a unique computed admissible two-class point, J at the circumcentre of BCD; the centrally symmetric hexagon tiles alone, so that candidate is **Falsified**. The point has an [independent exact root check](research/reviews/verify_ammann_two_class_collapse_point_root.sage). The generalized ≤2-interior-point/9,604-rhomb-pair search found no further free-angle candidate. | Exhaustiveness of the collapse classification still lacks an independent hostile review. More points, edge endpoints and neighbour-dependent decorations are outside the domain. Generic three-shape forcing is now separately reviewed. [Search record](research/searches/ammann-two-class-search.md), [coordinates](research/lemmas/ammann-two-class-reconstruction.md). |
| **Ammann three-shape forcing — completed reviewed verification** | [Lemma](research/lemmas/ammann-forcing-aperiodicity.md) is adversarially reviewed on G* = D ∩ (G1) ∩ (G2'): arbitrary contacts become edge-to-edge; reflections reduce to one handedness; an exact atlas reconstructs Penrose rhombs. [Repair rereview](research/reviews/ammann-forcing-repair-rereview.md) validates all eight repairs. | Non-generic parameters remain outside the theorem. This is not the two-tile target. The [mechanism analysis](research/reviews/ammann-mechanism-two-shape-survival.md) contains an **unresolved** Lemma S density argument; it must not be used as a proved reduction or as complete census coverage. |
| **Original P2 kite/dart recomposition — completed bounded exclusion, paused** | [Independent audit](research/reviews/kite-dart-exclusion-audit.md) and [VALID fresh rereview](research/reviews/kite-dart-exclusion-audit-rereview.md) close the 98-type/9,604-pair strictly-interior, source-edge-erased **varying-angle** domain. They checked 9,586 negative primal witnesses, 1,194 bounded faces, 660 metric options and 128 joint partitions. All four no-bounded-face templates are closed by empty-network/degree-one obstructions in the marked substitution-language hull. The unfinished direct flat branch is closed by an exact mirror transfer, not relabelled complete. | Isolated metric specializations, arbitrary bare kite/dart tilings, >2 points and neighbour dependence remain outside scope. Sage/Singular and Z3 trust remains; no formal UNSAT proof logs. [Campaign manifest](research/certificates/penrose-kite-dart-campaign.json) retains commands, hashes and domains. |
| **Matched-endpoint P2 attachments — completed computational screening, unaudited exclusion** | 706 one-centre star recipes: 522 small-polygon escapes, 181 slits, one holed face and two weak-convexity failures. A one-chord enlargement checked 2,000 recipes: 1,262 small-polygon escapes, 604 slits, 34 multiple cycles, 100 degenerate faces; no survivor. Encoding controls independently check the two 136-face quotients and 495 endpoint instances. | Encoding controls are not a hostile review of the exclusion. Chord-screen completeness/source scope still needs an independent audit. No larger enumeration is authorized by this checkpoint. [Separate edge manifest](research/certificates/penrose-kite-dart-edge-campaign.json). |
| **Prescribed Ammann H-to-two-pentagon dissection — completed reviewed bounded exclusion** | [Construction record](research/searches/boundary-attachment-ammann-h-gate.md) and [fresh review](research/reviews/boundary-attachment-ammann-h-gate-review.md) cover every two-piece convex dissection into the prescribed P1(J), P2(J), allowing reflections/rotations. Mixed pieces fail universally by the absolute-area bound abs(A1)+abs(A2) ≥ 1+√5 > 2 = abs(AH). Ten same-shape signed-area ideals are zero-dimensional; twelve rows including the original mixed controls were independently reconstructed. No continuous varying-angle family survives. | Isolated necessary points are unclassified; neighbouring-shape clusters, ≥3 pieces and different final boundary words are outside scope. The next construction needs different prescribed words or a cluster, with an exact convex varying-angle family and periodic escapes before source forcing. [Periodic two-pentagon control](research/searches/boundary-attachment-periodic-control.md) already has a mixed lattice escape for every parameter. |
| **Convex substitution — closed; internal bounded results** | [Search record](research/searches/convex-substitution-search.md) retains Euler/wedge obstructions and complete bounded alphabets. The golden b=c U/V pair is excluded for all inflation factors; the old phi³ 5U+8V question was exhausted by an exact five-node search. No candidate passed dissection. | Independent review remains outstanding. Partial hexagon and π/6 runs remain interrupted/UNKNOWN; do not convert them to UNSAT. No alphabet enlargement without a new angle system or specific parametric gate. |
| **Other-source decoration — abandoned, no search conclusion** | Exact hat patch producer and unfinished encoding retained in [the record](research/searches/source-decoration-search.md). No candidate or UNSAT result established. | Old downloaded/scratch files are discarded reconnaissance and are not retained evidence. Any future patch/search result must be regenerated and retained explicitly. Subsequent P2 work is the separate campaign above. |

## Established structural constraints

| Result | Status and scope | Proof and review |
|---|---|---|
| Monohedral escape; exclusion of triangles and quadrilaterals; rank-two side-count inequality | Internally checked. The torus inequality does not exclude rank-one periods. | [Side-count proofs](research/lemmas/side-count-and-monohedral-obstructions.md) |
| Every tileable finite convex protoset has a member with at most six sides | Fresh independent re-review VALID (2026-10-10). Includes partial contacts and T-junctions. | [Proof](research/lemmas/side-count-and-monohedral-obstructions.md), [review](research/reviews/global-side-count-review.md) |
| A hexagon paired with a polygon of more than six sides cannot be aperiodic | Fresh independent re-review VALID (2026-10-10). Depends on the cited unrestricted monohedral hexagon classification. | [Proof](research/lemmas/hexagon-limit-and-periodicity.md), [review](research/reviews/hexagon-higher-side-review.md) |
| A tileable two-hexagon pair admits an edge-to-edge, trivalent limit tiling | Defect-free limit adversarially re-reviewed after the uniform sector-disk repair. Honeycomb combinatorics and at least one-third same-type contacts follow; arbitrary periodicity does not. Fresh uniform vertex-separation re-review is valid. | [Proofs and review links](research/lemmas/hexagon-limit-and-periodicity.md) |
| Pentagon curvature and relative density constraints | Reviewed. An aperiodic (5,6) pair requires positive-density subdivision or excess-valence defects. | [Proof](research/lemmas/pentagon-curvature.md), [review](research/reviews/pentagon-curvature-review.md) |
| Uniform density when a subfamily cannot tile | Fresh independent review VALID. Every fixed-radius disk meets the complementary types; area/count lower bounds follow. Hypothetical aperiodic two-hexagon pairs require both types at positive lower density in every admitted tiling. | [Density theorem](research/lemmas/two-type-uniform-density.md), [review](research/reviews/two-type-uniform-density-review.md) |
| No angle multiset summing to pi forces edge-to-edge contacts | Proved internally; repaired after hostile review; independent re-review pending. Permits higher valence. | [Proof](research/lemmas/angle-nonresonance-edge-forcing.md), [review](research/reviews/angle-nonresonance-review.md) |
| All angles strictly between pi/2 and pi force edge-to-edge trivalence | Proved and reviewed; excludes all-obtuse (5,5) and aperiodic (5,6) pairs. | [Proof](research/lemmas/obtuse-edge-forcing.md), [review](research/reviews/obtuse-edge-forcing-review.md) |
| Convex fusion transfers strong aperiodicity under explicit source/partition hypotheses | Conditional lemma proved internally; repaired after hostile review; independent re-review pending. No usable source partition certified. | [Proof](research/lemmas/convex-cluster-fusion.md), [review](research/reviews/convex-cluster-fusion-review.md) |
| Finite convex multitile clusters cannot occur in everywhere-trivalent edge-to-edge convex tilings | Proved internally; extended during hostile review; independent re-review pending. Fusion must use a source with combinatorial defects. | [Proof](research/lemmas/convex-cluster-fusion.md), [review](research/reviews/trivalent-fusion-review.md) |
| Real corner/edge frequency balance | Proved necessary conditions; repaired after hostile review; independent re-review pending. Not a global realization theorem. | [Proof](research/lemmas/frequency-balance.md), [review](research/reviews/frequency-balance-review.md) |

Thus the surviving side-count possibilities are a pair containing a pentagon,
or two hexagons. These constraints do not resolve either general case.

## Retained restricted-family registry (all paused)

These older mechanisms are retained for reuse and are paused. The current
portfolio above records the later construction and global-census work. Details and exact
finite domains live in the linked subject artifacts. A proved periodic witness
kills only its stated family; it never establishes periodicity of an unrelated
pair. An every-original-tiling theorem is labeled separately.

| Mechanism / current status | Strongest result and hypotheses | First remaining global obligation | Reopening condition / exact restart artifact |
| --- | --- | --- | --- |
| **Reciprocal partial-contact mirror V/V — completed reviewed milestone, paused mechanism** | Exact A=(a,phi*k+a/phi,a,k,k), B=(k,phi*a+k/phi,k,a,a), a,k>0,a!=k. Four actual convex motifs with six full seams and two directed interval cancellations yield a periodic tiling throughout the positive cone. Partial native contacts persist in all five ratio cases, including coalescence boundaries. Full-cone independent review is VALID;292 complete coordinate comparisons pass. | No unresolved global lemma remains in this cone. Arbitrary independently chosen mirror metrics remain unclassified and are blocked without a new necessity invariant. At a=k the same construction is monohedral. | [Theorem](research/lemmas/pentagrid-v-v-reciprocal-partial-periodic.md), [VALID fresh review](research/reviews/pentagrid-v-v-reciprocal-partial-periodic-review.md), [exact producer](research/searches/pentagrid-v-v-reciprocal-partial-periodic.py). Reopen only changed exact data outside this cone with a new global mechanism. Periodic existence does not assert every tiling periodic. |
| **Branching repeated-length120-degree hexagons — completed reviewed milestone, paused mechanism** | New full 4D closed cone A=(p,a,q,p+a-c,c,q+a-c), B=(p+2(a-c),c,q+2(a-c),p+a-c,a,q+a-c), all eight values positive. A four-face periodic torus throughout the cone is independently reviewed VALID. Special p=a,q=c has a>0,0<c<3a/2,c!=a, adjacent repeats and no monohedral escape. | No unresolved global lemma remains in this full cone. Other repeated-length shapes and global extension of the second local branch are unclassified.24 complete fixture and12 local-branch comparisons independently pass. | [Full-cone theorem](research/lemmas/hexagon-adjacent-repeat-periodic-cone.md), [VALID fresh review](research/reviews/hexagon-adjacent-repeat-periodic-cone-fresh-review.md), [exact producer](research/searches/hexagon-adjacent-repeat-periodic-cone.py). Reopen only changed exact geometry outside the cone, with a new global mechanism; longer branch words do not remove the existing periodic escape. |
| **Non-affine repeated hexagons — completed reviewed cone** | Rational3D deformation outside affine120-degree families has two actual local branches and a four-face periodic torus; full cone independently reviewed VALID. | No gap inside this cone; other repeated shapes remain. | [Theorem](research/lemmas/branching-hexagon-rational-deformation.md). Existing periodic escape cannot be removed by longer branch words. |
| **Binary alternating/two-run hexagons — no-homogeneous branch complete, residual resonance slices paused** | All0<delta<30,p!=q,Aalternating/Bpppqqq with no homogeneous stars are untileable or have direct/length-swapped positive periodic-cone escape. Complete72mixed-cover hyperplanes necessary for every member. Single120/qq-low-high fullslice tiles iff beta120 after34exact duals/14exact phase filters; whole-proof synthesis VALID. | The entire unordered paired-qq family is now VALID, including all homogeneous pp planes and both native orders. One noncentral homogeneous arc with the other nonhomogeneous arc now has a VALID complete paired-or-untileable count theorem. The central120/120 case with the other arc nonhomogeneous is now VALID, with same/cross-slot positive families derived from actual contact saturation. Both noncentral mixed homogeneous arcs are now independently excluded in both relative orders. Center/mixed and center/pure are independently classified. Pure/mixed and pure/pure categories remain open. | [No-homogeneous theorem](research/lemmas/branching-hexagon-two-run-no-homogeneous-star-classification.md), [72planes](research/lemmas/branching-hexagon-two-run-mixed-cover-hyperplanes.md), [single120 slice](research/lemmas/branching-hexagon-two-run-single-120-complete-slice.md). No fixed frequency or original edge-to-edge rule is assumed. |
| **Fixed-B alternating hexagon transport — completed full family** | A threefold alternating(p,q), B=(r,p,q,q,q,q), all3 lengths distinct. Every tileable pair admits a period, including qq resonances. Fresh two-review audit VALID after explicit omission ledger. Required-angle multiplicity handles repeats; unique-target injection gives a saturated admitted limit, with j3periodic and j4/j5 native-parity contradictions. | No global gap inside the stated family. Other A geometries, B words or length coincidences remain. | [Full theorem](research/lemmas/branching-hexagon-new-fixed-b-classification.md), [independent review](research/reviews/branching-hexagon-new-fixed-b-classification-review.md), [root review](research/reviews/branching-hexagon-new-fixed-b-classification-root-review.md). Reopen only changed hypotheses and a concrete new mechanism. |
| **Fixed unit Robinson U/V compiler — closed** | Proper Penrose, all regular generalized sources at the fixed slope, and the stated local matching closure exclude every mandatory V boundary independently of residual filling. All 409 generalized objects independently certified; two full U objects occur in infinite generalized sources. | Arbitrary singular selections outside the closure are unclassified. This is not unrestricted U/V untileability. | No intercept-only or additional residual search. Require exact changed cuts, macro metric/scale, slope or another used assumption plus the obstruction removed. [Closure theorem and checklist](research/lemmas/pentagrid-robinson-generalized-source-gate.md), [VALID review](research/reviews/pentagrid-robinson-generalized-window-review.md). |
| **General V/V central-hexagon partner — completed reviewed theorem** | Every positive V-angle pentagon has a continuum of explicitly chosen noncongruent V partners with a periodic four-face dissection. Full4-parameter positive cone and56 complete fixture comparisons pass two independent reviews. | Arbitrary independently specified V/V pairs remain unclassified. | A new necessity/compatibility mechanism, rather than another supportive example, is needed. [Theorem](research/lemmas/pentagrid-v-v-general-double-y-partners.md), [fresh second review](research/reviews/pentagrid-v-v-general-partner-fresh-review.md). The older mirror theorem is a subfamily. |
| **General Y periodic partner — completed reviewed theorem** | Every positive Y=(R,theta,R,theta,2pi-2theta) pentagon, pi/2<theta<3pi/4, has an explicit distinct periodic Y partner. A given pair with Q2=P0,Q4=P1 also has a periodic carrier. Reflections and partial carrier contacts included. | Arbitrary given Y/Y pairs and other equal-multiplicity words are unclassified. | Need a new necessary edge relation or different global construction. [Theorem](research/lemmas/general-y-pentagon-periodic-partner.md), [fresh second review](research/reviews/general-y-pentagon-partner-fresh-review.md). |
| **V/W and U/W periodic partners — completed reviewed families** | Every genuine equiangular W has a selected V partner in a full 3D metric cone. U/W has the earlier explicit b>0,0<c<phi*b cone. Each has four-face periodic coverage for every stated parameter. | Unrelated independently specified U/W or V/W pairs remain unclassified. | Exact changed compatibility data or an independent necessity argument. [General V/W](research/lemmas/pentagrid-v-w-general-metric.md), [VALID fresh review](research/reviews/pentagrid-v-w-general-metric-fresh-review.md), [U/W](research/lemmas/pentagrid-u-w-periodic-continuum.md). |
| **Unique-private octagon chains — completed every-tiling theorem** | ANY equiangular108 P has adjacent-corner rigidity: a repeated side forces an actual reflection symmetry. Q with two nonadjacent108/six144 corners and two distinct unique lengths absent P forces a common nonzero period in EVERY original tiling, including extra Q contacts. | Other private multiplicities and broader Q data are unclassified. | Need exact changed private matching data. [Universal theorem](research/lemmas/private-octagon-adjacent-corner-rigidity.md), [VALID review](research/reviews/private-octagon-adjacent-rigidity-review.md). Supersedes the distinct-P good-limit proof. |
| **Equal-private octagon branches — completed reviewed restrictions** | Nonsymmetric Q3 with P=(2phi-2,phi,1,phi,2phi-2), Q=(phi^2,2phi-2,phi,phi^2,1,2phi-2,phi,phi) has a certified2Q+4P periodic torus,36 independent complete clips. An actual Q symmetry exchanging its two L slots implies every tiling periodic;12-case regular-unit closure and all actual symmetries independently reviewed VALID. | Arbitrary nonsymmetric equal-private metrics or mixed private choices remain unclassified; no every-tiling claim for Q3. | Inactive research under current portfolio. [Exact Q3 escape](research/counterexamples/new-octagon-q3-equal-private-periodic.md), [VALID independent review](research/reviews/octagon-q3-equal-private-periodic-review.md), [symmetry theorem](research/lemmas/private-octagon-equal-private-symmetric-periodicity.md), [VALID review](research/reviews/private-octagon-equal-private-symmetric-review.md). |
| **All-obtuse internally distinct(5,n) — completed restricted exclusion** | n>=8 untileable; n7 has a four-face periodic witness. New direct theorem proves a nonzero period in EVERY original tiling using two selected Q-private midpoint chains and unique P corners, without counting limits or graph enumeration. | Repeated native lengths or nonobtuse angles remain outside. | Exact changed metric coincidences/contact data. [General theorem](research/lemmas/distinct-length-obtuse-pentagon-higher.md), [direct strengthening](research/lemmas/distinct-length-obtuse-direct-common-period.md), both reviewed VALID. |
| **Two-angle(5,7) metric family — completed reviewed restrictions** | alpha4pi/7,beta5pi/7: full 4D positive cone has periodic coverage, even with coincidences. Internally distinct P/H implies EVERY original tiling periodic for all shared orders. Equal-private H=(L,a,L,b,c,d,e), five-distinct P, reduces to a complete2D positive cone with a periodic escape throughout. | Other repeated lengths/positions remain unclassified. | No longer private-chain words in the closed cone. Need exact changed coincidence pattern. [Full theorem](research/lemmas/two-angle-5-7-metric-continuum.md), [VALID second review](research/reviews/two-angle-5-7-metric-continuum-second-review.md), [equal-private theorem](research/lemmas/two-angle-5-7-equal-private-scaffold.md), [VALID review](research/reviews/two-angle-5-7-equal-private-scaffold-review.md). |
| **Regular higher-polygon partners — completed all-obtuse classification** | Strictly obtuse P with regular Q: n7 exact periodic family, n12 exact2D periodic family; other n>=7 excluded by reviewed angle/contact counts. Regular-Q7/four-alpha-one-beta is untileable. | Irregular Q or nonobtuse P remain outside. | Changed exact angle/metric data, not the same regular family. [Q7](research/lemmas/all-obtuse-pentagon-regular-heptagon-classification.md), [Q12](research/lemmas/all-obtuse-pentagon-regular-dodecagon-classification.md), [n>=13](research/lemmas/all-obtuse-pentagon-regular-large-polygon-obstruction.md), all reviewed. |
| **Pentagrid angular/metric reduction — reviewed necessary constraints** |101 words/13 classes leave U,V,W; ALL U/U metrics are untileable with unrestricted partial contacts. Conditional Rao filter: U/W monohedrally untileable; V mono iff L2=L4 or L3=L0 in the after-side convention. U/V,U/W,V/V,V/W general metric pairs remain open. | Unrestricted geometric forcing for surviving pairs. | New metric/contact invariant. [Two-U proof](research/lemmas/pentagrid-two-asymmetric-u-obstruction.md), [angular reduction](research/lemmas/pentagrid-pentagon-angular-reduction.md), [explicit Rao dependency](research/lemmas/pentagrid-pentagon-monohedral-filter.md). |
| **Area-compatible U/V partial-contact family — inactive; global mechanism blocked** | U=(phi^2*b+phi*c twice,b,c,b), V=(b,2phi*b+phi^2*c,b,phi*(b+c) twice), b,c>0, closed/convex and areaV=phi*areaU. EVERY metric lacks an ETE tiling. If c/b outside Q(sqrt5), no homothetic U/V substitution exists; inside, scale lies in Z[phi]. | Nonhomothetic infinite existence and unrestricted forcing lack a concrete mechanism. | New nonhomothetic mechanism or exact changed family; no larger old substitution search. [Area/source record](research/searches/pentagrid-golden-metric-area-compatible.md), [ETE obstruction](research/lemmas/pentagrid-area-family-edge-obstruction.md), [unbounded substitution theorem](research/lemmas/pentagrid-generic-metric-substitution-obstruction.md). The old SMT trial was UNKNOWN at120.205638s; a later exact dissection search exhausted this specific parent (see the substitution record above). |
| **Cairo/right-angle partial contacts — generic, monohedral, zero/one-sharing complete; exact two-sharing reduction reviewed** | Complete738generic patterns and monohedral classification. All zero/one-sharing metrics excluded, across every event resonance. Exact two-sharing:72patterns/13orbits,7,830flats,629necessary local strata,493exact seam duals; new reversed-right-pair fullperiodic cone removes one of136 relaxed primals. Known swapped/Y cones remain periodic throughout. |6 necessary targets remain (3 dimension2,3 dimension1; flat239 restricted to its low-ratio subcone), with additional reviewed order restrictions. All four dimension3 parents have reviewed periodic escapes. Internally repeated pairs and three/four shared-arm nongeneric metrics remain outside these complete reductions. | [Zero/one master](research/lemmas/partial-contact-cairo-one-shared-classification.md), [two-cross reduction](research/lemmas/partial-contact-cairo-two-cross-native-reduction.md), [new periodic cone](research/lemmas/partial-contact-cairo-reversed-right-pair-periodic.md), [fresh flat audit](research/reviews/partial-contact-cairo-two-cross-event-flats-review.md). No primal implies existence. |
| **Three-angle multiplicity and irrational witness — completed audit** | Different multiplicity rows for three combined angle values force rational angles. Equal rows admit periodic irrational theta/pi with cos(theta)=-2/5. Scaling the independently checked witness by sqrt2 gives private lengths sqrt2,sqrt10, both irrational and irrational ratio.52/48/48 complete comparisons pass. | Other equal-row metric pairs and four-angle families remain outside. | Exact changed compatibility data. [Rationality lemma](research/lemmas/three-angle-pentagon-multiplicity-rationality.md), [witness](research/lemmas/new-angle-three-pentagon-private-length-counterexample.md), [VALID review](research/reviews/new-angle-three-pentagon-periodic-review.md). Mixed X/Y finite ansatz967680 cases/8models is exhausted infeasible, not a full X/Y classification. |
| **Distinct/five-length hexagon graph selection — completed restricted exclusions** | Both internally distinct hexagons admit a periodic torus if tileable. Five-symbol/separation2 repeats: <=2 shared untileable,3 shared periodic; one private-repeat six-symbol order has periodic escape in both generic/doubled-angle cases. Unique complete intrinsic neighbors force a crystallographic group, conditionally. | Other repeated orders and genuinely branching physical neighbors remain outside determinism. | Exact changed repeated order with positive closure and two-ended contacts. [Distinct theorem](research/lemmas/hexagon-holonomy-distinct-lengths.md), [sparse repeats](research/lemmas/hexagon-five-length-sparse-sharing.md), [private repeats](research/lemmas/hexagon-five-length-private-repeat-periodicity.md), [conditional determinism](research/lemmas/hexagon-five-length-intrinsic-determinism.md), all reviewed. |
| **Equilateral rational-angle root classification — completed restricted exclusions** | Rational-angle equilateral(5,5),(5,6) cannot be aperiodic even at different scales. Two equilateral rational-angle hexagons are untileable or have a monohedral/three-face periodic escape. Imported root-sum theorem explicit. | Irrational-angle equilateral hexagons outside root classification. | Changed angle hypothesis and concrete geometry; denominator/scale enlargement does not repair closed cases. [Pentagons](research/lemmas/new-angle-equilateral-rational-obstruction.md), [hexagons](research/lemmas/new-angle-two-equilateral-hexagons.md), both reviewed. |
| **Affine-mirror repeated hexagons — completed periodic counterexample** | Two repeated-length irrational-angle noncentral hexagons have an exact periodic escape, with no monohedral escape; an affine image of mirror shapes needs a commuting affine map to keep exactly two classes. | General branching non-affine family remains outside. | New non-affine contact data. [Exact theorem/witness](research/lemmas/hexagon-affine-mirror-periodic-escape.md), [VALID review](research/reviews/hexagon-affine-mirror-escape-review.md). |
| **Convex source fusion/Ammann — blocked** | Conditional fusion lemma and exact coordinate reconstruction retained. Trivalent ETE sources cannot support finite convex multitile fusion. Aggregate H:P=1:2phi in the older count argument is conditional. Exact branch/shape data and three-shape forcing on G* now have separate retained proofs. | A global convex two-class partition and forcing for the resulting final shapes are missing; the generic three-shape source is now reviewed. | An exact new partition or source mechanism. [Current source forcing](research/lemmas/ammann-forcing-aperiodicity.md), [historical audit](research/reviews/ammann-convex-source-audit.md), [coordinates](research/lemmas/ammann-coordinate-parameterization.md), [fusion](research/lemmas/convex-cluster-fusion.md). |
| **Walton two-hexagon rule compiler — falsified recorded family** | Natural transcription and all24 relabelings collapse to regular hexagons;4094 state assignments leave4 angular branches, all fail equilateral closure. The one-block obstruction is narrower than the general target. | A different certified geometry compiler and shape-only global forcing are missing. | New source, extendible strict sublanguage or neighborhood-dependent geometry. [Exact domain](research/searches/walton-encoding-reconnaissance.md), [one-block lemma](research/lemmas/walton-one-block-obstruction.md). Do not repeat completed assignments. |
| **Nonresonant(5,6) scaffolds — falsified exact candidates** | Both recorded exact pairs are untileable. Original full-edge stars omit required corners; joint pair's94 ordered/chiral endpoint cases reduce12 then0. | No survivor exists in the recorded fixed data. | Change side/angle partition and apply cheap two-endpoint filters before global work. [Original](research/searches/nonresonant-5-6-angle-scaffold.md), [joint](research/searches/joint-5-6-synthesis.md), [endpoint review](research/reviews/joint-5-6-two-ended-review.md). |

## Paused binary-hexagon obligation ledger

For B with native side word `pppqqq`, use four arc categories: N has no legal
homogeneous triple; C has both native angles120; P has one120 angle and one
other angle; M has a noncentral mixed2+1 homogeneous triple. The four
homogeneous lines intersect only at C. Distinct p,q and `0<delta<30` remain
explicit hypotheses. Reflection may swap both native arc orders; exchanging
length names requires the reviewed A normalization and never changes the
aperiodicity definition.

| Domain | Strongest current result | Exact artifact / remaining obligation |
| --- | --- | --- |
| At least one N arc | Every tileable member has a reviewed periodic escape | [No-homogeneous](research/lemmas/branching-hexagon-two-run-no-homogeneous-star-classification.md), [one-noncentral](research/lemmas/branching-hexagon-two-run-one-noncentral-homogeneous-arc.md), [center/N necessity](research/lemmas/branching-hexagon-two-run-pp-center-no-qq-homogeneous-classification.md) |
| M/M, both relative native orders | Untileable; forward and complete reverse obstruction independently VALID | [Forward](research/lemmas/two-homogeneous-forward-mixed-arcs-obstruction.md), [complete reverse](research/lemmas/two-homogeneous-opposite-mixed-arcs-full-obstruction.md), [fresh whole reverse review](research/reviews/two-homogeneous-opposite-mixed-arcs-full-obstruction-review.md) |
| C/M, up to length normalization | Complete periodic-escape classification, independently VALID | [Center/mixed](research/lemmas/two-homogeneous-center-mixed-qq-classification.md) |
| C/P, up to length normalization | Complete periodic-escape classification, independently VALID | [Center/pure](research/lemmas/two-homogeneous-center-pure-qq-classification.md), [fresh whole-proof review](research/reviews/two-homogeneous-center-pure-qq-classification-review.md); all four phase/domain/native-metric transfers checked |
| C/C | Closure requires p=q, outside distinct-binary scope | Both equal120 arcs have unit chain norm2; closed positive p and q chains therefore require2p=2q |
| P/M and P/P | OPEN; no actual necessity/realization theorem retained | Both-end native contacts, allowable AA seams and actual phase must be handled. Old no-qq-homogeneity exclusion and center-slot arguments do not apply |

The [same-slot](research/lemmas/branching-hexagon-two-run-pp-center-periodic-family.md)
and [cross-slot](research/lemmas/branching-hexagon-two-run-pp-center-cross-periodic-family.md)
positive carriers are independently VALID on their full exact domains, both
admissible quadratic branches and their coalescence. They provide sufficiency,
not arbitrary-pair necessity. Equal lengths and arbitrary A remain outside the
negative binary-family classifications. No whole parent-family closure or
unrestricted impossibility theorem is claimed.

## Paused Cairo obligation ledger

[The native master reduction](research/lemmas/partial-contact-cairo-two-cross-native-reduction.md)
retains the complete72-pattern/13-orbit/7830-flat domain and493 exact seam
exclusions. Actual-order refinements and native Euclidean carriers replace
local feasible balances by reviewed periodic witnesses where proved. The
[seven-target signed native map](research/lemmas/partial-contact-cairo-mixed-quotient-seven-stratum-reduction.md)
is independently VALID. The [ray459 theorem](research/lemmas/partial-contact-cairo-mixed-quotient-fixed-ray459-periodic.md)
now has a fresh full native-geometry/links/holonomy/coverage VALID review.
[The six-target synthesis](research/lemmas/partial-contact-cairo-mixed-quotient-six-stratum-reduction.md)
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
[the native search](research/searches/partial-contact-cairo-mixed-quotient-native-search.py)
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
intercept/residual filling searches. [Source gate and checklist](research/lemmas/pentagrid-robinson-generalized-source-gate.md).

Arbitrary V/V and Y/Y compatibility needs a new necessity invariant; selected
periodic partners are not arbitrary-pair classification. Area-compatible U/V
nonhomothetic existence and forcing remain blocked. The retained phi3 SMT
trial remains historically UNKNOWN at120.205638s; the later exact golden-U/V
search exhausted the 5U+8V parent, independently of that timeout.
[Exact old trial](research/searches/pentagrid-golden-metric-phi3-macro.md),
[later exclusion](research/lemmas/convex-substitution-golden-uv-all-lambda.md).
Ammann now has a reviewed three-shape forcing proof on its stated generic
domain, but fusion still lacks a two-class convex partition and unrestricted
forcing for the final shapes.
[Current source proof](research/lemmas/ammann-forcing-aperiodicity.md).

## Preservation and verification checkpoint (2026-10-12)

The [superseded 2026-10-11 snapshot](research/searches/discovery-log-2026-10-11-history.md)
preserves the previous chronological checkpoints. Its running-job, novelty,
and intermediate review statements are historical; this file is the restart
entry point. Older subject reviews retain their original findings with links
to completed repairs where applicable. Outstanding review gates remain open.

The full rank≤3 flat input and all 316 raw census logs plus three summaries
are retained under `research/certificates/`; registry/archive/log SHA256 and
archive-summary integrity checks pass. The census replay no longer needs
scratch files. Empty checkpoint lock files are runtime artifacts and are
ignored by Git; mathematical checkpoints and SMT inputs remain retained.

Run registered certificate replays and independent checks without changing
retained certificates:

```text
conda run --no-capture-output -n arisearch python research/searches/verify.py
```

Use repeated `--only SCRIPT` to select checks. The runner covers its explicit
registry; it does not rerun every search, prove enumeration completeness,
review proofs, or turn solver verdicts into formal certificates. Writing audit
producers remain separate commands and can overwrite evidence unless directed
to temporary output. Do not disable assertions. The low-rank registry now has
an explicit nondestructive replay:

```text
conda run --no-capture-output -n arisearch python research/reviews/verify_two_hexagon_low_rank_registry.py --check
```

Checkpoint validation passed: 341 Python sources parse; 232 JSON, five JSONL
and four compressed JSON certificates parse; all local Markdown links resolve.
All 43 registered producer/certificate pairs and 142 verifier paths exist.
Five newly registered checks passed (Ammann repair rereview, stored-flat
registry, 695 torus records, P2 encoding, endpoint-star encoding), along with
one legacy producer and verifier exercising the unchanged invocation path.
The full 185-check registered suite was not rerun.

Additional targeted replays passed: all twelve repaired dissection-gate rows
match after excluding elapsed times and the temporary-output replay path;
9,586 P2 negative witnesses and 1,194 retained faces rebuild exactly; closed
source-star counts are 25/90 at patch3/4; the independent partition reviewer
checks all 101 original torus records with zero failures and reconstructs its
input from retained partitions without the old agent-specific scratch file.
All sixteen recorded script-hash pairs and the registry/archive/log/summary
hashes match. Of 355 certificate-directory artifacts checked against the
start-of-checkpoint snapshot, 354 are byte-identical; only the edge-campaign
manifest status text changed. Eight empty, unlocked runtime lock files were
removed and their pattern added to `.gitignore`. `git diff --check` passes.
No new research enumeration, staging, commit or push is part of this checkpoint.
The pre-existing README/devcontainer changes are separate infrastructure work.

The independent checkpoint diff audit repaired a false-PASS case in the
[registry replay](research/reviews/verify_two_hexagon_low_rank_registry.py):
missing or invalid one-hot logs could previously leave stale verification
metadata accepted. The checker now compares the complete reconstructed
schema, excluding only the separate `independent_torus_check` annotation.
Eight controls using temporary copies passed: valid input and external torus
annotations were accepted; missing, truncated and malformed logs, incorrect
counts, missing fields and stale extra derived fields were rejected. This
checks retained log integrity, not solver infeasibility or the external torus
annotation. The [mechanism note](research/reviews/ammann-mechanism-two-shape-survival.md)
was also narrowed: the 12-side count applies to two hexagons, and the proposed
two-orbit/free-parameter criterion is heuristic, not a necessary condition.
Its collapse-classification and Lemma S review gates remain open.

After those repairs, registered replays passed for the registry, all 695
torus records, P2 recomposition controls and endpoint-star controls. The
full 185-check suite was not rerun. The audit changed only the registry
checker, mechanism note and this log; it changed no retained certificate,
index entry or commit. All research remains paused.
