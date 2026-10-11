# The full V/W shared-order metric cone and a partner for every W

**Status:** adversarially reviewed VALID in the [fresh independent full-domain audit](../reviews/pentagrid-v-w-general-metric-fresh-review.md). Exact
formal replay and complete fixture overlaps are retained below. No novelty
claim is made. This extends the former mirror-V two-parameter family to the
full three-dimensional closure cone and covers every positive W shape after
cyclic renumbering.

## Full metric theorem

Put z=exp(pi*i/5), phi=(1+sqrt(5))/2. For real x,y,f>0 define

    H=y+phi*(f-x), E=f+phi*(y-x),
    r=phi*(x+f)-y, e=f+phi*(x-y).

Define V by consecutive side lengths (x,r,y,e,f), with angles after those
sides (2,2,4,3,4)*pi/5, and W by consecutive lengths (y,H,x,E,f), all angles
3pi/5. The complete positive metric cone of this shared-order family is

    x,y,f,H,E,r,e > 0.                                  (1)

Its dimension is three, or two modulo common scale. Its irredundant strict
inequalities are just

    x>0, y>0, H>0, E>0, e>0.                            (2)

Indeed E+e=2f, so (2) gives f>0, and e>0 gives y<x+f/phi, whence
r> x/phi+f>0. The closed cone has five extreme rays, normalized as

    (0,0,1), (0,1,phi), (1,0,phi),
    (1,1/phi,1/phi), (1,phi^2/sqrt(5),1/(phi*sqrt(5))).

Every metric in (1) has a doubly periodic whole-plane {V,W}-tiling with
four faces per period lattice, two copies of each shape. V and W have
different angle multisets and are distinct congruence classes. The metric
cone does not classify every independently specified V/W pair.

## Every positive equiangular W has a periodic V partner

Let W be any strictly convex equiangular pentagon, with exact native side
lengths. Cyclically number it so that side 0 has a minimum length y; put
x=length(side 2), f=length(side 4), and name the remaining lengths H,E.
After a direct isometry W's unit side directions are 1,z^2,z^4,z^6,z^8.
Its two real closure equations force

    H=y+phi*(f-x), E=f+phi*(y-x).

Because the given W is genuine, all five lengths y,H,x,E,f are positive.
The minimum choice implies x>=y. Consequently

    r=phi*(x+f)-y >= (phi-1)*y+phi*f>0,
    e=f+phi*(x-y)>=f>0.

Thus the metric lies in (1) and the theorem supplies an explicit positive
V partner. Both occur in the periodic tiling. This covers arbitrary
asymmetric W metrics, not only mirror-W. It asserts existence of *some*
V partner for each W, and does not assert that an arbitrary given partner
U or V already admits a period.

## Exact coordinates and closure

Use complex coordinates, identifying C with R^2. Write

    V=[y+e*z+f*z^3, r*z^2, 0, y, y+e*z],
    W=[0, y, y+H*z^2, y+H*z^2+x*z^4,
       y+H*z^2+x*z^4+E*z^6].

Their directed edges are respectively

    (x*z^4, -r*z^2, y, e*z, f*z^3),
    (y, H*z^2, x*z^4, E*z^6, f*z^8).

The V closure equations uniquely solve r,e in terms of x,y,f. The W
closure equations uniquely solve H,E. The formulas above follow using
z+z^(-1)=phi and phi^2=phi+1. Hence there are exactly three metric degrees
of freedom, without an extra hidden equality x=y or e=f.

All seven lengths in (1) are positive. Both directed edge chains turn
strictly counterclockwise once, with each exterior turn between 0 and pi.
For every supporting line the successive transverse increments first have
one positive arc and then one negative arc, returning to zero only at
closure. Every nonincident vertex lies strictly on the interior side of
each edge. This proves global strict convexity, not merely local turn
signs. The native corner angles of V are (4,2,2,4,3)*pi/5 and those of W
are (3,3,3,3,3)*pi/5, as required.

## Actual four-face quotient and its periods

Put

    u=2*y+e*z-r*z^2,
    v=(r+H)*z^2=2*phi*f*z^2.

Take counterclockwise reference faces

    F0=V, F1=r*z^2-V, F2=y-W, F3=r*z^2-y+W.

Each row (i,a,j,d,n,m) below means reversed endpoint equations
Fi[a]=Fj[d+1]+n*u+m*v and Fi[a+1]=Fj[d]+n*u+m*v, with indices modulo 5.

| i,a | j,d | n,m |
| --- | --- | --- |
| 0,1 | 1,1 | 0,0 |
| 0,2 | 2,0 | 0,0 |
| 0,3 | 1,3 | 1,0 |
| 0,4 | 3,4 | 1,0 |
| 0,0 | 2,2 | 0,1 |
| 1,2 | 3,0 | 0,0 |
| 1,4 | 2,4 | -1,0 |
| 1,0 | 3,2 | 0,-1 |
| 2,1 | 3,1 | 0,-1 |
| 2,3 | 3,3 | 1,-1 |

These are formal coordinate identities in x,y,f, not sampled coincidences.
Every side slot occurs once; the pairing uses only the three shared actual
values V0=W2=x, V2=W0=y, V4=W4=f. The r,e V sides and H,E W sides match
same-type copies. The former mirror construction imposed additional
coincidences that are unnecessary.

The corner-successor permutation has six genuine circular links: four
with angles (3,3,4) and two with (2,2,3,3), in units pi/5. Every sum is
2pi. The connected orientable quotient has 6-10+4=0 and no cone defects,
so is a compact flat torus. Actual seam reversals put face interiors on
opposite sides at each edge, and the circular positive sectors make the
coordinate map locally Euclidean at vertices.

Normalize crosses by s=sin(pi/5)>0. A direct calculation gives

    cross(u,v)/s = 2*phi*f*(2*phi*y+e)
                 = 2*phi*f*(phi*(x+y)+f)>0,
    cross(u,v) = 2*area(V)+2*area(W).                    (3)

Thus u,v are independent. The coordinate map from the compact polygon
quotient to R^2/(Z*u+Z*v) is a local homeomorphism, hence a finite covering
of the connected target torus. Its degree is total face area divided by
covolume; (3) gives degree one. Lifting proves full-plane coverage and
pairwise disjoint interiors of all Fi+n*u+m*v. This is an infinite legal
source, not merely a finite patch or a conjectural extension.

## Exact computation and scope

The source
[pentagrid-v-w-general-metric.py](../searches/pentagrid-v-w-general-metric.py)
independently solves the four real closure equations by exact linear
algebra over Q(zeta20), checks all ten seam endpoint identities and the
area identity over Q(zeta20)[x,y,f], and checks the actual circular corner
permutation. It also enumerates all 21 pairs of active constraints from
the seven inequalities to verify the five rays, and checks that the five
listed facets are irredundant.

The asymmetric fixture is x=2,y=1,f=3. It is outside the mirror subcone
x=y. Exact AA supporting-line and lattice-coordinate comparisons verify
the complete overlap domain and exact area density; their finite domain
is derived from pairwise exact lattice bounding boxes, not a fixed search
window. This is a check of one concrete instance; the general theorem is
proved by formal identities, positivity and covering degree.

Replay:

```text
conda run --no-capture-output -n arisearch python3 research/searches/pentagrid-v-w-general-metric.py
```

Replay environment: Python 3.12.13, SageMath 10.9. The completed fixture
checks all 32 possible nontrivial lattice overlaps. No random seed, solver,
timeout or memory cap is configured. No bounded
period search is involved. The primary target of two unmarked convex
polygons that force aperiodicity remains unresolved; this construction
supplies periodic partner pairs and falsifies any suggestion that a generic
asymmetric W metric alone prevents a periodic V/W source.
