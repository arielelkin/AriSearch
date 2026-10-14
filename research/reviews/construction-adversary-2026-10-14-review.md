# Fresh review of the construction adversary and one-Q-orbit negative

Date: 2026-10-14. Verdict: **VALID for the stated exact domains**, including the
conditional one-Q-translation-orbit exclusion after mandatory dimer completion.
No infinite construction or aperiodicity conclusion follows.

Reviewed implementations:
[generic applied adversary](../searches/construction-adversary-2026-10-14.py),
[its scope note](../searches/construction-adversary-2026-10-14.md), and
[independent P5/Q14 reconstruction](construction-adversary-2026-10-14-p5q14-independent.py).
The reviewer did not develop either implementation. The new
[critical checker](verify_construction_adversary_one_q_orbit.py) imports no adversary
or producer module and reads only the exact raw author certificate geometry and
cycle records.

## Generic geometric predicates and periodic sufficiency

Clipping normalizes each polygon to positive winding before testing supporting
halfplanes. The separating-axis implementation takes both polygons' native edge
normals and checks exact extrema, permitting arbitrary winding and tangencies.
The attachment implementation tries all equal native side lengths, both endpoint
identifications and both determinant signs, then retains opposite-side interiors.
The native source indices survive reflection. No alias uniqueness or prototype
symmetry is silently assumed. Congruence tests both cyclic orientations and all
pairwise squared distances; for the strictly convex prototypes this identifies
the actual polygon under allowed isometries.

The explicit periodic validator is a sound sufficient test. After normalizing
representative winding, it checks convexity, prototype congruence, a nonsingular
lattice, a complete involutive pairing of reversed full edges with integer deck
shifts, and total representative area equal to absolute covolume. Every candidate
edge shift is solved directly in the exact lattice basis; there is no bounded
translation-radius omission. Unique pairing is stricter than necessary but safe.

For completeness, sum the indicator functions of all representatives and their
lattice translates. This is a locally finite, nonnegative integer multiplicity
function. Reversed edge pairing cancels its distributional boundary jumps. It is
therefore constant almost everywhere on the connected plane. Its lattice mean is
one by the area/covolume check, so its value is one almost everywhere. There can
be no positive-area overlap or open gap. Local finiteness of the closed polygons
covers boundary points too. This argument permits accidental coincident edges;
it does not need a separate finite overlap-neighbor bound. A successful witness
is consequently a genuine periodic escape.

The finite omission domain for larger polygons tries two native-halfturn copies
and all pairs of native seam-midpoint gains as period generators. Failure is
correctly NO_WITNESS_IN_DOMAIN; it neither excludes monohedral tilings nor
certifies aperiodicity. The triangle/quadrilateral positive constructions and
known right-P/regular-Q8 mixed carrier give meaningful witnessed controls.

The complete generic certificate replay passed. Controls exercise all four
subject/clip winding combinations, overlapping and tangent squares, all square
side aliases and both reflection hands, accepted square omission, a rejected
mispaired proposed lattice, and the exact right-P/Q8 periodic carrier.
Regular P5/Q8 has angles108 and135 degrees; no nonnegative integer combination
sums180 or360, so its palette obstruction is genuinely exhaustive. The applied
new P5/Q6 seam failures concern whole native seams only; its30/60 omitted-witness
searches remain inconclusive.

## P5/Q14 indexing, omissions and forced contacts

The P5/Q14 implementation works with z=exp(i*pi/14), exact cyclotomic28
coordinates and an explicit QQbar embedding for signs. It constructs P with
lengths(1,1,1,v,y), directions(-5,1,7,13,19) in powers of z, 0<y<1<v.
The pentagon angles are alpha=5pi/7 and beta=4pi/7, while Q14 has gamma=6pi/7.
All exceedpi/2. Thus a full star has at most3 native corners, and a flat host
would need at least2 native corners summingpi, which is impossible.
The only full palettes are PPP=(2alpha,beta) and PPQ=(2beta,gamma).

For P alone, a star has zero weight under alpha->1,beta->-2, while a tile has
weight1-8=-7. Bounded boundary errors cannot balance quadratic tile counts, so
P omission is impossible under arbitrary contacts. Q alone has neither a full
nor a flat star, so Q omission is impossible locally. These exact necessary
arguments are stronger than the finite halfturn-lattice witness-search failure.
They do not assume a periodic tiling or a favored source hierarchy.

Native unit aliases0,1,2 are all counted geometrically before the existing
palette/dimer reductions leave only native1 on a Q unit side; native3 is the
unique v side. The mandatory alpha-alpha y dimers force every native3 v side
to contact Q. The independent options loop tries both hands and both endpoint
assignments, filters opposite-side interiors, and retains exactly2 actual
placements on each remaining side. Adjacent-cycle conditions compare the actual
other PP endpoints. Reflection across native y fixes both seam endpoints and
produces the forced mate; deduplication by exact vertex sets is valid for the
strictly convex polygons.

This review relies on the separately retained exact native-ring/dimer census for
its896 rings,364 disjoint dimer completions and532 forced overlap exclusions.
It did not rerun that entire census unnecessarily. The later separate
P5/Q14 endpoint-completion audit is outside this review; its28 dimer-valid
survivors are covered by this checker of all364 dimer-valid cycles. The new critical check
independently reconstructs the exact raw guests in the author's certificate,
without trusting its rejection strings or any C one-Q verdict. It verifies
opposite-side placement, unit isometries, actual PP endpoint cycles, and all
native-v candidate translation contacts.

## Independent critical one-Q check and its exact scope

The checker reads
[raw author geometry](../certificates/contact-pentagon-5pi7-q14-exact.json).
For each unit guest it reconstructs its actual native3 edge [F3,F4]. For every
one of Q's eight native v edges, it tries both translations mapping the source
edge's first endpoint to F3 or F4, demands exact equality of the two endpoint
sets, and checks that the translated Q interior is opposite the P interior.
This method uses actual polygon geometry rather than the author's handedness
formula, and has no lattice basis, period-generator choice or shift-radius bound.
It automatically includes equal-length native aliases and physical symmetries
of Q. The original formula is also correct: a direct P needs the opposite native
v vector, whereas a reflected P needs the same native vector relative to the
fixed counterclockwise Q.

Replay passed for all35 raw Q words,896 rings and5376 unit-guest bridges. Every
one of the364 dimer-valid rings has at least one mandatory v neighbor that cannot
be a translate of Q. The dimer hypothesis matters:868 of the896 pre-dimer rings
have such a failed bridge; the other28 pass all bridge tests, but all28 have
already been rejected for forced-dimer overlap. These are distinct from the
separate28 dimer-valid survivors of the later endpoint-completion audit. No claim that all896 rings fail
the translation test alone is valid.

This proves more than failure of one chosen fundamental basis. In any admitted
tiling of a fixed pair from this35-word domain, each Q has one of the retained
actual native rings and its forced dimers. If all Q polygons were in a single
translation orbit, every mandatory v neighbor would be some translate of this
same physical Q. The failing local bridge contradicts that. A global rotation
or reflection normalizes any single physical Q orientation to the saved
representative; both P hands and all native edges are already included. Therefore
**if a plane tiling exists, its Q copies cannot all belong to one translation
orbit**. Equivalently, modulo actual Q symmetries, at least two physical Q
orientations are necessary. This does not establish existence, exclude periodic
cells with multiple Q orientations, or prove aperiodicity.

## Fresh check of the no-flat finite-parent corollary

Reviewed corollary: [updated primary-track note](../searches/contact-pentagon-5pi7-q14-exact.md).

The repaired statement is valid for any simple finite polygonal parent dissected
into these fixed atoms, including nonconvex parents. Suppose a child native
corner lay in the relative interior of a genuine straight parent side. The inside
halfplane there has anglepi. At least2 strictly convex child corners would have
to fill it, and their angles are each greater thanpi/2, a contradiction. A flat
child sector already fills that halfplane and leaves no room for another corner.
Consequently no child native vertex can subdivide a genuine parent side. Each
parent side is CONTAINED IN one native atomic side, and its length is at most the
maximum atomic length L. It need not equal a full native side: a reflex parent
corner can truncate an atomic edge.

For p genuine parent corners, perimeter(parent)<=pL. A fixed finite polygon M
cannot therefore have dissections of every similarly inflated lambda^k M with
lambda>1, since p stays fixed and its perimeter grows without bound. This closes
that finite-polygon-parent strategy for this all-obtuse palette; it says nothing
about aperiodicity via another mechanism. Hole and disconnected-parent variants
are outside this reviewed corollary.

## Replay, defects and remaining obligations

    mise exec -- conda run --no-capture-output -n arisearch python research/reviews/verify_construction_adversary_one_q_orbit.py
    mise exec -- conda run --no-capture-output -n arisearch python research/searches/construction-adversary-2026-10-14.py --check research/certificates/construction-adversary-2026-10-14.json

Both checks passed. No source producer, retained certificate, registry or discovery
log was changed. No unresolved mathematical defect was found within the reviewed
claims. The unused pre-dimer28-ring case must not be silently absorbed into the
stronger negative without its mandatory overlap rejection. Plane existence and
mixed periodic witnesses with multiple physical Q orientations remain open.
The generic note's P5/Q14 review link was not yet present when read; root can
point that reference at this completed audit or the eventual primary-track review.
