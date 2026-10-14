# Independent hostile review: directed-offset 3+1 residual

Date: 2026-10-14. Verdict: **VALID**, for the four-parameter directed-offset topology and strict source geometry stipulated in the statement. This does not classify other surgery schemes or solve the two-convex-polygon problem.

## Independent reconstruction and branch coverage

I reconstructed the four pentagons directly from the directed edge arrows, without importing the construction or the author's residual checker. For a source rhomb with \(v=(c,s)\), vertices \(A=(0,0), B=(1,0), C=(1+c,s), D=(c,s)\), the AB donor node is \(p=(a_X,h_X)\). The CD donor node is \(q=(c+1-a_Y,s-h_Y)\) for thin and \(q=(c+a_Y,s-h_Y)\) for thick. The external receiving apices are respectively \(B+(1-a_X)v+h_X(s,-c)\), \(a_Yv+h_Y(-s,c)\), \(B+a_Yv+h_Y(s,-c)\), and \(a_Xv+h_X(-s,c)\) for \(T_0,T_1,K_0,K_1\). These reproduce the four cyclic pentagons in the two-plus-two lemma. In particular, the thin CD arrow is \(C\to D\), while the thick CD arrow is \(D\to C\); reversing this distinction would change the gate.

The prior reviewed diagonal reflections identify the other four indexed outputs with these four representatives, even if only one donor role occurs in a particular source. Every 3+1 partition has one of \(T_0,T_1,K_0,K_1\) as its singleton. Unequal source-pair area totals alone do **not** exclude these partitions: the triple contains one same-source pair and one cross-source pentagon. The six equalities used here compare the common area, sum of squared boundary-edge lengths, and sum of fourth powers of boundary-edge lengths for that triple. Under the gate's valid, strictly convex, counterclockwise output hypothesis, shoelace area is positive physical area and is invariant under rotations and reflections. The edge moments are invariant without that hypothesis. No choice of cyclic vertex map is omitted.

## Independent exact check

The [independent checker](ammann-directed-offset-residual-independent-2026-10-14.py) constructs all four coordinate pentagons with \(a=a_X,b=a_Y,x=h_X/t,y=h_Y/t\), and reduces their invariants using only \(\varphi^2=\varphi+1\) and \(4t^2=3-\varphi\). It imports no author code. The area totals reduce to \(A(T_0)+A(T_1)=1\) and \(A(K_0)+A(K_1)=\varphi\), where each area is divided by \(t\). The boundary-edge square sum differences also reproduce the independent two-plus-two lemma identities after the \(h=t(x,y)\) substitution.

Over the exact field \(\mathbb Q(\sqrt5)\), separate Gröbner bases for the six necessary equations in each singleton branch are:

| Singleton | Independent exact result |
|---|---|
| \(T_1\), \(K_0\) | Unit ideal \((1)\); no complex solution. |
| \(T_0\) | Contains \(a-1/2\), \(x-(\sqrt5-1)(y-1/2)\), and \(P(y)=y^2-(3/2+3\sqrt5/10)y+1/2+\sqrt5/10\). |
| \(K_1\) | Contains the same two linear polynomials and \(R(y)=y^2-(3/2+3\sqrt5/10)y+1+2\sqrt5/5\). |

The \(T_0\) branch has \(x>0\Rightarrow y>1/2\). Strict interior of the thin CD donor node gives \(h_Y<t\Rightarrow y<1\). Since \(P(1/2)=-\sqrt5/20\) and \(P(1)=-\sqrt5/5\), convexity of \(P\) makes it negative on the entire interval. The \(K_1\) branch has no real solution because \(\operatorname{disc}(R)=-(13+7\sqrt5)/10<0\). No parameter-dependent denominator was divided out in deriving the necessary equations or ideals; the normalizing divisor \(t\) is positive. Full source-sector sufficiency and periodicity are not used in the elimination. The strict convex, counterclockwise output hypothesis is used to make signed area equality necessary for congruence.

Replay: mise exec -- conda run --no-capture-output -n arisearch timeout 120s python research/reviews/ammann-directed-offset-residual-independent-2026-10-14.py --ideals

The bounded run completed in about eight seconds. This review predeclared at most 40 cross-pair vertex maps and 120 seconds of exact computation; the proof used **zero** vertex maps and no NLSAT call. Exact symmetric invariants avoid every dihedral branch while retaining a necessary test for each. The prior NLSAT UNKNOWN has no bearing on these exact exclusions.

## Brief check of the separate unit-chord filter

I also independently solved its eight chord-preserving linear systems from the same reconstructed coordinates, without importing the filter checker. Six systems are inconsistent. The same-order \(T_0\)–\(K_1\) map has exactly the stated one-parameter family; substituting it into \(E_T\) gives \(\sqrt5-2+2(\sqrt5-1)t h_Y>0\). The same-order \(T_1\)–\(K_0\) map has \(a_X=a_Y=1/2\), \(x=-1/2+\sqrt5/10=-y\), hence \(h_X<0\). This confirms the filter for its declared eight maps. It makes no claim about the 32 other cross-source maps, which are already covered by the full symmetric-invariant proof above.

## Scope checked

The lemma now states the combined result precisely: admissible two-class realizations in this topology are confined to the midpoint/common-height component, which exists and admits periodic monohedral omission. The result excludes an **aperiodic-pair candidate** in this topology, not every two-class realization.
