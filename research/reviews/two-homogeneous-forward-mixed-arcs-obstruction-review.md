# Fresh hostile review: forward both mixed-homogeneous obstruction

Verdict: **VALID**, with no substantive defect or required author repair. This review independently checks the complete actual native-angle/capacity proof in `research/lemmas/two-homogeneous-forward-mixed-arcs-obstruction.md`. It does not certify the relative opposite arc ordering or central arcs.

Reviewer structural_audit did not develop the forward four-case obstruction. Root suggested the opposite-sign selection and some forward case ideas; branching_hexagons wrote that theorem. This review reconstructs those assertions independently and does not count either author's own check as a fresh review.

## Exact claim and assumptions

A has native lengths(p,q,p,q,p,q), threefold directions(0,60+delta,120,180+delta,240,300+delta),0<delta<30,p!=q. B is strictly convex closed, native lengths(p,p,p,q,q,q), and its indexed homogeneous arcs satisfy2alpha+beta=2chi+psi=360,alpha,chi!=120. Reflections and unrestricted partial contacts are allowed; a tiling may initially omit either species. Claim: this precise simultaneous forward ordering is untileable.

The proof imports the reviewed actual defect-free trivalent ETE limit for fixed convex hexagons. It then proves a contradiction in every actual ETE tiling, rather than identifying a locally inconsistent hypothetical angle inventory. A frequency or density is not assumed. The remaining inputs are direct whole-AA endpoint exclusions and uniform square-window O(R) estimates for fixed shapes.

## Independent reconstruction and adversarial tests

1. **Length normalization and omission.** Each homogeneous relation forces its repeated angle into(90,180). The native p-chain has unit sum1+2i sin(alpha), and the analogous q-chain has the chi value. Since sin strictly decreases on that interval, distinct p,q forcealpha!=chi. Beginning B at oldside3 swaps the two complete forward homogeneous arcs. For A, reflecting and taking old edges(1,0,5,4,3,2), then rotating, produces exactly the same A(delta) directed-edge list with lengths exchanged; its new even native corners remain H. This independently confirms the allowed x=alpha>y=chi normalization, rather than changing delta or assuming an unoriented label symmetry.

   Whole-AA seams require120 or the unordered low/high paired arc at the two opposite endpoint fillers. Neither noncentral mixed homogeneous arc satisfies those conditions. Thus each A vertex has precisely one A, one B mixed and one B homogeneous sector. It gives6N_A<=2N_B+O(R). Direct pure/nonpure native inventories giveN_A=N_B-Yp-Yq+O(R) andM_beta+M_psi=N_B+N_A+O(R). The reviewed singleton forcing puts both these slot counts on A. HenceN_B<=5N_A+O(R), independently establishing the1/5 lower bound even if its separately accepted strengthening were omitted from the import list. Positive minimum tile area and bounded diameter yield totalOmega(R²); both species must then occur quadratically. No step quietly assumes both were initially present.

2. **Actual opposite-sign selection.** Each singleton sign set is nonempty, and absence of an opposite pair is equivalent to both sets being the same one-element sign set. This includes the possibility that either singleton has two available filler signs. A single A sign contains only3N_A corners, whereas singleton occurrences totalN_B+N_A+O(R). Thus failure of an opposite pair would forceN_A>=N_B/2-O(R), contradictingN_A<=N_B/3+O(R). This is an actual-count selection argument, not an assertion that every angle-legal star occurs.

3. **Exhaustive local possibilities.** A separate no-author-import checker reconstructs all1664 oriented native-corner triples with matching binary radial lengths, including both mirrors and repeated species/slot choices. Each repeated homogeneous slot has exactly four A filler possibilities(H/L with u/v) and three B-only filler possibilities(uu,uv,vv). With AA excluded, there is no missing second A corner or one-mixed parity case. The checker rederives every repeated-slot A sum and B-only residual, not just the four selected singleton equations.

4. **Cases F1/G1 and F2/G2.** The difference2(x-y) fixes the selected high/low order and forcesd=delta. In case1,v120 and both repeated angles below120 make every B-only repeated sum less than360. The only possibly matching A repeated equation requiresh=delta. Independently,-rho'(a)=2c/(5-4c²)<1/4 for c=-cos(a) in(0,1/2), since5-4c²-8c=(1-2c)(5+2c)>0. Mean value givesh<delta/4, eliminating it strictly.

   Case2 hasu120 and repeated angles above120; all B-only sums exceed360. The only repeated A star requiresh=delta. This exceptional phase cannot be discarded as nongeneric: the manuscript retains it and the independent checker verifiesbeta onlyH,psi onlyL,repeatx no nonpure star,repeaty onlyL. Therefore3N_A=M_beta=N_B/2+O(R), forcingN_A=N_B/6+O(R) and contradicting the actual1/5 lower bound. No inference is made from a failed metric solution or finite search.

5. **Cases F1/G2 and F2/G1.** Opposite target signs implyx+y240. Withx120+z,y120-z,h>0, all six B-only repeated residuals are strictly nonzero. In F1/G2,delta3z+h makes every repeated A offset strictly smaller than the target in absolute value; there is no equality resonance. In F2/G1 the initially possible reversed high/low order is resolved by the actual phase, not assumed. Direct tangent subtraction ofrho(120-z)-rho(120+z) gives tanh=sinz/(2cos²z). On0<z<30 both phases are in(0,90), tanh/tanz=1/(2cosz)<1, and tanh/tan(z/2)=(1+cosz)/(2cos²z)>1, since1+cosz-2cos²z=(1-cosz)(1+2cosz)>0. Thusz/2<h<z, selecteddelta=z-h>0, and possibleh=delta would require the excluded boundaryh=z/2. Both repeated counts vanish in each case, givingYp=Yq=N_B/2+O(R),N_A=O(R), contradicting the lower bound.

## Boundary, compactness and quantifiers

All integer inventories permit O(R) errors for each fixed pair, with constants independent of square center and large R. Corners, tiles and side events associated differently can disagree only in a fixed-width boundary band; positive minimum tile area bounds its tile count by O(R). Fixed-shape constants need not be uniform as the geometric parameters approach the domain boundary. Quadratic total count is enough for every contradiction. No limiting frequency, ergodicity, use of every prototile in the original tiling, or pointwise conclusion from an average is required.

The imported compactness theorem produces an actual admitted ETE tiling even when the original contacts are not ETE. All subsequent AA exclusions, singleton forcing, sign selection and endpoint incidence are performed in that actual limit. The source does not assume the selected four-case equations necessarily occur in the original partial-contact tiling.

Independent verifier:

    conda run --no-capture-output -n arisearch python research/reviews/verify_two_homogeneous_forward_obstruction_independent.py

Result: **PASS** all1664 raw oriented binary-compatible native stars; all native repeated-slot fillers; exact length-swap reflection; all four selected cover equations and signs; derivative/tangent factors; specialh=delta sign capacities; count eliminations. The verifier imports no author modules, retained producers or certificates. Analytic interval signs and the unbounded boundary/compactness implications were also audited in prose above.

Remaining uncertainty: none within this scoped obstruction. Opposite relative ordering and central homogeneous arcs remain separate problems. The theorem is partial research and does not resolve the unrestricted two-convex-prototile target.
