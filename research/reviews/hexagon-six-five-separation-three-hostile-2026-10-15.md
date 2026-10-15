# Fresh independent extension audit: separation-three repeat

Date: 2026-10-15. Verdict: **VALID** for the separation-three extension
specified below, using the reviewed defect-free-limit and intrinsic-
determinism dependencies. No novelty or main-problem resolution is claimed.
The reviewer did not develop the extension or its producer gate.

## Exact theorem

Let A have six distinct side lengths and let B have exactly five distinct
side lengths, with its equal side slots opposite (cyclic separation three).
If the genuine compact convex hexagon pair tiles the plane with unrestricted
contacts and reflected placements, then it admits a doubly periodic tiling.

The complete written author artifact
`research/lemmas/hexagon-six-five-opposite-repeat-periodicity-2026-10-15.md`
was read after completing the independent reconstruction. Its Sections1--4,
12-support census, explicit 2B torus and concluding geometric bridges agree
with this audit; no missing-draft qualification remains. This audit also
independently reconstructs the full finite domain supplied with
`research/searches/hexagon-six-five-separation-three-gate-2026-10-15.py`.
It does not treat the producer's eight input words alone as an exhaustive
classification; that completeness is established independently below.

## The pure-B escape is valid

After the defect-free limit, write B=(p,q,r,p,s,t), with five distinct
numerical lengths and corner i between side slots i,i+1. Its only pure-B
triangle stars are (0,1,2) and (3,4,5). If either occurs, its angles sum
to 2pi; the six native angles total 4pi, so the other triple also sums to
2pi. Construct a torus from two B faces: within each face pair repeated
side slot 0 to slot 3, and pair each of slots 1,2,4,5 to that same slot
of the other face. Reverse all boundary endpoint orders.

The independent verifier explicitly finds four quotient vertices, with
corner triples (0,1,2) twice and (3,4,5) twice. Their links are circular,
the quotient is connected and orientable, and V-E+F=4-6+2=0. Its angle
sums are 2pi and all side lengths match. Thus it is a compact flat torus,
whose developing universal cover gives a doubly periodic B-only tiling.
This argument includes all metric shapes having the specified angles and
side-slot equality; it assumes neither parallel opposite sides nor a
particular plane patch extension.

## Independent exhaustive mixed-star branch

Suppose no pure-B star occurs. A alone has a triangle-free corner graph,
and a B-only defect-free tiling would have a pure-B star, so both tile
types occur and all twelve actual corners occur in mixed stars. Three
ray lengths are distinct, since neither polygon has equal adjacent side
lengths. The same actual-side endpoint closure condition as in the
separation-two review therefore applies to the mixed support.

Independently normalize B=(p,q,r,p,s,t). The stabilizer of the two opposite
repeated slots has four elements (the two choices of starting repeated
slot and the two directions). For each shared symbol set and the five
role permutations, retain the lexicographically first word under these
four descriptions. This yields 30*sum(k=0,...,5)binomial(6,k)=1890 words.
No assumption k>=4 is made before enumeration. Direct indexed-corner
triple enumeration, with pure-B triples removed, retains 30 words with
four shared lengths and 36 with five; there are no other survivors.
Independent dihedral canonicalization yields exactly the eight producer
orbits.

For all eight representatives the verifier exhausts every subset of the
complete mixed-star atlas, keeping actual-corner coverage and closure
at both endpoints of every matched side. Closed-support counts are

    0,1,1,1,0,1,1,7  (total 12).

For each retained support the verifier searches actual equal-length side
perfect matchings on A0,A1,B0,B1, not producer formal-symbol rings. Ten
supports directly admit connected orientable four-face torus gluings with
eight trivalent quotient vertices, every triple drawn from that support.
The remaining two supports are four-triple partitions of all twelve
actual corner slots; each fixes the native neighbor corner uniquely
across every ray, with the same neighbor at the far endpoint. The
reflection and complete relative-isometry argument in the separation-two
review applies without change: endpoint order fixes the segment map,
and opposite interiors select its unique plane-isometry extension.
Thus the reviewed intrinsic determinism theorem makes the actual
defect-free tiling doubly periodic in these two cases.

All branches therefore prove the stated periodic escape. A diagram,
angle-linear-program feasibility result, or bounded plane-placement
search is not part of the proof.

## Replay and limitations

    mise exec -- conda run --no-capture-output -n arisearch python research/reviews/hexagon-six-five-separation-three-independent-2026-10-15.py

Observed result: PASS; 1890 words, 66 survivors, 8 orbits, 12 closed
supports, 10 direct four-face tori, 2 deterministic residuals, and the
explicit pure-B torus. The verifier uses only the Python standard library
and helpers from the independent separation-two review checker; it never
imports producer code. Its finite decisions use exact integers and sets.
The helper also reruns the complete independent separation-two census.

No mathematical defect found and no repair to the producer was required.
The theorem remains restricted to one internally distinct hexagon and one
five-length hexagon with a nonadjacent repeat. Adjacent equal sides have
a different ray-length issue and are not covered by either new theorem.
