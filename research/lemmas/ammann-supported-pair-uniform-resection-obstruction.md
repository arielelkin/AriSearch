# Uniform unmarked resection closes the variable-content loophole

Date: 2026-10-13. Author: sol. Status: [fresh independent hostile review VALID](../reviews/ammann-supported-pair-uniform-resection-fresh-hostile-review.md). This excludes a source-compiler mechanism, not all
pairs of convex polygons. No novelty claim is made.

## Hypotheses and source data

Fix ANY generic parameter J in the reviewed Ammann forcing domain G*.
Let S={H6,P1,P2} be its three DISTINCT UNMARKED source congruence classes,
with reflections and unrestricted contacts admitted. The reviewed source
forcing/count results imply that EVERY admitted S-plane tiling has

    h(R)=Theta(R^2), p1(R)/h(R)->phi, p2(R)/h(R)->phi,
    phi=(1+sqrt5)/2.

See [the freshly reviewed anchored count proof](ammann-anchored-count-split-fixed-cluster-obstruction.md).
The universal exact source area identities from the reviewed vertex lists are

    area(H6)=sigma,
    area(P1)+area(P2)=phi*sigma, sigma=sin36 degrees>0.

Their direct shoelace derivation is retained in
[the area-rank artifact](ammann-area-rigidity-and-whole-tile-fusion.md).
No rational independence of all three individual areas is assumed here.

A macro support M is WHOLE-SOURCE-SUPPORTED if some finite patch of whole
S tiles, with pairwise disjoint interiors, has union exactly M. The pieces
may be reflected and have arbitrary contacts. Different such dissections
of congruent supports are initially allowed to have different integer content
vectors. No recognition, global partition, unique dissection or boundary
marking is assumed in this definition.

## Theorem

Suppose M,N are two fixed compact positive-area macro supports, each
whole-source-supported, and some unmarked {M,N}-tiling of the plane exists
under unrestricted isometries/contacts. Then:

1. Every whole-source dissection of EITHER support has equal P1/P2 counts.
2. Each support has ONE content vector across ALL its whole-source dissections,
   even if their spatial arrangements differ.
3. The two content vectors are rationally independent and their nonnegative
   cone contains the limiting source direction(1,phi,phi).

Consequently no such tileable pair can contain a support congruent to source
P1 or P2. In particular allowing a same-shaped second macro to have different
source contents cannot repair a singleton-pentagon fusion at ANY G* parameter.
The macro supports need not be convex for this necessary obstruction.

## Proof: choose a section, not a recognizer

Choose ANY one finite whole-source dissection C of M and ANY one D of N,
with integer content vectors u,v. Given an existing macro tiling, choose an
isometry taking M or N onto every corresponding occurrence and insert its
image of C or D. Every inserted patch lies within and covers its macro support.
Different macro interiors are disjoint, so all inserted source tile interiors
are disjoint and their union covers the plane. Every piece is an admitted
S isometric copy, including reflections. Partial contacts across macro
boundaries are ADMITTED by S; no source decoration or matching rule remains
that could reject this resection. Therefore this is an actual S-plane tiling.

The source forcing theorem applies to this NEW tiling, not merely the source
tilings from which a proposed compiler was first obtained. It may force the
resection to be edge-to-edge; that is a conclusion, not an extra hypothesis
or a reason to reject the resection as geometrically invalid. Exact supports
and interior-disjointness already prove it is an admitted unmarked tiling.
The macro tiling need not be periodic. There is no period-orbit choice here:
each occurrence simply receives the chosen fixed patch through its isometry.

Let m(R),n(R) count macro anchors. Bounded diameters and finite fixed patches
give source counts

    c(R)=(h(R),p1(R),p2(R))=u*m(R)+v*n(R)+O(R).

Indeed corresponding anchors have bounded displacement; only a fixed-width
boundary annulus contributes an error. Fixed positive macro/source areas
bound all such annular tile counts byO(R). No macro densities or assumption
that both types occur with positive frequency is needed.

Take ANY rational row vector a annihilating both u and v. Since two vectors
inQ^3 have a nonzero annihilator, the space has dimension at least1. Divide
its identity a*c(R)=O(R) by h(R)=Theta(R^2) and use the universal source ratios:

    aH+phi*(a1+a2)=0.

Irrationality ofphi gives aH=0,a1+a2=0. Every rational annihilator therefore
lies in the one-dimensional span of(0,1,-1). Its dimension is exactly1, hence
u,v have rank2 and both satisfy u1=u2,v1=v2. The chosen dissections C,D were
ARBITRARY. Fixing one dissection of the other support and varying the first
shows that EVERY possible whole-source dissection of each shape is balanced.

Write any balanced content as(l,k,k). Its area is sigma*(l+phi*k) by the
universal source area identities. If two dissections support congruent M,
area equality yields(l-l')+phi*(k-k')=0. The coefficients are integers, so
irrationality forces l=l',k=k'. Thus all contents coincide, proving2.
No unique spatial dissection is inferred.

The rank2 assertion already proves the first part of3. Since c(R)/h(R)
converges to(1,phi,phi), its leading linear expression lies in the closed
nonnegative cone generated by u,v: dividing m,n by h gives nonnegative
bounded coefficients, because each fixed macro has positive area and m+n
isO(R^2). A subsequence supplies limits; boundary error vanishes. Hence the
source direction belongs to that cone. This is necessary, not sufficient
for a geometric or global construction.

Finally sourceP1 itself is a legal singleton dissection with content(0,1,0),
and P2 has(0,0,1). Both are unbalanced. If a macro shape were congruent to one
of them, it would admit that same singleton dissection through its placing
isometry, contradicting1. This proves the exclusion. QED.

## Scope and restart consequence

This theorem does not need an original source tiling already partitioned
into ONE particular patch type. Any alleged macro tiling plus one exact
source dissection for each support suffices to create the new source tiling.
It therefore closes an apparent variable-content loophole that would be real
for a DECORATED source whose patches might not match across macro boundaries,
or for a source with placement restrictions. It is closed here precisely
because the reviewed S source is unmarked with all isometries and contacts
admitted and the frequency theorem holds for EVERY such source tiling.

It does not exclude two NONTRIVIAL BALANCED macro supports, nor cuts or
fractional source-tile transfers, another source parameter outside G*, or a
source lacking this universal ratio. Two balanced content vectors and a cone
containing(1,phi,phi) still do not supply convexity, congruence, a global partition
or universal target forcing. Those remain separate construction obligations.
At rational area-rank2 parameters, different equal-area integer contents may
exist algebraically, but a tileable two-macro pair cannot use a support with
an unbalanced alternate dissection. Same support versus same abstract source
patch must be distinguished in applying these conclusions.

The [basic fusion theorem](convex-cluster-fusion.md) already uses the analogous
unmarked resection to lift a hypothetical target period. Here uniform content
is imposed on an arbitrary existing macro tiling to exploit source counts;
no periodicity assumption is used. Source recognizability is unnecessary.
No search, solver or numerical computation enters this analytic argument.
The fresh hostile review checks resection under unrestricted source contacts,
universal source frequencies and the arbitrary-dissection quantifier; no
consequential gap was found.
