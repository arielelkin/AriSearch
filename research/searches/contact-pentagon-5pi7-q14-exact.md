# Exact P(5π/7,4π/7⁴) / equiangular Q14 native-ring experiment

Date: 2026-10-14. **Independently reviewed VALID for the stated exact finite
domain, local palette audit and restricted periodic-model exclusion**
([original-domain/one-Q review](../reviews/contact-pentagon-5pi7-q14-independent-hostile-review.md),
[fresh palette review](../reviews/contact-pentagon-5pi7-q14-exact-palette-review.md)).
There remain28 native-palette-compatible21-face states, four per seven
indexed split-v-run words. Their global extension is unproved. Every
one-Q translation-orbit periodic model tested is excluded; this does not
exclude periodic tilings with differently oriented Q copies or establish
aperiodicity. The authorized bounded cycle is complete.

## Exact object and audited necessary reductions

Let z=exp(iπ/14), with minimal polynomial
z¹²−z¹⁰+z⁸−z⁶+z⁴−z²+1. Work in Q(z), with the specified complex embedding
and conjugation z↦z⁻¹. Put i=z⁷ and

    s=(z−z⁻¹)/(2i)=sin(π/14),
    y=2s+4s², v=1+2s(1−y).

The pentagon P has native side lengths (x,u,w,v,y)=(1,1,1,v,y) and directed
edge exponents (−5,1,7,13,19) in z. Starting at0 and summing these five
vectors gives the exact vertices; closure and every strict support
inequality pass. Exact real algebraic comparisons give 0.22<s<0.23 and
0<y<1<v. Native vertex0 has angle α=5π/7; vertices1–4 have β=4π/7.
Q is equiangular with γ=6π/7 and side directions z²ᵏ, k=0,…,13.

All three angles exceed π/2. Hence vertices are trivalent and cannot be
T-junctions: a straight host leaves π on its other side, insufficient for
two native corners, while one native corner is strictly less thanπ. Four
native corners likewise exceed2π. The complete integer angle equation
5A+4B+6C=14 has only PPP=(2,1,0) and PPQ=(0,2,1). QQ edges are therefore
impossible. P alone cannot tile, since the PPP alpha/beta demands conflict
with oneα/fourβ per P; Q alone is impossible locally and also has14 sides.

At a PPP vertex the two α copies share a full edge. Every P's uniqueα
therefore has exactly one α–α neighbor, so the P tiles form dimers. For
general bevel lengths x,y, a matched bevel leaves equal other bevels at
that vertex, including when x=y. The β guest must consequently have an
incident pair (x,x) or(y,y), among (x,u),(u,w),(w,v),(v,y). This gives the
six equality planes stated in the original candidate note. Reflection
does not alter lengths or this argument.

For this P only β vertices1,2 have an eligible equal pair, and both pairs
are(1,1). Thus every α–α edge uses native y (side4). The unique partner is
reflection in that side, fixing its α and β endpoints. At the other
endpoint the two β corners require Qγ; native v (side3) is therefore
always a Q contact. Adjacent native w (side2) is always a P contact,
because each PPQ β corner has precisely one P and one Q neighbor. Bevel
x (side0) cannot touch Q because it has an α endpoint. The remaining
possible Q side is u (side1). All equal-length aliases x=u=w were still
enumerated as actual placements before these necessary rejections.

If p,q count P,Q anchors in a square, native counting gives
N_PPP=p/2+O(R), N_PPQ=14q+O(R) and
4p=N_PPP+2N_PPQ+O(R). Hence p=8q+O(R).
Every P has exactly one v-Q edge, and only P-v has that length. A single
Q congruence class with k native v edges therefore satisfies p=kq+O(R).
Since p+q=Θ(R²), q=Θ(R²), forcing k=8. All other Q edges have unit length,
so each Q has8v/6u. This uses counts and bounded boundary errors, not an
assumed absolute density or a favored source tiling.

## Complete closed-word domain

The original displayed word is (v,v,u,v,v,u,u)². The producer first
exhausts all C(14,8)=3003 binary words with8v/6u and exact cyclotomic
closure. Exactly35 close; each has equal antipodal lengths.

There is also a direct completeness proof. Set t=z², εᵢ=1 on v slots and0
on unit slots. Closure, with v≠1, implies ∑εᵢtⁱ=0. Let
D(T)=∑ᵢ₌₀⁶(εᵢ−εᵢ₊₇)Tⁱ. Since t⁷=−1, D(t)=0, so
D=cΦ14=c(1−T+T²−T³+T⁴−T⁵+T⁶). Its coefficients lie in{−1,0,1}; thus
c=0,±1. If c=±1, every antipodal pair has exactly one v, giving7v,
contrary to8v. Therefore c=0 and opposite lengths agree. The35 seven-bit
periods with3u/4v exhaust all equiangular Q14 partners for this exact P
under the preceding contact/count deductions. No dihedral symmetry
reduction is used in the producer.

## Actual native PPQ cycles and forced dimers

For each word, the producer verifies Q closure and every strict support.
For each Q side it enumerates every equal P side and both reflected/direct
hands, placing the full native edge exactly on the Q edge with interiors
outside Q. A unit Q side has six raw placements (P sides0,1,2 × two
hands); a v side has two. The palette/dimer restrictions leave two
placements per Q side. Each is retained by an exact unit rotation and
translation in the certificate.

Adjacent guests are compatible precisely when the other endpoints of
their incident PP sides at the shared Q vertex agree exactly. This tests
the actual whole side, not merely an equal length tag. The complete
14-cycle transition domain is exhausted, then every guest pair is checked
for disjoint interiors by exact supporting lines. Every guest's forced
α–α reflection mate is added, with coincident faces identified, and all
resulting face pairs are checked again.

Results:

- 35 closed words were examined without quotienting by symmetry.
- 14 admit native cycles; each has64 cycles, all disjoint.
- The other21 have no complete native cycle.
- Of896 guest cycles,364 admit disjoint forced-dimer completion: Q plus20 P
  faces. The other532 have a positive-area overlap after mandatory mates.
- The displayed word has64 guest cycles and36 completed21-face patches.

All14 words with native rings have some dimer-completed patches. The14
surviving words are exactly the even-v-run words, although that tag
prefilter was not used to omit geometry. Odd v runs fail the actual
endpoint transitions: each v guest has one y-tag endpoint, and such an
endpoint requires another v guest with its y tag. Every finite v run must
therefore admit a perfect adjacent pairing. The certificate retains all
35 transition matrices and all cycle keys, plus one exact21-face completed
patch per surviving word. Every other patch is reconstructible from its
cycle, exact guest placement data and reflection in each native y edge.

## Independent native-palette and periodic counterexample gates

The [same-patch adversary](../reviews/construction-adversary-2026-10-14-p5q14-palette.py)
checked all364 geometrically disjoint completed patches. Of those,336
contain an actual native corner strictly inside another face's native
edge. Since every angle exceedsπ/2, no such T-contact can extend to an
admitted plane tiling. The remaining28 have no T-contact and every
coincident native-corner group is componentwise contained in PPP=(2,1,0)
or PPQ=(0,2,1). There are no star-only rejections. The
[pointed certificate](../certificates/construction-adversary-2026-10-14-p5q14-palette.json)
and [fresh verifier](../reviews/verify_p5q14_mandatory_palette_witnesses.py)
check all336 incidences and exhaust the absence tests for all28 positives,
reconstructing from raw guest placements rather than the adversary module.

The exact indexed restart is four states per period

    vvuvvuu, vvuuvvu, vuvvuuv, vuuvvuv,
    uvvuvvu, uvvuuvv, uuvvuvv.

These are seven rotations of the split2+2 v-run period, representing one
Q shape up to congruence. The single-four-v-run word class fails the
mandatory local palette gate. The displayed word has four surviving
states.

The [independent one-Q attack](../reviews/construction-adversary-2026-10-14-p5q14-independent.py)
imposes a single Q translation orbit with primitive counts8P/1Q.
Every P guest on a unit Q side also has its forced v-Q side. Its other
neighbor must match an actual native v side of a translated copy of the
same oriented Q. Every one of the364 geometric states, hence all28 local
palette positives, fails at least one such required match. None reaches
the lattice/area/seam stage. The
[independent certificate](../certificates/construction-adversary-2026-10-14-p5q14-independent.json)
records a failed unit slot per state. This excludes that one-Q orbit
model only; no larger quotient, orientation model or patch domain was
searched after failure.

## Replay, artifacts and scope

[Producer](contact-pentagon-5pi7-q14-exact.py),
[frozen certificate](../certificates/contact-pentagon-5pi7-q14-exact.json).
[Drawings of the four surviving displayed-word states](../figures/contact-pentagon-5pi7-q14-dimer-patches.svg)
show the palette-compatible21-face patches; they are diagnostic visualizations, not
proofs of extension. Regenerate with `python render_contact_pentagon_q14_patch.py`
from this directory inside the pinned environment.
The certificate records the field representation, Sage/Python versions,
exact P geometry, all3003-mask closure results, aliases/reflections,
transition matrices, cycles and retained patches. All proof-relevant
equalities and signs use exact field/real-algebraic arithmetic. No solver,
random seed or time-limited negative conclusion is used.

```text
mise exec -- conda run --no-capture-output -n arisearch python research/searches/contact-pentagon-5pi7-q14-exact.py /tmp/contact-pentagon-5pi7-q14-exact-replay.json
```

The finite native-ring experiment is complete. Its survivors establish
only the recorded geometric compatibility. Full-plane extension, universal classification
and mixed periodic escape remain separate obligations; the original
two-convex-tile problem is unresolved. The completed one-Q/8P attack and
mandatory-patch palette audit give the refined28-state restart above.
No quotient or patch domain was enlarged after those gates.

## Restriction on a polygonal-parent inflation strategy

This pair cannot support an iterable expansive similarity hierarchy whose
finitely many simple polygonal parents are patches of whole fixed P/Q
atoms. At an interior point of a straight parent-boundary side, its inside
half-disc has angleπ. Two native atomic corners cannot fill it because
every native angle exceedsπ/2. A flat sector already fills it alone and
creates no genuine subdivision. Therefore no native corner splits the
interior of that straight boundary side, which is contained in one native
atomic side and has length at most the fixed maximum atomic side L.
A parent with p genuine sides consequently has perimeter at most pL.

Similarity preserves p, while inflation by λ>1 multiplies perimeter by
λᵏ. Composed parent rules with defining atomic patches would dissect
arbitrarily large λᵏM into those same unit atoms, contradicting the bound.
A reflex parent corner may cut an atomic side; the proof uses containment,
not equality with a whole native side. Nonconvex parents are included.
This rules out that conventional whole-atom finite-polygonal-parent
strategy, not other possible hierarchies, cuts through atoms, changing
parent boundaries or aperiodicity itself. The current disjoint21-face
patches must not be inflated as though they already supplied such a rule.
