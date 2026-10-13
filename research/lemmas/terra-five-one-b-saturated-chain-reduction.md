# A five-plus-one B angle count gives a saturated B-chain limit

Date: 2026-10-13. Status: [fresh independent hostile review VALID](../reviews/terra-five-one-b-saturated-chain-reduction-fresh-hostile-review.md); exact identity/palette checker PASS. This is a structural reduction and two-word
exclusion, not a chain periodicity theorem or global solution.

## Changed family and exact star language

Let112.5<x<126 degrees, x!=120. Set

    y=720-5x, z=4x-360, r=360-2x, s=360-2y=10x-1080.

Let actual strictly convex A have two corners of each x,y,z and B have five
corners r and one s, in arbitrary actual metrics. A angles sum720 and
5r+s=720. All angles lie strictly between0 and180 and all five values are
distinct. Their slopes in x are1,-5,4,-2,10 and all equal120 atx=120.
Thus every nonidentity triple equation has its only possible root120.
The complete trivalent star language on this family is exactly

    AAA=(x,y,z), AAB0=(x,x,r), AAB1=(y,y,s), ABB2=(z,r,r).

The small exact checker exhausts all35 triples of these five angle types,
retaining exactly those four coefficient identities. In particular there is
no BBB star. The departure from B two-of-each multiplicities is essential;
the reviewed complementary ternary one-B classifications do not apply here.

Use the reviewed [defect-free hexagon limit](hexagon-limit-and-periodicity.md)
and its whole-side/trivalent compactness and uniform boundary estimates.
Any admitted original tiling supplies such a field, without restricting its
original partial contacts, rotations or reflections.

## Local BB degree capacity

Write B native word(s,r,r,r,r,r), with special s corner0. Any BB side has ABB2
at BOTH endpoints, so neither endpoint can be s. Thus only native sides1,2,3,4
are eligible. Two adjacent BB sides would make a BBB vertex at their shared
B corner, impossible. The four eligible sides form a path of length4; an
independent set has size at most2. Every B therefore has BB-degree d_B<=2.
The saturated pairs are exactly native masks

    {1,3}, {1,4}, {2,4},

or eligible-path labels {0,2},{0,3},{1,3}. Labels must not be interchanged.

## Uniform window balance forces sparse deficient B tiles

For a translated square Q_R, count tiles by centroid as N_A,N_B and stars
inside Q_R as Y0,Y1,U,Z for AAB0,AAB1,AAA,ABB2. All identities below have
uniform O(R) boundary errors, because fixed diameter/positive area bounds the
number of affected tiles and native incidences in a fixed-width boundary strip.
Counting native A0 and A1 corners gives

    2N_A=2Y0+U+O(R), 2N_A=2Y1+U+O(R),
    Y0-Y1=O(R).

The single B_s corner occurs only at AAB1, hence Y1=N_B+O(R).
Counting the five B_r corners gives5N_B=Y0+2Z+O(R).
Every ABB2 star is an endpoint of a BB side; each BB side has two endpoints
and each BB side is counted twice by its two incident B cells. Therefore

    Z=sum_B d_B+O(R)=2N_B-D_R+O(R),
    D_R=sum_(B centroids in Q_R)(2-d_B)>=0.

Substitution yields the useful deficiency identity

    Y0=N_B+2D_R+O(R).

Together with Y0=Y1+O(R)=N_B+O(R), this gives D_R=O(R), uniformly in every
translated square. Each degree0/1 B has positive integer deficiency, so their
centroids have a uniform O(R) count. No frequency or species-density premise
is used; AAA counts are neither assumed absent nor removed by a corner weight.

## A translated limit saturates all remaining B cells

For radiusL, use a separated grid of candidate clean disks of radiusL+D in a
large square, where D bounds diameters. Quadratically many disjoint disks
compete with only linearly many deficient B centroids. A clean disk exists.
Its radiusL interior meets no deficient B tile, because any such tile meeting
it has centroid within L+D. Translate these disks to the origin and letL grow.

Indexed placement compactness of the actual defect-free field gives a plane
limit. Whole-side contacts, trivalence and native star labels persist by the
reviewed uniform sector-disk separation argument. Each limiting B therefore
retains degree2 from approximants; no partner tile can coalesce or vanish
locally, and all native side partners remain whole-side partners.

If B disappears, the pure A limit gives a monohedral periodic escape by the
imported unrestricted convex-hexagon theorem. A pure B limit is impossible
because its trivalent vertices would require BBB, absent from the retained
language. Otherwise the limit is genuinely mixed and EVERY B has exactly
two B neighbours. Consequently the B-adjacency graph is a disjoint union of
finite cycles and bi-infinite chains. Neither type is claimed to tile or
admit a periodic extension by this graph description alone.

## Eleven A palettes: two native words are now excluded

At a saturated B vertex the necessary adjacent A corner colour is1 at s,
2 at an r corner incident to a BB side, and0 at the remaining r corner.
Thus the four AB sides have these required unordered endpoint pairs:

    mask{1,3} or{2,4}: 22,02,01,12;
    mask{1,4}: 02 and12 only, twice each.

An actual AB whole seam must match both endpoint colours, so the native A
palette must contain all pairs required by its mask, irrespective of lengths.
Among all11 bracelets of001122:

*001221 lacks02 and011022 lacks12: neither supports ANY saturated mask;
*001122 and010122 support all three masks;
*001212,002112,010212,011202,012012,012021,012102 support only{1,4}.

For the first two excluded words no saturated mixed limit exists. Therefore
any tileable pair in either of those two native A domains has a pure A limit
and a monohedral periodic escape, at every actual metric and every x in the
stated interval except120. Other nine native words remain open in this family.

## Early exact native fan and closure obligations

A saturated B has precisely two AAB vertices, at its s corner and at its
unpaired r corner, and four ABB vertices. On every AB side enumerate the
native A side choices whose endpoint colours equal the required pair.
Different endpoints give one placed orientation per native side; equal
endpoints give both orientations. Across9 surviving A words,3 masks and12
indexed B placements this leaves1392 partial four-A tuples BEFORE metric
filtering. This is a finite next domain, not a completed extension search.

At each of the two AAB vertices, the two chosen A corners must share equal
native AA arm lengths, while their other arms equal the prescribed B AB-side
lengths. At each ABB vertex, its chosen A2 corner supplies an exact required
exposed AB-arm length to the neighbouring B. These are necessary local
conditions; the two neighbouring B native placements and their saturated masks
still require explicit compatible BB endpoint/star tests.

The earliest geometric gate is inexpensive. Let R=180-r=2x-180 in(45,72).
With B native side0 directed along1, its sidej has unit direction exp(ijR).
The two unknown BB lengths are determined uniquely by polygon closure once
the four AB lengths are fixed. The BB direction separations are2R for masks
{1,3}/{2,4} and3R for{1,4}. Neither is a multiple of180 in this interval
except3R=180 atx=120, explicitly excluded. Hence the two-column closure matrix
is invertible. Its exact solution must be positive and the actual closed
polygon convex before any chain expansion is justified. This supplies a
concrete exact attack; it does not assert all1392 tuples pass geometry.

## Replay and status

[Small exact checker](../reviews/verify_terra_five_one_b_chain_palette.py).

    mise exec -- conda run --no-capture-output -n arisearch python research/reviews/verify_terra_five_one_b_chain_palette.py

PASS35 identities,3 masks,11 A palettes,9 surviving words and1392 partial
AB tuples. Standard-library integer coefficient/equality counting only;
no solver, seed, timeout, source enumeration or numerical acceptance.
The uniform-deficiency and saturation extraction are analytic and require
fresh hostile review. The route remains an ACTIVE B-chain reduction with
local native/closure obligations, not a proved periodicity mechanism.
