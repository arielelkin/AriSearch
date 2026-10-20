# Hostile review: tangential 110/140 all-scale exclusion

Verdict: **PASS / valid**, for the stated one-parameter pair only.
Reviewer: fresh Sol reviewer, 2026-10-19. No producer files edited.

## Claim and assumptions

Reviewed `research/searches/tangential-110-140-scale-gate-sol-2026-10-19.md`
and its Sage companion against research-problem.md and research-protocol.md
sections 5, 8, and 19. The claim is that no positive relative scale r of
these particular unit-support pentagon and equal-support heptagon admits
any unrestricted plane tiling, allowing reflections and partial contacts.
This is a candidate-family exclusion, not a solution to the research problem.

## Independent derivation

The retained independent Sage checker reconstructs exact vertices by solving
adjacent support-line equations over AA, then computes side distances. In
normal order the P corners are [120,90,110,110,110] and side lengths
[h,a,b,b,c]. The Q corners are [140,100,100,140,140,140,140] and sides
[d,f,d,e,e,e,e] before scaling. It confirms all repeated lengths and strict
inequalities c<b<a, c<b<h, e<d<f directly from support coordinates.
In particular no tacit equal-length identification or assumed numerical
rounding enters the scale gate.

The local angle inventory is complete: genuine corner stars are 90^4,
90+90+180, 110+110+140, 100+120+140, and 120^3. A straight seam
180+180 is not a vertex. Because the minimum native corner angle is 90,
a tile corner of angle greater than 90 cannot lie inside another tile's
native side: the remaining sector is strictly smaller than 90. Hence along
a ray issuing between two corners, whichever native side ends first must
end at a 90 corner, unless both sides end together. This proves the contact
rule used throughout without an edge-to-edge assumption.

Every Q100 has a unique adjacent Q140 at its 100+120+140 star. Both
incident Q sides have only obtuse far endpoints, so their common ray
must be a full common side. Their length palettes are {rf,rd} and
{rd,re}; strict inequalities leave only rd. A Q100's rd side ends at
one of its own boundary140 corners. Conversely the rd side at a boundary140
ends at Q100. At the far end of each forced seam the two corners exchange
100 and 140 roles, so that boundary140 is also a 100+120+140 star.
This supplies the sometimes implicit converse: exactly the two boundary140
corners of each Q are used in those stars. Each remaining Q140 is a
110+110+140 star and has two incident re rays toward P110 corners.

Disk incidence accounting gives 3p=2x+O(R), 2q=y+O(R),
5q=x+y+O(R), hence p=2q+O(R). The O(R) errors are justified for
each fixed positive r by a bounded-width boundary annulus: tiles have
uniform positive area, bounded diameter, and disjoint interiors. No density
limit or assumption that both species occur at positive density is needed.
In particular q=O(R) implies p=O(R), contradicting area coverage.

There are 6q+O(R) re/P110 rays. If re differs from b, equality at both
endpoints can only use a or c. For either fixed equality, each P has only
one such side and one 110 endpoint, so capacity is p+O(R). If the P
side ends first, its far endpoint must be 90, forcing that side to be a
and re>a. Each P90 has only two incident side rays, so this possibility
has capacity at most 2p+O(R). The shorter/equal alternatives are mutually
exclusive for a fixed scale. If Q ends first its far140 corner is forbidden.
Thus all non-b scales have 6q<=2p+O(R), a contradiction. This is an
injection into concrete side or corner-ray occurrences; there is no
unjustified multiplication of corner capacity. Intermediate partial
contacts cannot evade the first-endpoint rule.

At the unique remaining scale r=b/e, a boundary140 star has its Q/Q
seam along rd and its Q/P120 ray along re=b. The P120 sides have
lengths c,h. On c the P side ends first at P110, forbidden; on h the
Q side ends first at Q140, forbidden. Exact c<b<h kills both choices.
Rotation and reflection preserve all inventories and endpoint arguments.

## Attacks, defects, repairs, uncertainty

Attempted attacks included the flat180 exception, reversed seam endpoints,
a boundary140 assigned to the wrong star, repeated use of one P90,
nonexistent density limits, pure-type tilings, and relative-scale equality
exceptions. The arguments above close them. No mathematical defect found;
no repairs made. The producer text abbreviates the seam-end converse and
the annulus injection, but both follow as shown and require no additional
hypothesis. Remaining uncertainty: none within the asserted family. No
claim is made about other angle words or unequal supports.

## Replay

Both commands completed with PASS on 2026-10-19:

```
mise exec -- conda run --no-capture-output -n arisearch sage research/searches/tangential-110-140-scale-gate-sol-2026-10-19.sage
mise exec -- conda run --no-capture-output -n arisearch sage research/reviews/tangential-110-140-scale-independent-sol-2026-10-19.sage
```

The computational domain is the finite support-line reconstruction, exact
length comparisons, and producer enumeration of six angle multiplicities
in {0,...,4}. The global exclusion is the analytic proof reviewed above.
Per protocol section 5 this killed family should be archived; reopening
requires a new mechanism or changed family. Section 19 requires continued
research elsewhere, not extrapolation of this exclusion to all pairs.
