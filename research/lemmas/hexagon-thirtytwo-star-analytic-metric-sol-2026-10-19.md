# Last B orbit: exact analytic metric feasibility

For A=(0,1,2,0,3,4), B=(0,1,2,0,3,1), the retained eight-star support has a strictly convex closed common-length realization with five distinct positive lengths, and neither polygon belongs to monohedral classes H1/H2/H3. This is an existence proof by the analytic implicit function theorem; it does not establish a geometric corona or any plane tiling.

## Exact construction

Use radians throughout. Let C be the six-row matrix for the two polygon totals and the four displayed support equations

- a0+a1+b2=2π;
- a2+b1+b5=2π;
- a3+b0+b4=2π;
- a4+a5+b3=2π.

C has rank five. Let N be the exact 12 by 7 nullspace matrix in the accompanying certificate, and write the angles as θ=(2π/3)1+Nx. Thus every support equation and both polygon totals hold identically.

Define edge j's direction in polygon f by φ(f,0)=0 and φ(f,j)=Σ(k=1..j)(π-θ(f,k)). Let F(x,l) be the four real components of Σ(j=0..5) l[word(f,j)] exp(i φ(f,j)). At x=0 and l=(2,1,1,1,1), F=0 exactly: the two length-two opposite edges cancel, and the four remaining unit root-of-unity vectors cancel. Both polygons at this base are strictly convex.

The exact derivative D=∂F/∂(x0,x1,x2,x3) at the base is

```
[ 0   √3/2  -√3/2    -√3   ]
[ 2   -1/2   -1/2      2   ]
[ 0      0       0   -√3/2 ]
[ 0      0       2    5/2  ]
```

Its determinant is -3. Set l(t)=(2,1+t,1+2t,1+3t,1+4t), x4=t, x5=x6=0. The analytic implicit function theorem provides unique analytic x0(t),…,x3(t), vanishing at zero, with F=0 for all sufficiently small |t|. This is an exact existence statement, not a numerical closure approximation. For every sufficiently small positive t<1/4, the five lengths are positive and pairwise distinct. The resulting vertices remain strictly convex and simple by continuity from the strictly convex base polygon.

## Monohedral audit

The replay checks all twelve dihedral labels for each polygon, using start-of-side angles θj (the forward end angle of side j is θ(j+1)). The only opposite equal pair in either word is edges0/3. Every matching H1 label has a nonzero angle-sum derivative; representative sums θ1+θ2+θ3 have derivatives (5√3-1)/4 for A and (1+√3)/2 for B. The complementary sums have opposite derivatives.

A has no matching H2 length pattern. B does: forward offset4 and reverse offset2. Their required angle sums are respectively b4+b5+b1 and b3+b2+b0, with derivatives ±3(1+√3)/2, so both fail for sufficiently small positive t. No dihedral labeling of either word has the adjacent equal pairs required by H3. The finite collection of nonzero derivatives therefore excludes every H1/H2/H3 instance on one sufficiently small positive interval. The full label audit and exact derivatives are in the certificate.

## Scope and remaining mechanism (§5)

The formal support and closed metric gates are passed. A geometric realization of an entire formal corona has not been certified: prescribed stars are individually angle-compatible, but overlap of their developed neighboring polygons has not been checked. An unbounded extension mechanism, or a universal periodic escape, is also missing. No plane tiling or unrestricted aperiodicity follows from this IFT certificate.

Replay: `mise exec -- conda run --no-capture-output -n arisearch python research/searches/hexagon-thirtytwo-star-analytic-metric-sol-2026-10-19.py`.

The earlier denominator12 cyclotomic coefficient-rank gate only tested rational length vectors; its failure does not obstruct this real analytic family. An independent test of the same64 angle points over Sage AA found no positive five-distinct one-dimensional real kernel, but that bounded check is not needed for the proof above.
