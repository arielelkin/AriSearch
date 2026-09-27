# Autonomous Mathematical Research Protocol

This document specifies how an autonomous research run must operate. It governs research procedure, delegation, logging, proof preservation, computation, adversarial review, reproducibility, repository use, and stopping behavior.

It does not define the mathematical problem or weaken its acceptance criteria. The authoritative mathematical target is stated separately in `research-problem.md`.

## 1. Governing documents

At the beginning of the run, read:

1. `research-problem.md`
2. this document;
3. relevant repository documentation and existing mathematical artifacts;
4. the current `discovery-log.md`, if one exists.

When the documents differ in role:

* `research-problem.md` governs what constitutes a mathematical solution.
* `research-protocol.md` governs how the search is conducted.
* `discovery-log.md` records the current restartable research state.
* extracted lemma, proof, certificate, and computation files contain stable research artifacts.
* a final report exists only after the acceptance criteria in `research-problem.md` have been satisfied.

Procedural instructions must never be used to weaken the mathematical target.

## 2. Research objective

Conduct an active attempt to resolve the problem stated in `research-problem.md`.

Do not substitute any of the following for the required result:

* a literature survey;
* an implementation;
* a collection of partial results;
* a promising candidate;
* a bounded computational experiment;
* a reduction with a central unproved lemma;
* a reusable research framework;
* an explanation of why the problem is difficult.

Partial results should be preserved accurately as research artifacts, but they must not be presented as a complete resolution unless they logically satisfy the problem’s acceptance criteria.

## 3. Root-agent responsibilities

The root agent is responsible for the global research strategy.

It must repeatedly:

* inspect the mathematical state of the run;
* maintain a diverse portfolio of approaches;
* identify duplicated effort and neglected mechanisms;
* distinguish genuine progress from attractive reformulations;
* extract stable mathematics from working notes;
* submit important claims to independent hostile review;
* redirect agents away from theorem-strength dead ends;
* preserve exact restart states;
* decide when computational work is mathematically justified;
* integrate surviving results into a coherent proof.

The root agent must not behave merely as a collector of agent reports. It must synthesize, challenge, compare, falsify, and redirect.

Prefer experiments with high expected information gain, e.g. a cheap counterexample search against a critical assumption is generally preferable to extending supportive evidence for a downstream claim.

## 4. Multiagent research strategy

Use available agent delegation aggressively and dynamically when tasks can be made genuinely independent, adversarial, specialized, or mechanically verifiable Select the most suitable available model for each subagent, balancing task complexity, required reasoning depth, speed, and cost.

Do not use a fixed allocation such as a predetermined number of agents for each approach.

### 4.1 Independent initial portfolio

Begin with genuinely different mathematical mechanisms. Choose families appropriate to the problem, which may include:

* direct construction;
* minimal-counterexample arguments;
* induction and reduction;
* structural decomposition;
* extremal methods;
* compactness;
* algebraic formulations;
* geometric invariants;
* topological or dynamical arguments;
* probabilistic or ergodic methods;
* symbolic dynamics;
* finite-model formulations;
* exact computational searches;
* classification;
* attempted counterexamples;
* literature reconstruction of nearby results.

Do not tell most initial agents which route currently appears favored. Preserve enough independence to prevent premature convergence on the same seductive reduction. 

### 4.2 Approach-family registry

Track work by mathematical mechanism, not by agent identity or superficial phrasing.

For each mechanism family, record:

* the exact object or formulation being studied;
* the strongest rigorously established result;
* the central unresolved obligation;
* known counterexamples;
* relevant scripts and certificates;
* literature equivalences;
* whether the route is active, blocked, falsified, superseded, or complete;
* what materially new idea would justify reopening it.

If many agents converge on one family, redirect some toward underexplored or incompatible approaches.

### 4.3 Concrete agent returns

Require agents to return concrete mathematical content, such as:

* exact definitions;
* explicit constructions;
* candidate coordinates;
* proved lemmas;
* derivations;
* equations;
* finite classifications;
* counterexamples;
* exact search formulations;
* deterministic scripts;
* independently checkable certificates;
* precise literature matches.

Reject:

* vague progress reports;
* general brainstorming without a mathematical object;
* unexplained optimism;
* claims that a global step is “routine”;
* diagrams without exact definitions;
* numerical agreement offered as proof;
* restatements of the target as a missing lemma.

### 4.4 Preserve incompatible approaches

Keep several substantially different routes active through multiple rounds.

Do not allow one route to dominate solely because it produces elegant intermediate mathematics. A beautiful reduction whose remaining lemma is equivalent in strength to the original problem is not close to completion.

Cross-pollinate approaches only after their independent development has exposed their real strengths and weaknesses.

## 5. Blocked-route policy

A route is blocked when its remaining obligation is theorem-strength and no concrete new mechanism for proving it is available.

Examples include:

* replacing the original conjecture with an equally broad compatibility lemma;
* assuming recognizability, extension, compactness, or periodicity at precisely the point where it must be proved;
* reducing the problem to another open conjecture;
* repeatedly gathering bounded computational evidence for an unbounded claim;
* reformulating a global existence problem as a finite-model conjecture without proving the finite-model property.

When a route becomes blocked:

1. state the missing lemma exactly;
2. explain why existing methods do not establish it;
3. preserve all reusable artifacts;
4. mark the route as blocked in `discovery-log.md`;
5. stop assigning agents to it unless someone proposes a materially new invariant, construction, theorem, or proof mechanism.

Do not continue a blocked route merely because it is currently the most developed.

## 6. Continuous discovery log

Create or resume:

`discovery-log.md`

This is a continuously checkpointed working log. It is not a proof, paper, final result, or chronological transcript.

### 6.1 Organization

Organize the log primarily by mathematical mechanism.

Suitable sections may include:

* definitions and global invariants;
* construction mechanisms;
* structural reductions;
* algebraic formulations;
* geometric mechanisms;
* local-to-global mechanisms;
* compactness and limiting arguments;
* periodic or finite witnesses;
* impossibility mechanisms;
* exact computational searches;
* literature equivalences;
* surviving candidates;
* blocked routes;
* killed candidates and failure certificates.

Adapt these headings to the problem.

Do not organize the main body by agent name or by a minute-by-minute history of the run.

### 6.2 Required contents

For each mechanism, retain:

* the exact state of the construction or theorem;
* parameters and definitions;
* strongest proved lemmas;
* dependencies;
* commands, scripts, certificates, and seeds worth preserving;
* counterexamples and hostile findings;
* literature matches that killed a rediscovery;
* the exact unresolved obligation;
* the reason the route stopped;
* the state from which a future run can resume.

Never describe an item as a discovery merely because it appears in the log.

### 6.3 Checkpointing

Update the log throughout the run:

* after a substantial lemma;
* after a candidate is killed;
* after an adversarial review changes a claim;
* after an exact search completes;
* before switching away from a major route;
* before any likely context or execution limit.

Do not wait until the end to reconstruct the research history from memory.

## 7. Extraction of stable mathematics

The discovery log must remain an index of active research state. It must not gradually become a draft monograph.

Extract a result into a separate artifact when any of the following holds:

* it has survived at least one independent hostile review;
* two or more active routes depend on it;
* its proof is too long to audit comfortably inside the log;
* it introduces definitions or calculations likely to be reused;
* it is a meaningful theorem or counterexample independent of the main target;
* losing it would materially damage restartability.

Store stable mathematical artifacts under paths such as:

* `research/lemmas/`
* `research/proofs/`
* `research/counterexamples/`
* `research/certificates/`
* `research/searches/`
* `research/reviews/`

Each extracted artifact must be self-contained enough to audit without reconstructing the argument from scattered log entries.

### 7.1 Lemma artifact requirements

A stable lemma file should include:

* exact theorem statement;
* hypotheses;
* definitions;
* complete proof;
* dependencies;
* scope and non-consequences;
* unresolved qualifications, if any;
* adversarial-review status;
* references to supporting computation or certificates.

After extraction, replace the long proof in `discovery-log.md` with:

* a concise statement;
* the artifact path;
* current validity status;
* implications;
* exact remaining applications or blockers.

### 7.2 Counterexample artifacts

Preserve counterexamples in their smallest exact form.

Include:

* the claim being refuted;
* the exact example;
* a direct verification;
* a diagram or renderer when useful;
* a deterministic verification command when appropriate;
* the precise scope of the failure.

## 8. Independent adversarial review

Keep hostile review active throughout the run.

Do not wait until a full proof appears.

Every important candidate, structural lemma, computation, and proof outline must be given to fresh agents who did not develop it. Their primary task is to invalidate the claim.

### 8.1 Review instructions

Adversarial reviewers should search for:

* omitted cases;
* false quantifier changes;
* hidden assumptions;
* circular reasoning;
* unproved compactness or extension steps;
* local configurations that do not extend globally;
* infinite objects inferred from unrelated finite approximations;
* degeneracies;
* exceptional or measure-zero cases;
* symmetry mistakes;
* orientation or reflection errors;
* numerical dependence;
* incomplete enumeration;
* incorrect symmetry reduction;
* solver-model mismatch;
* reliance on an equivalent open statement;
* theorem statements weaker than the required target.

The task-specific problem file may add further attack categories.

### 8.2 Review artifacts

Retain a review file for every cornerstone result. It must state:

1. the exact claim reviewed;
2. assumptions checked;
3. counterexamples attempted;
4. defects found;
5. repairs made;
6. remaining uncertainty;
7. final verdict:

   * valid;
   * invalid;
   * unresolved.

A repaired result must be reviewed again by an independent agent. The agent proposing a repair must not be its only reviewer.

“No counterexample found” is not by itself a validity certificate.

## 9. Proof-status vocabulary

Use proof-status labels consistently:

* **Conjectural:** supported only by intuition or experiment.
* **Candidate:** an exact object exists, but a central obligation is unproved.
* **Computational evidence:** verified only over a stated finite domain.
* **Conditional lemma:** proved under explicitly stated hypotheses not yet established.
* **Proved:** a complete proof has been written and checked internally.
* **Adversarially reviewed:** an independent hostile review found no unresolved defect.
* **Certified:** supported by an exact independently checkable finite certificate.
* **Falsified:** an exact counterexample or proof of failure exists.
* **Blocked:** the remaining obligation is theorem-strength with no active mechanism.
* **Superseded:** a stronger or corrected formulation has replaced it.

Do not use “proved” for a numerical pattern, renderer output, solver search without a certificate, or an argument that still depends on a named unresolved lemma.

## 10. Computational environment

The reproducible Linux environment is defined by `.devcontainer/`.
Follow `AGENTS.md` to run tools in the `arisearch` Conda environment; the
default shell may use the base environment. This applies to delegated agents
as well as the root agent.
`environment.yml` is the human-edited dependency specification, and
`conda-lock.yml` is the generated, fully resolved `linux-64` lockfile consumed
by the Docker build. Do not edit the lockfile manually. After changing
`environment.yml`, regenerate it with the pinned lock tool:

```text
uvx --from conda-lock==4.0.2 conda-lock lock \
  --micromamba \
  --file .devcontainer/environment.yml \
  --platform linux-64 \
  --lockfile .devcontainer/conda-lock.yml \
  --without-cuda
```

Commit the specification and regenerated lockfile together, rebuild the
container, and run:

```text
conda run --no-capture-output -n arisearch python3 .devcontainer/verify_tools.py
```

Use Python or Sage scripts under `research/` for computation. The core tools
are:

* **SageMath:** exact rational, algebraic, and symbolic geometry;
* **Z3:** SMT formulations and bounded satisfiability checks;
* **OR-Tools CP-SAT:** finite combinatorial searches, exact cover, and periodic-witness searches;
* **Nauty/Traces:** graph canonicalization, automorphisms, and symmetry reduction; and
* **Graphviz and Sage plotting:** diagnostic diagrams and certificate inspection;
* **pytest:** deterministic unit, integration, and adversarial-fixture tests; and
* **Hypothesis:** property-based and metamorphic tests, especially over exact rational fixtures;
* **Poppler (`pdfinfo`, `pdftotext`):** metadata inspection and text extraction from literature PDFs;
* **ripgrep and jq:** fast repository search and inspection of JSON certificates or logs; and
* **librsvg (`rsvg-convert`):** conversion of diagnostic SVG artifacts when needed.

Use Python's standard-library `zipfile` and `json` modules when scripts need
archive or JSON processing; do not add redundant wrappers merely for those
operations.

Prefer Sage exact arithmetic for coordinates, congruence, convexity,
incidence, and intersection decisions. NumPy or floating-point plotting may
be used only for reconnaissance and visualization. Treat solver answers
according to their precisely encoded finite scope, and verify consequential
witnesses with a small independent checker.

Do not add another solver or formal proof system speculatively. Pin any new
dependency when a concrete active route requires it, document why the core
tools are insufficient, regenerate the lockfile, and add it to the environment
smoke test. Hypothesis can expose implementation defects but does not establish
an exhaustive mathematical claim. A drawing is never a substitute for an exact
definition or proof.

## 11. Exact computation standards

Computation must answer a specific mathematical question.

Do not build generic validators, databases, ontologies, research platforms, or solver abstractions unless a concrete active route requires them.

A bounded exact search is legitimate primary research when its domain is stated precisely.

### 11.1 Required search record

For every consequential computation, record:

* the mathematical question;
* exact finite domain;
* object encoding;
* permitted transformations or equivalences;
* constraints;
* symmetry reductions;
* solver formulation;
* software and dependency versions;
* deterministic seed, if any;
* exact replay command;
* timeout or resource limits;
* completion status;
* retained witnesses or certificates;
* what the result does and does not prove.

Distinguish explicitly among:

* SAT or witness found;
* UNSAT over the complete stated domain;
* timeout;
* memory exhaustion;
* interrupted execution;
* implementation failure;
* incomplete enumeration.

Never report timeout or failure to find a witness as UNSAT.

### 11.2 Exact arithmetic

Use exact arithmetic for proof-relevant decisions.

Suitable representations include:

* integers;
* rational numbers;
* symbolic expressions;
* algebraic numbers with defining polynomials and isolating intervals;
* modular arithmetic when the implication to the exact claim is justified;
* exact combinatorial encodings.

Floating-point arithmetic may guide exploration and visualization, but it must not decide a proof-critical equality, inequality, incidence, orientation, intersection, or combinatorial branch.

When floating-point reconnaissance produces a candidate, reconstruct and verify it exactly before promoting it.

### 11.3 Certificates and trusted verification

Prefer searches that emit finite certificates.

Where practical, separate:

1. a complex search or solver;
2. a small independent verifier.

The verifier should be simple enough to audit and should not rely on trusting the search procedure.

Retain both the certificate and the verification command.

### 11.4 Temporary artifacts

Do not leave consequential evidence only in `/tmp`, terminal output, or an agent’s private workspace.

A temporary experiment must either:

* be moved into `research/` with its replay instructions and scope; or
* be explicitly marked as discarded reconnaissance and removed from the chain of evidence.

No stable claim may depend on a missing script.

## 12. Long-running searches

Launch long-running exact searches early when they are relevant, while theoretical work continues.

Do not let a solver monopolize the research programme.

For each long-running search:

* state the exact finite domain in advance;
* preserve intermediate checkpoints when possible;
* record whether the domain was fully exhausted;
* continue independent theoretical and adversarial work;
* treat any result according to its actual logical scope.

Do not infer an unrestricted theorem from a sequence of increasingly large bounded searches.

## 13. Literature research

Use current literature to:

* establish definitions;
* locate applicable theorems;
* identify the closest known constructions;
* detect rediscoveries;
* verify assumptions;
* locate counterexamples to proposed lemmas;
* determine whether a claimed advance is already known.

Prefer primary sources for mathematical claims.

### 13.1 Separation of roles

Where useful, separate:

* construction agents, who develop mathematical mechanisms independently;
* literature agents, who search for prior art, applicable theorems, and known obstructions;
* adversarial agents, who attack the resulting claims.

Do not expose every construction agent to the currently favored literature route before it has developed independently.

### 13.2 Literature record

Record:

* databases and archives searched;
* exact query families;
* dates of the search;
* primary sources examined;
* theorem statements used;
* assumptions of those theorems;
* nearest known results;
* equivalences or prior art that kill a candidate;
* the precise boundary of any novelty claim.

Do not claim universal priority. State novelty only relative to the documented search boundary.

The fact that a problem is described as open is not a stopping condition.

## 14. Repository discipline

The root agent is the sole Git writer unless the environment explicitly requires another arrangement.

Only the root agent may:

* create or switch branches;
* stage files;
* commit;
* merge;
* rebase;
* push;
* resolve overlapping modifications.

Delegated agents should receive nonoverlapping file ownership where possible and should return patches or artifacts for the root agent to integrate.

Avoid unrelated changes to product code.

Mathematics comes before application integration. Until a candidate has passed the relevant mathematical gates, keep experiments narrow and under `research/` or another designated workbench directory.

Do not build presentation software merely to leave visible evidence of activity.

## 15. Visualization policy

Use visualization to expose mathematical structure and failure modes.

A useful visualization should make it easier to inspect:

* exact geometry;
* incidence;
* orientation;
* local alternatives;
* hierarchical structure;
* certificates;
* counterexamples;
* gaps and overlaps;
* periodic witnesses.

Every rendered object must have an exact source representation when it supports a mathematical claim.

Label diagnostic images clearly. Do not present a visually persuasive patch as evidence of infinite existence, uniqueness, forcing, or nonperiodicity.

## 16. Research hygiene

### 16.1 Separate existence from universality

A construction of one valid infinite object does not prove that every admitted object has the desired property.

Whenever the target quantifies over an entire space, keep separate files or proof sections for:

* existence;
* classification of admitted configurations;
* global forcing or universality;
* exclusion of unwanted components.

### 16.2 Separate local legality from global extension

A locally legal finite patch may:

* fail to extend;
* extend only with boundary conditions;
* extend into several incompatible global components;
* admit periodic and nonperiodic extensions.

State explicitly which implication is being used and prove it.

### 16.3 Separate bounded and unbounded claims

A finite search establishes only the statement quantified over its exact domain.

Do not use phrases such as “therefore impossible” or “must be aperiodic” unless the proof includes the step from the finite certificate to the unbounded theorem.

### 16.4 Track assumptions

Every active proof should maintain an assumption ledger.

Mark whether each assumption is:

* part of the problem definition;
* derived;
* temporary and conditional;
* imported from a named theorem;
* computationally verified only over a finite domain;
* still unproved.

Hidden assumptions are a primary target for adversarial agents.

## 17. Periodic portfolio reset

At major checkpoints, classify each route as:

* explicit candidate under audit;
* proved structural theorem;
* exact family killed by counterexample;
* active construction mechanism;
* active impossibility mechanism;
* bounded computational result;
* blocked theorem-strength gap;
* literature rediscovery;
* discarded reconnaissance.

Then ask:

* Is the portfolio concentrated on one mechanism?
* Are negative results crowding out construction?
* Are constructive searches ignoring known necessary conditions?
* Are agents polishing side results rather than attacking the target?
* Has a formerly useful route become blocked?
* Are there neglected mathematical formulations?
* Are stable results still trapped inside the log?
* Are temporary scripts supporting permanent claims?
* Has adversarial review kept pace with construction?

Redirect agents accordingly.

## 18. Final acceptance and synthesis

A final mathematical result may be declared only when every applicable gate in `research-problem.md` has been satisfied.

Before declaring success:

1. extract the complete proof into a self-contained report;
2. state the theorem exactly;
3. list every external theorem used;
4. identify every computer-assisted component;
5. provide exact replay commands;
6. run independent hostile audits of the whole proof;
7. resolve all objections;
8. confirm that the theorem matches the original quantifiers and permitted objects;
9. verify that no weaker convention has silently replaced the target;
10. complete any task-specific novelty audit.

A proof that survives only because the theorem statement was weakened is not a solution.

## 19. Stopping behavior

Do not stop merely because:

* early approaches fail;
* the problem is known to be open;
* agents report theorem-strength gaps;
* a favored candidate is destroyed;
* a bounded search returns no witness;
* the literature contains no obvious route;
* the current log already contains substantial partial mathematics.

Continue launching fresh rounds, preserving incompatible approaches, and redirecting away from blocked mechanisms.

Monitor token usage when available and reserve capacity for checkpointing,
artifact preservation, and the final response. Without telemetry, checkpoint
after each substantial result and continue until the target is resolved or
an explicit limit signal requires stopping. Do not invent token counts or
infer exhaustion from elapsed time, difficulty, or lack of progress.
Context compaction alone is not token-budget exhaustion; resume from the
checkpoint when execution can continue.

Do not claim to have spent time that was not actually available.

If an actual token, execution, tool, or context limit requires termination
before a solution is found, perform these steps before exhausting capacity:

* do not disguise partial progress as success;
* checkpoint `discovery-log.md`;
* preserve stable artifacts and exact restart states;
* mark unresolved claims honestly;
* follow the no-result response format required by `research-problem.md`.

## 20. Successful deliverable structure

The exact successful deliverables are defined by `research-problem.md`.

Unless that file specifies otherwise, a successful run should normally contain:

* a self-contained final mathematical report;
* exact definitions and theorem statements;
* complete proofs;
* literature and novelty boundary;
* extracted supporting lemmas;
* retained counterexamples;
* exact computational artifacts;
* finite certificates and independent verifiers;
* adversarial-review records;
* deterministic replay commands;
* minimal diagnostic visualizations where useful;
* the continuously checkpointed `discovery-log.md`.

The discovery log remains a working research record. It is not itself the mathematical result.

## 21. Start instruction

Read `research-problem.md` and the current repository state.

Create or resume `discovery-log.md`.

Build an independent, mechanism-diverse initial portfolio. Launch exact computations early when justified. Preserve all substantial results in self-contained artifacts, keep hostile review active, and continue until the mathematical target is resolved or a real limit requires graceful termination under Section 19.
