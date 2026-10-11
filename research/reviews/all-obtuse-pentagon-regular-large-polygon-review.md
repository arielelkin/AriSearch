# Fresh hostile review: regular n-gons with n>=13 and all-obtuse pentagons

**Verdict: VALID without repair.** Every fixed genuine convex pentagon with
strictly obtuse native angles is excluded as a partner of the regular n-gon
for every integer n>=13. The proof permits arbitrary pentagon lengths,
all rotations and reflections, partial contacts in the original definition,
and omission of either tile type. No numerical experiment or implementation
of the analytic counting proof was used.

Reviewed [the large-n obstruction](../lemmas/all-obtuse-pentagon-regular-large-polygon-obstruction.md),
the independently reviewed [all-obtuse forcing theorem](../lemmas/obtuse-edge-forcing.md),
and the full translated-limit procedure in
[the heptagon classification](../lemmas/all-obtuse-pentagon-regular-heptagon-classification.md)
and its fresh review. This reviewer did not develop the large-n proof or
either author's n=14 local gate. No monohedral classifier or finite angle
alphabet is needed.

## Quantifiers and uniform counting

Fix n and a hypothetical shape P and tiling. The proof constants may depend
on these fixed shapes and n; the theorem does not require them to be uniform
over all pentagon metrics or over unbounded n. They must be uniform over
translations of the observation window, and they are.

Both prototiles have fixed positive minimum area and bounded diameter D.
Tiles whose centroids lie in a square lie in its D-enlargement, and tiles
crossing its boundary lie in a fixed-width boundary enlargement. Disjoint
positive-area interiors bound the boundary population by O(R). Coverage of
the D-shrunken square and the fixed maximum tile area give the quadratic
lower bound, while the minimum area gives the upper bound. Thus total
centroid counts are uniformly Theta(R^2). Every tile supplies at most a
fixed finite number of sides and corners, so the stated changes of counting
convention cost uniformly O(R).

The forcing dependency applies: regular n>=13 has strictly obtuse angles,
as does P. It turns the original unrestricted hypothetical tiling into
full native-side contacts with trivalence. Let V count full vertex stars.
The independent count elimination is

    3V=5N_P+nN_Q+O(R),
    2V=3N_P+(n-2)N_Q+O(R),
    N_P=(n-6)N_Q+O(R).

Combined with quadratic total population, this gives uniform positive
quadratic bounds for both types. Therefore omission and zero-density use
of a type do not escape the argument. No convergence of frequencies or
replacement of an O(R) residual by a pointwise statement occurs.

## Four small corners, one high corner and the exact defects

Two Q corners at a star would require P angle4pi/n<=pi/2, and three Q
corners cannot sum to2pi. Thus all Q vertices are Q,P,P and every Q side
meets P. At a Q,P,P vertex each P angle is strictly less than
H=pi/2+2pi/n<2pi/3. Adjacent P sides cannot both meet Q because their
shared vertex would then have two Q sectors. The independent-set bound
on the five-side cycle gives at most two Q sides per P, necessarily
nonadjacent. These statements count sides rather than merely tile types
at a point. A convex pair with disjoint interiors also cannot share two
noncollinear positive side contacts.

If every P had at most one Q side, side counts would imply
nN_Q<=N_P+O(R), contradicting N_P=(n-6)N_Q+O(R). Hence some P has
two nonadjacent Q sides; their four distinct endpoints show that four
native angles of the fixed prototile are below H. This argument needs
only one such copy, not an assumption that every P attains two contacts.

Counting P sectors at PPP stars gives

    5N_P=2nN_Q+3Z+O(R), Z=(n-10)N_Q+O(R).

There are quadratically many PPP stars, and each needs an angle at least
2pi/3. The prototile therefore has exactly one high native angle beta>=2pi/3;
the other four are below H. This remains true when any of those four values
coincide. A beta incidence cannot be QPP because beta>H.

If beta=2pi/3, every PPP star has three beta sectors; inserting even one
small sector would lower the sum below2pi. Then N_P=3Z+O(R), forcing n=12.
Thus beta>2pi/3 for the present n>=13 domain. Every PPP star consequently
has one or two beta sectors. For their actual counts Y and X,

    2X+Y=N_P+O(R), X+Y=Z,
    X=4N_Q+O(R), Y=(n-14)N_Q+O(R).

These are nonnegative star counts. They are not signed defects that could
cancel one another. X is quadratically positive, so an actual two-beta star
exists. Its third angle is strictly greater thanpi/2, forcing beta<3pi/4.

## n=13 and n>=16

For n=13, Y=-N_Q+O(R) is incompatible with Y>=0 and quadratic N_Q.
For n>=16, an actual one-beta star exists because Y is quadratically
positive. Its other two angles are each below H, giving

    beta>2pi-2H=pi-4pi/n>=3pi/4,

in contradiction with beta<3pi/4. At n=16 the lower inequality remains
strict, so equality at135 degrees is not an exceptional case. Arbitrary
small-angle values and repetitions are already included.

## n=15 and arbitrary native multiplicities

Here H=19pi/30, S=17pi/15, and
11pi/15<beta<3pi/4. Define alpha=2pi-2beta. Actual two-beta stars make
alpha a native angle, with pi/2<alpha<8pi/15. It cannot enter a one-beta
star: even alpha plus the largest allowed other small angle is below
7pi/6, while that star's two-small-angle sum is greater than5pi/4.
Thus PPP alpha incidences are exactly X, one per two-beta star, regardless
of alpha's multiplicity on the native pentagon.

The complementary value alpha'=S-alpha is distinct from alpha because
alpha<S/2. In fact alpha' lies strictly between3pi/5 and H, so it is
strictly obtuse, below beta, and cannot appear in a two-beta star. It is
not necessary to assume alpha' is native: m', its native multiplicity,
is allowed to be zero. Its PPP incidences B' therefore satisfy
0<=B'<=2Y=2N_Q+O(R).

At QPP stars, every alpha sector pairs with exactly one alpha' sector
and conversely. No same-value pairing is hidden because alpha!=alpha'.
With m and m' the fixed integer native multiplicities, the two available
QPP incidence counts are

    mN_P-X+O(R), m'N_P-B'+O(R).

Their equality gives
B'=(9(m'-m)+4)N_Q+O(R). No integer difference m'-m puts9(m'-m)+4
in[0,2]. This contradicts the bounds on B', since boundary errors cannot
absorb the quadratic gap. In particular m'=0 is included and does not
need a separate assumed partner angle. Reflections and native cyclic
orders do not affect any multiplicity count.

## n=14: an admitted defect-free limit

Here Y=O(R) uniformly, but one-beta stars need not be absent from the
original tiling. Mark a P tile bad if it touches such a star. A bad centroid
in a window is charged to one of the three P incidences of a one-beta
star in a D-enlargement, so bad-centroid counts are uniformly O(R).

For each fixed H, if every radius-H disk contained a bad centroid, their
radius-H disks would cover a large square. Only O(R+H) such centroids lie
in its H-enlargement, so the covering area would be at most O((R+H)H^2),
less than the square's quadratic area for sufficiently large R. Thus there
are bad-free disks of arbitrarily large fixed radii. H is fixed during
that comparison and is then sent to infinity; no unproved uniform estimate
with H proportional to R is used.

Translate those centers to the origin. Fixed positive areas and bounded
diameters bound the number of tile placements in each bounded region.
Their positions and O(2) matrices have compact subsequences, including both
orientation components. Diagonal extraction produces a locally finite
collection of closed limit polygons. A tile covering any fixed point has
centroid within D, so a convergent covering placement remains available.
Interior overlaps or two distinct copies collapsing into the same positive
area tile would give an open overlap in the approximating tilings. Thus
the limit is an admitted plane tiling using the same fixed shapes. It does
not require a finite orientation alphabet.

The reviewed star-persistence hypothesis really holds here. Choose r below
the minimum native-vertex distance to every other vertex and nonincident
side of the two fixed shapes. At each original vertex its three corner
wedges cover the radius-r disk. Another vertex cannot enter a wedge
interior, and cannot lie on a wedge ray without subdividing a full native
side. Distinct vertex positions are therefore uniformly separated. For a
selected limit tile, extract its finitely many whole-side neighbors and
corner tiles as well, retaining their finite type/native-index labels.
Shared endpoints and sides persist; fixed positive lengths prevent collapse,
and the three retained angles still exhaust2pi. Stars cannot merge or
change their number of beta incidences through vertex coalescence.

Every relevant tile centroid in a fixed neighborhood lies inside the
growing good disk once its radius exceeds that neighborhood plus the
fixed diameter margin. Consequently the limit has no one-beta PPP star.
The forcing theorem independently applies to this admitted limit, and
the window identities may be reapplied to it. No property of the limiting
placement is illicitly imposed on the original tiling.

## n=14: the complete native cyclic/contact gate

All limit PPP stars are(beta,beta,alpha), with
alpha=2pi-2beta and exactly one native beta corner on each P. At a P beta
vertex, its beta neighbor shares one of its two full incident sides.
At the other endpoint of this beta--beta side, both contacting tiles have
already used their sole beta corner. They contribute two small sectors,
so that endpoint cannot be PPP, which requires two beta sectors. It is
QPP. The other side of each contacting P at that endpoint therefore meets
Q. This proves that every P has at least one Q side; a zero-Q P cannot
escape by putting all its beta contacts elsewhere.

A QPP corner on P is incident to a Q side, since all three sectors at a
trivalent vertex are pairwise adjacent. Conversely every P--Q side endpoint
is QPP. Therefore a P with exactly one Q side has exactly two QPP vertices,
the adjacent endpoints of that side. The remaining three vertices form
a consecutive PPP chain. They are its sole beta and two alpha corners.
There are exactly two possibilities up to reversing the chain:

* Beta is at an end. The two alpha corners are adjacent. Their whole P--P
  side neighbor must contribute beta at both endpoints, because each alpha
  lies in a(beta,beta,alpha) star. A genuine neighboring P with one beta
  native corner cannot do this at two distinct side endpoints.
* Beta is in the middle. Both beta-incident sides end at PPP alpha vertices.
  Its required beta--beta contact is one of those sides, contradicting the
  preceding fact that every such side has a QPP second endpoint.

These exhaust the native cyclic positions and include reflected copies.
No P has exactly one Q side. Combined with the general at-most-two bound,
every P in the admitted limit has exactly two. The full-side double count
then gives14N_Q=2N_P+O(R), while trivalence givesN_P=8N_Q+O(R).
The resulting2N_Q=O(R) contradicts quadratic N_Q. The defect-free limit
is impossible, and therefore the hypothetical original tiling is impossible.

## Scope

The analytic obstruction excludes precisely all n>=13 in the stated
strictly obtuse/regular family. It includes arbitrary positive side lengths
on P and all native angle multiplicities; no Rao classification is used.
The reviewed all-obtuse forcing closes the original partial-contact loophole,
and compact O(2) extraction covers all reflections and continuous orientations.
The proof says nothing about a pentagon with a right or acute corner or a
nonregular higher polygon. The other regular-n classifications and their
periodic witnesses retain their own review obligations. No priority or
novelty claim is audited or asserted. The unrestricted main problem remains
unresolved.

## Explicit follow-up audit of the standalone extracts

After the main review, the reviewer also explicitly read and audited
[the standalone two-beta neighbor lemma](../lemmas/pentagon-two-beta-star-neighbour-obstruction.md)
and [the direct tridecagon proof](../lemmas/obtuse-pentagon-regular-tridecagon-obstruction.md).
**Both are VALID without repair.** This addendum records that separate
inspection; it does not retrospectively claim those texts were part of
the initial source list.

The neighbor lemma uses only its stated full-edge/trivalent two-type
star hypotheses. Its zero/one-Q exclusions and exhaustive beta-middle
or beta-end path cases are exactly the locally audited argument above.
Its n=14 application keeps the linear one-beta count separate from the
admitted good-limit conclusion and then applies the local lemma to that
limit. No regularity or metric condition is silently added to the local
statement.

The direct n=13 proof has a different valid route to the unique high corner.
Call a native angle high when it is at least H=17pi/26. Such sectors are
excluded from QPP stars by the strict fellow-P obtuseness. The actual PPP
capacity gives kN_P<=3Z+O(R), with N_P=7N_Q+O(R) and Z=3N_Q+O(R), so
the fixed integer k is at most1. Positive Z supplies an angle at least
2pi/3>H, hence k=1. The equality case theta=2pi/3 would require
N_P=3Z, which has coefficients7 and9; theta>2pi/3 limits each PPP star
to at most two high sectors, giving coefficients7<=6 instead. Both are
quadratic contradictions. All boundary discrepancies remain uniform,
and no limiting tiling or angle-multiplicity assumption is needed.
The stated equiangular13-gon extension is also valid: the proof uses Q's
common angle and strict obtuseness, not equal side lengths.
