# Independent hostile review: unequal arrow-indexed cap cuts

Date: 2026-10-15. **Verdict: VALID.** Reviewer: independent of the construction and certificate author. I read the final corrected [obstruction proof](../searches/unequal-arrow-cut-angle-obstruction-2026-10-15.md), its equal-radius predecessor and source partition, the actual native-arrow tables, the exact producer, and the retained certificate. I wrote and ran a separate verifier with no producer imports.

## Exact claim and hypotheses

The construction retains the Ammann thin/thick rhomb source, opposite donor/receiver parity, mark-local normal-foot donor triangle rule, and the three-sector receiving partition. At each donor node its six rays are indexed by actual arrow roles as (tail, donor-foot, head, head-side receiver-foot, opposite donor, tail-side receiver-foot). Ray i is cut by a fraction r_(Z,i) depending only on mark Z and that role, identical in every species/parity context. Fractions may differ on different rays. Thin caps remain hexagons; thick caps split across the specified opposite-edge chord into two pentagons. All sectors, cuts and resulting polygons are assumed embedded, strict and genuine.

The theorem says this entire admissible component cannot have one common pentagon class P and one common hexagon class H. It makes no claim for arbitrary cut fractions depending on source context, arbitrary apex locations, other cap incidence, or arbitrary two-convex-polygon constructions. The contradiction among receiving hexagons is sufficient: strict pentagons cannot be congruent to strict hexagons, so a two-class outcome would require every receiving hexagon to belong to the same H class. It is not necessary to solve pentagon congruences or recognize the cap chord intrinsically.

## Actual source angles, independently reconstructed

Let Xt,Xh,Yt,Yh be triangle base angles at the actual arrow tail/head. The normal-foot hypothesis puts each strictly between 0 and 90 degrees. The source arrow data used are:

    thin:  (0->1,X), (2->1,X), (2->3,Y), (0->3,Y);
    thick: (0->1,X), (1->2,Y), (3->2,Y), (0->3,X).

A source vertex has one adjacent donor edge and one receiver edge. For the receiving quad, the external donor triangle adds its base angle to the source-rhomb corner, while the internal donor triangle removes its base angle. Both base angles must be selected by their actual endpoint role, not by the cyclic orientation of the edge. Thus the retained corner is sigma + incoming base - outgoing base. The geometry is the angle between the external triangle side and internal donor side; the assumed embedded strict source partition fixes the indicated sector and rules out a wrapped-angle ambiguity.

I independently enumerated both species, both donor parities and the two endpoints of both receiving edges. All sixteen forms agree with the written proof. In each thin parity their multiset is

    a, b, 144, 144,
    a=36+Xt-Yt, b=36+Yt-Xt.

In each thick parity it is

    c, d, 72, 72,
    c=108+Yt-Xh, d=108+Xh-Yt.

In particular incoming X-tail corners give a in thin contexts and 72 in thick contexts. Incoming Y-tail corners supply b, and do not carry the X-tail cut pair. The independent check explicitly asserts the X-tail value in each parity; it does not merely compare an unlabeled multiset. Strict final convexity puts a,b,c,d in (0,180), and a+b=72, c+d=216 are exact identities.

Every retained source endpoint remains a native corner of its receiving hexagon. Consequently common H has the six required numerical angle values (144,72,a,b,c,d), allowing coincidences. Its six native angles lie in (0,180) and sum 720.

## First angle gate: elementary proof and certified cross-check

The elementary replacement proposed by the root is VALID. Since a,b>0 and a+b=72, both a and b are strictly less than 72. If a!=b, the values a,b,72,144 are four DISTINCT native H angles and their sum is 288. The remaining two H angles are each less than 180, so the total is strictly less than 648, contradicting 720. Hence a=b=36 and Xt=Yt. No c,d constraints or finite classification are needed for this deduction.

The retained 406-branch equality-partition certificate independently corroborates the same conclusion. Any assignment of the six required labels to six H slots induces one of 203 equality partitions. At this order-free stage the slot names can be permuted freely; allowing different blocks accidentally to coincide only enlarges the domain. My verifier independently generates the 203 partitions by normalizing all maps from six labels to six slots, checks both strict signs of a-b, and validates all 406 exact contradictions. These certificates are supplementary evidence, not a dependency of the elementary proof.

## Unequal-cut pair invariance, order and geometry

For mark X, the local right triangle T,M,t is determined up to isometry by its mark-local offset and height and the unit source edge. Its two relevant rays point to T and M. The cut points on them depend only on r_(X,0) and r_(X,1). Therefore this local triangle together with the two cut points is congruent in every thin/thick and parity context, with T,M,t and the cut roles preserved. Changing the other four ray fractions or the neighboring internal donor geometry cannot alter this local pair.

Read the receiving half from retained source endpoint T toward M. Its boundary is T,c0,c1,M, so the two new angles have the same ORDERED values (s,t) in every X-tail context. A reflection of the local configuration preserves this role-defined order along that same boundary trace; it need not preserve a globally chosen clockwise direction. All prototype dihedral aliases are included later.

The external quad corner at the donor apex is the triangle angle theta=90-Xt, strictly between 0 and 90. Cutting that corner by an arbitrary chord removes a triangle with remaining base angles gamma,delta satisfying gamma+delta=180-theta. The new polygon angles are 180-gamma and 180-delta. Their sum is therefore 180+theta=270-Xt, strictly between 180 and 270. Equal distances, cyclicity of a cap, and equality of the two new angles are unnecessary. Admissibility guarantees the cut points really truncate this corner and that both resulting angles are strict.

After the first gate, a thin X-tail H has native cyclic triple (36,s,t), while a thick X-tail H has (72,s,t). Both are actual source contexts, verified in each parity. A 144 corner is also present in H because it occurs in a thin receiving context. It need not belong to this same source hexagon: all such polygons are hypothesized congruent to H.

## Second angle gate: complete elementary arc proof

Read the thin X-tail H to obtain cyclic triple (36,s,t). Congruence to the thick X-tail hexagon provides the cyclic triple (72,s,t), independently allowing either direction. Genuine convex-polygon isometries preserve the cyclic order or reverse it. Coincident large angle values are allowed. H also has a 144 angle and total 720.

The three OTHER angle slots besides one occurrence each of 36,72,144 sum to 468. Since each is less than 180, each is greater than 108. Thus 36 and 72 are unique native angle occurrences, and the other four angles are all greater than 108. The s,t pair cannot contain 36, because the thin triple already contains its unique occurrence; it cannot contain 72, because the thick triple already contains that unique occurrence. Therefore s,t>108. With s+t<270 this also gives s,t<162.

Remove the two unique small vertices from the cyclic six-angle word. The two intervening arcs contain four large angles, so their lengths, up to interchanging arcs, are (0,4), (1,3), or (2,2). Each small-predecessor triple must choose a direction whose arc starts with at least two large vertices. This accounts for all reflected and unreflected aliases without selecting a preferred prototype direction.

- For (0,4), both triples point into the long arc from opposite ends. Their two pairs occupy its four distinct slots. The total H angle sum is 108+2(s+t)<648, impossible.
- For (1,3), both triples point into the three-vertex arc from opposite ends. Its large-angle sequence must be (s,t,s). Let v<180 be the single other large angle. Then the H total is 108+(s+t)+s+v<108+270+162+180=720, impossible.
- For (2,2), if the triples use different arcs their pairs are disjoint, giving the same contradiction as (0,4). If they use the same arc, the ordered pairs are read in opposite directions, so s=t=q and q<135. The required 144 lies in the other arc, whose remaining angle is v<180. The H sum is 108+2q+144+v<108+270+144+180=702, impossible.

This proof is exhaustive even when some large angles coincide. It establishes the second angle gate without computation. I independently checked every arc case and each strict bound; no unresolved defect remains.

The retained 72-branch certificate is an independent exact cross-check: choose the thick 72 slot i, its direction epsilon, and a 144 slot k, impose hi=72, h_(i+epsilon)=h1, h_(i+2epsilon)=h2 with h0=36, and retain all 6*2*6 choices. The independently verified contradictions agree with the elementary arc proof. They are supplementary evidence, not required for the written theorem.

## Independent certificate verification

The retained [JSON certificate](../certificates/unequal-cap-minimal-angle-2026-10-15.json) contains exactly 478 unique cases: the complete 406+72 domain above. The separate [independent verifier](unequal-arrow-cut-angle-independent-2026-10-15.py) reconstructs all equalities and strict inequalities from the declared cases, with constant coefficients stored last rather than the producer's constant-first convention. It imports neither producer nor elimination routine and invokes no solver.

For an equality certificate the verifier computes the exact Fraction-weighted sum and checks that every variable coefficient vanishes and the constant is nonzero, contradicting equality to zero. For a strict certificate it checks every strict-row weight is nonnegative with at least one positive, adds arbitrary weighted equalities, and checks that all variable coefficients vanish and the constant is nonpositive. A positive combination of strictly positive affine rows must be strictly positive, so this is a genuine contradiction even when the constant is zero. All coefficient dimensions and domain records are checked.

Replay:

    mise exec -- conda run --no-capture-output -n arisearch python research/reviews/unequal-arrow-cut-angle-independent-2026-10-15.py

Observed result: PASS all sixteen actual arrow endpoint forms, all 203 equality partitions, all 406+72 weighted-row contradictions; 310 equality contradictions and 168 strict contradictions. This is a direct check of fixed finite evidence, with exact integer/Fraction arithmetic, no tolerances, sampling, timeouts, seeds or numerical rank decisions. It does not rely on the corroborating Z3 UNSAT gate.

## Further necessary angle restriction for changed cut rules

There is an additional deduction independent of mark-local cut-pair invariance. After a=b=36, a common receiving H has native values 36,72,144 and its other three angles are each greater than 108 by the total-angle argument above. Since c and d are also native H values and c+d=216, they cannot both be greater than 108. A value 36 would force the other to be 180, forbidden by strict convexity. Hence the smaller available alternative is 72, and the other is 144:

    {c,d}={72,144}, equivalently |Yt-Xh|=36.

Together with Xt=Yt this is a necessary restriction on the donor-triangle geometry even if the six cap fractions become source-context-dependent. It uses only unchanged retained endpoints, the mark-local normal-foot apex rule and the single-H requirement. It does not exclude the context-dependent-cut domain or prove that those conditions can be realized. An off-normal-foot rule must recompute the relevant source endpoint and triangle angle formulas rather than importing this restriction without checking them.

## Defects considered and final verdict

The abandoned 864-branch reduction assigned both a and b to X-tail contexts. That would be an invalid argument. I checked that the final proof does not reuse it: the first finite gate proves a=b before the single genuine X-tail pair is compared between thin and thick. The current 478-case certificate and independent verifier encode this corrected two-stage logic exclusively. The elementary replacements likewise first establish a=b, then compare only genuine X-tail contexts.

I also attacked coincident required angle values, arbitrary cyclic aliases, reflected H copies, unequal cut distances, source parity reversal, pair order reversal, missing 144 membership, strict versus weak inequalities, equality-only contradictions, and the possibility of an inadmissible cap geometry. The partition domain covers coincidences; the twelve aliases cover isometries; mark-local fractions preserve the external pair; the elementary four-angle and exhaustive arc arguments prove impossibility, with exact strict Farkas arithmetic independently confirming every branch; invalid partitions are already outside the candidate domain. No unresolved defect remains in the stated component theorem. I made no changes to the author's proof or certificate. After the author replaced both finite gates by the root's elementary proofs, I reread the exact rewritten artifact in full and again return VALID. The capacity argument, ordered-pair geometry and all three cyclic arc cases are correctly transcribed; the 478 cases are explicitly supplementary.

This is a scoped construction failure, not a positive construction or a global impossibility theorem. Genuine escape hypotheses include context-dependent external cuts, an off-normal-foot apex, changed source incidence, or abandoning the single-H-class requirement. The original two-polygon objective remains unresolved.
