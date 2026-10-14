# Pentagon / right-heptagon: a periodic carrier with genuinely branching Q neighbors

Date:2026-10-13. Adversarially reviewed VALID for the complete positive canonical family.
Fresh whole-family review: `research/reviews/contact-pentagon-heptagon-branched-hostile-review.md`.
Independent reconstruction: `research/reviews/contact-pentagon-heptagon-branched-independent.py`.
This changes Q's side count and corner signature; no octagon H metric sweep.

## Complete unrestricted angle ledger

P has native angles90,112.5^4, Q has90,135^6. Angles sum540 and900 as
required for genuine five/seven-sided polygons. Full native stars are

    2P112.5+Q135,
    P90+2Q135, Q90+2Q135,
    four90 corners of ANY species multiset.

Flat stars are one180 host plus two90 corners of any species multiset.
These exhaust integer solutions in22.5-degree units4,5,4,6 to full16 orflat8.
Native112.5 and135 cannot occur inside another side; native90 can, so no
unrestricted whole-contact theorem is imported. Native weightsP112.5=1,
right90=4,Q135=-2 give full-star scores0 except four-right with16, and
flat-star score8. Complete tile totalsP8,Q-8. Uniform boundary-strip native
occurrence counting therefore gives

    p-q=2z+t+O(R),

where z counts all four-right stars and t all flat-host stars. No frequency,
source language or deletion of sparse defects is assumed. A zero-defect
field may have PQQ and true QQQ vertices. Neither species alone tiles:
P112.5 cannot complete using Pangles; Q-only angle incidence gives
6q=2Ntriple+O(R), q=Ntriple+4z+2t+O(R), impossible at quadratic density.
These omission risks are stated for context; direct periodic existence
below requires neither a forced language nor a compactness argument.

## A positive metric aimed at the actual clean boundary

Put r=sqrt2,c=cos(pi/8),t=sin(pi/8),w=r-2t in(0,1),A=1+w/r.
P starts at0 and integrates directions-22.5,45,135,202.5,270 with
lengths(1,1,1,1,w). Q starts at0 and integrates directions0,45,90,135,
180,225,270 with lengths

    (A,1,1,w,1,1,A).

Opposite acute legs have lengthA; vector closure is exactlyA=1+w/r.
Both polygons are strictly convex with positive native sides. Pmiddlew
is shared with Q, so the earlier absent-middle filter is deliberately
avoided. Q's intendedQQ mask is{0,1,5,6}, one contiguous four-edge run
through its unique90 corner; its three public sides form(1,w,1).
The Q90 vertex has three Qtiles90+135+135, so this is a genuine QQ branch,
not a disguised degree-two chain.

The Qgeometry has reflection symmetry about y=x. Its two unit a-slots1,5
have reflected mates translated by D=(A,-A) or-D; its private A-slots0,6
have midpoint-halfturn matesQ'=(A,0)-Q andQ'-D in this chosen carrier.
Thus each component is a two-chain periodic Qladder. This is a property
of the constructed witness, not a forcing assertion about other fillings.

## Exact entire-plane carrier

Let R be rotation45 and B=(A,0). Define

    W=R(P-P4)+Q4,
    representatives Q, B-Q, W, B-W,
    D=(A,-A), U=Q2-B+W2.

These are two Qcopies and two ordinary Pcopies, allowing halfturns.
The producer research/searches/contact-pentagon-heptagon-branched-periodic-carrier.py
checks source closure, every strict support inequality, signed native-angle
and length identities, the complete labelled angular ledger, and exact
orthogonality of R. It retains TWELVE directed native-edge pairings. Every
one of24 edges occurs once; all48 endpoint coordinate identities are exact.
The second edge translated by its listed integer combination of D,U is
the reverse of the first. It verifies

    det(D,U)>0, 2area(Q)+2area(P)=det(D,U).

The lattice is discrete rank two and bounded closed representatives give
a locally finite periodic family. COMPLETE oriented edge cancellation
makes its integer multiplicity's distributional gradient zero. Connectedness
and area/covolume1 give multiplicity1 almost everywhere. Interior overlaps
and open gaps are impossible; local finiteness makes the union closed,
so every point is covered. This proves a legal actual rank-two plane tiling
of the original five/seven-sided pair, with both species and QQQ vertices.
There is no inference from a positive finite patch or an imposed matching rule.

Reflections remain allowed throughout; the producer's native labels impose
no marks. This fixture has a periodic escape and therefore is not aperiodic.
Nothing claims periodicity of every original filling, all P5/Q7 metrics or
a resolution of the unrestricted problem.

Replay:

    mise exec -- conda run --no-capture-output -n arisearch sage research/searches/contact-pentagon-heptagon-branched-periodic-carrier.py

## Full symbolic family extension: every positive right pentagon has this partner

The SAME canonical producer additionally verifies an analytic family over
Q(c)[x,y,u,a], not a metric sweep. Let x,y,u,a>0 and define

    v=u+rc(x-y)>0,
    w=(u+v)/r-t(x+y)>0,
    A=v+w/r, B=u+w/r.

These are exactly the two native vector-closure equations of any positive
right pentagon Pword(x,u,v,y,w), up to an allowed isometry. Define Q7 by
the same0,45,...270 directions and native word

    (A,a,u,w,v,a,B).

Its vector sum is0 since A=v+w/r and B=u+w/r. All seven lengths are positive.
Q has one90 and six135 angles at ALL these metrics. No P symmetry, native
length distinctness, numeric privacy or host exclusion is assumed.

Keep the same four representatives, replacing(A,-A) by

    D=(A,-B), U=Q2-(A,0)+W2.

The twelve pair indices/shifts are UNCHANGED. The producer checks all48
endpoint-coordinate polynomial identities, both closures, exact rotation,
native-angle identities and

    det(D,U)=2area(Q)+2area(P).

Strict positivity throughout the domain follows from genuine convexity:
positive lengths, ordered fixed directions with turns in(0,180), and exact
closure put every nonincident vertex strictly in each supporting halfplane.
Thus both polygon areas are positive and det(D,U)>0, without sampling a
lattice determinant. The previous local multiplicity proof applies directly
to the entire family and yields a rank-two admitted plane tiling for each
original pair. The quartic-field embedding chooses c=cos22.5 exactly.

The Qladder geometry no longer needs reflection symmetry: its equal a
edges1,5 pair by the exact translation D becauseQ1-Q6=(A,-B) and
Q2-Q5=(A,-B). Its A/B halfturn mates are(A,0)-Q and(0,B)-Q, differing byD.
The resulting constructed QQmask{0,1,5,6} retains true Q90/Q135/Q135
branch vertices, with Pmiddles and two acute leg tags on public run(u,w,v).
No old degree-two scaffold theorem or forced source language is invoked.

Consequently EVERY positive right-angle pentagon has this explicit genuine
convex heptagon partner admitting a periodic two-species plane tiling. This
excludes aperiodicity for the stated canonical partner family; it does not
classify all possible heptagon partners or all original fillings. The fixed
four-equal fixture above is one exact included example.

## Brief pre-search rejected metric

With the same P, Qword(1,1,b,1,b,1,1), b=1-1/r, also closes positively,
but omits Pmiddlew. All acute legs are unit and every other side is below2,
so a flat cap cannot fit; a native acute host1 is too short to reach its
nonright endpoint from an interior flat point. The field would be ETE.
Pmiddlew must then PPmatch, forcing indexed Sspecies. Every P90 has only
Pneighbors, so any four-right vertex with P is entirely P. Q90 consequently
has onlyQneighbors. At Q135 the possible stars have either bothneighborsP
or bothneighborsQ (P90+2Q135 is excluded byS). Thus neighbor species is
constant around EACH Q; Q90 forces allQQ, excluding everyP Qcontact.
Q-only incidence then contradicts coverage. This is a cheap rejected
absent-middle prefilter, not the main construction or a separate search.
