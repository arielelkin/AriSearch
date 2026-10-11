# An exact area-compatible pentagrid pentagon family

**Status:** exact geometric family independently reviewed as valid in the [fresh audit](../reviews/pentagrid-area-compatible-family-review.md); plane existence and shape-only forcing unresolved. This is a constructive metric selection, not a claimed aperiodic pair. Its simplest proposed substitutions are excluded by a finite dissection obstruction.

## Exact family

Let z=exp(pi*i/5), specified exactly by z^4-z^3+z^2-z+1=0, Im(z)>0 and 4/5<Re(z)<81/100. Set phi=z+z^(-1). For parameters b,c>0 define U by consecutive edge directions

    (1,z^4,z^6,z^7,z^8)

and lengths

    (phi^2*b+phi*c, phi^2*b+phi*c, b, c, b).

Define V by edge directions

    (1,z^3,z^6,z^7,z^9)

and lengths

    (b, 2*phi*b+phi^2*c, b, phi*(b+c), phi*(b+c)).

Each vertex list is given by cumulative sums from0. Both close exactly, and both are genuine strictly convex pentagons. Their angle words after the sides are U=(1,3,4,4,3) and V=(2,2,4,3,4), in units pi/5. Their angle multisets differ, so the congruence classes are distinct. Taking b=c=1 gives an exact Q(z) fixture:

    U lengths (phi^3,phi^3,1,1,1),
    V lengths (1,3*phi+1,1,2*phi,2*phi).

This extends the earlier pure-power alphabet to positive golden sums; it is not one of the four residual V fixtures in that finite search.

The [exact producer](pentagrid-golden-metric-area-compatible.py) checks the two linear vertex bases b=1,c=0 and b=0,c=1. For each genuine side direction and nonincident vertex, its normalized supporting cross product is linear in b,c. Both coefficients are nonnegative, and at least one is positive. Thus every b,c>0 gives strict supporting-side inequalities; no numerical sampling or assumption that local turn signs imply global convexity is used. Native side lengths are positive by the same coefficient test. The [certificate](../certificates/pentagrid-golden-metric-area-compatible.json) retains both vertex bases and all30 supporting-side coefficient pairs.

## Area selection rather than irrational-length inference

Put A_U=area(U)/sin(pi/5), A_V=area(V)/sin(pi/5). Exact shoelace calculations give

    A_U = phi^3*b^2+2*phi^2*b*c+(phi^2/2)*c^2,
    A_V = phi*A_U.

The identity is checked coefficient by coefficient in Q(z). One derivation starts from a mirror-symmetric V with lengths (x,x/phi+phi*s,x,s,s), whose normalized area is

    (x^2+2*phi^2*x*s+phi*s^2)/2.

Set x=b,s=phi*(b+c) and use phi^2=phi+1 to obtain the displayed ratio. This makes a Fibonacci count matrix compatible with areas. It does not construct the required geometric subdivision or force an irrational ratio in every admitted tiling.

Under the explicitly imported complete monohedral classification used in [the reviewed filter](../lemmas/pentagrid-pentagon-monohedral-filter.md), U never tiles alone. In angle-after-side conventions V tiles alone only if L2=L4 or L3=L0. Here both reduce to b=phi*(b+c), which is impossible for b,c>0. Hence these two shapes pass the conditional individual monohedral exclusion. That exclusion is not a tilability proof for the pair.

## Critical substitution test

Because area(V)/area(U)=phi is irrational, whole-tile dissection counts for a homothetic inflation are uniquely determined by area. For linear inflation phi, the count matrix, columns indexing U,V parents, is

    M = [[1,1],[1,2]].

For linear inflation phi^k the matrix is M^k. Its first three powers are

    k1: [[1,1],[1,2]],
    k2: [[2,3],[3,5]],
    k3: [[5,8],[8,13]].

Thus a phi-inflated U would need two pentagons, and a phi-inflated V three. A phi^2-inflated U would need five pentagons. The [small-dissection theorem](../lemmas/pentagrid-golden-metric-small-substitution-obstruction.md) excludes every nontrivial convex-pentagon partition into fewer than six genuine convex pentagons, including partial seams. Consequently the first two inflation proposals fail before any forcing argument.

The phi^3 count13 for U and21 for V survives this numerical obstruction. No corresponding exact macro-patch, full-plane extension, recognizability, or universal forcing is supplied. Area counts alone do not justify increasing bounded patch searches. To reopen a homothetic route, produce an actual geometric dissection at the surviving counts, or a compound-supertiling construction with a distinct exact mechanism. Other nonhomothetic tilings by this pair remain unrestricted and unclassified.

## Integer-multiple expansion rejected by its corner geometry

The next smaller integer-golden expansion 2phi would have matrix [[4,4],[4,8]], requiring eight children in U and twelve in V. The [short-boundary obstruction](../lemmas/pentagrid-golden-metric-short-boundary-obstruction.md) excludes it at b=c=1 before any solver search: each expanded short side must consist solely of V sides2phi, whose endpoint angles cannot occupy the parent144-degree corners. In fact the same argument excludes every positive integer multiple m*phi. No unbounded plane-tiling conclusion follows.

## Six/seven-piece proposal rejected before a solver search

Another positive area-compatible matrix is [[5,1],[1,6]], with linear expansion lambda=sqrt(5+phi). It would require six children in a U parent and seven in a V parent, meeting the six-piece lower bound. This proposed fixed macrogeometry was rejected before running a placement solver.

At b=c=1 every child side length lies in K=Q(phi). A genuine side of a convex parent, covered by finitely many convex child polygons contained in that parent, is a concatenation of whole child sides: an edge lying on its supporting line cannot continue past a genuine parent corner without leaving the parent. Therefore the expanded parent U side of original length1 would force lambda to be a sum of child lengths in K. But Norm_K/Q(5+phi)=29. If lambda belonged to K, its rational field norm would square to29, which is impossible. Thus lambda is not in K, contradicting the boundary-length requirement. The attractive six/seven area counts do not give a geometric dissection.

This is a falsified proposal, with no SAT search or bounded patch evidence. The broader exact field obstruction is developed separately in [the root metric substitution lemma](../lemmas/pentagrid-generic-metric-substitution-obstruction.md).

## Scope, exact domain and replay

The computational domain is the two fixed linear vertex bases of these two fixed angle words, all15 side/vertex support pairs for each, the three quadratic area coefficients, and three count-matrix powers. It is a symbolic family identity verified by positive coefficient signs, not a finite grid search over b,c. No solver, random seed, timeout, numerical equality, or dependency modification is used. A first serialization attempt failed on Sage integer/rational objects; converting the matrix entries to ordinary integers fixed it without changing any geometry or mathematical check.

    conda run --no-capture-output -n arisearch python3 research/searches/pentagrid-golden-metric-area-compatible.py

Normal execution prints nondestructive JSON; --output may explicitly save a certificate. Fresh independent review of this family calculation is valid. The six-piece geometric lemma is reviewed separately. The full research problem remains unresolved.
