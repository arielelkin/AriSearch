# Independent hostile review: pentagon/higher-partner substitution bound

Date: 2026-10-13. Reviewer: higher-partner research agent, not the author.
Verdict: **VALID**. No unresolved mathematical defect found.

## Exact claims reviewed

The [root artifact](../lemmas/pentagon-higher-partner-positive-conjugate-bound.md)
claims (i) a nontrivial finite dissection of a genuine convex pentagon into
convex children each with at least five sides requires at least six children;
(ii) an ordinary two-species similarity substitution with a pentagon and
an n>=5 convex partner, irrational quadratic area multiplier mu and positive
conjugate, requires mu >= (5+sqrt(13))/2.

## Assumptions and attack cases

I checked partial contacts/T-junctions, seams at outer corners, disconnected
seam components, cycles tangent to the outer boundary, side subdivisions,
one-child cross-species images, reducible matrices, column convention,
positive-conjugate determinant, and all integer diagonal cases.

The finite dissection argument is sound. For clarity, the connected planar
graph justification underlying F=E-I+1 can be made explicit: the union of
all child boundaries is connected. The finite tile intersection graph is
connected because otherwise its two disjoint compact subunions disconnect
the parent. Intersections of two interior-disjoint convex children lie on
both boundaries, and each child boundary is connected. The full planarized
graph, including the outer boundary, is therefore connected. Subtracting
the outer boundary's equal numbers of edges and vertices from disk Euler
gives the displayed identity. This covers seam components connected only
through different parts of the outer boundary. It is a justification of the
used identity, not an additional geometric hypothesis.

In the forest case the degree sum gives2E>=3I+B+J. Substituting
E=I+B+J-k gives I<=B+J-2k. Together with
B+J=F+k-1 and the angle sum, the contradiction H<=-k-J follows exactly.
Inserted straight incidences H are nonnegative even with partial contacts.
An interior degree-two kink would have complementary sectors with one
angle exceedingpi and violate convexity, so suppression is legitimate.

A simple seam cycle cannot contain a positive-length outer-boundary
segment: seam edges have relative interiors inside the parent, and the
parent is convex. Its bounded Jordan region lies inside the parent. It has
positive area, hence contains some child interior. Every such child lies
inside the region, since it cannot cross a seam cycle into a tile interior.
It can meet the outer boundary only at finitely many cycle/boundary nodes,
so every genuine side has positive-length contact with another child.
Convex intersection then requires distinct neighbours for distinct sides.
Five neighbours plus the selected child proves the six-child bound. No
particular cycle length or trivalent assumption was inserted.

For the matrix claim, a positive area left eigenvector and b,c>0 place mu
at the Perron root. Quadratic irrationality forces b,c>0; positive determinant
forces a,d>=1. One-child images contradict either mu>1 or determinant
positivity exactly as stated. Thus the pentagon column has a+c>=6.
The four a=1,2,3,4 branches and a>=5 exhaust all integers. Their lower
comparison matrices give the stated bound. In particular the a=4 comparison
[[4,1],[2,1]] has determinant2>0, while a=3 gives the minimizer
[[3,1],[3,2]] with determinant3 and Perron root(5+sqrt13)/2.
No n-gon-parent six-child requirement is needed or silently assumed.

## Defects, repairs and uncertainty

No invalidity found; no author-file repair made. The connected-boundary
argument above expands a standard Euler premise. The scope remains finite
ordinary substitution geometry. Matrix equality has no exhibited geometric
realization. No novelty claim, plane-tilability claim, hierarchy recognition,
or unrestricted aperiodicity/impossibility statement is validated here.
No computation or bounded search was needed.
