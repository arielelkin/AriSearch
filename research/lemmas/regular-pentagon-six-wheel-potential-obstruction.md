# Exact regular-pentagon six-wheel and its blocked second substitution image

Date:2026-10-13. Status: independently hostile-reviewed VALID;
research/reviews/regular-pentagon-six-wheel-hostile-review.md.
The displayed six-child image exists; the proposed seven-child second image
is impossible. This is not a claim about unrestricted plane tilings.

## Exact geometric first image

Let phi=(1+sqrt5)/2, rho=2/phi^3, z=exp(2pi i/5), chosen as the root of
z^4+z^3+z^2+z+1 with positive imaginary part and pi/3<arg(z)<pi/2.
Identify complex numbers with planar vectors. Set vi=z^i and mi=(vi+v_(i+1))/2,
indices mod5. Define

    P=conv(rho*m0,...,rho*m4),
    Qi=cyclic(vi,mi,rho*mi,rho*m_(i-1),m_(i-1)).

The five Qi are congruent genuine convex pentagons. Together with central P
they partition the regular parent R=conv(v0,...,v4). Their exact native angle
word is(108,90,126,126,90) degrees. P is regular, angles108, and has circumradius
rho*cos36=phi^(-2). Thus R is an isometric copy of phi^2 P, up to rotation.
The complete first substitution image is1P+5Q with linear scale phi^2 and
area factor mu=phi^4=(7+3sqrt5)/2. The classes are distinct because Q has
right corners and P does not.

The exact producer research/searches/regular-pentagon-six-wheel-exact.py
checks strict support inequalities, all pairwise intersections of the six
faces, complete parent area, the inflation area ratio, and all angle cosines.
Each child lies in R because all its vertices do and it is convex. The checked
pairwise interior disjointness and area equality prove covering of R: any
remaining gap in R would contain a relatively open positive-area region,
contradicting exact area conservation. No plane tiling is inferred.

## Angle-potential theorem

Let any P be a convex regular pentagon and any Q a genuine convex pentagon
with native angle multiset{108,90,126,126,90} degrees, arbitrary metric and
native cyclic order. A finite isometric P/Q partition of a similarity image
of P contains EXACTLY one P child. A finite P/Q partition of a similarity
image of Q contains ZERO P children. Contacts and reflections are unrestricted.

### Proof

All child native angles are at least90. At each point carrying a native corner,
incident sectors are genuine angles or at most one straight180-degree sector.
There are at most four genuine sectors. In units18 degrees, native angles are
6,5,7. The full-star equation6a+5b+7c=20 has only

    (a,b,c)=(1,0,2),(0,4,0),

and the flat-star equation6a+5b+7c=10 has only(0,2,0).
These are elementary exhaustive integer equations; the retained producer also
checks their domains a,b,c<=4 for full stars and<=2 for flat stars.

Assign native corner weights108->1,126->-1/2,90->0. Every interior native
star has total weight zero. Along the relative interior of a parent side the
child native sectors sum180, hence consist of two90 corners and have zero
weight; a child edge interior instead has no native corner weight. At a
parent native corner, its90/108/126 angle cannot split into two child native
angles because their sum would be>=180. There is exactly one unsplit child
native corner there, with the same angle and weight as the parent.

Summing all child native corner weights and grouping by location therefore
gives the sum of the parent native corner weights. Each P has weight5; each
Q has weight1-1/2-1/2=0. The P parent has weight5 and Q parent weight0.
Thus5N_P=5 or0 respectively, proving the claim. Every term is finite;
no density, compactness or selected-substitution assumption is needed.

## Consequence for the proposed seven-child second image

The proposed count matrix[[1,1],[5,6]] has area-compatible Perron root
phi^4 and first image1P+5Q, as constructed above. Its second image1P+6Q
is impossible by the theorem, regardless of seam topology, inner placement,
reflection or coordinates. More generally no ordinary geometric substitution
of this angle-palette pair can have a P child in a Q image; its count matrix
must have upper-right entry zero and cannot be irreducible.

The exact first image is not promoted to a plane tiling or forcing rule.
The obstruction excludes the proposed substitution mechanism for all these
metrics; it does not alone exclude arbitrary P/Q plane tilings.

## Replay and scope

    mise exec -- conda run --no-capture-output -n arisearch sage research/searches/regular-pentagon-six-wheel-exact.py

Finite domain: one exact six-wheel, six convex faces, all15 face-pair
intersections, exact support / angle / area identities; scalar star equations
in their fully stated finite ranges. The second-image exclusion is analytic
for any child count, not a bounded failed search. No exact seven-child geometry
or broader count enumeration was run because the potential obstruction acts
before that stage. Angle palettes with changed native corners evade the
proof and require a new mechanism.
