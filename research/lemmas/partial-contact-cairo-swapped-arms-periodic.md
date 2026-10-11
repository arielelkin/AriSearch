# A four-parameter partial-contact Cairo periodic cone

**Status:** freshly independently hostile-reviewed **VALID** throughout the
positive4D cone; see [review](../reviews/partial-contact-cairo-swapped-arms-periodic-review.md). No novelty claim. This gives a new sufficient
periodic family, not an aperiodic construction or arbitrary-Cairo theorem.

## Exact polygons and domain

Let w=sqrt3, the positive root of t^2-3 with1<w<2. Choose real a,c,d,D>0
and put

    b=c+w(d-a), B=a+w(D-c), e=w*c+d-2a, f=w*a+D-2c.

Require b,B,e,f>0. This is an open homogeneous4D linear metric cone. Define
P,Q by ordered lengths

    P=(a,b,c,d,e), Q=(c,B,a,D,f),

and directions0,90,150,240,300 degrees. For any word(A,B,C,D,E), its exact
vertices are

    (0,0), (A,0), (A,B), (A-wC/2,B+C/2), (-E/2,wE/2).

Closure is equivalent to E=wC+D-2A and B-C=w(D-A), satisfied for both
polygons. Positive lengths and strictly cyclically ordered edge directions
with total turn360 and every turn below180 give strict convexity: for each
edge, cross products against successive edge vectors first increase and
then decrease the supporting-height partial sum back to zero; every
nonadjacent partial sum remains positive. Thus the lists define genuine
convex Cairo-angle pentagons throughout the domain.

**Theorem.** Throughout this cone P,Q admit a doubly periodic plane tiling
by two P and two Q faces per displayed period cell. Native partial contacts
occur whenever b!=D or d!=B. The construction persists on both equality
boundaries, where the corresponding two T points coalesce to a full90^4
vertex. If P,Q are noncongruent this is a pair of exactly two classes.

Neither arbitrary independently specified Cairo pairs nor every tiling of
these shapes is classified. A periodic tiling suffices to exclude this
whole family as a universal aperiodicity mechanism.

## Four whole faces and periods

Use vertices P_j,Q_j and reflection matrix

    S=[[-w/2,1/2],[1/2,w/2]],

whose axis has direction75 degrees. It maps Q side2 to P side0 with their
native120 endpoints identified. Let

    p0=P, p1=P4-P,
    q0=S(Q-Q2), q1=q0_4+q0_0-q0.

P faces are counterclockwise, Q faces clockwise. All are whole isometric
copies, and reflections are permitted. Put

    u=p1_0-q1_2,
    v=p0_2-q0_0.

Equivalently,

    u=((a-3wc-d+wD)/2,(-wa+c+wd+5D)/2),
    v=((3a-2wc+wD)/2,(-wa+2wd+3D)/2).

The exact area/covolume identity is

    -det(u,v)=2area(P)+2area(Q)>0.

Thus u,v are independent. Consider the locally finite periodic collection
of these four motifs translated by Zu+Zv. Disjointness and covering will
be proved from exact native boundary cancellation, not presumed.

## Six whole native seams

Match the following native sides preserving native endpoint labels across
P/Q seams; reverse endpoint labels within the P/P and Q/Q e seams.
Translations are added to the second named face.

| First face,side | Second face,side | Translation |
| --- | --- | --- |
| p0,4 | p1,4 |0|
| q0,4 | q1,4 |0|
| p0,0 | q0,2 |0|
| p1,0 | q1,2 |u|
| p0,2 | q0,0 |v|
| p1,2 | q1,0 |u-v|

All endpoint equalities are identities over K[a,c,d,D]. Because Q faces
are clockwise, these same-native-order P/Q seams cancel in the oriented
positive boundary p0+p1-q0-q1.

## Two directed interval cancellations

Write [x,y] for the directed segment from x to y, and treat a face-side
notation as its directed native boundary edge. Collinear concatenations
are exact directed-chain identities, not equality of whole native sides.

The first cancellation is

    (p0 side1) - (q0 side3)
      = - (p1 side1 + v-u) + (q1 side3 + v).

Both left segments concatenate forward from q0_4 through p0_1=q0_3 to
p0_2, with total length D+b. The right segments concatenate over the same
interval with their internal break at q1_3+v=p1_1+v-u. Endpoints satisfy

    q1_4+v=p0_2, p1_2+v-u=q0_4.

The second cancellation is

    (p0 side3) - (q0 side1 + v)
      = - (p1 side3 + v) + (q1 side1 + u).

The left concatenation runs from q0_2+v=v through q0_1+v=p0_3 to p0_4,
with total length B+d. The other internal break is q1_1+u=p1_3+v, and
its endpoints are q1_2+u=p0_4 and p1_4+v=v.

Every component length b,D,d,B is positive. Thus these cancellations hold
for all orders of their internal breakpoints. Unequal breaks are the two
right-angle T points on the interval, with opposite banks at different
native right corners. Equality b=D or d=B makes the corresponding breaks
coincide. The identities never assume an imposed edge-to-edge rule.

After translating these two identities over the lattice, together with
six whole seams, every positive oriented polygon boundary cancels. They
exhaust the20 native sides of the four motif copies, splitting only the
four b/d/B/D side slots when needed.

## Zero boundary plus positive area gives the plane tiling

Let m(x) count motif interiors over all lattice translates at a point
outside their boundaries. Local finiteness follows from bounded tile
sizes and the discrete independent lattice. The exact chain cancellations
make its jump across every generic boundary segment zero: oriented boundary
multiplicity is the signed change in the number of interiors.

Any two points outside the boundaries can be joined by a piecewise straight
path avoiding the locally finite native/split vertices and crossing the
finitely many encountered boundary segments transversely. At each crossing
m has zero jump. Hence m is a constant integer almost everywhere in R2.
Its mean on the period cell is total motif area/covolume=1, so m=1.
An overlap of two tile interiors would contain an open set with m>=2,
which is impossible. A missed point would lie in the open complement of
the closed locally finite tile union and give an open set with m=0, also
impossible. Therefore these whole copies form a plane tiling. Translating
by u or v preserves the whole collection and gives two nonzero periods.

This argument simultaneously proves global extension, disjointness and
coverage. It does not infer them from a finite locally legal patch.

## Changed exact fixture and evidence

Take a=1,c=2,d=3,D=4. Then

    P=(1,2+2w,2,3,1+2w), Q=(2,1+2w,1,4,w).

Each has five pairwise distinct lengths; they are noncongruent. Their right
corner pairings form the shared-arm pattern P0=Q2,P2=Q0. The native side
words differ from the earlier scalene-Cairo family, which had repeated
arms within each species. This fixture has both bank breaks distinct:
b!=D and d!=B. Exact periods are

    u=(-w-1,w+11), v=(3/2,5w/2+6).

The exact checker reconstructs this fixture, supporting-edge convexity,
area/covolume, and all44 nonidentity translated motif comparisons in the
complete lattice-coordinate bounding ranges. Every pair passes exact
convex separating-axis checks. This independently validates the fixture
without extrapolating its finite checks to the general cone.

[Producer](../searches/partial-contact-cairo-swapped-arms-periodic.py),
[search record](../searches/partial-contact-cairo-swapped-arms-periodic.md).
Replay:

    conda run --no-capture-output -n arisearch python research/searches/partial-contact-cairo-swapped-arms-periodic.py

No monohedral classification or corner-frequency assumption is needed by
this proof. The polygons may coincide at some parameters; the periodic
construction still applies then, and distinctness is asserted only when
noncongruence is established. No claim about universality of periods or
other surviving Cairo matching patterns is made.
