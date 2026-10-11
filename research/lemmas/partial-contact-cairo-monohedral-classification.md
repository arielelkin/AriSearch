# A direct unrestricted monohedral classification within the Cairo angle family

**Status:** freshly independently hostile-reviewed **VALID**; see [master review](../reviews/partial-contact-cairo-monohedral-classification-review.md) and [paired-repeat component review](../reviews/partial-contact-cairo-paired-repeat-classification-review.md). No novelty
claim. This is a restricted angle-family classification, not an arbitrary
pentagon or two-prototile theorem, and uses no imported pentagon list.

## Exact condition

Let w=sqrt3 and let P be any genuine convex pentagon with side directions
0,90,150,240,300 degrees and positive native sides(a,b,c,d,e). Thus

    b-c=w(d-a), e=w*c+d-2a,

and its cyclic native corners are the two90 pairs(a,b),(c,d), and the three
120 pairs(a,e),(b,c),(d,e).

Then P admits an unrestricted monohedral plane tiling if and only if at
least one of the following exact conditions holds:

1. a=c;
2. b=d;
3. a=b and e=2a;
4. c=d and e=2d;
5. a=d,b=c and e=2a.

Every metric in this union admits a doubly periodic monotiling. Arbitrary
original contacts and all isometries, including reflected copies, are
allowed. No claim is made that every monotiling is periodic.

## Necessity: all six internal equality cases are exhausted

If the four arms a,b,c,d are pairwise distinct, the independently reviewed
[private-arm theorem](partial-contact-cairo-private-arms.md), applied to a
single species, excludes every tiling under arbitrary contacts. Thus a
monotile must satisfy one of the six unordered internal equalities

    a=b,a=c,a=d,b=c,b=d,c=d.

The a=c and b=d cases are exactly conditions1 and2, requiring no further
necessary restrictions. The
[adjacent-repeat obstruction](partial-contact-cairo-adjacent-repeat-obstruction.md)
shows that a=b permits a monohedral tiling only if all four arms agree
(already condition1), or e=2a (condition3). Native reflection maps
(a,b,c,d,e) to(d,c,b,a,e), so c=d similarly permits only the all-equal case
or e=2d, giving condition4.

Closure makes a=d equivalent to b=c. The
[paired-repeat classification](partial-contact-cairo-paired-repeat-classification.md)
shows that this case permits a monotiling only if a=b, again all-equal,
or e=2a, giving condition5. These six comparisons exhaust every way four
values can fail to be pairwise distinct. Multiple simultaneous equalities
introduce no unhandled case; the indicated necessary statement is applied
to whichever equality is present. Thus the five stated conditions are
necessary.

## Explicit periodic sufficiency

If a=c, use the independently reviewed
[swapped-arm periodic cone](partial-contact-cairo-swapped-arms-periodic.md)
with its parameters c=a,D=d. Its partner word(c,B,a,D,f) then equals P
exactly: B=a+w(d-a)=b and f=wa+d-2a=e. Its four-face motif is consequently
a monohedral doubly periodic tiling by P. Native reflection sends b=d to
a=c and transports this witness, proving condition2 as well.

For condition3, normalize a=1. Closure uniquely gives

    P=(1,1,(3w-1)/2,(w-1)/2,2).

The freshly independently reviewed
[adjacent-repeat carrier](partial-contact-cairo-adjacent-repeat-periodic.md)
gives an exact eight-face monotiling with periods(w,-w),(3w,3w), area18,
and complete lattice separation. Scaling and native reflection supply
conditions3 and4 for all permitted metrics.

For condition5, closure wb-a=2a gives b=w*a. Normalize a=1. The
[paired-repeat carrier](partial-contact-cairo-paired-repeat-classification.md)
constructs three copies of(1,w,w,1,2) in a regular side2 hexagon, repeated
with periods(3,w),(0,2w). Its complete original-face lattice verification
and area/covolume prove a doubly periodic monotiling. Scaling supplies the
whole remaining stratum. This completes sufficiency.

## Meaning for two-shape research and review boundary

The theorem is a direct necessary-and-sufficient monohedral filter for
this fixed90/120 angle word. A pair containing any shape in the stated
union admits a periodic escape using that member alone. A hypothetical
aperiodic Cairo pair must therefore have both members outside the union;
internal repeats outside it remain possible mixed-tiling candidates, so
this does not reduce the problem to four-distinct arms alone.

The extraction has no new computation: the four contact/carrier mechanisms
have separate exact checkers and review artifacts. The paired-repeat proof and this exact case exhaustion have received their own fresh hostile reviews. The broader user task remains unresolved.
