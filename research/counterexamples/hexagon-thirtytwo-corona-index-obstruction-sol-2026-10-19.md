# Exact IFT family fails formal-corona realization by a corner-index shift

Status: **Proved internally**, with exact finite replay; independent hostile review pending. This audits the exact metric family of `research/lemmas/hexagon-thirtytwo-star-analytic-metric-sol-2026-10-19.md`, not every possible metric with the same edge words.

## Claim

For all sufficiently small nonzero real t on that analytic IFT branch, none of the 32 signed stars in the forced-dimer builder is geometrically angle-compatible. Consequently none of its 100 formal AA-dimer coronas, including corona 59, is realized by this branch. Nonoverlap need not be examined: the necessary angle gate already fails. The metric closure and strict convexity assertions themselves are not contradicted.

## Indexing and proof

Let geometric vertices be v_j, with side j directed from v_j to v_(j+1). The metric construction uses side directions phi_0=0 and phi_j=sum_(k=1)^j(pi-theta_k). Thus the interior angle at v_j is theta_j, between sides j-1 and j.

The formal builder instead defines the two incident sides of port (c,+) as (c,c+1), with their order reversed at handedness minus. Within either polygon its corner c therefore has actual metric angle theta_(c+1), with subscripts modulo six. Reflection does not alter this angle. A signed formal star with ports c_1,c_2,c_3 requires the sum of these three shifted angles to be 2pi.

Write d_j=theta_j'(0), independently reconstructed in the replay from the exact IFT Jacobian. All angles at t=0 are 2pi/3, so the residual at zero is zero. For the four unsigned stars retained by the support, the actual shifted triples and residual derivatives are:

| Formal angle indices | Actual metric indices | Residual derivative |
| --- | --- | --- |
| 0,1,8 | 1,2,9 | (1+3 sqrt(3))/4 |
| 2,7,11 | 3,8,6 | -2-sqrt(3) |
| 3,6,10 | 4,7,11 | 3+2 sqrt(3) |
| 4,5,9 | 5,0,10 | -(5+7 sqrt(3))/4 |

Every derivative is nonzero. Moreover the replay checks all 32 signed stars, and every actual shifted residual derivative is nonzero in Q(sqrt(3)). If an analytic residual R obeys R(0)=0 and R'(0) != 0, then R(t)/t tends to a nonzero number, so R(t) != 0 on a punctured neighborhood of zero. Intersect the finitely many neighborhoods. None of the 32 stars is angle-compatible there. Every builder corona uses these stars by construction, proving the claim for all 100 coronas without a geometric overlap search or further enumeration.

## Exact replay and scope

`mise exec -- conda run --no-capture-output -n arisearch python research/searches/hexagon-thirtytwo-corona-index-obstruction-sol-2026-10-19.py`

The replay rebuilds the fixed 32-star/100-corona atlas and reconstructs the IFT tangent using SymPy exact symbolic arithmetic. It performs no solver search, random sampling, numerical sign test, or tolerance comparison. Its retained certificate is `research/certificates/hexagon-thirtytwo-corona-index-obstruction-sol-2026-10-19.json`. There are no timeouts or random seeds. The only equivalences are the cyclic star canonicalization already present in the builder. It checks all signed stars, including both handednesses.

The prior metric construction enforces unshifted support equations; these hold as equations in its chosen coordinates, but they are not the geometric corner equations of the builder for that edge-word convention. A new IFT construction enforcing shifted support equations would be a materially changed mechanism and is not ruled out here. Relabeling both angles and edge words consistently also changes the comparison and must be audited afresh. No unrestricted plane-tiling or aperiodicity statement follows.

Protocol 5 stopping state: the specific given IFT branch is falsified as a realization of the retained formal support and all builder coronas near t=0. Stop this branch. Reopen only with a corrected, consistently indexed metric construction or another explicit family; enlarging the corona search on this branch cannot repair its angle defect.
