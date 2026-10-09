# Necessary frequency balance for polygon tilings

**Status:** Proved necessary real-frequency conditions; repaired after
hostile review; independent re-review of the repaired version is pending.
Feasibility does not establish edge pairing, a plane tiling, or periodicity.

**Dependencies:** [the research problem](../../research-problem.md) supplies
the tiling convention; [side-count and monohedral obstructions](side-count-and-monohedral-obstructions.md)
supplies the uniform local and boundary count bounds.
[Hexagon limits](hexagon-limit-and-periodicity.md) supplies the defect-free
limit used in the final specialization.

**Review:** [frequency-balance review](../reviews/frequency-balance-review.md).

## Følner frequency-balance certificate

For any edge-to-edge tiling by fixed convex polygons \(P_q\), label every
native corner and side abstractly.  Along some square Følner subsequence there
are nonnegative per-area limits \(f_q\) for tile copies, \(v_t\) for labeled
vertex types, and \(e_p\) for labeled side-pair types satisfying

\[
 \sum_q \operatorname{area}(P_q)f_q=1,
\]

\[
 \sum_t v_t\operatorname{mult}_t(q,i)=f_q
 \quad\text{for every labeled corner }(q,i),
\]

\[
 \sum_p e_p\operatorname{mult}_p(q,j)=f_q
 \quad\text{for every labeled side }(q,j),
\]

and \(V-E+F=0\), where
\(V=\sum_tv_t\), \(E=\sum_pe_p\), and \(F=\sum_qf_q\).  Each vertex type has
angle sum exactly \(2\pi\); each side pair has equal lengths.  Endpoint
matching and placement parity may be retained as finite refinements.

To prove this, count centroid-anchored tiles and geometric vertices/edges in
\(Q_R\), divide by \(4R^2\), and extract a convergent subsequence.  Minimum
area, bounded diameter, and positive minimum corner angle give uniform count
bounds and finitely many labeled types.  Every incidence discrepancy lies in
an \(O(1)\)-width boundary strip and is \(O(R)\); area coverage and planar
Euler have the same vanishing boundary error.

For two hexagons in a defect-free limit, the finite necessary system reduces
to nonnegative variables on labeled corner triples summing to \(2\pi\), with
the twelve corner marginals above, plus equal-length side-pair variables.
This gives an exact finite rejection test for a specified pair.  It is only
necessary: frequencies are real, a globally present sparse type may have
zero limiting frequency, and the equations omit longer-range adjacency.
