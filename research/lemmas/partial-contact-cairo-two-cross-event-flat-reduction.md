# Complete contact-event reductions for two specified two-cross Cairo patterns

**Status: independently hostile-reviewed VALID for the stated finite reduction; see [the fresh root review](../reviews/partial-contact-cairo-two-cross-event-flats-review.md).** This is a restricted Cairo-family result.

Let P=(a,b,c,d,e),Q=(A,B,C,D,f) have positive Cairo sidewords, with w=sqrt3,

    b-c=w(d-a), e=wc+d-2a,
    B-C=w(D-A), f=wC+D-2A.

Each species has four distinct native90-to120 arms. The only cross arm
identities are either (I) a=A,b=B or (II) a=A,c=C.
All isometries and arbitrary partial contacts are admitted.

**Claim I:** under pattern(I), no plane tiling exists.
**Claim II:** under pattern(II), any tiling metric lies in one of the
thirty-eight open event flats retained in the exact certificate: twelve
of homogeneous dimension2 and twenty-six of dimension1. No surviving
stratum is asserted to extend to a tiling.

A native arm slot has perpendicular complement other=(1,0,3,2,5,4,7,6).
Its actual T-bank sums are S_i={arm_i+arm_j:other_i=other_j in length}.
By the reviewed two-T switch/contact theorem, opposing unequal arm rays
require S_i intersect S_j; equal arm lengths are allowed whole contacts.
An eH/arm_i ray requires eH in S_i, and eH/eG requires equality. This is
only a safe necessary compatibility relation and is not transitively
closed. Each native120 corner must occur in some compatible120 triple.

Under(I), equal perpendicular labels produce only six self-bank totals
2x. Under(II), they also produce Pb+Qb and Pd+Qd. On the exact cross arm
pattern, a self-total equality forces an undeclared arm equality. A cross
total compared with twice one of its own bank members does the same.
Thus omitting just these event/event forms cannot lose a valid metric;
every such omitted comparison is retained by index in the certificate.
All other event/event comparisons, every e/f event comparison and e=f
are included. There are exactly13 forms under(I),26 under(II), in a
four-dimensional homogeneous closure kernel.

For each metric take all arrangement forms that vanish there. Their full
intersection gives a flat, and the metric lies in its open stratum avoiding
all other proper forms. Therefore all metrics, including every event
resonance and nongeneric original metric, are covered by the full finite
intersection lattice. The producer enumerates canonical exact RREF flats
by adding every nonidentity form. Negative native-corner results do not
prune descendants, since an extra identity can create new contacts. Only
an undeclared arm identity or an exact positive-cone impossibility prunes,
both hereditary. A dimension1 flat has no positive proper descendants.
This proves the complete finite domain, without any codimension cutoff.

Every positive flat retains an actual positive metric. Every empty flat
has an exact Gordan certificate: ten nonnegative weights summing to1
whose combination of the ten native length forms is zero. If all lengths
were strictly positive the weighted sum would be positive, contradiction.
Strict positivity on the other flats is open; undeclared arm/proper event
forms are not identities, so their finite union cannot cover the positive
cone. Positive witnesses need not themselves be generic to establish that
an open exact-pattern stratum exists.

The native120 filter enumerates all56 unordered triples from the six
native120 corner types with all8 independent reflections. Every unordered
triple admits both cyclic orders among these reversed choices, so no
ordered star is omitted. Actual native compatibility identities are
constant on an open flat stratum. A missing native corner is impossible
in a tiling using that species. Both species must occur: either alone
has four distinct private arms and cannot tile by the independently
reviewed finite private-arm theorem.

The complete exact record has107 flats under(I):77 hereditary extra-arm
identities,2 Gordan-empty cones and28 missing-native-corner strata.
There is no local survivor. The exhaustive domain and necessary filter
therefore imply Claim I. Under(II),547 flats split into266 extra-arm,
92 Gordan-empty,151 missing-corner and38 surviving strata, proving Claim II.
Every deeper stratum of a survivor was also visited or safely pruned.

All surviving dimension2 sidewords, strict ratio intervals, excluded
privacy/event cut values and arm-order chamber fixtures are retained.
Dimension1 forms and positive fixtures retain exact metric rays directly.
The conclusion neither assumes local legality implies extension nor
supplies periodicity for the separated survivors. Other two-cross native
patterns and internally repeated arms lie outside the theorem.

Dependencies: [private-arm theorem](partial-contact-cairo-private-arms.md),
[actual two-T contact invariant](partial-contact-cairo-two-t-switch.md).
Supporting [producer](../searches/partial-contact-cairo-two-cross-event-flats.py),
[exact certificate](../certificates/partial-contact-cairo-two-cross-event-flats.json),
[complete search record](../searches/partial-contact-cairo-two-cross-event-flats.md).
