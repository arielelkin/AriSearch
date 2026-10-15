# Independent hostile review: arbitrary physical splits in the receiving-hexagon construction

Date: 2026-10-15, 11:00 UTC direction cycle. Reviewer: fresh direction agent, independent of the lemma author. **Verdict: VALID on the stated domain.** No unrestricted two-polygon result follows.

## Exact claim and hypotheses

Reviewed `research/lemmas/context-dependent-split-receiving-hexagon-obstruction-2026-10-15.md` in full. The domain has unit thin/thick rhombs with the displayed native arrows; opposite donor edges; mark-local donor triangles with interior projections and apexes; arbitrary physical source-edge split points shared by the two incident rhombs; strict receiving quadrilaterals; arbitrary proper truncations at the two donor-node corners; and one congruence class for all resulting genuine hexagons. Both source species occur. Both donor parities need NOT occur. Reflections are allowed.

The proof actually needs only one thin and one thick rhomb, each with either parity, once the common-H hypothesis and globally mark-local donors hold. It does not need the full neighboring-source atlas or a hidden equality between split points on different edges.

## Native incidence audit

I reconstructed the roles from the edge table, before consulting the author's checker. Edges are AB,BC,CD,DA numbered 0,1,2,3, and a listed pair denotes the DONOR edges.

| Source; donor edges | Receiver; tail internal role; head internal role |
|---|---|
| thin; 0,2 | BC: X tail / Y tail, X head / X head; DA: Y tail / X tail, Y head / Y head |
| thin; 1,3 | AB: X tail / Y tail, X head / X head; CD: Y tail / X tail, Y head / Y head |
| thick; 0,2 | BC: Y tail / X head, Y head / Y head; DA: X tail / X tail, X head / Y tail |
| thick; 1,3 | AB: X tail / X tail, X head / Y tail; CD: Y tail / X head, Y head / Y head |

In every row both required mark receivers are present. This regenerates all sixteen endpoint occurrences and all eight distinct symbolic endpoint forms in the lemma. In particular the thick Y tail really is at a 108-degree source corner and its head at a 72-degree source corner. The thick X tail is at A, next to the other X tail. Neither statement substitutes a thin incidence or identifies X and Y donors.

## Angle-capacity and isometry attacks

If a and b differ, a+b=72 and both are positive, so neither equals72 or144. The four selected angles therefore are genuinely distinct; their sum288 cannot be completed to720 by two angles strictly below180. Once a=b=36, the three other angles of H have sum468 and each exceeds108. Thus36 and72 occur exactly once, even if144 repeats. The c+d=216 argument then has precisely the stated branch. At either acute thin corner exactly one adjoining edge is an internal donor, so its strictly interior apex proves beta<36 without assuming both donor parities. Positivity excludes Xhead=beta-36.

Proper truncations leave the source endpoint and M at graph distance three in the six-cycle. A Euclidean isometry of genuine polygons preserves the cyclic adjacency relation, including under reflection. Consequently uniqueness of the72 corner identifies its opposite vertex and diagonal length. The two receiving hexagons along ONE thick Y edge retain different endpoints of that SAME edge and share its SAME M, giving m=1-m=1/2. The thick X tail then has opposite diagonal1/2. This does not assume thin and thick split equality, a donor-side independent split rule, or locality of the physical edge choices.

## Independent native-turn calculation

Normalize the thick X receiver with its interior above its arrow T=(0,0), H=(1,0). Write r=tan(beta), q=tan36 and A=q(1-r^2)+2r. The donor base-angle condition independently gives

    u=(r+q)/A, h=ur, 0<r<q<1.

The external apex is t=(u,-h). Rotating that vector through72 gives the actual internal apex p=(x,y), since the internal donor is another X tail. Using sin72=2q/(1+q^2), cos72=(1-q^2)/(1+q^2), the oriented turn at M=(m,0) is

    det(M-t,p-M)=m(y+h)-uy-hx.

Here y+h=u sin72(1+rq)>0. At m=1/2, direct rational expansion yields

    det(M-t,p-M)
      = -u sin72 [q(1-rq)+qr^2+(2+q^2)r^3]/(2A).

Every factor outside the minus sign is strictly positive throughout the entire admissible interval. This is a strict reflex turn, not a numerical near-degeneracy. I independently expanded the rational expression with SymPy and checked zero residual. The author's separate Sage checker also passes. No parameter grid or solver conclusion is needed.

## Counterexamples and quantifier failures attempted

* Arbitrary splits on every physical edge: insufficient, since the midpoint is forced within one thick rhomb.
* Missing one donor parity: insufficient, since each individual rhomb has both relevant receiver marks.
* Reflection exchanging the donor corners: irrelevant; only the unique retained72 vertex and its graph-opposite vertex are used.
* A second72 corner hidden among the cut corners: excluded by the exact angle-capacity bound.
* The beta18 reflection exception from the earlier proof: irrelevant; this proof never reconstructs donors from thin-wedge congruence.
* Very small positive beta or beta close to36: the rational determinant remains strictly negative. Boundary beta=0 or36 is already outside strict interior-apex hypotheses.
* Independently chosen donor-side split versus receiver-side split: a disagreement is not a physical dissection; allowing the donor to inherit the receiver's point is already included.

No defect or repair was required. Remaining uncertainty concerns only construction domains not covered by the hypotheses: context-dependent DONOR triangles, a different retained-vertex topology, nonstrict or differently truncated precursors, or more than one receiving-hexagon congruence class. The review does not infer aperiodicity or impossibility for arbitrary polygon pairs.

Replay performed:

    mise exec -- conda run --no-capture-output -n arisearch python research/searches/context-dependent-split-receiving-hexagon-check-2026-10-15.py

Independent symbolic calculation was run directly in SymPy from the displayed rotated donor vectors; it is not a new certificate or registry item. No discovery-log, registry or Git edit was made by this reviewer.
