# Staggered Fibonacci ordinary Voronoi rule: exact periodic escape

Status: **Falsified as an aperiodic-pair construction.** This fixed rule stops at its source symmetry. No finite patch census or parameter tuning was performed. Internally checked; independent review remains with the root agent.

## Exact full-plane source

Let phi=(1+sqrt(5))/2 and alpha=1/phi². For every integer n set
s_n=floor((n+1)alpha)-floor(n alpha), and g_n=phi if s_n=0, otherwise g_n=1. Set x_0=0 and x_(n+1)-x_n=g_n for all integers n. These are two-sided Fibonacci (mechanical) spacings, with irrational long/short ratio. The explicit site set is

    D = {(x_n + (m mod 2)/2, 2m): n,m in Z}.

This defines the entire plane source directly. Distinct sites in one row are at distance at least 1, and distinct rows at distance at least 2. Every plane point is within sqrt(1+phi²/4) of a site, by choosing a nearest row and then a nearest site in it. Thus D is Delone. Its ordinary closed Voronoi cells cover the plane and have disjoint interiors: the distance minimum is attained by local finiteness and relative density. The Fibonacci word has irrational symbol frequency alpha, hence is not periodic as a word; that fact does not remove the source's vertical period.

## Decisive exact obstruction

D+(0,4)=D. For every site p and its ordinary Voronoi cell V_p,

    V_(p+(0,4)) = V_p+(0,4),

because translating every distance inequality |z-p|<=|z-q| by the same vector preserves it and permutes D. Therefore the complete Voronoi tiling admits the nonzero translation (0,4).

This obstruction applies for every positive common row height h and every horizontal offset pattern periodic in the row index with period k: identical horizontal site chains give source period (0,kh), and their ordinary Voronoi cells inherit it. It applies even if the cell inventory were exactly two qualifying shapes. Selecting an aperiodic horizontal chain cannot cure this inherited translation.

## Symbolic calculation already completed before the stop

For clarity, this particular choice also fails the two-class gate. At an even-row site translated to the origin, let a,b in {1,phi} be its preceding and following gaps. Its vertical sides are x=-a/2 and x=b/2. Its upper boundary is

    y = min(1+((1/2-a)²-2(1/2-a)x)/4,
            1+(1/4-x)/4),

and its lower boundary is the reflection in y=0. The upper kink is x=1/2-a/2, strictly between the vertical sides. Hence these cells are strictly convex hexagons.

Only these two adjacent-row sites contribute: consecutive horizontal bisector positions in either adjacent row are their coordinate midpoints; the predecessor midpoint lies left of -a/2 because a+c>=2>1, while the successor midpoint is 1/2+b/2>b/2. The same-row nearest sites give the vertical sides. The displayed cell lies inside |x|<=phi/2, |y|<3/2 and has distance less than 2 from the origin (phi²/4+9/4<4). Every site at least two rows away has vertical distance greater than 5/2 from its points, so cannot cut it. This proves completeness without patch enumeration.

Odd-row cells are reflections of even-row cells with a,b exchanged. The mechanical word has exactly the adjacent gap pairs (phi,phi),(phi,1),(1,phi): consecutive short gaps are impossible since 2alpha<1, and each of the other pairs occurs on a nonempty interval of the irrational circle rotation. Each context occurs on every row. Integrating twice the upper boundary gives

    area(a,b) = (a²+15a-b²+17b)/16.

The three resulting areas are respectively 1+sqrt(5), 25/16+sqrt(5)/2, and 23/16+sqrt(5)/2. They are distinct; parity introduces only their reflected copies. Thus the full inventory is exactly three reflection-inclusive congruence classes of strictly convex hexagons. This confirms a second independent failure, but the source period alone already ends this rule.

## Scope and restart condition

No claim about general Fibonacci row couplings, other Delone sources, or impossibility of the original two-polygon problem follows. A materially different source would need genuinely nonperiodic coupling in the row direction and a new exact local-inventory mechanism. Its existence would still not prove shape-only aperiodicity: all tilings of the resulting shapes, including monohedral omissions and unintended assemblies, would remain to be controlled. No such changed rule is proposed here.
