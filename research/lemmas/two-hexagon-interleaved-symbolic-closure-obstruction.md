# Interleaved A cannot coexist with contiguous or interleaved B

Date: 2026-10-12. Status: [independently reviewed VALID for I/I and corrected I/C](../reviews/two-hexagon-interleaved-symbolic-closure-review.md),
including the corrected matrices, positivity exclusions and spatial gate.
The earlier I/C local-only proof is withdrawn; its [erroneous C-direction certificate](../certificates/two-hexagon-interleaved-symbolic-closure-withdrawn-C-direction.json)
is retained solely as historical evidence and is not a proof dependency.

Use the angles and colours of
[same-colour AAB transport](two-hexagon-rank-nine-colour-transport.md):
A has p and q=240-p, B has r=360-2p and s=2p-120,
90<p<150, p!=120. **Claim:** A=I=001011 with either B=C=000111 or B=I=001011
admits no plane tiling. Reflections, partial contacts, and type omission are
allowed originally. The reviewed hexagon defect-free limit is trivalent,
with only same-colour AAB stars, so it necessarily has full six-A rings around
B centres. Every ring in the two stated cases is excluded by the gates below.

## Complete local domain and corrected closure matrix

The complete native domain and twelve whole-side seams are in
[the local side gate](two-hexagon-interleaved-local-side-obstruction.md):
3072 I/C rings with 67 seam closures, and 12288 I/I rings with 105 closures.
Reflected native side indices are r-k-1. One positive unknown is assigned to
each of the k native side-equivalence classes of a closure.

Put theta=p-120 and t=tan(theta/2), so

    sqrt(3)-2 < t < 2-sqrt(3), t!=0.

Directions j*60+m*theta are accumulated from exterior turns at the next
native corner. The **correct** lists are

| Polygon | (j,m), native side order |
|---|---|
| A=I | (0,0),(1,-1),(2,0),(3,-1),(4,0),(5,1) |
| B=C | (0,0),(1,2),(2,4),(3,2),(4,0),(5,-2) |
| B=I | (0,0),(1,2),(2,0),(3,2),(4,0),(5,-2) |

In particular B=C switches from an r turn to an s turn at native corner 3.
Use cos(theta)=(1-t^2)/(1+t^2), sin(theta)=2t/(1+t^2). Form the 4-by-k matrix
M over Q(sqrt(3))(t), with A's summed x,y direction components followed by B's.
Closure requires M times the class-length vector to be zero. Its denominators
are powers of 1+t^2, hence have no real poles.

The [corrected producer](../searches/two-hexagon-interleaved-symbolic-closure.py)
and [certificate](../certificates/two-hexagon-interleaved-symbolic-closure.json)
retain every matrix, generic rank and gcd of maximal-minor numerators. Exact
real algebraic root isolation lists every possible rank-drop angle. The full
ring-weighted outcomes are

| A,B | No nonzero vector at any angle | Further positive-vector exclusions | Locally possible rings |
|---|---:|---:|---:|
| I,C | 2688 | 288 | 96 |
| I,I | 12240 | 48 | 0 |

The I/C number 96 is a union over parameters, not simultaneous existence.

## Reviewed I/I positive-kernel exclusion

The 48 residual I/I rings all have closure

    (0,1,2,1,3,1 ; 0,2,2,2,3,2).

Its generic rank is 3 with nullity 1. The gcd of its 3-by-3 minor numerators is
t, so rank never drops in the admitted domain. In its kernel the ratio of
the second to third class-length coordinate is

    2(t^4-1)/(t^2+1)^2.

It is negative because |t|<2-sqrt(3)<1. These two lengths cannot both be
positive, excluding all 12288 I/I rings. Exact kernels at normalized-basis
poles are also checked. The reviewer independently derived the directions by
exterior-turn recurrence and verified all 105 matrices, minor gcds and parameter
partitions. A basis pole does not imply a pole of M.

## Corrected I/C local positive-vector exclusions

For each residual generic-nullity-one or isolated-rank matrix, isolate all
admitted real roots of the generic-rank minor gcd and every nonzero rational
kernel numerator and denominator. Check the exact algebraic kernel at each
point and one exact algebraic parameter in each complementary open interval.
Rank and component signs cannot change inside such an interval. Nullity is at
most one for these cases; a kernel basis can be scaled strictly positive exactly
when all coordinates have one strict sign. These exact partitions reject 276
rings and leave 96 rings possible on some parameter subset.

The remaining 12 rings have the sole five-class closure

    (0,1,2,1,3,4 ; 0,0,2,3,3,2).

Its generic rank is 3 with nullity 2. The rank-drop gcd t^3-t has no admitted
roots. In an exact two-vector kernel basis, coordinates 2 and 3 (numbered from 1)
are (0,0) in one vector and

    (1, (t^2+1)/(2(t^2-1)))

in the other. Every nullvector has third coordinate equal to its second times
that strictly negative ratio. No kernel vector has both positive. The corrected
certificate retains the opposed-coordinate relation and exact rank-drop gcd.
This excludes these 12 rings without assuming nullity one.

## Corrected I/C spatial gate

The [constrained transport producer](../searches/two-hexagon-interleaved-contiguous-transport.py)
takes the 96 locally unexcluded native rings, allowing them simultaneously as a
sound superset irrespective of parameter. Its
[certificate](../certificates/two-hexagon-interleaved-contiguous-transport.json)
retains every native B/A ring, every compatibility pair and every deletion round.
Across coarse direction k, rings must agree on shared A placements k,k+1 and
k+4,k+3. Triangle support requires states j,l in directions k,k+1 and j to l in
direction k+2. Repeated deletion gives an empty core. No infinite compatible
native field can use this superset.

Every I/C ring is either locally impossible or in the empty spatial superset.
That proves I/C untileability by a local geometric plus spatial argument,
distinct from the withdrawn faulty all-local claim. The I/ALT case is not part
of this calculation. Positive local kernels or angle-only tori are never
identified with full Euclidean tilings.
