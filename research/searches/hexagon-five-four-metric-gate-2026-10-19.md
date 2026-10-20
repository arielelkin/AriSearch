# Fixed five/four word: exact metric feasibility gate

Date: 2026-10-19. Scope: A=(0,1,2,0,3,4), B=(0,1,1,0,2,3), with five distinct positive lengths, conditional on the edge-to-edge trivalent source model. No plane-tiling conclusion.

## Equiangular locus: eliminated exactly

Take side0 horizontal and all exterior turns 60 degrees. Write each polygon closure with the x equation doubled and the y equation divided by sqrt(3)/2. The two A rows and two B rows on lengths (l0,...,l4) are

    0 1 -1 -1  1
    0 1  1 -1 -1
    0 0 -1  1  0
    0 2 -1 -1  0

The kernel is exactly span((1,0,0,0,0),(0,1,1,1,1)), so l1=l2=l3=l4. This contradicts pairwise distinctness. Independent polygon rotations do not change either closure zero condition. This eliminates only the equiangular locus; angle sums do not force that locus.

## Exact finite combinatorial domain

Use the reviewed 22-star atlas and seven ten-factor corona cycles. Exhaust all 2^22 subsets of the signed stars, without identifying reflection. A retained support must cover all twelve corner types and provide at least one continuation within itself for each seam of each retained star. At least one of the seven corona cycles must have a witnessing retained star at each of its ten factors. These are necessary local conditions; external tile identity and geometric overlaps between neighboring tiles are not asserted.

Retain inclusion-minimal such supports. This reduction is complete for **metric feasibility**: every finite necessary support contains a minimal one, and its angle equations contain those of the minimal one. It is not a reduction preserving deterministic-neighbor classifications or plane extension. If a minimal support is realizable, larger supports and the determinism question still require separate work.

## Exact polynomial metric formulation

For each native corner i introduce a unit complex exterior rotation (c_i,s_i) with s_i>0. Thus its exterior angle lies strictly between 0 and pi. For a trivalent star, multiply its three exterior rotations and require the result (-1,0). Since their summed angles lie in (0,3pi), this is exactly exterior-angle sum pi, equivalently interior-angle sum 2pi. Handedness does not change an interior angle.

Introduce five pairwise distinct positive real lengths, normalized l0=1. For each polygon independently begin direction (1,0), multiply successive directions by the native exterior rotations, form all six exact side vectors, and impose zero vector sum. Impose final direction (1,0). For every directed side, require all four other vertices to lie strictly on its left. These strict polynomial halfplane inequalities ensure a simple strictly convex polygon in native order, excluding wrong winding and self intersections. Both polygon closures are essential.

The resulting existential real polynomial system is submitted to Z3 QF_NRA. Each call has a 30000ms solver timeout. The first UNKNOWN stops the branch; it is no elimination. The first SAT stops for exact model audit and geometric local-patch construction; even audited SAT would not establish a plane tiling. No torus search is authorized by either result. Enumeration itself has finite domain 4194304 masks and no heuristic pruning.

## Evidence and replay

Producer: `research/searches/hexagon-five-four-metric-gate-2026-10-19.py`.
Certificate: `research/certificates/hexagon-five-four-metric-gate-2026-10-19.json` records the complete finite support count, ascending-mask SHA256, minimal masks, per-corona counts, solver domain, statuses and timing.

    mise exec -- conda run --no-capture-output -n arisearch python research/searches/hexagon-five-four-metric-gate-2026-10-19.py

This producer imports the reviewed upper-atlas implementation. Its support enumeration and nonlinear encoding have not yet received independent hostile review. Any solver UNSAT is computational evidence pending independent certificate support; UNKNOWN has no exclusion content. Restart from the first unfinished minimal support only with a materially stronger analytic reduction or exact witness construction.

## Completed result and stop

**Blocked.** Complete enumeration retained 446 seam-closed full-cover supports. The seven corona compatibility counts, in producer order, are 254,128,128,256,128,128,256 (overlap allowed). There are seven inclusion-minimal supports with masks 33416,41032,1118212,2625540,20774,22550,3543044. The first has star indices 3,7,9,15 in the reviewed atlas. Its exact real polynomial query returned UNKNOWN, reason timeout, after 30.23 seconds. The other six minimal queries were not launched. No nonequiangular support was eliminated and no realizable witness was obtained. All larger support feasibility, deterministic propagation, and plane extension remain unresolved. No periodic escape search followed the timeout.

The separate checker independently reconstructs equiangular closure using exact trigonometric values and verifies rank/kernel and certificate status consistency:

    mise exec -- conda run --no-capture-output -n arisearch python research/searches/hexagon-five-four-metric-gate-check-2026-10-19.py

It passed. This checker does not independently certify the 446-support completeness or metric encoding. The exact unfinished obligation is feasibility or infeasibility of both strictly convex polygon closures with distinct positive lengths under the first minimal support's four angle sums, followed by the other six supports if necessary. A stronger elimination invariant or explicit algebraic nonequiangular metric is needed before reopening the expensive solver gate.

Independent exact trigonometric reconstruction caught incorrect initial y rows; both producer and certificate were corrected. The corrected matrix has the same rank and kernel, so the equiangular exclusion survives. The nonlinear query uses unit rotations directly and did not use these matrix rows.
