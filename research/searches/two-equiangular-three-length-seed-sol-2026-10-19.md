# Minimal integer three-length seed after the binary obstruction

Status: candidate metric pair only; no infinite tiling or periodicity proved.

Take the positive length words

    A=(1,2,2,2,1,3), B=(3,2,2,2,3,1),

with successive headings 0,60,120,180,240,300 degrees. Exact coordinates
are obtained by summing l_i(cos(i*pi/3),sin(i*pi/3)), so all coordinates
are in Q(sqrt(3)). Opposite differences are respectively -1,-1,-1 and
+1,+1,+1. Both close and are strictly convex equiangular hexagons, neither
centrally symmetric. The multisets differ (A has two 1 sides and one 3;
B has one 1 side and two 3), so arbitrary rotations/reflections do not
identify the prototiles. The two words belong to the symbolic family

    A=(a,a+t,a+t,a+t,a,a+2t),
    B=(a+2t,a+t,a+t,a+t,a+2t,a), a,t>0.

This is minimal only in the precise sense of using the smallest three
positive integer values, {1,2,3}; it is not a minimality claim over real
metrics or tiling complexity. It is a seed for a new construction, not a
pair already shown to tile.

## Exact local gate and its limit
The unordered adjacent length pairs for either word are

    {1,2}, {2,2}, {2,3}, {1,3}.

Thus the corner transition graph has a genuine 1-2-3 triangle and a loop
at 2. The bipartite corner obstruction for two alternating binary words
fails sharply: a 120-degree three-corner star with outgoing lengths
1,2,3 can use the native corner types (1,2),(2,3),(3,1), all present.
Another exact legal star uses three (2,2) corners. Sectors of angle120
place these corners without overlapping interiors near the vertex;
reflections allow either endpoint ordering. No assertion about extension
beyond this finite star is made. Equal adjacent labels must be retained
as loops: treating the graph as simple and deleting the (2,2) loop would
incorrectly discard this second star.

## Cheap quotient parity gate
A periodic full-edge quotient with n_A copies of A and n_B copies of B
has 2n_A+n_B edges of length1 counted with multiplicity and n_A+2n_B
edges of length3. Each must be even, so n_A and n_B are individually even.
In particular no translation quotient with exactly one of each species
exists. This is only a parity restriction: larger periodic quotients,
rank-one periodic tilings, or nonperiodic tilings are not excluded.
A quotient may be replaced by a finite-index cover, so the parity alone
cannot obstruct any given infinite periodic tiling.

No unbounded search was run. The two words were selected by the exact
closure formula, and all displayed checks are direct integer identities.
The next obligation is a complete infinite matching assignment or an
explicit periodic escape; enlarging patches without an extension mechanism
would supply no proof of either. No novelty claim; not hostile-reviewed.
