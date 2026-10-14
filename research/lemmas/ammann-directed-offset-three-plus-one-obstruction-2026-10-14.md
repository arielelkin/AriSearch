# Three-plus-one assignments of the directed-offset Ammann gate

Date: 2026-10-14. Status: **exact computer-assisted proof, independently hostile-reviewed VALID**; see the [fresh review](../reviews/ammann-directed-offset-residual-hostile-review-2026-10-14.md). This closes the four residual three-plus-one assignments of this local four-parameter topology. It does not solve the two-convex-polygon aperiodicity problem.

## Statement

Let \(\varphi=(1+\sqrt5)/2\), \(t=\sin36^\circ\), and take the four representative directed-offset pentagons \(T_0,T_1,K_0,K_1\) from [the two-plus-two lemma](ammann-directed-offset-two-plus-two-obstruction-2026-10-14.md), with \(0<a_X,a_Y<1\), \(h_X,h_Y>0\), strictly interior donor nodes, valid disjoint source-sector partitions, and strict convex counterclockwise output pentagons. Then no three of these four pentagons are mutually congruent. Reflections are included in “congruent.” In particular, no three-plus-one partition of the four representatives is realizable.

## Invariants and finite domain

Index \((P_0,P_1,P_2,P_3)=(T_0,T_1,K_0,K_1)\), and write \(a=a_X,b=a_Y,x=h_X/t,y=h_Y/t\). For each pentagon \(P_i=(v_0,\ldots,v_4)\), define

\[
A_i=\operatorname{area}(P_i)/t,\qquad
L_i=\sum_{j=0}^4\lVert v_{j+1}-v_j\rVert^2,\qquad
Q_i=\sum_{j=0}^4\lVert v_{j+1}-v_j\rVert^4.
\]

Indices in the sum are cyclic. All three quantities are invariant under rigid motions and reflections. Thus for singleton \(i\), the other three indices \(j,k,l\) must satisfy exactly six polynomial equalities \(A_j=A_k=A_l\), \(L_j=L_k=L_l\), and \(Q_j=Q_k=Q_l\). This is a necessary system; it has no dihedral-choice assumption and covers all ten vertex correspondences automatically. The polynomial identities can be derived without convexity. Congruence makes the signed-area equalities necessary here because the stipulated outputs are simple, counterclockwise and strictly convex, so their shoelace areas are positive physical areas.

The exact coordinates are reconstructed in the checker from the already stated formulae for \(T_0,T_1,K_0,K_1\). It substitutes \(\varphi=(1+\sqrt5)/2\) and \(t^2=(3-\varphi)/4\), obtaining six polynomials in \(\mathbb Q(\sqrt5)[a,b,x,y]\) for each of the four singleton branches. It also checks the independent area sums \(A_0+A_1=1\) and \(A_2+A_3=\varphi\).

## Exact elimination result

Compute reduced Gröbner bases of those six-polynomial ideals in \(\mathbb Q(\sqrt5)[a,b,x,y]\). The replay script derives every input polynomial from the polygon coordinates, uses exact SymPy algebraic-field coefficients, and asserts the following output:

* Singleton \(T_1\) or \(K_0\): the Gröbner basis is \(\{1\}\). Thus their necessary congruence systems have no solution even over \(\mathbb C\).
* Singleton \(T_0\): the ideal contains \(a-1/2\), \(x-(\sqrt5-1)(y-1/2)\), and
  \[
  P(y)=y^2-\left(\frac32+\frac{3\sqrt5}{10}\right)y+\frac12+\frac{\sqrt5}{10}.
  \]
* Singleton \(K_1\): the ideal contains \(a-1/2\), \(x-(\sqrt5-1)(y-1/2)\), and
  \[
  R(y)=y^2-\left(\frac32+\frac{3\sqrt5}{10}\right)y+1+\frac{2\sqrt5}{5}.
  \]

For singleton \(T_0\), positivity \(x>0\) forces \(y>1/2\). The thin donor on CD lies strictly inside the source rhomb, so \(h_Y<t\), equivalently \(y<1\). But \(P(1/2)=-\sqrt5/20<0\) and \(P(1)=-\sqrt5/5<0\). A convex quadratic lies below the chord joining these two negative endpoint values throughout \((1/2,1)\), so \(P(y)\ne0\) there.

For singleton \(K_1\), the discriminant of \(R\) is \(-(13+7\sqrt5)/10<0\), so it has no real root. This excludes the remaining branches. QED, subject to the exact algebra replay.

## Replay and scope

```text
mise exec -- conda run --no-capture-output -n arisearch python research/searches/ammann-directed-offset-residual-invariants-2026-10-14.py
```

The script completes in under 10 seconds in the locked environment. Its only discrete domain is the four named singleton branches; it performs no parameter grid, NLSAT query, patch growth, or sampling. The exact Gröbner computation is the proof-relevant computer step. The coordinate and role reduction, strict donor containment, and all two-plus-two branches are established separately in the cited gate and two-plus-two lemma. Together those results classify every admissible two-class realization in this particular directed-offset surgery scheme to the midpoint/common-height component. That component exists but admits periodic monohedral omission; thus the scheme cannot produce an aperiodic pair. They say nothing about other convex-polygon constructions or universal shape-only forcing.
