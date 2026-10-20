# Hat two-junction incidence gate (corrected)

Status: corrected exact finite necessary-condition computation; original version failed independent review for omitting boundary-flat sectors. The repair passed [fresh independent Sol review](../reviews/hat-two-junction-geometry-sol-review-2026-10-19.md). No two-tile candidate is asserted.

Fix the Hat outline in `research/certificates/hat-eight-kite-convex-cluster-gate.json`. The domain is a noncrossing cut tree with four boundary leaves at its reflex vertices 0,4,8,11 and exactly two distinct interior trivalent vertices. No other cut endpoints are admitted. Every sector, after removal of flat corners, must be a strictly convex pentagon or hexagon.

Label the leaves 0,1,2,3 in boundary order. Their boundary arcs have 4,4,3,2 original edges. The two planar binary trees pair leaves as (01|23) or (30|12); (02|13) crosses. Each sector consists of its boundary arc and the unique tree path between its endpoints. Original convex corners remain genuine.

At an interior trivalent junction the three positive sector angles sum to 2pi and each is at most pi, so at most one is flat. There are four choices (no flat or one of three sectors). At a reflex boundary leaf the two positive sector angles sum to an angle strictly between pi and 2pi; either one may equal pi, but both cannot. There are three choices (no flat or either adjacent sector). The original gate incorrectly required both angles strictly below pi and thereby omitted genuine cases.

Enumerating 2*4^2*3^4=2592 assignments gives 32 survivors for (01|23) and zero for (30|12). Nominal side counts are respectively (6,7,5,5) and (7,6,6,4); a flat corner decreases its sector count by one. Surviving side signatures and multiplicities are (6,6,5,5):4; (5,6,5,5):10; (6,5,5,5):6; (5,5,5,5):12. Sector 1 must have some flat corner, which can occur at a boundary leaf or an interior junction. The old conclusion that an interior T junction is forced is withdrawn.

Replay:

`mise exec -- conda run --no-capture-output -n arisearch python research/searches/hat-two-junction-incidence-gate-2026-10-19.py`

The producer uses standard-library integer arithmetic, has no solver, seed, timeout or symmetry heuristic, and exhausts its stated domain. Its certificate is `research/certificates/hat-two-junction-incidence-gate-2026-10-19.json`. Exact geometric and metric follow-up is in `hat-two-junction-geometry-2026-10-19.md`. No arbitrary-cut or plane-tiling conclusion follows.
