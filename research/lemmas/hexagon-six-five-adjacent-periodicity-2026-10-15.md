# Adjacent repeated sides also give a periodic hexagon escape

Date: 2026-10-15. Status: independently hostile-reviewed VALID;
[review](../reviews/hexagon-six-five-adjacent-hostile-2026-10-15.md). No novelty or
universal two-polygon impossibility claim is made here.

## Theorem

Let A and B be compact convex hexagons with nonempty interiors and six actual
corners each. Suppose A has six distinct native side lengths, and B has
exactly five distinct native side lengths, with its two equal-length side
slots adjacent in its cyclic boundary word.

If copies of A and B tile the Euclidean plane, allowing reflections and
unrestricted partial contacts, then the same shapes admit a doubly periodic
whole-native-edge tiling with a four-face flat-torus quotient consisting of
two A and two B faces. Thus this pair cannot be aperiodic under the definitions
of research-problem.md.

The reviewed [defect-free limit theorem](hexagon-limit-and-periodicity.md)
is the dependency removing partial contacts. The explicit four-face periodic
realization is the reviewed formal-symbol ring construction in Section 2 of
[the distinct-length theorem](hexagon-holonomy-distinct-lengths.md), also
reproduced in Sections 3-4 of
[the separation-two theorem](hexagon-six-five-separation-two-periodicity-2026-10-15.md).
The new finite calculation below accommodates repeated RAY lengths at a
trivalent vertex and does not assume an ordinary numerical graph triangle.

## 1. Exact corner convention and reduction

Index native sides by 0,...,5 cyclically. Corner i is after side i, between
sides i and i+1 modulo 6. Side i has endpoint corners i-1 and i. Use actual
corner indices 0,...,5 for A and 6,...,11 for B. In particular both B side
slots of the repeated length remain distinct native slots.

Apply the defect-free limit theorem to obtain an everywhere-trivalent
whole-native-edge tiling. Normalize the numerical length words to

    A=(0,1,2,3,4,5), B=(p,p,q,r,s,t),

where p,q,r,s,t are distinct. A's numerical corner graph is a simple six-cycle.
B's is the five-cycle p-q-r-s-t-p plus the loop p-p. A cannot tile alone in
the defect-free limit, since its distinct adjacent side lengths would require
a triangle in its six-cycle.

B cannot tile alone either. Its possible pure-B stars can have repeated
rays p,p,x and hence use only its p-p corner and its p-q or t-p corners;
or have all rays p. There is no three-distinct-length triangle in its
five-cycle. In particular its actual q-r corner cannot occur in any pure-B
trivalent star. Thus both types occur, and every actual corner of both
shapes occurs in some star.

Let k be the number of shared distinct numerical side lengths. Consider
an A-private length u, whose two distinct A-cycle neighbors are v,w. At
least one, say v, differs from B's repeated value p. A corner with lengths
u,v cannot be in a repeated-ray star: every repeated-ray star uses the
loop p-p, and hence all its other corner edges are p-x; here neither u
nor v equals p. Thus an occurrence of that actual A corner requires a
triangle on three distinct lengths. Since u has only neighbors v,w,
this requires the shortcut v-w. That shortcut cannot be an A edge, since
A's six-cycle has no triangle. It is therefore a B edge, so v and w are
both shared. This also applies if the other A corner u-w could have been
completed with repeated rays; only the selected u-v corner was needed.
Consequently private A values are isolated and there are at most three.
If there were three, A would alternate private and shared values and its
three required shortcuts would give a triangle on three distinct shared
values in B. The five-cycle plus loop has no such triangle. Hence k>=4;
and k<=5 because B has only five distinct lengths.

## 2. The complete numerical-word domain

For each k=0,...,5, choose k values from A's six length labels and append
5-k private B labels 6,7,... . Permute these five distinct values into the
roles p,q,r,s,t, retaining q<t to remove reversal. The word is (p,p,q,r,s,t).
Its equal adjacent pair fixes its cyclic starting slot; reversal swaps
(q,r,s,t) with (t,s,r,q). Thus exactly 5!/2=60 role assignments occur for
each chosen shared set, giving the complete 3,780-word domain:

    k:       0    1    2     3    4    5
    words:  60  360  900  1200  900  360.

For each word enumerate all multisets of three numerical ray lengths
{x,y,z}, allowing repetitions. A corner between each consecutive pair
must exist as an actual corner of A or B. Independently choose its actual
slot whenever more than one exists. The sorted triple of resulting corner
indices is a potential actual star, with repeated indices allowed. For
example, rays p,p,p give three copies of B's p-p corner; rays p,p,x give
that corner and two independently chosen p-x corners. An ordinary simple
triangle enumeration would omit precisely these cases and is insufficient.

Retain a numerical word only when these potential stars cover all twelve
actual corner indices. There are no survivors for k<4, forty-two for k=4,
and ninety for k=5. Up to dihedral relabeling of A and cyclic rotation or
reflection of B, they give twelve classes. The two numerical counts sum to
132, and the class sizes are included in Section 4's table.

## 3. Native-arm microstates and endpoint closure

A potential corner triple alone does not determine its rays when B's p-p
corner occurs. To retain every reflected and unreflected possibility, use
native-arm microstates as follows.

Choose the three actual corner occurrences in a cyclic order. At each
corner independently choose which of its two native sides goes to its
left and which goes to its right. These are the two choices of a Boolean
flip, even when the two numerical side lengths are equal. Retain a choice
only if the right arm of each corner has the same numerical length as the
left arm of the next corner. This specifies all three shared rays together
with the native side slots on both sides of each ray.

The implementation sorts the three corner indices and tests all eight flip
choices in that order. This is complete: for three objects every ordering
is a cyclic permutation of that order or its reversal, and reversing all
three left/right choices gives the same unordered native-ray pairing data
for the reversed order. This also applies when corner indices repeat.
No actual handedness restriction is imposed; arbitrary reflected copies
and the reverse cyclic order are included by this equivalence.

For every ray in such a microstate, follow each of its two actual native
side slots to that tile copy's far-end actual corner. Record the resulting
two corner indices as a MULTISET, since two different tile copies may have
the same native corner index. For instance, following side i from corner i
gives corner i-1; following side i+1 gives corner i+1, modulo 6 within its
type. Distinguishing B's equal slots is essential for this operation.

Let S be the set of actual corner triples occurring in a genuine tiling.
It covers all twelve indices and satisfies this necessary condition:
for every triple in S there is at least one microstate such that EACH of
its three far-end corner multisets is contained, counting multiplicity,
in some triple of S. The witnessing microstate is the one at an actual
occurrence of that triple. The same tile copies share a full side and meet
again at its far endpoint. Thus this implication does not presume that
arbitrary locally allowed stars can be assembled globally.

For any finite atlas, repeatedly discard a star if it has no microstate
whose three far-end pairs are supported by stars still in the atlas.
Every actual support S survives every deletion: its actual occurrence
supplies a witnessing microstate with all far stars also in S. Hence S
lies inside the final atlas. The iteration terminates because the atlas
is finite. For each surviving class then enumerate every subset of this
pruned atlas, retaining exactly the twelve-corner covers satisfying the
same simultaneous-microstate endpoint condition. This is the precise
finite support domain used below; it neither assumes nor concludes
infinite extension from an endpoint-supported subset.

## 4. Complete finite support classification

The exact enumeration gives the following table. A zero in the pruned-star
column means the entire atlas is eliminated. The last column counts all
endpoint-closed corner-cover subsets of the pruned atlas, without angle
feasibility restrictions.

| k | Representative cyclic B | Words | Potential stars | Pruned stars | Endpoint-closed covers |
|---|---|---:|---:|---:|---:|
| 4 | (0,0,1,6,2,4) | 12 | 9 | 4 | 1 |
| 4 | (0,0,1,3,5,6) | 12 | 9 | 4 | 1 |
| 4 | (0,0,1,3,6,4) | 12 | 9 | 4 | 1 |
| 4 | (0,2,5,3,6,6) | 6 | 7 | 0 | 0 |
| 5 | (0,0,1,3,2,4) | 12 | 11 | 6 | 3 |
| 5 | (0,0,2,3,1,4) | 12 | 11 | 0 | 0 |
| 5 | (0,0,2,4,5,3) | 12 | 11 | 0 | 0 |
| 5 | (0,0,1,3,5,4) | 12 | 11 | 6 | 3 |
| 5 | (0,0,1,3,5,2) | 12 | 12 | 4 | 1 |
| 5 | (0,0,2,1,5,3) | 12 | 11 | 0 | 0 |
| 5 | (0,0,1,5,2,4) | 12 | 12 | 4 | 1 |
| 5 | (0,0,1,4,2,5) | 6 | 10 | 0 | 0 |

There are eleven endpoint-closed covers in total. **Each contains a formal
four-triangle ring**, in actual corner slots. No residual deterministic
case and no angle-equation solver are needed in this adjacent-repeat case.

Here is the finite definition of the ring test. Select four different side
slots of B whose numerical values are distinct and shared with A. Match
them with their unique corresponding A slots. Give these four matches
formal common symbols, give every remaining slot a different private
formal symbol, and enumerate the formal corner graph. Retain the selection
if its four graph triangles partition the twelve actual corner slots.
The finite computation checks that at least one such four-triple set is
contained in each of the eleven closed covers. Splitting B's adjacent p
slots into different formal symbols is allowed: equal numerical lengths
need not have identical formal labels in the selected witness.

For transparency, the seven nonempty pruned atlases are, in the table's
order after dropping empty rows:

    {(0,6,7),(1,8,9),(2,3,10),(4,5,11)},
    {(0,6,7),(1,2,8),(3,4,9),(5,10,11)},
    {(0,6,7),(1,2,8),(3,9,10),(4,5,11)},
    {(0,6,7),(1,2,8),(1,8,9),(2,3,10),(3,9,10),(4,5,11)},
    {(0,6,7),(1,2,8),(3,4,9),(3,9,10),(4,5,11),(5,10,11)},
    {(0,6,7),(1,2,8),(3,4,9),(5,10,11)},
    {(0,6,7),(1,8,9),(2,3,10),(4,5,11)}.

Thus the final subset check involves at most 2^6 choices per representative.
The actual tiling's support is among these eleven covers, by Section 3.
Its contained ring triples are actual stars and have angle sums 2pi.

## 5. Geometric conclusion and union corollary

The contained formal ring has two private side symbols in each type and
four common symbols. Its corner graph consists of four edge-disjoint
triangles on a common four-cycle, each with one private insertion. Give
the cycle alternating bits. Take A0,A1,B0,B1, reflect B's reference if
needed to reverse the common cyclic order, pair private slots between the
two copies of their type, and pair each common x side of A_i to B_(i xor h(x)),
always reversing boundary endpoints. All numerical lengths match. The
result is a connected orientable surface with four faces, twelve edges,
and eight circular trivalent vertices: two for each legal ring triple.
Its Euler characteristic is zero and each vertex has angle 2pi. It is
therefore a compact flat torus. Its complete simply connected universal
cover develops isometrically onto the plane. The lifted faces give a tiling
by the original shapes, with a rank-two translation deck group. This is
the four-face doubly periodic witness asserted in the theorem.

Combining this result with the
[separation-two theorem](hexagon-six-five-separation-two-periodicity-2026-10-15.md),
the separation-three theorem, and the reviewed
[six-distinct/six-distinct theorem](hexagon-holonomy-distinct-lengths.md)
yields the following corollary, once each new component has completed its
independent review:

**Corollary.** If two convex hexagons each have at least five distinct side
lengths, and at least one has six distinct side lengths, then their pair
cannot be aperiodic. Whenever the pair tiles the plane under unrestricted
contacts and with reflections allowed, it admits a doubly periodic tiling.

Indeed a length occurring exactly twice among six sides has cyclic separation
one, two, or three, exhausting the five-distinct case; the six-distinct case
is the earlier theorem. The four-face quotient is asserted only in the
adjacent case here, not for every branch of that corollary.

## 6. Exact computation, review and limitations

The complete finite producer is
[hexagon-six-five-adjacent-gate-2026-10-15.py](../searches/hexagon-six-five-adjacent-gate-2026-10-15.py).
With explicit `--output` it writes [the retained certificate](../certificates/hexagon-six-five-adjacent-gate-2026-10-15.json),
including all 3,780-word counts, orbit representatives and counts, all actual
star triples with multiplicities, all simultaneous native-arm far-end-pair
assignments, pruned atlases, eleven retained supports, and their ring choices.

    mise exec -- conda run --no-capture-output -n arisearch python research/searches/hexagon-six-five-adjacent-gate-2026-10-15.py

The default command prints JSON without overwriting retained evidence.
The computation uses Python's standard library only. Its domain is fully
specified in Sections 2-4; all decisions use integer equality, finite
multisets and set operations. There are no solver calls, floating-point
angle decisions, stochastic seeds, timeouts, or bounded periodicity tests.
The unbounded geometric step is the reviewed defect-free theorem followed
by the explicit compact flat-torus construction. Independent verification of this new repeated-ray encoding and
classification PASSED; the fresh full proof review is VALID. Replay:

    mise exec -- conda run --no-capture-output -n arisearch python research/reviews/hexagon-six-five-adjacent-independent-2026-10-15.py

The theorem does not cover two five-distinct hexagons, a polygon with fewer
than five distinct side lengths, other side counts, or arbitrary pairs of
convex polygons. It is not a resolution of research-problem.md.
