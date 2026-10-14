# Right-angle pentagon / octagon construction mechanism: working source

Date: 2026-10-13. Historical analytic source note; later exact witnesses and family reviews are linked below.
The [exact regular-octagon carrier](../lemmas/contact-structure-right-pentagon-octagon-periodic-carrier.md)
is the retained rigorous witness, independently reviewed VALID together with the positive b,g,c family in the [family review](../reviews/current-exact-convex-source-right-carrier-hostile-review.md).

## Angle palette and obligatory checks

P=(90,112.5,112.5,112.5,112.5), Q=(135 repeated eight times).
The integer star equation is 4a+5b+6c=16 in units pi/8; its nonnegative
solutions are (4,0,0),(0,2,1),(1,0,2). The flat equation with right-hand
side 8 has only (2,0,0). Native-angle species hence force only PPPP-right,
PPQ-obtuse, PQQ-right, and flat/right/right stars. No edge-to-edge assumption
is justified universally. If x,y,z,t count these star species, corner balance
is x=2p, y=4q-p, p=y+4z+2t, and p=2q+2z+t. These are necessary ledgers,
not sufficient extension conditions. In particular 2<=p/q<=4 along positive
frequency limits. The exact source uses z=t=0 and p/q=2.

## Explicit symmetric source generalization (independently reviewed)

Let t0=sqrt(2)-1 and choose b,g,c>0. Set s=b+t0*g,
a=c+s, d=b+s, W=2a+g. Define Q in cyclic order by

    (a,b),(c,d),(-c,d),(-a,b),(-a,-b),(-c,-d),(c,-d),(a,-b),

and P by (0,-b),(g,-s),(g+s,0),(g,s),(0,b).
Q has eight 135 angles; P has four 112.5 angles and one 90 angle.
The regular-octagon channel proof formally extends with column lattice
(W,d),(0,2d), P shift(a,0), reflected-P shift(a+g,d). The seams from
(a,plus/minus b) to (a+g,plus/minus s) have slopes plus/minus t0.
The bank tip between them is (W-c,0)=(a+g+s,0), giving the stated P.
The reflected band tip is (c,d), as required. All positive parameters produce
convex shapes; the seam bands remain vertically ordered since d=b+s.
The linked family review proves a periodic escape throughout this positive
parameter family by exact horizontal-slice coverage. The regular instance
b=g=c=1 is fully extracted in the lemma.

## Next mechanism

A prospective shape-only construction must break the symmetric channel
architecture while retaining proved infinite existence. Cheap first attack:
choose a nonsymmetric P in this fixed angle palette and an asymmetric
135-degree octagon, then seek a periodic channel or small exact lattice motif
before any claimed global forcing. Neither a finite legal patch nor absence
of a bounded periodic motif settles the target. Right-angle T contacts are
still permitted and must be audited separately. No promising aperiodic
metric pair is asserted here.

## Native nonsymmetric metric parametrization (working analytic note)

Orient P with acute vertex first and consecutive edge directions
0,67.5,135,202.5,270 degrees, with lengths (u,b,c,d,v). Set
C=cos(pi/8), S=sin(pi/8), R=1/sqrt(2). Closure is equivalent to

    u=cR+dC-bS,    v=cR+bC-dS.

All b,c,d,u,v must be positive. In particular
u-v=(d-b)(C+S), so unequal acute legs are equivalent to unequal two bevel
lengths; equality gives the reflection-symmetric native shape. The newly
reviewed unrestricted native reduction confines T hosts to h=2u or h=2v
for h among b,c,d. Outside these six linear strata all contacts are whole
native sides; four-right full stars still remain admitted.

For nonsymmetric P (u!=v), a whole QQ contact identifying the SAME indexed
Q side by reflection across that side is impossible: at each endpoint the
two outgoing QP sides would have equal lengths, while the remaining P90
corner requires acute legs u and v. A same-index QQ match must instead
reverse endpoints by a halfturn. If exactly two private Q slots have distinct
lengths, each QQ side matches its own indexed length, and every Q has exactly
those two QQ slots. Along a QQ chain the two-step placement is then a fixed
translation, since it composes two halfturns. This intermediate transport observation alone does not establish
plane-wide periodicity. Its chain, band and completion obligations are now
closed in the [reviewed all-two-private synthesis](../lemmas/contact-right-angle-two-private-all-metric-periodic-escape.md),
including equal private lengths and other public aliases. The separate
[all-distinct one-private theorem](../lemmas/contact-right-angle-one-private-all-distinct-periodic-escape.md)
and [generic zero-private theorem](../lemmas/contact-right-angle-no-qq-generic-zero-private-reduction.md)
cover their stated subfamilies. Other side collisions and host regimes remain
outside those theorems; this source note supplies no broader classification.
