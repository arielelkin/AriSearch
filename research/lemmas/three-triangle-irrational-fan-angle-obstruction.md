# An irrational common-angle obstruction for convex three-triangle fans

Date:2026-10-13. Status: independently hostile-reviewed VALID; [review](../reviews/three-triangle-irrational-fan-angle-hostile-review.md). A restricted untileability theorem, not the unrestricted two-convex impossibility result.

## Exact statement

Fix theta with theta/pi irrational. Let r_1,...,r_k be positive rational numbers satisfying0<r_i theta<pi/3. For each i, let P_i be any genuine compact convex pentagon whose native angle multiset is

    {3r_i theta, (pi-r_i theta)/2, (pi-r_i theta)/2,
       pi-r_i theta, pi-r_i theta}.

Their native cyclic orders, lengths and areas may be arbitrary whenever such polygons exist. No finite collection of these polygons tiles the plane. Reflections, partial-side contacts and omission are all permitted.

In particular, two convex radial fans formed from three congruent isosceles triangles cannot tile if their central triangle angles are positive rational multiples of a common angle irrational relative to pi. This theorem does not require a chosen dissection or an intrinsic decoder.

## Native-star dichotomy

Fixed positive-area bounded polygons give local finiteness: every tile meeting a compact set lies in its bounded-diameter enlargement, whose area bounds the number of interior-disjoint tile copies. At a native polygon corner, all incident sectors are either native corner sectors or flat pi sectors. A native vertex cannot lie in another tile interior. Two flat sectors leave no room for a positive native sector. Thus there are either no flat sectors, in which case native angles sum to2pi, or one flat sector, in which case native angles sum to pi. This is valid for arbitrary contacts without assuming an edge-to-edge tiling.

Call3r_i theta a central corner, (pi-r_i theta)/2 an endpoint corner, and pi-r_i theta an intermediate corner. These are distinct angle categories for0<r_i theta<pi/3 except possible coincidences3r_i theta=(pi-r_i theta)/2 or3r_i theta=pi-r_i theta. Either would make theta/pi rational because r_i is rational, so neither occurs here. Their native occurrence labels can also distinguish them without using numeric distinctness.

## Maximal-angle species elimination

Suppose a tiling exists and choose the maximum r among species actually appearing. There is a tile of that species, and its central corner lies at a native star. Write a_i,b_i,c_i for the nonnegative integer numbers of central, endpoint and intermediate corners from species i at that star. Let h be1 or2 according as the star has a flat sector or not. The angle equation is

    pi (sum_i b_i/2 + sum_i c_i)
      + theta (sum_i 3r_i a_i - sum_i r_i b_i/2 - sum_i r_i c_i)
      = h pi.

Both coefficients are rational. Irrationality of theta/pi therefore forces separately

    sum_i b_i/2 + sum_i c_i = h,
    sum_i 3r_i a_i = sum_i r_i(b_i/2+c_i).

But the left side of the second equation is at least3r, since the selected central corner has parameter r. Every present species has r_i<=r, so its right side is at most

    r (sum_i b_i/2+sum_i c_i)=rh<=2r.

This contradiction rules out a tiling. Choosing the maximum among actually used species handles species omission; there is no assumed positive frequency, density limit or global hierarchy. The star is finite by local finiteness, and the proof is pointwise.

## Nonempty exact geometric family

Let u=(2+i)/sqrt(5), with positive sqrt(5), and theta=arctan(1/2). Then0<theta<pi/6. The pentagons

    P_1=convex cycle(0,1,u,u^2,u^3),
    P_2=convex cycle(0,1,u^2,u^4,u^6)

are exact algebraic polygons in R² by real and imaginary parts. Their respective radial fans consist of the three triangles with origin and successive pairs of radial unit-circle points. The triangles are congruent within each fan and have central angles theta and2theta respectively. All pentagon corners are strictly convex because3theta<pi and6theta<pi; the stated five-angle signatures follow directly from the unit-circle chord geometry. They are distinct congruence classes: their areas are3/(2sqrt(5)) and6/5 respectively, hence unequal.

Irrationality is elementary: if theta/pi were rational, exp(2i theta) would be a root of unity, so2cos(2theta) would be an algebraic integer. Yet cos(2theta)=3/5, and6/5 is a rational noninteger, whereas every rational algebraic integer is an integer. The contradiction proves the required irrationality. Consequently the displayed pair admits NO plane tiling; it is not an aperiodic construction.

## Dependencies, computation and scope

Only elementary convex polygon local finiteness, rational independence, and the algebraic-integer property of roots of unity are used. No solver or finite computation enters the proof. Exact coordinate verification is possible directly from u conjugate(u)=1 and powers of u; algebraic data sqrt(5)^2=5, sqrt(5)>0 are sufficient.

The conclusion does not extend to arbitrary affine relations r_i theta+s_i pi with nonzero s_i, to noncommensurate angular parameters without another separation argument, to rational angles, to larger or cut triangle clusters with different signatures, or to arbitrary pentagon pairs. A new fan construction must change one of these explicitly used assumptions. Literal unmarked triangles themselves also admit periodic tilings, so a selected pinwheel substitution does not supply shape-only forcing.
