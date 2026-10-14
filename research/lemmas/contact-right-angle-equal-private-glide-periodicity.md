# An exact equal-private distance-three pair forces a period in every tiling

Date: 2026-10-13. Status: **adversarially reviewed VALID**. Independent review: `research/reviews/contact-right-angle-distance-three-hostile-review.md`; independent verifier: `research/reviews/contact-right-angle-distance-three-ring-check.py`. Tileability is not established or asserted. The theorem suffices to exclude this exact pair as a candidate for the main target.

## Exact polygons and theorem

Let c be the unique root of8c^4-8c^2+1in(9/10,1). Define r=4c^2-2,t=r/(4c); r=sqrt(2),c=cos(pi/8),t=sin(pi/8). All coordinates lie in Q(c). Put

    x=1, y=2, v=5/2, u=v+r*c,
    w=(u+v)/r-t(x+y), H=v+w-u+r(w-u)=5-4c.

Define cyclic pentagon vertices

    A=(0,-w), B=(xc,-w-xt), C=B+(u/r,u/r),
    D=C+(-v/r,v/r), E=(0,0), P=(A,B,C,D,E).

Define Q by starting at(0,0)and successively adding the eight edge vectorsL_i d_i, where

    (L_0,...,L_7)=(H,u,u,H,v,w,w,v),
    (d_0,...,d_7)=((1,0),(1/r,1/r),(0,1),(-1/r,1/r),
                  (-1,0),(-1/r,-1/r),(0,-1),(1/r,-1/r)).

All lengths are positive; the Qedge vectors sum to0. P is genuine convex with one90corner atC and four112.5corners. Q is genuine convex with eight135corners. Their different side counts ensure distinct congruence classes.

**Theorem.** Every plane tiling by unmarked isometric copies of P,Q, allowing reflections and unrestricted contacts, has a nonzero translational symmetry. Thus this pair is not an aperiodic pair. The theorem makes no claim that any plane tiling exists.

## Native forcing dependencies

The reviewed unrestricted native reduction applies to this palette. P's five side lengthsx,u,v,y,ware distinct, and its three nonacute-adjacent lengthsx,w,yavoid2u,2v. Consequently every admitted tiling is edge-to-edge, though the proof does not impose this rule externally.

The QlengthHoccurs on exactly its two native slots0,3and is absent from P. Both slots are QQcontacts, and every Qhas at most two such slots by native neighbor-word reduction; its QQmask is therefore exactly{0,3}. The Qpublic lengths areu,v,w; x,yare absent. Every Pmust have neighbor wordQ-P-Q-P-Q, since the other native word would require itsx,ysides to match Q. Each Ptherefore has three Qneighbors, including both acute-adjacent sides and its side of lengthw. Omitting either prototile is impossible by the same native forcing, so any tiling contains Q.

All field signs, length inequalities, closures and distinctness claims are exact checks in the retained finite computation and independent verifier.

## Complete first-neighbor census

Fix one Qplacement. Its private sides0,3must each match either native private side of a Qcopy, with both rotations and reflections allowed. Enumerating their two endpoint identifications on the unoccupied side and quotienting exact polygon vertex sets yields two actual geometric placements per private side, including the Qsymmetry duplicates.

Each publicuorvside identifies a unique native Pside, and its acute endpoint is forced to the Qendpoint adjacent to a QQside. This gives one placement on slots1,2,4,7. Each wside has two obtuse endpoints and gives two placements on slots5,6. Thus the complete option counts are[2,1,1,2,1,2,2,1], giving16rings. Any actual ring must have interior-disjoint neighbor polygons and no vertex in another side interior, since whole-tiling edge-to-edge contact was already proved intrinsically.

Exact enumeration accepts precisely one ring, choices[1,0,0,0,0,0,1,0]; every other ring has an independently checked forbidden partial contact. The placement-order convention and all15witness pairs are retained in `research/certificates/contact-right-angle-equal-private-distance-three-ring.json`, rebuilt by `research/searches/contact-right-angle-equal-private-distance-three-ring.py`. The independent verifier reconstructs placements with exact real algebraic geometry and polygon clipping, without importing the producer. This finite census establishes uniqueness of a necessary actual neighborhood; it does not establish extension.

## Exact QQ maps

For the unique ring let S(z)=Mz+b be the side0neighbor map, and T(z)=-z+a the side3neighbor map, with

    M=((-2c^2+1,2c^2-1),(2c^2-1,2c^2-1)),
    b=(-8c^3+5c^2+3c-5/2,4c^3-15c^2-3c+5),
    a=(8c^3-10c+10,20c^2+2c-5).

Exact identities giveM^2=I,det(M)=-1, S*T(Q)=Qas sets, and

    S^2(z)=z+d,
    d=(-8c^3+6c-5,-20c^2-2c+5)!=0.

Thus S is a glide reflection and TQ=S^(-1)Q. Neighborhood uniqueness transports under every Euclidean isometry, including any symmetry fixing the Qset; no native orientation mark is imposed.

## Bi-infinite chains and common period

In an arbitrary admitted tiling, start from any Q. Its unique QQneighbors areSQandS^(-1)Qin normalized coordinates. Applying the unique ring at SQforces S^2Qas its other neighbor; continue in both directions. All S^nQare distinct: an even repetition would force a bounded polygon invariant under a nonzero multiple ofd, while an odd repetition would force invariance under a nonzero glide reflection whose square is such a translation. Hence each QQcomponent is a bi-infinite chain. It and all Ptiles in its forced rings are invariant underd. An arbitrary isometric placement gives the corresponding rotated/reflected period vector of the same length|d|.

Connect consecutive Qcentroids through their shared QQ-side midpoints. In each convex Qthe two centroid-to-midpoint segments lie in its interior except at endpoints and meet only at its centroid. The resulting chain core is a simple proper two-sided polygonal line. Distinct Qchains have disjoint core paths: path portions lie in Qinteriors, and seam points belong only to QQadjacent tiles of their own chain. Its finite two-tile motif repeats underd, so the core stays within a bounded slab parallel todand runs to its two opposite infinities.

Two disjoint such proper lines cannot have nonparallel asymptotic directions. A proper line confined to a horizontal slab and running to opposite horizontal infinities separates the two far normal halfplanes, by the proper-line form of Jordan separation. A second line with nonparallel direction has its ends in these opposite halfplanes and would intersect it, impossible for distinct Qchains. Therefore all chain periods are parallel. Their equal lengths make them one common vector up to sign. Each chain and its full Pneighbor ring set is invariant under this common vector. Every Pbelongs to such a ring because it has three Qneighbors. Their union is the entire tiling, proving the nonzero translational symmetry.

## Reproducibility and scope

Producer replay, nondestructive:

    mise exec -- conda run --no-capture-output -n arisearch python research/searches/contact-right-angle-equal-private-distance-three-ring.py --check research/certificates/contact-right-angle-equal-private-distance-three-ring.json

The finite domain is16first-neighbor rings for one exact metric pair, not a bounded patch search for periodicity. SageMath10.9and Python3.12.13are recorded in the certificate; all comparisons use exact algebraic embeddings, not floating-point tolerances. The global period argument is analytic and conditional on any admitted tiling. It requires no infinite extension theorem, preserves all isometries and initial partial contacts, and does not resolve arbitrary two-convex pairs or general equal-private octagon metrics. Existence for this exact pair remains open.
