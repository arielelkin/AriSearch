# Penrose rhomb-center power diagram: bounded first gate

Date: 2026-10-19. Status: exact computation independently [hostile-reviewed valid](../reviews/penrose-weighted-center-first-gate-hostile-sol-2026-10-19.md) on the stated interval. This is a materially changed rule from the unweighted Voronoi rule. It remains an incomplete exclusion of this one-parameter family, not a solution of the research problem.

## Rule and result

Assign each genuine unit-edge Penrose rhomb its center, weight zero for a thin (red Robinson-paired) rhomb, and weight delta for a thick (blue) rhomb. A power cell minimizes |x-c|^2-weight(c). Adding a common weight changes nothing. This assignment commutes with all Euclidean isometries.

Put phi=(1+sqrt(5))/2. For every

    -1/4 <= delta < phi/3+1/4,

the exact whole-plane substitution source used in the reviewed unweighted artifact has a complete strict convex quadrilateral power cell. Any proposed two-shape set containing every output class therefore fails unrestricted aperiodicity: this quadrilateral alone tiles periodically. This statement requires no census of all output classes.

The source and nesting proof are those in `penrose-center-voronoi-quadrilateral-2026-10-19.md`: the 20 labelled triangles of inflated level 1 occur in level 5, hence levels 1+4k form a nested genuine source whose supports exhaust the plane. The present script reconstructs and checks this source, base pairing, side lengths, and unmatched boundary bases independently on every replay. It uses the same primary recurrence and the same explicitly stated standard Robinson pairing dependency. Rhomb index 23 is thin; the 430 complete level-5 rhombs are genuine occurrences in that infinite source.

## Finite exact certificate

For center c at index 23, the four consecutive supporting centers have indices 21,68,18,22. In coordinates relative to c, each inequality is

    (q-c) dot v <= (|q-c|^2 + weight(c)-weight(q))/2.

Intersect consecutive supporting lines to obtain four affine vertices v_k(delta)=a_k+b_k delta. Their exact coefficients, over Q(phi) in the orthogonal frame z=x+i sin(36 degrees)y, are retained in the JSON certificate. The script imposes all 430 site inequalities on all four affine vertices. Since each residual is affine, their intersection is exactly the closed finite-constraint interval [-1/4,phi/3+1/4]. No numerical root decisions occur. At the lower endpoint, additional sites 27 and 71 touch vertex 2 without shortening an existing edge. At the upper endpoint some vertices coincide and strict quadrilaterality fails. The result does not claim that the cell ceases to be a quadrilateral outside this interval after changing its supports.

For each cyclic turn, the script verifies the quadratic turn polynomial has positive value at the lower endpoint and nonnegative Bernstein coefficients on the closed interval. It is therefore positive everywhere except possibly at the upper endpoint, which is excluded. Consequently all four supporting segments are genuine sides throughout the stated half-open interval. Every affine vertex has squared norm strictly below 1 at both endpoints; convexity of squared norm gives the same strict bound throughout.

## Infinite-tail completeness

The minimum squared distance from c to the exposed boundary of the union U of all 430 complete source rhombs is 7+(37/4)phi>9, checked exactly. The point c lies inside its source rhomb. Thus B(c,3) is contained in U. Every source rhomb not among these 430 has interior disjoint from U, and its center q therefore satisfies D=|q-c|>=3.

For every computed cell point v, |v|<1. On the certified parameter interval |delta|<1, so every omitted constraint has slack

    D^2 - 2(q-c) dot v + weight(c)-weight(q)
      > D^2 - 2D - 1 >= 2.

This proves that no omitted source center cuts the cell. The tail argument covers the whole real interval uniformly and is not an inference from an arbitrarily large finite patch.

## Search record and stop

Question: does this weighted intrinsic-center rule retain a periodic omission witness on an exact parameter interval? Domain: the fixed index-23 cell, its four original supports, all 430 finite constraints, all exposed source edges, and all real parameters satisfying those support constraints. Arithmetic: Sage CyclotomicField(10), with exact AA comparisons in the embedding exp(i pi/5); coefficient identities are checked in the field. There is no random seed, solver, floating branch, timeout, congruence reduction, or enumeration beyond this domain. Endpoint, convexity, and tail checks completed.

Replay:

    mise exec -- conda run --no-capture-output -n arisearch python research/searches/penrose-weighted-center-first-gate-sol-2026-10-19.py --check

The script and certificate use this report's stem with `.py` and `.json` suffixes. The independent Sol review reconstructed the power-cell geometry over Q(sqrt5) and supplied a separate exact checker. This bounded calculation proves failure on the stated interval. It proves neither failure nor success for delta<-1/4 or delta>=phi/3+1/4. In particular no interval with at most two exact output congruence classes has been established. A parameter-wide exclusion would require additional complete cells or an exact parameter classification with uniform source-tail bounds. A surviving interval would additionally require a complete output census and a shape-only forcing proof for every unrestricted tiling, including omissions, reflections, and partial contacts. No such global forcing mechanism is supplied. The present first-gate cycle stops here rather than treating those theorem-strength gaps as computational evidence.
