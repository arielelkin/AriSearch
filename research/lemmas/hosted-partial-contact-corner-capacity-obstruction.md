# Hosted partial contacts can exhaust a corner species: a general plane obstruction

Date: 2026-10-12. Status: [fresh hostile review VALID](../reviews/hosted-partial-contact-corner-capacity-review.md).

Let A,B be two fixed genuine compact convex polygons with nonempty interior,
all isometries admitted, and arbitrary partial edge contacts permitted.
Distinguish one native side e of A, one native A corner c, and native B
corners d and f. Assume:

1. Side e is strictly longer than every other native side of either shape.
   Both possible whole e-to-e endpoint identifications are geometrically
   impossible in any tiling (an exact angular exclusion suffices).
2. At every vertex with a straight tile-side sector of angle pi and at least
   one native polygon corner, the native corner sectors include c from an A
   tile and d from a B tile. Each polygon has just one designated native c/d.
3. Native B corner f cannot occur at a vertex carrying any straight pi sector.
   Every full native-corner star containing f includes c from A and contains
   at most one occurrence of f.

Then no plane tiling by A,B exists. These conditions do not require a
frequency limit, finite local complexity, a substitution or prior tileability.

## Each A side hosts a native vertex

Convex polygon tiles form a locally finite family: every copy contains an
inscribed disk of fixed positive radius, their disks are disjoint, and tile
diameters are uniformly bounded. A compact set consequently meets only
boundedly many tiles. Along e, contacts with neighboring tiles form finitely
many whole or partial side intervals. One convex neighbor cannot cover all
of e: its matching side would have length at least |e|, hence must be another
e, and equality of lengths would force the excluded whole e-to-e contact.
Therefore at least two positive contact intervals cover e, with some junction
in its relative interior. At such a junction another tile has a native corner.
A supplies a flat pi sector, while the opposite half-plane is filled by
native corner sectors. Two flat pi sectors cannot coexist with a positive
native sector. Select one such hosted vertex for each A tile.

Selected vertices from distinct hosts are distinct, since the same native
vertex cannot have two flat pi sectors. Each selected vertex consumes a
native c corner and a native d corner. It follows that those resources give
at least one distinct c and one distinct d per A host.

Every B tile contributes its native f corner at a full star. These stars
are distinct by the at-most-one-f hypothesis. Each consumes an additional
native c, disjoint from all c occurrences at hosted flat vertices. Thus
counting on a translation-invariant measure would give

    H>=a, a>=H+b, b>=H,

which forces a=b=H=0. The finite counting argument below supplies the same
contradiction without assuming such a measure exists.

## Finite windows and boundary error

Anchor each tile at a fixed interior reference point. Let a_R,b_R count
anchors in the Euclidean disk of radius R, and H_R count selected hosted
vertices in that disk. All associations above move at most a fixed distance,
because polygon diameters are bounded. The number of tile anchors or vertices
in any annulus of fixed width is O(R), by the disjoint inscribed-disk packing
bound and the bounded number of contacts per tile. Hence the local resource
injections give

    H_R >= a_R-O(R),
    a_R >= H_R+b_R-O(R),
    b_R >= H_R-O(R).

The first two imply b_R=O(R), and the first and third then imply a_R=O(R).
But a plane tiling covers a disk of radius R-D using tiles with anchors in
radius R. Uniformly bounded tile areas give a_R+b_R=Omega(R^2), a
contradiction. Boundary constants depend only on the two fixed polygons.

## Construction application and limitations

The current acute/obtuse feature has native words

    A=(65,140.5,147.5,75,112),
    B=(40,144.5,136,47,172.5) degrees.

Choose e=A0, c=A75, d=B40 and f=B144.5. Its only native180-degree
multiset is (A65,A75,B40). Its only full360-degree multiset containing
B144.5 is (A140.5,A75,B144.5). The designated side has endpoints65 and
140.5; reflected full matching leaves an unfillable79-degree sector,
and half-turn matching leaves an unfillable154.5-degree sector. The exact
coordinate sample makes A0 strictly longest, so the hypotheses apply.

The separate exact feature certificate must independently verify these
star lists, endpoint exclusions and strict metric inequalities. A valid
four-tile local module and a formal positive corner ledger survive those
checks but do not satisfy infinite existence: the additional hosted-contact
lower bound destroys the global ledger. The obstruction is scoped to
these forced-contact resource hypotheses; relaxing strict maximal length,
allowing other flat stars or freeing the required B corner can evade it.
