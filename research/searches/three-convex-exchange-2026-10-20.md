# Three-convex source exchange: routing gate

Date: 2026-10-20. Status: no candidate pair. This is a deduplication and design gate, not a new aperiodicity theorem. The target permits reflections, partial contacts, and omission of either tile.

## Sources checked

I read the exact Ammann H6/P1/P2 source in [the coordinate and forcing record](../lemmas/ammann-forcing-aperiodicity.md), the [three-to-two probe](ammann-three-to-two-convex-sol-2026-10-19.md), the [whole-source parity theorem](../lemmas/terra-ammann-balanced-convex-macro-parity.md), the [source-by-source area module](../lemmas/ammann-source-by-source-two-area-module-obstruction.md), the [H/D incidence obstruction](../lemmas/ammann-hd-incidence-preserving-convexification-obstruction.md), and the [six-pentagon Penrose source reconstruction](../literature/current-exact-convex-source-six-reconstruction.md). The literature boundary in `research/literature/two-convex-primary-boundary-2026-10-19.md` records that Sugimoto's three-convex Tile(1,1) cuts admit periodic reflected tilings; the [reported two-type degeneracies](../literature/sugimoto-two-type-degeneracies.md) already have monohedral or mixed periodic escapes. Those are not viable unrestricted precursors.

## Exact Ammann reduction gate

Use the reviewed source polygons

```
w = exp(i*pi/5), J = s + t*w
J' = 1+w^4*(J-1), J'' = w+w^6*(J-w)
K = w^2+w^6*(J-1), L = 1+w^7*(J-1-w)
J2 = 1+w+w^2-J
H = (0,J',1,J,w,J'')
P1 = (0,J',1,L,K)
P2 = (K,L,1+w^2,J2,w^2)
```

The most direct two-class reduction fuses P1/P2 across their compulsory `KL` seam and retains H. Its P1/P2 union D is nonconvex at K and L. A notch-filling exchange that preserves the H/D face incidence has already been excluded: an H has two forced degree-two boundary vertices J' and J'', so a convex output H would have at most four genuine sides and would tile periodically alone. Moving the existing cut endpoints does not change this combinatorial defect. The [reviewed proof](../lemmas/ammann-hd-incidence-preserving-convexification-obstruction.md) handles reflections and partial contacts in the source.

The exact source area identities are `area(H)/sin(pi/5)=1`, `area(P1)/sin(pi/5)=phi-f`, `area(P2)/sin(pi/5)=f`, with `f=(s^2+phi*s*t+t^2+(phi-2)*t)/2`. At the explicit reviewed generic parameter with `f` outside `Q(phi)`, these areas have rational rank three. Therefore *every* two-target dissection that keeps target boundaries within each source tile is impossible, independent of how many pieces are used. At rank-two parameters the integer-kernel constraint remains; at the reviewed rational fixture J=1/2+(4/5)w, each target class must occur in H in a multiple of 40, so a two-piece H cut is excluded. These are exact existing gates, not new computations here.

Whole-source macro fusion is likewise constrained: each of two tileable target classes has balanced P1/P2 content `(h,k,k)`. The no-flat-angle parity theorem gives every convex whole-source macro an even number of genuine sides. Thus any pentagon-containing two-class compiler is excluded; the only side-count slot left by that theorem is a pair of hexagons. No finite convex hexagon support or decoder is presently specified. Enlarging P1/P2 clusters while keeping whole-source boundaries repeats that closed lane.

## Changed mechanism required

A genuinely new exchange would create a *third final face at each former H/D two-face vertex* J' and J'', with its own finite cyclic boundary word and exact allocation of the sectors around that vertex. This changes the incidence hypothesis of the notch obstruction. It must also cross source boundaries to avoid the area-rank-three gate. The output must be exactly two congruence classes of strict convex polygons with at least five sides, with a source-plane-compatible rule and a decoder for **every** unmarked output tiling. I could not specify even one such finite allocation without leaving unassigned sectors or reintroducing P1/P2 as distinct classes. No area, patch, or aperiodicity check is claimed for an unspecified exchange.

I therefore switched the design search to a direct pair mechanism: an obtuse P5/Q6 or P5/Q7 pair whose angle stars enforce complete-edge contacts and whose repeated edge lengths support a nontrivial hierarchical grouping. This differs from fusing or cutting the three-convex source. An experiment in that lane needs an explicit native angle/side word and a first exact nonperiodic extension mechanism; another isolated finite star or torus-negative search would not meet the target. The fixed P5/Q7 and P5/Q8 words already in the [shape-first dedup audit](shape-first-dedup-audit-2026-10-20.md) are excluded from reuse. No specific new pair passed even the first geometry and omission gates in this pass, so none is advanced as a candidate.

## Outcome and replay

There was no novel finite computation and no script. The exact claims above are deductions imported with their stated hypotheses from linked reviewed artifacts. In particular this gate does **not** say every three-convex exchange is impossible. The research problem remains unresolved.
