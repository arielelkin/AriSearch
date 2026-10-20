# Hostile review: explicit binary power-cell periodic escape

Date: 2026-10-19. Scope: the adjacent `research/searches/fresh-convex-pair-construction-sol-2026-10-19.{md,py,json}` record. **Verdict: PASS within its stated scope.** No consequential mathematical or census defect found. The explicit pair has a rank-two periodic tiling for every stated parameter; this defeats this candidate pair as an aperiodic pair. It says nothing about all possible weighted fields or all convex pairs.

## Exact replay and finite census

Ran the exact supplied script with `mise exec -- conda run --no-capture-output -n arisearch python research/searches/fresh-convex-pair-construction-sol-2026-10-19.py`; it exited 0. Its output reproduces the stored JSON: 16 labelled tori with three classes and side counts {5,8}, eight with two classes and side counts {5,7}, witness 14025, rows 1001/0011/0110/1100, and the displayed Q7/P5 coordinates. There is no symmetry quotient: `range(1<<16)` visits every labelled 4x4 binary torus, and modulo-four indexing handles wraparound. Consequently no orbit-size assumption hides omitted fields. The 24 figure is the number passing the at-least-five-side filter, not the number of all fields.

The 512 local masks encode all nine sites without collisions. At contrast 1/5 the half-plane offset `(a*a+c*c)/2 + (b_center-b_neighbor)/10` is exactly the power inequality offset, including its sign. The initial [-1,1]^2 box contains every cardinal-bounded cell. Fraction predicates and interpolation are exact; deleting duplicate and collinear vertices is appropriate here because all cells are bounded and contain a neighborhood of their site. The final complete squared-distance matrix distinguishes different vertex counts and all noncongruent polygons. Every congruence of convex polygons maps extreme vertices in cyclic or reversed cyclic order, so the cyclic/reversal minimization is complete even for rotations not preserving lattice axes.

## Independent analytic attacks

Expanding `|x|^2-w(z) <= |x-v|^2-w(z+v)` gives exactly `2*x.dot(v) <= |v|^2+w(z)-w(z+v)`. Thus larger site weight expands its cell; the record uses the correct convention.

Independently evaluated the eight near-site inequalities symbolically on the stated vertices for residues 0,1,2,3. All slacks are nonnegative on 0<d<1/4; every polygon edge lies on its defining bound. The resulting cells are Q, P, -P, -Q, respectively. All farther bounds are strictly redundant: with cardinal box |x_i|<5/8, the worst integer-vector lower bound is at least 1 for a vector with an absolute coordinate at least 2. The stated n^2-5n/4 argument is valid, including negative coordinates after taking absolute values.

Independent symbolic edge and turn computations confirm no collapsed edge or straight angle throughout the entire open interval. For P the consecutive turn determinants are d(1-d)/2 twice, (2-d)(1-d)/2 twice, and (2-d)^2/4 once. For Q they are d(2-d)/4 four times, d/2 twice, and 1 once. Every value is strictly positive. The axis and diagonal edge directions yield exactly the asserted 90/135 degree angle counts. In the polygonal sense used here this proves strict convexity; it does not use the stronger definition of a strictly convex *set*, which excludes all polygon boundary segments. Five versus seven extreme vertices proves the two prototypes cannot be congruent.

Independent shoelace calculation gives area(P)=(d^2-8d+8)/8 and area(Q)=(-d^2+8d+8)/8. At d=1/5 these are 161/200 and 239/200; their sum is 2. Substituting d=1/5 gives precisely the rational vertices in the JSON.

## Consequential periodic escape

The field depends only on i+j modulo four. Both (1,-1) and (4,0) preserve it; translating every power inequality by either vector therefore translates the entire cell decomposition onto itself. Their determinant is 4, so they generate a genuine rank-two period lattice. The quotient has four lattice sites, one per residue, hence two P tiles and two Q tiles. Its area is also 2*area(P)+2*area(Q)=4, agreeing with the determinant.

Bounded weights ensure the power minimum is attained everywhere. Cells cover the plane, and interiors of distinct cells cannot intersect because their power differences are nonconstant affine functions. The explicitly computed polygons are all nonempty with positive area. Thus the escape is a full plane periodic tiling, not merely a compatible finite patch or a numerical pattern. It independently settles rejection of this particular pair family even if the census were omitted.

## Repairs and limits

No required repair. An optional robustness improvement would make the script assert its expected census and witness coordinates, rather than only print them; the present exact replay and analytic proof already establish the reported result. No search at other periods or contrasts, no general classification of fields, and no inference excluding a different power-cell pair is justified by this review. No Git or global-log edits were made.
