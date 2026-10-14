# Symmetric pentagon / exactly two-private octagon: all-metric periodic escape

Date:2026-10-13. Status: independently reviewed VALID synthesis; [full audit](../reviews/contact-symmetric-two-private-all-metric-synthesis-review.md) and [independent carrier audit](../reviews/contact-symmetric-two-private-symbolic-carrier-hostile-review.md).

## Statement and native reduction

Let P be a genuine compact convex pentagon with one90 and four112.5 corners,
and equal lengths a>0 on its two sides incident to the90 corner. Let Q be a
genuine compact convex octagon with eight135 corners and EXACTLY TWO native
side slots whose lengths are absent from all five P native side lengths.
If the original pair admits any unrestricted plane tiling, it admits a
rank-two periodic plane tiling of the same two shapes. Reflections, partial
contacts, other length aliases and omission of species are allowed. This
asserts existence of SOME periodic escape, not periodicity of every filling.

Use the reviewed unrestricted native reduction
research/lemmas/contact-right-angle-unrestricted-native-reduction.md.
Its statements do not require unequal acute lengths: Q contacts are whole;
Q has at most two QQ slots separated by distance3 or4; private slots must
be QQ; each P has typeR word Q-P-Q-P-Q starting at an acute leg, or typeS
word P-Q-P-Q-P. The flat-host exception is confined to PP contacts.
Pentagon vector closure for lengths(x,a,a,y,w) gives x=y and

    w=sqrt2*a-2sin(pi/8)*x, hence0<w<sqrt2*a.

No P-only or Q-only tiling exists in this palette: a native P112.5 or Q135
corner cannot be completed using that single species, even allowing a flat
host. Thus an existing plane tiling genuinely contains Q. Privacy attains
the two-QQ maximum, fixing its mask to0,3 or0,4 up to dihedral indexing.

## Clean typeR limit remains valid with symmetry

Here is why the already reviewed clean-limit construction applies without
an unequal-length assumption. Count centroid-anchored tiles p,q and native
stars y=P90+2Q135,z=4P90,t=flat+2P90 in translated squares of side2R.
All errors are uniform O(R), by positive areas and bounded diameters.
Whole QQ endpoints and the native angle ledger give

    y=2q+O(R), y=4q-p+O(R), p=2q+2z+t+O(R).

Consequently2z+t=O(R). Assign native weights P112.5=1,P90=4,Q135=-2.
The palette's full stars PPQ,PQQ,fourP90,flat+twoP90 have scores0,0,16,8.
Separated disks in sufficiently large windows therefore include arbitrarily
large disks without positive-score stars. Translate these disks to0 and
extract a fixed-polygon indexed placement limit. Positive areas bound local
tile counts, translations are bounded locally, and orthogonal placements
are compact; coverage and interior nonoverlap persist.

At any limiting native vertex, isolate its finitely many corner occurrences
in a small disk. In late approximants exactly those occurrences lie in the
disk, grouped into whole clean stars. Their total score is0 and preserved
under convergence, including coalescence of several stars. Thus the limit
has only zero-score PPQ/PQQ vertices: it is edge-to-edge and trivalent.
Every P90 star is PQQ, so all P are typeR. Privacy/native reduction fixes the
same two QQ slots. This does not assume per-prototile score zero (Pscore8,
Qscore-16) or finite-language persistence. The complete reviewed proof is
research/lemmas/contact-structure-two-private-octagon-clean-r-limit.md.

## Closure exhausts the two mask geometries

In the clean field every public Q side next to a QQ endpoint matches a P
acute leg and therefore has length a. Public sides with neither endpoint
at QQ match the typeR middle side w. Numeric aliases do not change these
indexed endpoint facts. Hence the only two native words are

    mask3: (H0,a,a,H3,a,w,w,a),
    mask4: (H0,a,w,a,H4,a,w,a).

Rotate the eight equiangular Q vectors to directions0,45,...315. In mask3,
vertical closure gives H3=(1+sqrt2)w-sqrt2*a, and horizontal closure gives
H0=H3. In mask4 the four opposite public vectors cancel, leaving H0-H4=0.
Thus DISTINCT private lengths are untileable, including symmetric P. Equal
private lengths reduce to the following explicit positive carriers. No
classification of allowed QQ attachments or finite QQ cycles is needed.

## Mask3: an explicit two-Q / four-P cell

Put r=sqrt2 and H=(1+r)w-ra. Private positivity and P positivity are exactly

    (2-r)a<w<ra.

For every point in this open domain, the explicit carrier in
research/lemmas/contact-symmetric-two-private-distance-three-periodic-carrier.md
uses P vertices

    (0,-w),(b,-w/2-a/r),(b+a/r,-w/2),(b,-w/2+a/r),(0,0),
    b=((2+r)a-(1+r)w)/2,

and Q obtained by integrating word(H,a,a,H,a,w,w,a). With rotations Rminus
by-45 and Rplus by135, six representatives are

    Q, Q0+Q1-Q, Q1-(P-P2), Q3+Rplus(P-P2),
    Q4+Rminus(P-P2), P-P2.

Their lattice vectors are

    V=(a+rw/2,(r+1)a+(r/2+1)w),
    U=(-(r/2+1)a-(r/2+1/2)w,ra/2+w/2).

The retained exact polynomial certificate
research/searches/contact-symmetric-two-private-symbolic-carrier.py verifies
18 reversed-edge pairs covering all36 native edges, all72 endpoint coordinate
identities in Q(sqrt2)[a,w], the exact rotation and native-angle identities,
and

    4area(P)+2area(Q)=det(V,U)=2(1+r)(a+rw/2)^2>0.

All side lengths are positive with ordered native directions, so the polygons
are strictly convex. The locally finite periodic multiplicity has zero
distributional gradient by the complete oriented-edge cancellation. Its mean
is area/covolume1, so multiplicity is1 almost everywhere. Interior overlaps
and open gaps are impossible; the union is closed by local finiteness, hence
covers every point. This proves actual legal entire-plane periodic existence,
without assuming the original field shares any contact structure.

## Mask4: the positive symmetric channel carrier

Here H>0 is arbitrary. Set

    b=w/2, s=a/r, tau=r-1, g=(s-b)/tau>0,
    c=H/2>0, A=c+s, d=b+s, W=2A+g.

Use channel pentagon vertices

    (0,-b),(g,-s),(g+s,0),(g,s),(0,b),

and octagon cyclic vertices

    (A,-b),(A,b),(c,d),(-c,d),(-A,b),(-A,-b),(-c,-d),(c,-d).

Their native words match the original P and Q: P has acute legs r*s=a,
seam2b=w, equal remaining legs x; Q has word(H,a,w,a,H,a,w,a) up todihedral
indexing. Ordered angles and lengths determine each original shape up to
an allowed isometry. Place Q at0, channel P at(A,0), and its reflection
across a vertical line translated to(A+g,d), repeating by lattice(W,d),(0,2d).

For completeness the channel's seam partition is explicit. For0<=y<=d,
the neighboring octagon banks are L=A fory<=b and L=A+b-y otherwise,
and R=A+g+s-y fory<=s and R=A+g otherwise. The first P occupies[A,R]
for0<=y<=b and[A+(y-b)/tau,R] for b<=y<=s. The reflected P occupies
[L,A+(y-b)/tau] for b<=y<=s and[L,A+g] for s<=y<=d. These adjacent closed
intervals partition the complete gap between the banks, with disjoint open
intervals. Reflection in y and repetition by2d cover the remaining heights;
neighbor columns differ by(W,d). The octagon columns plus these seam
intervals therefore cover the plane with disjoint interiors. Every polygon
is genuinely convex with positive native edges. This is the existing exact
channel proof at
research/lemmas/contact-structure-right-pentagon-octagon-periodic-carrier.md,
reviewed at
research/reviews/current-exact-convex-source-right-carrier-hostile-review.md.

Both masks thus supply rank-two periodic admitted tilings of the original
pair. No metric sweep, forced matching rule or unproved periodicity of P-only
fields occurs. Together with the independently reviewed nonsymmetric theorem,
this excludes every right-pentagon/equiangular-octagon pair having exactly two
private Q slots. Zero/one-private partners and other palettes lie outside this theorem; the separate [one-private all-distinct classification](contact-right-angle-one-private-all-distinct-periodic-escape.md) and [generic zero-private synthesis](contact-right-angle-no-qq-generic-zero-private-reduction.md) cover their stated subfamilies.
