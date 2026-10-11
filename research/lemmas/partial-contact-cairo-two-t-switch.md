# Cairo two-T switches and an exact changed pair killed by endpoint compatibility

**Status:** proved and independently adversarially reviewed VALID (2026-10-10);
see [the hostile review](../reviews/partial-contact-cairo-two-t-switch-review.md). This is a
new necessary partial-contact invariant and one unrestricted untileability
certificate, not a resolution of the two-convex-tile problem.

## The native right-corner event set

All tiles have Cairo angles (90,120,90,120,120) after sides(a,b,c,d,e).
Their right-corner arm pairs are(a,b),(c,d); isolated120 corner is(b,c).
Every full star is90^4 or120^3; every half star is90^2. In particular120
cannot occur inside a native side or coincide with90.

For a finite protoset, an oriented90-corner slot consists of a perpendicular
arm length u and its other arm length r. Its native90-to120 side u can pair
with any other such slot of the same length u. Call this a **right-corner
event**, with unordered bank multiset{r,s}, perpendicular length u, and
sum r+s. Identical slots from two copies are permitted. Events are a finite
necessary list of whole perpendicular seams; no extension is inferred.

At a T the perpendicular seam is whole: both native perpendicular arms
end120, so their first endpoint cannot occur inside the other arm. Thus
T banks always define an event. No private-length assumption is used here.

## Exact two-T switch invariant

Suppose two native arms start at the same120 star along the same ray, but
have unequal lengths m<M. The short arm ends at90 inside the long arm,
creating a T. Let n be the forward collinear arm of the other90 tile at this
T; its120 endpoint has ray coordinate m+n. The first event has banks{m,n}.

The long arm cannot reach or pass this120 endpoint: its own endpoint is90,
and a120 cannot lie inside a side or coincide with90. Thus M<m+n. Its90
endpoint at M lies inside the forward n arm and creates a second T. Let q
be the new forward arm at that T. Its120 endpoint must coincide with the
existing120 endpoint at m+n: either ordering puts120 inside a native arm.
Consequently

    m+n=M+q,    0<m<M<m+n,    0<q<n.

The second event has banks{M,q}. Their perpendicular lengths can differ.
No new native vertex can intervene on either shared open interval because
the two participating tiles cover both half-neighborhoods there. Thus this
argument does not assume that the original long arm had no subdivisions.

It follows that an unequal arm/arm ray match at120 requires two events
with equal bank sums, choosing unequal members m,M from their bank pairs.
This is a finite necessary numerical relation, independent of tiling size.

An e side with a T instead has its two120 endpoints at the two bank120
endpoints, and hence its length equals the event sum r+s. An e side without
a T is matched to a whole e side: an opposing arm would end90 internally
or coincide90/120, or its endpoint ordering would put120 inside a side.
Every native side has at most one T because the opposing forward arm from
one T ends120 and cannot end in the host interior, and both half-sectors
are already occupied before that endpoint.

## The exact pair

Let w=sqrt3, the positive root of t^2-3 with1<w<2, and put

    a=1, b=2, c=2w-1, d=w-1, e=3, f=3-w.

Define the two pentagons by ordered lengths

    P=(a,b,c,d,e),    Q=(a,c,d,b,f),

and side directions0,90,150,240,300 degrees. Exact vertices of any such
length word(A,B,C,D,E) are

    (0,0), (A,0), (A,B), (A-wC/2,B+C/2), (-E/2,wE/2).

Closure is equivalent to E=wC+D-2A and B-C=w(D-A), both satisfied for
P and Q. All lengths are positive, each polygon has five distinct lengths,
and all supporting-edge determinants are positive. They are noncongruent,
with private lengths e,f. P has right-pairs{a,b},{c,d}; Q has right-pairs
{a,c},{d,b}. This is a changed four-cycle of shared arms, outside the
private-arm theorem and the recorded scalene-Cairo periodic family.

## Finite event comparison and beta endpoint obstruction

The self-events have sums2a,2b,2c,2d. The cross-species events have banks
{b,c} for perpendicular a or d, and banks{a,d} for perpendicular b or c.
Their sums are b+c=2w+1 and a+d=w. Exact comparisons show all six numbers
2a,2b,2c,2d,b+c,a+d are distinct, and neither e nor f equals any of them.

Hence every native e/f side is whole matched to a same-species e/f side;
and every arm/arm ray match at120 has either equal lengths, lengths both
in{a,d}, or lengths both in{b,c}. These are necessary possibilities,
with no claim they all extend even locally.

Take any P e seam. At each of its120 endpoints both participating P tiles
use an e-adjacent120 corner, and each other incident arm is a or d. The
remaining120 tile K must therefore have both its incident side lengths
in{a,d}, because every matching arm ray preserves the two components
{a,d} and{b,c}. Neither incident side of K can be e or f: these sides
cannot host a T, cannot match an arm as a whole due to90/120 endpoints,
and cannot be shorter due to an interior120 corner.

Thus K must use its isolated120 corner. P's isolated arm pair is{b,c};
Q's isolated pair is{c,d}. Neither has both arms in{a,d}. This contradiction
excludes any P tile. If only Q were used, its distinct four arms satisfy
the separately reviewed private-arm theorem, so it cannot tile alone.
Alternatively repeat the same event comparison using only Q self-events:
unequal arm matches and e subdivisions become impossible, and its isolated
corner cannot form a threefold star. Thus the exact pair is untileable
under all isometries and unrestricted partial contacts, including species
omission.

## Exact replay, scope and gap

The checker
[partial-contact-cairo-two-t-switch.py](../searches/partial-contact-cairo-two-t-switch.py)
exhausts the eight oriented native right-corner slots and all their equal-u
pairings. It checks exact coordinate closure, side lengths, supporting
convexity, angle cosines, six distinct event sums, e/f exclusions, the
resulting finite arm compatibility relation, and the isolated-corner
obstruction. Replay:

    conda run --no-capture-output -n arisearch python research/searches/partial-contact-cairo-two-t-switch.py

Arithmetic is QQ(sqrt3); no randomness, timeout or tiling search is used.
The finite domain is exactly the two fixed polygons and their native slots.
The checker proves no unbounded theorem without the geometric switch
proof above. No certificate file is required for this small deterministic
computation. No primary-literature novelty claim is made.

These conditions need not hold for other Cairo pairs. Repeated event sums
with different bank multisets can create new arm compatibility, and e/f
values equaling event sums permit T-hosted e sides. Classifying those
contacts globally remains open. The killed pair does not constitute an
aperiodic construction or an unrestricted impossibility theorem.
