# Winding Honeycombs

## Strictly convex rational hexagons that carry aperiodic arithmetic shifts

### Abstract

We give an effective construction that converts a nonempty strongly
aperiodic nearest-neighbor face shift into a finite set of unmarked strictly
convex rational hexagons. Every interior angle of every output hexagon lies
strictly between \(\pi/2\) and \(\pi\). Copies may be translated, rotated, or
reflected, and contacts are unrestricted. Nevertheless, every admitted
tiling is forced to be edge-to-edge, has the standard honeycomb cell
structure, and decodes to the source shift up to one global orthogonal frame.

The construction is instantiated on a finite winding cover of the 13
Kari-Culik Wang tiles. The resulting set \(P_2\) contains 9,912 congruence
classes of rational hexagons, admits a tiling, and every \(P_2\)-tiling is
nonperiodic. More generally, the sets \(P_m\) form a family whose complete
all-orientation hulls are pairwise nonconjugate. The distinguishing invariant
is a relative continuous eigenmodule that follows the intrinsic geometric
frame of a tiling.

The priority claim is deliberately narrow. Robinson announced
variable-cardinality undecidability for convex lattice pentagons or hexagons
in 1971, without giving the construction or proof in that paper. No searched
primary source supplied an effective compiler in which every output is a
strictly convex all-obtuse hexagon and every unrestricted-contact tiling is
classified. The contribution claimed here is that explicit full-hull
construction, its exact certificate, and the winding family, not the first
observation that convex polygons might encode undecidable tiling systems.

## 1. Model and statements

A prototile is an unmarked simple polygon considered up to Euclidean
congruence. A tiling by a finite protoset \(P\) is a covering of
\(\mathbb R^2\) by congruent copies of members of \(P\), with pairwise
disjoint interiors. Reflections are allowed. No edge-to-edge condition,
matching relation, atlas, color, arrow, or one-sided convention is imposed.
The complete tiling hull is denoted \(X(P)\).

The main geometric result is the following.

**Theorem 1, all-obtuse convex compiler.** Let \(S\) be a nonempty
nearest-neighbor \(\mathbb Z^2\) shift of finite type specified by horizontal
and vertical adjacency relations, and view its symbols on honeycomb faces
with the third face-neighbor direction unconstrained. Suppose that every
configuration in \(S\) has no nonzero \(\mathbb Z^2\)-period. An effective
finite construction produces a protoset \(P(S)\) with these properties:

1. Every member of \(P(S)\) is an unmarked strictly convex hexagon with
   rational coordinates and every interior angle in \((\pi/2,\pi)\).
2. \(X(P(S))\) is nonempty.
3. Every tiling in \(X(P(S))\), including tilings using reflected copies and
   arbitrary initial contacts, is edge-to-edge and decodes locally to a
   configuration in \(S\).
4. Every tiling in \(X(P(S))\) has no nonzero translational symmetry.
5. The fixed-frame part of \(X(P(S))\) is locally shape-conjugate to the
   honeycomb suspension of a finite phase extension of \(S\).

The construction is effective whenever its locally legal black and white
vertex-state sets are nonempty. This is automatic for a nonempty source
shift. A total reduction on arbitrary finite inputs returns the empty
protoset when either state set is empty.

The method's scope is exact. Its input is a finite alphabet with two finite
directed nearest-neighbor relations on \(\mathbb Z^2\), embedded in two of
the three face-neighbor directions of the honeycomb. Its output is a
variable-cardinality finite set of rational all-obtuse convex hexagons.
Permitted placements are all Euclidean isometries and the contact model is
unrestricted. The construction is sound and complete for tileability:
\(P(S)\) tiles the plane if and only if \(S\) is nonempty, and every output
tiling decodes. It is a constructive compiler, not a decision procedure for
source nonemptiness, and it gives no fixed bound on the number of output
polygons.

For the explicit family, put
\[
  \theta=\frac{\log 2}{\log 6}.
\]
Section 2 defines a strongly aperiodic Wang shift \(K^{(m)}\) for every
integer \(m\geq 1\), and Section 3 defines
\[
  P_m=P(K^{(m)}).
\]

**Theorem 2, explicit winding family.** For every \(m\geq 1\), \(P_m\) is a
finite unmarked aperiodic protoset in the full shape-only sense above. In the
audited phase-two construction,
\[
  |P_m|=4956m,
\]
so \(|P_2|=9912\). All coordinates become integers after one common scaling.
The tiling action has positive topological entropy. If \(m\ne n\), there is
no topological conjugacy \(X(P_m)\to X(P_n)\) commuting with translations,
even after intertwining translations by one fixed Euclidean isometry.

The concrete protoset promoted in the implementation is \(P_2\). The values
\(m=3\) and \(m=5\) are exposed as replayable members of the same proved
family.

## 2. The arithmetic source

### 2.1 The 13 Kari-Culik tiles

Write a Wang tile as \((S,W,N,E)\). The six division tiles, with row
multiplier \(1/3\), are

| \(S\) | \(W\) | \(N\) | \(E\) |
|---|---|---|---|
| \(1\) | \(0/3\) | \(0\) | \(1/3\) |
| \(1\) | \(1/3\) | \(0\) | \(2/3\) |
| \(1\) | \(2/3\) | \(1\) | \(0/3\) |
| \(2\) | \(0/3\) | \(0\) | \(2/3\) |
| \(2\) | \(1/3\) | \(1\) | \(0/3\) |
| \(2\) | \(2/3\) | \(1\) | \(1/3\) |

The seven doubling tiles, with row multiplier \(2\), are

| \(S\) | \(W\) | \(N\) | \(E\) |
|---|---|---|---|
| \(0\) | \(-1\) | \(0'\) | \(-1\) |
| \(0\) | \(0\) | \(0'\) | \(0\) |
| \(0\) | \(0\) | \(1\) | \(-1\) |
| \(1\) | \(-1\) | \(1\) | \(0\) |
| \(1\) | \(-1\) | \(2\) | \(-1\) |
| \(1\) | \(0\) | \(2\) | \(0\) |
| \(0'\) | \(0\) | \(1\) | \(-1\) |

The colors \(0\) and \(0'\) are distinct. The symbols \(0/3,1/3,2/3\)
are also formal colors, not simplified numerical labels. Let \(K\) be the
nearest-neighbor Wang shift defined by this table.

### 2.2 The winding lift

Let \(c(\tau)=1\) for a division tile and \(c(\tau)=0\) for a doubling tile.
For \(m\geq 1\), replace each tile \(\tau\) by \(m\) symbols
\((\tau,r)\), where \(r\in\mathbb Z/m\mathbb Z\), with edge colors
\[
\begin{aligned}
 S(\tau,r)&=(S_\tau,r),&
 W(\tau,r)&=(W_\tau,r),\\
 E(\tau,r)&=(E_\tau,r),&
 N(\tau,r)&=(N_\tau,r+c(\tau)).
\end{aligned}
\]
Call the resulting Wang shift \(K^{(m)}\).

Horizontal matching makes \(r\) constant along a row. Vertical matching
gives
\[
  r_{j+1}=r_j+c_j\pmod m.
\]
Projection \((\tau,r)\mapsto\tau\) maps \(K^{(m)}\) onto \(K\), and every
configuration in \(K\) has exactly \(m\) lifts. Thus \(K^{(m)}\) is nonempty.
Any period of a lifted configuration would project to a period of a
Kari-Culik configuration. Culik's aperiodicity theorem therefore excludes
every full-rank period. A singly periodic two-dimensional SFT configuration
would induce a nonempty one-dimensional quotient SFT, which contains a
cycle and hence a doubly periodic configuration. Consequently every
\(K^{(m)}\) is strongly aperiodic.

### 2.3 One exact infinite configuration

The following point gives an exact existence witness and drives the finite
patch generator. Start with
\[
  \alpha_0=\sqrt2,\qquad
  \alpha_{j+1}=
  \begin{cases}
    2\alpha_j,&\alpha_j<1,\\
    \alpha_j/3,&\alpha_j\geq1.
  \end{cases}
\]
This recurrence defines the positive rows. For negative rows use its unique
inverse on the invariant interval:
\[
  \alpha_{j-1}=
  \begin{cases}
    3\alpha_j,&\alpha_j<2/3,\\
    \alpha_j/2,&\alpha_j>2/3.
  \end{cases}
\]
The orbit consists of irrational numbers, so equality with \(2/3\) never
occurs. Thus \(\alpha_j\) is defined for every \(j\in\mathbb Z\).
For \(n,j\in\mathbb Z\), put
\[
  A_j(n)=\lfloor n\alpha_j\rfloor.
\]
If \(\lambda_j=\alpha_{j+1}/\alpha_j\), define the four numerical labels in
row \(j\) by
\[
\begin{aligned}
 S_{n,j}&=A_j(n)-A_j(n-1),\\
 N_{n,j}&=A_{j+1}(n)-A_{j+1}(n-1),\\
 W_{n,j}&=\lambda_jA_j(n-1)-A_{j+1}(n-1),\\
 E_{n,j}&=\lambda_jA_j(n)-A_{j+1}(n).
\end{aligned}
\]
For division rows, the horizontal labels are retained in the formal
thirds notation. A zero on the south side of row \(j\) is written \(0'\)
exactly when \(\alpha_{j-1}\in[1/3,1/2]\); a zero on the north side is
written \(0'\) exactly when \(\alpha_j\in[1/3,1/2]\). Other numerical zeros
are written \(0\). These rules select exactly one of the 13 table entries at
every \((n,j)\).

All floor decisions are exact. Each \(\alpha_j\) is a rational multiple of
\(\sqrt2\), so \(\lfloor n\alpha_j\rfloor\) is computed by an integer square
root. Choose sheet \(r_0=0\) and propagate it by the displayed winding rule.
This defines an infinite point of \(K^{(m)}\) without numerical comparison.

## 3. Exact construction of \(P_m\)

### 3.1 The phase honeycomb

Let \(H_2\) be the following finite cellulation of the torus. Its vertices
are
\[
  B_{ij},W_{ij},\qquad i,j\in\mathbb Z/2\mathbb Z.
\]
The three neighbors of \(B_{ij}\) are
\[
  W_{ij},\quad W_{i-1,j},\quad W_{i,j-1}.
\]
Its four faces are the simple cycles
\[
\begin{split}
 C_{ij}=(B_{ij},W_{ij},B_{i+1,j},W_{i+1,j-1},\\
 B_{i+1,j-1},W_{i,j-1}).
\end{split}
\]
Thus \(H_2\) has 8 vertices, 12 edges, and 4 faces. Its universal cover is
the standard honeycomb.

Put source symbols \(x_{ij}\) on honeycomb faces indexed by
\((i,j)\in\mathbb Z^2\). The west-east Wang constraint is imposed in the
\(i\) direction, the south-north constraint in the \(j\) direction, and
the third face-neighbor direction is unconstrained.

At a black vertex use the ordered triple
\[
  B_{ij}:\quad(x_{ij},x_{i-1,j+1},x_{i-1,j}),
\]
and at a white vertex use
\[
  W_{ij}:\quad(x_{ij},x_{i,j+1},x_{i-1,j+1}).
\]
A vertex state consists of the indicated vertex of \(H_2\) and one locally
legal ordered triple.

The state sets are ordered finitely and explicitly. Source symbols have
indices \(m\tau+r\), with \(\tau\) in the order of the table and
\(0\leq r<m\). Phases are ordered first by \(i\), then \(j\). Black triples
are ordered by central symbol \(a\), west neighbor \(c\), and north neighbor
\(b\). White triples are ordered by central symbol \(a\), north neighbor
\(d\), and west neighbor \(b\). Let the resulting black and white indices be
\[
  b(q)\in\{0,\ldots,B-1\},\qquad
  w(q)\in\{0,\ldots,W-1\}.
\]

### 3.2 Legal coronas

Name a central face \(a\) and its six cyclic neighbors
\[
  b,d,e,f,g,c.
\]
The seven symbols form a legal corona when the following eight Wang
adjacencies hold:
\[
  c-a,\quad a-e,\quad b-d,\quad g-f
\]
in the west-east direction, and
\[
  g-a,\quad a-d,\quad c-b,\quad f-e
\]
in the south-north direction.

For phase \(C_{ij}\), the six vertex states of this corona are
\[
\begin{split}
q_0&=B_{ij}(a,b,c),\\
q_1&=W_{ij}(a,d,b),\\
q_2&=B_{i+1,j}(e,d,a),\\
q_3&=W_{i+1,j-1}(f,e,a),\\
q_4&=B_{i+1,j-1}(f,a,g),\\
q_5&=W_{i,j-1}(g,a,c).
\end{split}
\]
Let \(G\) be the simple bipartite graph whose black and white vertices are
the state sets and whose edges are the consecutive pairs that occur in one
of these legal cycles. Multiple corona witnesses never create parallel graph
edges.

### 3.3 Rational coordinates

Use the affine honeycomb hexagon
\[
\begin{aligned}
v_0&=(2,0),&
v_1&=(1,3/2),&
v_2&=(-1,3/2),\\
v_3&=(-2,0),&
v_4&=(-1,-3/2),&
v_5&=(1,-3/2).
\end{aligned}
\]
Set
\[
  D=4096BW
\]
and assign horizontal displacements
\[
  z_q=
  \begin{cases}
    b(q)/D,&q\text{ black},\\
    B(w(q)+1)/D,&q\text{ white}.
  \end{cases}
\]
The prototile associated with a legal corona is the polygon with cyclic
vertices
\[
  p_k=v_k+(z_{q_k},0),\qquad 0\leq k<6.
\]
Finally, \(P_m\) is the set of all such congruence classes over the four
phases and all legal coronas.

This is a finite exact definition. Every coordinate lies in
\((2D)^{-1}\mathbb Z\), so multiplication by \(2D\) gives integer
coordinates.

### 3.4 Unique edge lengths

For a black state of index \(b\) and white state of index \(w\), put
\[
  \delta=\frac{B(w+1)-b}{D}.
\]
The numerator belongs to the block
\[
  \{Bw+1,\ldots,Bw+B\}.
\]
These blocks are pairwise disjoint, and
\[
  0<\delta\leq\frac1{4096}.
\]
The black-to-white base edges have one horizontal direction and two slant
directions. Their squared lengths after displacement are
\[
  4+4\delta+\delta^2
\]
and
\[
  \frac{13}{4}-2\delta+\delta^2,
\]
respectively. The first function is strictly increasing on the relevant
interval, the second is strictly decreasing, and their ranges are disjoint.
The phase in a vertex state prevents one state pair from occurring in two
different slant directions. Therefore every edge of \(G\) has a globally
unique side length.

Each face cycle has six distinct graph edges. A congruence must preserve its
cyclic side-length word up to the dihedral action. Consecutive graph edges
recover their common vertex state, so two different corona cycles cannot
become congruent.

## 4. Shape-only forcing

### 4.1 Convexity and the exclusion of T-junctions

The undisplaced hexagon is strictly convex and all of its angles are obtuse.
Every perturbed edge changes only its horizontal component, by at most
\(1/4096\). Consecutive cross products remain positive. Consecutive forward
edge dot products remain positive, which is equivalent to a negative dot
product between the two rays defining the interior angle. Hence every
output polygon is strictly convex and every interior angle is in
\((\pi/2,\pi)\). For \(P_2\), both signs at all 59,472 corners are also
checked by exact integer arithmetic in the retained certificate.

Now consider an arbitrary tiling by the unmarked polygons. If a tile vertex
lay in the relative interior of another tile edge, the latter tile would
occupy one half-plane at that point. The other half-plane has angle \(\pi\).
One strictly convex corner cannot fill it, while two corners each larger
than \(\pi/2\) have total angle larger than \(\pi\). This is impossible.
Thus no T-junction occurs.

Every shared boundary segment is consequently a whole side of each incident
polygon. At a tiling vertex, two corners have total angle less than \(2\pi\),
while four corners have total angle greater than \(2\pi\). Exactly three
corners meet. Every admitted tiling is therefore an edge-to-edge trivalent
hexangulation.

### 4.2 The abstract honeycomb

Replace each physical face by a unit regular hexagon and glue corresponding
full sides. Three \(120\)-degree sectors meet at every vertex. The physical
tiling is locally finite because the protoset is finite and its members have
positive inradius. The regularized metric is complete, and the underlying
cell complex is homeomorphic to the plane. It is therefore a complete
simply connected flat surface. Its developing map is a global Euclidean
isometry. The abstract cell complex is the standard \(\{6,3\}\) honeycomb.

### 4.3 The line-graph star lemma

A physical side length decodes one edge of \(G\). At a physical vertex, each
pair among the three decoded graph edges occurs as a corner of one incident
face, so each pair shares an endpoint in \(G\). The three edges are distinct
because every face cycle is simple.

The graph \(G\) is simple and bipartite. A triangle in its line graph must
therefore be a star: otherwise the three original edges would form a
triangle in \(G\). Hence the three physical sides at a vertex share one
vertex state \(q\). This rules out a vertex assembled from three pairwise
plausible but mutually incompatible corners.

### 4.4 Phase covering and the global frame

The decoded state at each physical vertex maps it to a vertex of \(H_2\).
The three incident graph edges project to three distinct phase edges because
each polygon maps to a simple face cycle. Thus every physical vertex star
maps bijectively to a phase vertex star.

Two physical faces across one edge cannot map to the same phase face. If
they did, their remaining rays would violate this local star bijection. The
physical honeycomb therefore covers \(H_2\). Since its cell complex is
simply connected, it is the universal cover. The local orientation sign of
a surface covering is constant, so every tile placement uses one global
orientation or one global reflection of the canonical frame.

There is also a direct geometric formulation. Two Euclidean placement maps
that agree on a shared edge vector either have the same orthogonal part or
differ by reflection in that edge. The second choice puts the two incident
source faces on the same physical side of the edge and causes overlap. The
orthogonal part is consequently one common
\[
  R(\mathcal T)\in O(2)
\]
throughout a tiling.

### 4.5 Source reconstruction

At each physical vertex, the recovered state supplies its ordered source
triple. Around a face, the six states recover the same central symbol. Across
an edge, the states recover the corresponding adjacent source symbols and
their Wang match. The covering coordinates give a global configuration
\((x_{ij})\in K^{(m)}\).

This argument uses only polygon shapes and contacts. It classifies every
element of \(X(P_m)\), not merely tilings made by the intended generator.

## 5. Existence and aperiodicity

Start from any source configuration in \(K^{(m)}\). Place each honeycomb
vertex at its affine base position plus the displacement of its locally
determined state. Extend the vertex map affinely over a fixed triangulation
of every face.

The displacement is bounded by \(1/4096\). The exact convexity inequalities
preserve the orientation of every triangle and the cyclic order of rays at
each vertex. The resulting piecewise-affine map is a local homeomorphism. It
is proper because it remains at bounded distance from the identity. A proper
local homeomorphism of the plane is a covering of the plane, and hence a
homeomorphism. Its face images form a tiling by \(P_m\). This proves
nonemptiness.

Conversely, straighten an arbitrary \(P_m\)-tiling by sending every decoded
vertex
\[
  R(v+z_q(1,0))+t
\]
to
\[
  Rv+t.
\]
The same fixed triangulation extends this to a local, invertible,
translation-equivariant shape conjugacy with a regular honeycomb suspension.

If the original tiling had a nonzero translational period, the straightened
honeycomb tiling would have the same period. Such a period is a nonzero
honeycomb lattice vector and induces a nonzero \(\mathbb Z^2\)-period of the
decoded \(K^{(m)}\) configuration. Strong aperiodicity of the source excludes
it. This proves Theorems 1 and 2 up to the family-distinctness statement.

## 6. The complete hull and the winding invariant

### 6.1 Hull classification

All side lengths are globally distinct, and no prototile has a nontrivial
isometry. A tile occurrence therefore determines its prototile and its
placement isometry uniquely. The common orthogonal part defines an intrinsic,
continuous, translation-invariant map
\[
  R:X(P_m)\longrightarrow O(2).
\]
The straightening above is strongly pattern-equivariant and invertible.
Consequently each fixed-frame part of \(X(P_m)\) is the honeycomb suspension
of the full \(H_2\)-phased, vertex-collared \(K^{(m)}\) shift. Global
rotations and reflections supply the \(O(2)\) orientation factor. Orbit
closures and minimal components correspond exactly to those of the full
source shift; no selected generated orbit is substituted for the complete
hull.

The Siefken Sturmian core gives a distinguished minimal component. The
following computation is made there and then extended over all orientations.

For an \(N\times N\) legal source pattern, a sheet value on one row fixes
every other sheet value in the pattern. The number of lifted patterns differs
from the base pattern count by at most the constant factor \(m\). The winding
lift therefore has the same area-normalized topological entropy as the base
Kari-Culik shift. Finite collaring and the four-state phase extension do not
change entropy, and the bounded straightening has one honeycomb face per area
9. Durand, Gamard, and Grandjean's positivity theorem consequently gives
positive entropy for the fixed-frame geometric hull.

### 6.2 The source eigenvalue group

Let \(H,V\) be the horizontal and vertical shifts and write
\(e(t)=\exp(2\pi i t)\). Durand, Gamard, and Grandjean prove that every
Kari-Culik row has an average. In logarithmic coordinates,
\[
  u=\frac{\log\alpha+\log3}{\log6},
\]
the multiplier type satisfies
\[
  u_{j+1}=u_j+\theta-c_j\pmod1.
\]
The exact \(\sqrt2\) construction has a dense nonsingular itinerary, so the
multiplier factor is the full Sturmian shift of slope \(\theta\).

Balanced Sturmian discrepancy and the Gottschalk-Hedlund theorem give a
continuous function \(h\) with
\[
  h(\sigma c)-h(c)=c_0-\theta.
\]
On \(K^{(m)}\),
\[
  F_m(x,r)=e\left(\frac{r-h(c(x))}{m}\right)
\]
is \(H\)-invariant and has \(V\)-eigenvalue \(e(\theta/m)\).

For the upper bound, choose an irrational continuity point in Siefken's
parameter core. For every sequence \(q_j\) satisfying
\[
  q_j\theta/m\longrightarrow0\pmod1,
\]
write
\[
  q_j\theta=mp_j+\delta_j,\qquad\delta_j\to0.
\]
At a log coordinate away from the coding cut, the exact wrap count over
\(q_j\) rows is eventually \(mp_j\), so the sheet returns.
Siefken's horizontal density supplies corrections \(a_j\) with
\[
  H^{a_j}V^{q_j}y\longrightarrow y.
\]
Every \(H\)-invariant vertical eigenvalue \(\mu\) therefore satisfies
\(\mu^{q_j}\to1\) for every such return sequence. The homomorphism
\[
  q\theta/m\longmapsto\mu^q
\]
on the dense cyclic subgroup of the circle is continuous at zero and extends
to a circle character. Hence
\[
  E_H(K^{(m)})=\langle e(\theta/m)\rangle.
\]

The complete joint eigenvalue group on the lifted minimal core is
\[
  E(K^{(m)})=
  \{(1,e(k\theta/m)):k\in\mathbb Z\}.
\]
To see why no horizontal eigenvalue is missing, restrict a joint
eigenfunction with horizontal eigenvalue \(\lambda\) to a Siefken parameter
point \((\alpha,t)\) at which the coding is continuous. Horizontal motion is
the dense rotation \(t\mapsto t+\alpha\) on the 6-adic solenoid when
\(\alpha\) is irrational. Return continuity makes
\(a\alpha\mapsto\lambda^a\) a continuous character on a dense cyclic
subgroup. It follows that
\[
  \lambda=e(q\alpha)
\]
for some \(q\in\mathbb Z[1/6]\), the dual of that solenoid. The coding has
continuity points over an uncountable set of irrational \(\alpha\). If
\(\lambda\ne1\), the displayed equation places every such \(\alpha\) in the
countable union, over nonzero \(q\in\mathbb Z[1/6]\), of the countable
solution sets of \(e(q\alpha)=\lambda\). This is impossible. Therefore
\(\lambda=1\), and the controlled vertical-return argument gives the stated
joint group.

Fourier decomposition over the \(H_2\) phase
\((\mathbb Z/2\mathbb Z)^2\) gives
\[
  E(\Xi_m)=
  \{((-1)^\varepsilon,
  (-1)^\delta e(k\theta/m)):
  \varepsilon,\delta\in\{0,1\},\ k\in\mathbb Z\}.
\]

### 6.3 Relative eigenfields

The affine face-center lattice has basis
\[
  a=(-3,3/2),\qquad b=(0,3),
\]
with dual basis
\[
  a^*=(-1/3,0),\qquad b^*=(1/6,1/3).
\]
The continuous eigenmodule of the fixed-frame suspension is
\[
  M_m=
  \frac12\mathbb Z\,a^*+
  \left(\frac12\mathbb Z+\frac{\theta}{m}\mathbb Z\right)b^*.
\]

Ordinary fixed-vector eigenfunctions do not express this invariant on the
union of all rotated hulls. Instead, define a relative eigenfield on an
\(\mathbb R^2\)-tiling system \(X\) to be a pair
\[
  \kappa:X\to(\mathbb R^2)^*,\qquad f:X\to S^1
\]
where \(\kappa\) is continuous and translation-invariant and
\[
  f(\mathcal T-t)=
  e(\kappa(\mathcal T)\cdot t)f(\mathcal T).
\]
This definition uses only the translation action, and translation
conjugacies pull such pairs back.

Every \(k\in M_m\) extends over the complete rotating hull by
\[
  \kappa_k(\mathcal T)=R(\mathcal T)k,\qquad
  \widehat f_k(\mathcal T)=
  f_k(R(\mathcal T)^{-1}\mathcal T).
\]

Suppose \(\Phi:X(P_m)\to X(P_n)\) is a translation conjugacy. Restrict it to
the fixed-frame lifted Siefken minimal core. The function
\(R_n\circ\Phi\) is continuous and translation-invariant, so minimality
makes it a constant orthogonal map \(A\). Pulling back every relative
eigenfield gives
\[
  AM_n\subseteq M_m.
\]
The inverse conjugacy gives an orthogonal \(B\) with
\[
  BM_m\subseteq M_n.
\]

The closure of \(M_m\) is
\[
  \overline{M_m}=
  \bigcup_{r\in\frac12\mathbb Z}
  (r a^*+\mathbb R b^*).
\]
Its connected components have the unique line direction
\(\mathbb Rb^*\). Therefore \(A b^*=\pm b^*\), and
\[
  \frac12\mathbb Z+\frac{\theta}{n}\mathbb Z
  \subseteq
  \frac12\mathbb Z+\frac{\theta}{m}\mathbb Z.
\]
In particular,
\[
  \frac{\theta}{n}=\frac r2+\frac{k\theta}{m}
\]
for integers \(r,k\). Irrationality of \(\theta\) forces \(r=0\) and
\(m=kn\), so \(n\mid m\). The inverse inclusion gives \(m\mid n\).
Thus \(m=n\), proving family distinctness.

## 7. Substantive advance and comparison boundary

The construction advances two linked fronts.

First, it gives an explicit and checkable way to make arbitrary contacts
harmless while retaining convexity. The all-obtuse condition itself forces
edge-to-edge contact and trivalence. Unique mixed-radix lengths then turn a
line-graph identity into complete radius-one decoding. No tabs, dents,
colors, selected atlas, or forbidden reflection is left in the final model.

Second, the winding cover is not a split color decoration. Its maximal
equicontinuous circle factor has rotation \(e(\theta/m)\), and the relative
eigenmodule proves that the complete all-orientation hull changes with \(m\).
The source and geometric hulls have positive entropy, inherited from the
Kari-Culik system.

The finite comparison set is as follows.

| Comparison | Distinction |
|---|---|
| Robinson's 1971 convex announcement | It states the same broad variable-cardinality convex lattice undecidability conclusion, but gives no construction, protoset, forcing proof, or complete hull to compare. It prevents a general convex-priority claim. |
| Unlifted Kari-Culik hull | It has the \(m=1\) eigenmodule. The relative module above separates it from every nontrivial winding index. Entropy does not separate them. |
| Healey-Ammann convex recomposition | Conditional on its asserted Penrose recomposition theorem, it has Penrose zero entropy, unlike \(P_2\). Its published vertex-atlas proof does not expressly exclude T-junctions in the unrestricted-contact model used here. |
| Sugimoto's three convex polygons | The source explicitly reports periodic tilings when reflected copies are allowed, so its complete all-isometry hull is not aperiodic in the present model. |
| Hat and Spectre hulls | Their finite metatile hierarchies have zero area-normalized patch entropy. \(P_2\) has positive entropy. |
| Baake-Gähler-Grimm hexagonal inflation hull | It is a pure-point inflation/model-set hull with zero patch entropy. \(P_2\) has positive entropy. |
| Demaine-Langerman's published Jeandel-Rao output | Its wheel, shuriken, and staple use reflex geometry. The present theorem restricts every output tile to the strictly convex all-obtuse rational-hexagon class. |
| Stade's two-polygon compiler | Its Wang carrier is a highly concave modified polyhex stick. It does not meet the convex output restriction. |
| Yang-Zhang orthogonally convex compiler | Its seven polyominoes are not Euclidean-convex and copies are restricted to translations. Its open problem fixes the number of convex input polygons, unlike this variable-cardinality output. |
| Existing repository hulls and shape sets | Bare triangles, rhombs, dominoes, chairs, and parallelograms represented there admit periodic tilings. Their selected generated patches do not define strongly aperiodic shape-only hulls. |

There is an important limitation. A universal concave compiler can be
instantiated on the same \(K^{(m)}\) source, and that output is expected to
be locally equivalent to the same symbolic phase extension. The relative
module does not distinguish two faithful compilers fed the same source. The
new method claim is therefore the strict convex all-obtuse output class and
its full unrestricted-contact theorem. It is not a claim that older concave
compiler theorems could not present the same symbolic dynamics.

## 8. Novelty search

The search was conducted on 2026-07-25 and 2026-07-26 through arXiv, Crossref
and publisher search pages, Google Scholar-style citation results, zbMATH
publication listings, primary-paper bibliographies, and repository source.
Queries included:

```text
unmarked aperiodic protoset convex polygons tiling plane
three convex polygons aperiodic Penrose
convex hexagons undecidability tiling
arbitrary finite set of convex hexagons Robinson
obtuse convex hexagons aperiodic tiling
all angles obtuse convex hexagons matching rules
rational obtuse hexagons tiling
Kari-Culik cyclic extension eigenvalues
finite cyclic extension Sturmian shift
positive entropy polygon aperiodic protoset
```

The search included backward and forward trails from Robinson 1971,
Demaine-Langerman 2025, Stade 2025, Yang-Zhang 2025, Healey 2011, Sugimoto
2024, and Baake-Gähler-Grimm 2012. No searched primary source gave the
all-obtuse compiler and complete-hull theorem above.

Robinson's 1971 paper contains the strongest priority warning. On page 181
he announces that Berger's theorem can be reduced to finite sets of convex
lattice-coordinate hexagons or pentagons even when rotations and reflections
are allowed. The paper supplies no proof there and says that those results
were intended for later publication. The searched publication and citation
records did not locate that later proof. This report therefore describes the
compiler as an explicit strengthening and proof within the stated output
class, not as the origin of convex-polygon undecidability.

Yang and Zhang ask whether undecidability holds for a fixed number \(k\) of
convex polygons. The cardinality of \(P(S)\) grows with the source state and
corona languages, so this construction does not resolve their problem.

## 9. Exact certificates and replay

The retained exact audit is
`workbench/kc-convex-candidate.mjs`. It uses `BigInt` coordinates with common
denominator \(2D\). It enumerates every source symbol, vertex state, graph
edge, and legal corona, and checks:

1. every face cycle is simple;
2. every corner has positive exact cross product;
3. every corner has negative exact interior-ray dot product;
4. every graph edge has one consistent squared length;
5. distinct graph edges have distinct squared lengths;
6. distinct corona cycles remain distinct under the dihedral action;
7. a \(201\times201\) exact source window obeys every Wang match and sees all
   13 base tile types.

Replay the promoted \(P_2\) audit with:

```sh
node workbench/kc-convex-candidate.mjs 2 2 100
```

Expected principal values are:

```text
alphabetSize                 26
blackCount                   1136
whiteCount                   1200
graphEdgeCount               7264
coronaCount                  9912
congruenceClassCount         9912
exactConvexityChecks         59472
exactUniqueLengthChecks      7264
coordinateCertificateSha256 96b836e8490e292ce2b94f151945752aa53d61163e82195661c0384495ac9e2b
```

The \(m=5\) family check is:

```sh
node workbench/kc-convex-candidate.mjs 5 2 100
```

Its expected prototile count is 24,780 and its coordinate certificate is:

```text
9f8202a849d35024bb5ef883d6eb9309e04788675fda43afc7fca846e7a50249
```

## 10. Implementation contract

The repository implementation is a pure deterministic generator named
`winding-honeycomb`. It evaluates the exact \(\sqrt2\) source point using
integer arithmetic, builds the globally indexed vertex-state catalog, and
emits compatible honeycomb face patches as canonical `TilingSpec` values.
The mathematical decisions use exact integers. Conversion to JavaScript
numbers occurs only when exact rational vertices are handed to the renderer.

The geometry parameters are:

| Parameter | Meaning |
|---|---|
| `patchRadius` | Hexagonal face radius of the finite patch |
| `windingModulus` | Family index \(m\), with audited choices 2, 3, and 5 |

Faces are ordered by honeycomb shell and then lattice coordinate, so a
radius-\(r\) patch is a literal geometric subset of radius \(r+1\). The
central face has centroid at the origin for every radius. Shared vertex IDs
and reciprocal edge references encode the finite-patch topology. Edge labels
are null and `matchingRules` is `none`, reflecting the fact that the theorem
uses shapes alone.

Browser-free replay is:

```sh
npm run tiling:data -- geometry --query '?tiling=winding-honeycomb&geom.patchRadius=4&geom.windingModulus=2'
npm run tiling:data -- analysis --query '?tiling=winding-honeycomb&geom.patchRadius=4&geom.windingModulus=2'
```

Visual inspection uses the same query with the development server.

## 11. Limitations

The construction favors proof transparency over small cardinality. \(P_2\)
has 9,912 shapes, and its length differences are exact but visually subtle.
It does not address the two-convex-polygon or fixed-\(k\) convex
undecidability problems.

The family invariant is proved on the lifted Siefken minimal core and
extended to the complete all-orientation hull as relative eigenfields. It
separates winding indices, but it does not distinguish alternative faithful
geometric presentations of the same \(K^{(m)}\) source.

The search boundary is serious but finite. Robinson's unpublished announced
construction is a particular reason not to make an unconditional priority
claim beyond the exact restrictions and sources recorded here.

## References

1. Karel Culik II, "An aperiodic set of 13 Wang tiles," *Discrete
   Mathematics* 160 (1996), 245-251.
   https://doi.org/10.1016/S0012-365X(96)00118-5
2. Bruno Durand, Guilhem Gamard, and Anaël Grandjean, "Aperiodic tilings and
   entropy," *Theoretical Computer Science* 666 (2017), 36-47.
   https://doi.org/10.1016/j.tcs.2016.12.013
3. Jason Siefken, "A minimal subsystem of the Kari-Culik tilings," *Ergodic
   Theory and Dynamical Systems* 37 (2017), 1607-1634.
   https://doi.org/10.1017/etds.2015.118
4. Raphael M. Robinson, "Undecidability and nonperiodicity for tilings of the
   plane," *Inventiones Mathematicae* 12 (1971), 177-209.
   https://doi.org/10.1007/BF01418780
5. Erik D. Demaine and Stefan Langerman, "Tiling with Three Polygons Is
   Undecidable," SoCG 2025, article 39.
   https://doi.org/10.4230/LIPIcs.SoCG.2025.39
6. Jack Stade, "Two Tiling is Undecidable," 2025.
   https://arxiv.org/abs/2506.11628
7. Chao Yang and Zhujun Zhang, "Undecidability of Translational Tiling with
   Orthogonally Convex Polyominoes," 2025.
   https://arxiv.org/abs/2506.12726
8. Vivian Olsiewski Healey, "A Family of Recompositions of the Penrose
   Aperiodic Protoset and Its Dynamic Properties," 2011.
   https://arxiv.org/abs/0912.3814
9. E. Arthur Robinson Jr., "The dynamical properties of Penrose tilings,"
   *Transactions of the American Mathematical Society* 348 (1996),
   4447-4464. https://doi.org/10.1090/S0002-9947-96-01640-6
10. Teruhisa Sugimoto, "Aperiodic sets of three types of convex polygons,"
    version 5, 2024. https://arxiv.org/abs/2404.00534
11. David Smith, Joseph Samuel Myers, Craig S. Kaplan, and Chaim
    Goodman-Strauss, "An aperiodic monotile," *Combinatorial Theory* 4(1)
    (2024), paper 6. https://doi.org/10.5070/C64163843
12. David Smith, Joseph Samuel Myers, Craig S. Kaplan, and Chaim
    Goodman-Strauss, "A chiral aperiodic monotile," *Combinatorial Theory*
    4(2) (2024), paper 13. https://doi.org/10.5070/C64264241
13. Michael Baake, Franz Gähler, and Uwe Grimm, "Hexagonal Inflation Tilings
    and Planar Monotiles," *Symmetry* 4 (2012), 581-602.
    https://doi.org/10.3390/sym4040581
14. Michael Baake, Daniel Lenz, and Christoph Richard, "Pure point
    diffraction implies zero entropy for Delone sets with uniform cluster
    frequencies," *Letters in Mathematical Physics* 82 (2007), 61-77.
    https://arxiv.org/abs/0706.1677
