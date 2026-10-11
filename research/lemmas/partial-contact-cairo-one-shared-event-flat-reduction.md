# A complete finite event-stratum reduction for the specified sole-cross pattern Pa=Qd

**Status:** freshly independently hostile-reviewed **VALID** in the specified
sole native Pa=Qd scope; see [review](../reviews/partial-contact-cairo-one-shared-event-flat-reduction-review.md). Sixteen one-parameter families
remain after scaling. This is a necessary reduction, not a construction,
classification of admitted tilings or solution of the global problem.

## Hypotheses and retained conclusion

Use w=sqrt3 and the native Cairo word convention. Let

    P=(s,b,c,d,e), Q=(A,B,C,s,f),

satisfy closure and strict positivity, with each species internally
four-distinct and with Pa=Qd=s its sole cross-native-arm equality. Every
isometry and arbitrary partial contact are allowed; either species can
be omitted in principle. Under these exact hypotheses, any plane tiling
must have its metric in one of the sixteen two-dimensional homogeneous
strata listed in the [record](../searches/partial-contact-cairo-one-shared-event-flats.md)
and retained in the [certificate](../certificates/partial-contact-cairo-one-shared-event-flats.json).
The shared arm ends at an e-adjacent120 corner in both species. Mixed
e-adjacent/isolated and both-isolated sole-cross native patterns lie outside
this theorem. After setting s=1 these are sixteen explicitly parametrized positive ratio
families with all privacy and proper-event exclusions and arm-order chambers
retained. The sixteen are local survivors only; no existence is asserted.

## Why the relevant arrangement is finite and complete

The two closure equations and Pa=Qd are independent and leave a
five-dimensional real homogeneous metric kernel over Q(w). There are
seven distinct numerical arm values. The actual native right-corner
perpendicular pairing inventory gives event bank multisets

    {s,s},{b,b},{c,c},{d,d},{A,A},{B,B},{C,C},{b,C}.

The two-T switch theorem requires equality of event totals for unequal
arm rays, and the e-host rule requires an e length equal to the actual
bank event total. Whole e/e matches require equal e lengths.
A self-event/self-event equality forces an undeclared arm equality and
is outside these hypotheses. The equality b+C=2b or2C similarly forces
b=C. Thus the complete remaining contact-changing hyperplanes are exactly

    b+C=2x, x in {s,c,d,A,B};
    e=2x or f=2x, x in {s,b,c,d,A,B,C};
    e=b+C, f=b+C;
    e=f.

There are 22 forms. Every exact positive privacy-preserving metric belongs
to the relatively open stratum of the intersection flat defined by all
forms vanishing at it, avoiding every proper unactivated form. Additional
undeclared native arm equality hyperplanes are excluded by hypothesis.
The finite arrangement therefore covers every admitted metric; no generic
assumption is made about the original pair.

## The stable necessary contact relation on a flat

Number native arms0..7 as Pa,Pb,Pc,Pd,Qa,Qb,Qc,Qd and native e sides8,9.
The perpendicular complement map is(1,0,3,2,5,4,7,6). On a flat define

    S_i={arm_i+arm_j: arm_other(i)=arm_other(j)}.

The necessary side-ray relation is: arms i,j may oppose only if equal
or S_i intersects S_j; side e_H may oppose arm i only if e_H belongs to
S_i; two e sides may oppose only if equal. All these comparisons are
identities of full linear forms on the quotient kernel. No transitive
closure is added and no collapsed numerical length is substituted for an
actual native slot. Strict two-T inequalities are dropped, so the relation
is a safe overapproximation.

For the e/arm rule, both rays start at120. An arm cannot be longer than
its opposing e side because the e's120 endpoint would be internal to it;
it cannot have equal length because the far endpoints are90 and120.
Hence it ends90 inside the e, giving a T whose actual bank event includes
that native arm slot. The e-host rule yields exactly the stated necessity.
For e/e rays, unequal lengths would put a120 endpoint inside the longer
side, so a whole equal match is necessary.

Every original120 vertex is a three120 star. Its native corner types are

    (Pa,eP),(Pb,Pc),(Pd,eP),(Qa,eQ),(Qb,Qc),(Qd,eQ).

Exhaust all 56 unordered triples, and all 8 independent native reflection
choices. Match the three rays cyclically by the necessary relation.
Sorted triples suffice because reversing cyclic order is represented by
reversing all three corners. Any actual star appears on this safe list.
If one native corner is absent from every listed star, that species cannot
occur. Each species individually is a four-distinct-arm nonmonotile by
[the private-arm theorem](partial-contact-cairo-private-arms.md), so any
pair tiling must contain both. An absent corner therefore kills the flat's
open stratum under unrestricted contacts.

If this filter leaves a flat but none of the twelve forms b+C=2x,e=2x,
f=2x for x in {c,d,A,B} is an identity, then its open stratum satisfies
[the reviewed forced-core obstruction](partial-contact-cairo-single-shared-core-obstruction.md)
and is also untileable. Proper excluded forms, rather than a sample
metric, justify that application.

## Exhaustion, positivity and pruning certificates

The producer begins with the exact closure flat and repeatedly intersects
with each proper arrangement form. It canonicalizes each flat by exact
RREF in eight native arm coordinates. It expands a contact-negative flat:
proper subflats can introduce contacts and must not be pruned. Only an
undeclared forced arm equality or an empty positive cone prunes descendants,
since every subflat inherits that obstruction. A one-dimensional kernel
has no positive metric in any proper further subflat, so its expansion
ends without an arbitrary depth cutoff.

For each privacy-preserving kernel the producer tests the equivalent
scaled strict positivity system: all eight arms and e,f are at least1.
All positive flat witnesses are retained. For each of the 34 negative
systems, the certificate retains nonnegative sum1 weights on these ten
length forms whose weighted sum is identically0. A strictly positive
metric would make this sum positive, so this is a direct Gordan dual
certificate independent of solver trust.

The complete output is 1639 visited flats: 1270 forced undeclared arm
equality, 34 no positive metrics, 318 missing native120 corners, 1 reviewed
forced-core obstruction, 16 local survivors. Each surviving kernel has
dimension 2. Every proper descendant stratum is also visited or safely
pruned and classified; there is no unexamined deeper exceptional metric.
A strict positive witness gives a nonempty relatively open kernel cone;
finitely many proper arm/event hyperplanes cannot cover it. The retained
normalized chamber samples additionally verify positivity, native privacy
and every unactivated event inequality directly for each survivor chamber.

This proves the stated necessary sixteen-family reduction with fresh
independent verification of the finite exhaustion. The no-author-import
checker reconstructs the full lattice in five reduced metric coordinates,
checks all duals and native slots, and validates all sixteen normalized
sidewords and their 102 open chambers. It does not prove any
of the remaining families tile, or that a locally legal star extends.

[Producer](../searches/partial-contact-cairo-one-shared-event-flats.py),
[exact certificate](../certificates/partial-contact-cairo-one-shared-event-flats.json),
[complete record and ratio sidewords](../searches/partial-contact-cairo-one-shared-event-flats.md).
