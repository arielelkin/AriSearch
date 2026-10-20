# Exact first gate for the 60/105/115/125/135 pentagon and 150/120 heptagon

## Scope and declared finite limits

P has cyclic interior angles (60,105,115,125,135); Q has cyclic
(150,150,120,120,120,120,120). Reflections are allowed. This is a local
feasibility and small torus exclusion, not a plane tiling construction.
Before computation the finite domains were fixed: angle multiplicities
with at most six genuine corners, total 180 or 360 degrees; one exact
unit-incircle metric per polygon; one three-tile star motif; and all
11!! = 10,395 pairings of twelve native edges in a one-P/one-Q torus,
with either relative chirality. Runtime cap: 120 seconds per replay.
No larger patch radius is authorized by this result. The absent extension
mechanism is the next mathematical gate.

Replay:

```
mise exec -- conda run --no-capture-output -n arisearch python research/searches/pentagon-heptagon-astra-first-gate-2026-10-19.py
```

The adjacent Python producer writes the coefficient certificate at
`research/certificates/pentagon-heptagon-astra-first-gate-2026-10-19.json`.

## Complete indexed angular atlas, including partial contacts

Write A=60, B=105, C=115, D=125, E=135, F=120, G=150.
The complete 360-degree multisets are

```
FFF, CDF, BEF, BBG, AGG,
AAFF, AACD, AABE, AAAAF, AAAAAA.
```

With one straight (180-degree) host sector the only possibilities are
`AF + flat` and `AAA + flat`. Two flat sectors alone form an interior
point of a seam, not a junction; include this trivial case when counting
all boundary points. Two flats plus genuine corners are impossible.
There are no other possibilities: the minimum corner is 60 degrees,
so exhaustive nonnegative multiplicities of sum at most six suffice.

This is an indexed atlas by the following exact expansion rule: A through
E each have their unique P index 0 through 4; every F occurrence may
independently be any of Q2,...,Q6, and every G occurrence any of Q0,Q1.
The flat host may independently be any native side index of P or Q,
with contact in its relative interior. Every cyclic order and its reversal
is allowed. Corners in one star belong to different tile copies, so equal
indices may recur. This finite schema specifies ALL indexed local stars.
It describes angular feasibility; compatibility of far endpoints and
multiple stars remains additional work. Locally each such indexed star
embeds by assigning its convex tiles consecutive disjoint angular sectors;
the same statement holds with a half-plane host for a flat sector.

In particular the proposed inventory omitted BBG and the higher valence
and flat-host stars. Its four advertised triples alone are incomplete.

## Exact strictly convex metrics

Let z=exp(2*pi*i/72), with Phi_72(z)=z^24-z^12+1=0 and the specified
complex embedding. Let c(k)=(z^k+z^-k)/2 and
s(k)=(z^k-z^-k)/(2*z^18). These are real elements of Q(z).
For P take side directions in degrees (0,75,140,195,240); for Q take
(0,30,90,150,210,270,330). Put n_i=(-sin d_i,cos d_i), and define
vertex v_i by n_(i-1).v_i=n_i.v_i=-1. The certificate stores every
coordinate and native edge length as 24 rational coefficients in Q(z).

These are genuine convex tangential polygons. Successive outward normals
have gaps 180-alpha_i in (0,180), winding exactly once; their support
lines circumscribe the unit disk. Every line is exposed and adjacent
intersections are distinct. The native edge length is exactly

`l_i = tan((180-alpha_i)/2) + tan((180-alpha_(i+1))/2) > 0`.

The formula lies in Q(z), using tan(t/2)=sin(t)/(1+cos(t)). The script
checks every edge vector, this exact length formula, and closure by
polynomial reduction. Strict convexity and sign follow from the displayed
angles, rather than floating point tolerances.

For a specific finite motif translate P0 and two copies of Q0 to the
origin, with outgoing directions 0,60,210 degrees. Their interior sectors
are [0,60], [60,210], [210,360]. Convexity places the whole respective
polygons in these sectors, proving disjoint interiors and exact incidence
at the origin. Coordinates are certified. This generic star has no known
extension mechanism and establishes no plane existence claim.

## Neither species tiles alone, at every metric with these angles

For P alone, every 115-degree corner must occur in the unique native star
(60,60,115,125). There is no straight-host star involving 115. Consequently
every P demands two 60-degree corners, while each P supplies only one.
This is impossible in a plane tiling: count tiles contained in a radius-R
disk and the demanded corner incidences. Only tiles in a fixed-width
boundary annulus can affect the mismatch. Congruent compact polygons with
positive area give O(R) boundary tiles and Theta(R^2) interior tiles.
The resulting inequality 2N <= N+O(R) contradicts N=Theta(R^2).
This direct argument includes partial contacts and reflections and avoids
reliance on the complete convex-pentagon monohedral classification.

Q alone has no flat-host star (all corners exceed 90 degrees) and its only
native star is (120,120,120), which cannot receive either 150 corner.
Thus Q alone is impossible immediately. The average-side argument for
convex monohedral polygons with more than six sides gives another route.

## Complete one-P/one-Q whole-native-edge torus exclusion

An orientable flat torus tiled by one copy of each has 12 native edges
paired into six seams. A P side cannot pair with another P side: the
displayed five directions have no antiparallel pair, for either chirality.
Hence all five P sides must pair with Q sides. All Q directions are
multiples of 30 degrees; after a rotation/reflection they lie in one
residue class modulo 30 degrees. P's first two directions differ by
75 degrees. They cannot both pair with Q under one fixed relative
isometry. Thus no such torus exists, for ANY positive metric having these
cyclic angle words. Translation periods cannot repair direction mismatch.

The script independently enumerates all 10,395 labeled pairings and both
relative chiralities and retains zero direction-compatible pairings.
This is an upper-domain exclusion: no Euler or vertex-angle filter is
needed because direction consistency already excludes every pairing.
It excludes only a one-P/one-Q torus with whole native sides. It says
nothing about larger fundamental domains or subdivisions of sides.

## Global frequency constraints, with the correct zero-density scope

For densities in large disks (or any convergent subsequence of normalized
counts), denote tile densities p,q. In the order of the ten native stars
listed above write densities a,b,c,d,e,f,g,h,i,j, and write k,l for
the flat-host stars AF and AAA. Count each star once, independently of
which tile supplies its flat host. Corner conservation gives

```
b+g=p                         (115 and 125)
c+h=p                         (135)
c+2d+h=p                      (105)
2e+d=2q                       (150)
e+2f+2g+2h+4i+6j+k+3l=p       (60)
3a+b+c+2f+i+k=5q              (120).
```

Consequently d=0 and e=q, and

```
p-q = 2f+2g+2h+4i+6j+k+3l >= 0,
5q = 3a+2p-g-h+2f+i+k.
```

Since g+h <= (p-q)/2, the latter identity also implies p<=3q.
Thus q<=p<=3q is necessary; p=q is NOT forced. If p=q, all
f,g,h,i,j,k,l vanish, and the equations force a=b=c=e=q, exactly
the advertised four-star inventory in density. Nonnegative feasible
frequency vectors with p>q exist: p=2,q=1,b=c=7/4,g=h=1/4,
e=1,a=1/2,d=f=i=j=k=l=0 satisfies every equation. This is a formal
frequency witness only, not a geometric realization.

In an arbitrary nonperiodic tiling d=0 means BBG stars have zero areal
density, not that none occur. In a periodic tiling a zero-density star
cannot occur, so its absence does follow there. Boundary errors are O(R),
since there are finitely many polygon types of positive area and bounded
diameter. These equations include partial contacts and do not rely on
native edge-to-edge incidence.

## Remaining gap

The exact metric pair passes strict convexity and local angular embedding,
and both monohedral omissions are excluded. The smallest balanced native
torus fails. There is still no certified mixed infinite tiling, no finite
incidence template known to extend to one, and no unrestricted mixed
non-tilability invariant. Pair existence, periodic escape at larger domain,
and aperiodicity are all unresolved. Advancing this branch requires a
changed explicit incidence/extension mechanism before further patch search.
