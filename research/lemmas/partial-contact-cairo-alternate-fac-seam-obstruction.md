# A two-ended seam invariant excludes the alternate f=a+c Cairo resonance

**Status:** freshly independently hostile-reviewed **VALID** with exact
complete-domain reconstruction; see [review](../reviews/partial-contact-cairo-alternate-fac-seam-review.md).
The retained rational dual has been replayed with exact Fraction arithmetic
on every listed star and tile variant. The reviewed f2a/e2c seam mechanism
is reused, but this separate complete fac domain requires its own review.

## Exact pair and claim

Let w=sqrt3 with1<w<2 and put, for any scale a>0,

    k=w, b=ka,
    c=((3+w)a+(1-w)b)/4,
    d=((3-w)a+(1+w)b)/4,
    e=(w-1)(a+b)/2=a, f=a+c.

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
bank lengths must be(a,c) in either order. Every P e is whole. Each Q f may
independently be whole or split in either bank order; no all-hosted assumption
is inserted. The equality e=a introduces no extra admissible contact: whole
e has two120 endpoints, whereas whole native a has one120 endpoint.
Native a,b may independently have one T at distance c,d respectively
from their120 endpoints. The pieces are c,(a-c) and d,(b-d), reversed
when the native orientation runs90-to120. Native c,d stay whole.

This gives all16 necessary augmented placement variants: four flags for
P, and four flags times the whole/two hosted choices for Q. Each variant is a
contact state of one original shape, not a marked new prototile. In each
augmented boundary keep the actual native and straight subdivision corners
in order, with their actual directed side indices. The domain contains104
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
allowed. The resulting exact necessary domain contains8253 oriented stars.
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
explicitly. There are1045 other seam keys, including harmless zero-feature
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

[The exact certificate](../certificates/partial-contact-cairo-alternate-fac-guided-slot-edge-dual.json.xz)
(xz-compressed; `xz -dk` to read)
contains the variant list,104 indexed corners,8253 oriented stars, all corner
counts and signed seam features, and rational vectors W,Y satisfying

    W dot C_t + Y dot S_t >= 0 for every retained star t,
    W dot M_s <= -1 for every one of the16 variants s.

All values are rational strings; direct Fraction arithmetic verifies these
8253 inequalities and16 inequalities. All16 variant charges in fact equal-1. W has35 nonzero entries, Y has413.
The certificate is a finite separating functional, not a tiling certificate.
The solver's UNSAT answer is not needed once this certificate and complete
necessary domain have been independently reconstructed.

## Infinite boundary proof

Suppose a tiling exists and augment each actual tile at all its actual T
points. This assigns each occurrence one of the16 states, with its native
indices and actual side flags. Select native tiles whose interiors meet
int Q_R, and let N be their number. The total W charge of all their
augmented corners is at most-N.

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

Thus nonnegativity of complete augmented star charges bounds the total selected tile charge below by-O(R).
Since that charge is at most-N, it follows that N<=O(R). But selected tiles cover Q_R and have bounded area,
so N>=4R^2/Amax. This is impossible for large R. It excludes either
monohedral tiling as well, without a positive-density assumption for both
types. Scale a merely rescales the fixed strip constants.

## Replay, status and non-consequences

[Producer](../searches/partial-contact-cairo-alternate-slot-edge-dual-discovery.py):

    conda run --no-capture-output -n arisearch python research/searches/partial-contact-cairo-alternate-slot-edge-dual-discovery.py fac

Normal replay is read-only. The retained file was explicitly generated with
--output research/certificates/partial-contact-cairo-alternate-fac-guided-slot-edge-dual.json.xz
(the producer writes xz when the path ends in .xz).
The finite necessary domain is precisely the16 augmented variants,104 typed
corner slots,8253 cyclic oriented stars and1045 seam keys. No period bound,
forced-host choice, or assumed density of a species occurs.

A floating optimizer is used solely to propose a dual vector. Its entries
are reconstructed as rational numbers, and every8253 star inequality and
all16 tile inequalities are verified with exact Fraction arithmetic before
the result is accepted or retained. A numeric infeasibility answer would
supply no conclusion; the producer falls back to exact solving. The original
full exact primal run and a separate support-discovery run were interrupted
as redundant after the exact rational dual was retained, and their unfinished
results are UNKNOWN, not UNSAT.

The fresh review and no-solver --kind fac checker return VALID/PASS.
This excludes the final open ratio k=w. Together
with the independently checked periodic construction at k=1+4w/3 and the
reviewed generic/four-other-resonance exclusions, it classifies this entire
alternate four-shared-arm family: the only tileable nondegenerate ratio is
k=1+4w/3, which has a periodic tiling. This family therefore cannot meet
the main branching target. No unrestricted classification beyond this
specified family and no main-target resolution follows.
