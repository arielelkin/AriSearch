# Autonomous discovery of a novel unmarked aperiodic protoset

This prompt has one objective: discover and formalize a genuinely new finite
set of unmarked planar shapes that forces aperiodicity by geometry alone. The
resulting tiling space must be suitable both for exact implementation as a
`TilingSpec` generator in this repository and for development into an academic
paper.

## Required result

Find a finite protoset `P` of unmarked simple polygons that is plausibly new to
mathematics within a documented literature-search boundary and prove that `P`
is aperiodic in the strong shape-only sense defined below.

Assume for purposes of this task that a qualifying construction is within
reach. Do not substitute a literature survey, implementation of a known
tiling, negative result, reusable research tool, list of future directions, or
cosmetic variation for the required result.

A finite rendered patch is evidence about a construction; it is not itself a
hull or an aperiodicity proof. The mathematical object must be defined
independently of the software.

## Target object and aperiodicity

Let `P = {P₁, …, Pₖ}` be a finite set of congruence classes of unmarked simple
polygons with exact coordinates. A `P`-tiling is a covering of the Euclidean
plane by congruent copies of members of `P` with pairwise disjoint interiors.
Unless geometry itself forces a restriction:

- translations, rotations, and reflections are all permitted;
- tiles are two-sided;
- contacts are unrestricted and need not be edge-to-edge; and
- there are no colors, arrows, labels, markings, adjacency tables, matching
  rules, selected vertex atlases, or other supplementary placement rules.

Let `X(P)` be the complete space of all `P`-tilings with the local tiling
topology and translation action. The protoset `P` is **aperiodic** exactly when:

1. `X(P)` is nonempty; and
2. every `T ∈ X(P)` has no nonzero translational symmetry.

This definition quantifies over every tiling admitted by the shapes, not only
the tilings produced by a favored generator. If `X(P)` contains multiple
local-isomorphism classes, orbit closures, or minimal components, identify
them rather than silently calling a selected component the whole hull. Every
component must still be nonperiodic for `P` to qualify.

A new exact method for discovering or certifying such protosets is an
independent success condition. It qualifies on either of two grounds:

- it includes a proved constructive theorem that produces at least one
  explicit qualifying `P`, instantiated both mathematically and as a
  `TilingSpec`; or
- it decides a question previously undecided for a named, exactly encoded
  class — for example, an exact procedure that certifies or refutes shape-only
  aperiodicity for a stated finite encoding, permitted isometries, and contact
  model, with proved soundness and a stated completeness boundary.

A method claimed on the second ground must be validated against known ground
truth: it must return the correct verdict on established unmarked aperiodic
protosets and on shapes known to admit periodic tilings, and those runs must
be reproducible from the recorded commands. Solver plumbing, a faster search,
or a reimplementation of a published procedure does not qualify.

## What counts as new

Substitution, fusion, multigrid, cut-and-project, symbolic matching rules,
geometric matching-rule compilation, SAT/CSP, and other established
techniques are permitted as construction, search, or proof tools. Their use
neither qualifies nor disqualifies a result. The mechanism itself need not be
new. What must be new is the unmarked aperiodic protoset and its complete
shape-admitted tiling space, or a discovery or certification method qualifying
on one of the two grounds stated above.

A substitution or cut-and-project construction may prove that `X(P)` is
nonempty by generating one tiling. It proves shape-only aperiodicity only if
every tiling in `X(P)` is shown to obey enough forced structure to exclude
periodicity. Symbolic marks may be used internally, but the final polygons
must enforce the required structure without those marks. Any compilation of
rules into geometry must prove that no unintended fits or periodic escape
tilings remain.

Novelty of the hull alone is not enough, because arbitrary new symbolic rules
can generate mathematically routine new tiling spaces. State the substantive
frontier advanced by `P`.

Small cardinality is not itself a frontier. An unmarked aperiodic protoset is
already known at `k = 1` and at `k = 2`, and no convex polygon forms an
aperiodic protoset on its own, because every convex polygon that tiles the
plane also tiles it periodically. Confirm the current state of each of these
during the novelty audit rather than assuming it; the point is that a smaller
tile count is not available as the advance.

Frontiers that do qualify include:

- unmarked aperiodic protosets of **convex** polygons, in particular the open
  two-convex-polygon case and any three-convex-polygon claim under the
  two-sided, unrestricted-contact model defined above;
- a forcing mechanism that is not hierarchical or near-hierarchical, since
  every established construction forces through a hierarchy;
- an aperiodic protoset carrying a proved additional geometric restriction,
  such as exact rational coordinates, membership in a named polyform class, or
  a bounded corona depth;
- a new parameterized family with proved changes of hull invariants across the
  family; or
- a new theorem about the complete shape-admitted space `X(P)` of an existing
  or new protoset.

An arbitrary fresh substitution or Wang system compiled mechanically into
jigsaw edges does not qualify merely because its hull has not been named
before. Compiling matching rules into unmarked geometry is a known technique,
so the compiled output is only as interesting as the frontier it advances.

The following do **not** qualify:

- a known hull newly added to this application;
- a different seed, phase, viewport, palette, or parameter choice inside a
  known hull;
- a newly written substitution or symbolic rule considered only as its own
  restricted legal tiling space, without unmarked polygon geometry that
  forces that space;
- a routine geometric encoding of arbitrary marked or symbolic rules with no
  substantive advance beyond producing another technically distinct hull;
- polygons that generate an interesting aperiodic subspace but also admit a
  periodic tiling or a tiling outside the claimed forcing structure;
- a marked protoset, an imposed edge-to-edge convention, forbidden
  reflections, or any other non-geometric placement rule;
- subdivision, recomposition, regrouping, collaring, relabeling, decoration,
  or geometric deformation of a hull in the audited comparison set when the
  result is mutually locally derivable from, shape-conjugate to, or otherwise
  merely a new presentation of that hull;
- a finite patch with no exact infinite construction;
- a construction that admits one interesting nonperiodic tiling but does not
  establish aperiodicity of all of `X(P)`; or
- an unimplemented idea whose essential compatibility, recognizability, or
  extension lemma remains open.

Using known objects as ingredients is allowed. The result qualifies only if
the resulting hull is materially different from every member of an explicit,
finite comparison set produced by the novelty audit. The comparison set must
contain the nearest hulls found in the searched literature and the relevant
hulls already represented in the repository. Prove a meaningful distinction
against each member of that set. Prefer a hull-invariant obstruction to mutual
local derivability or topological conjugacy, such as a difference in patch
language, complexity growth, entropy, dynamical spectrum, invariant measures,
frequencies, cohomology, or another precisely justified invariant. A visual
difference is never enough.

No claim of mathematical priority may exceed its search boundary. “Plausibly
new” means that a serious documented search produced the stated comparison
set and found no prior construction in the searched class. It is not a
universal claim about the entire literature or proof of priority.

## Mathematical acceptance gate

Do not promote or integrate a candidate unless all of the following survive
adversarial review:

1. **Exact definition.** Prototiles, coordinates, rules, and allowed
   isometries are finitely and unambiguously specified. Algebraic coordinates
   must have exact representations or exact defining equations.
2. **Existence.** An infinite tiling in `X(P)` is proved to exist. Arbitrarily
   large computed patches alone do not establish this.
3. **Global shape-only forcing.** Prove that every tiling in `X(P)` has no
   nonzero translational symmetry using the unmarked polygon geometry alone.
   The proof must cover reflections, unrestricted contacts, alternative
   assemblies, and every component of `X(P)`.
4. **Distinctness within the audited comparison set.** Enumerate the finite
   comparison set produced by the novelty audit. For every member, state and
   prove the invariant or structural argument that distinguishes the
   candidate. Do not infer distinctness from different-looking prototiles.
5. **Substantive advance.** State the nontrivial geometric, combinatorial, or
   dynamical frontier advanced by the protoset. Technical hull distinctness
   produced by arbitrary new symbolic data is insufficient.
6. **Discovery-method theorem, when claimed.** State its exact input class,
   output class, permitted geometry, contact model, proved soundness, and
   completeness boundary. Identify what is mathematically new about the method
   rather than its solver plumbing. If the method is claimed as a constructive
   route, instantiate it on the qualifying `P`. If it is claimed as a decision
   or certification procedure for a named class, report its verdicts on known
   ground truth with reproducible commands. Gates 3 and 5 apply to a claimed
   protoset; gates 1, 8, and 9 apply to a method claimed on its own.
7. **Exact implementation.** A deterministic generator emits valid finite
   patches as canonical `TilingSpec` values, centered at the origin, without
   gaps or overlaps. It can generate successively larger compatible patches
   from replayable parameters through `tiling-data-cli.ts`.
8. **Reproducibility.** Proof-related searches have exact finite domains,
   deterministic commands, retained artifacts, and independently checkable
   certificates where applicable.
9. **Novelty audit.** The search records databases, primary sources, query
   terms and citation trails, versions or dates, the classes searched and
   excluded, and the finite comparison set of closest constructions found.
   The distinctness claim is quantified over this set and no larger one.

Primitivity alone does not prove recognizability or aperiodicity. Numerical
agreement does not prove an exact identity. A stable rendering does not prove
an infinite tiling. Failure to find a periodic patch is not a proof of
aperiodicity.

## Research procedure

Read `AGENTS.md`, `readme.md`, `testing.md`, `docs/theory.md`, the tiling
registry, and the existing tiling generators before changing the repository.
Build a concise internal exclusion list of hulls and construction mechanisms
already represented. Do not turn it into a deliverable or bibliography.

Use Sol Ultra's agent delegation aggressively and dynamically. Begin with a
genuinely diverse portfolio of independent construction mechanisms. Do not
tell most agents a currently favored route, and do not allocate a fixed
number of agents to each idea.

The orchestrator is the sole Git writer: only it may branch, stage, commit,
merge, rebase, or push, and only on `discovery` or branches created from it.
Give concurrent agents nonoverlapping file ownership, and integrate their
returned artifacts yourself.

From the beginning, maintain
`workbench/discovery-log-<YYYY-MM-DD>.md`, using the run's start date. This is
a continuously checkpointed working log, not a result or final deliverable.
Organize it by mathematical mechanism rather than agent or chronology. For
each route record:

- the exact construction or rule definition reached;
- parameters, commands, code, certificates, and computed invariants worth
  retaining;
- literature matches or equivalences that killed a rediscovery;
- counterexamples and adversarial findings;
- the precise unresolved lemma or failed invariant on which the route
  stopped; and
- the exact state from which another run can resume.

Never describe the log or anything in it as a discovery merely because it is
recorded. When several agents converge on substitutions, recompositions, or
multigrids, redirect some toward genuinely different mechanisms. A route that
reduces the problem to a theorem-strength compatibility or recognizability
lemma is blocked until someone supplies a materially new way to prove that
lemma.

Separate construction from literature anchoring:

- construction agents should first develop exact mechanisms and invariants;
- literature agents should search current primary sources to kill
  rediscoveries and identify the nearest known hulls; and
- once a candidate survives the first novelty screen, deepen both its proof
  and its source audit.

Do not require any preselected paper as a starting point. Search the current
literature as needed, using primary sources rather than relying on a fixed
local PDF packet.

Require concrete returns from agents: exact rules, tile coordinates, proofs,
counterexamples to candidate lemmas, deterministic generators, invariant
computations, or checkable certificates. Reject vague progress reports and
attractive pictures without an exact infinite construction.

Keep independent adversarial review active. Give candidate definitions and
artifacts to fresh agents instructed to find:

- a known equivalent hull;
- a periodic escape;
- an illegal local fit, gap, or overlap;
- failure of extension from finite patches to the plane;
- non-recognizability or ambiguous hierarchy;
- a hidden reflection or chirality assumption;
- a floating-point dependency; or
- circular use of the desired hull theorem.

Do not stop when initial approaches fail. Preserve restartable mechanisms,
killed rediscoveries, partial lemmas, computations, and exact blockers in the
working log and use them to redirect the search. These records are research
state, not discoveries or final deliverables.

## Time and stopping rule

Spend at least eight hours of active construction, falsification, proof, and
novelty checking before considering a no-result termination. A missing exact
token meter is not a reason to stop early. If an actual system or context
limit forces an earlier stop, do not disguise partial work as success.

Return a successful result only after the complete mathematical acceptance
gate survives adversarial audit. Do not return a known construction, a
promising lead, a reduction with a missing central lemma, a tooling change, or
a “best effort” research report as the discovery.

If the run reaches its real execution limit without a qualifying protoset or
discovery method, return only a concise statement that none was found. Leave
the dated working log in a restartable state, but do not summarize or promote
it as the result. Do not modify product code merely to leave an artifact.

## Implementation policy

Mathematics comes before product work. Until a candidate passes the exact
definition, existence, preliminary distinctness, and preliminary novelty
gates, keep experiments narrow and outside product code.

Do not build generic validators, search frameworks, ontologies, databases, or
artifact systems in anticipation of a candidate. Add a tool only when a
surviving candidate requires it to decide a specific named ambiguity and
existing repository capabilities cannot do so. The tool is supporting
evidence, never the result.

A bounded, exactly specified search over an enumerated class is primary
research, not anticipatory infrastructure. Enumerating polyforms, coronas,
periodic-witness lattices, exact-cover or SAT instances, and candidate
protosets is a direct attempt at the required result, and building and running
such a search is permitted from the outset, before any candidate exists. Each
search must state its enumeration domain, tile encoding, permitted isometries,
and contact model exactly, and must retain its certificates and exact replay
commands in the working log. Launch long-running searches early and continue
construction, proof, and literature work while they run. Distinguish a
completed exhaustive search from a timeout or resource exhaustion. A search
harness is still not the result; only what it certifies can be.

Agents may install pinned dependencies when a concrete active experiment
requires them. Record the dependency, exact version, reason, and replay
command in the working log. Reuse existing integrations before adding another
one; in particular, this repository already has Google OR-Tools installed as
the `or-tools-wasm` node package, available for constraint, exact-cover, and
SAT work without any additional setup. Installing a dependency does not make
its surrounding infrastructure a research result.

After the mathematical gate is passed:

- implement the smallest pure, typed, deterministic generator needed to emit
  the candidate as `TilingSpec`;
- expose all mathematical behavior through stable CLI parameters;
- generate beyond the requested region and crop only when this preserves the
  claimed patch semantics;
- use exact arithmetic for combinatorial decisions and exact algebraic
  identities wherever the proof depends on them;
- add focused mathematical and regression tests; and
- complete `npm run smoke` and `npm run test`.

## Successful deliverable

Only a qualifying discovery receives a full deliverable. It consists of:

1. A paper-oriented `workbench/tiling-discovery-report.md` containing an
   abstract, exact definitions, main theorem, construction, proofs, comparison
   with the closest known hulls, novelty-search boundary, limitations, and
   stable primary-source citations.
2. The deterministic `TilingSpec` implementation and its CLI/URL replay
   contract.
3. Exact proof or search artifacts and commands needed to audit consequential
   claims.
4. Tests establishing deterministic compatible finite patches, topology,
   centering, and any finite invariants used in the paper.
5. Exact instructions for mathematical replay and visual inspection.

The dated discovery log remains a working research record. It is not part of
the claimed mathematical result, even when a successful discovery is made.

Begin now. Search for shapes that force a new aperiodic tiling space, not a
new restricted rule system or rendering of an old one.
