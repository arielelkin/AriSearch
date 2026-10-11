# Private repeated sides and a cofinite isometry mechanism

**Status:** adversarially reviewed; [fresh independent whole-claim review](../reviews/hexagon-five-length-private-repeat-periodicity-review.md) valid. The two nongeneric flat-torus witnesses have an exact gluing
certificate and a small independent checker. No novelty claim is made.

**Review:** [independent hostile review](../reviews/hexagon-five-length-private-repeat-periodicity-review.md).

## The restricted hexagon theorem

Let six pairwise distinct positive numerical lengths be denoted 0,1,2,3,4,5.
These digits are length symbols, not the numerical values of the lengths.
Let A and B be convex hexagons whose cyclic side-length words, allowing an
independent reflected reference for either polygon, are

    A = (0,1,0,2,3,4),
    B = (5,3,5,2,1,4).

Thus both have five distinct lengths, their repeated lengths have separation
two, and both repeated lengths are private to their own type. If these shapes
tile the plane with reflections and unrestricted contacts allowed, they admit
a doubly periodic tiling. If both repeated corner-angle pairs defined below
are unequal, every edge-to-edge trivalent tiling by the pair is itself doubly
periodic. This does not exclude other five-length side orders.

Dependency: the [defect-free limit theorem](hexagon-limit-and-periodicity.md),
reviewed separately. Compact-flat-torus development is explained in
[the distinct-length theorem, Section2](hexagon-holonomy-distinct-lengths.md).
No monohedral classification or crystallographic-group theorem is imported.

## 1. The intrinsic-state periodicity lemma

The [separate conditional lemma](hexagon-five-length-intrinsic-determinism.md)
proves that finitely many intrinsic states with fixed complete relative neighbor
isometries yield a discrete cocompact symmetry group, whose translation subgroup
has rank two. It assumes connected complete-side tile adjacency, which an
edge-to-edge plane tiling supplies. It needs neither finite absolute orientations
nor a honeycomb coordinate system. Its hypotheses must be established from the
actual shapes; branching symbolic rules do not suffice.

## 2. The four graph triangles and their angle choices

Use a defect-free trivalent tiling. Adjacent sides of both words have distinct
lengths, so vertex stars correspond graph triangles with three distinct ray
lengths. The simple corner graphs of A and B are each triangle-free. Both
prototypes therefore occur, and every actual corner slot occurs.

Let a_i,b_i be the corner after side slot i in the displayed words. The union
corner graph has exactly four triangles:

| Triangle | Actual corner triples |
|---|---|
| 012 | (a_x,a_2,b_3), x=0 or1 |
| 014 | (a_(1-x),a_5,b_4), x=0 or1 |
| 235 | (a_3,b_y,b_2), y=0 or1 |
| 345 | (a_4,b_(1-y),b_5), y=0 or1 |

In this table the complementary choices across a pair of rows are selections,
not an a priori rule. Each triangle kind occurs because one of its unduplicated
corner edges belongs to no other triangle. Both a_0,a_1 must occur in the first
two rows and both b_0,b_1 in the last two. The two-set matching argument chooses
some x and y giving all four displayed 2pi sums.

If a_0 differs from a_1, each of 012 and014 permits at most one choice, and
corner coverage forces the complementary choices x,1-x. If they are equal,
both choices are angle-legal in both rows. The same assertions hold for b_0,b_1.

## 3. Generic angles give geometric uniqueness

Suppose a_0!=a_1 and b_0!=b_1. The complete angle-legal star language is the
four triples selected by one fixed pair (x,y). All full-edge neighbors are
uniquely determined in the tile's reference frame:

* If x=1, A's repeated-length-0 slot0 matches slot0 of another A, and slot2
  matches slot2, swapping their endpoint roles. If x=0, slot0 matches slot2
  and conversely, with the endpoint matching prescribed by 012 and014.
* If y=1, B's repeated-length-5 slots match the same slots of another B.
  If y=0, they match the opposite repeated slots. Again endpoint matching is
  fixed by 235 and345.
* Every shared side of numerical length1,2,3,4 matches the unique side of
  that length in the other type. Its endpoint matching is fixed by the four
  selected star triples: length1 uses the x choice, length3 the y choice,
  and lengths2,4 each have one fixed endpoint pairing.

For completeness, unlike-type matching on these shared sides is forced.
Around A's length1 side both adjacent corner lengths are 0; an A/A match
would repeat a ray label at its endpoint. Around B's length1 side the other
labels are 2,4, whose connecting edge is absent from the union graph. Around
length2 or4 the respective same-type neighbor pairs likewise have no shortcut,
and the same argument applies to length3. Only the A/B possibilities remain.

The shared-side endpoint correspondences, written in source corner indices,
are a_x<->b_3 and a_(1-x)<->b_4 at length1; a_2<->b_3 and a_3<->b_2 at length2;
a_3<->b_y and a_4<->b_(1-y) at length3; a_4<->b_5 and a_5<->b_4 at length4.
For x=0 the A slot0/slot2 matching is a_5<->a_1 and a_0<->a_2; for x=1
both repeated A slots match themselves reversing their endpoint corner roles.
The B length5 correspondences are identical with b,y in place of a,x.
The independent checker enumerates all192 same-length neighbor-slot/endpoint
candidates across all four (x,y) supports, retaining exactly one at every
native side slot. It checks both endpoints, including same-type possibilities.

Two fixed endpoint images on a full side, with polygon interiors on opposite
sides of its supporting line, determine the neighbor's full plane isometry.
Every type/side slot therefore uniquely determines the relative neighbor
isometry, even though copies may be reflected and may initially have infinitely
many absolute orientations.

Neither polygon has a nontrivial side-index symmetry: at least three uniquely
occurring length symbols fix different side slots. Thus each actual copy has
an unambiguous reference-side indexing. The uniqueness rule is equivariant
under all plane isometries. The two prototype types are finite intrinsic
states for Section1. The original defect-free tiling itself is doubly periodic.

## 4. Equal duplicated angles have explicit four-face witnesses

If a_0=a_1 or b_0=b_1, the corresponding pair of rows permits both choices.
The other pair has at least one matching choice. Select x=y in {0,1}, agreeing
with any forced choice of the unequal pair. All four selected angle sums are
then 2pi.

For x=y=1 take faces A0,A1,B0,B1 without reflected references. For x=y=0 take
A0,B0 in the displayed references and A1,B1 in reflected references. Exact
full-side pairings for both models are retained in
[the gluing certificate](../certificates/hexagon-five-length-private-repeat-tori.json).
A side index in that certificate refers to the cyclic word of the face's
chosen reference; a reflected word is the displayed word in reverse order.
All identified side endpoints are reversed in these chosen face-boundary orders.

The checker verifies all 24 side occurrences are used exactly once, every
paired full side has equal numerical length, the quotient is connected,
there are eight vertices of three actual corners each, and each of the four
selected star triples appears at precisely two vertices. Consequently the
quotient is a connected closed orientable surface with Euler characteristic
8-12+4=0 and all cone angles2pi. It is a flat torus. Its universal cover gives
a doubly periodic tiling by the original whole convex hexagons, including the
specified reflected copies when x=y=0.

This also shows why a negative bounded search would be insufficient: the
uncoupled generic choices x!=y are resolved by the existing tiling's cofinite
isometry action, not by asserting that no four-face witness was found.

## Verification and non-consequences

```text
conda run --no-capture-output -n arisearch python3 research/reviews/hexagon-five-length-private-repeat-verify.py
```

The checker uses only integer arithmetic and the retained finite side-pairing
lists. It does not solve polygon closure; the faces are the given original
polygons. The exact source angle equations are supplied by the mathematical
selection above. The [verification record](../searches/hexagon-five-length-private-repeat-tori.md)
records its finite domain and conditions.

This theorem concerns the two explicit cyclic length orders only. It does not
prove that arbitrary internally-five-length hexagon pairs have geometric
uniqueness or that arbitrary angle-legal star languages admit a flat torus.
Repeated-side branching in other orders remains an unresolved obligation.
