# Current research state for two convex tiles

**Problem status: unresolved.** No exact aperiodic pair or complete unrestricted
impossibility theorem meets [the acceptance criteria](research-problem.md).
**Checkpoint: 2026-10-13, completed construction cycle; four new checks passed.**
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

## Current construction cycle (2026-10-13): completed

The [fixed single-cycle contract and decisions](research/searches/construction-cycle-2026-10-13.md)
were executed by two independent construction tracks and a separate hostile
reviewer. Original unrestricted definitions are unchanged; **B5+1 remains
closed and paused**. No closed enumeration, global solver query, bound or
adjacent parameter sweep was resumed. The requested one-cycle scope is the
stopping boundary; no execution-limit termination is claimed.

| Mechanism / status | Strongest reviewed result | Failure and restart obligation |
| --- | --- | --- |
| [A: incidence-changing centroid edge diamonds](research/searches/construction-cycle-a-edge-diamonds.md) — proposal falsified, stopped | Exact infinite finite-prototile polygonal covering at J=1/2+(4/5)w: source-crossing faces and restored degree-three incidence at H-J'. An audited crossed diamond is strictly convex. This genuinely escapes the old incidence-preserving hypothesis. | Every complete face has at most four corners; any convex two-class output admits periodic omission. The ONE outward-kink repair makes the audited face a convex pentagon but gives its neighbor a reflex corner, with exact containment and area conservation. Next: a genuinely branching network with complete faces of at least five corners, an exact compatible infinite covering, then class/congruence checks and an intrinsic decoder. Centroid or epsilon tuning cannot repair these obstructions. |
| [B: bevelled-chair pentagon parents](research/searches/construction-cycle-b.md) — proposal falsified, stopped | Exact distinct strict convex P/Q, areas 3/2 and 11/8, partition one nonconvex chair. BOTH atoms independently tile the plane periodically by certified central-hexagon lattice carriers. | Fixed four-child scale-2 extension protrudes at (3/4,1/16); mixed-parent recognition fails by either species omission. Zero repairs spent: simple seam/bevel edits preserving the right-angle carrier do not address forcing. Next: different exact atomic geometry without these carriers AND pointwise repeatable parent/child compatibility before hierarchy recognition. |

[A hostile review](research/reviews/construction-cycle-a-hostile-review.md) independently
checked original and repaired claims; [B hostile review](research/reviews/construction-cycle-b-hostile-review.md)
checked exact geometry, covering and both omission escapes. [Root integration](research/reviews/construction-cycle-root-integration-2026-10-13.md)
records the scope audit. Reflections and partial contacts remain unrestricted;
none can exclude a periodic tiling already admitted by half-turns/translations.
Both omission witnesses have nonzero periods, defeating even single-direction
period exclusion. A has no final intrinsic decoder; B's universal mixed-parent
recognition is explicitly false. No new two-convex-shape aperiodic covering,
unrestricted impossibility theorem, or novelty claim follows.

Exact coefficients/certificates and independent checker outputs are retained
in the linked artifacts. Four new nondestructive registered checks passed:
A producer/certificate reconstruction, B read-only certificate reconstruction,
and two independent geometric verifiers. [Replay output](research/reviews/construction-cycle-targeted-replay-2026-10-13.txt).
Registry now has 44 producer/certificate pairs and 226 verifiers (270 total).
Locked environment verification passed; no dependency changed. Full legacy
replay was not repeated in this cycle; its earlier 266-check full PASS is
retained separately below. No staging, commit or push occurred during the construction cycle itself.
The subsequent user-requested [Astra diff review](research/reviews/construction-cycle-astra-diff-review-2026-10-13.md)
found no substantive defect and independently reran all four new checks,
including retained-output equality. The user authorized committing and pushing
this reviewed checkpoint on the existing convex-pair branch.

## Trustworthy native-family coverage

Generic complementary ternary angles split the eleven A bracelets into
[five parameterized native families](research/lemmas/two-hexagon-ternary-five-native-family-ledger.md)
under simultaneous colour relabelling. All actual side metrics, reflections,
original partial contacts and omission are included where stated.

| Native A representative | Current status / mechanism | Residual scope |
| --- | --- | --- |
|012012|[Reviewed VALID allmetrics](research/lemmas/terra-ternary-opposite-a-all-metric-escape.md):64 AAA cycles force centrality; absentAAA the B-ring colour contradiction removes mixed fields|Equal-angle/120 loci remain; six soleABB lines removed by reviewed potential|
|001122|[Reviewed VALID allmetrics](research/lemmas/terra-001122-all-metric-periodic-escape.md):203 partitions/360 rings; surviving outerAAB forces globalBcoset; six-state native actions and metriclift giveperiod|Same sixABB lines transfer; equal-angle/120 loci remain|
|001221 orbit (three bracelets)|[Reviewed VALID allmetrics](research/lemmas/terra-001221-all-metric-periodic-escape.md):missing endpointpairs forceBsameword;768 connectedAA equalitygraphs forceAequilateral/H1 omission|Native-independent ABB transfer applies; singular120/equal-angle cases remain|
|001212 orbit (three bracelets)|[Reviewed VALID allmetrics](research/lemmas/terra-001212-all-metric-periodic-escape.md):23 functional fibres; remaining AAA geometry forces equal A angles|Equal-angle/120 loci remain|
|010212 orbit (three bracelets)|[Reviewed VALID allmetrics](research/lemmas/terra-010212-all-metric-periodic-escape.md):all outer-completable fibres have H1/H2 omission escape|Equal-angle/120 loci remain|

[Single-cross-palette fresh review](research/reviews/two-hexagon-single-cross-palette-fresh-hostile-review.md)
is VALID; its earlier root audit remains separate. Its fixture-angle closure
scope was narrowed and an independent all-generic-angle proof added. It is
superseded for coverage by the broader012012 theorem, not repeatedly re-audited.

The requested012012 equality refinement covers all52 partitions:34 formally
allowAAA but closure leaves only L=P=Q,M=V and its all-equal merge; all other32
exact AAA strata are geometrically empty. The18 noAAA strata are covered
wheneveractualpolygons exist. The five minimal patterns are P=L,Q=L,V=M,
(M=P,Q=V),(M=Q,P=V); furthercoarsenings were explicitly checked.
[Certificate](research/certificates/terra-ternary-aaa-equalities.json).

### Reusable transfers and exact counterexamples

- [Reviewed singleABB resonance removal](research/lemmas/two-hexagon-opposite-a-resonance-removal.md):56 triples give12 resonance lines; six have one extraABB star. Zero-tile cornerpotential makesextra stars O(R); a zero-core limit transfers native coverage. Type-constant potentials preservingall5corestars cannot removeextra stars onthe other6lines. No complete-angle-grid/jointmetric implication.
- [Reviewed ETE zero-star lemma](research/lemmas/nonnegative-corner-potential-zero-star-limit.md). The unrestricted additive zero-SCORE extension and its separate extraction have [fresh independent VALID review](research/reviews/terra-unrestricted-corner-potential-review.md). Coalescing stars preserve scores, not contactcombinatorics/trivalence.
- [Reviewed001122 AAA counterexample](research/counterexamples/terra-generic-aaa-does-not-force-monohedral.md) refutes AAA=>monohedral outside012012. Its exact fixedmetricpair family is [closed by periodic omission](research/lemmas/terra-001122-fixed-fixture-periodic-escape.md), now superseded for coverage by general001122.
- [Reviewed rational-unit actualA001122/B001221 geometry and48-ring obstruction](research/counterexamples/two-hexagon-closed-generic-pair-native-seam-gate.md): bothpolygonsareclosed/convex/nonmonohedral but pairisUNTILEABLE. Eachring has onea/c andoneb/c mismatch. This falsifies central-only Bclosure extrapolation, while illustrating actualpolygons≠plane tilability. Ten reciprocalresultants include6zeros; no further root search needed after nativecoverage. High-degree originalslice was interrupted for arithmeticcost; low-degree slice completed6roots exactly.

### Construction track: coverage, blockers, reopening conditions

- [Deformed source dual pentagon](research/lemmas/penrose-dual-single-fusion-deformation-gate.md), tau=1/100: exactconvex/nonmonohedral local polygon, reviewedVALID. Centered predecessor hasType1periodic escape. Localpatch≠infinite two-shape covering.
- [Reviewed14-angle inventory](research/reviews/penrose-dual-fusion-angle-palette-fresh-hostile-review.md):35 fully surrounded sourcepoints/26anglevalues/six signatures/1296unions excludes totalnativecorners≤13 forfixedpoint-preservingdegree3/4 compiler. Matching deletions can fuse chains, notjustpairs. Boundaryerrors and retained-point hypotheses repaired and reviewed.
- **Independently reviewed VALID:** [exteriorbudget837>720](research/lemmas/penrose-fixed-point-two-shape-exterior-budget-obstruction.md) strengthens that compiler exclusion to ANYtwo genuineconvexpolygons regardless sidecount. Same1296 unions,26 exactalgebraic integerdegree lowerbounds; repeatedcorners onlyconsume more4pi budget. The reviewed open-interval extension retains bound811>720; the wholeparameterfamily is NOT classified. Allowing straight degree2 collapses initially passes localbudget605, but sharededge arcconsistency forces11 classes with budget750>720, reviewed VALID in [the strengthened gate](research/lemmas/penrose-dual-straight-collapse-shared-edge-obstruction.md). Its open-interval bound739>720 is reviewed; degree0 deletion/newpoints/cuts remain outside.
- [Reviewed anchored Ammann count/fixedcontent obstruction](research/lemmas/ammann-anchored-count-split-fixed-cluster-obstruction.md):H↔thin,P1↔P2↔thick exactbijections andsourcehierarchy givephi:phi:1. Singletonpent+onefixedcontentmacro impossible forANYpartner size. Anytwo fixedcontentclasses musteach haveequalP1/P2counts. A new [uniform-resection obstruction](research/lemmas/ammann-supported-pair-uniform-resection-obstruction.md), fresh independently reviewed VALID, forces EVERY dissection balanced and contentunique for ANY tileable two-macro pair at ANYG*. Variablecontent rescues and singletoncompilers close throughoutG*; cuts and balancedtwocluster geometry remainopen; no unproved fixedfrequencyassumption fromold Euler note used. [Basic repairedfusion theorem review](research/reviews/convex-cluster-fusion-basic-fresh-rereview.md)VALID; its ancillary statements retainseparate gates.

The [freshly reviewed synthesis](research/lemmas/two-hexagon-complementary-ternary-distinct-all-native-escape.md) covers all121 native pairs, arbitrary actual metrics, and six soleABB resonance lines; equal-angle/120 loci remain. A fully reified angular exclusion passed [fresh hostile review](research/reviews/two-hexagon-ternary-angular-filter-fresh-hostile-review.md),8100 native arrangements,12 CP controls,24 resonance/grid controls and6 API boundaries. The [one global query](research/searches/two-hexagon-ternary-filtered-global-query.md), SAME radius3/grid5394/60second cap, returned UNKNOWN. No witness/invariant/globalcoverage follows; no cap increase. Reopen global CP only with concrete new pruning/domain decomposition.

**Fresh independently reviewed VALID balanced-macro invariant:** no180 native-angle relation atG* forbids flat boundary vertices and T-junctions in a convex whole-source support. Balanced content(h,k,k) then makes its genuine side count even, [reviewed proof](research/lemmas/terra-ammann-balanced-convex-macro-parity.md). This excludes pentagon macros at ALL cluster sizes; no minimal-cluster enumeration was needed. Combined convex whole-source construction would reduce to (6,6), so a distinct pentagon route must change cuts/sourcepoints/sourcegenericity.

**Changed multiplicity track:** B has five r corners and one s corner on the
specified ABB line. Its degree-two saturated-chain extraction has independent
VALID review. The original [A012012 row lift](research/lemmas/terra-five-one-opposite-a-row-periodic-lift.md)
and palette exclusions are now part of the complete eleven-word coverage below; their
old assignment of eight further words is superseded.

**Changed cut construction:** an exact H-midpoint chord yields two genuine convex pentagons, both outside15 monohedral families, but retained-source-boundary covering fails. The [fresh reviewed area-module theorem](research/lemmas/ammann-source-by-source-two-area-module-obstruction.md) excludes EVERY source-by-source two-target compiler at rank3 sources; at J0 primitive area kernel(-71,120,-80) forces EACH H targetcount divisible40, excluding ALL H chordcuts and all<40-piece cuts, independent of endpoint tuning. No40/80-piece enumeration is justified. Cross-boundary reassembly, other module-compatible parameters and changed sources remain outside; a concrete geometry proposal is required before reopening.

### Complete B5+1 native-family coverage

**All eleven native A words now have independently reviewed all-metric
coverage.** The [whole-family synthesis](research/lemmas/five-one-complete-native-all-metric-periodic-escape.md)
has a [fresh independent VALID review](research/reviews/five-one-complete-native-all-metric-synthesis-review.md). The [full strict-convex angle-line review](research/reviews/five-one-full-strict-convex-angle-line-extension-review.md)
extends the first nine mechanisms to 108 < x < 126, x != 120; the two new
used/unused seam proofs apply directly on that full interval. The parameters are
A angles x, y = 720 - 5x, z = 4x - 360 (twice each), and B angles
r = 360 - 2x (five times), s = 10x - 1080 (once).
For each actual strictly convex metric, tileability implies a periodic escape
in the unrestricted problem, including reflections, partial contacts and
omission. The original tiling need not itself be periodic or trivalent.

| Native A words | Reviewed coverage mechanism |
| --- | --- |
| 001221, 011022 | [Endpoint-palette exclusions](research/lemmas/terra-five-one-b-saturated-chain-reduction.md) |
| 002112, 012012, 012102 | [Three-word all-metric interface escape](research/lemmas/five-one-three-native-word-all-metric-interface-escape.md) |
| 001212, 011202 | [001212 boundary resource exclusion](research/lemmas/terra-five-one-001212-universal-boundary-exclusion.md), [011202 boundary resource exclusion](research/lemmas/terra-five-one-011202-universal-boundary-exclusion.md) |
| 010212, 012021 | [010212 empty interface](research/lemmas/five-one-010212-all-metric-interface-escape.md), [012021 empty interface](research/lemmas/five-one-012021-all-metric-interface-escape.md) |
| 001122, 010122 | Actual used-AA22 seam gives a monohedral escape; [unused-AA22 support gives a binary periodic lift](research/lemmas/five-one-all-mask-no-cross-periodic-escape.md) |

**The formerly residual all-mask words 001122 and 010122 are closed.** The
[001122 used-AA22 seam theorem](research/lemmas/terra-five-one-001122-full-cross-22-escape.md)
has [independent VALID review](research/reviews/terra-five-one-001122-full-cross22-luna-hostile-review.md).
An actually used whole AA seam involving native side 4 (22), whose endpoints
are forced rainbow AAA stars in the extracted four-star field, gives a
monohedral periodic escape by A. The exact finite check covers 96 necessary
seam configurations and all 203 side partitions: 40 of 41 admissible
coarsenings have an H2 escape; the remaining one has no positive closure.
Length equality alone does not establish that such a seam is used.

The [all-mask support theorem](research/lemmas/five-one-all-mask-no-cross-periodic-escape.md)
now assumes absence of AA22 in the actual extracted tiling and permits every
metric alias. The [fresh independent review](research/reviews/five-one-unused-aa22-support-fresh-hostile-review.md)
validates its sparse limit, species recurrence, B-fibre collapse and geometric
lift, together with the [001122 all-metric synthesis](research/lemmas/five-one-001122-all-metric-periodic-escape.md).
For [010122](research/lemmas/terra-five-one-010122-full-cross-22-escape.md),
all 96 used-seam cases and all 71 compatible side partitions force H1/H2;
its [independent review](research/reviews/five-one-010122-cross22-fresh-hostile-review.md)
is VALID. The used/unused alternatives exhaust one actual saturated field;
length equality is never treated as evidence that a seam occurs.

The whole-family review checks the complete fixed-colour eleven-word split,
component scope and original quantifiers. This closes the stated B5+1 angle
line at all actual metrics, not arbitrary hexagon pairs. Equal-angle x = 120,
degenerate endpoints, other angle multiplicities and general pentagon pairs
are outside this synthesis. There is no surviving aperiodic pair here.

The older A002112 nonmonohedral AAA fixture, 42-partition closure ledger and
positive local B/BB cells remain valid retained artifacts, but are superseded
for coverage by the universal interface theorem. Do not resume A002112 AAA
metric-cone enumeration, or the now-completed four middle-word assignments.
The earlier five-of-eleven and nine-of-eleven frontiers are superseded by this table;
its working provenance remains in the
[historical log](research/searches/discovery-log-2026-10-13-working-history.md).

**Changed cross-boundary construction:** knowninfinite H/D precursor(Hsingle,D=P1+P2cpartners) is nonconvex. [Freshreviewed local incidence obstruction](research/lemmas/ammann-hd-incidence-preserving-convexification-obstruction.md) excludes ANYincidence-preserving convexification: anHH r-seam farendpoint forcesoneHwithK-typeJ'andL-typeJ'', bothdegree2afterpairing, soonefinalclasshas≤4cornersandperiodicomissionescape. Initialclaim'allHJ''L'wasfalseandrepairedusingalternateJstar; nofrequency/primitivityassumptionneeded. Reopeningrequiresnewbranchingincidence/newthirdface/explicitfacecuts, notmorecapgeometry.

Current justified actions are the [construction portfolio strategy](research/searches/construction-portfolio-strategy.md),
which requires an exact infinite covering before extensive local shape search,
and targeted structural work outside the completed B5+1 line. The strategy
has an [independent review](research/reviews/construction-portfolio-strategy-independent-review.md)
with its decoder and finite-scheme stopping clarifications integrated. It is
a strategy, not execution of new construction searches. Pause the completed
B5+1 family rather than automatically sweeping adjacent parameters.

The unchanged bounded global query remains inactive after UNKNOWN; reopening
it requires new pruning or a concrete domain decomposition. No automatic
timeout or bound increase is justified. Other angle families and general
pentagon pairs remain unresolved.

### Current consolidation and verification checkpoint

The [consolidation audit](research/reviews/frontier-consolidation-2026-10-13.md)
records the corrected frontier, superseded assignments and nondestructive
registry decisions. Fourteen checks were added: exact boundary/resource,
used-AA22 and unused-support obligations, retained local controls, a four-face
pentagon carrier and seven positive metric tori. All fourteen passed targeted
registered replays. The registry now contains 43 producer/certificate pairs
and 223 verifiers, 266 checks total. Producer outputs are directed to temporary
storage or explicit read-only `--check` modes. Legacy fixed-path writers and
non-failing diagnostic scripts remain excluded for the documented reasons.

The complete disposable replay **PASSED all 266 checks** with assertions
enabled and confirmed that original research files were unchanged. The
[full replay output](research/reviews/frontier-full-replay-2026-10-13.txt) is retained.
Locked environment verification also passed, including exact package builds
and command provenance. The [root integration review](research/reviews/frontier-root-integration-review-2026-10-13.md)
records the independent reviews, scope checks and documentation repair.

This state is preserved in a local Git checkpoint containing the retained
research artifacts, reviewed eleven-word closure, replay registry and
construction strategy. No remote push is part of this preservation work.
Older statements below that the full suite was not rerun and that no
staging/commit occurred describe those earlier checkpoints. The full replay
checks retained finite evidence; it does not prove the unrestricted objective.

### Earlier preservation / literature / verification (historical)

[Targeted primary refresh](research/literature/2026-10-13-opposite-angle-coverage-boundary.md)
records Zhu–Wang–Yan,Healey andRao. Sparse-star removal is related toRao2017
Lemma2/Proposition3; no novelty of that mechanism claimed. No priority claim.
Exact certificates and no-author-import checkers are retained. The additional six collapse/capacity/row/area/angular controls passed nondestructively. [Targeted compiler literature refresh](research/literature/2026-10-13-uniform-resection-and-convex-compilers.md) records a convex eight-piece sigma-morphic forcing template, which permits periodic tilings; no two-shape construction or priority claim. New checks are
registered inresearch/searches/verify.py and replayed nondestructively; all six new native-family/exterior-budget checks passed nondestructively. Thefull registered suite hasNOTbeen rerun. Sourceparse,
JSON/currentlink andgitdiff checks passed at priorcheckpoint; repeatafternew
proofintegration. No staging, commit orpush. Intermittent subagentservice capacity failures didnot stoproottools or mathematical work. Mise auto-install later failed for unrelatedPuppeteer provenance; retained MISE_AUTO_INSTALL=0 skips unrelated installation withoutalteringtrustpolicy orresearchenv, and workcontinued.

Follow [main_prompt.md](main_prompt.md) and [research-protocol.md](research-protocol.md).
Run shell tools through Conda `arisearch`. Rotations, reflections, partial
contacts and omission of a species remain allowed. The
[corrected literature boundary](research/literature/2026-10-11-convex-aperiodic-boundary.md)
recognizes Healey 2011 as the three-convex-tile benchmark under its stated
conventions. The repository's Ammann proof is a verification/strengthening,
not a new three-tile discovery. No fresh literature search is claimed here.

## Current audited results (2026-10-12)

The audit round is complete. The reviewed family closures below do not resolve
the unrestricted problem. Solver caps and UNKNOWN outcomes remain individual
computational records, not mathematical negative results.

### Reviewed general tools

- [Full-state one-B ring reduction](research/lemmas/two-hexagon-one-b-ring-spatial-reduction.md):
  exact species coset and overlap lifting; sound finite pruning; one functional
  direction gives a genuine period. The two-basis full-period index bound is
  an upper bound. Complete-wheel propagation explicitly checks diagonal and
  inverse identities. The full-A-tuple quotient forgets only central B labels
  and supplies periodic escapes via canonical lifts. Independent reviews VALID.
- [Periodic binary equality fibre](research/lemmas/periodic-binary-equality-fibre-lifting.md):
  signed-cycle translation gains give a finite periodic cover whenever a
  periodic binary side-matching fibre has any solution. Pins and nonprimitive
  rank-one stabilizers are included; twice the base period need not suffice.
  Fresh review VALID.
- [Hosted-contact corner capacity](research/lemmas/hosted-partial-contact-corner-capacity-obstruction.md):
  forced hosted flat stars can exhaust native A/B corners. Finite-window
  resource injections contradict area growth without FLC or density assumptions.
  Fresh review VALID.
- [Shortest side with non-flat endpoints](research/lemmas/shortest-side-nonflat-endpoint-obstruction.md):
  a minimum side whose endpoints cannot lie on flat stars must whole-match an
  equal-length side. Fresh review VALID.

### Completed unique-B-star hexagon family

[Whole geometric theorem](research/lemmas/two-hexagon-unique-b-star-impossibility.md)
is independently VALID: when every exact triple is2A+1B and each B corner
has one allowed A pair, tileability implies a periodic escape for arbitrary
actual metrics, irrational angles, reflections and original partial contacts.
Corner balance and exact closure give268 graphs/eight component types and
11850 native orders. Complete census:11739 empty,77 functional,34 branching
covered by49 forced-metric periodic witnesses. The600 two-triangle subset is
fully covered. The12 hardest residues also have independently checked unique
wheels and commuting finite actions. Additional triples/multiple pair options
are outside this theorem. [Graph domain](research/lemmas/two-hexagon-unique-b-pair-graph-classification.md).
[Bounded literature refresh](research/literature/two-hexagon-one-b-spatial-boundary.md)
makes no priority claim.

### Complementary two-angle hexagons: broad restricted family

[Whole-family native-word synthesis](research/lemmas/two-hexagon-complementary-angle-native-word-reduction.md)
uses A angles3p+3(240-p), B angles3(360-2p)+3(2p-120),90<p<150,p!=120.
Its exact triple set has36 same-colour AAB stars, allowing multiple A pairs
per B corner. Native words are C=000111,I=001011,ALT=010101.

All nine native pairs are now independently discharged: four direct colour
empties, C/C periodic binary lifting, I/C and I/I geometric/spatial emptiness,
and all-metric I/ALT and ALT/ALT periodic escapes or emptiness. The full
ALT/ALT audit passed after its parameter provenance correction; the whole-family
synthesis has a fresh VALID review.

The corrected [I/C and I/I proof](research/lemmas/two-hexagon-interleaved-symbolic-closure-obstruction.md)
is VALID. Initial B=C direction coefficients were wrong; the old certificate
is explicitly withdrawn. Corrected matrices, exceptional roots/sign partitions
and96 residual native rings (all removed in one sound triangle round) were
independently reconstructed. The withdrawn local-only C claim is not used.

[All-metric I/ALT theorem](research/lemmas/two-hexagon-interleaved-alternating-all-metric-escape.md)
is fully independently checked:123 empty metric words,12 index-six native
tori,1 index-nine torus for equal odd A lengths. All even A lengths remain
independent. The last case also has a reviewed actual whole-plane
[triangular carrier](research/lemmas/two-hexagon-interleaved-alternating-equal-odd-carrier.md).
The [private seams and complete AB alphabet](research/lemmas/two-hexagon-interleaved-alternating-private-seams.md)
include merged lengths and all reflections.

[All-metric ALT/ALT synthesis](research/lemmas/two-hexagon-alternating-all-metric-escape.md)
has passed independent complete-chain replay of the exact finite reductions:203 A-side
partitions/39628 necessary B words;137 A-only impossible partitions; all270
three-length joint cases impossible;20970 remaining words collapse under
colour-preserving D3 symmetries to685 joint geometry orbits;628 are uniformly
excluded by actual-class kernel equalities. The separately reviewed
[six-distinct-A-side local theorem](research/lemmas/two-hexagon-alternating-distinct-a-sides-obstruction.md)
removes all900 all-distinct word cases. Remaining37 orbits/828 words have
30 empty native cores and7 functional six-state cores. Raw states, intrinsic
profile aliases, all native constraints and deletion records are retained.
Seven direct index-three finite-action periodic witnesses are retained;
all seven have passed independent verification. ALT-specific matrices use
t=tan((120-p)/2), correcting the documented sign without changing matrices
or outcomes over the symmetric angle domain. No native
559872-state angle search or SAT negative premise was needed.

This is a restricted angle-family closure, not the global two-convex-tile
impossibility theorem. Other angle types and all general pentagon pairs remain.

### Ternary-angle extension

[Generic ternary star balance](research/lemmas/two-hexagon-ternary-angle-star-balance.md)
and [opposite-angle A endpoint-palette obstruction](research/lemmas/two-hexagon-ternary-opposite-a-palette-obstruction.md)
have a fresh VALID review. The former includes pure AAA/BBB stars and identifies
how these escape the earlier one-B coset reduction. For A native word012012,
when each A side-length class has a fixed endpoint-colour pair, propagation
eliminates mixed AAA stars and the remaining B ring would require a two-colour
B word, contradicting two corners of each of three colours. Thus tileability
implies a periodic escape in this metric domain. Cross-palette equal lengths
and other A native words remain open.

### Parallel construction: exact features and immediate failures

[Acute long-edge track](research/searches/acute-long-edge-construction-track.md)
retains the positive double-acute family, actual reflected modules and six-tile
periodic strip. Its cap operation arrests; of four natural full-c/B-a bridges,
two overlap neighboring-period A tiles and two fit locally. No plane covering
or unrestricted forcing survives. The old single-acute cap has a reviewed
zero-intensity corner-budget obstruction.

Hat compiler gates: the fixed eight-kite convex subsets and the horizontal
four-pentagon deformation are independently killed by monohedral periodic
escapes. The changed three-pentagon/one-hexagon cut has a valid convex partition
cone but no two-class point (six circle systems/eight points; review VALID).
Reflex native corners kill boundary-junction shifts before enumeration.
Two-interior-junction 2p2h cuts also have real convex partition samples, but
necessary side inventories eliminate their two-class metrics: the interior-T
branch has four nonconvex points (fresh review VALID); the horizontal branch
has an analytic angle/reflex contradiction (fresh independent review VALID).

[Acute/obtuse native-word obstruction](research/lemmas/acute-obtuse-native-word-untileability.md)
now excludes A=(65,140.5,147.5,75,112), B=(40,144.5,136,47,172.5)
at ALL actual side metrics. The proof excludes one full star geometrically,
then uses native side continuations and finite-window corner injections to
contradict area growth. Arbitrary partial contacts, reflections and all
possible vertex valences are included; no density assumption is needed.
Both the hostile review and a separate fresh independent audit are VALID.
The exact local caps remain valid patches, without infinite extensions.

[Reordered pentagon tileability criterion](research/lemmas/reordered-acute-pentagon-four-face-periodic-carrier.md)
closes A=(65,140.5,75,147.5,112), keeping B unchanged. Tileability is equivalent
to A0=B1,A2=B0,A3=B3; every such actual metric admits a periodic four-tile
plane tiling. Pointwise exclusion of the flat star forces whole contacts;
native continuation then forces those aliases. An initial host table omitted
eligible host endpoints ending inside outer rays. The repaired five-host
argument and full actual-metric flat-torus development passed a fresh
independent review. A separate exact strictly convex positive sample has also passed independent
review: exact closure, native angles, positivity, all30 strict supports and
the three aliases hold. The normalized two-parameter periodic metric region
is nonempty and open (a slice of the homogeneous length cone). This is a completed family closure,
not an active aperiodic construction.

The reviewed general six-piece convex-pentagon dissection theorem remains
stronger than the new angle-specific small-child cross-check. A new reviewed
[positive-conjugate substitution obstruction](research/lemmas/two-pentagon-positive-conjugate-substitution-obstruction.md)
excludes direct linear golden and silver inflation for ANY two convex
pentagons: positive quadratic conjugate forces positive replacement determinant,
which excludes one-child images and hence requires area inflation>=6.
No substitution claim replaces existence and forcing obligations.

### Replay coverage and next research obligation

The completed independent checks used by the main family closures and the
double-acute construction record are registered for nondestructive replay.
Additional historical and duplicate controls remain separately retained.
Targeted checks passed without overwriting retained certificates.
The full historical suite was not rerun. The complete ALT chain, whole
nine-case hexagon synthesis, and repaired pentagon carrier audits are finished
with VALID verdicts. The registered checks have nondestructive outputs and passed their recorded
replays.

[Regroup note](research/searches/regroup-smallest-unresolved-contact-mechanisms.md)
identifies a next narrow mechanism: one cross-palette A-side equality can
permit an AAB-to-AAA interface in the generic ternary hexagon language.
It supplies an exact convex A seed, but no B pair, infinite covering or
forcing proof. The next proposed step is a local transition-edge successor
lemma before enumeration. Construction still needs BOTH infinite existence
and shape-only forcing, including all reflected and unintended contacts.

## Retained earlier portfolio and restart gates

These preserve earlier scoped results and unresolved obligations. The current
priority and latest audited conclusions are stated above.

| Mechanism / status | Strongest retained result | Remaining obligation / exact restart |
| --- | --- | --- |
| **Global two-hexagon route — active inherited-escape/analytic-obstruction analysis** | The repaired SFT reduction has a [VALID fresh rereview](research/reviews/two-hexagon-global-repaired-reduction-rereview.md), conditional on reviewed structural dependencies. A single physical translation is preserved in a defect-free translated limit; the original tiling is not asserted defect-free. All **316 stored covering types of rank ≤3** have final UNSAT queries, **695 independently checked torus records**, and a second one-hot encoding giving 316 INFEASIBLE outcomes. The 100 partition types are a subset; the 216 extra rank-three types are already checked. | Rank **4..10** remains unenumerated. Continue from **all 27,373 stored flats**, including noncovering parents; minimal covering roots need not have a covering ancestor. Inherited coverage now extracted as 38 direct/554 symmetry supports; first 20-query refinement batch is inconclusive. Analytic corner potential supplies a reviewed 195-triple radius-12 empty region and a minimal rank-five covering root. Continue closure refinement from retained implications and retain noncovering parents. Stored ranks/closures were independently checked, but exhaustive regeneration of the flat enumeration was not. Solver infeasibility proof logs are absent. Angle-box feasibility is not joint polygon/side realizability. [Census and replay](research/lemmas/two-hexagon-global-census.md), [audit](research/reviews/two-hexagon-reduction-and-census-audit.md). |
| **Ammann three-to-two collapse — closed on the recorded domain** | Among the reconstructed-family strata with five-or-more-corner tiles, the unique computed admissible two-class point is J at the circumcentre of BCD; its centrally symmetric hexagon tiles alone, so that candidate is **Falsified**. Periodic-killed small-polygon strata are excluded from this uniqueness claim. The point has an [independent exact root check](research/reviews/verify_ammann_two_class_collapse_point_root.sage). The generalized ≤2-interior-point/9,604-rhomb-pair search found no further free-angle candidate. | Original reconstructed-family candidate exclusion now independently VALID via 130 full-distance systems. Literal uniqueness on periodic-killed small-polygon boundary strata is unclassified. Generalized exhaustiveness remains UNRESOLVED: negative graph/unit-ideal cases, sampled collinearity signs and slit convention. All 38 stored real-point rows independently checked. [New review](research/reviews/ammann-two-class-exhaustiveness-review.md). More points and changed decorations remain outside the domain. [Search record](research/searches/ammann-two-class-search.md), [coordinates](research/lemmas/ammann-two-class-reconstruction.md). |
| **Ammann three-shape forcing — completed reviewed verification** | [Lemma](research/lemmas/ammann-forcing-aperiodicity.md) is adversarially reviewed on G* = D ∩ (G1) ∩ (G2'): arbitrary contacts become edge-to-edge; reflections reduce to one handedness; an exact atlas reconstructs Penrose rhombs. [Repair rereview](research/reviews/ammann-forcing-repair-rereview.md) validates all eight repairs. | Non-generic parameters remain outside the theorem. This is not the two-tile target. The [mechanism analysis](research/reviews/ammann-mechanism-two-shape-survival.md) contains an **unresolved** Lemma S density argument; it must not be used as a proved reduction or as complete census coverage. |
| **Original P2 kite/dart recomposition — completed bounded exclusion, paused** | [Independent audit](research/reviews/kite-dart-exclusion-audit.md) and [VALID fresh rereview](research/reviews/kite-dart-exclusion-audit-rereview.md) close the 98-type/9,604-pair strictly-interior, source-edge-erased **varying-angle** domain. They checked 9,586 negative primal witnesses, 1,194 bounded faces, 660 metric options and 128 joint partitions. All four no-bounded-face templates are closed by empty-network/degree-one obstructions in the marked substitution-language hull. The unfinished direct flat branch is closed by an exact mirror transfer, not relabelled complete. | Isolated metric specializations, arbitrary bare kite/dart tilings, >2 points and neighbour dependence remain outside scope. Sage/Singular and Z3 trust remains; no formal UNSAT proof logs. [Campaign manifest](research/certificates/penrose-kite-dart-campaign.json) retains commands, hashes and domains. |
| **Matched-endpoint P2 attachments — completed reviewed bounded exclusion** | 706 one-centre star recipes: 522 small-polygon escapes, 181 slits, one holed face and two weak-convexity failures. A one-chord enlargement checked 2,000 recipes: 1,262 small-polygon escapes, 604 slits, 34 multiple cycles, 100 degenerate faces; no survivor. Encoding controls independently check the two 136-face quotients and 495 endpoint instances. | [Independent hostile audit](research/reviews/kite-dart-edge-attachment-audit.md) now VALID: all 2704 rejection witnesses, 12 coordinate representatives, both weak-convexity queries and patch4 occurrence in the marked substitution hull checked. Shared Sage/Z3 trust and absent formal UNSAT logs remain. Changed higher-valence attachments need exact geometry before any enumeration. [Separate edge manifest](research/certificates/penrose-kite-dart-edge-campaign.json). |
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

## Preservation and verification checkpoint before resumption (2026-10-12)

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
index entry or commit. All research remained paused at that earlier checkpoint.

## Historical checkpoint: Active resumption checkpoint (2026-10-12)

Locked environment verification passed on resumption. The low-rank torus
library has 695 records but only 38 distinct direct (actual used triples,
actual glued side pairs) supports. The bounded global radius-3 queries completed
from `research/searches/two-hexagon-inherited-escape-query.py`, blocking all
symmetry images and learning exact rational-closure implications. This tests
inherited escape coverage without enumerating rank-four flats. Any residual
is a finite patch, not polygon realizability or a plane tiling.

Independent reviews of the Ammann collapse and P2 attachment exclusions and
a corner-star balance criterion completed; their exact findings and review
gates are integrated below. No closed-domain enlargement is inferred.

During this run mise began attempting to auto-install unrelated Netlify CLI
from external configuration, failing its provenance trust check. Commands
continue with `MISE_AUTO_INSTALL=0 mise exec -- conda run
--no-capture-output -n arisearch ...`; this skips unused tool installation,
uses the existing locked research environment, and changes no trust policy
or dependency configuration.

## Historical checkpoint: Corner-balance and inherited-escape mechanism

[Reviewed lemma](research/lemmas/two-hexagon-corner-balance-obstruction.md),
[root hostile review](research/reviews/two-hexagon-corner-balance-obstruction-review.md),
[exact minimal rank-five root](research/certificates/two-hexagon-corner-balance-obstruction-example.json).
The integer potential d=(0,0,0,-2,-1,2,0,0,0,0,-1,0) has species sums
(-1,-1). Its 195 nonnegative triples form a universal empty region for every
side relation. A radius-12 ball would require 469<=444; this is an analytic
finite empty certificate. Every obstructed subset and symmetry image is
excluded. Adding negative-potential triples may restore feasibility, so
obstructed parents still cannot be pruned from flat enumeration. All316
stored low-rank covering types pass the balance filter.

The [first radius3 query](research/certificates/two-hexagon-inherited-escape-radius3.json)
reached its20-iteration cap; all20 proposed physical supports acquire an
inherited torus after exact angle closure. The
[independent checker/review](research/reviews/two-hexagon-inherited-escape-review.md)
validates all695 source tori,38 direct/554 symmetry supports and20 rational
refinements; it does not reproduce intermediate solver assignments. Recorded
seed metadata was corrected to the actual CP-SAT default1 without changing
outcomes. Continuation adds all symmetry images of the analytic empty region
and starts from these implications; the second20-query batch also reached
ITERATION_LIMIT, leaving40 exact refinements retained. Independent replay
checks all40 implications and144 distinct symmetry empty regions. No higher-rank
census completeness, polygon realization or plane tilability follows.

## Historical checkpoint: Neighbour-dependent boundary-point mechanism

[Reviewed dual-spoke theorem](research/lemmas/penrose-boundary-dual-spoke-obstruction.md),
[fresh review](research/reviews/penrose-boundary-dual-spoke-hostile-review.md),
[exact local star](research/reviews/penrose-boundary-dual-trivalent-star.json).
Arbitrary interior points, shared edge-interior crossing points and full
spokes produce dual faces. Convexity forces degree-two crossings straight;
a single actual trivalent source vertex then forces a triangular final tile
and a monohedral periodic escape. This covers a neighbour-dependent
boundary-point mechanism outside the earlier strictly interior Ammann
domain. It assumes an actual source with that star; universal Penrose source
occurrence/repetitivity is not newly proved. Reopen only changed network
incidence or another explicitly used assumption, not a larger point search.

Six new registered verifiers passed through the nondestructive replay runner:
corner-balance example,130 Ammann distance systems,38 retained generalized
real-point rows,P2 attachment audit,40 inherited-query refinements,and the
exact dual-spoke star. Review-output writers now accept disposable paths.
The full registered suite was not rerun; no previous mathematical certificate
was overwritten by these targeted replays.

## Historical checkpoint: Complete angle-grid mechanism and current solver limits

[Reviewed grid theorem](research/lemmas/two-hexagon-complete-angle-grid.md),
[hostile review](research/reviews/two-hexagon-complete-angle-grid-review.md),
[constructive bound certificate](research/certificates/two-hexagon-complete-angle-grid.json).
Every rationally closed exact triple type has an exact representative on
integer-degree denominator5394; denominator323633 gives a representative
in(119,121). Integer kernel minors and a greedy forbidden-hyperplane
avoidance construction prove this uniformly, without enumerating all types.
The maximum deviation bound323632 is below60*5394=323640.

This makes `Query(grid=5394)` complete for the abstract angle relaxation,
eliminating iterative rational-closure refinements. It does not produce
actual polygons with a given length relation. The
[near-regular-grid trial](research/certificates/two-hexagon-complete-grid-radius3.json)
and [smaller complete-grid trial](research/certificates/two-hexagon-complete-grid5394-radius3.json)
both returned UNKNOWN at their explicit60-second single-worker query caps.
No infeasibility proof, live candidate, or geometric witness was obtained.
The [independent checker](research/reviews/two-hexagon-inherited-escape-check.py)
validates library/analytic-region metadata and supports exact numerator
checks if a later grid trial returns SAT.

The next global query should use5394, the inherited554 supports, the
144 distinct analytic empty symmetry regions, and any newly certified
spatial obstructions. Another longer identical timeout is not a new
mechanism. The balanced rank-five root being analyzed separately shows that
corner balance alone does not restore a covering low-rank ancestor; its
fixed native order requires actual spatial constraints.

## Historical checkpoint: Balanced higher-rank root and spatial gate

[Exact balanced rank-five root](research/lemmas/two-hexagon-balanced-minimal-covering-root.md),
[certificate](research/certificates/two-hexagon-balanced-minimal-covering-root.json).
T={(0,1,6),(1,2,7),(0,2,8),(3,4,9),(4,5,10),(3,5,11)} is closed,
rank5 and covering. Weights1/3 give species weights2/3 and1/3. Every B corner
occurs once, so every covering ancestor must equal T. This falsifies the
proposal that positive corner balance guarantees a covering rank<=3 ancestor.

The fixed native cyclic order has an internally checked solver-free local
obstruction: each B placement has a unique A-neighbour ring; the admissible
placements for mandatory successors in directions0 and1 are disjoint.
The angle-only SFT is empty for every side relation in this native order.
Radius2 and56 index<=8 torus controls are separately INFEASIBLE with no
formal solver proof logs. The [fresh hostile review](research/reviews/two-hexagon-balanced-minimal-covering-root-review.md)
and [independent solver-free checker](research/reviews/check_two_hexagon_balanced_rank_five_ring.py)
validate the finite spatial certificate. Non-dihedral corner reorderings are outside scope;
this root is no geometric or aperiodic candidate.

The complete-grid bound/table constructive verifier also passed its registered
nondestructive replay. Both complete-grid UNKNOWN records passed independent
library and analytic-region metadata checks; they contain no solved angle
vectors. All351 research Python sources and uncompressed JSON files parse;
current-log/grid links and `git diff --check` pass. No stage, commit or push
was performed.

## Historical checkpoint: Restart state after the resumed run

No research solver or checkpoint writer is running. The worktree contains the
new lemmas, certificates, independent reviews/verifiers and narrowed earlier
scope statements; no staging, commit or push occurred. No aperiodic pair or
unrestricted impossibility theorem has passed the acceptance gates.

Next steps proposed at this historical checkpoint (superseded by the current priority above):

1. Continue the complete-grid global angle query at5394 using the retained
   periodic supports and certified analytic/spatial empty regions. Improve
   branching or constraint propagation before increasing identical timeouts.
   Higher-rank flat enumeration still must retain noncovering parents.
2. Use the balanced minimal covering root as a test of spatial constraints;
   positive corner balance is insufficient. Any changed native-order candidate
   needs exact local realizability and a cheap periodic escape test before
   global forcing work.
3. Finish generalized Ammann negative-case/unit-ideal reconstruction and
   replace sampled collinear sign decisions by exact coefficient ratios.
   The original reconstructed candidate exclusion is already reviewed valid;
   broad generalized exhaustiveness remains open.
4. A new construction through boundary attachments must change the reviewed
   full-spoke/higher-valence obstruction assumptions with exact boundary
   data. The completed706-star/2000-chord exclusion is not a reason to enlarge
   those closed enumerations.

The two60-second complete-grid trials were UNKNOWN; the two20-query relaxed
batches reached their iteration caps. These are recorded computational limits,
not mathematical negative results. The general pentagon cases and unrestricted
higher-rank two-hexagon case remain unresolved. This checkpoint preserves the restart state. The previous response's claim
that a response-budget limit required termination was unsupported: no token
budget or execution-limit signal had been received. The bounded solver caps
did not require stopping the research under protocol Section19.

Final targeted registered replay of the independent balanced-root ring checker
passed; all eight newly registered checks have passed. Final Python/JSON
parsing, new-lemma/current-log links and whitespace checks pass. The full
registered suite was not rerun.
