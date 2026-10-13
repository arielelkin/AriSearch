# Generic ternary A001212: native reduction, exact AAA-hole exclusion, and periodic escape

Date: 2026-10-13. Status: internally proved; separate native checker PASS;
independent hostile review VALID. Restricted family theorem only.

## Theorem and dependencies

Let actual strictly convex A,B have two copies of angles x,y,z and of
r=360-2x,s=360-2y,t=360-2z, with x+y+z=360 and90<x,y,z<180. Assume six distinct
angle values and exactly the five trivalent stars AAA=(x,y,z), BBB=(r,s,t),
and same-colour AAB=(x,x,r),(y,y,s),(z,z,t). A has native word001212.
B has arbitrary native order; both actual metrics are arbitrary, including
all side equalities. Whenever the pair tiles, it admits a periodic tiling,
with reflections, original partial contacts and omission permitted.

Use the reviewed defect-free limit, monohedral periodic escape, no-ABB
propagation, exact honeycomb slots, full-A quotient/native metric lifting, and
Reinhardt H1/H2 sufficient families, as named in
[the A001122 all-metric theorem](terra-001122-all-metric-periodic-escape.md).
The outer-AAB-to-one-B-coset proof is also written there and applies unchanged
once its actual-field hypothesis has been verified below.

## Complete necessary native domain before geometry

In a genuinely mixed defect-free field every B vertex is same-colour AAB.
A001212 native endpoint pairs are00,01,12,12,12,02, so B cannot have11 or22
edges. Exactly five of the11 native bracelets remain:

    001212,010212,012012,012021,012102.

For any indexed B placement, each AB neighbour must match its two B endpoint
colours in spatial order. A has two orientation choices at a00 edge, three
native side choices at a12 edge, and one at either01 or02. Thus B001212 has
54 possible A tuples per placement,648 across12 placements. Each of the other
four has9 per placement,108 across12. All1080 raw tuples are retained.

Each raw ring fixes its six native B side lengths as particular native A side
lengths through its AB seams. This assignment is performed before aliases;
when lengths merge the same native alternatives remain rather than being
silently deleted. Project every tuple through all203 partitions of six A side
lengths, giving219240 exact cases. Check six AA seam equalities and every native
AAA/AAB completion of each outer endpoint, allowing both arm orientations.
For every complete case test H1/H2 sufficient omission escapes for A and B
under all12 dihedral relabellings, using their rainbow360 angle identities.

The exact exhaustive reduction gives7896 AA-compatible and2736 outer-complete
projections. After sufficient omissions,324 ring projections in24 distinct
joint A/B metric cases remain. All further metric specializations are included.
There are two kinds:

*23 cases with B012021,12 rings each; every outer endpoint is AAB;
*one case with B001212 and A side partition(0,0,1,1,1,0), B side partition
 (0,0,1,1,1,0),48 rings; every ring has exactly two outer AAA endpoints.

These are necessary finite native survivors, not jointly realized polygons or
infinite tilings. In particular the single AAA case must pass actual closure.

## The sole AAA-hole metric case cannot close at generic angles

Put u=180-x, v=180-y, w=180-z, so0<u,v,w<90 and u+v+w=180. Write
U=exp(iu), V=exp(iv), W=exp(iw), with degree arguments andUVW=-1.
The unit edge vectors of A001212, after rotating its first edge to1, are

    (1,U,UV,-1,-V,U^-1).

In the surviving AAA case its side lengths are(a,a,b,b,b,a), with a,b>0.
Exact polygon closure is

    a(1+U+U^-1)+b(V(U-1)-1)=0.

The first term is real, so positivity b>0 gives Im[V(U-1)]=0. But

    U-1=2i sin(u/2) exp(iu/2),
    Im[V(U-1)]=2 sin(u/2) cos(u/2+v).

The sine is strictly positive; u/2+v lies strictly between0 and135 degrees.
Its cosine vanishes only at90 degrees. Thus u+2v=180, which together with
u+v+w=180 implies w=v, equivalently z=y. This contradicts the six-distinct
angle hypothesis (and the generic five-star stratum). Therefore this entire
positive-length fibre has NO actual closed A polygon under the theorem,
before any B closure or spatial extension is considered.

## All twenty-three actual residual fibres have periodic escapes

Now any actual non-omission mixed field belongs to one of the23 B012021 cases.
For its fixed actual A partition and fixed actual B metric, all12 eligible
native rings have only same-colour outer AA endpoints. These force B at every
z+Delta_k around every B centre z. The reviewed honeycomb displacements
Delta0=(1,1),Delta1=(-1,2), their negatives and differences generate the index3
cosetL. Induction fills it with B; every other cell is an A neighbour of that
coset, and each trivalent vertex has exactly one B. No distant AAA region is
assumed away: it is excluded by this propagation.

Each of these23 actual metric fibres has six distinct FULL A-neighbour tuples,
with12 raw native rings. Every directional overlap on those tuples is
functional and total. Exact finite maps are commuting involutions, opposite
maps agree, and T2=T1*T0^-1. In particular every quotient field has a period
2Delta0. The reviewed full-A-tuple lift chooses one available native central
B representative per tuple and preserves all actual side/angle constraints;
overlap is independent of that omitted B label. The reviewed metric development
gives a nonzero actual translation, squaring a glide if necessary.

An actual field, rather than local survival, supplies existence for this step.
The canonical lift establishes a periodic admitted replacement, not universal
periodicity of the source field or an unsupported extension of every formal
partition. Pure limits already give monohedral periodic escapes. These cases,
plus the sufficient H1/H2 omissions and the exact impossible AAA fibre,
exhaust every admitted original tiling and prove the theorem.

## Exact evidence and replay

[Producer](../searches/terra-001212-all-metric-native-rings.py),
[complete native certificate](../certificates/terra-001212-all-metric-native-rings.json),
[23 residual actions](../certificates/terra-001212-residual-functional-actions.json),
[separate no-import checker](../reviews/verify_terra_001212_all_metric_rings.py).

    mise exec -- conda run --no-capture-output -n arisearch python research/reviews/verify_terra_001212_all_metric_rings.py

Output PASS:203 partitions,1080 rings,219240 projections,23 six-state AAB
functional fibres, and one48-ring AAA fibre requiring the separate analytic
closure exclusion above. The checker independently reconstructs native
placements, AB tuples, B-side assignments, all AA/outer constraints, omission
labels, all joint metric fibres and six overlap relations. Standard-library
integer equality operations only; no solver, randomness, timeout, torus bound
or numerical geometric acceptance. The trigonometric closure proof is analytic
and needs independent hostile review together with the whole theorem.

No residual case remains inside this exact-star/native domain once reviewed.
Other native representatives and extra-angle-star strata remain unresolved.

Fresh independent review: [VALID](../reviews/terra-001212-all-metric-periodic-escape-fresh-hostile-review.md).
