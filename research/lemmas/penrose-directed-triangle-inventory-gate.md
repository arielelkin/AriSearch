# Directed Penrose triangle exchange: exact inventory gate

Date: 2026-10-19. Status: necessary inventory theorem and matrix solution,
[independently Sol-reviewed](../reviews/penrose-directed-triangle-inventory-sol-review.md);
**no geometric two-class partition, no aperiodic pair**. This branch stops at
the specified matrix-only gate. No cluster-size census was run.

## Actual source, coordinates, and directed substitution

Use `research/searches/penrose-kite-dart-patch.py`, whose source is the
Lang--Hayes 2013 equation (1). Work exactly in Q(w), w=exp(i*pi/5),
phi=w+w^(-1). The ordered references are

    A=(x,y,z)=(1,0,w), O=(0,w/phi,1).

A has angles (72,36,72) degrees and O has (36,108,36) degrees.
These are *ordered* asymmetric atoms: their unmarked supports are isosceles
triangles. The sign +/- means the orientation of the ordered triple, not
an extra geometric triangle class. Proper rotations preserve this sign;
reflection reverses it. The coordinate step is exactly:

    a1: p=x/phi+y/phi^2; children a2(p,z,x), o2(z,p,y)
    o1: children o2(x,y,z)
    a2: children a1(x,y,z)
    o2: p=x/phi^2+z/phi; children a1(y,x,p), o1(z,p,y).

Two steps return to a1/o1. Multiplication by phi restores the initial scale.
In a1's split both child orientations equal the parent orientation. In
o2's split the a1 orientation reverses and o1 preserves it. Therefore, in
atom order (A+,A-,O+,O-), with columns denoting parents,

    S = [1 1 0 1]
        [1 1 1 0]
        [1 0 1 0]
        [0 1 0 1].

Forgetting orientation yields T=[[2,1],[1,1]], but using T alone loses a
necessary directed constraint. The replay script reconstructs S from the
actual child coordinates, checks exact area preservation through the source,
and independently splits all parent/child sides at their endpoints to check
positional directed boundary cancellation for all four parent types. No
floating-point decision enters the checks (real algebraic ordering is exact).

## Complete rank-two inventory restriction

Suppose C is a nonzero nonnegative integer 4-by-2 matrix and M is an integer
2-by-2 matrix such that SC=CM. This describes a substitution with a fixed
ordered-atom inventory for each output class, allowing proper rotations of
an output representative. It does not automatically describe substitutions
that independently reflect output representatives: those need separate
chirality states and a correspondingly larger intertwiner.

Then there is a nonsingular integer 2-by-2 matrix N with nonnegative entries
such that

    C = B N, B = [[1,0],[1,0],[0,1],[0,1]],
    M = N^(-1) T N.

In particular every individual output inventory must have equally many
A+ and A-, and equally many O+ and O-.

Proof. The characteristic polynomial of S is
(x^2-3x+1)(x^2-x+1), with distinct irreducible factors over Q. No rational
one-dimensional invariant subspace exists. Thus rank(C)=2. Its rational
column space is an invariant plane and must be one of the two irreducible
summands: this follows, for example, from the coprime polynomial spectral
projectors. The expanding summand is
U={(a,a,b,b):a,b in Q}; the other is
V={(a,-a,b,-b):a,b in Q}. The latter has no nonzero nonnegative vector, so
the column space must be U. Reading its entries gives N and SC=CM gives the
conjugacy. Conversely every such N for which N^(-1) T N is integral solves
the stated inventory equation; a genuine output substitution additionally
requires this conjugate to be entrywise nonnegative. This is an analytic characterization, not a
bounded inventory search. QED.

Equivalently the chirality imbalance map D sends an inventory to
(A+-A-,O+-O-), and DS=RD with R=[[0,-1],[1,1]]. Its eigenvalues are primitive
sixth roots, and R^3=-I. In particular SC=CM cannot support a nonzero
chirality imbalance in a two-state nonnegative inventory model.

There are solutions: N=I gives C=B, M=T. Also N=T gives
C=[[2,1],[2,1],[1,1],[1,1]], M=T, with six and four atoms in the two columns.
Thus there is no inventory impossibility theorem for all two-class
recompositions. The second example supplies no partition topology.

## Directional boundary and convex-corner gates

For an actual geometric cluster, orient each constituent triangle boundary
counterclockwise. Regard a side [u,v] as an oriented positional segment;
subdivide at every constituent vertex on it. Interior segments must cancel
with their exact opposite [v,u], leaving one simple outer boundary. Recording
only the five unoriented Penrose directions, or only scalar edge lengths,
loses this necessary positional condition. The replay verifies this boundary
identity for the source substitution itself. An inventory C does not specify
locations, rotations, seams, or this boundary chain and therefore cannot
certify the identity for either proposed output class.

If all atoms lie in the common Penrose frame of this source, their angles
are multiples of 36 degrees. A convex cluster's genuine outer corners must
then have angles 36k degrees for k=1,2,3,4. If n_k counts these corners,

    4 n_1 + 3 n_2 + 2 n_3 + n_4 = 10.

At each boundary vertex, the constituent sectors must form one contiguous
sector of weight k<=4; weight 5 is flat and must be suppressed, while weight
>=6 is nonconvex. Interior vertices have total weight 10. These are exact
local constraints in addition to directed seam cancellation. They need not
hold for atom rotations outside the source's common frame; that changed
model requires a new analysis. The area of one A is sin(36)/2, of one O is
sin(36)/(2phi); a balanced column (a,a,b,b) therefore has area
sin(36)*(a+b/phi). This is consistent with area growth phi^2 and gives no
additional exclusion.

The minimal solution C=B has two triangles per output. Any convex connected
union of two triangles with disjoint interiors has at most four genuine
sides: convexity forces the shared positive-length interface to run between
the two union-boundary endpoints, and each endpoint cannot be a strict
corner of both triangles; equivalently summing the two triangle side counts
and deleting the common side yields at most four sides. Point-only contact
has disconnected interior and cannot be a convex polygon. Such an output
admits a periodic monohedral tiling. Thus the minimal inventory cannot
solve the problem, regardless of whether it is realized by rhombs or another
two-triangle assembly. This does not exclude the N=T inventory.

## Tested stronger implication: chirality balance does not force central symmetry

For a CCW boundary let d_j, j=0,...,4, be total length in direction w^j
minus total length in its opposite direction w^(j+5). The exact canonical
atom vectors, with r=1/phi, are

    A+ : (-1, 0, r, 0, -1)
    A- : ( 1,-1, 0, r,  0)
    O+ : (-1, r, 0, 0, -r)
    O- : ( 1,-r, 0, 0,  r).

These are for the specific reference supports above, conjugated when needed
to get the named ordered chirality. The replay computes them from exact
edge vectors, not a drawing. In particular A+ plus A- has imbalance
(0,-1,r,r,-1), which is nonzero. Its geometric realization is the convex
kite with CCW vertices

    (0, conjugate(w), 1, w).

The two triangles meet along [0,1], one has each ordered chirality, and the
same exact nonzero imbalance is the kite boundary. The corners are
(72,72,144,72) degrees in this vertex order. Thus the kite is not centrally
symmetric. Its four sides still give the periodic omission escape already
recorded; this is a counterexample to the suggested boundary inference,
not a new candidate.

Moreover independently rotating either directed atom cyclically permutes
and changes signs of these five directional components without changing its
chirality count. Consequently the four-row inventory cannot determine
boundary imbalance at all: a full boundary certificate needs orientation
states as well as positions. Even the cancellation for the displayed O+
and O- pair is reference-dependent, not a class invariant. One cannot infer
zero imbalance or central symmetry for every output from C=B N, and cannot
apply the whole-parallelogram fusion obstruction on that basis.

## Unmarked decoder audit and stop

Neither exact SC=CM nor exact source boundary cancellation proves that
unmarked output shapes decode to legal directed Penrose atoms. Missing are:

* two explicit convex polygon supports with exact coordinates;
* a globally covering partition of a legal source tiling into those supports;
* the output substitution's actual positional subdivision, not just counts;
* an intrinsic decoder for every tiling by those two unmarked supports;
* exclusion of wrong-arrow assemblies and alternative atomizations;
* reflection consistency (the problem permits reflected output tiles);
* exclusion of partial-side contacts and T-junctions bypassing intended seams;
* exclusion of periodic tilings using either output alone.

The minimal two-triangle solution already fails the last gate. The larger
matrix solution has no proposed supports, so none of these gaps may be
silently promoted to a construction. In particular it is invalid to invoke
Penrose aperiodicity after erasing the ordered atom data. This artifact is a
new directed inventory restriction for the stated source/model, not a
novelty claim about the literature or a general fusion obstruction. It does
not reuse the closed whole-parallelogram fusion route.

Replay:

    mise exec -- conda run --no-capture-output -n arisearch python research/searches/penrose-directed-triangle-inventory.py

Outputs `research/certificates/penrose-directed-triangle-inventory.json`.
The finite exact domain is the four directed reference atoms and their one
full substitution step. There is no geometric candidate search domain.
A useful next step requires a specified positional partition with a boundary
mechanism; increasing a cluster-size bound is not justified by this result.
