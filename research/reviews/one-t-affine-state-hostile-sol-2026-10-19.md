# Independent hostile review: first-cut exact affine-state gate

2026-10-19. Target: `../searches/one-t-affine-state-gate-sol-2026-10-19.{md,py,json}`. **PASS for the stated fixed-cut computation, sufficient merge theorem, and immediate stop.** This is not a feasibility/infeasibility result for a full parent or any of the 48 parent-map pairs. No construction was resumed, and no source, discovery-log, or Git operation was performed by the reviewer.

## Independently reconstructed finite domain and cut

The source SHA256 matches the report and JSON:
`33d0b6da814916e886daa93daee3b095519749120e42b0eaabfe6e84e550a47b`.
The selected input is precisely P-parent map0. I reconstructed native child words from `expanded_words`, removing the flat node f5 only from host a0. This reproduces `corner_words` exactly, including all other occurrences of f5. The host is Q, with seven native incidences; its expanded boundary has the extra flat incidence. The map has thirteen children, eleven P and two Q, with exactly five/seven native incidences per P/Q child.

Independent enumeration used subsets by cardinality and `itertools.combinations`, rather than the source bitmask loop. It exhausted Σ_(k=1)^12 binomial(13,k)=8190 subsets. For each cut I independently counted nodes whose native incidence list meets both parts and computed the raw assigned-domain product. The minimum lexicographic score is exactly (3,10,1,('e0',)); it uses the report's declared ordering of separator size, raw domain, child count, and assigned tuple. The chosen unfinished nodes are f16,t0,t1; the completed nodes are u1,u2; the remaining child list agrees exactly with the certificate.

This verifies the minimum for the stated **native-incidence cut criterion**, not a geometric separator claim or a claim that this cut maximizes compression. The T host's flat sector is fixed rather than a native angle variable, so excluding it from native incidence counting is correct.

## Exact state equivalence, including unfinished incidences

For a fixed assigned set, completed-node affine equations plus polygon sums are sufficient summaries of past completed equations. Equality of their augmented rational row spaces implies equality of their simultaneous affine solution sets. This statement is collective: individual completed-node rows need not agree. The report's argument is valid when read in that collective sense.

At each unfinished node the state retains **every identified assigned native incidence**, including child identity, native position, and shared coordinate index. The fixed map retains all unassigned incidence positions. Therefore any identical suffix assignment produces identical remaining contributions and identical full rows at these nodes. Untouched rows depend only on the suffix. Fixed parent-coordinate subtraction and the transition/T right sides are unchanged in both prefixes. Adjoining these future rows to identical past affine solution sets preserves equality, and intersection with the identical open box preserves equality again. Keeping one representative prefix is therefore valid for future angle-witness reconstruction.

I checked that the actual state key contains the remaining child tuple, all of these identified unfinished incidence records, and the full thirteen-column augmented RREF. The unchanged remaining dihedral domains are determined by that child tuple and fixed map. JSON entries retain all ten representative assignments, their incidence records, and their RREFs. No coincidence quotient or separator aggregate replaces individual incidences.

Full augmented RREF, including possible RHS pivots, is a sufficient canonical row-space representation even for inconsistent systems. Two distinct inconsistent row spaces could both describe the empty solution set, so this is not a minimal semantic representation; the report only claims a sufficient merge condition. Likewise, coordinate equalities implied by past rows might permit extra merges under a stronger representation. The negative result here does not reject those stronger representations.

## Ten branches, ten states, and exact partial feasibility

The retained assignments are exactly every (p,ε)∈{0,…,4}×{−1,+1} on e0, each once. Its native word is [t0,u1,u2,t1,f16]. The unfinished indices at t0,t1,f16 are p,p+3ε,p+4ε modulo five. If two such records agree, t0 gives identical p, and t1 gives 3(ε−ε')=0 modulo five. Opposite signs would give ±6, nonzero modulo five, so ε also agrees. Thus the unfinished records alone separate all ten states, independently of RREF implementation. Maximum multiplicity one and zero merging follow.

For every branch I reconstructed the completed rows independently, recomputed their augmented RREF with SymPy rather than the implementer's Fraction elimination routine, and compared every rational entry to JSON. All match. I also checked the certificate a=(3/5 repeated five times,5/7 repeated seven times) against each raw row using Fraction arithmetic. It satisfies every strict bound, both polygon sums, and the completed u1,u2 equations. Those equations identify the child coordinate with the fixed corresponding P-parent coordinate. This is exactly **partial** feasibility; no transition or T equation has completed at this cut, and the constant vector need not satisfy future rows.

## Replay and declared stop

Both checks passed under the prescribed wrapper:

    mise exec -- conda run --no-capture-output -n arisearch python research/searches/one-t-affine-state-gate-sol-2026-10-19.py --check
    mise exec -- conda run --no-capture-output -n arisearch python research/reviews/verify_one_t_affine_state_hostile_sol_2026_10_19.py

The independent verifier retains the reconstruction, combinations-based cut enumeration, SymPy RREF comparison, complete branch-domain check, and Fraction witness check. No solver or strict-feasibility relaxation was introduced. The supplied elapsed runtime is historical metadata; current replays also complete far below the declared 180-second cap.

The implementation computes all cuts to select the declared one and then traverses only that single child's ten assignments. It does not traverse an alternative cut, add a second child, or retry the prior SMT system. The certificate expressly sets `full_parent_cover=false` and `shared_parent_witness=false`. The report correctly stops because this exact first-cut representation produces no nontrivial compression. No map-pair exclusion, complete feasible-region cover, shared full angle witness, metric realization, plane extension, or aperiodicity conclusion follows. No blocking defect or correction required.
