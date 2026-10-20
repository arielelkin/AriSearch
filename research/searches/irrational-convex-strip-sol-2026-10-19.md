# Irrational row synchronization: exact failure and interface obstruction

Date: 2026-10-19. Status: internally checked diagnostic and conditional lemma; no independent hostile review. One bounded analytic design cycle; no enumeration or numerical patch search. Main problem unresolved. No novelty claim.

## Early escape gate

Take A=[0,1]×[0,1] and B=[0,√2]×[0,1]. Both have positive area and all interior angles strictly less than π. These are distinct convex polygon congruence classes, but they violate the necessary at-least-five-sides omission gate: each rectangle separately tiles the plane periodically. Accordingly this is a killed diagnostic, not a surviving candidate.

There is also an explicit mixed rank-two periodic tiling, using both shapes with positive density. Set L=1+√2. For every m,n∈Z place A at (mL,n) and B at (mL+1,n). Each horizontal interval [mL,(m+1)L] is exactly partitioned into widths 1 and √2, and the unit-height bands partition the plane. Interiors are disjoint. The periods are (L,0) and (0,1). This witness is admitted under arbitrary isometries and unrestricted contacts; allowing more placements cannot eliminate it. Thus irrational length ratios alone do not preclude even mixed rank-two periodic tilings.

## What irrational rows actually achieve

Let α=√2−1 and s_n=⌊(n+1)α⌋−⌊nα⌋ for all n∈Z. In band n≤y≤n+1 use only A if s_n=0 and only B if s_n=1, placing width-w_n rectangles at (kw_n,n) for all k∈Z. This is a full-plane tiling by the same two shapes. Partial-edge contacts along band boundaries are allowed by the problem.

This particular tiling has no nonzero translation. The horizontal lines contained entirely in its tile boundary are exactly y∈Z: at any noninteger height, a horizontal line intersects rectangle interiors. Hence a translation symmetry (t,u) must have u∈Z. It must preserve row species, since A and B are noncongruent. If u≠0, the binary word s would be periodic. But its frequency of 1 is α, since ∑_{n=0}^{N−1}s_n=⌊Nα⌋, whereas a periodic binary word has rational frequency. This is impossible. Thus u=0. Both row species occur, and preservation of the vertical seams in each type implies t∈Z and t∈√2 Z, hence t=0.

This is an explicit example of the exact quantifier failure that must be avoided: one genuinely translation-free tiling coexists with monohedral and mixed periodic tilings of the same pair. No claim about every placement follows from its Sturmian source.

## Continuous-interface obstruction

**Lemma.** Let f:R→R be continuous and have periods p,q>0 with p/q irrational. Then f is constant. Consequently, if a common boundary is the graph of a continuous function and the complete row tilings on its two sides have horizontal periods p and q, respectively, then the boundary is straight whenever p/q is irrational.

Proof. Every integer combination mp+nq is a period. This additive subgroup is dense: by the pigeonhole principle, for every ε>0 it contains a nonzero δ with |δ|<ε (compare N+1 residues of kp modulo q); integer multiples of arbitrarily small such δ approximate every real displacement. Continuity then gives f(x+t)=f(x) for every real t, so f is constant. For the consequence, the shared boundary set is preserved by each row period; because it is a graph, these are periods of f. QED.

The consequence requires preservation of the complete shared boundary by each row translation. It does not apply to two periodic edge subsets whose union is a boundary, to a boundary not represented by a continuous graph, to rows with nonhorizontal translations, or to nonperiodic rows. No universal convex-polygon tiling theorem is claimed.

Thus replacing the diagnostic straight interfaces by two incommensurately periodic corrugated interfaces cannot create the desired synchronization. They cannot meet as the same entire graph. If all rows instead share a common horizontal period, the entire row-built tiling already has that nonzero period, and the stronger existing finite-state repeatable-strip theorem additionally supplies a rank-two periodic escape under its independent-reuse assumptions.

## Exact missing geometry and stopping state

No pair of exact convex polygons with at least five genuine sides was obtained. The absent geometric step is a two-congruence-class strip construction whose row boundary is intrinsically nonperiodic and whose adjacent rows force an irrational phase relation, while admitting neither an independently repeatable complete boundary state nor a monohedral periodic omission. To advance this particular mechanism one must specify actual side vectors and a full-plane covering that realize this step; an externally chosen Sturmian row word supplies none of that forcing. Universal recognition would then still have to cover reflections and partial contacts.

This is a missing construction obligation, not a proved impossibility result. Under protocol §5 stop the mechanism here: do not enlarge row-word searches, tune an irrational parameter, or search generic patches without concrete convex pentagon-or-higher geometry. A materially new design must evade both the explicit rectangle escape and the complete periodic-interface hypothesis above.

Dependencies inspected: research-problem.md; research-protocol.md §§5,19; latest discovery-log.md; research/lemmas/two-hexagon-repeatable-strip-cycle-2026-10-14.md; research/lemmas/periodic-scaffold-anchored-strip-completion.md; research/lemmas/convex-parallelogram-fusion-periodic-escape-2026-10-19.md. The present diagnostic does not reopen their closed families. No Git or discovery-log edits made.
