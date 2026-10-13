# Fresh hostile review: anchored Ammann counts and fixed-content fusion

Date: 2026-10-13. Independent reviewer: sol, distinct from luna author.
**Verdict: VALID** for the exact generic reviewed source and fixed-content
whole-tile partition hypotheses. It is a mechanism exclusion, not a global
pair impossibility theorem or novelty claim.

## Dependencies applied, not repeatedly audited

Reviewed Ammann forcing Lemma5 supplies a genuine partition of the source
pieces into thin/thick groups, with one H distinguished quad in every thin
group and one P1/P2 distinguished quad pair in every thick group. Reviewed
Lemma6 supplies legal composition at all powers ofphi with Robinson
red/blue child rules. I read these two exact dependency statements and
checked their use here; their whole Penrose forcing proofs were not re-audited.
The old coordinate-parameterization Euler assumptions and a P3 identification
are neither necessary nor invoked.

## Three anchor bijections

Each source H occurrence has exactly one distinguished quad and initiates
exactly one thin group. Conversely a thin group contains exactly one such
quad. Piece-partition disjointness gives injectivity and exhaustiveness.
Each source P1 initiates a thick group containing exactly one P2 quad across
its uniquely specified complete c edge; thin groups contain no P2 quad.
Every P2 quad belongs to one group by the reviewed piece partition, so every
P2 occurs in exactly one P1 group and both P1 and P2 occurrences are in
bijection with the thick groups. These are piece-identity counts, not an
inference from similarity or Euler density.

Polygon and rhomb partners share their distinguished quad. Uniform fixed
shape diameters bound their anchor displacement. Comparing anchors in a
square leaves only partners in a fixed-width boundary annulus, with O(R)
counts by positive area/inscribed-disk packing. Thus h=t+O(R) and p1=p2=
T+O(R) hold uniformly with arbitrary fixed interior anchor conventions.
Reflections and orientations preserve these bijections and counts in the
reviewed generic forcing domain. Distinct source congruence classes ensure
reflection cannot silently relabel a P1 occurrence as P2.

## Irrational source ratio without an absolute-density assumption

The dependency explicitly identifies thin halves as red and thick halves
as blue. Their child matrix is[[1,1],[1,2]]. Direct exact algebra gives
(-phi,1)M=phi^(-2)(-phi,1). At fixed composition scale k, every unit half
away from a boundary annulus of width O(phi^k) belongs to a complete parent
half within the square. The omitted unit halves therefore contribute O_k(R),
with k fixed; no uniform-in-k boundary constant is asserted.

Complete scale-k parents have minimum area a0 phi^(2k), so their total
number is at most R^2/(a0 phi^(2k)). Applying the stable left eigenvector to
M^k gives residual at most C phi^(-4k)R^2+O_k(R), with C independent ofk.
Taking R to infinity FIRST, then k to infinity, proves T-phi*t=o(R^2).
The sum t+T is Theta(R^2) by fixed area coverage, so the relation forces both
counts Theta(R^2) and validates division. The three bounded-displacement
bijections give p1/h,p2/h ->phi and p1/p2 ->1. No individual absolute tile
density, unique ergodicity or prescribed source tiling is assumed.

## All fixed-content singleton-pentagon fusions excluded

If P1 remains singleton and every other final tile has one fixed integer
content vector u, the H and P2 window counts are uH*m+O(R), u2*m+O(R).
They are quadratically positive, so uH,u2>0 and m=Theta(R^2).
Consequently p2/h tends to the rational u2/uH, contradictingphi. Arbitrary
P1 content inside the cluster is harmless. The P2-singleton case is identical
with the pentagons exchanged. The proof allows singleton target density0;
no unnecessary strict-positive singleton-frequency assumption is used.
The bounded cluster diameter and exact whole-source-tile partition are
consequential for boundary errors and cannot be dropped for arbitrary cuts.

For two fixed-content vectors u,v, every rational annihilator a satisfies
0=aH+phi(a1+a2). Irrationality gives aH=0,a1+a2=0. The annihilator is thus
at most one-dimensional, while two vectors inQ^3 have at least one-dimensional
annihilator. Hence rank2 and annihilator span(0,1,-1), proving u1=u2,v1=v2.
This is a necessary count condition; it does not prove any balanced cluster
is convex, congruent, compatible, or globally realizable.

## Counterexample attacks and scope

Attempted loopholes were boundary-straddling clusters, zero target density,
reflection-induced source-label exchange, variable absolute source densities,
wrong matrix eigenvalue/colour assignment and unequal source dissection of
congruent macro supports. The first five are handled by the stated hypotheses
and exact count proof. The last is expressly OUTSIDE fixed content: a final
shape could have several distinct source-content dissections. Congruence of
macro shapes alone does not justify the theorem's fixed-content assumption.
This result cannot exclude such a mechanism, fractional-tile cuts, another
source, or nongeneric absence of the reviewed source decoding.

No geometric patch enumeration or solver is required. The exact child matrix
and canonical piece bijections are the proof obligations, and they have been
checked in the named scope. Reopening the closed singleton/fixed-content route
requires a changed content/dissection hypothesis or source mechanism, not a
larger cluster search with the same assumptions.
