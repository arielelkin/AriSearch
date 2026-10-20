# Alternating binary hexagon: bipartite-partner charge obstruction

Date: 2026-10-19. Status: proved internally; fresh hostile review pending.
The initial global charge proof is valid, but exact closure strengthens it
to an uncompletable native corner; no genuinely global gain is claimed.
One exact structural design cycle, no search or new solver domain.

## Theorem and scope
Let A be a strictly convex equiangular120-degree hexagon with length word
(a,b,a,b,a,b), a,b>0, a!=b. Let B be any strictly convex equiangular120-degree
hexagon. Form its numerical-length corner graph G_B: vertices are actual
numerical side lengths, and every adjacent pair in the native cyclic word
is an undirected graph edge; equal adjacent lengths give loops.

1. If G_B is bipartite, {A,B} does not tile the plane.
2. In particular, if B is noncentral and has no two consecutive sides of
   equal numerical length, {A,B} does not tile the plane.
3. Consequently, any potentially aperiodic pair having this A must have
   a noncentral B with at least one consecutive equal-length pair. If B
   is central instead, B alone provides the standard hexagon lattice escape.

Reflections, arbitrary rotations, partial-edge contacts, and omission of
either species are included. No claim covers the remaining equal-adjacent
noncentral B words. This is a necessary gate, not a complete classification.
No novelty claim; no literature theorem is needed beyond elementary
Euclidean tiling geometry. The prior reviewed full-edge trivalent reduction
can be replaced by the local120-degree sector argument below.

## Contact and corner support reduction
All corner angles are120 degrees. A tile corner inside another tile's
side would leave180 degrees to be filled by120-degree sectors, impossible.
Thus all contacts are full sides, with three corners at every vertex.
At such a vertex its three outgoing ray lengths x,y,z form a triangle
(including repeated vertices/loops) in the union of corner graphs.
A's graph is the single edge {a,b}. A-only tiling is therefore impossible.
B-only tiling is impossible if G_B is bipartite, since an odd closed walk
cannot occur in a bipartite graph. Thus any assumed tiling uses both types.

If a or b is absent from G_B, a vertex containing A cannot close: one A
corner requires the edge a-b, two A corners would require a B loop aa or
bb, and one A corner with two B corners requires both labels in G_B.
If a,b lie in opposite parts of one B component, adding a-b preserves
bipartiteness, so there is no vertex at all. For disconnected G_B choose
partitions component by component: if a,b are in different components,
choose opposite parts and reach the same contradiction. The only case
left is a,b in the SAME part of one B component.

There can be neither AAA nor BBB vertices, and AAB requires a B loop aa
or bb, forbidden by bipartiteness. Every vertex must therefore be ABB.
Its ray lengths are a,b,x and its B corners are {a,x},{b,x}. In particular
EVERY corner of B must contain exactly one public label a or b. A native
corner with neither would be unable to occur anywhere; a native corner
with both is a forbidden bipartite same-part edge. Hence B alternates
public sides from {a,b} with other sides; it has exactly three public
sides. This conclusion uses actual tile occurrence, not independently
extendible stars.

## Simplest metric proof: an unavoidable uncompletable corner

The previous reductions already force B to alternate public and private
sides. Write its cyclic word (p,x,q,y,r,z), with p,q,r in {a,b}, and
x,y,z outside {a,b}. Exact closure gives

    x=r-delta, y=p-delta, z=q-delta.

If all p,q,r are equal, B contains no corner involving the other public
label, so no ABB star is possible. Otherwise, after interchanging a,b
and cyclically shifting by an even number of positions, take p=q=a and
r=b. Then x=b-delta is a private value occurring exactly once, while
y=z=a-delta is a different private value (a!=b). The unique x side is
flanked by a sides at both ends. B therefore has an (a,x) corner but no
(b,x) corner. Its (a,x) corner cannot complete an ABB star. This is a
pointwise contradiction, stronger than the global charge below. There
is no equality exception: disjoint bipartition classes already ensure
x,y,z are not a or b, and x!=y follows from a!=b. Thus NO positive
closing B in this subfamily has a locally compatible star at every native
corner. The charge is preserved only as a useful symbolic diagnostic;
it adds no metric scope here.

## Optional global signed corner charge
Give every B corner incident to its side of length a charge+1, and every
B corner incident to its side of length b charge-1. These assignments are
intrinsic and unchanged by reflection. Every B corner has exactly one
such side, as just proved. Every ABB vertex has one charge+1 corner and
one charge-1 corner, hence net zero.

A whole B has charge

    C_B=2(n_a(B)-n_b(B)),

where n_a+n_b=3. Therefore C_B is a nonzero integer. This incompatible
bulk charge gives an alternative global obstruction. For symbolic words
without exact closure, all individual corners can have locally legal
supports: (a,x,a,x,b,x) has both required corner types. Such a word
does not close as a120-degree hexagon when a!=b. No claim of an exact
closing locally complete B example is made.

For completeness, justify the infinite counting step rather than silently
summing divergent quantities. Fix a large disk D_R and sum complete tile
charges of tiles wholly inside it. Each interior vertex whose incident
tiles are all selected contributes zero. The remaining contributions lie
in a bounded-width boundary annulus. There are O(R) tiles there: each has
one of two fixed positive areas, their interiors are disjoint, and their
diameters have a fixed upper bound. Hence

    C_B N_B(R)=O(R).

Since every vertex is ABB, counting A and B corners in the same
disk yields6N_B(R)=12N_A(R)+O(R). Combined with positive-area coverage,
this forces N_B(R)=Omega(R^2), contradicting the nonzero charge identity.
All discrepancies are in the same bounded-width boundary annulus.
This proves assertion1 for arbitrary infinite tilings, not just periodic ones.

## Deriving the no-equal-adjacent partner corollary
For any equiangular closing native word l, exact closure is

    l0-l3=l2-l5=l4-l1=delta.

B noncentral means delta!=0, so no two opposite native side positions
can have the same length. The no-equal-adjacent hypothesis prohibits
repeated labels at cyclic distance1 or5. Therefore every repeated label
occurs only at cyclic distance2 or4: the even-position and odd-position
length palettes are disjoint. These two palettes bipartition G_B, proving
assertion2. This includes arbitrarily many lengths (up to six), arbitrary
real equalities among nonadjacent positions, and all reflection phases.

A concrete closing noncentral metric in the excluded subfamily is

    B=(1,5/2,1,3/2,2,3/2), delta=-1/2.

The even palette is {1,2}, odd palette {3/2,5/2}; both are disjoint.
Every length is positive and all turns are60 degrees, so B is strict.
Together with A=(1,2,1,2,1,2), it cannot tile, despite some locally
legal ABB stars using the shared private length3/2.

## Remaining mechanism and stop
The known periodically escaping fixture B=(2,2,3,1,3,2) has consecutive
equal2 sides and passes this necessary gate, as expected. Likewise the
three-length seed B=(3,2,2,2,3,1) has adjacent equal2 sides. The theorem
does not claim either fixture is representative of every surviving word.

A fresh global mechanism would have to control B corners at its repeated
adjacent lengths: those loops permit BBB or AAB stars and absorb the
signed charge above. The exact missing step for unrestricted B is a
replacement nonzero bulk charge, a forced repeatable strand, or another
complete global argument accommodating these loop stars. No such invariant
is established here. This cycle stops after the proved broad gate; no
larger corona, quotient, or bounded enumeration was run.

## Reproducibility
This artifact is a self-contained proof with one exact rational example.
There is no computational enumeration, certificate cutoff, solver version,
or random seed. Check the sample closure by the displayed rational differences.
Independent hostile review is required before integration as reviewed mathematics.
