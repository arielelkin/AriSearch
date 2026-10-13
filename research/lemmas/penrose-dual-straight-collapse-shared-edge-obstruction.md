# Straight rhomb-point collapse still exceeds the two-shape exterior budget

Date: 2026-10-13. Status: **proved by exact finite elimination certificate, internally checked; fresh hostile review pending**. This genuinely changes and then closes the degree2-collapse exception of the preceding [fixed-point budget obstruction](penrose-fixed-point-two-shape-exterior-budget-obstruction.md). No enlarged source patch, added graph node or degree0 removal is covered.

## Changed hypothesis and finite domain

Keep exactly the same retained three-deflation source fixture, the same35 fully surrounded rhomb points, and the same exact thin-point shift tau0=1/100. The earlier obstruction retained3 or4 rays at every point. Now also permit a point to retain exactly2 original rays if and only if they are exactly opposite. Their two sectors arepi, so contraction of this straight degree2 point produces no intrinsic native corner and consumes no exterior-angle budget. Degree0/1 removal is excluded; no additional edges, nodes or cuts are allowed.

For the26 positive angle classes and their exact integer exterior floors, use the independently reconstructed geometry and cosine certificates in the preceding obstruction. Native angle values can repeat; flatpi sectors are ignored as a valid relaxation. Rotations and reflections preserve these native values.

The finite question was first whether the additional straight-collapse choices evade the independent local budget, and then whether those choices survive the necessary equality of ray retention at both ends of each original network edge. Outcomes: a budget or shared-edge contradiction excludes the changed compiler; a surviving consistent local choice would establish only a finite necessary pattern, with no plane extension or two-class congruence theorem.

## Independent local budget survives collapse

Exactly ten points have an opposite pair:

    center3: neighbors10,6;
    center10: neighbors12,3;
    center17: neighbors22,12;
    center22: neighbors24,17;
    center29: neighbors34,24;
    center34: neighbors36,29;
    center41: neighbors46,36;
    center46: neighbors48,41;
    center53: neighbors58,48;
    center58: neighbors6,53.

Every equality is checked in exact complex algebra: the quotient of the two rays has negative real phase, exactly-1 after normalization. No approximately collinear ray is accepted.

The six distinct local-choice signatures now have5,3,3,3,5,3 choices, so2025 Cartesian products suffice. Their minimum integer-floor union cost is605 degrees, with required angle IDs

    {5,7,8,10,12,13,14,16,17,23,24}.

This is a genuine pass of the relaxed local exterior-budget condition: each actual exterior deficit is strictly less than its certified floor plus1, so this witness's actual union deficit is strictly less than605+11=616<720 degrees. It is not a plane covering or a two-shape construction. The contrast with the old837-degree bound shows why excluding degree2 collapse would have been a consequential hypothesis.

## Shared network-edge consistency restores an exact contradiction

An original network edge joins rhomb points r,n. If it remains in the final graph, both endpoint choices must retain that ray; if it is deleted, both must omit it. For each of the35 constrained points, use its exact finite set of degree2/3/4 local choices. Points outside this35-point domain are left unconstrained, so the resulting model is a necessary relaxation of every claimed final compiler on the full source.

Perform exact arc consistency: remove a choice at r if its retained/omitted value for edge(r,n) is unsupported by every currently remaining choice at the constrained neighbor n. Each such removal is sound because no globally consistent assignment can use it. The retained certificate records40 elimination steps, including the current neighbor domain and every removed option. No branching, CSP solver, larger patch or mathematical finite-model conjecture is needed.

After these eliminations, intersect the required angle-ID sets of all remaining choices at each point. Every global assignment must contain every angle in that intersection. The union across the35 points is

    C={0,3,8,10,11,13,14,17,20,22,23}.

These are11 distinct algebraically checked native interior-angle values. Their certified exterior floors are respectively

    71,53,35,107,89,72,90,56,54,72,51 degrees,

which sum to **750 degrees**. The actual exterior sum is at least750, exceeding the720-degree exterior-angle budget of any two genuine convex polygons. Consequently no two unmarked convex polygon shapes, regardless of their side counts, can realize the changed degree2/3/4 compiler on the fixed fixture.

The exploratory CP-SAT optimum was1286 degrees, but that optimum is not load-bearing and is not independently certified here. The proof uses only the40 exact support-removal steps and the750-degree forced-angle sum.

## Open-parameter consequence

The same contradiction holds throughout some open real interval around tau0=1/100 in the original thin-point shift family, allowing the exact degree2-collapse exception.

Proof. The finite strict interior and edge-crossing inequalities persist near tau0, preserving radial orders. Any previously reflex size3/4 subset stays reflex after shrinking a common interval; the old list already includespi-gap choices. A size2 subset not opposite at tau0 remains nonopposite nearby, so no new admissible straight-collapse option appears. An old opposite pair may cease to be opposite, which only removes choices. Thus every nearby actual choice maps to an old allowed local option, and shared-edge consistency forces it to survive all40 old support-removal steps.

The11 forced old angle classes therefore still occur as native positive sectors. Their positive sector functions are continuous. Each associated exterior deficit is strictly greater than d_j-1 degrees near tau0. Different old angle classes remain in disjoint small neighborhoods; splitting a class cannot reduce the distinct native-angle budget. Selecting one nearby native value for each of the11 old labels yields an exterior sum strictly greater than

    750-11=739>720 degrees.

New corners opening from old flatpi sectors can be ignored because their deficits are nonnegative. This contradicts the general two-polygon budget lemma. QED.

The interval is existential, obtained by finite continuity and strict margins; no numerical epsilon or whole-family classification is claimed. Parameters outside that interval remain unclassified. Degree0 removal of rhomb points, additional network nodes, changed cuts/source, or changed point geometry outside the interval change actual used hypotheses and are outside the result. Reopening requires a concrete such proposal, not a larger fusion enumeration on the same constraints.

## Artifacts and independent replay

* [Straight-collapse choices](../certificates/penrose-dual-fusion-opposite-ray-collapse.json): all35 exact domains, ten opposite-pair points and2025 independent-product cost histogram.
* [Arc certificate](../certificates/penrose-dual-collapse-shared-edge-arc-certificate.json):40 exact deletions, final domains, forced angles and750-degree lower bound.
* [Exploratory shared-edge query](../certificates/penrose-dual-collapse-shared-edge-gate.json): retained CP-SAT result, not proof-critical.
* [Independent checker](../reviews/check_penrose_dual_collapse_shared_edge.py): imports no producer, invokes no solver, reconstructs all geometry, verifies all26 cosine-floor bounds without floats, rebuilds degree2 choices, replays2025 independent products, and checks every support deletion and forced-angle conclusion.

    MISE_AUTO_INSTALL=0 mise exec -- conda run --no-capture-output -n arisearch python research/reviews/check_penrose_dual_collapse_shared_edge.py

External hostile review must assess the source-point/ray model, straight-degree2 scope, shared-edge necessity, exact elimination trace, angle budget and continuity argument. No novelty or unrestricted two-convex-tile conclusion is asserted.
