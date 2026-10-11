# Geometry audit of the density-wave dodecagon/pentagon lead

**Status:** exact candidate reconstruction checked; its identification with
the published raster remains conditional. The reconstruction has a periodic
two-convex-shape escape. A depicted interior fragment has a reflex corner,
which blocks regrouping complementary cells while retaining the pentagons.
No global reconstruction of the author's generator, novelty claim, or
shape-only forcing result is asserted.

## Primary source and scope

This extends the [narrow source audit](regular-dodecagon-pentagon-source-audit.md).
Primary evidence is Roshal, Konevtsova, and Rochal,
[arXiv:2510.18734v2](https://arxiv.org/pdf/2510.18734v2), Sec.III.A and
Fig.2(b), PDF pages5–6; [journal record](https://doi.org/10.1103/xvv5-t3sn).
The downloaded PDF SHA256 is
`c07f2dfa267cfb7f85064d4f0add374fa9992c46ab8762563cedb289cd6aa153`.

The source selects auxiliary AP3 vertices by a density-wave mismatch
threshold above0.52, then removes close competitors. Its half-integer phase
case uses narrow rhombs, squares, and regular hexagons as auxiliary cells.
The pentagon has two edge lengths. The Fig.2(b) caption explicitly includes
dodecagon fragments. The periodic approximant in Fig.3 changes wave vectors.
These are source statements, not assertions about all unmarked tilings.

The retained PDF's Fig.2 is an embedded1430-by520 pixel RGB image on PDF
page5, object39. The inspected paper gives no indexed pentagon/fragment
coordinate atlas or all-fragment regrouping rule. The arXiv source and
e-print endpoints returned that same PDF, not a vector/source archive.
Consequently a pixel measurement is not used as an exact metric proof.
The following integer-direction walks are our mathematical reconstruction
of the visible AP3 walks. This identification gate remains explicit.

## Exact pentagon reconstructed from the AP3 star

Normalize an auxiliary AP3 edge to1 and put

    a_j=exp(i*j*pi/6), j=0,...,11,
    h=sqrt(3), S=sqrt(2+h), L=1+h=sqrt(2)*S.

Group the twelve consecutive star directions into blocks2,3,2,3,2:

    E0=a0+a1,
    E1=a2+a3+a4,
    E2=a5+a6,
    E3=a7+a8+a9,
    E4=a10+a11.

Their sum is zero. Their respective directions are15,90,165,240,315 degrees,
with lengths(S,L,S,L,S). The positive exterior turns are75,75,75,75,60
degrees. Thus the exact pentagon is strictly convex with native angle word
(120,105,105,105,105). In Q(sqrt(3)) coordinates it is

    P0=(0,0),
    P1=(1+h/2,1/2),
    P2=(1+h/2,3/2+h),
    P3=(0,2+h),
    P4=(-(1+h)/2,(1+h)/2).

It is also the pentagon obtained by selecting vertices of a regular AP3
unit-side dodecagon with successive cyclic gaps2,3,2,3,2. This is a finite
exact definition independent of the density-wave generator.

The native image's pentagon near bounding box(598,77,638,124), and the gray
auxiliary walks surrounding it, motivate these block choices. This locator
is evidence for the inference, not a source-provided list of lattice indices.

For comparison with the reviewed
[n12 classification and periodic family](../lemmas/all-obtuse-pentagon-regular-dodecagon-classification.md),
normalize a regular dodecagon side to the long length L. Then

    p=0, ell=t=S/L=1/sqrt(2),
    sqrt(3)*ell-2sin(15 degrees)=ell.

The family inequality ell>2sin(15 degrees)/sqrt(3) holds. Hence this exact
P paired with the regular Q12 of side L has a proved periodic plane tiling.
If the source's pentagon is this reconstructed P, this periodic escape
applies to its unmarked geometry. The density-wave example can still be
quasicrystalline; that does not restrict the other admitted tilings.

## Interior fragment: exact conditional reconstruction

The native Fig.2(b) includes a closed fragment wholly inside its frame near
bounding box(716,110,776,201). It therefore cannot be explained solely by
clipping complete dodecagons at the displayed window boundary.

Reading its successive directed edges in the same star frame gives

    (length, direction degrees)=
    (S,315),(L,30),(S,105),(S,45),
    (L,120),(S,195),(L,240),(L,270).

This is an exact closed walk. Its vertices are

    F0=(0,0),
    F1=((1+h)/2,-(1+h)/2),
    F2=(h+2,0),
    F3=(h+3/2,1+h/2),
    F4=(2+3h/2,3/2+h),
    F5=(h+3/2,3+3h/2),
    F6=((1+h)/2,5/2+3h/2),
    F7=(0,1+h).

Nonadjacent edges do not cross. Its native angles are

    (135,105,105,240,105,105,135,150) degrees.

In particular it is a concave octagon, with its single240-degree corner
at F3. Exact shoelace gives

    area(F)=21/2+6sqrt(3)=area(Q12 of side L)/4.

The quarter-area identity does not prove that four copies regroup into a
dodecagon. In the inferred source adjacency, the120-degree sector missing
at F3 is occupied by the beta corner of a P tile.

Here there is a precise local obstruction to the proposed regrouping. Any
convex union containing the whole fragment F contains the convex hull of
F. At its reflex corner, that hull meets the interior of the adjacent P:
take points on the two incident F rays sufficiently close to F3; their
joining chord crosses the complementary120-degree wedge. Therefore no
union of whole complementary cells, leaving all source P tiles intact,
can turn this fragment into a convex tile. This argument does not depend
on the area ratio, remote adjacencies, or the number of other fragments.
Regrouping that also changes or cuts P tiles is a different mechanism and
requires a new complete partition rule.

The fragment's metric word and source adjacency are conditional on the
visible star-walk reconstruction. An author-provided indexed atlas would
be needed to promote them to a certified statement about the entire
source generator. No claim that every source fragment is congruent to F,
or that there are exactly three source congruence classes, follows here.

## Exact replay and resolved restart boundary

The [exact checker](../searches/regular_dodecagon_source_reconstruction.py)
uses CyclotomicField(24), with q=exp(i*pi/12), to verify closure, signed
native turns, all strict P support inequalities, the fragment's signed
turns and noncrossing edges, both exact areas, and the n12 metric identity.
The [retained certificate](../certificates/regular-dodecagon-source-reconstruction.json)
records `PASS_exact_candidate_only`; normal invocation writes nothing.

    conda run --no-capture-output -n arisearch python research/searches/regular_dodecagon_source_reconstruction.py

This source lead does not presently supply the requested two convex
prototiles. The reconstructed two-shape P/Q12 pair admits a period, while
the depicted source decomposition includes a reflex complementary cell.
Its smallest unresolved source question is exact indexed identification,
not a larger random packing search. Its smallest unresolved constructive
question is a different repartition that changes the pentagons and has
exact global coverage and shape-only forcing proofs.
