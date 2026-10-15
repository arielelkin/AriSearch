# One exact nonempty precursor in the identical-donor branch

Status: retained author-level precursor PASS; common-H gate FAIL. This
fixture record remains unreviewed evidence and is not a theorem dependency.
The full construction branch is CLOSED by the later independently reviewed
[arbitrary-context-cut theorem](../lemmas/context-dependent-receiving-hexagon-obstruction-2026-10-15.md)
and stronger [arbitrary-split theorem](../lemmas/context-dependent-split-receiving-hexagon-obstruction-2026-10-15.md).
This verifies precursor geometry only. It supplies neither receiving-H
congruence nor cap/P congruence, nor any two-prototile tiling.

The closed mark-local-tail-cut construction is not reopened. The historical
next construction gate permitted the external tail truncations to depend on
thin/thick context; that entire extension is now excluded by the reviewed theorems above. This fixture has no truncation cuts at all: it checks
that the necessary common-donor geometric branch is nonempty BEFORE solving
for a common truncated H.

## Exact fixture and source domain

Set c=cos36=(1+sqrt5)/4, s=sin36=sqrt(10-2sqrt5)/4, r=1/100 and

    u=(s+r*c)/(s*(1-r*r)+2*r*c), h=r*u, m=u-h/10.

Both marks X and Y use this SAME donor triangle and split. All square roots
are positive. These formulas are exact finite algebraic definitions.
The tail base angle beta has tan(beta)=r, and the head base angle is
beta+36, verified algebraically by

    h/(1-u)=(r+s/c)/(1-r*s/c).

Use vertices V0=(0,0), V1=(1,0), V2=(1+C,S), V3=(C,S), where (C,S)=(c,s)
for thin and (2c²-1,2sc) for thick. Their arrow assignments are

    thin:  (0,1,X), (2,1,X), (2,3,Y), (0,3,Y);
    thick: (0,1,X), (1,2,Y), (3,2,Y), (0,3,X).

For each of two donor parities, the donor edges are parity and parity+2.
On a donor edge e with arrow T->H, let a=V_H-V_T and evec=V_(e+1)-V_e;
the internal donor apex is V_T+u*a+h*left_normal(evec). The remaining two
edges receive. Each source splits into its two donor triangles and its two
native receiving sectors (V_e,V_(e+1),p_(e+1),p_(e-1)). This gives FOUR source
configurations and eight receiving sectors in total.

On a receiver, take external apex t=V_T+u*a-h*left_normal(evec), split
M=V_T+m*a, p=p_(e-1), q=p_(e+1). The two receiving quads are

    (V_e,t,M,p), (V_(e+1),t,M,q),

and the remaining central triangle is C=(M,q,p).

## Exact successful checks

The [producer](context-dependent-identical-donor-precursor-2026-10-15.py)
is adapted from the retained strict-M coordinate gate, with the parameters
changed to the single requested identical-donor fixture. It uses Sage AA
exact real-algebraic arithmetic for every geometric sign and identity.
The [certificate](../certificates/context-dependent-identical-donor-precursor-2026-10-15.json)
retains all four source configurations, eight receivers and sixteen native
endpoint records.

All checks PASS:

* 0<m<u<1 and h>0, with every donor apex strictly inside its source rhomb;
* all four cells of each source partition are strictly convex;
* their interiors are pairwise disjoint by exact separating-axis tests;
* all cell vertices lie in the source and their areas sum to its exact area;
* all sixteen receiving quads are strictly convex by every edge/other-vertex
  half-plane determinant, not just a selected corner inequality;
* all eight central triangles C are strictly convex;
* for each receiver, its two quads and C have pairwise disjoint interiors
  and total area equal to the original sector plus the external donor;
* each receiving quad splits across its retained-endpoint/M diagonal into
  a triangle contained in the external donor and a triangle contained in
  the original sector, while C lies in the sector. Together with the area
  identity and disjointness, this proves exact coverage.

The source and receiving partitions are checked for BOTH parities, all
receiver edges and both endpoints. No omitted symmetry cases are inferred.
The donor half-angles obey 72<theta_tail<90 and 54<theta_head<90, using
strict exact cotangent inequalities. The necessary bound m<u-h²/u also
holds exactly. Interval arithmetic is used only to display the useful
approximate values

    beta ~ 0.5729386977 degrees,
    theta_tail ~ 83.7164681648 degrees,
    theta_head ~ 59.1376544398 degrees.

In particular the old mark-local common-pair requirement theta_tail>=108
fails for this fixture, as expected. Its successful precursor geometry
therefore cannot by itself rescue context-INDEPENDENT external cuts.

Replay:

```
mise exec -- conda run --no-capture-output -n arisearch python research/searches/context-dependent-identical-donor-precursor-2026-10-15.py --output research/certificates/context-dependent-identical-donor-precursor-2026-10-15.json
```

## Independent mirror-branch algebra check

Root separately derived that the exceptional beta=18 reflection branch
requires incompatible split bounds. The independent [algebra verifier](../reviews/context-dependent-mirror-branch-algebra-2026-10-15.py)
imports no producer and confirms the direct-coordinate upper bound and
factorization in Q(c)(v), where 4c²-2c-1=0 and c=cos36.

Writing v=uY, k=tan18, the thin tail determinant is
k*[m(c+v)-2cv], hence m>L=2cv/(c+v). The thick Y-head determinant yields

    m<U=1-((1-v)^2+k²*v²)/(1-v+k*v*cot54).

The verifier reconstructs that bound from p=(1-a,b), with

    a=(1-v)*(2c²-1)+2c*(1-c)*v,
    b=k*[(1-v)*2c*(1+c)-v*(2c²-1)].

It then checks exactly

    L-U = v*[2c*v²-(c+3/2)*v+(1+c)/2]
            /[(c+v)*(1+c)*(c+(1-2c)*v)].

All denominator factors are positive for 0<v<1; the last ranges between
c and 1-c. The numerator quadratic has positive leading coefficient and
discriminant 3/2-(5/2)c<0. Thus L>U, excluding the mirror branch. This
independent algebra check supports the root's separate whole geometric
reduction; it is not a substitute for hostile review of that reduction.

## Follow-up: retained-angle failure and a counterpoint to overclaiming

The original m=u-h/10 point fails the next common-H capacity gate exactly.
In a thick cross-tail receiver put U=(0,0), t=(u,-h), M=(m,0), and

    p=(-(1-u)*cos72+h*sin72,(1-u)*sin72+h*cos72).

The exact cotangent of its retained M angle lies strictly between
-cos72/sin72 and zero. Thus 90<Mangle<108 (approximately96.62784286).
The common-H endpoint-capacity theorem permits only36,72,144 or angles
strictly above108, so THIS POINT cannot admit a common H under any cuts.
The producer and certificate now retain this failure separately from the
successful precursor checks.

A universal claim Mangle<108 from precursor convexity alone would be false.
At the same exact beta, take the analytically chosen interior split

    m=u*((1+r²)/(1+r*tan18)+1/1000000).

The boundary term is the exact thin-tail strict-convexity threshold. The
[boundary counterpoint producer](context-dependent-boundary-counterpoint-2026-10-15.py)
and [certificate](../certificates/context-dependent-boundary-counterpoint-2026-10-15.json)
check every one of the SAME sixteen quads, four source partitions, eight
central triangles and eight receiving partitions, all successfully. Here
cross-tail Mangle>108 exactly (approximately108.34107273). This is an
explicit counterexample to that proposed universal ANGLE bound, not a
construction candidate and not the result of a random or parameter scan.

Root then supplied a stronger metric obstruction independent of all cut
fractions. The unique36 vertex compares thin X/Y-tail receiving hexagons:
its opposite native M gives mX=mY. The unique72 vertex compares thick
X-tail and thick Y-head hexagons: its opposite M gives mX=1-mY. Hence a
common H requires m=1/2. Both preserved precursor points instead satisfy
m>1/2 exactly; their certificates now state this common-H failure.

The root's full component proof uses the independently checked mirror
exclusion above and, in the identical-donor branch, strict thin-tail
convexity m>mL with

    mL=sin(beta+36)*cos18/[sin(2beta+36)*cos(beta-18)]
       >= sin36*cos18 = sqrt5/4 > 1/2.

The denominator is positive and at most1 for0<beta<36, and sin(beta+36)
is at leastsin36. Thus context-dependent truncation cuts also cannot make
one H under the stated mark-local donor/split geometry. This adviser
independently checked the opposite-vertex correspondences and trigonometric
formula, and informed root; root owns extraction and fresh whole-proof
review. The weaker precursor checks remain useful controls for that proof.

## Remaining construction boundary

The root's stronger component proof has passed independent review, and the
later theorem also excludes arbitrary physical split contexts. Any new
construction must change donor geometry by context, retained-vertex or
source incidence, or the single receiving-H requirement. Changing only the cut
fractions cannot overcome the new diagonal obstruction. These precursor
fixtures establish local geometric nonemptiness only, not common H. No randomized
scan, generic-rank exclusion, cap search or metric congruence search was
performed in this gate.
