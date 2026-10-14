# Distance-three private mask: exact changed native candidates

Date: 2026-10-13. Status: finite ring computations and exact-pair universal-period argument independently reviewed VALID; [review](../reviews/contact-right-angle-distance-three-hostile-review.md). No plane extension inferred from a finite ring.

Use the fully asymmetric P defined in `contact-right-angle-nonsymmetric-carrier.md`: x=1,y=2,v=5/2,u=v+sqrt(2)c,w=(u+v)/sqrt(2)-t(x+y), c=cos(pi/8),t=sin(pi/8). All five P lengths are distinct; the three nonacute-adjacent lengthsx,w,yavoid2u,2v. Thus every admitted tiling is edge-to-edge by the reviewed native reduction.

If Q has two private slots and all other lengths amongu,v,w, no P can have the P-Q-P-Q-P neighbor word: that word would require its x,y sides matched to Q, and those lengths are absent from Q. Every P has the Q-P-Q-P-Q word. The private mask fixes every Q's two QQslots. Native incidence counts require each of u,v,w exactly twice among the six public Q slots. Each u/vside's unique acute endpoint must be next to a QQslot; a wside has two obtuse endpoints. For private slots0,3, the two short-gap public slots must therefore be u/vand the two middle long-gap slotsw,w.

## First exact candidate: mixed short gap killed

Take Q's cyclic lengths[H1,u,v,H2,u,w,w,v], with

    H2=sqrt(2)(w-v)+w+v-u,
    H1=u+w-v+sqrt(2)(w-u).

Orient edgei at i*pi/4. These defining lengths close the octagon and are positive; H1,H2are distinct and absent from P. The exact finite full-neighbor audit `contact-right-angle-distance-three-local-ring.py` checks16rings and all fail edge-to-edge contact consistency.

The reason is analytic: the short-gap u/vneighbors have their acute corners at the outer QQvertices and their obtuse corners at the central Q vertex. Their P-P sides issuing from that common vertex have lengthsxandy. These two whole sides must agree: both opposite endpoints are112.5and cannot lie in another native side interior. Sincex!=y, no tiling exists. This is a new native-metric exclusion, not a global distance-three classification.

## Second exact candidate: equal short gap, unique ring

Set H=v+w-u+sqrt(2)(w-u)=5-4c>0 and Q lengths[H,u,u,H,v,w,w,v]. The two Hslots0,3are private; x,yremain absent from Q. The octagon is closed and convex. The independent first-neighbor choices have sizes[2,1,1,2,1,2,2,1], hence16full rings. The exact audit `contact-right-angle-equal-private-distance-three-ring.py` permits exactly one ring, choices[1,0,0,0,0,0,1,0]; every other ring has a native vertex in another side interior and cannot occur in an admitted tiling. Native private-edge duplication is quotiented by exact vertex sets, so symmetries do not inflate the placement count.

For that unique ring, the neighbor across native side0is an affine glide reflection S(z)=Mz+b, with

    M=((-2c^2+1,2c^2-1),(2c^2-1,2c^2-1)),
    b=(-8c^3+5c^2+3c-5/2,4c^3-15c^2-3c+5).

The side3neighbor is T(z)=-z+a, where

    a=(8c^3-10c+10,20c^2+2c-5).

The exact audit verifies M^2=I,det(M)=-1, S*T(Q)=Qas a vertex set, and

    S^2(z)=z+d,
    d=(-8c^3+6c-5,-20c^2-2c+5)!=0.

These are exact field identities. They supply a plausible universal-period mechanism below, conditional on the independently reviewed ring census.

## Conditional global period lemma: chain barriers

Assume the unique-ring claim and the exact rigid-map identities above. In any admitted tiling, every Q has exactly two Q neighbors. Its unique Q/P ring transports by any isometry taking the reference Q to it. The side0glide therefore generates its entire bi-infinite QQchain S^n(Q), n in Z; the other neighbor is S^(-1)(Q)because S*T fixes the reference Q set. The chain and all its Pneighbor tiles are invariant under the nonzero translationd=S^2.

Choose within each chain a polygonal path through successive Qcentroids and shared QQ-side midpoints. Convexity puts path segments in Qinteriors except at their shared-side crossings. The path is simple because tiles have disjoint interiors and each Q is visited once. It is proper and stays within a bounded-width slab parallel to d, since the even vertices repeat by d and odd vertices by the glide. Thus it is a proper embedded line running to the two opposite directions of d.

Two different QQchains cannot have nonparallel period directions. A proper embedded line confined to a horizontal slab and running to opposite horizontal infinities separates the upper and lower half-planes outside that slab (the proper-line form of the Jordan curve theorem). A second proper line with nonparallel asymptotic direction has its ends on these opposite sides and must intersect the first. Their paths lie in disjoint Qinteriors and shared sides internal to their own chains, so intersection is impossible.

All QQchain periods are isometric images of d and hence have equal lengths. Parallelism therefore makes them the same vector up to sign. Each chain and its Pneighbor set is invariant under this common vector. Every P has three Qneighbors, so the union of these chain rings includes every tile. The whole admitted tiling therefore has a nonzero translation symmetry.

The argument proves no aperiodic tiling for this exact pair if the ring census and barrier lemma survive independent review. It does not construct a plane tiling; an empty tiling space also satisfies the universal conditional statement. Unique local rings alone are never used to infer existence. No arbitrary two-private metric classification or general aperiodicity theorem is claimed.

## Remaining gates

The retained [mixed-ring certificate](../certificates/contact-right-angle-distance-three-local-ring.json), [equal-private ring certificate](../certificates/contact-right-angle-equal-private-distance-three-ring.json), [independent checker](../reviews/contact-right-angle-distance-three-ring-check.py) and [fresh review](../reviews/contact-right-angle-distance-three-hostile-review.md) validate the finite domain and the chain-barrier exclusion. The result is extracted in [the stable exact-pair theorem](../lemmas/contact-right-angle-equal-private-glide-periodicity.md). Finite first-neighbor validity is not an infinite tiling certificate. General metric parameter families and other private masks remain unclassified; their missing global classification is not replaced by a larger bounded sweep.
