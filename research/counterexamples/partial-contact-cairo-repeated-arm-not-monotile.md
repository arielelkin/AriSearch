# A repeated native right-angle arm need not give a Cairo monotile

**Status:** independently hostile-reviewed **VALID** with a no-author-import
exact checker; see [review](../reviews/partial-contact-cairo-repeated-arm-counterexample-review.md). This counterexample refutes the proposed shortcut that any repeated
arm implies a periodic monohedral escape. No Rao classification is needed.

## Exact example

Let w=sqrt3>0, w^2=3,1<w<2. Give the Cairo pentagon P side lengths

    (a,b,c,d,e)=(1,1,1+w/2,1/2,w)

and side directions0,90,150,240,300 degrees. Its vertices are

    (0,0),(1,0),(1,1),
    (1-w*(1+w/2)/2,1+(1+w/2)/2),(-w/2,3/2).

Positive vector closure follows from b-c=w(d-a) and e=w*c+d-2a.
All supporting-edge determinants are strictly positive. Thus P is a genuine
convex Cairo pentagon with a=b, while the three distinct arm values are
1,1+w/2,1/2. Its e is not twice any of those values.

## Direct unrestricted untileability proof

Right-corner native arm pairs are(a,b)=(1,1) and(c,d). At a T the perpendicular
seam is a full90-to120 native side: its120 endpoint cannot lie inside its
mate's side. Every possible perpendicular pairing has two equal bank arms.
For perpendicular length1 both arm slots have other arm1; for the unique c
the bank length is d; for the unique d the bank length is c.

Suppose unequal90-to120 native arms of lengths m<M opposed along a ray from
a120 vertex. The exact two-T switch theorem would require equal bank sums
at the two switches. Both bank pairs here are equal pairs, so their sums
are2m and2M, impossible. Thus no arm can host a T.

An e side hosting a T would have its two120 endpoints at the two equal bank
endpoints, so e=2r for r in{1,1+w/2,1/2}. The exact displayed e=w avoids
all three values. Hence no T exists, and any hypothetical tiling is ETE.

Every e side would whole-match another e side, since a90-to120 arm cannot
whole-match a120-to120 e side (endpoint types differ), and splitting was
excluded. At an endpoint of an e/e seam the third120 tile cannot use an
e-adjacent120 corner, since its e would face an arm without a permitted T.
It must use the isolated120 corner with arm lengths{1,c}.

An endpoint-preserving e mate exposes arm pair(1,1) at one end and(d,d) at
the other. Neither can be filled by isolated pair{1,c}, because c!=1,d.
An endpoint-reversing e mate exposes{1,d} at both ends; again the isolated
pair{1,c} cannot match because d!=c. Whole arm lengths must agree in an
ETE tiling. All e mates are therefore impossible. Every copy has an e side,
which is the final contradiction.

This proof allows every isometry and arbitrary contacts. It uses no
classification, periodicity assumption or finite extension claim. The same
argument excludes any monohedral Cairo pentagon with a=b and three distinct
arm values a,c,d, whenever e avoids2a,2c,2d.

## Exact replay and scope

[Checker](../searches/partial-contact-cairo-repeated-arm-not-monotile.py):

    conda run --no-capture-output -n arisearch python research/searches/partial-contact-cairo-repeated-arm-not-monotile.py

Its domain is this exact pentagon,15 support determinants,5 squared lengths,
the5 unordered pairings of oriented90-arm slots with equal perpendicular
lengths (including self), all bank sums, and the3 doubled exclusions.
No tiling search, solver, randomness, deadline or numerical decision is used.
The local geometric two-T switch is imported from its separately reviewed
[lemma](../lemmas/partial-contact-cairo-two-t-switch.md).

This kills only the any-repeat shortcut. It does not classify e=2a or e=2d,
nor the monohedral potential of other repeated-arm patterns. A separate
primary RaoTable2 audit is consistent with this obstruction but is not a
dependency of the direct proof. No novelty claim is made.
