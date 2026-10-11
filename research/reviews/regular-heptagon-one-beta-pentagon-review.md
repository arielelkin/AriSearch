# Fresh hostile review of the regular-heptagon one-beta obstruction

**Verdict: valid.** This is an analytic review of
[regular-heptagon-one-beta-pentagon-obstruction.md](../lemmas/regular-heptagon-one-beta-pentagon-obstruction.md),
developed by other researchers. No finite computation or external
monohedral classification is needed. The reviewed
[all-obtuse forcing theorem](../lemmas/obtuse-edge-forcing.md) is an explicit
dependency; the remaining contact and closure arguments are checked below.

Both alpha=4pi/7 and beta=5pi/7 are strictly obtuse and below pi.
The forcing theorem therefore excludes partial native-side matches and
forces three genuine corners at every tiling vertex, even under the
unrestricted original contact rules. Of the four possible triple angle
multisets, only alpha,beta,beta sums to2pi. In particular every vertex
has precisely one alpha corner.

Every P side has endpoint types alpha/alpha or alpha/beta. In a whole
P-to-P contact, an alpha/alpha side necessarily matches an alpha endpoint
of the other P at one end, since that other P has only one beta corner.
This gives two alpha sectors and is impossible. Both matched P sides
must therefore be alpha/beta. Their endpoint correspondence must reverse
the types: a beta/beta correspondence at one end would produce an
alpha/alpha correspondence at the other. Thus each PP contact is incident
to the unique beta vertex on both copies, with the neighboring P supplying
alpha at that vertex. No assumption of equal PP lengths or unreflected
copies is used.

At P's beta corner, two Q side neighbors would supply three beta sectors.
Two P side neighbors would each supply alpha by the preceding PP rule,
giving two alpha sectors. Exactly one side neighbor is therefore P and
the other Q. Every PP contact is incident to that beta corner, so every
P has exactly one PP side. Its other four complete native sides meet Q
and have Q's unit side length. This is a pointwise deduction, without
frequency, saturation, or a defect-free limit.

Omitting a prototile cannot escape the deduction. A Q-only tiling has
no alpha sector at any native vertex. If P occurs but Q is omitted,
both neighbors at P's beta vertex would be P, which was just excluded.
Hence any hypothetical admitted tiling contains P and the four-unit-side
constraint applies to a selected P copy.

Label its beta vertex0 and traverse counterclockwise. The four alpha
vertices give exterior turns3pi/7, so, after rotation, the side directions
are 0,3pi/7,6pi/7,9pi/7,12pi/7. The potentially nonunit PP side is
incident to vertex0 and is side0 or side4. Reflecting the placed copy
and reversing its vertex traversal interchanges these two cases while
retaining the beta-first angle word. This is allowed under the stated
isometry rules and does not assume that P itself has a mirror symmetry.

With the arbitrary PP length on side0, closure requires

    L + sum_(j=1)^4 exp(3j*pi*i/7)=0.

The imaginary part of L is zero. Summing the elementary telescoping
identity 2sin(t/2)sin(jt)=cos((j-1/2)t)-cos((j+1/2)t) gives

    sum_(j=1)^4 sin(jt)=sin(2t)sin(5t/2)/sin(t/2).

At t=3pi/7 this equals

    -sin(pi/7)sin(pi/14)/sin(3pi/14) < 0.

The numerator factors and denominator are all strictly positive. No
positive, zero, or negative real choice of L could close these directions.
The required P therefore cannot exist. This proves the claimed
untileability for arbitrary positive side lengths of P.

The regular-n corollary is also correct. For a pentagon with four alpha
corners and one regular-n beta corner, the angle sum gives
alpha=(n+1)pi/(2n). For n>=8 both angles remain strictly obtuse. If a
trivalent star contains p alpha sectors, direct substitution into
p*alpha+(3-p)*beta=2pi gives

    p=2-2/(n-5).

For every finite n>=8 this lies strictly between1 and2, so no integer
star is possible. The exceptional n=7 value is p=1 and is exactly the
metric case proved above. For n=5 both angles equal108 degrees; neither
an integer number of those angles nor that number plus one straight
sector gives a full star. For n=3,4,6, the regular Q already has its
standard periodic monohedral tiling, which is permitted when P is omitted.

The unequal-side equiangular heptagon in the existing
[two-angle periodic witness](../counterexamples/two-angle-5-7-periodic-instance.md)
does not contradict the result: this proof specifically forces the four
PQ sides of P to share Q's common side length. No classification of other
pentagon angle words or irregular heptagons follows. No substantive defect
was found, and no code or implementation-mirroring test was added for this
entirely analytic proof.
