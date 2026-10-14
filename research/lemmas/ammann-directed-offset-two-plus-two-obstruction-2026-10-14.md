# Two-plus-two branches of the directed-offset Ammann gate

Date: 2026-10-14. Status: **independently hostile-reviewed VALID** for the stated local topology. The later [three-plus-one theorem](ammann-directed-offset-three-plus-one-obstruction-2026-10-14.md) completes the scheme classification: every admissible two-class rule is the midpoint/common-height component with periodic omission. See the [fresh review](../reviews/ammann-directed-offset-hostile-review-2026-10-14.md) and its [independent coordinate checker](../reviews/ammann-directed-offset-independent-2026-10-14.py).

## Definitions and theorem

Let phi=(1+sqrt(5))/2, t=sin(pi/5), c_T=phi/2, c_K=(phi-1)/2, s_T=t and s_K=phi*t. In either rhomb set A=(0,0), B=(1,0), C=(1+c,s), D=(c,s) and v=(c,s). Choose parameters 0<a_X,a_Y<1 and h_X,h_Y>0. Donor apices are measured from the actual arrow tail with the height into the donor rhomb. The thin directed edges are AB:X A->B, BC:X C->B, CD:Y C->D, DA:Y A->D. The thick directed edges are AB:X A->B, BC:Y B->C, CD:Y D->C, DA:X A->D.

For donor edges AB/CD write p=(a_X,h_X), and q=(c+1-a_Y,s-h_Y) for thin or q=(c+a_Y,s-h_Y) for thick. The four representative output pentagons are

    T0=(B, B+(1-a_X)v+h_X(s,-c), C, q, p),
    T1=(D, a_Y v+h_Y(-s,c), A, p, q),
    K0=(B, B+a_Y v+h_Y(s,-c), C, q, p),
    K1=(D, a_X v+h_X(-s,c), A, p, q),

using each type's own c,s,q. Assume their source sectors are valid disjoint partitions, all donor nodes are strictly interior, and all outputs are strict convex pentagons. Reflections are permitted in congruence comparisons. The opposite donor choice has the same unordered pair of congruence classes: reflection in BD preserves thin arrows and exchanges roles, and reflection in AC preserves thick arrows and exchanges roles. Thus this four-output domain represents all eight indexed outputs.

**Theorem.** If these four outputs have exactly two congruence classes with two indexed outputs in each class, then the grouping must be {T0,T1}/{K0,K1}, and a_X=a_Y=1/2, h_X=h_Y. Every admissible such rule has periodic monohedral omission coverings. Consequently all three two-plus-two partitions fail the aperiodic-pair target. This theorem does not exclude the four three-plus-one partitions.

## Exact invariants

Put D_T=area(T0)-area(T1) and D_K=area(K0)-area(K1). Direct shoelace expansion gives

    area(T0)+area(T1)=s_T,
    area(K0)+area(K1)=s_K,
    D_T=(a_Y-a_X)s_T+a_X h_Y-a_Y h_X+(c_T+1)(h_X-h_Y),
    D_K=(1-a_X-a_Y)s_K+a_X h_Y+a_Y h_X+c_K(h_X-h_Y)-h_X.

The differences of the sums of squared boundary-edge lengths are 2E_T and -2E_K, respectively, where

    E_T=(a_X-a_Y)(a_X+a_Y-2)+h_X^2-h_Y^2,
    E_K=a_X^2-a_Y^2+2a_Y+h_X^2-h_Y^2-1.

These are polynomial identities in the four parameters, not sample observations. The independent checker expands each from its separately reconstructed polygons and verifies the identities symbolically.

## Proof

Either crosswise two-plus-two grouping matches the two thin areas to the two thick areas. Summing would force s_T=s_K, contrary to phi>1. Hence only the within-type grouping remains.

For this grouping, congruence implies D_T=D_K=E_T=E_K=0. Subtracting the edge invariants gives E_T-E_K=1-2a_X, so a_X=1/2. Write a_Y=1/2+d, h_X=t*x, h_Y=t*y, and delta=x-y. Dividing the area equations by t gives

    d(1-x)+(c_T+1/2)delta=0,
    d(x-phi)+(c_K-1/2)delta=0.

If d is nonzero, adding the equations implies

    delta/d=(phi-1)/(phi-1/2)>0,
    x=1+(c_T+1/2)(phi-1)/(phi-1/2)>1.

The thin AB donor node is p=(1/2,h_X). Since it must be below the opposite horizontal side at height t, strict interior requires h_X<t, or x<1. This is a contradiction. Therefore d=0; the first area equation forces delta=0. The parameters are exactly a_X=a_Y=1/2 and h_X=h_Y.

This component erases the marks from the common isosceles donor triangle and is precisely the [reviewed common-triangle construction](../searches/ammann-bipartite-tree-pentagons-2026-10-14.md). Apply the same valid local partition to either homogeneous unit-rhomb lattice, with a checkerboard vertex coloring. All resulting pentagons have the associated one output class, and the periods 2(1,0) and 2(c,s) preserve the coloring and surgery. The partition therefore gives an actual periodic monohedral plane covering. This proves failure of the target for the entire admissible component, independently of a chosen Ammann source. QED.

## Dependencies, scope and replay

The known marked source and its directed edges are supplied by [the Ammann source proof](ammann-forcing-aperiodicity.md), Lemmas 5–7. The local algebra theorem itself does not assume source frequencies, periodicity, a finite tiling quotient, or a universal decoder. The midpoint omission construction uses the exact global partition argument linked above. Pairwise area equality alone is insufficient, which is why the edge-length invariant is necessary in the proof.

This lemma left four three-plus-one class assignments. The later [independently reviewed invariant theorem](ammann-directed-offset-three-plus-one-obstruction-2026-10-14.md) excludes all four exactly. The combined results classify admissible two-class rules in this topology to the midpoint/common-height component with periodic omission. The historical solver UNKNOWN was not used as an exclusion.

    mise exec -- conda run --no-capture-output -n arisearch python research/reviews/ammann-directed-offset-independent-2026-10-14.py --fixture

This verifies the symbolic invariants and an asymmetric strict-convex fixture; it is not a feasibility or exhaustive solver certificate for the residual.
