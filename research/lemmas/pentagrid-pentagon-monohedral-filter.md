# Monohedral filter for the three pentagrid pentagon words

**Status:** adversarially reviewed as valid in the
[fresh source and algebra audit](../reviews/pentagrid-monohedral-filter-review.md),
conditional on the explicitly imported complete monohedral classification
below. Date2026-10-10.

## Statement and conventions

Let P be a genuine convex pentagon whose interior angles, in cyclic order at
vertices0,...,4, are one of

    U=(1,3,4,4,3), V=(2,2,4,3,4), W=(3,3,3,3,3),

in units pi/5. Let l_i>0 be the length of the side from vertex i to i+1.
All isometries, including reflections, and unrestricted contacts are allowed.

Under Rao's complete classification of convex monohedral pentagons:

1. No positive closed U pentagon tiles the plane alone.
2. No positive closed W pentagon tiles the plane alone.
3. A positive closed V pentagon tiles the plane alone if and only if
   l_1=l_3 or l_2=l_4. In these cases it has a periodic monohedral tiling.

The first and third conclusions concern **all real positive side lengths**,
not merely a finite golden-power alphabet. This lemma does not prove mixed
tilability, mixed aperiodicity, or any exclusion of an arbitrary two-shape pair.

## External dependency

Michaël Rao, *Exhaustive search of convex pentagons which tile the plane*,
[arXiv1708.00274v1](https://arxiv.org/pdf/1708.00274), Section4 and Table2,
is used as an external theorem: every genuine convex pentagon admitting a
monohedral plane tiling belongs, after a cyclic or reflected relabeling, to
one of the fifteen known families. Those families admit periodic tilings.

The paper permits translations, rotations and mirrors on page1 and defines
full and half native vertices on page2. It does not restrict contacts to
whole edges. Types16–19 in its computational table are subsets of the fifteen;
types20–24 have no genuine positive closed realization. This artifact does
not independently replay Rao's371-case classification. Its local application
to the three fixed words is reproduced exactly here.

## Exact closure and finite family test

Set K=Q(sqrt5) with its positive real embedding and phi=(1+sqrt5)/2.
Place side0 along the positive horizontal axis. If the angle word is m, the
successive side directions in pi/5 units are d_0=0 and

    d_j=d_(j-1)+5-m_j (mod10), j=1,...,4.

Vector closure is equivalent to two K-linear equations in l:

    sum l_j C_(d_j)=0, sum l_j S_(d_j)=0,

where C_k=cos(k*pi/5) and S_k=sin(k*pi/5)/sin(pi/5). Their ten exact values
are written in the producer, with no floating-point decisions. Dividing the
vertical equation by sin(pi/5)>0 does not change its solutions.

For each of the fifteen families, test every relabeling of its vertex angles.
For sign epsilon=+1 or-1 and offset h=0,...,4, the new vertex index i refers
to old index h+epsilon*i. Its outgoing side refers to old index h+i when
epsilon=+1, and h-i-1 when epsilon=-1. The latter shift is essential:
the reflected outgoing side is the old **incoming** side. Apply these side
maps to the homogeneous length equalities in Rao Table2.

There are exactly3*15*10=450 angle tests. The compatible counts are:

| Word | Compatible families and number of relabelings |
|---|---|
| U | Type2:4; Type8:2 |
| V | Type2:4; Type6:2; Type8:2; Type9:2 |
| W | none |

For each of these16 cases, impose its side equalities and the two closure
equations. Normalize sum l_i=1 and introduce delta satisfying delta>=0 and
l_i>=delta for every i. The resulting ordered-field polyhedron is compact:
all l_i lie in[0,1] and delta lies in[0,1/5]. If nonempty, its vertices are
computed exactly over K. A strictly positive real solution exists precisely
when its maximum vertex delta is positive. This applies to real lengths
outside K as well: a nonempty compact polyhedron with coefficients in K has
vertices in K, and a linear objective attains a maximum at a vertex.

The retained exhaustive result is:

* All six U compatible cases have an empty normalized nonnegative closure
  polyhedron.
* Of the four V Type2 cases, the gates l_0=l_3 and l_0=l_2 have maximum
  delta0. The gates l_1=l_3 and l_2=l_4 have positive maximum delta.
* The six other V cases have an empty normalized nonnegative closure
  polyhedron.

An exact positive normalized witness for both surviving V gates is

    l_0=(-5+4sqrt5)/11,
    l_1=l_2=l_3=l_4=(4-sqrt5)/11.

The full certificate records every compatible angle test, actual side map,
transformed length equations and exact optimum as a pair of rational
coefficients in the basis(1,sqrt5). It omits no positive metric branch.
Thus every U is excluded by the imported necessary family list. For V,
the two surviving gates are exactly relabeled Type2 conditions and hence
are sufficient as well as necessary. The known Type2 periodic tiling gives
the asserted monohedral escape.

For W one can dispense with the external theorem: every genuine corner
has angle3pi/5, so a full native vertex would require3k=10 and a half vertex
would require3k=5 for an integer k>0. Neither is possible. Every plane tiling
has a native tile corner, at which one of these two cases must occur.

## Reproducibility and scope

Producer:
`research/searches/pentagrid_monohedral_family_filter.py`.
Certificate:
`research/certificates/pentagrid-monohedral-family-filter.json`.
Replay:

```text
conda run --no-capture-output -n arisearch python research/searches/pentagrid_monohedral_family_filter.py
```

This deterministic finite test uses SageMath exact ordered-field polyhedra;
there is no seed, numerical threshold or bounded patch inference. The
[independent checker](../reviews/verify_pentagrid_monohedral_filter.py) uses
exact rowspace certificates instead: twelve strictly positive linear
relations exclude even nonzero nonnegative closure, two semipositive
relations force zero native sides, and analytic bounds recover the two
positive optima. It imports neither the producer nor its polyhedron backend.
The fresh review also checked the original source and actual convex witnesses.
The adjacent-supplementary reduction
to these three words is a separate lemma with a separate review.

The golden metric search elsewhere puts angle_i **after** side_i. Under that
convention the same fixed displayed V word has monohedral gates
L_2=L_4 or L_3=L_0. Do not apply the vertex-convention indices directly to
those metric certificates.
