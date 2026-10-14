# A one-right-angle pentagon and regular octagon: exact periodic carrier

Date: 2026-10-13. Status: independently hostile-reviewed VALID, including the symmetric family; [family review](../reviews/current-exact-convex-source-right-carrier-hostile-review.md) and [independent regular-instance checker review](../reviews/contact-structure-right-carrier-review.md).
This pair is periodic, not an aperiodic candidate.

## Exact shapes and placements

Put r=sqrt(2)>0, a=1+r and W=2a+1. Define cyclic vertices

    Q=((a,1),(1,a),(-1,a),(-a,1),(-a,-1),(-1,-a),(1,-a),(a,-1)),
    P=((0,-1),(1,-r),(a,0),(1,r),(0,1)).

Q is the regular octagon of side length 2. P is a genuine convex pentagon
with one 90-degree angle at (a,0) and four 112.5-degree angles. Let J(x,y)=
(-x,y). For every integer m,k, place

    Q + (m W, m a + 2k a),
    P + (m W+a, m a + 2k a),
    J(P) + (m W+a+1, m a + a + 2k a).

These polygons form an edge-to-edge plane tiling, periodic under lattice
vectors (W,a) and (0,2a). In particular both tile types are used.

## Plane covering and disjointness proof

In each column m, the octagons with centres (mW,ma+2ka) touch along their
horizontal top/bottom sides. Their interiors are disjoint. Different columns
are separated in x by a positive gap W-2a=1, so octagon interiors in
different columns are also disjoint. A column union has a left and right
piecewise-linear boundary, each the graph x=f(y), and fills precisely the
region between those two graphs. No horizontal gap remains at the joining
heights because successive horizontal sides coincide.

It suffices to describe the channel between columns 0 and 1, since all
other channels are translates by (W,a). Column 0 has centre heights 2ka;
column 1 has centre heights a+2ka. Its left bank is the right boundary of
column 0 and its right bank is the left boundary of column 1.

For each k join the following pairs of reflex bank vertices by straight seams:

    (a, -1+2ka) to (a+1, -r+2ka),
    (a,  1+2ka) to (a+1,  r+2ka).

The first seam has slope -(r-1) and the second slope r-1. They lie in the
channel, since at the displayed endpoint heights and throughout the seam
both banks bound the interval a<=x<=a+1, while the channel may extend
farther left/right. This is also seen directly from the octagon bank
segments. Each seam is a graph y=g(x) on [a,a+1]. Their order alternates
strictly, because r<a and a>1: a lower seam is below its upper seam, and
that upper seam lies below the next lower seam for all x in [a,a+1].

The band between the two seams for the same k has cyclic boundary

    (a,-1+2ka), (a+1,-r+2ka), (2a,2ka),
    (a+1,r+2ka), (a,1+2ka).

This is P+(a,2ka). The two diagonal right-bank segments meet at (2a,2ka),
the joining endpoint of successive column-1 octagons. The band between
that upper seam and the next lower seam has cyclic boundary

    (a+1,a-1+2ka), (a,a-r+2ka), (1,a+2ka),
    (a,a+r+2ka), (a+1,a+1+2ka),

which is J(P)+(a+1,a+2ka), with reverse cyclic order if desired. Its two
left-bank segments meet at the corresponding column-0 joining endpoint.
These bands exhaust the channel in both vertical directions and share only
seams or boundary segments. Thus they cover without interior overlap.
Together with all octagon columns they cover the entire plane.

## Exact geometric and angle checks

Successive Q edge directions differ by 45 degrees and edge lengths are 2,
so Q has eight 135-degree angles. For P the edge directions in the displayed
counterclockwise order are -22.5,45,135,202.5,270 degrees. Turning angles
are 67.5,90,67.5,67.5,67.5 degrees; all are positive and below 180. Thus
P has four 112.5 angles and one 90 angle. The first direction uses
r-1=tan(pi/8), and all vertices belong to the exactly specified quadratic
field Q(r), r^2=2, 1<r<2.

Shoelace areas are area(Q)=8+8r and area(P)=3+r. The lattice covolume is
2aW=14+10r=area(Q)+2area(P), consistent with the explicit covering proof.
Area equality alone is not used to infer covering or nonoverlap.

The complete native angle stars permitted by this palette are precisely
(112.5,112.5,135), (90,135,135), and four 90 corners; partial-contact stars
consist of two 90 corners opposite a straight sector. The exhibited carrier
uses only the first two full stars. Reflections are admitted in the original
problem, so use of J(P) imposes no supplementary rule.

## Research significance and limitations

Neither prototile tiles alone: Q has more than six sides; every P112.5
corner has no all-P full or flat star, so P cannot cover the plane alone.
The mixed pair nevertheless has the explicit periodic escape above.
This exposes the risk in a new right-angle partial-contact mechanism without
reopening the earlier Cairo or adjacent-low-private-octagon families.
A changed metric pair with this palette requires its own periodic escape
search and infinite existence proof. No arbitrary-metric classification,
aperiodicity, recognizability or novelty is asserted.

## Exact symmetric family extension

The same construction works for any positive real b,g,c (choose rational
values to keep coordinates in Q(sqrt(2))). Set t0=sqrt(2)-1,
s=b+t0*g, a=c+s, d=b+s, W=2a+g, and use

    Q=((a,b),(c,d),(-c,d),(-a,b),(-a,-b),(-c,-d),(c,-d),(a,-b)),
    P=((0,-b),(g,-s),(g+s,0),(g,s),(0,b)).

Use lattice vectors (W,d),(0,2d), with one Q centred at zero, one P shifted
(a,0), and one reflected P shifted (a+g,d). Q has four axial sides of
length 2b or 2c and four diagonal sides of length sqrt(2)*s; all its angles
are 135 degrees. P has the same one-right/four-112.5 angle word as above,
since its bevel slope is -(s-b)/g=-t0 and its tip slopes are plus/minus1.
Strict positivity of b,g,c gives genuine compact convex shapes.

Here is the global proof with the replacements written explicitly. Octagons
in each column touch along horizontal sides and different columns have a
horizontal clearance g. In the channel from column 0 to column 1, join
(a,-b+2kd) to (a+g,-s+2kd), and (a,b+2kd) to
(a+g,s+2kd). These seams lie in the channel. Their endpoint height ranges
are ordered: -s<=-b<b<=s<2d-s, since s>b and d=b+s.
They therefore form an ordered family of disjoint cross-channel seams.
The first band has vertices

    (a,-b),(a+g,-s),(W-c,0),(a+g,s),(a,b)

plus (0,2kd). Because W-c=a+g+s this is the stated translated P.
The next band is reflected P shifted (a+g,d+2kd); its leftmost tip has
x=a+g-(g+s)=c, exactly the column-0 octagon joining endpoint. The other
four vertices are the preceding upper seam and succeeding lower seam,
since d-s=b and d-b=s. The same monotone bank argument proves these
bands exhaust the entire channel with disjoint interiors. Translates cover
all channels, and together with all octagon columns cover the plane.

Areas provide an independent check:

    area(Q)=4ad-2s^2,
    area(P)=g*(b+s)+s^2,
    2dW=area(Q)+2area(P).

The last equality follows from d=b+s. It is supplementary to the explicit
partition proof. The regular instance above is b=g=c=1. This family is a
proved periodic source construction; it neither classifies arbitrary metrics
of the angle palette nor provides shape-only forcing.
