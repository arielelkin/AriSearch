# Fresh hostile review: all-obtuse distinct-length pentagon–higher pairs

**Date:** 2026-10-09. **Reviewer:** primary-literature agent, independently
reviewing the root agent's new proof and checker. I did not construct this
lemma, its finite classification, or its certificate. No proof/checker edits
were made during this review.

**Verdict: VALID within the exact stated restrictions.** No mathematical
counterexample or unresolved proof defect was found. The complete actual
certificate was checked independently; the author resolved the validator
completeness/metadata concerns before this review's final replay.

## Exact claim and dependencies

Reviewed claim in
[distinct-length-obtuse-pentagon-higher.md](../lemmas/distinct-length-obtuse-pentagon-higher.md):
P is a genuine compact convex pentagon, Q a genuine compact convex n-gon,
n>=7; all angles of both polygons lie strictly between pi/2 and pi; each
polygon separately has pairwise distinct numerical side lengths. If the pair
tiles using arbitrary isometries and contacts, then n=7 and it admits a
doubly periodic tiling. For n>=8 it is untileable. Cross-type numerical
length coincidences are permitted. The periodic witness may use reflections
and has two copies of each original shape in a four-face torus quotient.

The sole tiling-structure dependency is the previously reviewed
[obtuse forcing theorem](../lemmas/obtuse-edge-forcing.md), whose proof was
read again here. Finite positive-area polygons give local finiteness. At a
genuine tile corner, a straight sector would leave a half-plane requiring
either one corner of angle pi or at least two corners totaling greater than
pi. Both are impossible. Thus no genuine vertex lies inside another side;
all positive-length interfaces are whole matched sides. Angle sums then
force exactly three genuine sectors per vertex. This applies to the original
unrestricted contacts, without an imported matching rule.

## Attack 1: side-count bound and domain completeness

At a full matched ray its two sides have one numerical length. Any two rays
at a trivalent vertex bound one incident tile corner. Equal ray symbols
would therefore make adjacent sides of that tile equal, contrary to internal
distinctness. The three corner edges form an ordinary graph triangle.
Neither single simple C5 nor simple Cn contains a triangle, so both types
must occur. Once a type occurs, each of its actual corner slots occurs in
some triangle star.

A private symbol has degree two in the union graph. Its only possible graph
triangle uses its two neighbors and the shortcut between them. That shortcut
is not in its own simple cycle; hence it belongs to the opposite cycle, and
both neighbors are shared. All private symbols are consequently isolated.

With k<=5 shared symbols, Q has n-k isolated private symbols, so
n-k<=floor(n/2), equivalently k>=ceil(n/2). Thus n<=2k<=10. P also has
5-k<=2 private symbols. For n>=7 this leaves exactly

```text
(n,k) = (7,4),(7,5),(8,4),(8,5),(9,5),(10,5).
```

There is no omitted unbounded-n case and no hidden search cutoff. In
particular (7,3) is excluded analytically because four private Q symbols
cannot be isolated in a seven-cycle.

I independently checked the closed formulas. The isolated-private domain
has C(5,k)(k-1)!C(k,n-k)/2 words: select shared symbols, cyclic common
order, and the insertion gaps. The larger domain allowing adjacent private
symbols has C(5,k)(k-1)!C(n-1,k-1)/2 words. Private labels are renamed by
first occurrence. Reversal acts freely because k>=4 distinctly labeled
common symbols cannot have their cyclic order equal to its reverse.

| n,k | isolated domain | all interleavings | survivors |
|---|---:|---:|---:|
|7,4|60|300|5|
|7,5|120|180|10|
|8,4|15|525|0|
|8,5|120|420|5|
|9,5|60|840|0|
|10,5|12|1512|1|

The totals are 387 isolated words, 3,777 larger-domain words, and 21
survivors. The separate checker exhausts the larger domains, so deriving
private isolation and then enumerating only isolated words did not omit a
triangle-covered pattern.

## Attack 2: dihedral orbit reduction and certificate metadata

P's distinct lengths may be renamed 0,...,4 in cyclic order. Its ten
dihedral relabelings preserve the same corner-cycle structure. Q rotations
and reflection are valid quotient operations because all isometries are
allowed. Renaming a private Q symbol loses no equality information: no such
symbol occurs in P, and all Q sides have different lengths.

A fresh inline implementation, importing neither generator nor checker,
normalized private labels and independently calculated all ten P-dihedral
images. It checked every retained representative and every displayed graph
triangle against the original words. The five representative classes in the
proof are exactly the resulting classes. Their sizes in the normalized
certificate are respectively 5,5,5,5,1. Corner angles are not equated by this
reduction; the proof transports typed actual corner slots under the
relabeling/reflection.

I also reran the generator and compared its parsed full JSON with the
retained certificate. They agree. Certificate SHA-256:

```text
c117b158633a3128c43d5871e3755cb1d66514e554de75323f27d76e63a2b24a
```

## Attack 3: higher-case angle contradictions

For n=8, the representative Q=(0,2,5,1,3,6,4,7) has no duplicated corner
edge between types. The five listed triangle equations are forced by the
unique-corner witnesses named in the proof. I independently expanded each
triangle into the actual source corner slots. All thirteen slots occur once,
except P's {1,2} corner which occurs three times. Thus their five sums give

```text
5(2pi) = (5-2)pi + (8-2)pi + 2 a_12,
a_12 = pi/2.
```

This is a contradiction to **strictly** obtuse angles. It is not a rounded
angle or an unjustified angle-frequency estimate. The other n=8 domain and
the n=9 domain have no triangle-covered graph survivor at all.

For n=10, the five graph triangles partition all fifteen actual corners;
each is forced by its P corner. Summing them gives 10pi, while the polygon
angle sums give 3pi+8pi=11pi. The two equations cannot coexist.

The independent exact span checker confirms these consequences for every
corner-covering star support. Its augmented rational equations include the
right-hand side, and contradiction is represented by a nonzero constant
row. If a support is itself inconsistent, row-space implication becomes
vacuous; that does not introduce a counterexample because an actual tiling's
angle support must be consistent. No positivity relaxation is being used
as a sufficient condition for existence.

## Attack 4: k=5 duplicated-corner selection

In Q=(0,1,4,5,3,6,2), triangles 012 and 014 each have a unique nonduplicated
P-corner forcing them to occur. Each has a nonempty availability subset
from {a_01,b_01}. Both actual 01 corner occurrences must occur somewhere,
and neither can occur outside these two triangle kinds. Their two
availability subsets therefore cover both choices. The only failing
two-set matching situation would be both subsets the same singleton; that
would omit one actual corner. Hence one triangle can use a_01 and the other
b_01. Splitting numerical symbol 1 or 0 according to the selected assignment
creates the stated four-common-symbol ring.

In Q=(0,2,4,5,3,1,6), triangles 016 and 345 are forced by the private Q
symbols, while 024 and 123 are forced by the specified actual corners. Each
assignment is unique. Splitting symbol 2 makes these four triangles exactly
the ring. Extra legal triangles need not be prohibited in the original
tiling: the conclusion constructs another permitted tiling.

Formal splitting imposes no marking on the original polygons. It restricts
the contacts chosen for the witness; a formal symbol still denotes the same
old numerical length. Each of the twelve actual corner slots is used once
in the selected ring. The independent verifier enumerates every possible
typed-corner covering support, rather than only the favorite support drawn
in the proof, and finds a ring whose four angle equations follow.

## Attack 5: reflection, endpoint order, and global plane coverage

Deleting private symbols gives the same four-cycle on shared lengths in
opposite type orientations. Choosing Q's reference reflection from its
projected common order is necessary. The current verifier tests whether
that order is the P order or its reverse and reverses Q only in the first
case. I inspected the slot-to-corner conversion for reversed Q: it recovers
the actual corner by its unordered adjacent length pair. Uniqueness holds
inside each simple native cycle. An unconditional Q reversal would be a
real checker error; the retained version no longer makes it.

There are 2*5+2*7=24 whole sides. Private sides join same-type copies in
matching slots; the common pairing is j=i xor h(x), with alternating h.
For a private insertion between x,y, the two common seams reach the same
opposite-type face because h(x)!=h(y). Reversed boundary endpoints produce
the exact three source corners of that ring triangle.

The direct endpoint checker found eight three-corner vertex classes for
each of twenty possible retained ring maps. Each corner has two link ends
paired across its incident sides. Every paired side joins distinct faces,
so a link cannot have a one-corner loop. A three-corner class therefore has
one circular three-sector link. Along edges the quotient is also locally a
disk. Consequently it is a connected closed surface, not merely a cell
complex whose Euler characteristic happens to be zero. Boundary-reversing
gluing preserves an orientation. With V-E+F=8-12+4=0 it is a torus.

The actual polygons, including their already closed side vectors, supply
the face metrics. Full sides match and every selected corner triple sums
to 2pi. Thus the compact quotient is nonsingular and flat. Its complete
simply connected universal cover is Euclidean; the lifted faces cover it
with disjoint interiors. This establishes the entire plane, not a locally
legal finite patch. The free orientation-preserving deck group is Z^2;
under development a nonidentity member cannot be a rotation because that
would have a fixed point. Its translations are discrete and rank two, so
two generators are independent. Scale differences between the two types
cause no problem: every gluing pairs sides already known numerically equal.

## Replay evidence and author checker hardening

Fresh replay completed with exit 0 in Python 3.12.13, Conda `arisearch`,
standard-library rational/integer arithmetic:

```text
conda run --no-capture-output -n arisearch python3 research/reviews/verify_distinct_pentagon_higher.py
```

```json
{
  "audited_four_face_torus_maps": 20,
  "corner_covering_supports": 66,
  "full_normalized_word_domain": 3777,
  "retained_survivors": 21,
  "verdict": "PASS"
}
```

**Concern reported and resolved by the author:** the initial verifier
iterated whatever `records` the input certificate supplied, so omission of
an entire record could evade that validator. It also printed declared
`survivor_count` without directly validating every representative/triangle
metadata field. The author added assertions for the exact six (n,k) records
once each in the specified order, native A word, survivor count, graph
triangles, dihedral representatives, formal B words and ring corner triples.
I inspected those additions and freshly reran the strengthened checker.
It passed with the same complete output above. My separate domain-formula
and metadata checks agree. No requested theorem domain is missing from the
retained data. No mathematical proof repair was required.

## Counterexample attempts, uncertainty, and scope verdict

Attacks based on adjacent private symbols, an omitted n>=11 case,
disappearing types, duplicated-corner assignments, wrong Q reflection,
nonmanifold vertices, rotational holonomy, partial contacts, and unequal
type scales did not produce a counterexample under the stated hypotheses.

Weakening strict obtuseness admits the local sector equality
pi=pi/2+pi/2 at a straight side, so this proof's contact forcing fails; the
n=8 branch also ends at a right angle instead of a contradiction. That is
an identified proof boundary, not a constructed tiling counterexample.
Removing internal distinctness likewise permits repeated ray symbols and
destroys the simple-cycle/ordinary-triangle encoding. Neither weakening
is covered by this review. Irrational angles and arbitrary exact length
values cause no additional gap inside the retained hypotheses.

The restricted theorem is sound on the inspected proof and actual complete
finite data. The general two-polygon aperiodicity problem remains open in
the repository's remaining families. This hostile review establishes
validity, not novelty; the classical flat-torus mechanism and prior-art
comparison should be attributed separately.
