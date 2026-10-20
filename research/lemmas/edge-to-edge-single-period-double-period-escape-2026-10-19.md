# Edge-to-edge single-period tilings admit a double-period escape

Date: 2026-10-19. Status: proved within stated scope; [independent Sol hostile review](../reviews/edge-to-edge-single-period-double-period-escape-hostile-sol-2026-10-19.md) PASS.
This is a restricted structural lemma, not a resolution of the two-tile problem.
No novelty claim is made. No computation or literature theorem is used.

## Statement

Let F be a finite set of compact convex polygons with nonempty interiors.
Suppose an edge-to-edge F-tiling of the plane is invariant under a nonzero
translation T. Then F admits an edge-to-edge tiling invariant under two
linearly independent translations. Reflections are allowed throughout.
The new tiling can differ from the given one.

Here edge-to-edge means that an intersection of two distinct tiles is empty,
a common native vertex, or a complete native side of both tiles. The proof
also works for any finite polygon protoset with uniform positive inradius
and bounded diameter, whenever bounded sets meet uniformly finitely many
tiles and its full-side adjacency graph admits the bounded paths used below.
Only the stated convex case is asserted here.

## 1. Uniform bounded path lemma

Choose a diameter bound D and, in each reference polygon, an interior disk
of radius at least rho>0. The transported disks are disjoint. Every tile
meeting a ball of radius R has its disk center within R+D of its center.
Area packing therefore bounds the number of such tiles by a constant N(R),
uniformly in the ball location and the tiling.

For two interior points at distance at most R, a generic polygonal path can
be taken inside the ball of radius R+2D+1 about the first point, missing all
native vertices and crossing sides transversely. There are only finitely
many vertices in the ball by the packing bound. Removing loops in its tile
adjacency walk gives a path of at most K(R)=N(R+2D+1) full-side adjacencies.
Convexity ensures that crossing a side away from its endpoints crosses to
the unique tile matched along that complete side. The path may be perturbed
arbitrarily little to avoid a straight segment running along a side.

For indexed reference polygons there is a finite set H of relative
isometries that match one whole reference side to another, with opposite
interiors. Choose two side slots, two endpoint correspondences and two tile
types. Each choice gives at most one relative isometry. Thus a bounded
adjacency walk has relative placement in a finite set of products H^{<=K}.

## 2. A period discretizes absolute orientations

Write a placed tile as f(P), f(x)=g x+b, with g orthogonal, and choose an
interior reference point c_P. Its T-translate has interior point f(c_P)+T.
A full-side walk of length at most K(|T|) reaches it. Lift the indexed
placements along that walk using H. The last placement is f h(P), for some
h in the finite product set, and physically equals f(P)+T. Because initial
and final types are the same congruence class, h(P)=P+w where w=g^{-1}T.
Taking centroids gives the uniquely determined displacement

    w = centroid(h(P)) - centroid(P).

This belongs to a finite set and is nonzero. The identity g w=T permits
at most two orthogonal maps g for each nonzero w. Hence, for this fixed
period vector, there are finitely many possible absolute tile orientations.
Reference symmetries and reflections merely enlarge the finite list; no
canonical indexing of symmetric copies is required.

Consequently every patch of bounded diameter meeting a selected tile has
only finitely many possibilities up to translation. Indeed the selected
tile has finitely many type/orientation choices, and every tile of the
patch is joined to it by a uniformly bounded full-side path as in Section 1.
The finite product set bounds every relative placement, so there are only
finitely many subsets of the resulting finite candidate placement set.

## 3. Finitely many complete cylinder collars

Rotate coordinates so T=(ell,0), ell>0, and quotient by T to a cylinder C.
The given periodic tiling descends to a locally finite cylinder tiling.
Use tile centroids as anchors. The positive inradius and finite diameter
imply that for arbitrarily high y there are tile centroids there.
Select tiles with centroid heights y_n tending to positive infinity, with
successive heights separated by more than 10D. Choose each centroid lift
(x_n,y_n) with x_n in [0,ell).

For each n retain all complete tiles, modulo T, whose interiors or boundaries
meet the horizontal cylinder collar |y-y_n|<=2D. Express the entire collar
patch relative to the selected centroid (x_n,y_n). Every retained tile has
a suitable planar lift within distance ell+4D of that centroid, and the
selected tile also belongs to this patch. Section 2 therefore gives only
finitely many exact normalized cylinder patches. We retain complete tile
polygons, their types and absolute orientations, and the horizontal collar
levels relative to the anchor. Lifts at the x seam are represented modulo T;
only finitely many lifts are needed within the bounded rectangle.

Two indices i<j have identical normalized collar patches. Put

    U=(x_j-x_i, y_j-y_i).

Translation U identifies the complete tiling in the two cylinder collars.
Its vertical component L=y_j-y_i is greater than 10D, so U and T are
independent. There is no assertion that U preserves the original whole plane.

## 4. Exact cut and repeat

In the original plane choose precisely the tiles whose centroid height lies
in the half-open interval [y_i,y_j). Include all their integer T-translates;
this is just the entire original periodic tile layer with those anchors.
Repeat this layer by all translations kU, k in Z.

Away from the horizontal seams y=y_i+kL by distance greater than D, this
family agrees locally, after translation by kU, with the original tiling.
Near a seam only tiles with centroids within 2D of the corresponding two
original seam levels can matter: every point of a polygon is at distance
at most D from its centroid. Equality of the complete collar patches
identifies exactly those tiles. The tiles selected from below and from
above consequently coincide with the two complementary centroid selections
in one original collar. At centroid height exactly on the cut, the half-open
convention assigns the whole tile to exactly one side; the matching lower
and upper copies are identified by U. No tile is cut geometrically.

Thus each point has a neighborhood on which the new family is exactly a
translate of an original tiling patch. This proves disjoint interiors,
coverage, and native edge-to-edge contacts, including every seam point.
The family is invariant under T and U by construction. This proves the lemma.

## Scope, dependencies, and stop condition

This differs from periodic-carrier band completion: the starting tiling
already has a period, and equal transverse cylinder collars construct a
second period. It needs no private side, unavoidable species, anchored
lattice, or assumed finite set of orientations. The discretization step
uses full native sides and fails for unrestricted sliding partial contacts.

If geometry forces EVERY admitted tiling to be edge-to-edge, then absence
of doubly periodic tilings implies absence of ANY translationally periodic
tiling. In a problem whose original tilings need not be edge-to-edge,
an edge-to-edge limit theorem alone does not transfer an original period
to a limit and is insufficient for that implication.

The result supplies no bound on the original period length. It does not
license upgrading any bounded torus search to an unrestricted exclusion.
No candidate pair or new plane extension is obtained. Stop this branch;
reopening requires a concrete candidate with forced edge-to-edge contacts
and a complete (unbounded) double-period obstruction, rather than a larger
finite torus search.

Internal audit and independent hostile review checked bounded paths, symmetry
of reference polygons, reflection cases, exact collar equality modulo T,
centroid ties, arbitrary skew U, and preservation of whole tiles at cuts.
