# Independent integration audit: extracted six-child wheel theorem

Date:2026-10-13. Verdict: **VALID extraction; no quantifier drift found.**
This is an integration audit, not a new enumeration or replacement for the
retained independent geometric and certificate reviews. No tests rerun.

## Sources compared

* [Extracted combined lemma](../lemmas/two-size-pentagon-six-child-wheel-obstruction.md).
* [Original480 record](../searches/resumed-two-size-six-wheel.md), its
  [independent review](resumed-two-size-wheel-review.md), and producer.
* [Complete-count/640 record](../searches/resumed-two-size-wheel-complete-counts.md),
  its [independent review](resumed-two-size-wheel-complete-counts-review.md),
  and producer.

## Hypotheses and indexing

The extraction retains a genuine convex pentagon with five pairwise distinct
native angles, arbitrary positive REAL side lengths, parent mu P, small
children P, large children lambda P, and lambda²=mu>1. Its wheel scheme
retains one center plus five distinct single-child parent corners, complete
consecutive native sides on both rays, and exactly the two endpoint children
covering every whole parent side. The center's rotation and inner seam
choices are not fixed: their exclusion is justified because the proof uses
only necessary boundary equations. The extraction expressly denies any
claim that all six-piece partitions have this topology.

Vertex i precedes side i. For the initial corner on side i the reflected
contribution is l_(i-1); for its final corner i+1 the reflected contribution
is l_(i+1). This matches BOTH producers and the independently reconstructed
identity/swap corner blocks on rows/columns(i-1,i). All five binary reflection
choices are retained jointly for both rays of each placed child. Distinct
angles, rather than an imposed orientation condition, force native vertex i
at parent vertex i. Reflections and arbitrary real metrics have not been
silently excluded.

## Counts and analytic pruning

b+d=6,b>0,d>=0 gives exactly d=0,...,5. The six exact positive roots in the
extraction agree with the originals. Each discriminant is nonsquare and
its other root negative, so irrationality/negative conjugacy have not been
introduced as extra conditions that omit a count.

The row bound uses positivity of the actual real side lengths, not an
algebraic-field restriction: at a maximal component, C*l=mu*l implies
mu<=max row sum<=2lambda, hence mu<=4. The d4,d5 roots violate this.
For d0 all corner scales1 give row sums2<sqrt6. For d1 at most one LARGE
CORNER (including zero when the center is large) gives row sums<=1+lambda;
the strictly positive square comparison using1<mu<3 matches the complete
review and rules out this count. No additional computational domain was
silently assigned to these four analytic cases.

## Certificates and replay pointers

For d2, center-small gives two large corners and320 reflection patterns;
center-large gives one and160. For d3 the respective large-corner counts
are three and two, giving320 and320. Total480+640=1120 exactly, without
symmetry reduction. The extracted field polynomials, basis order1,a,a²,a³,
case labels and certificate paths agree with both producers and prior
independent reviews. The independent-verifier method is described accurately:
separate corner-block assembly and120-term integer-polynomial Leibniz
expansion, without producer/Sage imports. Its earlier full-case PASS verdicts
are evidence for this extraction; I did not rerun them.

Nonzero determinant in either degree4 field is correctly transferred to
its positive real embedding by injectivity, giving nonsingularity overR.
Thus the theorem covers real length vectors outside the computation's
number field, exactly as the original reviewed claims do. No inner geometry
or positive-kernel feasibility is inferred from mere matrix singularity;
all determinants are nonzero and that branch never arises.

## Scope and verdict

The extraction retains the original exclusions of repeated native angles,
subdivided corners, additional boundary children and other dissection
schemes/counts. It makes no infinite-covering, recognizability, monohedral
classification, aperiodicity, universal impossibility or novelty claim.
The repeated-angle U restart suggestion has16 formal native-corner
assignments (two choices independently at each of its four repeated-angle
parent corners). Status refreshed during the Astra diff review: the
[7680-case boundary audit](../searches/resumed-two-size-repeated-u-wheel.md)
is complete and excludes that wheel; the older unrestricted two-U theorem
already supersedes it for candidate coverage. It does not reopen or weaken
the proved distinct-angle theorem.

No discrepancy requiring a producer replay, new computation or text repair
was found. The extracted theorem's hypotheses, indexing, count split,
prunings, exact certificate dependencies and limitations agree with the
independently reviewed original records. **VALID**.
