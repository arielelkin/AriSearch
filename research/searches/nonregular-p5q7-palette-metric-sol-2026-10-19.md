# One nonregular pentagon/heptagon native metric gate

Status: **Exact metric and native-corner support independently reviewed; fixed candidate subsequently killed by a periodic torus.** One design cycle, internally checked and independently reviewed. The review caught and the root corrected a reflected-mate wording error for Q side5. No plane tiling is proved by this report. No discovery-log or Git changes were made by the producing agent.

## Domain and prior work

Input angle multisets are P=(100,100,110,115,115), Q=(125,125,125,130,130,130,135) degrees. The reviewed obtuse-edge-forcing lemma applies to unrestricted contacts and reflections, forcing full-edge trivalent tilings. The reviewed regular-heptagon classification requires a regular Q and does not apply. A literal normalized palette search over existing research Markdown/Python and discovery-log found only the simultaneous structural report `nonregular-p5q7-dimer-structural-sol-2026-10-19.md`; no earlier copy of this palette was found. This is a repository duplicate check, with no literature novelty claim.

Only one pair of cyclic words is retained below. The script performs exact checks on that fixed pair and enumerates the complete five angle resonances. It performs no angle grid, patch growth, corona census, or periodic-quotient enumeration.

## Exact resonance and frequency gate

The complete unordered trivalent resonance list is:

* P100 Q125 Q135;
* P100 Q130 Q130;
* P110 Q125 Q125;
* P110 P115 Q135;
* P115 P115 Q130.

There is no PPP (maximum sum345) or QQQ (minimum375). The fourth resonance must not be omitted from the initial enumeration. Both P115 corners are necessarily PPQ. For each P the number of its PPQ corners equals twice its number of PP sides: a PP side has PPQ at each endpoint, and at a PPQ corner exactly one incident P side has a P neighbor. Thus the number is even. Its unique110 cannot also be PPQ. The fourth resonance never occurs, pointwise. Each P has exactly one PP side, joining its adjacent115 corners, and lies in a PP dimer. P words with nonadjacent115 are impossible.

For square windows, count whole tiles/corners and absorb the fixed-width boundary collar into O(R). Fixed positive areas and bounded diameters bound its tile count by O(R), uniformly in the window center. Let p,q be tile counts and x,A,B,C the counts of PPQ115/115/130, PQQ100/125/135, PQQ100/130/130, PQQ110/125/125. Then

    x=p+O(R), A=q+O(R), C=p+O(R), A+B=2p+O(R),
    x+2B=3q+O(R).

Consequently p=q+O(R), and all four star counts equal p+O(R). Along any convergent normalized frequency subsequence p=q=N and x=A=B=C=N. N denotes frequency here, not an exact finite-window identity. The two types have uniform quadratic counts by area and this ratio.

In an arbitrary angle-only tiling, each Q has one or three PPQ130 corners: its other corners are endpoints of QQ sides, hence their number is even. The average-one ledger only makes three-corner Q defects O(R); it does not exclude sparse defects pointwise. The fixed metric below excludes them by private lengths.

## One cyclic-word choice and metric

Sides are indexed from vertex j to j+1. Retain

    P angles = (115,115,100,110,100)
    P lengths = (L,1,1,1,1)
    Q angles = (130,130,130,125,125,125,135)
    Q lengths = (1,a,1,b,1,1,1).

P is chosen with a symmetric unit-length outer chain around its forced115–115 dimer side. Q has three candidate QQ dominoes in order: 130–130, 125–125, 125–135. Its four intervening PQ sides have endpoint P-corner patterns115–100,100–110,110–100,100–115, exactly the four P outer-side patterns. This supplies a combinatorial reason for this word rather than a generic cyclic-word census.

Let z=exp(2*pi*i/72). Define

    L = 2*cos(35 degrees)-2*cos(65 degrees),
    a*z^10+b*z^31 = -(1+z^20+z^42+z^53+z^62),

where a,b are real and the displayed complex equation is an invertible two-by-two real linear system. The retained script works in Q(z), solves it exactly, and proves positivity via exact real-algebraic comparisons. Numerically L=0.7930675650965846, a=0.9728413872067758, b=1.259272723569946. These decimals are explanatory only.

The exact edge-direction exponents are P=(0,13,29,43,59), Q=(0,10,20,31,42,53,62). Set the first vertex to0 and cumulatively sum each length times z to its direction exponent. The certificate retains all exact cyclotomic coordinates and minimal polynomials. The embedding z=exp(2*pi*i/72) selects the intended algebraic roots. Exact vector closure holds for both polygons. The checker tests strict supporting half-plane inequalities against every nonincident vertex for every side, proving both are genuine strictly convex polygons with the stated exact angles.

The four numbers L,1,a,b are pairwise distinct. L occurs only on the P115–115 side, forcing PP dimers. Q side1 of length a is private to Q and must be QQ; its two130 endpoints are therefore PQQ. The parity result forces the remaining Q130, at vertex0, to be PPQ. Q side3 of length b is also private and QQ. Q vertices3,4 (125) are therefore PQQ, and their other sides2,4 are PQ. Q vertex0 forces sides0,6 to be PQ, leaving side5 QQ. Thus every Q has precisely the intended three QQ sides in this metric, and three-PPQ defects are excluded pointwise.

## Exact native-corner support

Every native corner is supported by one of these metric stars (triangle entries are seam lengths):

* PPQ115/115/130: (L,1,1);
* PQQ100/130/130: (1,a,1);
* PQQ110/125/125: (1,b,1);
* PQQ100/125/135: (1,1,1).

The replay verifies the native corner indices and their two incident lengths, and checks that these four witnesses cover all five P and seven Q corner indices. At each star, match the three sides with their indicated lengths and choose suitable isometries. Each pair of polygons lies on opposite sides of its shared supporting line, so these are actual legal three-tile vertex stars. QQ edges have compatible mates. The Q125–Q135 side5 requires a half-turn pairing to another Q side5, which swaps the endpoint types; mirror reflection across that side gives incompatible stars. Every P/Q side also has an endpoint-compatible mate: P sides1,2,3,4 correspond to Q sides0,2,4,6.

This is stronger than angle coverage and weaker than an extendible corona. Different locally legal vertex stars have not been assembled around a complete tile. No density or local-star calculation implies that they can be assembled globally.

## Replay and exact next obligation

Run:

    mise exec -- conda run --no-capture-output -n arisearch python research/searches/nonregular-p5q7-palette-metric-sol-2026-10-19.py

The stdout must reproduce `nonregular-p5q7-palette-metric-sol-2026-10-19.json`. Sage exact arithmetic and assertions are proof-relevant. There is no numerical solver, seed, cutoff, or optimization flag. The only finite enumeration is the explicitly complete unordered species-aware angle resonance domain.

The later [exact four-face torus](nonregular-p5q7-minimal-torus-sol-2026-10-19.md),
[independently hostile-reviewed valid](../reviews/nonregular-p5q7-torus-hostile-sol-2026-10-19.md),
now proves plane existence and a rank-two periodic escape for this fixed pair.
The metric/corner checks in this report remain local facts; the later torus
supersedes the former missing-corona and existence obligations. Stop this
fixed candidate for the original aperiodicity objective under §5.
