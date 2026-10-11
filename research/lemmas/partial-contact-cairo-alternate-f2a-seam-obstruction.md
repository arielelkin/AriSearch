# A two-ended seam invariant excludes the alternate f=2a Cairo resonance

**Status:** freshly independently hostile-reviewed **VALID**, with complete
no-solver reconstruction; see [review](../reviews/partial-contact-cairo-alternate-f2a-seam-review.md). This is a new fixed-ratio unrestricted
untileability theorem, not a main-target resolution. Do not infer reviewed
status from the earlier angle-marginal reduction.

## Exact pair and claim

Let w=sqrt3 with1<w<2 and put, for any scale a>0,

    k=(20w-11)/13, b=ka,
    c=((3+w)a+(1-w)b)/4,
    d=((3-w)a+(1+w)b)/4,
    e=(w-1)(a+b)/2, f=2a.

Take Cairo pentagons P=(a,b,c,d,e), Q=(a,d,b,c,f), in the side direction
order0,90,150,240,300degrees. Their native angles after sides are
(90,120,90,120,120). The coordinates and strict convexity are those
verified in [the complete alternate domain](partial-contact-cairo-alternate-resonance-reduction.md).
Their four arm values are distinct and ordered c<a<d<b; e!=f.

**Theorem.** No plane tiling by this pair exists, including all rotations,
reflections, unrestricted partial contacts, and omission of either species.

## Complete finite contact states

The reviewed alternate-domain reduction gives six distinct event sums,
with components{a,c},{b,d}. At this ratio only f can host a T and its
bank lengths must be(a,a). Every P e is whole. Each Q f may independently
be whole or split into(a,a); no all-hosted assumption is inserted.
Native a,b may independently have one T at distance c,d respectively
from their120 endpoints. The pieces are c,(a-c) and d,(b-d), reversed
when the native orientation runs90-to120. Native c,d stay whole.

This gives all12 necessary augmented placement variants: four flags for
P, and four flags times the whole/hosted choice for Q. Each variant is a
contact state of one original shape, not a marked new prototile. In each
augmented boundary keep the actual native and straight subdivision corners
in order, with their actual directed side indices. The domain contains76
such typed corner slots. No variant is assumed to occur.

Every ray color records its exact piece length and the number of120
endpoints on that piece. A120 corner cannot meet90 or180, so both incident
tiles give the same color to an actual shared piece. Every actual star
is120^3,90^4, or180+90+90.

One further necessary native-side fact is used: a ray separating two90
corners starts along two90-to120 native arms. The first120 endpoint cannot
lie inside the other arm. Thus the native arms are equal and whole matched,
and their shared piece ends at120. This applies at a T's perpendicular
seam and at a90^4 star. Therefore every90/90 ray has exactly one120
endpoint, rather than ending at a straight artificial subdivision.

## Oriented stars and two-ended seam data

For each typed corner slot there are two possible cyclic orientations,
corresponding to a reference copy or its reflection. They order its two
actual indexed incident sides, resolving which reference endpoint of each
side is at the current vertex. Enumerate cyclic sequences of3 or4 oriented
corners with angle total360, equal colors on every adjacent ray, and the
preceding90/90 full-arm condition. Identify only cyclic changes of the
starting corner. Repetition of a typed slot from different occurrences is
allowed. The resulting exact necessary domain contains2617 oriented stars.
No finite local configurations are assumed to extend globally.

A typed edge slot is(s,i), where s is the augmented variant and i its
indexed side piece. Across an actual shared piece let the slots be x,y
and let px,py in{0,1} indicate which reference endpoints coincide at the
current vertex. Set parity=px xor py. If x<y in lexicographic order, the
seam key is(x,y,parity), and its current sign is+1 for px=0 and-1 for
px=1. If y<x use y as the canonical slot and its endpoint flag instead.
At the other geometric endpoint both flags reverse, the key is unchanged,
and the sign changes. These seam contributions cancel **exactly**, with
no assumption of translational symmetry or existence of frequencies.

For x=y and parity0, both flags agree, so the same sign rule is unambiguous
and again changes at the other end. For x=y and parity1, the two endpoints
have the same unordered slot description and no distinguished first
occurrence. Define its seam potential to be zero and omit its imbalance
feature. Choosing one occurrence by the cyclic star order in this case
would be an invalid invariant. The retained model handles this case
explicitly. There are465 other seam keys, including harmless zero-feature
keys if multiple incidences cancel in a star.

For each oriented star t, let C_t be its typed-corner count vector and
S_t its signed seam vector. A variant's corner vector M_s has one copy
of each of its indexed corners. The finite necessary system is

    sum_t C_t x_t = sum_s M_s F_s,
    sum_t S_t x_t = 0,
    x_t>=0, F_s>=0, sum_s F_s=1.

Unlike numerical corner marginals, this keeps the actual native/augmented
side slot and ties the two ends of each possible tile-to-tile seam together.
It still overincludes possible global assemblies and therefore can only
provide an obstruction when infeasible.

## Retained rational certificate

[The exact certificate](../certificates/partial-contact-cairo-alternate-f2a-slot-edge-balance.json)
contains the variant list,76 indexed corners,2617 oriented stars, all corner
counts and signed seam features, and rational vectors W,Y satisfying

    W dot C_t + Y dot S_t >= 0 for every retained star t,
    W dot M_s = -1 for every one of the12 variants s.

All values are rational strings; direct Fraction arithmetic verifies these
2617 inequalities and12 equalities. W has13 nonzero entries, Y has107.
The certificate is a finite separating functional, not a tiling certificate.
The solver's UNSAT answer is not needed once this certificate and complete
necessary domain have been independently reconstructed.

## Infinite boundary proof

Suppose a tiling exists and augment each actual tile at all its actual T
points. This assigns each occurrence one of the12 states, with its native
indices and actual side flags. Select native tiles whose interiors meet
int Q_R, and let N be their number. The total W charge of all their
augmented corners is exactly-N.

At a complete selected star, add its signed Y seam potentials. The resulting
charge is nonnegative by the retained star inequalities. Any shared piece
with both endpoint stars complete has two opposite potentials and contributes
zero to the global sum. The exceptional identical-slot reversed-endpoint
case contributes zero at both ends by definition.

An incomplete star has a selected incident tile and an unselected incident
tile. It cannot lie in int Q_R, since the latter tile then has interior
points in the square and would have been selected. Every selected tile
incident there meets partial Q_R. Such tiles lie in the fixed maximum-
diameter strip about the boundary, with area O(R); disjoint interiors and
positive minimum tile area give O(R) boundary tiles. Each variant has
uniformly finitely many corners and side pieces, and the finite rational
weights W,Y are bounded. All incomplete corner contributions and all
uncancelled seam-end contributions are consequently O(R). In particular,
a seam whose other endpoint is an incomplete star is incident to selected
boundary tiles; there are only O(R) such seams. Point contacts, multiple
boundary components and holes do not affect this counting.

Thus nonnegativity of complete augmented star charges implies
-N>=-O(R), or N<=O(R). But selected tiles cover Q_R and have bounded area,
so N>=4R^2/Amax. This is impossible for large R. It excludes either
monohedral tiling as well, without a positive-density assumption for both
types. Scale a merely rescales the fixed strip constants.

## Replay, status and non-consequences

[Producer](../searches/partial-contact-cairo-alternate-slot-edge-balance.py):

    conda run --no-capture-output -n arisearch python research/searches/partial-contact-cairo-alternate-slot-edge-balance.py

Normal replay is read-only. The retained file was explicitly generated by
adding --output research/certificates/partial-contact-cairo-alternate-f2a-slot-edge-balance.json.
The finite domain is precisely the12 augmented variants and all oriented
actual-slot3/4-corner stars above, with no randomization, timeout, floating
arithmetic or assumed period bound. Sparse exact equation assembly changes
only runtime, not the domain. The complete rational dual is directly checked.

The independent review of the invariant, sign convention, complete star
enumeration and infinite cancellation proof returns VALID. The
[no-producer-import checker](../reviews/verify_cairo_alternate_f2a_slot_edge_independent.py)
returns PASS. This reduces the previous four unresolved alternate ratios to
k in{w,1+w,1+4w/3}. No claim of existence or periodicity at those ratios,
and no main-target impossibility or novelty claim, follows from this theorem.


The later independently verified [complete alternate-family classification](partial-contact-cairo-alternate-classification.md)
settles every remaining ratio described above: all except1+4sqrt3/3 are
untileable, and that ratio has a periodic tiling. Earlier remaining-gap
phrasing records this intermediate theorem's original scope.
