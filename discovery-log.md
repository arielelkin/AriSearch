# Two-convex-tile research state

This is a restartable working index governed by `research-protocol.md`. It is
not a solution or final report. The authoritative target remains exactly two
unmarked convex polygons under all isometries and unrestricted contacts.

## Unrestricted-contact reductions

### All-obtuse convex hexagons

**Status:** Candidate under repair. Hostile review found a gap in the original
completeness argument; a uniform-star repair awaits fresh review.

The candidate lemma asserts that if every prototile is a strictly convex
hexagon with every angle in `(pi/2,pi)`, arbitrary contacts automatically
become an edge-to-edge trivalent honeycomb. The repaired proof is:

`research/lemmas/all-obtuse-hexagon-contact-reduction.md`

If validated, this would discharge the unrestricted-contact and partial-edge-
contact obligations for any future two-hexagon candidate in this angle class.
It does not encode matching rules and does not exclude periodic or monohedral
tilings.

**Resume point:** For a proposed pair in this class, first apply the
monohedral periodic-tiling gate. If both shapes survive, determine what
information two unmarked honeycomb face types can force beyond the cell
structure. Do not rebuild the many-prototile collared compiler unless a new
mechanism compresses its state into exactly two congruence classes.

## Compatibility-graph carriers

### Three simple six-cycle carrier

**Status:** Candidate periodic-escape obstruction under repair. Hostile review
found that the original periodic cover was not self-contained; explicit
incidence coordinates and a flat-torus argument now await fresh review.

The candidate theorem asserts that when exactly three prototiles are simple
six-cycles in a simple bipartite compatibility graph, globally unique side
lengths and common-endpoint vertex decoding do not suffice: every tileable
three-cycle system has an explicit doubly periodic honeycomb tiling. The
repaired proof is:

`research/counterexamples/three-simple-cycle-hexagon-periodic-escape.md`

**Implication if validated:** Do not search for a three-tile solution merely
by selecting three simple cycles from the workbench compatibility graph. A
route worth reopening must add a genuinely different geometric channel or
leave the simple-cycle carrier hypotheses. No two-cycle corollary is presently
claimed by the extracted artifact.

### Four simple six-cycle carrier

**Status:** Candidate periodic-escape generalization; not extracted as a
stable theorem.

The workbench proposes that every nonempty system of four selected simple
six-cycles also has a periodic escape, using an incidence count followed by a
torus/Klein-bottle or `K_3,3` case split. The argument is directly relevant
to low-cardinality compression but has not been independently reviewed, and
several incidence assertions need a fully self-contained audit before it may
be labeled proved.

Source working notes:

`workbench/discovery-log-2026-07-25.md`, section “Extension of the
periodic-escape theorem to four cycles”.

**Resume point:** Hostile-review the claims that every active graph vertex
belongs to exactly three or four cycles, that the active graph is necessarily
cubic, and that the stated incidence equation exhausts all cases. Extract a
counterexample artifact only if those steps survive.

## Target-divergent convex compilation

### All-obtuse honeycomb compiler

**Status:** Blocked for the main objective; potentially meaningful separate
many-prototile theorem.

The workbench gives a detailed proposed compiler from a nearest-neighbor
two-dimensional shift of finite type to rational strictly convex all-obtuse
hexagons. Its local forcing mechanism combines the contact-reduction lemma,
globally unique edge lengths, a line-graph star argument, and a finite phase
cover. The explicit winding Kari-Culik instance has 9,912 prototiles.

This construction is not a candidate for the present problem, which requires
exactly two congruence classes. Its remaining main-project obligation is a
state-compression theorem from an unbounded collared alphabet to exactly two
convex unmarked shapes without introducing periodic or monohedral escape
tilings. No such mechanism is currently available, so the route is blocked
under the protocol.

The general compiler manuscript remains in:

`workbench/all-obtuse-convex-hexagon-compiler.md`

Only its generally reusable contact reduction has been promoted into
`research/`.

### Winding-family invariant

**Status:** Conditional and target-divergent; not incorporated.

The workbench's main report states pairwise nonconjugacy of the winding
family, but its dedicated extension manuscript leaves controlled returns,
horizontal-eigenvalue exclusion, finite-phase analysis, spectral
completeness, and component recognition open. Those claims are not needed for
the two-tile target and must not be cited as proved.

## Exact computation

No proof-relevant computation was promoted in this extraction. The
workbench JavaScript enumerator is generator-side evidence for a thousands-of-
tiles instance, not an independent certificate for a two-tile candidate.

## Current portfolio and next actions

- **Candidate reusable lemma:** all-obtuse hexagon contact reduction, with a
  repaired completeness step awaiting review.
- **Candidate obstruction:** native three-simple-cycle compatibility carrier,
  with a repaired periodic-cover step awaiting review.
- **Review queue:** proposed four-cycle periodic-escape theorem.
- **Blocked mechanism:** collared all-obtuse compiler without a concrete
  two-shape state-compression mechanism.
- **Unaddressed central gate:** find exact convex shapes `A,B` for which
  neither admits a periodic monohedral tiling and whose geometry forces more
  than a two-symbol periodic honeycomb coloring.

No surviving two-tile candidate is currently recorded.

## Review checkpoint — 2026-08-15

Three independent hostile reviews were completed and preserved under
`research/reviews/`. They found repairable proof gaps in both extracted
artifacts. The root then edited both artifacts to add the proposed repairs and
kept their status at **Candidate**.

Fresh cross-reviews of the repaired versions were assigned but interrupted at
the user's request before verdicts were returned. They must not be treated as
completed reviews.

**Exact resume point for the next agent:**

1. Read the three files under `research/reviews/`.
2. Independently review the repaired uniform closed-star completeness argument
   in `research/lemmas/all-obtuse-hexagon-contact-reduction.md`.
3. Independently review the repaired `F/U/D` honeycomb incidence calculation
   and flat-torus development in
   `research/counterexamples/three-simple-cycle-hexagon-periodic-escape.md`.
4. Preserve each fresh verdict in a new review file. If a repair survives,
   update its artifact and this log to **Adversarially reviewed**; otherwise
   retain **Candidate** and record the remaining defect.
5. Do not revive the unproved two-cycle or four-cycle extensions without
   separate proofs and hostile reviews.
