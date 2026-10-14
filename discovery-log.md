# Current research state for two convex tiles

**Problem status: unresolved.** No exact aperiodic pair or complete unrestricted
impossibility theorem meets [the acceptance criteria](research-problem.md).
**Checkpoint: 2026-10-14, reviewed and verified research checkpoint; unrestricted target unresolved.**
The unique-B-star and complete complementary two-angle hexagon families
admit periodic escapes whenever tileable. The complementary three-angle
result covers distinct, non-120 angles on its stated resonance domain. The original acute/obtuse pentagon native
words are untileable at every metric; the reordered words have an exact
three-equality tileability criterion and a four-tile periodic carrier.
These are restricted family results, not a global impossibility theorem.

**2026-10-13 active frontier:** the unrestricted objective remains unresolved;
no construction meets all acceptance criteria. Individual branch results are checkpoints. Source-only or local
objects below are not aperiodic pairs. Historical incremental notes are
[archived](research/searches/discovery-log-2026-10-13-working-history.md).

## Current restart and verification state

The previous research run stopped at the user's request. This checkpoint audits
and preserves that work and completes bounded independent reviews. No aperiodic
pair or unrestricted impossibility theorem has been established. Keep both
pentagon-containing pairs and two-hexagon pairs in scope; requiring a pentagon
is a construction preference, not a proved global necessity.

Locked environment verification passed on 2026-10-14. The final registry has
53 certificate pairs and 277 verifiers (330 checks). The entire disposable
replay **PASSED**, with no certificates written and original research files
unchanged during verification; [complete output](research/reviews/checkpoint-full-replay-2026-10-14.txt).
The [checkpoint audit](research/reviews/checkpoint-diff-audit-2026-10-14.md) records
repairs, review scope and the remaining mathematical obligations. All commands use `mise exec -- conda run
--no-capture-output -n arisearch <command>`. `mise run replay` verifies the full
registry on a disposable copy; targeted replay is `python
research/searches/verify.py --only SCRIPT` inside that environment.

Earlier progress tables, replay counts and completed-cycle narratives are in
[the historical checkpoint archive](research/searches/discovery-log-2026-10-13-checkpoint-history.md).
They preserve provenance and finite domains; current status below takes precedence.

The next research obligations are:

1. **Ammann cross-source replacements:** the [J-star 5/7 resection](research/searches/contact-structure-ammann-j-star-resection.md) is an [independently reviewed local witness](research/reviews/ammann-cross-source-resections-independent-review.md). Both outputs are now proved unable to tile alone; the pentagon audit exhausts 251 exact native-angle multisets and excludes flat-host stars. A global cover of the reviewed generic source by equal whole triads conflicts with its frequencies (1,φ,φ). A viable next step needs compatible fractional transfers or a different global rule, followed by an intrinsic decoder and exclusion of mixed periodic tilings. The earlier 6/6 split is killed by a direct Q-only periodic carrier. All four fixed Ammann records are now independently reviewed; none establishes a mixed full-plane 5/7 tiling.
2. **Mixed-PPP P5/Q14 palette:** P=(5π/7,4π/7^4), Q14=(6π/7)^14. Whole contacts, p=8q and mandatory α-α P dimers are necessary constraints. A β guest at every PPP star must have both adjacent native lengths among the two bevel values; target these equality planes. [Exact provisional candidate and full restart equations](research/searches/contact-pentagon-5pi7-q14-candidate.md): x=u=w=1, y=2sin(π/14)+4sin²(π/14), v=1+2sin(π/14)(1−y); Qword(v,v,u,v,v,u,u)^2. No metric producer has run. First audit equality/tag reductions, then check this one exact dimer/guest cycle; plane existence and global forcing are still open.
3. **Direct hierarchy construction:** the [eight-child support-reflection topology](research/searches/affine-two-convex-eight-child-support-reflection-gate.md) is now [independently reviewed excluded](research/reviews/affine-two-convex-eight-child-support-reflection-hostile-review.md) on P=(120,120+ε,60,120−ε,120), 0<ε<30. Its exact checker covers both reflex cases, all relevant length aliases and parent-corner indexing. A new proposal must change actual topology or angle data and supply compatible parent geometry; no surviving second-parent rule exists.

Do not relaunch the straight-edge pinwheel resection: [its entire admissible cut family has a reviewed direct periodic omission escape](research/lemmas/affine-two-convex-straight-edge-resection-periodic-escape.md), independently of the failed200-cell compiler. The full canonical Q7 family and complete P120/105-Q12 palette also have freshly reviewed periodic carriers, not unresolved candidates. Other closed families are indexed below.

## Current mechanism registry

The unrestricted target remains unresolved. Completed B5+1, two-U, old wheel, fan, fixed-source and capped global query domains are not resumed. The mechanisms below are new analytic results or exactly specified finite computations; none establishes an aperiodic pair or a universal impossibility theorem.

| Mechanism / current status | Strongest retained result | Remaining obligation / restart condition |
| --- | --- | --- |
| Affine stationary transport — reviewed VALID restricted exclusion | [Equivariant affine theorem](research/lemmas/affine-two-convex-iterable-obstruction.md), [finite transported-species extension](research/lemmas/affine-two-convex-finite-shape-transport.md); non-scalar-power inflation forces parallelograms or no polygon dissection. [Exact rectangle control](research/searches/affine-two-convex-fibonacci-rectangle-control.md). | Finite scalar-power matrices and alternative orientation-dependent hierarchies remain outside; finite transported shapes do not automatically provide their dissections. |
| All-obtuse pentagon/high partner — reviewed VALID | [PPP-density theorem](research/lemmas/contact-structure-high-partner-ppp-density.md): for n>=9 pentagon-only vertices are syndetic; no native PPP angle triple implies untileability at every metric. [Review](research/reviews/contact-structure-high-partner-ppp-density-review.md). | Pentagons with repeated-angle PPP stars, nonobtuse shapes and all other families remain. Uniform positive quadratic counts DO imply bounded gaps; earlier obtuse prose repaired. |
| One-right pentagon/equiangular octagon — reviewed reduction with residual domains | [Native reduction](research/lemmas/contact-right-angle-unrestricted-native-reduction.md), [fresh review](research/reviews/contact-right-angle-hosted-side-necessity-hostile-review.md): no Q-hosted T, all Q contacts whole, only21 native Q masks, flat hosts only three middle P sides of length2u/2v. [Private-side capacity](research/lemmas/contact-structure-right-palette-private-octagon-capacity.md) and [review](research/reviews/contact-structure-right-private-capacity-review.md). | Exactly two private Q slots are closed by the all-metric synthesis below. Zero/one-private repeated-length and zero-private host cases remain subject to the narrower classifications below; no general existence or forcing theorem follows. |
| Symmetric pentagon/octagon channels — reviewed VALID periodic escape | [Exact carrier and positive-parameter family](research/lemmas/contact-structure-right-pentagon-octagon-periodic-carrier.md); [independent quadratic-field checker](research/reviews/contact-structure-right-carrier-independent-check.py), [family slice review](research/reviews/current-exact-convex-source-right-carrier-hostile-review.md). Neither species tiles alone, but the mixed periodic motif kills every displayed pair. | A new candidate must change the symmetric channel geometry; these partners do not classify all arbitrary pairs with the palette. |
| Pinwheel three-triangle fusion — reviewed VALID finite exclusion | [Complete finite record](research/searches/pinwheel-three-triangle-convex-clusters.md), [certificate](research/certificates/pinwheel-three-triangle-convex-clusters.json), [independent checker/review](research/reviews/pinwheel-three-triangle-convex-clusters-review.md):1/6/36 anchored patches, five convex classes, four quadrilaterals and one supplementary pentagon, all periodic omission escapes. | Larger/cut/partial-side clusters are outside. Source decoding is not inherited from a selected pinwheel substitution. [Primary boundary](research/literature/pinwheel-convex-cluster-boundary.md). |
| Irrational radial fans — reviewed VALID pointwise exclusion | [Common-angle theorem](research/lemmas/three-triangle-irrational-fan-angle-obstruction.md), [review](research/reviews/three-triangle-irrational-fan-angle-hostile-review.md): any finite family with positive rational parameter multiples and theta/pi irrational is untileable, including partial contacts and omission. Exact u=(2+i)/sqrt5,u² pair killed. | Rational angles, nonzero affine intercepts and changed corner signatures remain outside. No arbitrary polygon impossibility follows. |
| Six-convex-source reconstruction — reviewed VALID exact fixture, conditional source transfer | [Recovered incidence and primary record](research/literature/current-exact-convex-source-six-reconstruction.md), [profile script](research/searches/current-exact-convex-source-six-profile.py), [explicit thin four-P motif](research/searches/current-exact-convex-source-thin-four-motif.md), [hostile review](research/reviews/current-exact-convex-source-six-hostile-review.md). Four thick/two thin faces recovered; midpoint thin collapse has explicit periodic omission. | Original Penrose arrow/kink compatibility, exact source parameters and universal decoder still unproved. Conditional frequencies(phi,phi,phi,phi,1,1) force balanced fixed macro contents(m,m,m,m,n,n), not a convex partition. |
| Six-child dissection topology — reviewed VALID universal finite theorem | [Every six-child dissection is a native wheel](research/lemmas/six-child-topology-universal-wheel.md), [fresh review](research/reviews/six-child-topology-hostile-review.md); arbitrary convex children>=5 sides, partial contacts and isolated boundary touch handled. [Substitution consequences](research/lemmas/six-child-topology-substitution-consequences.md): no uniform six-child pentagon inflation; stronger positive-conjugate P5/Qn bounds with both parent count gates. | The earlier two-size distinct-angle six-child obstruction now applies to all topologies; [combined synthesis review VALID](research/reviews/six-child-topology-two-size-synthesis-review.md). Seven-child constructions and repeated-angle boundary mappings remain unclassified. |
| General two-private octagon scaffold — reviewed VALID all-metric periodic escape | [Complete theorem](research/lemmas/contact-right-angle-two-private-all-metric-periodic-escape.md), [source review](research/reviews/contact-right-angle-two-private-general-hostile-review.md), [affine review](research/reviews/contact-structure-two-private-octagon-core-all-metric-synthesis-review.md). For every P, exactly two private Q slots force a periodic escape whenever tileable. Nonsymmetric P uses a clean typeR limit and periodic Q scaffold with anchored-band completion; [symmetric synthesis](research/lemmas/contact-symmetric-two-private-all-metric-periodic-escape.md) uses explicit symbolic carriers. Equal/distinct private lengths and all public-side aliases are covered. | Zero/one-private Q remains outside. Every original filling need not be periodic; no existence is claimed for an untileable pair. |
| Equal-private distance3 pair — reviewed VALID restricted universal-period exclusion | [Exact equal-private pair theorem](research/lemmas/contact-right-angle-equal-private-glide-periodicity.md), [finite native analysis](research/searches/contact-right-angle-distance-three-native-analysis.md), [independent ring/global review](research/reviews/contact-right-angle-distance-three-hostile-review.md). All16 radius1 choices were audited independently; clockwise reflected clipping polygons are now normalized, and repaired replays retain both original results. The unique ring transports QQ chains and all P neighbors with a common nonzero period. | Plane existence is not asserted. [Symbolic positive-parameter family](research/searches/contact-right-angle-symbolic-equal-private-glide-family.md) has a [VALID review](research/reviews/contact-right-angle-symbolic-glide-hostile-review.md). The broader two-private existence-of-a-periodic-escape theorem above is distinct from every-original-tiling periodicity. |
| Regular-pentagon six-wheel construction — reviewed VALID complete family exclusion | [Plane theorem](research/lemmas/regular-pentagon-six-wheel-plane-obstruction.md), [potential obstruction](research/lemmas/regular-pentagon-six-wheel-potential-obstruction.md), [exact script](research/searches/regular-pentagon-six-wheel-exact.py), [fresh review](research/reviews/regular-pentagon-six-wheel-hostile-review.md). All0<rho<1 pairs are untileable except rho=1-tan36°, with explicit four-Q periodic escape. | The proposed phi²-inflation[1,5]/[1,6] candidate is permanently killed. A locally disjoint cap does not extend: forbidden108/126 corners inside longer legs supply the repaired global obstruction. New angles or changed support data are required. |
| Binary octagon metric carrier — reviewed VALID unrestricted subfamily exclusion | [All-positive symbolic periodic carrier](research/lemmas/contact-right-angle-no-qq-periodic-carrier.md), [certificate](research/certificates/contact-right-angle-no-qq-symbolic-carrier.json), [independent review](research/reviews/contact-right-angle-no-qq-hostile-review.md). Every positive P in this palette has a grouped binary Q partner with an explicit four-P/one-Q periodic cell. | [Unrestricted binary-Q exclusion](research/lemmas/contact-right-angle-no-qq-binary-native-boundary.md), including partial contacts and derived noQQ, passed the fresh audit. The five-distinct/no-host zero-private domain is closed by the synthesis below; repeated-length and host-plane cases remain open. |
| One-private repeated-middle alias — reviewed VALID unrestricted family obstruction | [Complete all-host theorem](research/lemmas/contact-structure-one-private-repeated-middle-all-host-obstruction.md): w=x with x,y,u,v pairwise distinct and one private Q side is untileable. Native integer counts split into a binary-middle field obstruction or a clean all-R closure contradiction. | [Fresh complete review](research/reviews/contact-structure-one-private-repeated-middle-all-host-hostile-review.md) VALID. Other repeated-side identifications remain outside; the older two-word bridge still requires its explicit extra-middle-R premise. |
| Changed angle/size palette — reviewed VALID complete family exclusion | [Complete theta=720/n family](research/lemmas/sixty-degree-pentagon-equiangular-dodecagon-omission.md), [fresh review](research/reviews/sixty-degree-pentagon-equiangular-dodecagon-omission-hostile-review.md). For every n>=9, P has one theta/four(135-theta/4) corners and Q is an equiangular n-gon. All n!=12 pairs are untileable by complete native-star/corner-weight analysis; n=12 has an explicit central-hexagon periodic P-only escape at every metric. | Different corner signatures and nonequiangular partners remain outside. This entire specific size/angle family is closed without a monohedral classification. |
| Generic zero-private octagon — reviewed VALID full restricted synthesis | [AllR/degree-two reduction](research/lemmas/contact-right-angle-no-qq-generic-zero-private-reduction.md), [native-count(3,3,2) obstruction](research/lemmas/contact-right-angle-no-qq-zero-private-321-obstruction.md), [(4,2,2) clean-core extension](research/lemmas/contact-right-angle-no-qq-zero-private-422-core-reduction.md). New exact tagged geometry replaces numerical privacy; actual-contact persistence and mask symmetry are explicit. | [Complete fresh synthesis review](research/reviews/contact-right-angle-zero-private-full-synthesis-hostile-review.md) VALID. Side collisions and zero-private host planes remain outside. |
| Changed nonequiangular octagon — reviewed VALID exact fixture exclusion | [Exact support-line deformation](research/lemmas/contact-non-equiangular-octagon-one-deformation-obstruction.md), [fresh review](research/reviews/contact-non-equiangular-one-deformation-hostile-review.md). Q has angles112.5,157.5,135^6; its mixed acute star admits a local patch but five forced public unit edges give5q<=p while corner capacity gives4p<=13q. The pair is untileable, retaining arbitrary P-P partial contacts. | A further changed support/metric mechanism must escape these precise contact-budget bounds. No blanket ETE assumption or all-nonequiangular theorem is made. |
| One-private / all five P lengths distinct — reviewed VALID complete classification | [All-metric classification](research/lemmas/contact-right-angle-one-private-all-distinct-periodic-escape.md). Global native integer counts force dimers pointwise; all partial-contact host planes reduce to the aligned periodic ray or the crossed negative-metric ray. [Incidence audit](research/reviews/contact-right-angle-one-private-global-incidence-review.md) and [native bridge audit](research/reviews/contact-right-angle-one-private-native-bridge-hostile-review.md) are VALID. | [Fresh complete audit](research/reviews/contact-right-angle-one-private-all-distinct-complete-hostile-review.md) VALID. General repeated P side lengths remain outside. The separate w=x, pairwise-distinct x,y,u,v family is closed by the all-host obstruction above; its earlier two-word bridge exhaustion alone was insufficient. |
| Ordinary similarity / moved shared boundary — reviewed VALID scheme exclusion | [Complete straight-edge family periodic escape](research/lemmas/affine-two-convex-straight-edge-resection-periodic-escape.md), [fresh review](research/reviews/affine-two-convex-straight-edge-resection-hostile-review.md): every admissible cut preserves equal antiparallel hexagon edges and an explicit2Q periodic carrier. Quarter fixture has covolume17/2. | [Specified200-cell compiler](research/searches/affine-two-convex-pinwheel-quarter-cut-parents.md) independently has insufficient candidates for both parents. New boundary directions/topologies are required; changing only cut position or source depth cannot rescue the scheme. |
| Genuine Q-host fixtures — reviewed exclusions and periodic escape | Nonequiangular Q8 directions(22.5,45,90,135,202.5,225,270,315), four-equal P acute/bevel lengths and private Q host H=2u. Earlier asymmetric Q-host caps fail at a missing far native side pair; the repeated P metric supplies that missing pair. | The private-H2 four-equal fixture is now [untileable after independently reviewed repairs](research/reviews/contact-non-equiangular-four-equal-repaired-hostile-review.md): genuine caps are sparse, and a clean limit requires the absent middlew. The public-H1 variant has an [exact rotated periodic carrier](research/lemmas/contact-non-equiangular-public-h-four-equal-periodic-carrier.md), now [freshly reviewed VALID](research/reviews/contact-non-equiangular-public-h-four-equal-hostile-review.md). No old equiangular whole-Q/contact theorem is imported. |
| Nonequiangular alias fixture — reviewed VALID local exclusion | [Exact support pivot c with P x=w=1](research/lemmas/contact-non-equiangular-octagon-alias-candidate-obstruction.md), [independent review](research/reviews/contact-non-equiangular-alias-hostile-review.md). All four rings in the complete4^5 native domain fail at a mandatory far PP endpoint needing a Q135 side pair absent from Q. | This specific changed alias fixture is closed; not a theorem about all nonequiangular aliases. |
| Two-support nonequiangular Q — reviewed VALID full positive family carrier | [All-positive symbolic family carrier](research/lemmas/contact-non-equiangular-two-support-symbolic-periodic-carrier.md), [independent symbolic reconstruction](research/reviews/contact-non-equiangular-two-support-carrier-independent.py). ANY positive right P(x,u,v,y,w), partner Qword(H,u,w,v)^2 and two changed supports admit1Q/2P periodic cells for arbitraryH>0; all36 endpoints and area identities passed symbolically. | [Complete third audit](research/reviews/contact-non-equiangular-two-support-full-family-hostile-review.md) VALID. Other Qwords remain outside. |
| P5/Q7 branching signature — reviewed VALID full canonical family periodic escape | [Full positive family](research/lemmas/contact-pentagon-heptagon-branched-periodic-carrier.md): every right-palette P has Q7word(A,a,u,w,v,a,B), A=v+w/√2,B=u+w/√2, and an exact2P/2Q periodic cell with true QQQ vertices. [Independent closed-coordinate reconstruction](research/reviews/contact-pentagon-heptagon-branched-independent.py) regenerates all24unrestricted integral partners symbolically. | [Fresh full audit](research/reviews/contact-pentagon-heptagon-branched-hostile-review.md) VALID. Other heptagon metrics remain outside; branching by itself does not force hierarchy. |
| P120/105 + equiangular Q12 — reviewed VALID full palette periodic escape | [Complete metric classification](research/lemmas/contact-pentagon-120-105-dodecagon-periodic-escape.md): unrestricted contacts force x=y,u=v and regular Q; every positive remaining metric has an exact6P/1Q triangular periodic cell. [Independent alternate-field native reconstruction](research/reviews/contact-pentagon-120-105-dodecagon-independent.py) verifies42whole-edge partners and all-w>0 support signs. | [Fresh complete audit](research/reviews/contact-pentagon-120-105-dodecagon-hostile-review.md) VALID. The entire stated angle palette is closed; mixed PPP and different Q angles remain outside. |
| Mixed-PPP P5/Q14 third-angle palette — provisional paused algebraic lead | [Candidate and necessary native reductions](research/searches/contact-pentagon-5pi7-q14-candidate.md). Pangles(5π/7,4π/7^4), Q14angles6π/7; proposed positive x=u=w=1 metric and a centrally symmetric binary Qword are defined exactly. | No metric computation, tileability or hierarchy is established. Analytic equality/tag reductions await fresh review. Resume with one exact candidate check, not a metric grid or larger patch bound. |
| Ammann cross-source J-star — reviewed local 5/7 witness; omission excluded | [Exact strict-convex resection](research/searches/contact-structure-ammann-j-star-resection.md) spans H/P1/P2 at a changed native star and yields two exact output classes. | A whole equal-triad cover of the reviewed generic source contradicts its frequencies. Both single-species tilings are excluded by the [independent audit](research/reviews/ammann-cross-source-resections-independent-review.md); fractional transfer, mixed plane tilability and every-tiling decoding remain unproved. |
| Ammann K/L replacements — reviewed fixed schemes closed | [Single triad4/8 gate](research/searches/contact-structure-ammann-corner-triad-gate.md), [four double-corner alternatives](research/searches/contact-structure-ammann-double-corner-gate.md); the6/6 branch has a separate exact Q-only periodic escape. | The [independent review](research/reviews/ammann-cross-source-resections-independent-review.md) confirms these fixed boundary gates and the 6/6 periodic omission. Any convex 6/7 realization is excluded by the reviewed hexagon/higher-side theorem, although tileability is unclassified. All four fixed double-corner schemes are closed for the target; larger or fractional replacements remain outside. |

## Inherited results and paused mechanisms

The completed unique-B-star, complementary two-angle hexagon and eleven-word
B5+1 families remain closed within their stated hypotheses. Distinct,
non-120 complementary three-angle coverage retains its stated resonance domain.
The original two exact pentagon/hexagon candidates are falsified. The full
[historical mechanism index](research/searches/discovery-log-2026-10-13-checkpoint-history.md)
links all older proofs, certificates, reviews and finite search domains.

- The [global two-hexagon census](research/lemmas/two-hexagon-global-census.md)
  remains paused: 316 stored rank-at-most-three covering types were checked;
  ranks 4 through 10 and exhaustive regeneration of the flat census were not.
  Inconclusive queries require a new geometric constraint or decomposition,
  not an increased timeout. Preserve noncovering parents if reopening.
- [Ammann three-shape forcing](research/lemmas/ammann-forcing-aperiodicity.md)
  is reviewed on its stated generic domain. Two-class convex replacement and
  universal decoding remain separate obligations; the old Lemma S density
  proposal remains unresolved. Generalized collapse exhaustiveness is still
  [unresolved outside the reviewed original domain](research/reviews/ammann-two-class-exhaustiveness-review.md).
- The [kite/dart recomposition](research/reviews/kite-dart-exclusion-audit-rereview.md),
  [edge attachments](research/reviews/kite-dart-edge-attachment-audit.md),
  fixed-unit Robinson compiler and old whole-source fusion schemes retain
  their exact exclusions. New cuts, branching incidence or a changed source
  hypothesis must be specified before any new enumeration.
- Periodic partner constructions for V/V, Y/Y, U/W and V/W do not classify
  arbitrary independently chosen metrics. Repeated-length and irrational-angle
  hexagon families retain the exclusions and residual domains in the archive.
  No closed family is reopened merely by increasing patch depth.

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
