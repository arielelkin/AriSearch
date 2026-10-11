# Hostile review: five distinct lengths with sparse sharing

**Date:** 2026-10-09. **Verdict:** valid. This reviewer did not develop the
repeated-side theorem. Its two explicit dependencies already received
independent reviews in this run.

## Exact claim reviewed

[The theorem](../lemmas/hexagon-five-length-sparse-sharing.md) concerns two
genuine compact convex hexagons, each with one length repeated in side
slots of cyclic separation two and four other single lengths. If their
length sets share at most three values, tileability implies a doubly
periodic four-face torus witness. With at most two shared values no plane
tiling exists. The theorem does not address repeat separations one or
three, a (six-distinct,five-distinct) pair, or four/five shared values.

The proof, generator, certificate, separate verifier, and abstract-angle
failure diagnostic were read. No deep monohedral classification is used.

## Attacks and checks

1. **Coincident ray labels:** the repeated side slots are not adjacent.
   Thus no native corner has two equal side lengths. At a trivalent
   vertex each pair of its three rays bounds one tile corner, so any
   coincident pair of numerical ray lengths would contradict that native
   corner property. This step remains valid although each type has a
   nonadjacent repeat. The simple length graph can therefore use genuine
   triangles, while duplicated native corners are separately retained.
2. **Monochromatic limit:** the simple corner graph of either repeat-two
   word is a four-cycle with a pendant edge. It is triangle-free. Hence
   the freshly reviewed defect-free limit cannot omit either type, and
   all twelve native corner slots must appear in actual stars.
3. **Exact finite domain:** A can be labelled (0,1,0,2,3,4) without
   restricting its metric values. For each k=0,...,3 shared values, every
   five-element B length set, every choice of B's repeated value, and
   every separation-two order is included. Rotation/reflection quotienting
   preserves the unordered side pairs and native angle slots. The raw
   permutation replay includes duplicates of its repeated symbol and
   removes them by set normalization; its 93,600 visits give the stated
   60,300,600,600 normalized domains. The sole covered pattern at k=3
   requires the repeated value itself to be shared; no such requirement
   was assumed beforehand.
4. **Corners of the survivor:** directly reading the two cyclic words
   gives 015=(a0 or a1,b2,b3), 016=(a0 or a1,b4,b5),
   023=(a2,a3,b0 or b1), 034=(a4,a5,b0 or b1).
   Every triangle is forced to occur by one of its private side values.
   Merely covering all corners does not yet choose consistent repeat
   slots; the proof acknowledges this and uses endpoints.
5. **Case I endpoint:** at a0 the unique incident side bearing label 0
   is A slot 0; at b2 it is B slot 2. A full shared side consequently
   has corners a5 and b1 at its other endpoint, regardless of tile
   reflection. The remaining length pair is {3,4}, uniquely corner a4.
   Thus the forced star is (a4,a5,b1), not the potentially unrelated
   b0 choice. This validates the required cross-coupling of the two
   ambiguous pairs.
6. **Case II endpoint:** if 015 uses a1, its zero-labelled A side is
   slot 2. The other endpoint is a2,b1, with unique remaining corner a3.
   Thus 023 uses b1. Reversing cyclic sector order under reflection
   never changes these native endpoints or angle sums.
7. **Companion-row selection:** when a missing companion corner occurs
   only in the chosen row, the two permitted equations there share the
   other two actual angles and force a0=a1. The nonempty companion row
   then permits either equal angle. The same argument handles b0=b1.
   Thus supports (3) and (4) follow from actual corner occurrence plus
   the endpoint relation, rather than two independently selected
   matchings. Chiral choices at vertices are not being treated as
   independent global face orientations.
8. **Formal zero-slot assignment:** writing A as (u,1,v,2,3,4), case I
   requires B=(v,3,u,5,1,6), and case II B=(u,3,v,5,1,6). The private
   symbols 2,4 and 5,6 insert on complementary edges of the common
   four-cycle. Its four triangles map exactly to the stated native
   supports. u and v denote equal positive numerical lengths, not an
   actual unequal geometric replacement. Matching like symbols still
   pairs valid full native side slots.
9. **Global torus:** the separately reviewed four-face construction
   explicitly reflects the B reference when needed and reverses both
   endpoints at each gluing. It has eight circular three-corner links,
   twelve edges, four faces, is connected and orientable, and is a torus.
   All cone-angle sums are those just proved. Complete flat development
   yields a plane tiling with disjoint interiors and two independent
   translation periods. Multiple quotient adjacency edges between the
   same face orbits do not require the same *lifted* tile neighbour;
   deck translates give the distinct actual plane occurrences as needed.

## Diagnostic and computation

The [abstract-angle diagnostic](../counterexamples/hexagon-five-length-angle-support.md)
was checked directly. Both six-angle lists sum to 4pi and are strictly
obtuse. Exactly the four listed length-compatible stars sum to 2pi and
cover all twelve native corner slots. Neither consistent formal-slot
support is legal, and the forced other endpoint has angle 19pi/10.
This correctly refutes the purely algebraic corner-cover shortcut. It
is explicitly an abstract fixture without polygon closure, rather than
a claimed geometric counterexample to the theorem.

The [independent verifier](hexagon-five-length-verify.py) was run:

    conda run --no-capture-output -n arisearch python3 research/reviews/hexagon-five-length-verify.py

It passed on Python 3.12.13 / Conda arisearch: 93,600 raw words, 1,560
normalized words, the unique k=3 survivor, both four-face reversed endpoint
gluings, and the rational angle-only failure fixture. It imports no
search implementation. The endpoint relation itself was additionally
checked above from the native side endpoints, not inferred merely from
the fixture or from a solver.

## Defects, repairs, uncertainty, and verdict

No defect was found in the completed theorem; no repair was made by this
reviewer. The earlier corner-only support problem is preserved as a precise
diagnostic and is genuinely resolved by the current endpoint proof. The
repaired defect-free-limit dependency is covered by
[its re-review](hexagon-defect-limit-rereview.md), and the explicit torus
construction by [the distinct-length review](hexagon-holonomy-distinct-lengths-review.md).

The result excludes only the exact sparse-sharing repeated-side family.
It is not a general two-hexagon periodicity theorem and makes no novelty
claim. Remaining numerical coincidences and repeated-side arrangements
outside the finite domain require different arguments.

**Final verdict:** valid under the exact stated hypotheses.
