# Additional fresh hostile review of the general Y partner construction

**Verdict: VALID throughout the stated open angle range and all positive closed Y metrics.**
Reviewer: `/root/penrose_extension_gate`, 2026-10-10. The reviewer authored neither
[the lemma](../lemmas/general-y-pentagon-periodic-partner.md), its fixture producer,
nor [the earlier independent formal checker](verify_general_y_partner_formal_independent.py).
This is a new review record and preserves the earlier reviewer identity.

## Full angle and metric domains

The hypotheses pi/2<theta<3pi/4 give 0<k<1/sqrt(2), h>0 and d>0. Every genuine
closed positive Y pentagon is covered; no relation from the former two-parameter
family is used. From S=sum(L_i), lambda=S+kL0/d is finite and exceeds every
L_i. Thus delta2=(k(lambda-L1)+L0)/h and

delta4=(L1+d*S)/h are both strictly positive. These arguments work for real or
transcendental angles and lengths, including repeated native lengths. The
angle endpoints are correctly excluded. At theta=2pi/3, theta=gamma is harmless:
the construction still works, with two distinct angle values instead of three.

The displayed Q edges close by direct coordinate substitution. Their cyclic
turns are 0<turn<pi and total 2pi; the supporting-height argument gives global
strict convexity and simplicity. The same proof applies to the carrier, whose
positive edge vectors are x,y,z,-x,-y,-z. The reflected Q angle word is Y; after
reflection and numbering from q2, its lengths are
(delta2,delta4,L0,lambda,L1). The side lambda exceeds every P side, proving two
distinct congruence classes under all isometries.

## Oriented dissection and complete plane

The five designated reversed internal seams cancel. The ten remaining child
segments form precisely the six carrier sides, with positive subdivisions.
All four children and the carrier are counterclockwise strictly convex polygons.
Therefore winding additivity proves the interior indicator identity. Open-set
arguments exclude any exterior child interior or overlap; taking closure of
finite polygons supplies coverage of every carrier point. No assumption about
an already embedded cut tree or only area equality is needed.

The pairwise determinants cross(x,y),cross(x,z),cross(y,z) are strictly positive
throughout the stated angle range. Their sum is both area(H) and cross(u,v).
The three opposite side shifts -v,u-v,u have the two actual circular corner
links (0,4,2) and (1,5,3), with total theta+theta+gamma=2pi and zero accumulated
shift. The source's complete flat universal-cover argument is valid. Equally,
its exact coordinates give a local Euclidean map of the compact quotient to
R^2/(Zu+Zv); area(H)=cross(u,v)>0 makes that covering degree one. This independently
checks the claimed disjoint full-plane lattice translation tiling. Partial
native-side contacts across carrier boundaries are admitted by the original
unrestricted tiling definition and cause no coverage problem.

## Compatibility criterion and scope

For an independently supplied Q in the reflected native numbering, put
lambda=length_Q(3). Its closure equations are

    h*delta4+k*L0-d*lambda-L1=0,
    delta2+k*delta4-h*L0-2*k*h*lambda=0.

These force exactly the displayed delta4 and delta2 when
length_Q(2)=L0 and length_Q(4)=L1. Actual positivity of Q suffices for the same
carrier and dissection; lambda>S is used only when freely selecting a new
partner to guarantee distinctness. This compatibility result is sufficient,
not necessary. The universal theorem asserts existence of a selected Q for
each P, and licenses no conclusion for an arbitrary unrelated given partner.

## Replay and independent checks

Read the complete lemma and both checker implementations, then replayed:

```text
conda run --no-capture-output -n arisearch python research/reviews/verify_general_y_partner_formal_independent.py
conda run --no-capture-output -n arisearch python research/searches/general-y-pentagon-partner-verify.py
```

The formal checker imports no author producer and reduces polynomial identities
only by h^2+k^2=1. It derives five reversed seams, the ten-edge exterior cycle,
all six carrier vectors, the area/determinant identity and opposite translations.
Its lambda is free, so it also checks the supplied-pair compatibility case.
The two fixture replays pass positive supporting sides, native angle cosines,
distinctness, carrier coverage density and all 38 possible lattice overlaps
each, 76 total, using exact algebraic lattice bounds and separation. Their
irrational theta/pi claims follow from rational nonintegral 2cos(theta), which
cannot be the sum of a root of unity and its inverse. These finite checks do
not stand in for the general proof. No theorem defect, reflection exception,
or omitted positive-metric case was found; arbitrary-pair classification and
novelty remain outside the claim.
