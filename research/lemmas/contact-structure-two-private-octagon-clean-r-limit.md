# Two private octagon slots admit a clean trivalent type-R limit

Date:2026-10-13. Status: independently reviewed VALID; [clean-limit review](../reviews/contact-structure-two-private-octagon-core-clean-limit-review.md).
This is a translated-limit existence reduction, not periodicity of the original
tiling. The two private lengths may be equal; P may be symmetric here.

## Statement

Let P have native angles90,112.5,112.5,112.5,112.5 and Q have eight135angles.
Suppose Q has exactly two side slots whose lengths occur nowhere among P
native side lengths. If {P,Q} admits an unrestricted plane tiling, it admits
an edge-to-edge trivalent plane tiling using the same fixed polygons in which
every P has native side-neighbor word Q-P-Q-P-Q, starting with an acute leg.
The fixed two-private QQ mask remains valid in the limit. Reflections are
still admitted. No forced language persistence is assumed in taking the limit.

## Uniform defect counts from native incidence

Use the reviewed [native reduction](contact-right-angle-unrestricted-native-reduction.md).
All contacts involving Q are whole sides and each Q has at most two Q-neighbor
slots. Its two private slots must be Q-neighbor slots, so every Q has exactly
two QQ sides and exactly six PQ sides. Let p,q count centroid-anchored tiles
in any square of side2R; let y count P90+2Q135 stars, z count4P90 stars,
and t count flat-host+2P90 stars by vertex position. All boundary errors below
are uniform O(R), because fixed positive tile areas and bounded diameters
bound tiles in fixed-width strips, and vertices carry native corners.

Whole QQ endpoints are precisely y stars. Thus

    y=2q+O(R).

Full native corner counting gives

    y=4q-p+O(R),    p=2q+2z+t+O(R).

Therefore p=2q+O(R) and 2z+t=O(R), uniformly in square position. In particular
the number of all flat and four-right vertices in any translated square
has a uniform linear bound. No positive-frequency assumption or infinite
mean is needed; a species is allowed to disappear in a limit.

## Clean disks and compactness

Assign angle-dependent native weights

    P112.5 ->1,    P90 ->4,    Q135 ->-2.

A tile meeting a point in a side interior contributes no native corner weight.
The complete palette stars are PPQ with twoP112.5, PQQ with oneP90,
fourP90, and flat-host with twoP90. Their respective scores are0,0,16,8.
So the positive-score vertices are exactly the linearly bounded z/t defects.
The complete PROTOTILE scores are8 for P and -16 for Q; we do NOT invoke a
lemma requiring the individual prototile scores to be zero.

For any prescribed L, put disjoint radius(L+D) disks on a separated grid
in a sufficiently large square, where D bounds tile diameters. There are
quadratically many disk candidates but only linearly many bad vertices;
each bad vertex spoils at most one disk. Some disk therefore has no positive
score. Translate its centre to zero and let L tend to infinity.
Fix a native indexing of each prototile and retain the chosen indexed
isometry on every tile occurrence, including any symmetry-resolving choice.
Fixed polygon diameters and positive areas uniformly bound tiles meeting
compact windows; their bounded translation parameters, compact orthogonal
parameters and finite native labels have convergent diagonal subsequences. Coverage and interior
nonoverlap persist, giving an admitted P/Q plane tiling T0. This is the usual
fixed-polygon placement compactness; it does not assert native vertices are
separated in the original unrestricted fields.

## Additive cluster proof prevents new bad vertices

Fix any native-corner position a in T0. Only finitely many limiting native
corner positions meet a small bounded window. Choose epsilon>0 so a is the
only one in the closed2epsilon disk around a. Work with all tiles meeting a
larger window expanded by D. For late approximants, the multiset of native
corner OCCURRENCES in the epsilon disk is exactly the multiset converging
to a; every other limiting native corner stays outside that disk. Polygon
corners remain distinct within each tile; different tiles corner occurrences
may coalesce but are all counted separately. There are no untracked tiles,
by the fixed local-count bound and the placement subsequence construction.

Group approximating corner occurrences by geometric position inside this
disk. Each group is a whole approximating native star: every corner at the
same position is inside, and a side-interior host contributes zero. All these
stars are in the growing clean disk, hence have score zero. The sum of their
weights is therefore zero. The occurrence bijection preserves every weight,
so the score of the limiting star at a is zero. This allows several zero
stars to merge; it does not assume unchanged star incidence or a finite
language closed under merging.

The only zero-score stars in the fixed angle palette are PPQ and PQQ.
Thus T0 has neither flat contacts nor four-right vertices. It is consequently
edge-to-edge and trivalent. At every P90 corner its star is PQQ, so both
acute legs have Q neighbors. Native alternation at the four obtuse corners
then gives Q-P-Q-P-Q everywhere. Every Q still has its two private lengths
and the native reduction fixes the same QQ mask in this admitted limit.
This proves the statement directly; no second S-free selection step or
unproved edge-to-edge language persistence is needed.

## Scope

This creates one cleaner admitted tiling if any tiling exists. It does not
show all tilings lack sparse defects, are type-R, or share a period. Equal
private lengths and all P side-length coincidences remain permitted. The separate common-core and anchored-completion obligations are completed in the [reviewed all-metric synthesis](contact-right-angle-two-private-all-metric-periodic-escape.md). This file proves only the clean-field reduction. No substitution,
computation, novelty claim or unrestricted two-polygon theorem is asserted.
