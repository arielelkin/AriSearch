# Exact five/four fixture has an A-only periodic tiling

Date: 2026-10-19. Status: exact certificate internally checked; awaiting independent hostile review.
Claim falsified: this particular pair could be aperiodic under the problem definitions.
This does not classify its mixed tilings or its dimer-corona extensions.

Put r=sqrt(3)>0. In counterclockwise order the exact A vertices are

    (0,0), (1,0), (1,2), (1-3r/2,7/2), (-3r/2,7/2), (-2r,2).

Its side word is (0,1,2,0,3,4) for lengths (1,2,3,r,4),
and its end-of-side angles are (90,120,150,120,90,150) degrees.
The corresponding B vertices are

    (0,0), (1,0), (1+r,1), (1+r,3), (r,3), (-r/2,3/2).

B has word (0,1,1,0,2,3) and angles (150,120,90,150,90,120).
The verifier constructs both from their words and exact rotations, checks closure,
and checks that every nonincident vertex lies strictly left of each side.
Thus both are simple strictly convex hexagons. Their angle descriptions are
realized exactly, without a numerical reconstruction.

## Periodic certificate and direct proof

Let h=(2+2r,0), t=(-3r/2,7/2), s=(2,2), L=Zh+Zt.
The complete tile family is

    { A + ell, -A + s + ell : ell in L }.

Here -A means a half turn, which is an allowed isometry. The determinant of
(h,t) is 7+7r, and area(A)=(7+7r)/2. Both periods are nonzero and independent.
Number each directed boundary side i from vertex i to vertex i+1 modulo 6.
For the A representative the reversed matching edges are as follows:

| A side | Representative and lattice offset of matching side |
| --- | --- |
| 0 | A side 3 at -t |
| 1 | (-A+s) side 1 at 0 |
| 2 | (-A+s) side 2 at t |
| 3 | A side 0 at t |
| 4 | (-A+s) side 4 at -h+t |
| 5 | (-A+s) side 5 at -h |

The other six matches follow by the half turn x -> s-x. All equalities are
exact endpoint equalities; the checker independently finds the unique match
for every side among both representatives and all lattice offsets (integer
coordinates are solved exactly, rather than bounded enumeration).

For completeness this boundary certificate proves both no gaps and no overlaps.
Let m(x) be the sum of the indicators of all listed closed tiles, ignoring
boundaries of measure zero. The lattice family is locally finite. Each
oriented polygon-boundary measure has its negative in the ledger, so the
distributional gradient of m vanishes. A locally integrable function with
zero distributional gradient on the connected plane is constant almost
everywhere. Its integral over a lattice cell is the sum of the representative
areas, equal to det(h,t). Its constant value is therefore exactly 1.
Any overlap of interiors contains an open set of positive measure and would
contradict m=1 almost everywhere. The locally finite union of closed tiles
is closed; an uncovered point would have an open uncovered neighborhood,
also contradicting m=1 almost everywhere. This proves a plane tiling.
Consequently the pair admits a doubly periodic tiling omitting B and is not
aperiodic under the stated problem definitions.

## Relation to the existing source theorem

The monohedral escape construction in
`research/lemmas/hexagon-both-opposite-repeat-periodicity-2026-10-15.md`
requires one actual convex hexagon with equal opposite native sides 0 and 3,
and end-of-side angle triples {0,1,2} and {3,4,5} summing to 360 degrees.
A satisfies every one of these assumptions exactly. Its repeated side length
is 1, both triples sum to 360, and strict convexity is verified above.
That source pairs side0 to side3 within each of two oriented faces, and
pairs every other native side across the faces. The explicit lattice above
realizes those same pairings. No assumption about B, a mixed source support,
a corona, or an extension of a finite patch is used in this certificate.
The direct boundary proof avoids reliance on the imported classification or
the flat-torus development theorem.

## Replay and scope

    mise exec -- conda run --no-capture-output -n arisearch python research/searches/hexagon-five-four-periodic-attack-2026-10-19.py

The check uses exact arithmetic in Q(sqrt(3)) via Sage, no solver, randomness,
timeout, parameter sampling, or numerical geometry. It checks exactly these
two shapes and the displayed two-representative lattice. It is a positive
infinite periodic certificate, not a bounded negative tiling search.
