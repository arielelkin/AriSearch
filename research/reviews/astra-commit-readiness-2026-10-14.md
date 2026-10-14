# Astra independent commit-readiness review

Date: 2026-10-14. Scope: the entire tracked and untracked change relative to HEAD, including earlier uncommitted construction cycles. Reviewer: fresh independent Astra reviewer; no author proof/code/registry edits, staging, commits, pushes, solver searches, or child agents.

**Verdict: READY after the documentation repairs recorded below.** This is readiness to commit scoped partial research, not acceptance of a solution. The unrestricted two-unmarked-convex-polygon problem remains unresolved. No global impossibility or novelty claim is certified here.

## Findings and repairs

No blocking mathematical or implementation defect was found in the reviewed changes. Four stale current headers required low-severity documentation repairs: the bipartite-tree and strip manuscripts still said review was pending, the altitude manuscript called its verdict pre-review, and the two-plus-two lemma called the full gate unresolved. Root replaced those with the actual reviewed statuses and closure links; I reread the replacements. Root also added later-status banners to the original directed-offset hostile review and the earlier Astra strategy assessment. Their historical UNKNOWN and then-open conclusions are preserved rather than rewritten as successful solver outcomes.

The older discovery-log section labeled “Current restart and verification state” also required historical labeling: its 347-check “current registry” was stale beside the actual 364-check checkpoint. This is a restart-state clarity issue, not an algebraic defect. Root relabeled the section as historical and changed the registry reference to that earlier checkpoint; I reread and verified both replacements. All requested documentation repairs are complete.

## Mathematical audit

The directed-offset closure is a complete exclusion for its explicitly restricted admissibility domain: shared mark-directed unit-base triangle rule, opposite two-donor/two-receiver source topology, 0<a_X,a_Y<1, positive heights, interior donor nodes, valid disjoint source-sector partitions, and strictly convex counterclockwise pentagonal outputs. It is not an exclusion of other offsets outside that declared domain, other partitions, or arbitrary convex pairs.

The role reflections reduce eight indexed outputs to four representatives without assuming both coloring roles occur. Both source species occur in the imported legal source. Two-class partitions of four representatives have only 2+2 and 3+1 forms; all four congruent is impossible by unequal source-pair area totals. The two crosswise 2+2 cases contradict those totals. The within-type case uses the squared-edge-sum invariant as well as area, forcing midpoint/common-height parameters. The homogeneous checkerboard carrier then gives an actual periodic single-species plane cover for each output class. A legal marked source is not needed for that counterexample, since the final polygons are unmarked.

For each 3+1 case the six equations are differences of area, squared-edge sum, and fourth-edge sum of the actual three polygons. The independent checker reconstructs these polygons rather than importing the producer. Its exact coefficient field is Q(sqrt(5)); t^2=(3-phi)/4 and h=t(x,y) eliminate the auxiliary trigonometric variable. No parameter-dependent denominator or extra ideal generator is introduced. I checked the generator construction and membership assertions: singleton T1 and K0 yield the unit ideal; singleton T0 yields x=(sqrt(5)-1)(y-1/2) and a quadratic negative on 1/2<y<1; singleton K1 yields a negative discriminant. The interval follows from positive h_X and the thin CD donor's interior condition h_Y<t. Convexity of the first quadratic makes the endpoint argument valid. Counterclockwise strict output geometry makes signed shoelace equality a necessary physical-area equality even under reflected congruence. These symmetric necessary invariants cover every cyclic/reversed correspondence; no unit-diagonal uniqueness assumption enters the closure.

The unit-chord filter has precisely eight maps and is correctly only a partial obstruction. Its remaining 32 alias maps are covered by the separate invariant proof, not silently discarded. The registered checker asserts ranks, solutions, and the positive invariant, rather than merely printing a symbolic answer. The computer-assisted proof still trusts exact SymPy polynomial algebra; it is not a separately formalized proof or a retained explicit Bezout certificate. The second reconstruction meaningfully reduces geometry/formulation risk, while sharing that algebra implementation. This is an accurately disclosed practical trust boundary, not a commit blocker.

The earlier common-triangle construction supplies an actual infinite two-class partition, then fails by periodic omission. The unequal-height variant supplies compatible partitions but at least three areas for every admissible unequal-height rule. Neither confuses construction from a marked source with intrinsic recognition of all unmarked tilings.

For the rational Y pair, the seven angle stars, five whole-side-compatible stars, and two flat stars have distinct scopes. Both monohedral omissions are excluded even with arbitrary partial contacts. The intact-parent obstruction is valid: its angles exceed 90 degrees, so T contacts and valence four are impossible, and its sole trivalent angle star has unmatched arm lengths. The mixed atomic pair's unrestricted existence is not inferred from this failed parent.

The whole-edge propagation proof follows one actual P reached across Q's GG4 side. Both R arms force its two A corners into ABG; the native AB5 far endpoints force its two B corners into ABG; the connecting BB2 then requires a nonexistent native GG2 mate. Reflections preserve those actual incidences. P-only is separately excluded. This proves no whole-native-edge plane cover, without a torus assumption or an infinite-frequency inference. Partial contacts can change the neighbor along BB, so they remain genuinely outside this proof.

The fixed 6P+4Q CP-SAT formulation uses exact squared lengths, sound face/slot relabelings, and the intrinsic reflection symmetries of P and Q. Its matching and corner-count constraints are necessary. The positive postcheck's link permutation and connectedness suffice for the claimed compact flat surface; no positive witness was returned. Its INFEASIBLE JSON is historical solver metadata, not a formal UNSAT certificate. The registered negative replay checks metadata and invokes the separate propagation checker without rerunning CP-SAT.

The strip theorem requires independent strip reuse, a finite complete boundary-state graph, a common horizontal period, bounded continuous graph boundaries, and positive gaps. Averaging around a cycle gives strictly positive vertical drift, so repeated cycles cover the plane with two independent periods even for irrational phase shifts. The explicit polygons already have periodic omission covers. This neither recognizes arbitrary hexagon tilings as rows nor classifies general two-hexagon pairs.

## Replay and provenance audit

The registry delta adds four certificate pairs and thirteen verifiers: from 58+289 to **62+302=364 checks**. There are no duplicate verifier paths. I inspected the new argument mappings: producer-style entries either emit JSON to stdout or use explicit read-only --check, the residual independent checker receives --ideals, the directed-offset fixture checker receives --fixture, and CP-SAT's replay cannot invoke its default writing/solving branch. Assertions remain enabled. The default CP-SAT research command can overwrite its output by design; it is not the registered replay command.

The three retained targeted transcripts cover all seventeen additions: 3 certificate replays+9 verifiers, then 1+1, then 0+3. I inspected those transcripts and source implementations; I did not represent them as a fresh full-suite run. All seven new JSON files parse. Their contents have different evidentiary roles: exact geometry/algebra outputs versus the explicitly historical NLSAT and CP-SAT run records. The historical NLSAT timeout and interrupted second branch are not transferred to the current stronger, unqueried support/separation encoding. That old exact solver input is not retained as an immutable standalone snapshot, so the history is a record rather than a byte-for-byte replay promise; no proof depends on it.

Fresh reviewer validation used:

```text
mise exec -- conda run --no-capture-output -n arisearch python research/searches/verify.py --only ammann-directed-offset-residual-independent-2026-10-14.py --only pentagon-y-no-full-edge-independent-2026-10-14.py --only ammann-directed-offset-gate-2026-10-14.py
```

Result:

```text
PASS certificate replay: ammann-directed-offset-gate-2026-10-14.py
PASS verifier: ammann-directed-offset-residual-independent-2026-10-14.py
PASS verifier: pentagon-y-no-full-edge-independent-2026-10-14.py
All 1 certificate replays and 2 verifiers passed; no certificates written.
```

These were selected to test the new exact closure, independent infinite whole-edge obstruction, and algebra-certificate integration. No new enumeration or full 364-check replay ran. All relative Markdown links in the changed/new documentation resolved; git diff --check passed. Environment/dependencies are unchanged. A fresh full disposable replay can be requested as a checkpoint policy choice, but nothing found here requires rerunning all historical research checks to validate this patch.

## Ranked next cycles

1. **One bounded incompatible two-parent incidence-design cycle.** Keep the concrete target H=2P+Q, K=P+2Q and phi H=2H+K, phi K=H+K, with P,Q convex pentagons and simple nonconvex H,K. The necessary atomic area ratio is 3phi+1. First supply complete planar incidence and oriented boundary words for all four dissections, including every seam endpoint. Bound the initial task to one candidate template and one adversarial audit; no coordinate census, child-count expansion, or substitution-depth search. Stop at a topological/angle contradiction, a closed palette, or failure to supply the template. Only a surviving explicit template earns a separately bounded exact support/closure/area solve. Exact expanding plane extension and universal geometric grouping remain separate later gates. This is a design task, not an existing candidate or a claim that the matrix can be geometrically realized.

2. **Conditional second mechanism: a split-edge fractional interface.** Change the actual shared-boundary rule: allow one marked subdivision point on a source edge and two separately assigned exchanged pieces instead of a single complete unit-base donor triangle. Before solving, specify one finite source-sector incidence template and all local role/arrow cases, showing exactly which piece is used once on each shared edge. Bound this to one topology, one interior subdivision per affected edge, and the resulting finite local case list; do not vary old offsets/heights or enlarge source patches. Reject immediately if outputs collapse to quadrilaterals, convexity fails, more than two congruence classes are forced, or the interface merely recodes the closed common-triangle topology. Use exact area/edge invariants before nonlinear solving; stop at UNKNOWN rather than extending time. A two-class survivor must face explicit homogeneous-carrier omission and intrinsic chord/subdivision decoding attacks before any larger work. No viable such incidence template is currently supplied; this earns at most a design cycle alongside the first, not a full construction-search fleet.

3. **Preserve Y partial contacts as an optional analytic challenge, not another torus census.** The concrete question is whether flat stars rr and bc can interrupt the reviewed native BB contradiction in a globally consistent repeatable seam. A first bounded task should trace a single split-BB seam and its two adjacent native corners, with at most one interior breakpoint, exact reflection/flat-sector alternatives, and a declared length/endpoint system. Stop with a scoped impossibility or an exact local seam witness; the latter does not establish plane existence. Do not interpret failure in this one-breakpoint domain as unrestricted untileability, and do not grow face counts without a new extension mechanism.

Do not restart fixed P5/Q14, excluded mixed-angle words, quadrilateral fans, whole-edge Y quotients, directed-offset 3+1 aliases, or independently reusable finite-state periodic strips. Keep the unrestricted two-hexagon question open without funding a generic larger census. The main missing result remains an actual admissible two-shape infinite covering together with shape-only forcing for every tiling, including reflections, omissions, and partial contacts.

## Reviewed file inventory

The governing problem, protocol, AGENTS.md, and discovery log were read for scope. The inventory below covers all 50 pre-review changed/new files: two tracked modifications and 48 untracked artifacts. New certificates were inspected for schema/provenance and against their generators and retained replay evidence; fresh replay was limited to the three checks above. Existing imported source theorems and older families were checked as dependencies and scope, not re-proved wholesale. This review itself is the 49th new artifact.

### Tracked modifications

- `discovery-log.md`
- `research/searches/verify.py`

### research/certificates/

- `research/certificates/ammann-bipartite-tree-pentagons-2026-10-14.json`
- `research/certificates/ammann-directed-offset-gate-algebra-2026-10-14.json`
- `research/certificates/ammann-directed-offset-gate-historical-run-2026-10-14.json`
- `research/certificates/ammann-mark-altitude-gate-2026-10-14.json`
- `research/certificates/pentagon-y-6p4q-flat-torus-cpsat-2026-10-14.json`
- `research/certificates/pentagon-y-interface-2026-10-14.json`
- `research/certificates/two-hexagon-sawtooth-strip-cycle.json`

### research/lemmas/

- `research/lemmas/ammann-directed-offset-three-plus-one-obstruction-2026-10-14.md`
- `research/lemmas/ammann-directed-offset-two-plus-two-obstruction-2026-10-14.md`
- `research/lemmas/ammann-directed-offset-unit-chord-filter-2026-10-14.md`
- `research/lemmas/pentagon-y-full-edge-torus-balance-2026-10-14.md`
- `research/lemmas/pentagon-y-whole-edge-native-propagation-2026-10-14.md`
- `research/lemmas/two-hexagon-repeatable-strip-cycle-2026-10-14.md`

### research/reviews/

- `research/reviews/ammann-bipartite-tree-pentagons-2026-10-14-hostile-review.md`
- `research/reviews/ammann-directed-offset-hostile-review-2026-10-14.md`
- `research/reviews/ammann-directed-offset-independent-2026-10-14.py`
- `research/reviews/ammann-directed-offset-residual-hostile-review-2026-10-14.md`
- `research/reviews/ammann-directed-offset-residual-independent-2026-10-14.py`
- `research/reviews/ammann-directed-offset-residual-targeted-replay-2026-10-14.txt`
- `research/reviews/ammann-directed-offset-targeted-replay-2026-10-14.txt`
- `research/reviews/ammann-mark-altitude-independent-2026-10-14.md`
- `research/reviews/ammann-mark-altitude-independent-2026-10-14.py`
- `research/reviews/interface-construction-2026-10-14-integration-review.md`
- `research/reviews/interface-construction-2026-10-14-targeted-replay.txt`
- `research/reviews/pentagon-y-equal-count-torus-obstruction-2026-10-14.py`
- `research/reviews/pentagon-y-full-edge-balance-hostile-2026-10-14.md`
- `research/reviews/pentagon-y-full-edge-balance-hostile-2026-10-14.py`
- `research/reviews/pentagon-y-interface-2026-10-14-hostile-review.md`
- `research/reviews/pentagon-y-interface-2026-10-14-independent.py`
- `research/reviews/pentagon-y-no-full-edge-hostile-2026-10-14.md`
- `research/reviews/pentagon-y-no-full-edge-independent-2026-10-14.py`
- `research/reviews/two-hexagon-strip-cycle-independent-2026-10-14.md`
- `research/reviews/two-hexagon-strip-cycle-independent-2026-10-14.py`
- `research/reviews/verify_ammann_bipartite_tree_pentagons_independent.py`

### research/searches/

- `research/searches/ammann-bipartite-tree-pentagons-2026-10-14.md`
- `research/searches/ammann-bipartite-tree-pentagons-2026-10-14.py`
- `research/searches/ammann-directed-offset-gate-2026-10-14.md`
- `research/searches/ammann-directed-offset-gate-2026-10-14.py`
- `research/searches/ammann-directed-offset-residual-invariants-2026-10-14.py`
- `research/searches/ammann-directed-offset-unit-chord-check-2026-10-14.py`
- `research/searches/ammann-mark-altitude-gate-2026-10-14.md`
- `research/searches/ammann-mark-altitude-gate-2026-10-14.py`
- `research/searches/astra-construction-portfolio-assessment-2026-10-14.md`
- `research/searches/pentagon-y-6p4q-flat-torus-cpsat-2026-10-14.md`
- `research/searches/pentagon-y-6p4q-flat-torus-cpsat-2026-10-14.py`
- `research/searches/pentagon-y-interface-2026-10-14.md`
- `research/searches/pentagon-y-interface-2026-10-14.py`
- `research/searches/two-hexagon-sawtooth-strip-cycle.py`

