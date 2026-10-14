# Open six-pentagon diagram recovered; exact symmetry specialization

Date: 2026-10-13. Status: new inspectable incidence data, internally checked
exact fixture, conditional macro-content lemma, and a failed symmetry collapse.
No original-source forcing theorem or final two-tile construction is claimed.

## Primary / authored sources actually inspected

1. Liam Watson, UBC Math308, Fall2021, Assignment6, problem3, page1:
   https://personal.math.ubc.ca/~liam/Courses/2021/Math308/files/Assignment_6.pdf
   Course authorship and date: https://personal.math.ubc.ca/~liam/Courses/2021/Math308/
   The openly accessible exercise displays a recomposition of Penrose rhombs
   into six convex nonregular pentagons. The image was downloaded to /tmp and
   rendered with Poppler; no source scan is copied into this repository.
   It supplies the incidence diagram, not explicit parameter values, matching
   arrows, or a worked proof. It is an authored teaching source, not the original
   Danzer/Grunbaum--Shephard publication. We do not identify attribution beyond
   the diagram's explicit six-piece Penrose-rhomb exercise.
2. Teruhisa Sugimoto, Convex pentagonal monotiles in the15 Type families,
   arXiv2501.07090v2, dated29Jan2026 in inspected HTML:
   https://arxiv.org/html/2501.07090
   Figure1 and Section1 describe a periodic translation unit for every Type2
   polygon, permitting reflections. Type2 is A+B+D=360 degrees, a=d;
   the extra c=e in Section2 is for the additional edge-to-edge specialization.
3. Grunbaum--Shephard book public searchable fragments were refreshed using
   https://be-api.us.archive.org/fts/v1/search and identifier:isbn_0716711931.
   These still give no exact parameter values. No restricted files were fetched.
4. Dzuklevski2507.20867v1 Section3.2 was inspected again:
   https://arxiv.org/html/2507.20867v1
   It is provenance for the classical convex sources, not this fixture's decoder.

## Recovered incidence data, without measuring pixels

Write a thick rhomb's consecutive counterclockwise vertices V0,V1,V2,V3.
Replace each old side Vi Vi+1 by two straight segments through Ki. The diagram
has outward kinks K0,K1 and inward kinks K2,K3. Its two additional boundary
cutpoints are S0 on K0 V1 and S1 on V1 K1. The two interior trivalent vertices
are X,Y. The four pentagons have these exact incidence cycles:

    (V0,K0,S0,X,K3), (S0,V1,S1,Y,X),
    (S1,K1,V2,K2,Y), (K2,V3,K3,X,Y).

In particular, the cuts DO NOT end at both outward kinks. Confusing the
cutpoints with those kinks gives quadrilaterals and loses the real construction.

For the thin rhomb W0..W3, outward kinks L0,L2 and inward kinks L1,L3 occur.
The interior seam joins L1 to L3, giving two pentagons:

    (W0,L0,W1,L1,L3), (L3,L1,W2,L2,W3).

Thus there are four native faces per modified thick rhomb and two per modified
thin rhomb. This is not a literal subdivision of the straight rhombs: some
pieces cross their original boundary. Matching modified profiles consistently
with Penrose edge arrows is a necessary additional source obligation.

## Exact internally chosen realization

The replay script research/searches/current-exact-convex-source-six-profile.py
sets eps=1/100, uses exact cos/sin36 and18 degrees in Sage AA, and chooses
midpoint kink locations. The left normal displacement is -eps at outward
kinks and +eps at inward kinks. Thick cutpoints S0,S1 are midpoints of their
stated subedges. With u=(cos36,-sin36), v=(cos36,sin36), take

    X=(7/20)(u+v), Y=(13/20)(u+v).

The script checks all strict supporting halfplane inequalities for all six
pentagons, pairwise interior disjointness by exact clipping, and exact sums of
their areas against the modified parent areas.
Its finite domain is ONE stated exact profile, six cycles; no parameter or
patch search is claimed. It finds three thick congruence classes and one thin
class, hence four classes total. Full cyclic pairwise distance signatures
include reflection identifications. The literal algebraic data live in the
script. This is our own exact geometric realization of the diagram incidence,
not a claim that these are the book's generic forcing parameters.

## Specific symmetry-collapse obstruction

The opposite midpoint thin profiles make the two thin faces congruent. Let
P=(W0,L0,W1,L1,L3) and let A0..E0 denote its consecutive interior angles.
At the two old vertices W0,W1 the angles A0 and C0 are supplementary.
Indeed, the profile tilt delta=arctan(2eps) rotates the two incident
rays at each old corner by the SAME signed angle; the old corner angles
remain36 and144 degrees. Their sum is180.
Equivalently, the script checks cos(A0)=-cos(C0), sin(A0)=sin(C0) exactly.
The four sides inherited from kinked source edges all have squared length
1/4+eps^2. Only the new seam may have a different length.

Relabel the consecutive vertices as (D0,E0,A0,B0,C0). Then the new angles
satisfy A+B+D=D0+E0+B0=360 degrees. Under the source convention
a=EA,b=AB,c=BC,d=CD,e=DE, all a,c,d,e are equal profile sides; only b
is the new seam. Thus a=d establishes Type2, and c=e also holds. Sugimoto's primary representative
Type2 translation unit gives a periodic tiling by P alone, with reflections
allowed. Therefore ANY proposed protoset containing this exact thin face
fails the target's aperiodicity gate, irrespective of how many other classes
can subsequently be identified. The source-plane compatibility and decoder
are unnecessary for this falsification: the periodic monohedral escape uses
only the final shape. This narrow midpoint symmetry specialization is killed;
generic asymmetric thin profiles and changed seams remain open.

The explicit classification-independent four-P lattice carrier is now retained
at research/searches/current-exact-convex-source-thin-four-motif.md. Its
checkerboard profile identities and positive fan determinants replay in the same
Sage producer. A proper PL deformation proves allplane coverage and nonoverlap;
area equality is only a supplementary check. Independent hostile review of the
Type2 identification and carrier is VALID in
research/reviews/current-exact-convex-source-six-hostile-review.md. No numerical angle equality or
finite absence of witnesses is used as proof.

## Conditional two-macro content constraint

Assume a genuine Penrose-compatible source realizes six distinct faces with
these incidences, with universally decoded count ratio thick/thin=phi. Its
normalized six-component source count vector is proportional to

    f=(phi,phi,phi,phi,1,1).

This is a conditional calculation from native face counts, not a frequency
claim for arbitrary tilings of the unverified six shapes. Its coordinate Q-rank
is2; the earlier possible rank>=3 gate DOES NOT exclude this source.

If this source plane is grouped into two kinds of bounded whole-source macro
patches with fixed integer content vectors u,v, conservation gives
f=lambda*u+mu*v with nonnegative real coefficients. Both coefficients are
positive and lambda/mu irrational: a zero coefficient or rational ratio would
make all coordinates of f rational multiples of one number, contradicting
phi irrational. Subtracting any two of the first four coordinate equations
therefore forces ui=uj and vi=vj. Subtracting the last two forces u5=u6 and
v5=v6. Thus each macro has content

    u=(m,m,m,m,n,n), v=(p,p,p,p,q,q),

for nonnegative integers m,n,p,q. Conversely these algebraic conditions alone
say nothing about possible convex patch geometry or its global partition.
This is stronger than simply observing rank2, but remains conditional on the
original distinct-source decoder and frequencies. It must not be applied to
the four-class periodic symmetry fixture just killed above.

## Retained search boundary

Queries in this round (web index unless endpoint stated):
- Danzer nine convex pentagons
- Tilings and Patterns10.3.29 pdf
- six convex pentagons
- Grunbaum Shephard aperiodic pentagons Danzer Penrose recomposition
- A convex sigma-morphic protoset
- Tilings and Patterns pdf Grunbaum Shephard1987
- Danzer pentagons aperiodic convex source
- convex aperiodic recomposition six pentagons geometry
- Grunbaum six convex aperiodic
- convex pentagon type2 tiling A B D360 c e
- Convex pentagonal monotiles in the15 Type families Sugimoto arxiv
- FTS: lines of subdivision, nine convex, Show that the recomposition,
  each AND identifier:isbn_0716711931.
Google Books SearchWithinVolume2 for id0x0vDAAAQBAJ, q=pentagons returned0
results. The public page549 URL was not accessible through the web reader.

## Exact restart obligations

Recover two-colored/oriented Penrose profile identifications for the recovered
six-piece incidence diagram, then derive rational/algebraic genericity choices
and prove unrestricted intrinsic assembly. For a symmetry collapse, avoid the
midpoint thin Type2 locus above BEFORE solving thick-class equalities. For
whole-source regrouping, use balanced integer contents (m,m,m,m,n,n) only
once genuine source decoding is proved. Cross-boundary cuts can evade this
integer-content restriction and require their own mass/forcing invariants.
No final pair, plane-wide partition, or decoder is supplied here.
