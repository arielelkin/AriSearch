# All-mask B5+1 words: unused AA22 support gives a periodic binary lift

Date: 2026-10-13. Status: [fresh independent hostile review VALID](../reviews/five-one-unused-aa22-support-fresh-hostile-review.md);
exact native certificate and independent checker PASS. This strengthens the earlier metric
stratum theorem to a theorem about contacts actually used in an admitted
field. It does not assert that equal side lengths force a contact.

## Exact support theorem

Let 108 < x < 126, x != 120, with angles measured in degrees, and put

    y=720-5x, z=4x-360, r=360-2x, s=360-2y.

Let A and B be fixed actual strictly convex hexagons. A has native corner
word 001122 or 010122 in colours (x,y,z); B has native corner word
(s,r,r,r,r,r). Native side i joins native corners i and i+1 modulo 6.
All positive side lengths and all their equality specializations are allowed.
Assume there exists an actual plane tiling T by these shapes satisfying:

1. Every contact is along a whole native side and every vertex is trivalent.
2. Every B has exactly two B neighbours.
3. Every native side 4 of every A meets B, rather than A.

Then the pair admits a plane tiling with a nonzero translational symmetry.
The conclusion constructs a possibly different tiling; it does not claim
T itself is periodic. Hypothesis 3 is called **unused AA22 support** because
native side 4 has two z endpoints. It allows a4 to equal any of a0,a1,a2.
An admitted pure-A tiling is already a periodic omission escape by the
imported monohedral theorem, and a pure-B trivalent field is impossible.
Thus the proof below treats the genuinely mixed case.

The complete trivalent star language on the stated interval is

    AAAxyz, AABxxr, AAByys, ABBzrr.

For completeness, the five angles are affine functions of x with distinct
slopes (1,-5,4,-2,10), and all take value 120 at x=120. Of the 35 unordered
triples only the four displayed triples have slope zero. All other triple
sum equations have their only possible root at excluded x=120. Strict
convexity holds exactly on the open interval stated. No angle>90 premise
is used after the trivalent field has been supplied.

## Imported dependencies and assumption ledger

- [Defect-free limit and honeycomb](hexagon-limit-and-periodicity.md), with
  its reviewed fixed-shape native compactness and uniform O(R) boundary
  bounds. These provide an admitted trivalent whole-side field from an
  unrestricted tiling, not a restriction on all original contacts.
- [B saturation extraction](terra-five-one-b-saturated-chain-reduction.md),
  with the [full-interval scope review](../reviews/five-one-full-strict-convex-angle-line-extension-review.md).
  Every B in the supplied mixed saturated field has BB mask {1,3}, {1,4}
  or {2,4}. This theorem is used only for the corollaries; saturation is an
  explicit premise of the support theorem itself.
- [Binary equality finite-cover theorem](periodic-binary-equality-fibre-lifting.md)
  and its independent review: an infinite solution with at most two full
  native states per cell over a periodic base has a finite-periodic solution
  when its constraints are equalities of maps of the cell bits.
- [Actual polygon development](two-hexagon-global-sft-encoding.md), Theorem
  1(a),(c), with its fresh repaired-reduction review: exact native angle sums
  and actual length matches develop to an admitted plane tiling, and a
  nonzero symbolic period supplies a nonzero Euclidean translation.
- The named unrestricted convex-hexagon monohedral classification retained
  in the first dependency supplies the omission escape when A tiles alone.

All shapes, lengths, and angles are fixed throughout compactness. Constants
may depend on those shapes. There is no uniform-in-x compactness assertion,
no lower species-density assumption, and no finite-patch extension premise.

## Metric noncollision corollary (the original result retained)

If additionally a4 differs from a0,a1,a2, every unrestricted tiling admits a
periodic escape. Indeed, extract a saturated field; a pure limit has the
omission escape. In a mixed field an AA seam using side 4 has two AAAxyz
endpoints, since neither AAB star contains z. Its other A side avoids z at
both ends and must therefore be one of native sides 0,1,2. Whole-side length
matching contradicts the three inequalities. Thus the saturated mixed
field satisfies unused AA22 support, so the support theorem applies.
The inequalities are sufficient for support, and are not needed afterwards.

## A nonnegative count removes AAA and middle B

Work in the actual mixed field from the support theorem. Its B masks are
curved {1,3},{2,4}, or middle {1,4}; this follows because BB edges cannot
contain native s and cannot be adjacent (otherwise a BBB star occurs).
Every A22 side is AB by the actual-field support premise. Each curved B has exactly one AB22 side, and each middle B has none. Counting this whole-side matching in any translated square gives

    N_A=N_curvedB+O(R).

Let U count AAA vertices and M count middle B cells. Native A1 corners give 2N_A=2Y1+U+O(R), while each B has exactly one s corner so Y1=N_B+O(R). Since N_B=N_curvedB+M,

    U+2M=O(R).

Both summands are nonnegative, so their combined count is at most CR
in every translated square of radius R, with C depending only on the fixed
shapes. This is not a pointwise disappearance claim. For an avoidance radius
L and maximum tile diameter D, choose R sufficiently larger than
C(L+D)^2. The radius-(L+D) neighbourhoods of the O(R) bad objects occupy
at most O(R(L+D)^2) area; the available square interior has area of order
R^2. A centre remains whose radius-L disk meets neither an AAA star nor
a middle-B tile. Translate these centres to the origin, let L tend to
infinity, and take a subsequential local placement limit.

Reviewed whole-side/trivalent compactness preserves fixed polygon metrics,
native indices, star types and side partners: distinct vertices have a
fixed positive sector-disk separation, and no positive-length side partner
can vanish or coalesce in a bounded window. In particular hypotheses 2
and 3 are local closed conditions on these indexed fields; a new AA22
contact cannot appear in the limit even when its length happens to equal
an A side. The limit has no AAA and only curved B masks. Pure B would
require a BBB star; pure A would require AAA stars, now absent. Thus the
limit remains mixed. No frequency premise enters the extraction.

## Opposite marked AB links give a periodic species base

In the zero-AAA field, each A0/A1 corner has exactly one AA arm; each A2 corner has none. For both native words the AA sides are exactly0,2. For A001122 these are private00 and11 sides; for A010122, corner0 has side5 AB and forces0 AA, corner3 has side3 AB and forces2 AA, and corners1,2 then force1 AB. Therefore side1 is its unique AB01 seam, and side4 its unique AB22 seam. They are opposite.

Curved B has exactly one AB01 and one AB22 seam, also opposite: their native indices are respectively(5,2) for mask{1,3}, and(0,3) for mask{2,4}. Mark these two seams on every tile. A marked seam always joins A to B, with matching endpoint palettes. Every cell consequently has exactly two opposite marked neighbours. Continuation gives complete alternating A/B primitive lines in the
COMBINATORIAL triangular lattice of honeycomb cells. An opposite pair of
slots continues in the same lattice direction at each step. Two lines in
distinct primitive directions meet at an integer cell: any two of
D0=(1,0), D1=(0,1), D2=(-1,1) form an integer basis. Their meeting would
require four marked neighbours at that cell, contradicting exactly two.
Hence all lines have the same combinatorial direction. Normalize it to
D0=(1,0). This is not an assumption that geometric tile centres lie on
Euclidean parallel lines. Every combinatorial row alternates A/B.

Write q_j in {0,1} for its species phase, with A at(i,j) precisely when i+q_j is even. The six neighbour directions are

    (1,0),(0,1),(-1,1),(-1,0),(0,-1),(1,-1),

where neighbour slot k is global side k-1. Each B has one B neighbour above and one below. If q_(j+1)=q_(j-1), those two directions are opposite, giving the forbidden middle BB mask. Thus

    q_(j+1)=1-q_(j-1).

After a horizontal shift q0=0; q1 is arbitrary, and (q0,q1,q2,q3)=(0,t,1,1-t). Species has periods2D0 and4D1. This is a proved backbone, not a general assertion that bounded strips are periodic.

## Full native fibres: why four B states reduce to two

At each periodic species cell, its two AAB/ABB corner roles are fixed. An A's two ABB corners must be z and its other four corners x/y. Among all twelve indexed placements, exactly TWO full native A states satisfy these roles, for both words and both species bases. Their native AA set is0,2 and their marked AB22/01 edges are4/1. Their angle profiles may differ; no identical-angle-fibre assumption is made.

B has two AAB corners and four ABB corners. Its s corner must be one of the former, leaving FOUR full native states: two s positions and two handedness choices. The two marked seams reduce them by actual metric matching. Every marked AB22 side has length n=a4; every marked AB01 side has length
m=a1. These definitions allow m=n and every other alias. The possible native B index pairs(AB22,AB01) are exactly

    (2,5) or(3,0),

with two states in each branch. If only one metric branch is feasible, each B cell retains at most two states. If neither is feasible, no actual field exists. A singleton can be duplicated as a binary fibre if needed.

If BOTH branches are feasible, B2=B3=n and B0=B5=m. Let its remaining side lengths be p=B1,q=B4. Direct B edge directions are E^j, j=0,...,5, where E=exp(iR), R=180-r=2x-180 in(36,72) degrees. Its closure polynomial is

    f(E)=m+pE+nE^2+nE^3+qE^4+mE^5=0.

Conjugate closure multiplied by E^5 gives

    f(E)-E^5 f(E^-1)=(p-q)(E-E^4)=0.

E-E^4 is nonzero throughout R in (36,72): E^3=1 would require R to
be an integer multiple of 120 degrees. Thus p=q. Native B side word(m,p,n,n,p,m), together with its single s and five r angles, is invariant under native reflection k->-k. The corresponding two reflected poses at each s-position have IDENTICAL global angle and length profiles. Choose one canonical representative of each pair. Replacing a reflected label by that representative changes no corner or seam constraint; it leaves exactly TWO full native B representatives at each cell. No unsupported four-state periodic-lifting theorem is invoked.

This handles every B metric alias: one branch gives two states directly, while both branches force the symmetry needed to collapse the four-state fibre. The argument uses actual B closure, not just a length-equality pattern.

## All angle and metric constraints are binary equalities

Assign one bit to each cell's two full native states. The AAB star requires its two A colours to agree, and to agree with the B corner map r->0,s->1. It is expressible by pairwise equalities of the two A-corner maps with that B map. At every ABB star, A is already z and both B corners r, so its angle condition is automatic. No AAA or BBB star occurs. Every seam constraint is equality of two native length maps, each depending on the bit at its own incident cell.

Thus the complete actual constraints form a periodic graph of equalities of binary-valued maps, including all corner and side coincidences. The original zero-AAA/all-curved field supplies an infinite solution; in the symmetric B case first canonicalize its duplicated profiles. The independently reviewed binary-equality finite-cover theorem gives a solution on a finite-index cover. Its full native periodic labels enter settled actual metric development, yielding a plane tiling with nonzero translation, after squaring a possible glide. This constructs a periodic extension from actual existence; it does not infer an infinite tiling from a finite local table.

## Exact finite proof obligation and replay

Domain fixed before enumeration: two A words, two periodic species phases, eight cells per species base, all twelve indexed placements per cell; plus one symbolic closure identity. Questions: are A fibres size two, do each B metric branch and the symmetric-profile quotient have size two, and are all marked native indices correct? A contrary count would block this binary route rather than justify search expansion.

[Producer](../searches/five-one-all-mask-no-cross-binary-lift.py), [certificate](../certificates/five-one-all-mask-no-cross-binary-lift.json). It reconstructs native sides by endpoint sets, enumerates all thirty-two representative cells, verifies both native words and both bases, the marked opposite side roles, curved masks, all branch sizes, the symmetric B combined profiles, and the exact closure identity. No solver, numeric acceptance, actual polygon search or timeout is used.

    mise exec -- conda run --no-capture-output -n arisearch python research/searches/five-one-all-mask-no-cross-binary-lift.py --check research/certificates/five-one-all-mask-no-cross-binary-lift.json

Result: PASS. The finite obligation is unchanged by replacing metric
noncollision with unused contact support: its input is the derived
no-AAA/all-curved field. Producer/certificate scope metadata now explicitly
states that all metric aliases are retained. The count/sparse-limit and
selected-line arguments are analytic; no finite certificate alone proves
them. The independent review and its checker audit support preservation, sparse removal,
combinatorial direction propagation, the global phase recurrence, actual B
reflection reduction, and the pairwise angle encoding; their verdict is VALID.

## Scope and all-metric use

The support theorem covers both all-mask A words at every actual metric
whenever an actual saturated field uses no AA22 seam. The original metric
noncollision stratum remains a corollary. For A001122, the independently
reviewed used-AA22 lemma supplies the other case; their composition is in
[five-one-001122-all-metric-periodic-escape.md](five-one-001122-all-metric-periodic-escape.md).
A010122 requires its own used-seam theorem. Neither the support theorem nor
its corollaries settle another B multiplicity, another angle line, general
pentagon pairs, or the original two-convex-tile problem.
