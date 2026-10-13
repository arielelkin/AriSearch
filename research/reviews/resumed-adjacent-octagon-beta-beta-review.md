# Independent hostile review: necessary alpha-alpha/beta-beta equality

Date:2026-10-13. Claim reviewed: stronger metric escape in research/searches/resumed-higher-partner.md. P has five108° corners; Q has adjacent108° corners and six144° corners. If Q's108–108 side length differs from each144–144 Q side length, then no plane tiling exists. No privacy from P or108–144 Q sides assumed.

Assumptions checked: genuine strict corners, all-obtuse edge forcing and trivalent stars, whole-side matching under rotations/reflections, bounded diameters, positive inradii, no density-limit assumption, omitted-species allowance.

Every Q has at least two QQ sides: if e meets P, both flanking sides meet the beta-Q sectors; if e meets AA Q, both flanking sides meet third Qs; if e meets AB Q, one AA endpoint forces a third-Q neighbour. BB mating is excluded by the actual metric hypothesis. Every P has at least three PQ sides by the five-cycle independent-set argument. Thus dP=PQdegree−3 and dQ=QQdegree−2 are nonnegative pointwise. Summing within a square gives sum(dP)+sum(dQ)=6NQ−3NP+O(R)=O(R), using the independently checked corner ratio NP=2NQ+O(R). Consequently positive-deficit tiles number O(R), uniformly even if no frequencies exist.

I attacked the claimed bounded-distance bad-tile association in all three cases:

1. P mate of e: that P's e-side and both adjacent sides meet Q; the other two neighbour slots are adjacent, so at most one is P. It has at least four PQ sides and dP≥1.
2. AA Q mate: the original Q has e and both flanking sides QQ. The neighbours cannot repeat by convex intersection, so dQ≥1.
3. AB Q mate: at the AA endpoint the third Q supplies beta and has two QQ sides incident with its beta corner. Each of its two alpha corners requires at least one incident QQ side, since its star must contain a different beta-Q. Two sides incident with a beta corner can cover at most one of adjacent alpha corners in the native eight-cycle. Therefore an additional QQ side exists and dQ≥1.

Reflections exchange endpoint correspondences but do not change that one AB mate endpoint is AA. A third Q cannot merge with either initial Q because three disjoint sectors occur at the star. Repeated placed neighbours across distinct native sides are impossible by positive-area convex intersection. The beta-Q argument is combinatorial and does not assume a chosen chain ordering.

Each initial Q associates to a bad tile at uniformly bounded distance: their anchors differ by at most a fixed multiple of maximum diameter. Disjoint inscribed disks bound how many Q anchors can associate to one bad anchor by a uniform constant. A square boundary enlargement changes counts only by O(R). Hence NQ=O(R), NP=O(R), contradicting plane coverage with bounded tile areas. This is valid finite-window reasoning, not measure selection or an unproved recurrence assumption.

Counterexamples attempted: shared e-length on P; multiple AB mate slots; flipped AB mate; degree2 Q with an incident beta QQ pair and both alpha corners somehow covered by those same sides; species omission; zero-density defects. All are explicitly discharged by the above argument. No unaddressed degeneracy survives genuine convexity.

No repair needed. The exact tangential fixture was independently verified in the earlier review script research/reviews/resumed-higher-partner-fixture-check.py; this stronger proof itself uses no computational result. The older fixture's P side length was subsequently changed from2t+1 to2u; neither case changes the support-line Q or this proof.

Verdict: **VALID** for the complete stated family. Any actually tileable pair in this angle system must have Q's AA side equal in length to at least one BB side. This is solely necessary: no infinite covering, decoder, or aperiodicity follows from that equality. No novelty claim is assessed.
