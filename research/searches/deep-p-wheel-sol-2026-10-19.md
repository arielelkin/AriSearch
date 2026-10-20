# Deep central P wheel, one changed J=1 design

Status: complete oriented abstract disks; fixed pair fails the necessary strict angle gate (P-only UNSAT), pending independent hostile review. No polygon dissection, plane tiling, or forcing claim.

## Analytic incidence design

The six interior P vertices induce W6: deep center z joined to rim i0,...,i4, with rim cycle. Its ten edges use twenty of thirty native interior degrees, so exactly ten edges join the core to the boundary. Each rim vertex has core degree three and needs two boundary neighbors; the center already has degree five. The chosen annulus has five outer vertices a0,...,a4 and one advance at each rim vertex. All original outer vertices have degree four. This is one specific annulus, not a classification of every permitted annulus.

The P and Q disks have respectively E=29 and E=27. Thus boundary-induced edges number 9 and 7, exceeding their final outer boundary cycle lengths 7 and 6 by c=2 and c=1. An ear attached to an original outer edge raises both original endpoint degrees to five; these endpoints must be Q because a boundary P needs degree at most four. For Q choose ear (a0,a1,e0), original endpoints a0,a1 Q, and third Q a3. Boundary order (a0,e0,a1,a2,a3,a4); untouched corner counts (1,2,1,0,2,0), total six.

For P choose the same first ear, then attach (a0,e0,e1). The only Q children are a0,a1. Boundary order (a0,e1,e0,a1,a2,a3,a4); degrees (6,2,3,5,4,4,4); untouched corner counts (0,2,1,1,0,0,0), total four. Two ears on distinct original boundary edges would require at least three original Q endpoints, violating this P inventory; the nested ear resolves that degree obstruction.

In both parents the final boundary transition (a4,a0) is the sole split parent corner, labeled native parent corner zero. Other native parent corners are assigned in order along the outer boundary. The generator reconstructs child cyclic words and every primal seam endpoint and verifies orientation, connected path/cycle links, disk Euler identity, native degrees, inventories and opposite seam traversals. P has 13 children, 29 seams, 17 trivalent junctions; Q has 12 children, 27 seams, 16 trivalent junctions. Both have six interior P children. Full exact maps are retained in deep-p-wheel-incidence-sol-2026-10-19.json.

## Necessary strict angle gate

The companion angle script uses the previously reviewed finite-disjunction exact linear encoding on this new JSON. Twelve real native angle variables have bounds 0<a<1 in units pi, with P sum three and Q sum five. Every child admits all phases and both reflections independently. Interior junction sums are two; ordinary transitions sum one; untouched native corners and the split corner sum to the actual corresponding parent native angle. There are no phase normalizations or restrictions on repeated angles. The P-only domain has 10^11*14^2 assignments and its infeasibility would suffice to reject the fixed pair. The simultaneous domain has 10^20*14^5 assignments. No other incidence or angle allocations are being enumerated.

Replay:

    mise exec -- conda run --no-capture-output -n arisearch python research/searches/deep-p-wheel-incidence-sol-2026-10-19.py
    mise exec -- conda run --no-capture-output -n arisearch python research/searches/deep-p-wheel-angle-sol-2026-10-19.py --parent P --core --timeout-ms 180000

## Result and precise stop

The exact P-only system returned **UNSAT**, Z3 4.16.0, seed zero, elapsed 25.516830124994158 seconds under a 180000 ms timeout. Input SHA256 is `412bdd5ae5ae25714fa3c927d0fe6d63f75f93a4d06b172d26af59b28c491b93`; formula SHA256 is `0af01bba7b404ade37581aea22a6ea79c27fb2a6e8f3e2b596e4fe9dc18b5471`. The retained angle JSON contains the nonminimal tracked core. This is a solver decision with Z3 and the encoding in the trust boundary, not a solver-independent UNSAT proof certificate. Independent review is pending.

P-only infeasibility excludes the simultaneous common angle system on this pair, so the simultaneous solve was unnecessary and was not run. There is no rational angle witness and no metric feasibility gate is justified. Stop this one cycle. The result excludes only the explicit five-vertex one-advance annulus, nested P ears, displayed Q species allocation, ordered parent-corner roles, and final exceptional transition. It does not exclude other W6 annuli, native allocations, split-corner positions, J=1 disks, geometric polygon pairs, or unrestricted plane tilings. No alternate core, larger inventory, Git edit or discovery-log edit was performed.
