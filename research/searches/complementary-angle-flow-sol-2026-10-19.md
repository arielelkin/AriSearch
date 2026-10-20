# Complementary-angle conservation: complete first global gate

Date: 2026-10-19. Status: internally checked analytic necessary theorem and exact finite word enumeration; independent hostile review pending. No novelty claim. No plane existence or general periodicity theorem is asserted. Scope: P is the unit regular pentagon; Q is fixed strictly convex with angles A=144°, B=alpha, C=252°−alpha, 108°<alpha<126°. Reflections and unrestricted contacts and omission are allowed. The closed alpha=126° case is not used or reopened.

## 1. Complete stars, including omission

Local finiteness follows by bounding diameters by D and areas below by s>0: tiles meeting compact K lie inside its D-enlargement and have disjoint interiors. At a corner lying in another tile's open side, the remaining 180° cannot be filled by one native corner (each <180°) or two (each >=108°). Partial contacts therefore cannot occur; sides meet full sides. Exactly three corners meet since two sum to <360° and four to >360°. This argument does not assume either tile occurs.

For completeness every unordered triple of {P,A,B,C} is tested symbolically by the retained script, using angle pairs (constant, alpha coefficient)=(108,0),(144,0),(0,1),(252,−1). Identically 360° triples are precisely PPA and PBC. Solving every nonconstant triple equation and intersecting with the open alpha interval yields exactly BBB at alpha=120°. Thus generically P alone and Q alone are impossible. At resonance P alone remains impossible, but Q alone is possible at the star level and is preserved below.

## 2. Uniform square-window estimates, without density assumptions

Use S_R=[0,R]^2, and an arbitrary fixed interior reference point transported with each tile. Counts p_R,q_R refer to references in S_R; vertex counts refer to vertices in S_R. Put N=max(5,n), M=max tile area, s=min tile area, D=max tile diameter. A tile meeting the width-w neighborhood of the square boundary lies wholly in its width-(w+D) neighborhood. That neighborhood has area at most 8(w+D)R+4(w+D)^2 (the same upper bound follows from outer and inner concentric squares). Hence at most [8(w+D)R+4(w+D)^2]/s tiles meet it. Each contributes at most N incidences. All discrepancies below have some fixed w<=4D and hence an explicit bound by a fixed multiple of N[40DR+100D²]/s. Constants may depend on the fixed Q, but are uniform over placements, windows and tilings. No uniformity as Q degenerates or alpha approaches an endpoint is claimed.

Let x_R,y_R,z_R count PPA,PBC,BBB vertices respectively, with z_R=0 off resonance. Incidence counting gives

    x_R=a q_R+O(R+1),  y_R=c q_R+O(R+1),
    b q_R=y_R+3z_R+O(R+1),
    5p_R=2x_R+y_R+O(R+1).

Consequently

    5p_R=(2a+c)q_R+O(R+1),
    (b−c)q_R=3z_R+O(R+1).                 (1)

Coverage supplies R² <= M[p_R+q_R+O(R+1)]: tiles covering S_R have references in its D-enlargement, and those references outside S_R belong to the bounded boundary strip. Combining with (1) gives q_R=Omega(R²) for all sufficiently large R, with constants depending only on P,Q. Thus no division by an assumed density is necessary. Off resonance b=c. At resonance b>=c, since b<c and z_R>=0 would give q_R=O(R+1), contradicting coverage. This also handles omission: if Q is absent, (1) makes p_R=O(R), impossible; if P is absent at resonance, actual stars force a=c=0 and all Q corners B.

The polygon angle identity is 36a+(180−alpha)b+(alpha−72)c=360. Generically b=c reduces it to a+3b=10, giving precisely

    (a,b,c,n)=(10,0,0,10),(7,1,1,9),(4,2,2,8),(1,3,3,7).

At resonance divide the angle sum by12: 3a+5b+4c=30. Together with b>=c the complete inventory is

| a | b | c | n | (2a+c)/5 |
|---|---|---|---|---|
|0|6|0|6|0|
|1|3|3|7|1|
|2|4|1|7|1|
|4|2|2|8|2|
|5|3|0|8|2|
|7|1|1|9|3|
|10|0|0|10|4|

Completeness follows by 0<=a<=10, 0<=b<=6, 0<=c<=7 and substitution in the displayed integer equation, which the exact script exhausts.

## 3. Reflection-aware edge rules

At A both adjacent Q sides face P and have unit length. At a generic B or C, precisely one adjacent side faces Q. Hence QQ edges form a perfect matching on non-A vertices in their cyclic boundary graph. Every non-A run has even length and its path matching is unique. All other Q sides have length one. On a QQ edge each physical endpoint has one B and one C corner. Accordingly BB edges can face only CC edges, and BC only BC; matching lengths are necessary. If directed boundary orders are chosen consistently counterclockwise in the plane, endpoint matching reverses order and complements letters. A reflected copy reverses its native boundary order, so the invariant statement uses physical endpoints, not a fixed native orientation. BB↔CC and BC↔BC hold for both parities. This does not force a unique successor, chirality, or global arrow. For any balanced perfect matching, BB and CC edge counts are equal already by counting B and C endpoints.

At resonance a B at a PBC vertex still has one QQ side and faces C across its QQ endpoint; a B at BBB has two QQ sides, and faces B across either. C always has one QQ side and faces B. Thus CC edges can face BB only, BC edges can face BC or BB, and BB can face CC, BC or BB, subject to the endpoint conditions just stated. In particular the generic complement rule MUST NOT be imposed at BBB endpoints. Every side touching A still faces P. Let t(T) be the number of B corners of a Q copy T assigned BBB. A cyclic QQ-edge subset then has degrees 0 at A, 1 at C, and 1 or2 at B, and t(T) counts degree2 vertices. These local conditions are necessary, not a realizability certificate.

## 4. AA capacity and the extra resonance branch budget

At every P corner the stars PPA/PBC persist even at resonance. PP sides cannot be consecutive, so a P has at most two PP sides. A PQ side opposite an AA side is flanked by PP sides. In a five-cycle a nonconsecutive pair of PP sides flanks at most one intervening side. Thus every physical P receives at most one AA side, including repeated-neighbor and reflected placements. If m is the number of AA sides of Q,

    m q_R <= p_R+O(R+1),
    [5m−(2a+c)]q_R <= O(R+1).

Hence m <= (2a+c)/5. If this fails, q_R=O(R), and (1) and coverage give a contradiction. At resonance an equivalent formula explicitly recording the branching source is

    m q_R <= [2a+(b+c)/2]q_R/5 −3z_R/10 +O(R+1).    (2)

Indeed y_R=[(b+c)q_R−3z_R]/2+O(R). The negative source correction is essential; the symmetric palette's old P/Q ratio cannot be reused.

Counting BBB incidences per tile also gives

    sum_{reference(T) in S_R} t(T)=3z_R+O(R+1)
                               =(b−c)q_R+O(R+1).   (3)

For a fixed word let t_min,t_max range over all allowed cyclic edge subsets. Necessarily t_min<=b−c<=t_max. Any strict violation again gives q_R=O(R), then contradicts coverage. This adds a global obstruction beyond AA capacity.

## 5. Complete survivor table for this gate

All words below are up to rotation and reflection; B and C are NOT interchangeable in taking dihedral representatives. The script enumerates every labeled multiset word, canonicalizes under the dihedral group, then exhausts all 2^n cyclic QQ subsets. It applies AA capacity and (3). These are necessary survivors, not metric or plane extensions.

Generic alpha (including every real value other than120 in the open interval):

* n=7: ABBBCCC, ABBCBCC, ABBCCBC, ABBCCCB, ABCBBCC, ABCBCBC, ABCBCCB, ABCCBBC, ACBBBCC, ACBBCBC. Each has m=0 and its unique matching pairs the six-letter run consecutively.
* n=8: AAABBACC, AAABCABC, AAABCACB, AAACBABC, AABBAACC, AABCAABC, AABCAACB. Each has m=2. The four non-A corners form two runs of length2, paired within runs.
* n=9,10: none. The two non-A vertices of n9 must be adjacent, giving m=6>3; all-A n10 gives m=10>4.

For n8, one run of4 gives m=3>2 and is excluded. The remaining run lengths2+2 leave A-run lengths3+1 or2+2. Assigning two B and two C across those pairs gives exactly the seven listed dihedral classes. Thus no unlisted cyclic word survives the combinatorial gate.

At alpha120, the same ten balanced heptagon words and seven balanced octagon words survive. Additional survivors are:

* (a,b,c)=(2,4,1), only AABBBBC;
* (0,6,0), BBBBBB, necessarily Q-only in any actual tiling.

Here is a direct global exclusion of the other (2,4,1) words. Non-A runs cannot have length1, because their vertex would have QQ degree0. If the two A's are separated, the five non-A vertices split as2+3; only one vertex can have QQ degree2, giving t_max<=1<3=b−c. If the A's are adjacent there is a run of5. Three degree2 vertices are possible only when all three interior letters are B; the lone C must be an endpoint. This is exactly AABBBBC up to reversal. Every other locally admissible word has t_max<=1, while the remaining words have no allowed cyclic QQ subset; (3) excludes all of them. For AABBBBC its local t values are1,3. Equation (3) forces the number of t=1 copies in any square to be O(R+1), but DOES NOT prove that no such copies occur. The saturated t=3 assignment uses all four sides within the BBBBC run as QQ edges; its three interior B corners are BBB.

For (5,3,0), a non-A run has length at least2, so all three B's lie in one run. The remaining A-run contributes m=4>2; it is excluded. The n9,n10 exclusions persist. For balanced n7, t can be0 or2 on some words, and (3) bounds the number of t=2 copies by O(R); it does not imply pointwise absence of BBB. Balanced n8 survivors have only length2 non-A runs, so t=0 for every copy and BBB is absent exactly.

For BBBBBB, a=c=0 and no P-containing star exists, so P cannot occur even sparsely. Every vertex is BBB, every side QQ, t=6. Q is an equiangular120° hexagon. No claim is made that every such metric hexagon tiles: establishing tilability or a periodic witness requires an applicable monohedral theorem with its hypotheses checked or a direct carrier. The present branch is preserved, not silently omitted or declared tileable.

## 6. Stopping point and exact remaining gap

The parameter-wide exclusion of all generic unbalanced inventories, all n9/n10, the n8 one-run words, and four of the five local (2,4,1) resonant words is proved by uniform global counts. The surviving table is a precise necessary theorem. Endpoint rules, matching lengths and branch budgets do not prove plane extension, intrinsic recognition, or the existence of a periodic tiling whenever a survivor tiles. A required next theorem would say: for every real alpha and every positive metric realization of one of these surviving words which admits a plane tiling, construct a complete periodic carrier or derive a global contradiction. There is currently no return invariant controlling reflected QQ paths or the BBB branching graph to prove that theorem. Nor does O(R) defect counting imply defect absence. Under protocol §5 the route stops here; no numerical alpha sampling, larger tori, patch growth, or seam atlas is justified. Reopening requires a new global return/extension invariant or a specifically derived complete carrier.

Dependencies read: research-problem.md; research-protocol.md (especially5,19); progress-assessment-2026-10-19-2052.md; the complete reviewed regular-pentagon-126-144 synthesis; the octagon AA-capacity hostile review and first-gate report. The proof above reproduces the needed AA argument and square bound independently. No Git or discovery-log edits.

Replay exact finite domain:

    mise exec -- conda run --no-capture-output -n arisearch python research/searches/complementary-angle-flow-sol-2026-10-19.py

The script uses integers and fractions only; no numeric alpha or metric coordinates are sampled. Its output is a finite enumeration check, while the unbounded implications are proved analytically above.
