# Exact hosted one-private dimer periodic carrier

Date:2026-10-13. Exact producer and [independent coordinate checker/audit](../reviews/contact-right-angle-one-private-hosted-carrier-hostile-review.md) PASS; adversarial verdict VALID.

The single positive metric ray isolated in research/searches/contact-structure-one-private-x2u-dimer-candidate.md admits a genuine periodic entire-plane tiling. Thus this proposed hosted one-private dimer mechanism does not supply an aperiodic pair. The claim concerns exactly this metric ray and its ordinary similarities, not all one-private or hosted palettes.

Put c=cos(pi/8), defined as the real root of8c^4-8c^2+1=0 in(9/10,1), r=4c^2-2=sqrt2 and t=r/(4c). Define x=1,u=1/2 and

    y=(r+2c-t-1)/(2c+t+1/r),
    v=1/2+rc(1-y),
    w=1+(c+1/r)(y-1),
    H=y-(u+v-y-1)/r.

Let P=(A,B,C,D,E), with A=(0,-w), B=A+(xc,-xt), C=B+(u/r,u/r), D=C+(-v/r,v/r), E=0. Let Q start at0 with cyclic side lengths(H,u,x,y,y,x,w,v) in directions0,45,...315 degrees. Both polygons close, are strictly convex, and all six lengths are positive and distinct. The pentagon has four112.5 angles and one90 angle at C; Q has eight135 angles. The only permitted host length equation is x=2u.

The exact native-Q ring producer research/searches/contact-structure-one-private-x2u-ring.py recovers its unique necessary opposite-side neighbor placements, with choices(0,0,1,1,0,0,1,0). Write h_i(P) for its Pneighbor across Qsidei, i=1,...,7. Every h_i is the unique indexed native isometry from P to this retained polygon. Writing h_i(z)=M_i z+b_i, use

    U=b_1-b_6,
    V=b_2-M_2 M_3^(-1)b_3-(H,0).

The retained isometries give M_1=M_6=-I, M_7=I and M_2 M_3^(-1)=-I. The two vectors U,V are linearly independent; their signed determinant is checked exactly and its absolute value is positive. The six pentagon and two octagon representatives can be recovered without any search for a large patch as follows: take the central Q ring, its image under z↦(H,0)-z, and each mandatory complementary pentagon at the central rings flat caps (reflection across the common perpendicular vleg). Identify representatives modulo the lattice ZU+ZV. This produces precisely two Q copies and six P copies. The producer retains every coordinate, so this is a concrete finite construction.

Orient each representative CCW. Subdivide every boundary edge whose length is x=1 at its midpoint; leave other edges whole. This yields56 oriented atomic segments. The standalone producer research/searches/contact-structure-one-private-x2u-periodic-carrier.py verifies that each atomic segment has exactly one reversed partner translated by an integral combination of U,V. The partner map is an involution, and all endpoints agree exactly. It also verifies

    sum(representative areas)=abs(det(U,V)).

All polygon placements are ordinary congruences of the original P,Q. The lattice is discrete rank two, so their closed translates form a locally finite family. The reversed atomic-boundary identities cancel the distributional derivative of integer covering multiplicity. On the connected plane this multiplicity is constant almost everywhere. Its average over a fundamental cell is1 by the area identity. Hence interiors do not overlap and no open gap exists. The locally finite union is closed, which excludes uncovered boundary points as well. This proves a legal entire-plane periodic tiling with the required half-edge contacts. It requires no claim that a finite legal patch extends and no generic finite-local-complexity assumption.

The construction permits both species and uses non-edge-to-edge contacts. It gives a periodic escape; uniqueness or periodicity of every admitted tiling is not asserted. The earlier rank-one forced Rbridge calculation was insufficient by itself; consistent half-turn Sbridges provide this explicit rank-two carrier.

Replay:

    mise exec -- conda run --no-capture-output -n arisearch python research/searches/contact-structure-one-private-x2u-periodic-carrier.py

Default stdout is the complete exact JSON, with all representatives and56 segment partner entries; --output is exclusive creation and --check fully recomputes before comparison.

Retained exact witness: research/certificates/hosted-oneprivate-x2u-periodic-carrier.json. It freezes both canonical polygons, all six native lengths, field polynomial and isolating interval, eight congruent representatives, U,V, software versions, and every atomic-segment partner. Nondestructive replay:

    mise exec -- conda run --no-capture-output -n arisearch python research/searches/contact-structure-one-private-x2u-periodic-carrier.py --check research/certificates/hosted-oneprivate-x2u-periodic-carrier.json
