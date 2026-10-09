# Two-type degeneracies in Sugimoto's convex dissections

**Status:** primary-source reconnaissance; reported negative examples, not an
independent exact proof.

## Source and convention

Teruhisa Sugimoto, *Aperiodic sets of three types of convex polygons*,
arXiv:2404.00534v5, studies five-piece convex dissections of the chiral
Tile(1,1).  The paper normally treats front and back as different types and
forbids reflected placements.  Our target instead permits reflection, so its
positive claims cannot be imported.  Section 2 explicitly says the divided
sets have periodic tilings when reflected pieces are allowed.

## Reported parameter collisions

The paper nevertheless explores precisely the tempting way to reduce its
three convex congruence classes to two.  The reported collisions all fail:

* Method 1 at \(\alpha=105^\circ\), equivalently Method 2 at
  \(\beta=105^\circ\), makes two dissection pieces identical.  The remaining
  convex hexagon is a Type-1 monohedral tiler and has a periodic tiling.
* At \(\alpha=165^\circ\) (or \(\beta=165^\circ\)), the paper reports that
  none of the individual pieces tiles monohedrally even with reflections,
  but two of the resulting convex classes together have the displayed
  periodic tiling in its Figure 6.
* Method 1 at \(\alpha=180^\circ\) again has individually non-monotile
  pieces, but two pentagons have the displayed periodic tiling in Figure 7.
* Method 4 at \(\gamma=150^\circ\) produces two convex types, one a Type-1
  convex-hexagon monotile.

Thus both failure modes predicted by the current structural work occur in a
published construction family: either one member has a periodic monohedral
escape, or the pair itself has a periodic mixed tiling even though its
members reportedly do not tile alone.

## Implication for the search

Simple congruence specialization of this Tile(1,1) dissection family is not a
candidate.  More importantly, checking that each member is not a monotile is
not enough; the mixed periodic-tiling search is an independent acceptance
gate.  A future use of a hat-family dissection must start from a source that
is aperiodic under reflections and must enumerate the geometry admitted by
the convex pieces, rather than inherit the source tile's chirality argument.
