# Squared-pinwheel four-face geometric omission gate

Date: 2026-10-13. Status: cheap exact construction gate passed; this specific whole-face route discarded. Fresh independent review VALID for the stated finite domain: [contact review](../reviews/affine-two-convex-pinwheel-four-face-hostile-review.md). This is not a broad impossibility theorem.

The proposed changed scalar route was M²=((3,4),(-4,3)), ordinary similarity factor5, with P and Q made of four whole 1-2-sqrt5 triangles. A parent would contain100 primitive triangle cells and need25 four-triangle children. Before selecting an actual parent dissection or searching its child exact cover, the minimal geometric omission gate below already kills the route. No100-cell source,25-child contact scheme or substitution was constructed; no such thing is asserted.

Exact finite domain: all unions of four congruent unit-area triangles, connected by full native-side adjacency. Any additional contacts may be partial. Anchor one triangle at((0,0),(2,0),(0,1)); add each child by reflection across or half-turn about a current full native edge; retain disjoint interiors. All isometries are thereby included because the triangle has three distinct side lengths. Congruence of convex boundaries is reduced by the full squared-distance matrix under cyclic/reversed indexing. Hull area four is equivalent to convex union once the four tile interiors are disjoint. Domain output is1,6,36,221 anchored patches and15 convex classes: one triangle, ten quadrilaterals, three pentagons, one hexagon. The producer openly reuses the earlier exact rational primitive functions; it is not an independent review.

The ONLY class with at least six genuine sides is

    H=((0,0),(6/5,-8/5),(2,-1),(2,0),(4/5,8/5),(0,1)).

It is centrally symmetric about(1,0). Opposite edge midpoint differences are (4/5,8/5),(-6/5,13/5),(-2,1), with the latter equal the difference of the first two. Its area is4. Its translates by lattice basis (2,-1),(4/5,8/5) have covolume4 and cancel all six oriented edges in three reversed pairs. Periodic multiplicity consequently has zero distributional gradient and area mean one; local finiteness gives full covering with disjoint interiors. Thus H alone admits a periodic plane tiling.

Because omission of P is admitted by the original problem, any proposed P5/Q6-or-higher pair made solely from this four-whole-triangle domain has an immediate periodic escape. Triangles/quadrilaterals already have their usual omission escapes, and no higher class exists. The pentagon without adjacent supplementary angles does not rescue a pair whose higher-sided Q already tiles alone. No squared-pinwheel parent exact-cover search is justified in this domain.

This gate does not exclude partial-only-connected four-triangle unions, clusters with cut triangle atoms, other cluster sizes, or different scalar parent geometries. Increasing the cluster-size bound alone would not constitute the requested changed construction; a concrete parent resection and two-class contact scheme would be needed first. The discarded gate is kept for restartability rather than promoted to a resolution.

Replay (full exact class coordinates and triangle decompositions on stdout):

    mise exec -- conda run --no-capture-output -n arisearch python research/searches/affine-two-convex-pinwheel-four-face-gate.py

## The already enumerated two-pentagon choices

The three pentagon classes are:

    A=((0,-1),(4/5,-8/5),(2,0),(4/5,8/5),(0,1)),
    B=((0,-1),(4/5,-8/5),(2,0),(2,1),(0,1)),
    C=((0,-1),(4/5,-8/5),(14/5,-3/5),(2,0),(0,1)).

A has no adjacent supplementary corners; no mono-tilability classification is made here. B has a supplementary pair at indices3,4 and C at1,2. Joining a copy to its half-turn across that connecting native edge gives a convex central hexagon of area8. The exact doubled hexagons and lattice bases are:

    Bdouble=((0,-1),(4/5,-8/5),(2,0),(2,3),(6/5,18/5),(0,2));
    Bbasis=((6/5,23/5),(-4/5,18/5));
    Cdouble=((0,-1),(8/5,-11/5),(18/5,-16/5),(18/5,-6/5),(2,0),(0,1));
    Cbasis=((2,1),(-8/5,16/5)).

In each case the half-turn copies have disjoint interiors and hull area8, so they exactly partition the hexagon. Opposite-edge translations are the two basis vectors and their difference, and covolume8. The same complete oriented-boundary multiplicity proof gives a periodic tiling by each doubled hexagon and hence by its two P copies. These are explicit mono-periodic omission carriers for B and C.

Every selection of TWO DISTINCT pentagon classes from {A,B,C} contains B or C. Thus these exact three possible two-pentagon choices all admit an omission escape, without asserting that A tiles alone. This conclusion uses the two supplementary carriers and the complete finite class census; it is not inferred from the sole-hexagon observation. No classification of arbitrary four-triangle pentagons outside the full-native-side-connected domain follows.
