# One exact thirteen-piece inflation test

**Status:** completed prescribed 120-second exact solver experiment; Z3 returned **unknown (timeout)**. No second run or count expansion was made. This tests a fixed macrodissection, not aperiodicity, plane tilability, or a sequence of larger patch bounds.

## Exact mathematical question

Use the b=c=1 pair in [the area-compatible family](pentagrid-golden-metric-area-compatible.md): U lengths (phi^3,phi^3,1,1,1), V lengths (1,3phi+1,1,2phi,2phi), with respective angles after their sides (1,3,4,4,3), (2,2,4,3,4) in units pi/5. Let z=exp(pi*i/5), phi=z+z^(-1), rho=phi^3. Does the convex parent rho*U admit a finite partition into five U and eight V copies, including reflections and partial contacts?

The prescribed counts are uniquely required by area: area(V)=phi*area(U), rho^2=5+8phi. The [reviewed short-boundary obstruction](../lemmas/pentagrid-golden-metric-short-boundary-obstruction.md) shows that, conditional on the named monohedral classification, rho is the smallest surviving homothetic scale for this metric. This is why one specific13-child question is tested. There is no automatic attempt at the21-child V parent or a larger scale.

## Reduction to a complete fixed geometric domain

Every finite convex partition has connected positive-length edge adjacency: connect two piece interior points by a path in the parent interior avoiding the finitely many graph vertices; it crosses piece sides at positive contact segments. If two pieces have positive contact, their native edges at that contact are parallel, even when contact is partial. Since all reference side directions are powers of z, the relative orientation angles propagate in integer multiples of pi/5.

The parent36-degree corner can contain only one genuine child corner, which must be the unique U36 corner. Fix that child as index0, rotation0 and translation (rho-1)*phi^3 on the real axis. Its two rays coincide with the parent corner rays.

Both reference polygons have exact intrinsic mirror symmetries, checked on all five vertices before solving:

    U: w -> z^9*conjugate(w)+U1-z^9*conjugate(U1), vertex j -> 2-j mod5;
    V: w -> z*conjugate(w)+V4-z*conjugate(V4), vertex j -> 3-j mod5.

Thus reflected copies reduce to proper reference rotations z^k, k=0,...,9. The remaining12 children have10^12 raw orientation assignments. Their two translation coordinates are arbitrary real numbers in the independent basis (1,z), with no grid or rational-denominator bound. Copies of the same type, excluding the anchored U, are ordered by their first translation coordinate to remove label permutations only.

## Exact solver formulation

[The producer](pentagrid-golden-metric-phi3-macro.py) uses SageMath exact cyclotomic arithmetic to calculate reference vertices, intrinsic mirrors, rotation support intervals and the area identity. A real field element is encoded as a+b*phi with exact rational a,b. Z3 phi satisfies phi^2-phi-1=0 and3/2<phi<5/3, selecting the intended root. No floating coefficient or approximate equality enters a constraint.

Containment uses all five parent supporting half-planes for each of13 children,65 constraints. For each child orientation, extrema of the projection cross(z^j,p)/sin(pi/5) are precomputed exactly. A translated minimum is a linear expression in translation coordinates over Q(phi), selected by a one-hot orientation Boolean.

For each of78 unordered child pairs, the model imposes separation along one of five unoriented global edge-normal axes, including either order of the two projection intervals. Every possible child edge is parallel to one of those five axes. The separating-axis theorem therefore gives necessary and sufficient pairwise interior disjointness for these convex polygons. Partial sides and point contacts remain permitted.

Total child area equals parent area exactly. Hence a satisfying contained, interior-disjoint model gives a full parent partition by the same closed-union and area argument as for the periodic witness. Any SAT model must nevertheless be independently reconstructed and verified in Sage before being accepted.

This is a finite orientation/separation-branch domain with continuous translations: each fixed branch is a finite linear-inequality feasibility problem over fixed exact algebraic coefficients. The QF_NRA presentation introduces the fixed algebraic root explicitly. Z3 AtMost orientation constraints are serialized using its SMT-LIB extension; the retained formula is intended for the recorded Z3 version.

## Resource limit, replay and result

The solver receives exactly one check with timeout120000ms and random seed0. Formula construction time is separate and retained in the result. The producer is nondestructive by default; explicit output arguments preserve the complete formula and result:

    conda run --no-capture-output -n arisearch python3 research/searches/pentagrid-golden-metric-phi3-macro.py --formula-output research/certificates/pentagrid-golden-metric-phi3-macro.smt2 --output research/certificates/pentagrid-golden-metric-phi3-macro-result.json

[Retained exact formula](../certificates/pentagrid-golden-metric-phi3-macro.smt2); [result and metadata](../certificates/pentagrid-golden-metric-phi3-macro-result.json). The result records formula SHA256, byte count, Z3 version, completion status, reason_unknown when applicable, exact raw model when SAT, and actual solver statistics.

A timeout or unknown result does not exclude the macrodissection. An UNSAT response is evidence only for this fixed complete macro-domain unless the encoding and proof evidence are independently audited. A SAT partition of the U parent alone would still require a V-parent dissection, a full-plane extension proof, and universal shape-only forcing before it could contribute to a solution. No bounded failure is promoted to aperiodicity.

If the critical seed times out, change construction mechanism rather than increasing the child count. The precise remaining question is the existence of the specified exact13-piece dissection; its statement does not by itself provide a new method for proving it.

## Completed result

The sole check returned unknown with reason timeout after 120.205638 seconds. Formula construction took 2.334517 seconds. Z3 version 4.16.0; retained formula 781096 bytes, SHA256 92a78e9028b41707d5ab306f28faf76d1449703e6be0929f13d576fcec964727. No SAT model, UNSAT certificate, dissection, or tilability consequence was obtained. This experiment is completed and is not a reason to increase the patch count. The changed direct Robinson-triangle partition mechanism is now investigated separately.
