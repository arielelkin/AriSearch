# Arbitrary metrics for generic ternary opposite-angle A

Date: 2026-10-13. Status: independently adversarially reviewed VALID;
[fresh review](../reviews/terra-ternary-opposite-a-all-metric-fresh-hostile-review.md).
This is a restricted angle/native-word family theorem, not the global problem.

## Theorem

Let A,B be actual strictly convex hexagons. A has cyclic angles x,y,z,x,y,z,
where x+y+z=360 degrees and 90<x,y,z<180. B has two copies of each
r=360-2x,s=360-2y,t=360-2z, in any native order. Assume these six
angle values are pairwise distinct and the complete
three-angle star language is exactly AAA=(x,y,z), BBB=(r,s,t), and the
three AAB stars (x,x,r),(y,y,s),(z,z,t). In particular the generic distinct
angle stratum in the reviewed ternary star lemma satisfies this hypothesis.
There is no restriction on either polygon's actual side lengths.

Every tileable pair admits a periodic tiling, allowing omission of a species.
Reflections and unrestricted contacts in the original tiling are included.
Indeed, if any AAA corner star is metrically legal, A is centrally symmetric
and supplies a periodic escape. Otherwise no genuinely mixed defect-free
field exists; an admitted pure limit gives a monohedral periodic escape.

Dependencies: the independently reviewed defect-free convex-hexagon limit
and unrestricted monohedral convex-hexagon theorem in
[hexagon-limit-and-periodicity.md](hexagon-limit-and-periodicity.md); the
reviewed ternary star language and B-B propagation gate in
[two-hexagon-ternary-angle-star-balance.md](two-hexagon-ternary-angle-star-balance.md);
and the native colour ring argument in
[two-hexagon-ternary-opposite-a-palette-obstruction.md](two-hexagon-ternary-opposite-a-palette-obstruction.md).
The previous palette condition is removed here rather than assumed.

## Closure kernel and its strict triangle property

Write a_i>0 for side i between native corners i and i+1, indices modulo6.
Set u=180-x, v=180-y, w=180-z, so u,v,w>0 and u+v+w=180.
After rotating A, its first three unit edge vectors are

    e0=1, e1=exp(iv), e2=exp(i(v+w)),

with angles interpreted in degrees. The next three are their negatives.
Polygon closure therefore gives

    d0 e0+d1 e1+d2 e2=0,  di=ai-a_(i+3).

The real kernel is one dimensional, since e0,e1 are independent, and equals

    (d0,d1,d2)=lambda(c0,-c1,c2),
    (c0,c1,c2)=(sin w,sin u,sin v).

This follows directly by taking imaginary parts, then real parts, or the sine
law for the triangle whose angles are u,v,w. All ci are strictly positive.
They satisfy strict triangle inequalities: for positive p,q,h summing180,

    sin p+sin q-sin h
      =4 sin(p/2) sin(q/2) cos(h/2)>0.

Consequently every signed sum epsilon0 c0+epsilon1 c1+epsilon2 c2, with each
epsiloni in {+1,-1}, is nonzero. One opposite side equality forces lambda=0.
Any signed relation +/-d0 +/-d1 +/-d2=0 likewise forces lambda=0.
Thus either condition forces all three opposite side equalities.

## A legal AAA star forces one of those conditions

An AAA star chooses one native corner of each colour: one from {0,3}, one
from {1,4}, one from {2,5}. Reflections independently reverse its two arms.
There are exactly8 corner choices and8 independent arm reversals. Fix cyclic
colour order012; reversed cyclic order is included by reversing the entire
star and all arms. Its three ray matches impose three equalities among side
labels. Equalities are necessary even when multiple lengths coincide.

Six corner choices are three consecutive native corners i,i+1,i+2. Their
arm multiset is {a_(i-1),ai,ai,a_(i+1),a_(i+1),a_(i+2)}.
Each ray pairs two arms and each of the three corners has two incident rays.
In the equality graph, the two outer arms are the only vertices of odd
incidence; paired internal occurrences have even incidence. Every component
has an even number of odd incidences, so the outer arms belong to one equality
component. Hence a_(i-1)=a_(i+2), an opposite equality.
Equivalently cancellation of repeated internal labels along the three-ray
cycle gives this equality. The finite certificate checks all48 cases directly.

The other two choices, (0,4,2) and (3,1,5), use each native side exactly once.
Ray matches give a perfect matching M on the six sides. Let O be the opposite
pairing {(0,3),(1,4),(2,5)}. If M has an O edge, an opposite equality is
immediate. Otherwise M union O is one alternating six-cycle: a smaller
alternating cycle would have length2 and give a common edge. Traverse it and
sum the three opposite differences in traversal direction; equality along
M edges cancels all intervening values. This yields

    epsilon0 d0+epsilon1 d1+epsilon2 d2=0.

The kernel argument proves lambda=0 in every case. The exact64-case ledger
has56 direct-opposite cases and8 signed-relation cases. It is corroboration
of this complete combinatorial proof, not a bounded tiling inference.

Opposite edge vectors of A are then negatives of one another; the half-turn
pairs opposite vertices. A is centrally symmetric. Every convex centrally
symmetric hexagon tiles the plane periodically by translations, by the named
monohedral dependency. The pair admits that tiling with B omitted.

## When AAA is absent, the mixed field is impossible

Suppose A is not centrally symmetric. The preceding lemma prohibits every
AAA star in any defect-free field, at every actual side metric. A B-B edge
forces a pure B field by the reviewed no-ABB propagation gate. A connected
genuinely mixed field therefore has neither AAA nor BBB, and every vertex is
one of the three same-colour AAB stars.

Take a B cell with cyclic colour word b_k, k modulo6. The reviewed native
ring geometry numbers its A neighbours A_k so A_k has colours b_k and
b_(k-1) at consecutive slots k+2,k+3. Every direct or reflected placement
of A012012 has period3 and three different colours in consecutive slots.
Therefore b_k differs from b_(k-1), and its preceding slot k+1 has the third
colour absent from that pair. At the outer endpoint of the AA seam between
A_k and A_(k+1), their colours are respectively the third colours absent from
{b_k,b_(k-1)} and {b_k,b_(k+1)}. That vertex is AAB, so the two colours agree.
It follows that b_(k-1)=b_(k+1) for every k. This forces period2 and at most
two colours, contrary to B having two corners of each of three colours.

The defect-free limit of any original tiling is consequently pure A or B;
in fact pure A is also excluded when AAA is absent. The unrestricted
monohedral hexagon theorem gives a periodic tiling using its surviving type.
No purity assertion is made about every original non-edge-to-edge tiling.

## Requested additional-equality classification and specializations

Start with side word (L,L,M,P,Q,V), treating its five labels as distinct before
additional merges. The finite domain is all52 set partitions of those labels,
and the same64 corner/reversal cases. Exactly34 partitions admit AAA and18
do not. The five minimal additional equality patterns admitting AAA are

1. P=L;
2. Q=L;
3. V=M;
4. M=P and Q=V;
5. M=Q and P=V.

Every one of the34 admitting partitions is a coarsening of at least one of
these five; all further specializations were included, not inferred from
minimal cases alone. Only patterns4 and5 themselves lack an opposite equality;
all their proper coarsenings acquire one. Pattern4 imposes d0-d1+d2=0 and
pattern5 imposes d0-d1-d2=0. All34 therefore force centrality for actual closed
polygons by the strict triangle kernel. In the base stratum centrality yields
side word (L,L,M,L,L,M). Positive L,M give actual strictly convex centrally
symmetric hexagons at every admitted angle triple; their opposite edge vectors
close and their strictly increasing edge directions form a convex boundary.
The all-equal specialization is included. The18 non-AAA partitions require no
separate geometric realizability classification for this theorem: whenever
an actual polygon exists, the no-AAA mixed-field argument applies.

Positivity, convexity and compatible B neighbourhoods therefore leave no
residual case inside the theorem's angle/native domain. This does not claim
all52 formal equality partitions have actual polygon realizations. Arbitrary
other native A words and extra-star angle strata remain outside the theorem.

## Exact evidence and replay

[Producer](../searches/terra-ternary-aaa-equalities.py),
[certificate](../certificates/terra-ternary-aaa-equalities.json),
[independent checker](../reviews/verify_terra_ternary_aaa_equalities.py).
The producer uses standard-library integer equality operations only; no
solver, random seed, timeout or numerical geometry is involved. It exhausts
its stated finite domain. Replay the checker nondestructively:

    mise exec -- conda run --no-capture-output -n arisearch python research/reviews/verify_terra_ternary_aaa_equalities.py

Fresh hostile review is complete. The next mathematically justified obligation
is another native A word or a concretely changed extra-star hypothesis. Increasing metric or patch bounds on012012 cannot add
coverage to the theorem.
