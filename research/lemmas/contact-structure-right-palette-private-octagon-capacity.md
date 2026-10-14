# One-right pentagon / equiangular octagon: private-side capacity

Date: 2026-10-13. Status: independently hostile-reviewed VALID; [review](../reviews/contact-structure-right-private-capacity-review.md).
This is an unrestricted necessary metric condition for a new angle family.
It neither resolves the original target nor establishes tileability.

## Theorem

Let P be any genuine compact convex pentagon with one angle pi/2 and four
angles 5pi/8. Let Q be any genuine compact convex octagon with eight angles
3pi/4. Lengths are arbitrary, and all isometries, partial contacts and omission
of a prototile are initially permitted. Let k be the number of native SIDE
SLOTS of Q whose lengths occur nowhere among the five native side lengths
of P; repeated Q lengths still count once for each native slot.

If {P,Q} tiles the plane, k<=2. Consequently if Q has eight pairwise distinct
native side lengths, {P,Q} does not tile the plane, for any metric P with
this angle word. Neither distinctness nor a rationality assumption on P is
required. This obstruction permits all right-angle partial contacts.

## Complete local angular language

Express angles in units pi/8: P acute=4, P obtuse=5, Q=6. Full native stars
solve 4a+5b+6c=16. The complete nonnegative integer solutions are

    (a,b,c)=(4,0,0),(0,2,1),(1,0,2).

A vertex in a native side interior has one straight sector; its other sectors
solve 4a+5b+6c=8, whose only solution is (2,0,0). Two straight sectors
cannot coexist with a positive native corner. Therefore every nonnative
subdivision vertex consists of a single flat host and two P-right corners.
In particular neither a P-obtuse corner nor a Q corner can lie inside
another native side.

Let x count the two-P-obtuse/one-Q stars, y the one-P-right/two-Q stars,
z the four-P-right stars, and t all flat/two-P-right stars. Count tile
centroids and star locations in any square of side 2R. Then uniformly,

    4p=2x+O(R),    8q=x+2y+O(R),
    p=y+4z+2t+O(R),
    y=4q-p+O(R),    p=2q+2z+t+O(R).             (1)

The O(R) terms come only from bounded-width boundary strips. Minimum tile
area and bounded diameter bound tiles in these strips; each tile has finitely
many native corners. Every star is anchored at a native corner, so star counts
in strips have the same bound. No frequency limit is used.

## The whole-contact versus host resource dichotomy

Every positive-length Q-Q contact is a whole native side of both tiles.
If a contact ended in the relative interior of either native side, a Q
corner would lie there, forbidden by the flat-star language. At each endpoint
of a Q-Q side the two Q angles occupy 3pi/2 and the remaining sector is the
unique P-right corner. Conversely each y star is an endpoint of exactly one
Q-Q side: the two Q sectors are consecutive in this trivalent star.
If e denotes the number of Q-Q side contacts, counted once by midpoint,

    2e=y+O(R).                                             (2)

Consider one private-to-P native Q side. If it contacts Q at all along a
positive interval, that interval covers the entire side by the previous
argument. Otherwise finitely many P neighbor contact intervals cover it.
If there were just one neighbor covering the entire Q side, its matching
P native side would contain that side. Its endpoints cannot strictly extend
beyond the Q endpoints, because those endpoints would be Q corners inside
a P side. Thus it would be a full equal-length match, contrary to privacy.
There must be an interior junction of P contact intervals. At that junction,
Q is the flat host and the opposite two corners are P-right corners.

Select one hosted flat vertex from every private Q side not wholly matched
to Q. Distinct native Q sides yield distinct selected vertices: a flat/native
star has just one flat host, and a flat vertex lies in the relative interior
of only one native side of that host. Write t_Q for Q-hosted flat vertices.
Counting private sides and their two possible resource assignments gives

    kq <= 2e+t_Q+O(R) <= y+t+O(R).                         (3)

The first term counts all Q-Q side incidences, so it may overcount nonprivate
sides, which is harmless. The second counts selected hosts by an injection.
Combining (1)-(3),

    kq <= 4q-p+t+O(R) = 2q-2z+O(R) <= 2q+O(R).

If k>=3, this forces q=O(R). Equation (1) and y>=0 also give p<=4q+O(R),
hence p=O(R). But bounded tile areas and coverage give p+q=Omega(R^2),
a contradiction. This includes omitted or hypothetically zero-density types.
Thus k<=2. Eight distinct Q lengths can match at most five distinct P lengths,
so at least three Q slots are private, proving the stated corollary.

## Adversarial checks and limits

Privacy is absence from ALL P native side lengths, not just sides selected
by a desired trivalent template. Hosts may be P or Q; t_Q<=t includes that
possibility. The four-P-right stars are retained with the favorable term -2z.
A private Q side is not automatically unsplit: the proof explicitly charges
its subdivision to the same acute-corner resource appearing in (1).

The proof does not use full-edge forcing for the whole tiling. It derives
full Q-Q matching only, and leaves Q-P and P-P partial contacts admitted.
Repeated Q lengths count by slot, not distinct value. k<=2 is necessary only;
it does not imply global extension, a periodic escape or an aperiodic pair.
The exact symmetric periodic carrier satisfies k=0 and so survives the bound.

No computational proof component is used. The two displayed Diophantine
angle equations are solved analytically over their complete finite domains.
No novelty claim is made, pending primary-literature comparison.

## Later unrestricted local refinement

The subsequently reviewed
[native reduction](contact-right-angle-unrestricted-native-reduction.md)
proves t_Q=0 and all contacts involving Q whole. Every private Q side is
therefore Q-neighbor labeled, and its local native word permits at most two
such slots with cyclic distances three or four. Thus two private slots at
cyclic distance one or two already imply untileability, without a frequency
argument. Exactly two allowed private slots fix every Q copy QQ mask; the
native corner ledger then makes full four-right and flat stars O(R) uniformly,
which does not assert their complete absence. The earlier global side/host
resource argument above remains valid and independently reviewed, but this
later local parity gives stronger contact and native-position information.
