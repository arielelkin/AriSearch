# Additional fresh hostile review of the general V/V partner theorem

**Verdict: VALID for the stated four-parameter family and partner existence.**
Reviewer: `/root/penrose_extension_gate`, 2026-10-10. The reviewer authored neither
[the lemma](../lemmas/pentagrid-v-v-general-double-y-partners.md), its producer,
nor the earlier [independent checker](verify_pentagrid_v_v_general_partner_independent.py).
This review preserves the earlier reviewer identity and records a separate
analytic audit and fresh execution of that independent checker.

## Domain, closure, convexity and congruence

The closure identities fix r,e,l,m uniquely from x,k,y,f. Their positive-side
domain is exactly

    x,k,y>0; x+k/phi<f<phi*(x+k); y<x+f/phi.

Indeed l>0 and m>0 give the two f bounds and e>0 gives the y bound; the remaining
r=x/phi+f+(x+f/phi-y)>f is positive automatically. Conversely every positive
side walk has these inequalities. There is no implicit extra condition on an
old mirror-family parameter.

Both native direction lists increase strictly, each cyclic gap is below pi,
and their total turn is 2pi. The signed-height block argument proves that every
edge supports the whole positive closed polygon. Hence all four reference
faces are honest strictly convex embedded polygons for every point of the
cone, including repeated side values. Half-turns preserve their orientation.

The unique edge between the two 72-degree corners has length r in A and f in
B, with r>f. This proves noncongruence including reflections. Changing y changes
r strictly, so the claimed partners are also pairwise noncongruent. No generic
or internally-distinct-side hypothesis is hidden in either statement.

## Dissection, partial contacts and infinite extension

The five designated internal reversals and ten exterior side chains account
for all 20 native sides. All are formal identities on the entire four-dimensional
cone. The exterior is the strictly convex hexagon with positive edge lengths
y, beta=e+l, gamma=m+r, y,beta,gamma; none can vanish in the strict domain.

Oriented boundary cancellation is a sufficient global embedding argument here:
each counterclockwise convex child has winding 0 or 1, so the sum of their
interior indicators equals the macro indicator away from the finite boundaries.
This excludes both overlap and exterior child interiors. Closure of each child
and finiteness of the union extend containment and coverage to all boundaries.
The proof thus does not assume that the seam drawing is already embedded and
does not infer dissection merely from equality of areas.

The three exact opposite macro translations are -v,u-v,u. The two actual
vertex links have three positive sectors each, total angle 2pi and zero total
shift. Their compact local Euclidean map to the lattice torus has covolume

    cross(u,v)/sin(pi/5)=y*beta+phi*y*gamma+beta*gamma>0

and area equal to that covolume. The covering degree is one, proving the full
infinite periodic plane. Unequal native cut locations on opposite macro sides
produce permitted partial contacts and do not affect the macro tiling or its
child dissection. No edge-to-edge hypothesis is being smuggled into the proof.

## Selected-partner quantifier and verification

For an arbitrary supplied V pentagon B=(b,d,c,h,j), positive closure gives
f=d,k=b,x=j and l=c,m=h, exactly the two f inequalities. Every
0<y<j+d/phi then gives a positive A_y and the proved torus. Reflection gives the
stated alternate mirror choice by exchanging the two flank side roles. This
proves existence of infinitely many selected periodic partners for each B;
it does not classify arbitrary independently supplied V/V pairs, nor claim
all tilings of a selected pair periodic.

Replayed:

```text
conda run --no-capture-output -n arisearch python research/reviews/verify_pentagrid_v_v_general_partner_independent.py
```

PASS: independently reconstructed native walks, five canceled seams, the ten-edge
exterior cycle and six-sided macro, formal periods and determinant, and all 56
complete exact separating-axis fixture comparisons. The checker imports no
producer; its exact lattice bounding intervals cover every possible overlap.
I inspected its implementation as well as the proof. The fixture remains a
check of one instance; the full theorem follows from the audited identities,
positivity, winding and degree-one covering. No defect or unaddressed strict
positive-metric case was found. No broader arbitrary-pair conclusion is licensed.
