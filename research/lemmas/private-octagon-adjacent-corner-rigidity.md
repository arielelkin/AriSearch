# A direct private-octagon theorem and universal pentagon corner rigidity

**Status:** adversarially reviewed; [fresh independent review](../reviews/private-octagon-adjacent-rigidity-review.md) valid. This strengthens the separate weaker
[distinct-length periodic-escape theorem](private-octagon-distinct-pentagon-periodic-escape.md).
Its author reviewed the weaker statement; the independent reviewer of this
stronger theorem did not develop it. This file is not a
solution of the unrestricted two-convex-polygon problem, and makes no
literature priority claim.

## Intrinsic corner rigidity and its exact classification

A genuine convex equiangular108-degree pentagon P has **adjacent-corner
rigidity** if two specified noncollinear whole line segments meeting at
108 degrees, together with their interior108 wedge, determine at most one
geometric placed copy of P having those two segments as adjacent native
sides. Copies may be rotated or reflected; uniqueness concerns the actual
polygon subset, not a labeled native placement.

**Classification.** Such a P has adjacent-corner rigidity if and only if
at least one of the following holds:

1. its five native lengths are pairwise distinct;
2. it has a reflection symmetry.

The regular pentagon is included in the second case. A nonregular reflection
case has cyclic lengths

    (a,b,c,b,a),  c=phi*a-b/phi,  a,b>0,  b<phi^2*a,  a!=b,   (1)

where phi=(1+sqrt(5))/2. Its three values a,b,c are automatically pairwise
distinct. This is a complete metric description of the reflection case,
up to cyclic relabeling and unrestricted isometry.

### Proof of necessity

Suppose corner rigidity holds and some native length repeats. In a five-
cycle any two distinct edge slots have cyclic distance1 or2. If equal
lengths occupy adjacent slots, reflection of P in that corner's angle
bisector exchanges the equal whole segments and preserves the108 wedge.
Both copies meet exactly the same prescribed data, so rigidity says that
this reflection is an actual symmetry of P.

If a repeated value occurs in slots at distance2, the intervening side
forms an adjacent pair with each occurrence. If it has that same value,
the preceding case applies. Otherwise the two distinct native corners
have the same unordered pair of unequal lengths and the same108 angle.
Place the polygon from those two corners onto one prescribed wedge and
its unequal side segments. Rigidity identifies the resulting geometric
copies. Composing their placement maps yields a nonidentity symmetry of
P carrying one native corner to the other.

The symmetry group of a genuine convex pentagon acts on its five vertices
as a subgroup of their cyclic dihedral group. A nonidentity orientation-
preserving symmetry has order5 and forces P to be regular. Otherwise the
nonidentity symmetry is a reflection. Thus a repeated length under corner
rigidity always implies a reflection symmetry, proving necessity.

### Proof of sufficiency and exact metric formula

With five distinct lengths, the two prescribed lengths identify unique
native sides. Their common vertex is unique, the unequal assignments to
the segments are fixed, and the three noncollinear endpoints determine
at most one isometry. This includes reflections.

A reflection of a five-sided convex polygon fixes one native vertex and
the midpoint of its opposite side. The side length word, starting at the
fixed vertex, is(a,b,c,b,a). Put z=exp(pi*i/5). An equiangular108 pentagon
has successive side directions1,z^2,z^4,z^6,z^8. Closure gives

    a*(1+z^8)+b*(z^2+z^6)+c*z^4=0.

Since1+z^8=-phi*z^4 and z^2+z^6=z^4/phi, this is precisely c=phi*a-b/phi.
Its positive cone is the one in (1). Conversely the positive closed walk
in these increasing directions is strictly convex and the palindromic
length word gives its actual reflection fixing the indicated vertex.
The reflected native walks coincide because their starting vertex, first
edge and successive angle/length data coincide.

If any two of a,b,c are equal, the closure relation forces a=b=c; this is
the regular case. Otherwise the five native corner pair types are one
(a,a), two(a,b), and two(b,c). The latter two pairs are precisely orbits
of the actual reflection. Thus all choices of a native corner with the
prescribed unequal lengths give the same placed polygon by composing
with that reflection. At the(a,a) corner, exchanging the equal segments
is exactly its existing reflection. Every ambiguity is an actual global
symmetry, so no second geometric placement is possible. For the regular
case its dihedral symmetries likewise identify every native corner and
both segment assignments. This proves sufficiency and the classification.

## Every equiangular pentagon has this rigidity

The preceding apparent alternative is exhaustive for every genuine convex
equiangular108 pentagon, because **any repeated native side length forces
an actual reflection symmetry**. Here is the exact closure argument.

Put w=exp(2pi*i/5)=z^2 and let its positive native lengths be L_0,...,L_4.
After a rotation, closure is

    sum_(h=0)^4 L_h*w^h=0.                            (2)

Suppose L_i=L_j for distinct slots i,j. The index involution

    rho(h)=i+j-h mod5

swaps i,j, swaps one other pair p,q and fixes the remaining slot. The
permuted length vector also closes, since

    sum_h L_(rho(h))*w^h
       =w^(i+j)*conjugate(sum_h L_h*w^h)=0.

Subtracting these two closures gives exactly

    (L_i-L_j)*(w^i-w^j)+(L_p-L_q)*(w^p-w^q)=0.

The first term vanishes and w^p!=w^q, hence L_p=L_q. Thus the whole native
length word is invariant under the reflection permutation rho. The uniform
turn angles show that the reflected edge walk is the same polygon after
a translation and rotation; equivalently the polygon has an orientation-
reversing self-isometry with this vertex/side involution. Such an isometry
of a compact polygon must be an actual reflection, since a nonzero glide
reflection would square to a nonzero translation preserving a compact set.
This establishes the asserted reflection symmetry.

Therefore every equiangular108 pentagon either has five distinct lengths,
has a nonregular reflection word(a,b,c,b,a) with exactly three distinct
values, or is regular. Each case has adjacent-corner rigidity by the proved
classification. In particular there is no exceptional repeated-length
equiangular pentagon with an unresolved local two-side branch.

## Direct every-tiling theorem

Let P be any genuine convex equiangular108 pentagon. Let Q be a genuine convex octagon with two nonadjacent108 corners
and six144 corners. Suppose Q has two different native length values x,y,
each occurring exactly once on Q and neither occurring on P. The other six
Q lengths are unrestricted. Then **every admitted plane tiling by{P,Q} has
a nonzero translation period**.

The universal rigidity theorem just proved supplies the needed local
uniqueness for every P metric, including repeated-length and regular cases. It needs no
defect-free limit and allows additional Q-to-Q contacts in the original
tiling. It establishes one period, without a rank-two or finite-cell claim.

### Original-tiling private chains and their common period

Fix any admitted plane tiling T. By the independently reviewed
[all-obtuse forcing theorem](obtuse-edge-forcing.md), its contacts are full
native sides and every vertex has three genuine sectors. The only sector
sum is108+108+144=360. Thus two144 sectors cannot meet at a vertex.

An x/y side cannot meet P and so meets the identical unique side of a Q
copy. Q has no108/108 side. A144/144 private side would match that same
native type on the other Q and produce two144 sectors at a vertex. Hence
each private side is108/144, and its endpoint correspondence exchanges
the corner types. The mate is exactly the half-turn about its midpoint:
the alternative endpoint-exchanging reflection preserves the supporting
interior half-plane and causes overlap along the shared side. This argument
also applies to reflected placed Q copies.

Consider the graph using only those two private contacts at each Q. Every
Q is a vertex of degree2, even if it has other Q contacts. Its two mates
are different: two distinct whole sides shared by genuine convex polygons
would have a positive-area convex hull in their intersection. Let a,b be
the two native private midpoints, with d=b-a!=0. The open midpoint chord
lies strictly inside Q because its endpoints lie on distinct genuine sides.
Across either private side, the half-turn extends the chord straight past
its shared endpoint. Starting at Q and following the b mate then the a
mate gives

    Q, H_b(Q), Q+2d, H_b(Q)+2d, ...

and extending backwards gives all integer translates of these two copies.
The chords cover their entire affine line in intervals of fixed positive
length|d|. No cycle or additional branch exists. A placed chain under
isometry F has period u_F=2L_F*d, where L_F is its orthogonal linear part.

Different chain axes cannot intersect. An intersection involving an open
chord puts a different closed tile inside a Q interior and creates an open
interior overlap. At a chord endpoint, full native-side matching permits
only its two Q side mates, which belong to the same private chain. Thus
axes are disjoint entire lines, hence parallel. All u_F have length2|d|
and are parallel, so they are the two signs of one nonzero vector u.
Both signs preserve each chain. Every Q belongs to its private chain, and
therefore the entire Q occurrence set is invariant under both u and -u.

These are pointwise facts in the original T, without a saturation count.
They are the midpoint mechanism in the independently reviewed
[regular-P theorem](regular-pentagon-private-octagon-periodicity.md), with
its pentagon regularity used nowhere in the chain argument.

### Every P has prescribed Q data and inherits the period

At a P corner two P side neighbors would give three108 sectors, whose
sum324 is impossible. Thus its P-neighbor slots are nonadjacent and number
at most2; every P has at least3 Q side neighbors. Any three slots in a
five-cycle include two consecutive slots. Consequently every P has at
least one corner with two Q side neighbors, hence a PQQ star. This need
not be its only PQQ corner.

Choose such a corner v of an occurrence P0. Its two adjacent Q copies
prescribe the residual108 wedge and both adjacent whole side segments of
P0. Translation by u sends these Q copies to actual Q copies and sends
all the prescribed data to their translates at v+u. Full-side contacts and
trivalence ensure an actual third tile R occupying the residual wedge.

If R had type Q, invariance of the whole Q set under -u would give an
actual Q tile R-u at v. Its positive corner sector would lie inside P0's
108 wedge near v, creating positive-area interior overlap with P0. Hence
R has type P. By adjacent-corner rigidity it equals P0+u as a polygon.
This proves that every P translates to an actual P under u. Repeating the
same argument with -u proves the reverse inclusion. The entire P occurrence
set and the entire Q occurrence set are therefore invariant under u!=0.
This proves the direct every-tiling theorem.

## Independent review and scope

The [fresh hostile review](../reviews/private-octagon-adjacent-rigidity-review.md) validates the classification, repeated-length reflection argument, universal corner rigidity and direct every-original-tiling theorem. Its [independent exact checker](../reviews/verify_private_octagon_pentagon_rigidity.py) checks all10 repeated-edge pairs and reflected walks without relying on this proof. The stronger statement explicitly supersedes the weaker good-limit periodic escape; it does not depend on that limit.
Potential attacks include reflection branch choices at equal adjacent
lengths, the five-cycle repeated-length necessity argument, all-Q chain
inclusion when extra Q contacts occur, and the pullback exclusion of a Q
third sector in an original tiling with defects.

Only the reviewed all-obtuse full-edge/trivalent forcing is imported into
the direct theorem; no classification of monohedral pentagons, exact search,
compactness limit, or literature priority is used. Additional unshared Q
lengths are permitted by the statement; they may instead force no tiling.
Repeated private values, a missing second private side or adjacent108 Q
corners are outside this theorem.
The unrestricted research target and arbitrary V/V pairs remain open.
