# Independent hostile audit: the off-normal strict precursor counterfixture

Date: 2026-10-15. Verdict: **VALID** for the exact finite positive precursor
fixture and its stated counterexample to a convexity-only angle bound.
The reviewer did not develop this parameter point or its master determinants.
No producer module is imported by the independent checker. No discovery log,
registry or Git state was modified.

## Exact claim and scope

Reviewed:
[producer](../searches/offnormal-strict-m-determinants-2026-10-15.py),
[retained record](../certificates/offnormal-strict-m-determinants-2026-10-15.json),
and [written argument](../searches/offnormal-strict-m-determinants-2026-10-15.md).

The point has tau=1/100, uY=2/5, hZ=tau*uZ,

    uX=(sin36+tau*cos36)/(sin36*(1-tau^2)+2*tau*cos36),
    mX=uX+(337/1000)hX,
    mY=uY+(708/1000)hY.

It asserts all four thin/thick and donor-parity precursor partitions,
all sixteen strict assembled receiving quads, all eight strict central
triangles, all sixteen analytic M determinants, and BOTH external tail
half-apex angles greater than 108 degrees. It satisfies the displayed
endpoint-capacity branch, not the full common-H or common-P congruence
conditions. No cap-cut parameters are supplied or certified.

Consequently it refutes an inference from strict precursor convexity plus
that endpoint branch to the claim that at least one tail half-apex is at
most 108 degrees. It does NOT refute a theorem additionally assuming common
H congruence, and is not a two-prototype or aperiodic construction. The root's
separate common-H obstruction is compatible with this positive local fixture.

## Independent reconstruction

I used the exact radical embedding

    cos36=(1+sqrt5)/4, sin36=sqrt(10-2sqrt5)/4,
    cos72=(sqrt5-1)/4, sin72=sqrt(10+2sqrt5)/4,

rather than the author's twentieth-root-of-unity construction. Sage AA
performs exact algebraic comparisons; no float, decimal parameter or
numerically evaluated angle is used. The checker verifies the unit identities
and double-angle relations before reconstructing the rhombs.

Both marks have 0<uZ<mZ<1 and hZ>0. The exact identity

    hX/(1-uX)=(tau+tan36)/(1-tau*tan36)

holds, with positive denominator and 0<beta=atan(tau)<36. Since beta+36<90,
there is no tangent-branch ambiguity: Xhead=beta+36. Also hY/(1-uY)=1/150,
and both donor tails have slope tau. These are precisely the claimed
endpoint-branch equalities, without asserting any further prototype matching.

## Source coverage and strict/reflex audit

All actual source arrows were reconstructed separately in native side order:

    thin:  X 0->1, X 2->1, Y 2->3, Y 0->3;
    thick: X 0->1, Y 1->2, Y 3->2, X 0->3.

For each parity I rebuilt its two internal donor apexes, two donor triangles
and two receiving quads directly from those arrows and inward normals.
Every source cell is strictly convex in its specified CCW native boundary
order, using EVERY supporting-line inequality, not merely the sign of
successive turns. This rejects a reflex corner, self-crossed order, or
suppressed collinear vertex.

The reviewer checker uses exact convex-polygon CLIPPING to compute each
pairwise intersection, independently of the author's separating-axis
routine. All intersections have zero area. Every vertex of every cell
satisfies the source rhomb's four closed supporting half-planes, so all
cells are contained. Their positive areas sum exactly to the rhomb area,
for all four cases.

These facts prove full coverage, not just almost-everywhere coverage. The
finite cell union is closed. A missing source point would have a neighborhood
missing that union; its intersection with a full-dimensional convex rhomb
has positive area, contradicting equality of areas. Zero-area intersections
of convex cells exclude interior overlap. Boundary contacts are permitted.

For each of the eight receivers I then rebuilt the actual words

    L=(U,t,M,p), R=(M,t,V,q), C=(M,q,p).

Every L and R is strictly convex in this CCW source-boundary convention.
All eight C triangles are strict. The three internal triangles U-M-p,
M-V-q and M-q-p are strict, pairwise interior-disjoint, and their areas
sum exactly to the original receiving quad. Exact area identities also
identify L and R as their internal half-triangle plus the appropriate
external donor half-triangle. All six assembled outputs owned by each
source case have pairwise zero-area clipped intersections as well.
Thus the off-normal edge split does not cause an unnoticed reflex output,
reversed R word, overlapping central sector, or source gap at this point.

Mark-local u,h,m and the actual shared arrow make the triangle and split
positions identical on the two sides of every physical source edge.
Together with the known infinite source partition, the finite dissection
checks justify the stated repeatable precursor partition. They do not
supply any omitted cap or two-class congruence data.

## Analytic M formulas and arrow handedness

In the receiver's actual-arrow frame, T=(0,0), H=(1,0), inward y>0,
t=(u,-h), M=(m,0), internal p=(x,y), one obtains directly

    cross(M-t,p-M)=m(y+h)-u*y-h*x.

For a tail quad the required normalized sign is positive. The author's
head quad is (H,t,M,pH), the reverse cyclic order of the actual R word,
so its normalized sign is negative; D_H is the negative of that expression.
This is a valid orientation convention, not a missing case.

The actual-arrow tangent a may oppose the source boundary tangent. With
n the receiver's inward normal, the global determinant equals

    cross(a,n) * [m(y+h)-u*y-h*x],

where cross(a,n) is +1 or -1. The independent checker verifies this equality
for every one of the sixteen actual configurations before checking its
normalized sign. Thus reflected/left-handed arrow frames are not silently
treated as CCW frames.

For the adjacent donor apex, let sigma be the source angle at that endpoint,
k its donor projection measured FROM that endpoint, and g its height.
The actual coordinate decomposition is

    f=k*cos(sigma)+g*sin(sigma),
    g0=k*sin(sigma)-g*cos(sigma).

At the receiving tail p=(f,g0); at its head p=(1-f,g0). This follows by
resolving the adjacent donor-edge direction and its inward normal in the
receiver frame. The projection k is u of the adjacent mark at a donor tail,
and 1-u at a donor head. I checked the complete eight-context table from
the physical arrows, with each row occurring in both parities. All sixteen
coordinates, y>0 conditions and strict determinant signs agree with the
retained certificate.

The formulas are universal coordinate identities over the stated admissible
six-parameter domain. Their positive evaluation here concerns ONE exact
point. Since y+h>0, each determinant is indeed a linear interval condition
on m: its boundary is the intersection of the corresponding t-p line with
the source edge. These conditions alone do not certify the other corners;
those were checked independently above.

## Both tail half-apex inequalities

At the external apex, the two vectors to T and M have dot product
h^2-u(m-u) and absolute determinant h*m>0. Thus their angle lies strictly
between 0 and pi and has cotangent

    [h^2-u(m-u)]/(h*m).

Because h=tau*u and m=u+k*h, this simplifies to the rational value
(tau-k)/(1+k*tau). The two exact fixture values are

    X: -32700/100337,
    Y: -17450/25177.

The checker derives these from the reconstructed vectors. Each is strictly
less than cos108/sin108=-cos72/sin72, using exact radical inequalities with
positive denominators. Cotangent is strictly decreasing on (0,pi), so BOTH
angles are strictly greater than 108 degrees. No numerical inverse tangent
or visual approximation enters the conclusion. Reflections preserve these
dot products and absolute determinants, so they cannot reverse the result.

## Independent replay, defects and verdict

The reviewer-owned checker is
[offnormal-strict-m-independent-2026-10-15.py](offnormal-strict-m-independent-2026-10-15.py).
It imports no author code; its exact radical geometry and polygon clipping
provide a separate implementation of the consequential geometric checks.
It also reconstructs all certificate record fields rather than trusting
its `strict` or `valid` flags.

    mise exec -- conda run --no-capture-output -n arisearch python research/reviews/offnormal-strict-m-independent-2026-10-15.py

Result: PASS. All four contained source partitions, sixteen assembled strict
quads, eight central partitions, sixteen actual-arrow M comparisons and
both >108 inequalities are verified exactly. No mathematical defect requiring
repair was found.

**Final verdict: VALID** as the stated positive precursor counterfixture.
The evidence establishes neither common output classes nor cap-cut
admissibility, universal decoding, periodicity exclusion, or an aperiodic
pair. The separately closed common-H construction component is not reopened
by this counterexample to its weaker convexity-only surrogate.
