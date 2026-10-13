# Two similar convex pentagons: negative-conjugate size hierarchy


**Superseded for U candidate coverage:** the previously reviewed
[unrestricted at-most-two-U theorem](../lemmas/pentagrid-two-asymmetric-u-obstruction.md)
already excludes every pair of these cyclic angles at arbitrary metrics,
including fullquartic lengths and partial contacts. The U-specific boundary
application below is retained as an exact audit, not a new construction route.
The general count reduction and non-U statements remain unaffected.
Date: 2026-10-13. Status: exact count reduction and exact metric obstruction,
independently hostile-reviewed VALID; [review](../reviews/resumed-two-size-negative-conjugate-review.md). No construction or
novelty claim. The unrestricted problem remains unresolved.

## Exact hierarchy and independently checked count domain

Let A be a genuine convex pentagon of area1 (normalization only), and let
B have area r>=1. Consider an ordinary homothetic two-shape substitution
with linear inflation lambda>1 and irrational area multiplier mu=lambda²<6.
Both parent supports must be exactly partitioned into isometric whole copies
of A,B, permitting reflections and partial internal contacts.

The [reviewed six-piece theorem](../lemmas/pentagrid-golden-metric-small-substitution-obstruction.md)
states that a nontrivial convex-pentagon dissection into genuine convex
pentagons has at least six children. Every child has area at least1, but
lambda A has area mu<6. Therefore its dissection has one child. This child
cannot be A because lambda>1; hence B is congruent to lambda A and r=mu.
Choose a representative B=lambda A.

The second parent lambda B cannot have one child: neither A nor B has its
area mu²>mu. Its dissection has b copies of A and d copies of B, with

    mu²=b+d mu,  b,d in N,  b+d>=6.

Irrationality forces b>0. Its count matrix, with parent columns A,B, is

    [[0,b],[1,d]].

The positive root mu=(d+sqrt(d²+4b))/2 has conjugate
mu_-=(d-sqrt(d²+4b))/2<0. The inequality mu<6 is equivalent to
b+6d<36: the polynomial t²-dt-b has its unique positive root below6 exactly
when its value at6 is positive. Consequently the complete integer domain is

    d=0,...,5;
    max(1,6-d)<=b<=35-6d;
    d²+4b is not a square.

There are105 pairs before the last test and94 after it;67 have d>0.
These totals were independently reconstructed with integer arithmetic, not
quoted from the root. No geometric conclusion follows from the count domain.

A deterministic reconstruction command, requiring no retained solver state:

    mise exec -- conda run --no-capture-output -n arisearch python -c 'from math import isqrt; c=[(b,d) for d in range(6) for b in range(max(1,6-d),36-6*d)]; a=[(b,d) for b,d in c if isqrt(d*d+4*b)**2!=d*d+4*b]; assert len(c)==105 and len(a)==94 and sum(d>0 for b,d in a)==67; print("PASS:105 integer,94 irrational,67 d-positive counts")'

This is the complete stated finite count domain, with no solver, numerical
threshold, symmetry reduction, random seed or timeout.

## Conditional periodic-omission consequence for d=0

If d=0, substituting the one-child rule into the second rule gives a genuine
finite dissection of mu A into b isometric A copies, with mu=sqrt(b)>1.
Iteration provides A-only patches containing disks of arbitrarily large
radius, because the inflated convex parent's inradius tends to infinity.
The fixed positive tile area, bounded diameter and compact orientation space
give a locally convergent subsequence after centering these parents; disjoint
interiors and complete disk coverage survive. Thus A tiles the whole plane
monohedrally.

Under the explicitly imported complete convex-pentagon classification,
every tileable convex pentagon belongs to one of the fifteen families and
admits a periodic monohedral tiling. This imported dependency is the same
as in the [reviewed monohedral filter](../lemmas/pentagrid-pentagon-monohedral-filter.md).
Hence d=0 cannot produce an aperiodic pair under the original omission
quantifier. Without that classification dependency, the elementary argument
here establishes monohedral existence only; it does not itself prove
periodicity of every pentagon reptile.

## A concrete exact shape excludes every94 count pair

Set phi=(1+sqrt(5))/2. Take the exact pentagon A=U at b=c=1 from
[the reviewed geometric family](../searches/pentagrid-golden-metric-area-compatible.md).
For clarity, define z=exp(pi*i/5) exactly by

    z⁴-z³+z²-z+1=0, Im(z)>0, 4/5<Re(z)<81/100,
    phi=z+z^(-1).

Its consecutive edge vectors are

    phi³, phi³ z⁴, z⁶, z⁷, z⁸,

and its vertices are their cumulative sums beginning at0. Exact closure,
strict convexity and positive area are established in that reviewed family.
The interior angles AFTER those five sides are (1,3,4,4,3)*pi/5; avoid
shifting these labels into a vertex-before-side convention. The side-length
multiset is {phi³,phi³,1,1,1}. **Conditional on the explicitly imported complete pentagon classification**,
this pentagon cannot tile monohedrally, as established in the reviewed filter.
The94-count dissection exclusion below does not use that classification. Scaling it
to area1 changes no argument below; instead retain its stated short length1.

**Claim.** There is no one-child two-size hierarchy on this A with
irrational mu<6, b,d>=0, b>0, mu²=d mu+b, b+d>=6.

Write K=Q(sqrt5), lambda=sqrt(mu), and F=Q(lambda). Since mu is irrational
quadratic and its other real embedding is negative, mu is not a square in
Q(mu): a square would map to a nonnegative real number under both embeddings.
Therefore [F:Q]=4, with minimal polynomial

    t⁴-dt²-b.

Its roots are ±sqrt(mu) and ±i sqrt(-mu_-): two real and two nonreal roots.
Thus F is not Galois over Q: F is a subfield of R and cannot contain its
nonreal conjugate roots. Its only quadratic subfield is Q(mu). Indeed two
distinct quadratic subfields would generate a degree4 biquadratic Galois
extension, which would equal F, a contradiction.

In a convex parent partition, every supporting boundary side is a
concatenation of complete native child sides. A child side cannot continue
past a genuine parent endpoint without leaving the parent. This remains
true with arbitrary reflections and partial internal contacts. Consider a
parent mu A side corresponding to one of the original length1 sides.
Its length is mu. Small-child side lengths are1 or phi³; large-child side
lengths are lambda or lambda phi³. Hence

    lambda²=mu=a+lambda c,
    a=m+n phi³, c=u+v phi³,
    m,n,u,v nonnegative integers.                    (1)

This is an actual boundary equation, not an imposed edge-to-edge rule.

If K is not contained in F, adjoining sqrt5 to F has degree2, so
[K(lambda):K]=4. But(1) would give lambda a polynomial of degree at most2
over K, impossible. Therefore K is contained in F. By uniqueness of the
quadratic subfield, K=Q(mu). Now lambda is quadratic over K, and(1), whose
left side and a are in K, forces c=0. Nonnegativity consequently gives
u=v=0: no large-child side occurs on this particular parent side.
Thus

    mu=m+n phi³.                                    (2)

Since 4<phi³<5 and mu<6, either n=0 (mu is rational, excluded), or n=1 and
m=0 or1. For m=0, mu=phi³=2+sqrt5 satisfies mu²=4mu+1, forcing b=1,d=4,
whose child total is5, contrary to b+d>=6. For m=1, mu=3+sqrt5 has positive
conjugate3-sqrt5, contradicting mu_-<0. All94 count pairs are excluded.
This is an unbounded geometric argument across the finite count domain;
no placement enumeration was needed.

### Explicit six-child example killed before placement

The small surviving arithmetic option b=4,d=2 gives

    mu=1+sqrt5=2phi, lambda=sqrt(2phi),
    lambda A -> B,
    lambda B -> 4A+2B.

It meets the six-child lower bound and has negative conjugate1-sqrt5.
Nevertheless its boundary equation fails: lambda is quadratic over K, so
no B side can contribute to the mu-length short parent side; phi³>mu leaves
only unit A sides, whose integer sum cannot equal2phi. This is a direct
singleton failure certificate, including unrestricted child isometries and
partial internal contacts.

## Scope, assumptions, and remaining construction obligation

Derived: the count domain, negative conjugate, quartic field structure,
whole-side boundary equation and obstruction for the explicitly given U.
Imported: the six-child dissection theorem and exact U geometry.
**Conditional external dependency:** the complete pentagon classification is
used only for the periodic d=0 escape and the U monohedral exclusion, never
for the94-count geometric obstruction. No edge-to-edge,
chirality, neighbor uniqueness or fixed contact graph is assumed.

The general d>0 two-size mechanism remains open. The field obstruction
uses the specific length module of U; it does not exclude pentagons with
other lengths, angles or metric modules. An angle-star exclusion of a base
pentagon would also exclude its similar-sized pair immediately, because
sizes do not change corner angles. Thus a successful base must admit the
necessary corner sums while avoiding monohedral metric families.

The next constructive object must give another exact convex pentagon P,
a specific surviving(b,d), and a pointwise dissection of mu P into bP+d
sqrt(mu)P. It must separately prove whole-plane existence and universal
shape-only aperiodicity. Neither the one-child rule nor a Perron irrational
frequency supplies recognition or excludes unintended periodic tilings.
No placement search is justified without new exact metric geometry.
