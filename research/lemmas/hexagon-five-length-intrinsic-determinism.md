# Intrinsic geometric determinism forces a translation lattice

**Status:** adversarially reviewed conditional proof; [fresh independent
hostile review](../reviews/hexagon-five-length-intrinsic-determinism-review.md) valid. The crystallographic conclusion is proved here by an
elementary planar group argument.

**Review:** [independent hostile review](../reviews/hexagon-five-length-intrinsic-determinism-review.md).

## Statement and hypothesis ledger

Let T be an edge-to-edge plane tiling by finitely many compact convex polygon
congruence classes, with nonempty tile interiors. Suppose its full-side tile
adjacency graph is connected. Reflected copies are permitted.

Assume the following **additional, conditional** data exist:

1. A finite intrinsic state set S. Every state s specifies an actual reference
   polygon P_s with fixed side/vertex indices. A state may refine a prototile
   class by finitely many flags; it does not specify absolute position or angle.
2. Each tiling tile U is assigned a state s(U) and an indexed placement isometry
   g_U from P_(s(U)) to U. Any reference symmetries are resolved by these indices.
3. For every reachable state s and side index i of P_s, there is one fixed
   triple (s',j,h_(s,i)), where h_(s,i) is a **complete plane isometry**, such
   that the unique tile V across U's full native side i satisfies

       s(V)=s',      g_V = g_U composed with h_(s,i),

   and h_(s,i) matches reference side j of P_s' to reference side i of P_s,
   with polygon interiors on opposite sides. Thus endpoint matching, relative
   displacement, orthogonal part, and neighbor indexing are all specified.

Then T has two linearly independent translational periods. No finiteness of
absolute tile orientations is assumed.

The full-side condition and graph connectivity are hypotheses here, not
conclusions for arbitrary contacts. The state finiteness and unique complete
relative isometry are also hypotheses; finite symbolic matching rules with
branching are insufficient. In applications the geometric shape constraints
must establish these hypotheses, including reflections and both endpoints.

## Proof

For tiles U,W of the same state, define I=g_W composed with g_U^(-1). If V is
the neighbor of U across side i, the neighbor X of W across corresponding
side i has placement g_X=g_W composed with h_(s,i). Consequently

    I composed with g_V = g_W composed with h_(s,i) = g_X.

The states and full indexed placements correspond. Iterate across the connected
full-side adjacency graph. Every source tile is carried to a tile of T, with
its state and indexing. The images cover the plane, so the image collection
is the whole tiling. Thus I is a symmetry of the framed tiling.

Let G be the group of plane isometries preserving this framed tiling. Equal
states lie in one G-orbit, so G has finitely many tile orbits. Choose one
compact representative tile per orbit and let K be their union. G K is the
plane, so G acts cocompactly.

G is discrete. If g_n in G converges to the identity, take an interior point p
of a fixed tile U. For large n, g_n(U) contains p in its interior. Only U can
do so, hence g_n(U)=U. A nondegenerate polygon has a finite isometry group;
therefore g_n is eventually the identity. This also proves discreteness if
one forgets the states and indices.

Let N be G's subgroup of translations. It is normal, and its vectors form a
discrete additive subgroup of R^2. Suppose first that N is trivial. The
orientation-preserving subgroup H of G injects, by taking linear parts, into
SO(2). Since SO(2) is abelian, H is abelian. An orientation-preserving plane
isometry is a translation or a rotation. With no nonidentity translations,
every nonidentity member is a rotation. If H contains one nonidentity rotation,
all members of H commute with it and fix its unique center. Thus H lies in a
compact circle group and its discreteness makes it finite. If H contains no
such rotation, H is trivial. H has index at most two in G, so G is finite,
contradicting G K=R^2 for compact K. N is therefore nontrivial.

A discrete additive subgroup of R^2 is a lattice in its linear span, of rank
one or two here. If N had rank one with primitive vector v, conjugation by
any g in G would send v to v or -v. The linear part of g therefore preserves
the axis spanned by v. There are only four orthogonal maps with that property.
The kernel of the linear-part homomorphism is N, so G/N has at most four
members. G K would then be a finite union of translates of bounded sets along
parallel rank-one lattice cosets; its coordinate perpendicular to v would
be bounded. It cannot be R^2, a contradiction. N has rank two, and its basis
vectors are two linearly independent periods of T. QED.

## Difference from previous conditional periodicity

The former [full-placement state theorem](hexagon-limit-and-periodicity.md)
assumes finitely many absolute orthogonal parts. Here only intrinsic states
are finite; repeated states produce global plane isometries, and discreteness
plus cocompactness forces translations. There is no assertion that arbitrary
two-hexagon tilings have unique relative neighbor maps. This lemma cannot
replace that missing shape-only determinism obligation with symbolic finiteness.

A concrete application with independently checked endpoint maps is
[the private-repeat hexagon theorem](hexagon-five-length-private-repeat-periodicity.md).
