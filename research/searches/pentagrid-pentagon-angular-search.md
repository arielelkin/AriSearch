# Pi/5 pentagon angle and native-star classification

**Question:** Which cyclic pentagon angle words in integer pi/5 units
survive the adjacent supplementary monohedral escape, and which pairs
pass all native-angle sum and aggregate incidence constraints when
partial-side contacts are allowed?

**Scope:** The conclusion is the restricted theorem in
[the angular lemma](../lemmas/pentagrid-pentagon-angular-reduction.md).
Lengths and plane tilings are not enumerated.

**Exact domain and encoding:** Ordered angle words are the 1024 members
of {1,2,3,4}^5, restricted by sum15. Cyclic rotations and reversals are
identified by the minimum of their ten dihedral images. All101 valid
ordered words give13 dihedral classes and5 sorted multisets. Unordered
word and multiset pairs allow repetition, respectively91 and15 pairs,
because distinct congruence classes can have the same angle word.

Native stars are count vectors in {0,...,10}^4, of weighted sum5 or10.
This overincluding domain has14641 vectors and29 legal sums. Minimum
angle pi/5 proves the valence bound10 for full stars and5 for half stars,
so the angle sum classification has no missing higher-valence cases.
No side-contact or shape-congruence inference is made from a star vector.

**Constraints and certificates:** A word is removed if an adjacent angle
pair sums to5, invoking the proved half-turn periodic escape. All108/all108
is removed because no native star exists. Rational nonnegative star
decompositions certify incidence feasibility for all other multiset pairs.
The exceptional (2,3,3,3,4)/all108 pair permits only zero all108 incidence
count, certified by a separating functional. The same functional certifies
sharp all108-to-partner incidence bounds2,1,1,0. No linear-program solver
is trusted; the retained witnesses and integer functional are checked
directly.

**Software:** Python3 standard library only: itertools, fractions, json,
collections, pathlib. No stochastic seed, configured timeout, memory cap,
floating-point branch, or solver dependency. The producer rejects Python
optimization; the independent checker uses explicit exception-based checks.

**Replay from the repository root:**

```text
conda run --no-capture-output -n arisearch python3 research/searches/pentagrid_pentagon_angles.py
conda run --no-capture-output -n arisearch python3 research/reviews/verify_pentagrid_pentagon_angles.py
```

The first command prints the complete certificate. To regenerate the
retained file, redirect its standard output to
`research/certificates/pentagrid_pentagon_angles.json`. The second reads
that certificate. It imports none of the producer and uses integer
partitions and permutations instead of ordered Cartesian-product enumeration
to check completeness of words and stars.

**Completion:** The complete stated domains were exhausted. Retained
results: 101 ordered words,13 dihedral words,29 full/half stars,15 multiset
incidence cases,5 surviving aperiodicity word-pair signatures. The
[certificate](../certificates/pentagrid_pentagon_angles.json) records every
word, star, seam, incidence witness, and functional value.

**What is not proved:** No polygon with prescribed lengths, finite patch,
plane tiling, monohedral classification of U or V, geometric realization
of an incidence vector, periodicity exclusion, or main-problem resolution
is inferred. In particular this is not a bounded search for a periodic
tiling.
