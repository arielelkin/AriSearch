# Plane obstruction for the regular-pentagon six-wheel metric family

Date:2026-10-13. Status: independently hostile-reviewed VALID;
research/reviews/regular-pentagon-six-wheel-hostile-review.md.
This excludes a concrete construction family, not arbitrary convex pairs.

## Exact family and conclusion

Let R be a unit-circumradius regular pentagon with vertices vj=exp(2pi i*j/5).
Let mi=(vi+v_(i+1))/2. For0<rho<1 define the central regular pentagon
P=conv(rho*mi) and Q=cyclic(v0,m0,rho*m0,rho*m4,m4). Angles are
P:(108)^5 and Q:(108,90,126,126,90) degrees. In the notation

    L=sin36, Rlen=(1-rho)*cos36, C=rho*2sin36*cos36,

Q's side word is(L,Rlen,C,Rlen,L). To avoid confusion Rlen is a side length,
whereas R above denotes the parent polygon.
The pair is untileable when Rlen!=L. At Rlen=L, equivalently
rho=1-tan36, Q is a Type2 periodic monotile, so the pair admits a periodic
Q-only tiling. Therefore no rho in this family gives an aperiodic pair.
The specific proposed substitution rho=2/phi^3 is untileable.

All lengths are positive and C<2L because C/(2L)=rho*cos36<1.
For an arbitrary metric Q with the same angle-side endpoint word, the proof
below establishes Q untileability under C<2L and Rlen!=L.

## Permitted native stars and perpendicular cap equality

The exact full stars of this palette are108+126+126 and four90 corners.
The only flat star is90+90 opposite a straight180 sector. These stars were
proved and replayed in regular-pentagon-six-wheel-potential-obstruction.md.
In particular,108 and126 can never lie in the relative interior of another
tile side. Every Q90 corner has one L leg ending at108 and one Rlen leg
ending at126.

If two Q90 corners form a flat cap against a host side, the guests share a
perpendicular ray. Their perpendicular legs must have equal length: otherwise
the shorter leg ends with108 or126 in the relative interior of the longer
leg, impossible by the flat-star list. This is a GLOBAL extension obstruction;
a finite patch with such unequal legs may nevertheless have disjoint interiors.
When L!=Rlen, equal perpendicular legs have the same type. L-L perpendicular
legs end in108+108 at their common far endpoint, impossible in any native
full or flat star. Rlen-Rlen legs end in126+126 and require a third108 corner.
Thus only the latter cap could occur. If L=Rlen the equal-length legs might
have different endpoint types, but their along-host lengths are still equal.

## No flat cap on the C edge

A C edge has126 corners at both ends. If it hosts a flat90+90 cap, each
guest's along-host leg ends at108 or126. These nonright corners cannot lie
strictly inside the C edge. Conversely, a host126 endpoint cannot lie strictly
inside an extended guest side. Thus the two guest segments must exhaust the
C edge exactly, ending at its two native endpoints.
If L!=Rlen, the possible perpendicular Rlen-Rlen cap has along-host L-L,
so C=2L. The other perpendicular L-L cap is impossible because of its far
108+108 endpoint. If L=Rlen any cap similarly has C=2L. Since C<2L,
NO C edge can host a flat cap.

No other kind of nontrivial interior contact on C exists: the only allowed
native corner opposite a straight side is90, and then another90 completes
exactly such a cap. Consequently every C edge in a Q-only plane tiling must
meet a single complete Q edge. Neither endpoint can be in the relative
interior of that neighbor side, and the endpoint126 cannot meet a neighbor90
in any full star. The neighbor edge must therefore also be C (the other
Q edges each have a90 endpoint).

## Whole C pair forces Rlen=L

At either endpoint of a whole C-C seam, the two126 corners require a third
Q108 corner. Each adjacent seam matches an Rlen side of a126 host to an L
side of the108 guest. If these lengths differ, the shorter ends at90 inside
the longer, so a flat cap must complete that point.

If Rlen<L, the shorter Rlen endpoint's other leg is L. Its completing90 cap
must share an L perpendicular leg by perpendicular equality. That pair's far
ends108+108 are forbidden, contradiction.

If L<Rlen, the shorter L endpoint's other leg is Rlen. The completing cap
must share an Rlen leg. At their far126+126 endpoint a third108 guest is
forced. Its adjacent seams now match a C side to an L side. Such a C/L seam
starting at126+108 is impossible in every length comparison:

- C<L: the C end126 lies inside the L flat sector;
- C>L: the L end90 lies inside C and requires a C-hosted flat cap, excluded;
- C=L: the common far endpoint126+90 occurs in no full or flat star.

Thus L<Rlen is also impossible. Every Q-only tiling would contain a C-C
pair, which forces Rlen=L. This proves the claimed Q-only untileability.
The potentially tempting C=2Rlen locus is NOT an exception: its proposed
C-host cap shares perpendicular L-L and fails at the far108+108 vertex.

## The P species has zero density and a Q-only limit

Assign native weights108->1,126->-1/2,90->0. Every full or flat star has
weight zero, every Q total weight zero, and every P weight5. Group all native
corner weights in a square window by their positions. Their sum is exactly
zero because every included position has a complete incident star. Tiles
meeting the window boundary are O(r) for side-length r: bounded diameter
places them in a strip of area O(r), and positive minimum tile area bounds
their number. Replacing their incomplete corner sums by full-tile sums changes
the total by O(r). Hence the number of P tiles in the window is O(r).
The constants depend only on the two fixed shapes and apply to every centre.

There are P-free balls of arbitrarily large radius. Otherwise every ball of
some fixed radius would meet P, and disjoint coarse grid cells would force a
quadratic number of P tiles in growing squares, contradicting the linear
bound. Translate a sequence of increasingly large P-free balls to the origin.
Finite-prototile local compactness yields a Q-only plane tiling: isometry
orientations have compact O(2) parameters, centres are locally bounded in
number by fixed diameter and minimum area, and diagonal subsequences retain
all-plane coverage and disjoint interiors. Reflections and partial contacts
remain admitted. This contradicts Q untileability when Rlen!=L, proving the
original pair untileable there. This limit step is used only for exclusion,
not to infer a desired aperiodic tiling from unrelated bounded patches.

## Explicit periodic exceptional point

At rho0=1-tan36, put q0..q4 for Q's original cyclic vertices and

    A=q4, B=q0, CV=q1, D=q2, E=q3, h=D+E,
    u=CV-A, v=h-CV-A, Qstar=Q-A.

Exact coordinate identities give cross(u,v)>0, u.v=0 and |u|=|v|. The parent H formed by
Qstar and its halfturn(u+v)-Qstar has old square vertices
0,u,u+v,v and midpoint kink points

    K=(B-A,D-A,h-B-A,E-A).

The two convex Q copies occupy opposite supporting halfplanes of their
common D-E seam, so have disjoint interiors; their two outer arcs give the
modified parent boundary. This local decomposition does not rest on area
equality. All four inherited profile legs are equal. Each Ki is equidistant from its
two old side endpoints, so it is on their perpendicular bisector.
Let S be reflection across u+v, explicitly

    S=2*(u+v)*(u+v)^T/|u+v|^2-I.

In original CCW side numbering the reflected kinks are M_i=S*K_(3-i).
The exact neighboring profile identities are

    K1=M3+u, K2=M0+v, K3=M1-u, K0=M2-v.

Place H+mu+nv for m+n even and S(H)+mu+nv for m+n odd. This square
checkerboard has period lattice generated by u+v,u-v. Its explicit four-Q
motif is

    Qstar, (u+v)-Qstar, S(Qstar)+u, S((u+v)-Qstar)+u.

For complete all-plane coverage, triangulate the ordinary square grid by
its cell centres and side midpoints. Fix vertices and centres, and move each
midpoint continuously to its checkerboard kink. The profile identities ensure
a globally continuous affine map on all triangles. Every initial and final
fan determinant is positive, as checked exactly in the retained producer;
each determinant is linear along the displacement homotopy and therefore
stays positive. Local winding at every mesh vertex starts at1 and cannot
change while consecutive image rays have positive determinant. Thus each
map is a local homeomorphism. Displacements are uniformly bounded, hence
the map is proper. A proper local homeomorphism onto the connected simply
connected plane is a homeomorphism (its image is open and closed, and it
is a covering map). The image modified-square cells therefore cover the
whole plane without interior overlap. Each consists of its two stated convex
Q copies. This proves the four-Q lattice escape directly.

The producer independently checks |det(u+v,u-v)|=4area(Q); area is only a
check, not the covering argument. This construction is the square version
of the independently reviewed midpoint thin checkerboard carrier at
research/searches/current-exact-convex-source-thin-four-motif.md.

A classical corroboration uses Type2: label Q's consecutive vertices as
(old2,old3,old4,old0,old1). Then A+B+D=126+126+108=360,
a=Rlen=d=L and c=Rlen=e=L in Sugimoto's convention(a=EA,b=AB,etc).
The primary source https://arxiv.org/html/2501.07090 Figure1 / Section2 also
gives a periodic Type2 translation unit permitting reflections; the explicit
checkerboard above makes this imported classification unnecessary.

## Exact proposed rho check, computation and scope

For rho=2/phi^3, phi=(1+sqrt5)/2, exact lengths satisfyRlen<L and C<2L.
The retained producer will check these strict algebraic inequalities. The
plane proof is analytic; no bounded periodic search or local patch failure
stands in for a global claim. The native family is constructed explicitly;
no original Penrose source or generic source decoder is assumed.
This theorem closes this metric family only. Changed angles, different native
side endpoint data, C>=2L or unrelated convex pairs remain outside its scope.
