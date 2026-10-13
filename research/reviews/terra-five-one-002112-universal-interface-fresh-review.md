# Fresh hostile review: universal A002112 boundary-interface obstruction

Date: 2026-10-13. Reviewer: terra. Verdict: **VALID**, conditional on the already reviewed actual honeycomb/saturation reductions. This verifies root's new interface proposal independently and upgrades the A002112 branch beyond the earlier finite metric exclusions.

I read root's `research/lemmas/five-one-middle-mask-b-rows-and-bounded-a-strips.md` and the independently reviewed no-AAA binary lift `research/lemmas/five-one-adjacent-pair-no-aaa-binary-row-escape.md`. No settled global development/classification dependency was re-audited. The new assertion needing review is that A002112 cannot border a B row on one side and an A row on the other, regardless of its six side lengths.

## Spatial row premise

Every saturated B has native BB sides1,4, which are opposite in the developed triangular cell lattice. Each component continues without turning forever in either direction, so it is a complete primitive lattice line. Different possible directions meet at an integer cell because their determinant is plus or minus one. At such an intersection the supposed B cell would have four B neighbours, contradicting its exact degree two. Hence all B lines are parallel and the species field is a union of full rows. Adjacent B rows are impossible. This reasoning uses complete native cells supplied by the actual honeycomb theorem; it is not a claim about arbitrary polygon-centre segments in a general tiling.

## Exact local interface check

Rotate the common row direction so an A boundary row has its two top AB sides at global slots1,2. Their common vertex slot2 is ABB and therefore must be A colour z. Let C=(0,0,2,1,1,2). Independently enumerate the twelve native A placements C[(rotation+sign*k) mod6]. Exactly four placements have Cglobal2=2, namely (0,+),(3,+),(1,-),(4,-). In all four,

    Cglobal0=Cglobal1, and Cglobal3=Cglobal4.

These identities say the two row-direction AA sides have the same native colour at both endpoints; they are the private00 and11 native sides. Reflection is included. No side-length equality is assumed, and merging lengths cannot alter these angle identities.

For adjacent boundary A copies, their row seam is side0 of the left copy and side3 of the right. The outer B-facing endpoint has A angles (leftC1,rightC3). The inward endpoint has A angles (leftC0,rightC4). The two ordered colour pairs are identical by the displayed identities. The outer endpoint is AAB, so its two A colours must coincide, either x/x or y/y; the inner endpoint, if the next row is A, is AAA and must have three distinct x,y,z colours. Its first two A colours already coincide, an immediate contradiction. No complete ring feasibility, polygon closure, source reflection symmetry, or private-side metric distinctness is needed.

The independent finite domain is12*12 orientations, reduced by the two ABB top-corner constraints to16 pairs. Eight pairs pass outer AAB equality; zero pass both outer AAB and inward AAA. I wrote and replayed the length-independent checker:

    MISE_AUTO_INSTALL=0 mise exec -- conda run --no-capture-output -n arisearch python research/reviews/verify_terra_five_one_002112_boundary_interface.py

PASS. It also checks the retained exact certificate `research/certificates/terra-five-one-002112-boundary-interface.json`.

## Global consequence and scope

If a B row exists, each neighbouring row is A. The interface argument forces the next row on either side to be B. Induction therefore gives alternating A/B rows throughout the whole plane; there is no AAA vertex anywhere. This conclusion does not require compactness to bound A-strip widths, nor an assumption that A cannot tile alone. If no B exists, the field is pure A and supplies a periodic omission escape via the settled convex-hexagon classification.

For a mixed field, the fresh independently reviewed no-AAA binary lift applies to the SAME actual A and B metrics, including all equality specializations, and supplies a periodic tiling. Combined with reviewed defect-density extraction from an original unrestricted pair tiling, this gives full arbitrary-metric coverage for the native A002112 word on this five-plus-one resonance line. Partial contacts and reflections of the original tiling are handled by those imported reductions, not by silently assuming the original tiling already has the row form.

The finite AAA/Chebyshev artifacts remain useful counterexamples and exact records: genuine nonmonohedral AAA polygons can exist, so the universal assertion is an interface obstruction in a saturated global field, not “AAA implies monohedral” or “all local AAA patterns are impossible.” This new theorem supersedes the four remaining geometry-positive three-class families and all four two-dimensional four-class kernels without discarding any ancestor or assuming low-rank coverage.

No claim about other six-side native words, other angle multiplicities, global hexagon impossibility, or the construction route follows. The four other middle-mask words and two all-mask words still require their own mechanisms; root's portfolio ledger decides the next route.
