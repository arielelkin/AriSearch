# Fresh hostile review: sixty-degree pentagon / equiangular dodecagon omission

Date:2026-10-13. Reviewer:source_recovery. Verdict:VALID.
Reviewed research/lemmas/sixty-degree-pentagon-equiangular-dodecagon-omission.md.

The angle classification is exact: at a150 corner a flat180 leaves30,
which no palette corner can fill. With one Q, remaining210 is not a multiple
of60; two Q leave60; three exceed360. Thus only QQP150+150+60 stars contain
Q, including unrestricted native/flat possibilities. The Q corner cannot
be interior to another native edge for the same30 obstruction. Positive QQ
contacts are therefore whole on both sides. At each Q vertex the two Q
sectors are adjacent and share one incident edge ray, so each Q native side
is either wholly QQ or starts and ends with P60; the QQ slots alternate.

The directed side-cover induction is valid without an edge-to-edge rule.
At an interior point of a Q side, a P60-started interval cannot change
neighbor before that P's native endpoint: two flat sectors already exhaust
360. Its far native endpoint is120. If the P edge were longer than the
remaining Q side interval, it would contain the far Q150 vertex in its
interior, forbidden by150+180>360 minus insufficient30. If the edges end
together, the P120 cannot be the unique required P60 at that QQP star.
If it ends earlier, the actual Q-flat180+P120 leaves exactly60, uniquely
forcing the next P's acute corner. The same alternatives repeat. No third
P60 flat cap can replace this120 endpoint: only60 remains. Every successful
intermediate interval is a whole positive native P acute-adjacent edge,
with a fixed positive lower length bound. Thus there are only finitely many
steps, and none reaches the far endpoint. This is a genuine contradiction
to Q occurrence, not a frequency or finite-patch inference.

The result only says all admitted plane tilings omit Q. P-only tilings may
exist and their periodicity has not been assumed or deduced. Arbitrary side
lengths, reflections and partial contacts remain in scope. No objection.

## Fresh audit of the infinite n-partner extension

Verdict:VALID for n>=9, n not2(mod4), n not4(mod16), exactly as stated.
The full-star arithmetic is complete. theta<=80 implies beta>theta and
2beta>180+theta/2. A single Q can therefore have either zero or one beta:
the corresponding acute counts(n+2)/4 and(n+12)/16 are nonintegral in the
stated residue classes. Two Q leave exactlytheta; three exceed360. A Q
corner against any flat host leaves theta/2 below all native angles.
Hence QQ contacts are whole and QQ/QP alternation holds; odd n excludesQ
already, without invoking any directed chain.

For even n, an arriving beta endpoint against flatQ leaves
45+theta/4<beta. Any remaining sectors must be native theta, with count
(n+4)/16; if nonintegral there is no legal internal endpoint. If this count
is integral and exceeds1, the sector adjacent to the FORWARD host-side ray
still belongs to one Ptheta tile. Other theta sectors occupy wedges between
that tile and the arriving beta tile and do not displace the forward guest.
That forward tile's acute native edge is therefore the next boundary
interval. It cannot change neighbor before its native endpoint because
Pflat+Qflat already exhaust360. A longer edge through the far Qcorner is
forbidden by the flat-Qcorner obstruction; an equal ending gives beta,
where the only allowed QQP star requires theta. Every shorter edge is a
whole fixed acute leg and has a uniform positive lower length. Thus the
same finite-step contradiction is valid even with several intervening
acute sectors. The extension asserts only Q omission; the excluded residue
classes and P-only periodicity remain outside scope.

## Independent audit of the stronger whole-family corner potential

The appended formal stronger extension in the reviewed lemma is VALID: all n>=9 except n=12 make the
entire pair untileable. The n=12 case retains the separately proved Q
omission, without a P-only periodicity claim. This audit checks exact
star arithmetic and the unrestricted corner-window obstruction.

A star containing a>=1 Pbeta corners, b Ptheta corners and c Qgamma
corners must satisfy

    a(3n-4)+16b+4c(n-2)=8n (full), or4n (one flat host).

For full stars a<=3,c<=2. The only feasible pairs(a,c) are:
(1,0), b=(5n+4)/16, requiring n12mod16;
(2,0), b=(n+4)/8, requiring n4mod8;
(3,0), b=(12-n)/16, possible only n=12;
(1,1), b=(n+12)/16, requiring n4mod16.
All other pairs give negative b for n>=9. For flat stars a<=1,c<=1;
only(1,0), b=(n+4)/16, is possible, requiring n12mod16.
Therefore n not4mod8 admits no Pbeta occurrence. P cannot occur at all,
and Q-only cannot fill a native Qgamma corner: two gamma leave theta,
three exceed360, and a flat host leaves theta/2. The pair is untileable.

For n=16k+12,k>=1, the reviewed residue omission theorem removes Q.
The P-only full stars are2beta+(2k+2)theta,
beta+(5k+4)theta and(8k+6)theta; flat stars are
beta+(k+1)theta and(4k+3)theta. Assign theta weight1 and beta weight-(k+1).
Their scores are respectively0,4k+3,8k+6,0,4k+3, all nonnegative.
Every P has total weight1-4(k+1)=-(4k+3)<0. The excluded k=0 is essential:
at n=12 the additional full3beta star would have negative score.

For n=16k+4,k>=1, put theta weight1,beta weight-(2k+1)/2,
gamma weight-1/2. Dividing the angle equation by theta gives
beta/theta=3k+1/2,gamma/theta=4k+1/2, full total8k+2,
flat total4k+1. Parity of a+c and nonnegativity exhaust full stars as
2beta+(2k+1)theta, beta+gamma+(k+1)theta,2gamma+theta,
and(8k+2)theta. The first three have score0 and the last positive.
The only flat star is(4k+1)theta, with positive score. P has total
weight-(4k+1), Q total weight-n/2, both strictly negative.

For either weight argument, summing complete native corner occurrences
inside a square gives a nonnegative sum, since every whole geometric
star has nonnegative score; side-interior hosts have no native weight.
Summing complete prototile weights for centroid-anchored tiles differs
only by O(R) in a fixed-width boundary strip. Positive fixed tile areas
and bounded diameters provide this uniform error and force quadratically
many tiles by coverage. All complete tile weights are bounded strictly
below0, so the same sum is negative quadratic plus O(R), contradiction.
This proof permits arbitrary vertex coalescence, partial contacts, rotations,
reflections and omission. It requires no positive individual species
frequency, vertex separation, FLC or matching rule.

## Fresh audit of the n=12 omission carrier

Verdict:VALID. The pentagon's unique60 corner is adjacent to120, so choose
that connecting side AB. The halfturn about its midpoint puts the two
convex pentagons in opposite supporting halfplanes. Their union is a disk
with an eight-edge boundary before simplification; at A and B the joined
angles are180, merging the two pairs of adjacent edges. The remaining six
corners all equal120, so the resulting polygon is a genuine strictly
convex centrally symmetric hexagon. No other degeneracy occurs because
all original native sides are positive and the remaining angles are120.

For a centred CCW hexagon(v0,v1,v2,-v0,-v1,-v2), the stated a=v0+v1,
b=v1+v2 pair its three edges to opposite reversed edges by displacements
a,b,b-a. The direct cross-product expansion gives det(a,b)=area(H)>0,
exactly as written, so the lattice is discrete rank two. All six oriented
edges cancel in the periodic indicator gradient, and area/covolume is1.
This proves genuine plane cover/nonoverlap by the reviewed multiplicity
argument, without assuming a hexagon classification. Subdividing every
hexagon by its original seam gives a periodic tiling by allowed P copies.
Thus n=12 admits a periodic P-only omission escape for EVERY positive P
metric, while the other n>=9 pairs are untileable. The complete stated
angle/size family supplies no aperiodic pair. This conclusion retains
unrestricted rotations, reflections, contacts and species omission.
