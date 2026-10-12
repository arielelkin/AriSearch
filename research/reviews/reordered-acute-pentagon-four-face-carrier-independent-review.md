# Fresh independent review of the reordered acute pentagon carrier

Date: 2026-10-12. Verdict: **VALID after the five-host repair**.

## Scope and independent reconstruction

Reviewed [the exact criterion](../lemmas/reordered-acute-pentagon-four-face-periodic-carrier.md)
for actual strictly convex pentagons A=(65,140.5,75,147.5,112),
B=(40,144.5,136,47,172.5): plane tileability is equivalent to
A0=B1,A2=B0,A3=B3, and these aliases supply a periodic4-face covering.
The original tiling may use rotations, reflections, arbitrary valences and
partial contacts; the proof removes T pointwise rather than through density.
Other native orders and angle inventories are outside scope.

The [fresh checker](check_reordered_acute_pentagon_independent.py) imports no
producer. It reconstructs the1flat/9full native support, treats eligible host
endpoints separately, enumerates relevant P/D seam choices and independently
reconstructs the four-face torus corner-link permutation from the edge data.
It passes all exact finite checks.

## Defect found and repair audited

The initial proof/certificate listed only A3,A4,B3 as possible flat hosts.
That assumes both host endpoints coincide with the fan's outer endpoints.
Flat-eligible beta or gamma host endpoints may instead end strictly inside
an outer native side. Independent reconstruction adds A2 and B4. The author
independently caught the same gap and saved the repaired five-case proof
and tables before this review verdict.

The repair is sound: an A2 host's non-flat x must coincide with the cap's
outer x. Both relevant segments have actual length A2, so T would equal
the host's beta endpoint, contrary to an interior flat junction. A B4
host's non-flat w must coincide with cap x, giving P. The cap x uses A2
toward w, so its remaining A3 faces the third gamma; the resulting far
y/delta or y/w pair is impossible. The B3 case has the same local P
obstruction. A4 fails by its identical-length y endpoint, and A3 forces
A3=A2+A4 but also A3=A4, contrary to positive A2. No additional host types
pass the non-flat endpoint test. Eligible-endpoint overruns are now included.

A minor original exposition sentence said every continuation use has
combined far angles above180. The B3 y/v bank has sum159. Its coincident
vertex is nevertheless full because neither y nor v belongs to any native
flat fan. This was reported for wording correction and is not an unresolved
mathematical defect.

## Pointwise T and alias necessity

Every alpha/beta internal fan seam has an unsupported pair of non-flat far
endpoints, so gamma must be the middle T sector. If beta uses A2 internally,
far x/w forces P and then the prohibited xA3/gamma continuation. Thus beta
uses A1 with outer A2, while alpha uses A0 with outer A4. The fan's far x/y
banks reduce to the complete five-host gate above. T is impossible locally.
Any vertex-on-side incidence would have native180 fan T, so all contacts
are whole-side after this exclusion. Fixed positive area and bounded
diameter guarantee local finiteness and preclude accumulating subdivisions.

Now(alpha,x,x) requires alphaA0/xA2 and alphaA4/xA3 by the exact far-star
support. The mutual x-x seam would be A3/A2, with unsupported far y/beta.
Thus every x uses P and every delta uses D. If only one tile type were
present its obligatory x or delta could not be completed; omission is
therefore already included.

At P, x/gamma is uniquely A2/B0 by complete endpoint tests. The remaining
x/w seam is A3/B3 after that incident A2 is used. At D, beta/delta is
uniquely A2/B0; beta's other A1 must meet z's A1, leaving zA0/deltaB1.
Hence precisely the three claimed actual aliases are forced. Neither
reflection nor a coincidence of additional lengths supplies a different
native angular completion.

## Positive torus and infinite conclusion

All20 directed polygon sides occur exactly once in ten reverse-boundary
pairs. Independent reconstruction gives a connected face graph and exactly
six single cyclic vertex links, with two copies each of D,P,F. Every link
has exact doubled-angle sum720. Reverse-boundary pairings preserve a global
surface orientation; F-E+V=4-10+6=0, so the quotient is an orientable torus.
Each seam either pairs equal native slots or uses one of the three aliases.
Thus it is a genuine compact flat metric surface built from the input
polygons for EVERY admitted metric satisfying those aliases.

The infinite covering conclusion is sound: its complete simply connected
flat cover is Euclidean plane. Deck isometries preserve orientation and act
freely, so nonidentity rotations, which have fixed points, are excluded.
Compactness gives a rank-two translation lattice. Lifted polygon faces cover
with disjoint interiors and deck translations preserve species and native
labels. This proves the periodic escape, rather than merely a finite patch
or corner-colour torus. It does not claim every admitted tiling is periodic.

No remaining defect found in the repaired theorem. This closes only the
specified reordered-word construction family.

Replay:

    MISE_AUTO_INSTALL=0 mise exec -- conda run --no-capture-output -n arisearch python research/reviews/check_reordered_acute_pentagon_independent.py

## Ancillary exact-coordinate nonemptiness addendum

The separate [positive-coordinate sample](../certificates/reordered-acute-pentagon-periodic-sample.json)
was independently reconstructed without its producer or helper imports. Unit
edge vectors were rebuilt directly from exp(2*pi*i/720) in QQbar, with exact
AA real/imaginary parts. The lists(0,79,289,354,490) and(0,71,159,425,440)
are doubled-degree directions; cyclic exterior turns recover exactly the
stated native A/B angles, including the first corner across direction720.

Independent two-by-two linear systems solved A0,A4 from A1=t,A2=1,A3=d,
then B2,B4 from B0=1,B1=A0,B3=d. Both determinant constants are nonzero.
Basis evaluations at(t,d)=(0,0),(1,0),(0,1) verify the published affine length
formulas identically, rather than merely at the positive fixture. At the
exact rational fixture t=1/10,d=1/5 all ten lengths are positive, both edge
sums close exactly, and all15 nonincident strict support determinants per
species are positive. The three aliases hold identically by construction.

All these quantities are continuous in(t,d); finite strict inequalities at
the fixture therefore persist in an open neighbourhood. This proves a
nonempty open normalized two-parameter metric region. With A2=1 this is a
slice of a homogeneous length cone, rather than itself a scaling-invariant
cone; the author corrected the ancillary metadata accordingly. No claim
that every positive(t,d) is admissible is needed or made. The decimal display
coordinates were not used as exact input. Periodic plane realization still
follows from the separately reviewed flat carrier, not from sample geometry
alone. This ancillary audit changes no native-word theorem premise.
