# Fresh hostile review: the four-face mixed-word trial

Reviewer: `primary_literature`, 2026-10-09. This review covers **only** the
X/Y four-face branch of
[the shared three-angle artifact](../lemmas/new-angle-three-pentagon-private-length-counterexample.md),
[its enumerator](../searches/new-angle-three-pentagon-explore.py),
[the angle-model certificate](../certificates/new-angle-three-pentagon-mixed-word-angle-models.json),
and [the exact closure certificate](../certificates/new-angle-three-pentagon-mixed-word-closure.json).
The reviewer did not develop or modify the author proof. The positive105
and irrational-angle Y/Y witnesses are outside this review and have a
separate root audit.

## Exact claim and declared finite scope

Fix theta=105 degrees and gamma=150 degrees. The two native angle words,
at the starting vertex of each side, are

    X=(90,150,90,105,105), Y=(90,105,90,105,150).

The ansatz takes two labeled copies of each, independently allows reflected
references, and pairs all twenty **whole** native side occurrences in ten
seams reversing their face-boundary endpoint orders. Within this ansatz,
every angle-flat model is enumerated; its induced equal-length relations
do not permit both reference pentagons to have strictly positive closed
side-length vectors. No four-face orientable flat-torus tiling in this
declared ansatz therefore exists.

The claim does not exclude larger torus quotients, nonorientable four-face
quotients, nonperiodic plane tilings, or right-corner T-junctions. It does
not establish no tiling or aperiodicity for any unrestricted X/Y pair.

## Defect found and author repair independently re-reviewed

The original claim of four **distinct equality partitions** was incorrect.
The stored tuples

    (0,0,0,2,0,0,1,0,2,1),
    (1,1,1,2,1,1,0,1,2,0)

encode exactly the same equality relation, with class labels0 and1
interchanged. Their closure matrices are corresponding column permutations.
The original generator normalized by sorted union-find representatives,
which need not canonically label an equality relation by its first native
slot. This was a count/terminology defect, not a false metric infeasibility.

The reviewer reported it to root and the author without editing the proof.
The author retained all four raw labelings and all exact matrices/nullspaces,
corrected the proof and search record, and added explicit metadata:
four raw labelings, three distinct equality relations. First-occurrence
canonicalization now records the three relations. The independent checker
freshly rechecked the repaired metadata, every model's relation, each
closure record's canonical relation, and full coverage of all relations.
The repair resolves the defect without weakening or removing metric evidence.

## Reflection and finite-domain completeness

At105/150 degrees the only full native-sector stars are four90-degree
corners and105,105,150. This follows by enumerating sums of three or four
members of {90,105,150}; there is no mixed right/nonright full star. Thus
an endpoint of a full seam that is right on one side must be right on the
other. Each reference face has two right-to-nonright sides, two
nonright-to-right sides, and one nonright-to-nonright side. There are no
right-to-right native sides.

After reflection, the chosen positive face-boundary order has corner j
corresponding to original corner -j mod5, and side j corresponding to
original side -j-1 mod5. The distinction between these formulas is
essential; the enumerator and independent checker use the correct one.
This branch's corner convention is vertex-before-side, unlike some earlier
corner-after-side artifacts. No off-by-one identification was found.

There are initially sixteen reflection-bit assignments. Reflecting the
whole assembly toggles every bit and reverses native boundary indices,
giving a bijection between assignments with face0 reflected and unreflected.
Both geometrical mirror copies are permitted. Fixing face0 unreflected
therefore retains every possible model up to global reflection, leaving
eight assignments. This is not a reduction by a presumed polygon
self-symmetry. Arbitrary world rotations do not alter the native side
pairing possibilities.

Reversed endpoint order pairs each right-to-nonright side to exactly one
nonright-to-right side. All such choices are the8! bijections. The four
nonright-to-nonright sides have exactly three perfect matchings. There
are no omitted seam types: any other pairing would create a right/nonright
vertex forbidden by the full-star language. Consequently the domain is

    8 * 3 * 8! = 967680.

Same-face side pairings are not prematurely excluded from that domain.
The enumeration does not assume side-length equalities or positivity when
screening angle topology. Cyclic labels remain fixed native labels, while
every pairing of those slots is represented.

## Independent exhaustive enumeration and actual links

The reviewer retained
[verify_three_pentagon_mixed_word_independent.py](verify_three_pentagon_mixed_word_independent.py).
It does not import or execute the author enumerator, verifier, or LP.
It independently visits all967,680 cases and builds the side-twin
permutation. Vertex links are cycles of that permutation composed with
the native incoming-side predecessor permutation, rather than the
author's union-find calculation.

All angle sums use exact integers. Early rejection is sound because
every additional corner contributes a positive angle: a link with total
at least360 before closing cannot become a360-degree link. Each surviving
link is an actual single circle. Its source corners have sum360, and the
total angle across all four faces is2160, giving six such links. The
reviewer additionally checked connected face adjacency of every survivor.
All seams reverse boundaries, so those surviving combinatorial surfaces
are closed and orientable with six vertices, ten edges and four faces.

The independent enumeration gives exactly eight survivors, distributed
as two each for reflection masks2,3,4,5 and none for masks0,1,6,7.
After treating each seam as an unordered pair and each list of seams as
unordered, its full model set equals the certificate's full eight-model
set. Every retained vertex-class table and every induced native-side
equality relation also matches. Thus the count is independently recovered,
not accepted only because the original loop reported exhaustion.

## Exact closure matrices and positivity obstruction

For the unreflected reference polygons the direction lists are

    X: 0,30,120,195,270;
    Y: 0,75,165,240,270.

They follow from the native exterior turns180 minus the next corner angle.
Reflection or rotation of a whole polygon gives an invertible orthogonal
map of its vector closure equation, so reference closure is necessary
regardless of which copies were reflected in the quotient. The reflection
side-slot formula above transports seam equalities back to those reference
length slots before forming the matrices.

There is one positive variable for each native length-equivalence class.
The first two matrix rows sum X's unit edge vectors, and the last two sum
Y's. Equal slots share a column. Any real polygon realization must satisfy
this homogeneous four-row system; no sufficiency of vector closure for
convexity is needed because strictly positive closure is excluded already.

The independent checker reconstructs every matrix from the exact unit
vectors in Q(sqrt2,sqrt3), independently of the retained SymPy strings.
It chooses the exact positive embedding and checks sqrt2^2=2,
sqrt3^2=3, and both roots positive. Every certificate entry is evaluated by
a restricted arithmetic/radical parser and equals the independently
constructed entry. Every retained nullspace vector is in the exact kernel;
the retained vectors are independent and their number equals the exact
kernel dimension, so they span the **complete** kernel rather than a
possibly incomplete sample of solutions.

Across the three actual relations the nullities are0,1,1. The relation
with three columns has rank3 and only the zero length vector; its two raw
labelings were independently confirmed to be column permutations. Each
five-column relation has rank4 and a one-dimensional kernel. The native
side3 of X and native side3 of Y are in the same equality class, and that
coordinate is zero in every kernel vector. Hence neither relation has a
strictly positive solution. Extra accidental equalities would restrict
these kernels further, so do not supply an omitted escape.

The exploratory LP used floating equations, normalization sum(lengths)=1
and lower bounds1e-6. Such a lower bound would by itself miss highly
unequal positive solutions. It is not used for the promoted contradiction:
the complete exact kernels exclude **all** positive length vectors, with
no lower bound, rationality restriction, numerical tolerance, or period
bound beyond the declared four-face ansatz.

## Reproduction, repairs, uncertainty, and final verdict

Both repaired computations were freshly executed with assertions enabled:

```text
conda run --no-capture-output -n arisearch python3 research/reviews/verify_three_pentagon_mixed_word_independent.py
conda run --no-capture-output -n arisearch python3 research/searches/new-angle-three-pentagon-mixed-word-verify.py
```

The independent final result is:

```text
PASS independent mixed-word audit: 967680 candidates, 8 exact angle-flat linked models; 4 stored closure records, 3 distinct equality relations; exact complete nullspaces exclude all positive lengths.
```

No further mathematical defect or positive metric counterexample was found
in the declared domain. The reviewer made no proof repair. The author
resolved the reported raw-label-versus-equality-relation count defect,
and its repair has now received a fresh independent check. This review
does not cover the positive Y/Y branches, rule out a larger or different
global X/Y construction, or establish any unrestricted aperiodicity
conclusion. No novelty claim is audited.

**Verdict: VALID after the count repair, for the fixed105-degree four-face
reversed-endpoint X/Y ansatz only.**
