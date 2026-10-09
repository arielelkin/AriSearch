# Hostile review: Walton state-assignment exhaustion

**Re-review status:** this record includes repairs or extensions made during
review. A separate independent review of the resulting version is not
established by the retained record and remains pending under
[protocol Section 8.2](../../research-protocol.md#82-review-artifacts).

**Artifact reviewed:** [walton-encoding-reconnaissance.md](../searches/walton-encoding-reconnaissance.md).

**Object reviewed:** [research/searches/walton_state_assignment_rank.py](../searches/walton_state_assignment_rank.py) and
its certificate.

**Verdict:** valid finite no-go within its explicitly limited compiler family;
not a no-go for all two-polygon encodings.

## Checks and repairs

1. **Finite-domain check.**  There are twelve source states (six rotations
   times two reflection states), hence exactly (2^{12}-2=4094) nonconstant
   Boolean assignments.  The search includes both alternating corner triples
   `(0,2,4)` and `(1,3,5)` and begins from the independently transcribed 1,056
   ordered Walton-legal flag triples.
2. **Rank direction.**  Modular rank can be smaller than rational rank, never
   larger.  The search uses modular elimination to locate the four minimum
   cases and then rechecks all four over `Fraction`; the exact and modular
   minima agree at 11.  Thus no assignment was incorrectly discarded as
   full-rank because of modular arithmetic.
3. **Exceptional nullspace.**  Direct rational reduction gives, for every
   exceptional mask, the one-dimensional angle-deviation vector
   `(0,-1,0,0,0,1)` on each tile.  This was independently recomputed from the
   retained row sets, rather than inferred from mask symmetry.
4. **Length propagation.**  Union-find over the sides of every contact in
   every retained ordered triple yields the single class `{0,...,11}` for
   each exceptional mask.  This is stronger than merely observing many
   contacts: all sides of both proposed polygons must share one length.
5. **Closure repair.**  Rank 11 initially looked like a possible deformation.
   It is not.  For unit sides and the indicated angle deformation, the six
   edge directions can be chosen as
   (1,ze^{it},z^2e^{it},z^3e^{it},z^4e^{it},z^5), where
   (z=e^{i\pi/3}).  Their sum is
   ((1+z^5)(1-e^{it})), and (1+z^5\ne0).  In the convex range, closure
   therefore gives (t=0).

## Scope warning

The mapping from source states to geometric types is an algebraic relaxation,
not a proof that bare polygons can select exactly those placement states.
Consequently a failure is useful and sound, whereas a surviving mask would
still have required a separate geometric forcing proof.  The computation does
not examine arbitrary strict subsets of source vertices or different source
matching systems.

## Relative-relabelling extension

The companion search [walton_relative_relabeling_rank.py](../searches/walton_relative_relabeling_rank.py) was checked for a
common-frame redundancy: fixing type 0 and varying type 1 through six shifts,
two chiralities, and two charge flips gives all 24 relative choices.  Its
near-start bit is complemented under a chirality reversal, as required when
source and physical boundary traversal oppose; charge orientation is reversed
as well.  Placement reflection remains a separate flag.  All 24 cases return
rank 12 and one length class.  This closes relabelling freedom only; it does
not close arbitrary changes to the compiler or strict source sublanguages.
