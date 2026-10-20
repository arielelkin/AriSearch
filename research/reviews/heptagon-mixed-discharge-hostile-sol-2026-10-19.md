# Independent hostile review: mixed-Q7 PP-degree discharge

Date: 2026-10-19. **Verdict: valid**, within the stated necessary-incidence and translated-purification scope. This is not a periodicity theorem or a solution of research-problem.md.

## Exact claim and dependencies

Reviewed research/searches/heptagon-mixed-discharge-sol-2026-10-19.md and its Python/JSON artifacts against research-problem.md, research-protocol.md, the reviewed complementary-angle necessary theorem, and the 21:22 strategic assessment. Fix unit regular P5 and a strictly convex Q7 with cyclic word ABBCCBC, ABBCCCB, ABCBBCC, or ACBBBCC, with A=144 degrees, B=alpha, C=252-alpha, and 108<alpha<126. Assume the two fixed polygons tile with unrestricted contacts and isometries.

The claim is: PP-degree two is impossible locally; PP-degree zero has O(R) count in large square windows; after translation and a subsequential limit, the same pair admits a BBB-free tiling in which every P has exactly one PP neighbor. The finite incidence relaxation has an exact nonnegative charge certificate and feasible rational flows, without claiming those flows are realizable tilings.

The full-edge/trivalent star theorem is a dependency. Its relevant assertions were rechecked: native angles lie between 108 and 180 degrees, so a corner-in-side contact cannot fill the remaining straight angle, two corners cannot fill 360 degrees, and four exceed it. The only stars are PPA, PBC and, at alpha=120, BBB. Full-edge contacts mean that one P side has one fixed Q neighbor along its whole length. This last fact is essential to the proof.

## Independent local proof and attacks

At a PPA corner the two P copies meet along exactly one incident PP edge; at a PBC corner neither incident P edge faces P. Thus adjacent PP sides on one P are impossible. An independent subset of the five-cycle has size at most two. Any independent pair of its edges is separated on one side by exactly one other edge. That intervening edge is PQ, and both its endpoints are PPA. At either endpoint the Q angle must be A. Because the PQ contact is full-edge, these two angles belong to the same Q side. Q has only one A vertex and hence no AA side. Contradiction.

Reflections do not alter physical endpoint labels. A rotation or reflection cannot make the two endpoints of a nondegenerate Q side be its same unique A vertex. No chirality choice or BB/CC matching assumption enters this argument. It actually applies to every balanced Q7 word with a single A, rather than only the four mixed survivors.

At alpha=120 this pointwise proof still holds in the original tiling: every vertex involving P is PPA or PBC, while BBB has no P. The producer incorporated this strengthening during review: there are zero degree-two pentagons, rather than merely O(R) possible exceptions near BBB. There is no resonant counterexample to the local proof.

## Conservation and the exact dual

For a BBB-free tiling the six non-A Q vertices form a path with a unique QQ perfect matching. Hence Q sides 1,3,5 face Q and 0,2,4,6 face P. Give the four PQ slots respective weights -1/5, 1/5, 1/5, -1/5. Their sum on Q is zero. If P has k PP sides, it has 5-k PQ sides and 2k A endpoints on those sides. Its received charge is [(5-k)-4k]/5=1-k. The independent local result gives k in {0,1}, so the charge is precisely the nonnegative indicator of k=0. This is an exact linear combination of PQ incidence equations and nonnegative type counts; no floating-point optimum is needed.

Summing over a square leaves only bounded-distance boundary terms. Fixed tile diameter D and positive minimum tile area bound the number of tiles meeting a fixed-width boundary strip by O(R+1), uniformly over translated windows. Therefore n0=O(R+1). Equivalently, PPA and PBC incidence counting gives p=q+O(R), total PP degree=q+O(R), and n0-n2=O(R). Since n2=0, the same conclusion follows directly.

At resonance balanced B/C counting gives 3z=O(R), where z counts BBB stars. Each BBB star touches only finitely many Q copies. Consequently fixed-radius neighborhoods of their tiles have area O_r(R). One may first take the previously reviewed BBB-free translation limit and then apply the charge. Alternatively the global degree ledger still gives n0=O(R) directly because its errors include only the O(R) BBB budget. Both routes justify the claimed reduction.

## Complete finite domain and reflection audit

The P-side domain lists all independent PP subsets of C5 (one empty, five singleton, five doubletons). Every remaining side independently takes one of four PQ native slots and either reflection parity. Reading its endpoint labels in the two opposite orders exhausts the isometries relevant to native incidence. PPA and PBC endpoint tests impose exactly the stated local requirements. It is legitimate to start from degree at most two: this was proved from the star list before enumeration. It is also legitimate to use the fixed PQ slot set only after removing BBB.

The PP descriptor involution reverses its two endpoints and replaces each adjacent Q slot s by 6-s, preserving that Q's reflection parity. This operation is valid here because a descriptor at PP touches A, so s is necessarily 0 or 6. These are the two sides of the same Q incident at its A corner. The operation is not an unjustified reversal of an arbitrary asymmetric Q word.

The QQ domain checks all three QQ slots against all three slots, with both independent parity choices. Equal physical boundary orientation reverses endpoint order, whereas opposite native parity preserves it. The endpoint test is exactly B/C complementation. It retains both BB-to-CC parity choices and the permissible BC self pairs. No unproved common chirality is imposed.

The implemented LP includes PQ and PP balances. QQ balances are supplied by an explicit exact completion: for each parity r, pair BB with CC at weight q_r and pair the remaining BC slot with itself at weight q_r/2. Such a self slot consumes two incidences; it represents a frequency pairing of different Q copies, not a polygon glued to itself in the plane. These checks prove that eliminating QQ variables does not restrict the remaining incidence cone. The listed QQ domain includes cross-parity states even though the chosen feasible completion need not use them.

This is a complete enumeration of the stated local necessary relaxation, not a characterization of geometric neighborhoods or plane tilings. Its finite flow may omit metric compatibility, overlap exclusion, and distant consistency; all are explicitly outside its claim. Omitting those constraints only enlarges the cone and cannot invalidate the nonnegative upper bound.

## Replay and defects

Replayed the latest producer script using:

    mise exec -- conda run --no-capture-output -n arisearch python research/searches/heptagon-mixed-discharge-sol-2026-10-19.py

It returned P-type counts 104,82,104,82 and exact n=(0,1,0) for the four words in the stated order. Fraction checks verified every retained LP equality, nonnegative rational support, QQ completion, the local charge formula, and the zero total Q charge. The rational reconstruction step would fail an exact assertion rather than silently accept an inaccurate float.

An earlier working script merely listed QQ seam types without checking their balances. The final artifact repairs this with the explicit rational completion just audited. This procedural defect did not affect the elementary dual proof. No unresolved mathematical defect was found in the final stated claim. The producer has incorporated the resonance strengthening above; it is independently justified by the same local proof.

## Compactness and remaining uncertainty

For a fixed radius r, the O(R) defective tiles have O_r(R) total neighborhood area, while a large square has Theta(R squared) area. Thus a radius-r disk avoiding every defect exists. Translating centers of progressively larger clean disks to the origin gives tilings by the same fixed shapes. Polygon positions and orientations have convergent subsequences locally; fixed positive area bounds local tile counts. Alternatively, anchor one tile and use the finite side-matching choices to diagonalize exact finite neighborhoods. The limit covers the plane, has disjoint interiors, and has no forbidden local star or degree-zero P. Every P therefore belongs to a full-edge PP dimer. At resonance the same extraction removes BBB first, or removes both defect sets together.

The extraction does not prove the original tiling itself has no degree-zero tiles. It does not prove dimer axes align, reflected seams return, a finite quotient exists, or any translational period occurs. Positive rational incidence flows do not prove plane existence. A global mechanism connecting the PP matching and QQ seam graph is still required for periodicity or an obstruction. These distinctions agree with the producer's stopping statement and with the 21:22 assessment. The four mixed words remain unresolved for the original aperiodicity objective.
