# Mixed Q7 exact native incidence discharge gate

Date: 2026-10-19. Status: exact local conservation certificate; independent review pending. Scope: ABBCCBC, ABBCCCB, ABCBBCC, ACBBBCC, all 108<alpha<126. No plane existence, periodicity, or aperiodicity conclusion.

## Result

The target certificate exists and is elementary: **a pentagon cannot have PP-degree two** in a defect-free tiling of any of these four pairs. Consequently PP-degree-zero and PP-degree-two pentagons have O(R) square-window count. The degree-one PP graph is a perfect matching after translated purification. This conclusion supplies no global ribbon, reflection parity, or carrier theorem.

At a PPA vertex exactly one of the two P sides faces P. At a PBC vertex neither does. Thus the PP sides on P are an independent set in its five-cycle, of size at most two. Any two independent edges in a five-cycle flank a single intervening side. That intervening side faces Q and both its endpoints are PPA, so its Q neighbor must supply an AA native side. Q has a unique A corner, hence no AA side. This excludes degree two pointwise. This is the additional local constraint missing from the ledger n0=n2+O(R).

## Explicit nonnegative conservation certificate

Q vertices are 0..6 rooted at A, side j joins j to j+1. Its PQ sides are 0,2,4,6; QQ sides are 1,3,5. Put weights (-1/5,+1/5,+1/5,-1/5) on its four PQ slots in that order, independent of reflection. Equivalently a PQ side receives (1-2a)/5 where a is the number of its Q endpoints labeled A. Their sum on each Q is zero.

A pentagon of PP-degree k has 5-k PQ sides and exactly 2k Q-A incidences across them, so its total received weight is

    ((5-k)-2(2k))/5 = 1-k.

Since k is 0 or 1, this is nonnegative and equals the indicator of degree zero. Summing in a square gives n0=O(R), while n2=0 pointwise, including in the original resonant tiling: BBB contains no P, so every P corner is still PPA or PBC. Every error involves fixed bounded tile neighborhoods and is O(R). This is an exact rational dual certificate, not numerical LP evidence.

At alpha120, the reviewed balanced B/C budget gives O(R) BBB stars and affected tiles. Enlarge the boundary and remove all tiles meeting BBB; the remaining native incidence equations have only O(R) errors. The local AA exclusion remains valid pointwise because BBB contains no P; in particular n2=0 in the original tiling. Only the public-side charge bookkeeping requires the O(R) defect correction, yielding n0+n2=O(R) in the original tiling as well. Alternatively the reviewed translated compactness argument removes BBB first, and this certificate then removes degree-zero pentagons in a second translation limit. These uses are justified by positive minimum tile area, bounded diameter, and fixed-radius defect neighborhoods of area O_r(R).

## Complete finite incidence domain and exact equations

For each word enumerate all independent PP subsets of C5 (1+5+5 possibilities). Every remaining P side is assigned one of the eight labels (s,r), with s in {0,2,4,6} and Q reflection parity r in {0,1}. Read its Q endpoint labels in native order if r=1 and reversed order if r=0. At a P vertex touching PP require A on the other side; at every other vertex require the pair B,C. This enumerates all native corner and side incidence types, including reflected placements; it deliberately imposes no polygon overlap test or long-range consistency. Exact surviving P counts are respectively 104,82,104,82. No degree-two type survives.

Let x_t>=0 be P-type frequencies and q_r>=0 Q parity frequencies. For each PQ label (s,r), impose sum_t N_t(s,r)x_t=q_r. Normalize q_0+q_1=1. For a PP side record its ordered endpoint descriptor d=((s_left,r_left),(s_right,r_right)) from its two adjacent PQ sides. Its required partner is d*=((6-s_right,r_right),(6-s_left,r_left)). Impose sum_t [N_t(d)-N_t(d*)]x_t=0 for every descriptor. These are necessary full PP-side endpoint balances.

QQ seams enumerate every (e,r,f,u) with e,f in {1,3,5} and r,u in {0,1}; endpoints are reversed for equal parity and retain order for unequal parity. Retain exactly those with B,C at both physical endpoints. Assign nonnegative seam variables y and impose sum_y multiplicity((e,r),y)y=q_r. Self seams count twice. This includes both BB/CC parities; mixed BC seams require equal parity. The JSON records the complete retained domain. QQ feasibility is independent of the P variables here: at each parity pair the BB slot to the CC slot with weight q_r and pair the mixed slot to itself with weight q_r/2. The script verifies those balances exactly. Metric side-length restrictions may only shrink this necessary domain; BB and CC equality is already a reviewed necessary condition.

The optimized matrix is the P/PQ/PP incidence relaxation; QQ variables are completed and verified separately by the explicit formula above, rather than inserted as matrix columns. This is a necessary endpoint incidence cone, without metric development or plane-extension constraints. The LP maximizes n0+n2. SciPy proposes a solution; every retained equality and nonnegativity is checked using Python Fraction. The displayed dual certificate proves the upper bound exactly independently of the optimizer. Its objective is zero for all four words; exact rational primal supports are retained in JSON to demonstrate feasibility of the relaxation, with n=(0,1,0). These primal supports are incidence flows, not plane tilings or geometric quotients.

## Replay and stopping state

    mise exec -- conda run --no-capture-output -n arisearch python research/searches/heptagon-mixed-discharge-sol-2026-10-19.py

The adjacent JSON retains exact primal support, Q parity frequencies, full QQ seam domain and flow, and dual weights. There is no search radius, seed, timeout, alpha sample, or metric continuation. This is one bounded design cycle. The reviewed mixed-QQ obstruction and 124/128 strand atlas permit both immediate seam parities; the new discharge does not constrain their holonomy. The precise next gap is a global consequence of the perfect PP matching plus reflected QQ seam matching that proves plane obstruction or a periodic escape. The prior reviewed four-face gate was UNSAT for these remaining mixed words at alpha124; this discharge does not justify rerunning a two-Q carrier search or enlarging it. Stop this gate without a new mechanism for that gap. No Git or discovery-log edits were made by this worker.
