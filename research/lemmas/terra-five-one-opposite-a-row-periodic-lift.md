# Opposite-angle A gives a periodic row lift in a saturated five-plus-one B field

Date: 2026-10-13. Status: [fresh independent hostile review VALID](../reviews/terra-five-one-opposite-a-row-lift-fresh-hostile-review.md); native row and independent endpoint checkers PASS. Its core input is an ACTUAL saturated defect-free field. The separately reviewed saturation reduction now gives the all-original-tiling corollary below.

## Hypotheses and conclusion

Use the changed family x in(112.5,126), x!=120, y=720-5x,z=4x-360,
r=360-2x,s=360-2y. Actual strictly convex A has native angles012012
(colours x,y,z); actual B has native angles(s,r,r,r,r,r). Assume an actual
connected defect-free trivalent edge-to-edge mixed field in the exact four-star
language AAAxyz,AABxxr,AAByys,ABBzrr, with every B having exactly two B neighbours.
Then the pair admits a periodic tiling. Rotations/reflections and omission
are permitted; a hypothetical partial-contact original field is not assumed
saturated by this lemma itself.

Dependencies: the internally proved metric AAA=>central lemma in
[opposite-A all-metric coverage](terra-ternary-opposite-a-all-metric-escape.md),
the reviewed honeycomb full-native indexing and actual metric development in
[two-hexagon-global-sft-encoding.md](two-hexagon-global-sft-encoding.md),
and the central-hexagon translation escape. Saturation extraction is a
separate [capacity lemma](terra-five-one-b-saturated-chain-reduction.md).
Independent review of both is required before their combined corollary.

## Noncentral A removes AAA and fixes its private seams

If A is centrally symmetric, it supplies an immediate periodic omission escape.
Otherwise a metrically legal AAA star would force centrality by the cited
A012012 closure/strict-triangle lemma. Thus AAA is absent everywhere in this
actual field. The same closure kernel shows every opposite side difference
is nonzero; in particular a0!=a3.

The A palette has only01,12,02. Of the three saturated B masks only native
BB{1,4} has its four AB endpoint pairs all present:12,02,02,12.
Thus every B uses this mask. Its special s corner has A-colour1 at both A
neighbours; its remaining AAB r corner has A-colour0; its four ABB corners
have A-colour2.

A native01 sides0,3 cannot AB-match a B side of the permitted12/02 palette,
so are AA. Because AAA is absent, each A0/A1 corner has one AA and one AB arm,
and each A2 corner has two AB arms. Consequently A has EXACTLY its two opposite
native AA sides0,3, and its other four sides are AB.

## Species rows are globally parallel and alternate

Develop the combinatorial field on the reviewed triangular cell lattice with
D0=(1,0),D1=(0,1),D2=(-1,1) and their negatives. Every A has two A neighbours
in opposite cell slots because its native AA side indices differ by3.
Its A component is therefore an entire straight integer lattice line.
Two such lines in different primitive D directions meet at an integer cell:
each pair of these directions has determinant1 in absolute value. At their
intersection an A would have four A neighbours, contradicting degree2.
Thus all A lines have one common direction. Rotate the global cell indexing
so it isD0.

Every lattice row parallel toD0 is now wholly A or wholly B. Adjacent A rows
would give an A more than two A neighbours; adjacent B rows would give a B
its two same-row B neighbours plus two extra B neighbours in the next row,
contradicting saturated BB-degree2. Therefore rows alternate A,B,A,B globally.
No global periodicity of arbitrary chains was assumed; the private opposite
A seams force this particular species backbone.

## B closure makes its BB metric independent of labels

At an AAB0 B vertex, both A0 corners attach through native02 arms. Their
remaining AA arm is a0 for native A corner0 and a3 for native corner3.
Since a0!=a3, AA matching forces both A corners to use the same native slot.
Their remaining AB arms therefore have equal length. At the B r AAB vertex
(native corner3), this gives B side2=side3=n.

Likewise at the special s AAB1 vertex(native0), an A1 corner uses AA arm a0
or a3; same-slot necessity gives B side0=side5=m. Denote its BB lengths at
native sides1,4 by p,q. B length word is(m,p,n,n,q,m).

Let R=180-r=2x-180 in(45,72), and E=exp(iR). B edge unit directions are
1,E,E^2,E^3,E^4,E^5. If(m,p,n,n,q,m) closes, conjugate its closure equation
and multiply byE^5: the reversed word(m,q,n,n,p,m) also closes. The two
unknown BB columns E,E^4 are real-linearly independent because sin(3R)!=0
throughout the stated interval exceptR=60, precisely excludedx=120.
The same prescribed four AB lengths therefore have a UNIQUE pair of BB
lengths. Hence p=q. This is an exact positive-shape closure implication,
not an assumed symmetry of a formal polygon.

## Full A labels have period2 along rows

A placement(r,s) has native corner at slotk equal r+s*k and native side at
side-slotk equal r+k ifs=+1, r-k-1 ifs=-1. A row AA neighbours lie atD0,D3,
so their side-slots are5,2. Those must be native0,3 in either order.
Exactly four indexed A placements satisfy this:

    (0,-1),(1,+1),(3,-1),(4,+1).

Across a D0 AA seam, unequal a0,a3 force its two native side indices equal.
The same-colour AAB endpoint rule matches the native A0/A1 colours in spatial
order. These conditions give unique native row transitions

    (0,-1)<->(4,+1), (1,+1)<->(3,-1).

Thus every actual A row has FULL native-label period2D0. The same period
works for every row, irrespective of their phases or metric choices across
rows. No projection to colours alone is used here.

## Canonical B choices preserve every constraint

B row BB side-slots5,2 must be its native sides1,4. Exactly four native B
placements satisfy this: (1,-1),(2,+1),(4,-1),(5,+1).
In every one, the BB endpoints at global corners0,2,3,5 are r, and the two
BB side lengths are the same commonp. Therefore ALL B-B seam and ABB2 angle
constraints are independent of which available B representative is chosen.

Each B cell has four A neighbours in the two adjacent A rows. Let its ordered
four-A tuple retain their full native placements at directions1,2,4,5.
The source actual field supplies at least one B representative compatible
with every tuple that occurs: all AB metric/endpoints and both AAB vertices
are checked there. Since all A labels repeat under2D0, these ordered tuples
repeat under2D0 as well.

Choose one such compatible native B representative once for each occurring
tuple, and use it at every occurrence. A labels and AA constraints are retained;
AB seams and AAB vertices are legal by the selected tuple membership; BB seams
and ABB vertices remain legal by commonp and r/r endpoints, independently of
neighbouring representative choices. Hence the replacement is a FULL native
legal field, periodic under2D0. The reviewed actual metric-development theorem
gives a plane tiling with a nonzero translation, after squaring a glide if
needed. No local configuration was promoted to infinite existence: the actual
field supplies existence and the canonical replacement preserves its exact
constraints.

## Replay and non-consequences

[Separate native row checker](../reviews/verify_terra_five_one_opposite_a_row_lift.py).

    mise exec -- conda run --no-capture-output -n arisearch python research/reviews/verify_terra_five_one_opposite_a_row_lift.py

PASS: all12 native placements of each tile, four permitted A/four B row states,
unique two-cycle A transitions, common BB metric and r/r endpoint labels.
The geometric row and exact closure arguments above are analytic and require
hostile review. No solver, geometry sample, chain bound or torus search was used.
This closes only an ACTUAL saturated A012012 field. Extending to arbitrary
original tilings depends on review of the saturation/pure-A extraction;
other nine-word chain mechanisms are not settled by this proof.

## Reviewed all-original-tiling corollary

For every actual A012012/B five-r-one-s pair in the stated x interval, original unrestricted tileability implies a periodic escape. Apply the reviewed defect-free hexagon limit and saturation-capacity extraction. A limit omittingB gives the reviewed monohedral periodic escape. IfB remains, the exact four-star language excludes pureB and the field is mixed/saturated, so the row theorem applies. Both contact and omission quantifiers are retained. Eight other surviving native A words remain unclassified; this corollary does not assert arbitrary-chain periodicity.
