# Independent hostile review: eight-star determinism and analytic escape

Date: 2026-10-19. **Verdict: PASS / valid for the two stated restricted claims.**

## Claim and independence

Reviewed `research/lemmas/hexagon-thirtytwo-star-support-determinism-sol-2026-10-19.md`, its producer and certificate, the corrected end-corner metric lemma, intrinsic determinism theorem, and the defect-free limit theorem and rereview. This reviewer did not develop these results. This is not an unrestricted two-convex-tile impossibility theorem, nor a tilability assertion for the analytic branch.

## Independent finite verification

Created `research/searches/hexagon-thirtytwo-star-support-independent-check-sol-2026-10-19.py`. It imports neither producer, enumerates all 24^3 signed triples allowing repeated corners, quotients only by cyclic rotation, and independently iterates remote-endpoint necessity to a fixed point. The resulting ordered atlas agrees with all 32 certificate stars. An actual star survives every pruning round inductively: the two incident tiles persist at the remote endpoint of their whole shared side, in reversed circular adjacency. This implication does not require any global corner cover or occurrence of the other species.

The checker collects mate constraints in BOTH directions from each of the 24 adjacent-port incidences of the eight selected stars. Every signed native side has exactly one mate, the result is involutive, and all 24 states agree with the claimed certificate. This strengthens the producer check, which gathers outgoing-side constraints then checks involutivity. The seven displayed species-native rows give exactly that map, including the sign flips on A3/B0 and B1/B5.

Using independently transcribed exact end-corner derivatives, the checker reproduces all 32 claimed residual derivatives, obtains exactly {2,5,13,15,17,20,22,23} as their zeros, and directly differentiates both complex polygon closures with side-j direction sum(k<j)(pi-alpha_k). Both derivatives vanish. The four defining star tangent sums also vanish. These are exact symbolic checks; the metric branch's IFT existence and uniqueness remain the stated reviewed dependency, rather than being inferred from this first-order calculation.

Replay:

    mise exec -- conda run --no-capture-output -n arisearch python research/searches/hexagon-thirtytwo-star-support-independent-check-sol-2026-10-19.py

Result: PASS for the reconstructed upper atlas, both-endpoint mate sets, residuals, and direct differentiated closure. No randomness, solver, numerical equality test, or timeout is used.

## Attempts to invalidate the global implications

**Complete placement:** Once both native side slots and both absolute handedness flags are specified, the relative determinant is fixed. Of the two endpoint identifications of congruent segments, exactly one has that determinant. Hence the unique side mate supplies one complete relative isometry. Opposite interiors hold for every transition occurring in an actual tiling. Unused states or formally impossible transitions do not need realization. Native indexing resolves reference symmetries; a continuous absolute angle is never smuggled into the four states.

**Intrinsic propagation:** Same-state occurrences give a plane isometry carrying each indexed neighbor to its corresponding unique neighbor. Connected full-side adjacency propagates it over the plane. Local finiteness follows from positive minimum area and bounded diameter. A compact path can avoid the locally finite vertex set and give finite full-side connectivity. Thus the symmetry group has finitely many tile orbits, is discrete and cocompact. The imported elementary group argument excludes translation ranks zero and one and supplies rank two. No assumption of finitely many absolute tile orientations is needed.

**Unrestricted contacts:** The proof first applies the defect-free limit theorem to the fixed pair at a fixed t. Its defect count, large clean disks and uniform sector-disk separation address subdivision contacts and degeneration under limits. The pair is not changed or rescaled. The resulting tiling is edge-to-edge and trivalent, so upper-atlas necessity applies. This is a conditional existence-to-periodic-escape argument, not extension of an arbitrary formal finite patch.

**Subset versus equality:** All uses require actual support contained in S. Unique options in an upper language remain unique under deletion. No requirement that all eight stars occur enters propagation or the symmetry argument. If deletion removed all options for an occurring side, that would contradict existence of the actual tiling. Species omission is therefore allowed throughout. Indeed S contains only mixed-species stars, so a nonempty actual tiling with this support cannot be monohedral; the proof does not need to assume this beforehand or invoke classification. No hidden full-cover SAT requirement from the earlier candidate producer is used in the theorem.

**Parameter quantifiers:** At t=0 all residuals vanish, so exclusion at the base is false and is not claimed. For each excluded residual with derivative d!=0, continuity of R(t)/t supplies epsilon_r>0 such that |R(t)/t-d|<|d|/2 for 0<|t|<epsilon_r. The minimum of these 24 positive radii, the metric IFT radius, convexity radius, and 1/4 is positive. Consequently the result holds for every t in one positive interval (0,epsilon). Five lengths are pairwise distinct there. The eight permitted residuals vanish identically because each uses one of the four defining angle sums. No uniform interval over other analytic branches or metrics is claimed.

## Defects, repairs, and remaining scope

No mathematical defect found; no repair proposed. The source's phrase “reviewed native upper atlas” could be made easier to audit with a direct link to its producer/review, but the independent reconstruction above closes this dependency for the present fixed word. The independent checker reads retained atlas/certificate data for comparison but reconstructs its combinatorics without trusting their search implementation.

The exact positive epsilon is existential. The result does not prove tilability, construct a periodic witness, or close other supports or other metrics of the remaining B orbit. Those are outside the reviewed claim. Final verdict: valid for the stated restricted determinism theorem and sufficiently-small-positive corrected-branch periodic escape.

## Reviewed metric-locus generalization

PASS also for this immediate generalization: fix these native words and any strictly convex closed reference metrics with five pairwise distinct positive common length values. If every angle-compatible star in the full 32-star upper atlas belongs to S, then any unrestricted tiling implies existence of a doubly periodic tiling. The proof is exactly defect-free reduction followed by atlas necessity and statement 1, and requires no analytic parametrization. Imposing the four retained angle sums and excluding all 24 other atlas sums is a sufficient, more explicit description of such a metric locus; requiring all four is stronger than the subset implication needs. The reviewed corrected IFT branch shows this metric locus is nonempty for sufficiently small positive t, without asserting the tilable sublocus is nonempty.
