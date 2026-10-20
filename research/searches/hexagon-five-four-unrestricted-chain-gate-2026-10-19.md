# Residual hexagons: unrestricted AA chain gate stops at recognition

Date: 2026-10-19. Status: exact local counterexamples to full-seam local
recognition; universal plane-tiling chain **unresolved and blocked**.
[Independent Sol hostile review](../reviews/hexagon-five-four-unrestricted-chain-sol-review-2026-10-19.md) passed the stated local claim. No collar, larger patch, or torus search.

## Claim tested and result

For exactly retained metric rows 15,16,23,26,31, can the two mandatory
full-seam halfturns at A3 and A5 define a nonbranching noncrossing AA chain
in **every unrestricted plane tiling**? The existing atlas proves these
contacts only in an everywhere-trivalent edge-to-edge source. The defect-free
limit theorem supplies some such source if a plane tiling exists, and does
not make the original tiling edge-to-edge. This quantifier distinction
prevents transfer of the chain to every original tiling.

An exact local attack succeeds against full-side local recognition: each
metric admits four three-tile patches with a complete disk neighborhood of
an interior point of A5, where A5 is split between two exterior tiles. The
four ordered species pairs are AA, AB, BA, BB. None supplies a full-side
A5 midpoint-halfturn mate to the host. This is a counterexample to the
unrestricted *local* inference, not a plane tiling or proof that any one of
these patches extends to the plane.

## Exact construction and proof

Use the stored counterclockwise host A and let a=A[5], b=A[0],
u=b-a, n=(u_y,-u_x), m=(a+b)/2. The host lies in the closed left
halfplane of its supporting line. Both prototypes have a right corner;
the producer selects the least-index right vertex c of each shape. Let v,w
be the vectors from c to its preceding and succeeding vertices. They are
perpendicular. Convexity puts the entire shape in their inward quadrant.

For each exterior species assignment, map the first tile's v,w rays to
-u and n, and the second tile's rays to +u and n, preserving each ray's
length, and translate c to m. Perpendicular ray bases of matching lengths
define exact orthogonal matrices. The first transformed tile occupies
{(x-m).n>=0, (x-m).u<=0}; the second occupies
{(x-m).n>=0, (x-m).u>=0}. Thus all three interiors are disjoint. Their
sectors at m have angles 180,90,90 and cover a disk of some positive
radius: m is strictly inside the host side and each corner's other sides
have positive distance from m. Each exterior tile meets a positive interval
of the host seam on its own side of m. Neither can contain both a and b.
This uses genuine partial contacts, not colored or imposed matching rules.

The construction explicitly permits determinant -1. Both ordered exterior
quadrants are checked. Conjugating the whole patch by any plane isometry,
including reflection, preserves the obstruction. The AA and BB exterior
choices show that a local species-count assumption cannot repair it.
They do not settle monohedral or mixed plane existence. No crossing witness
is claimed: failure to recognize the initial mandatory dimer already stops
the requested universal-chain gate.

## Precise gap and stop

To revive this route one must prove that all such split-A5 configurations
(and every other partial-contact alternative) are globally nonextendible,
or give a different chain definition valid through them with a proof of
uniqueness and noncrossing. The seven-corona atlas excludes neither: its
domain requires full-side neighbors. The explicit periodic strip packing
also excludes neither and supplies no unrestricted decoder. A defect-free
limit cannot preserve an arbitrary chosen defect or recover a universal
property in the original tiling. Omission must separately be excluded by
an actual monohedral theorem, not by imposing both species in this patch.

The existing data therefore do not furnish a universally defined AA chain.
Stop at this precise recognition gap; do not enlarge collars. The finite
patches are not advertised as counterexamples to universal chains in plane
tilings, because their global extension remains unproved.

## Reproduction

Producer: `research/searches/hexagon-five-four-unrestricted-chain-gate-2026-10-19.py`.
Certificate: `research/certificates/hexagon-five-four-unrestricted-chain-gate-2026-10-19.json`.
Domain: five rows times four ordered exterior species pairs, exactly 20
patches. Exact arithmetic is Q(sqrt(3)), positive embedding. Assertions
verify right corners, orthogonal transformations, full-polygon quadrant
containment, host halfplane containment, and strict interior split point.
No numerical tests or solver are used.

    mise exec -- conda run --no-capture-output -n arisearch python research/searches/hexagon-five-four-unrestricted-chain-gate-2026-10-19.py

Result: PASS, 20 exact disk-complete flat-host patches. The independent
hostile review checked the local/global distinction and quadrant proof.
