# Shape-only aperiodic protoset research log — 2026-07-25

This is a restartable working record for the run begun at 21:40 CEST. Nothing
recorded here is a discovery unless it separately passes every acceptance gate
in `workbench/tiling-discovery-prompt.md`.

## Convex polygon forcing

### Model

- Target: preferably two or three convex simple polygons.
- Allowed placements: every Euclidean isometry, including reflections.
- Contacts: unrestricted; no edge-to-edge assumption.
- Required certificate: exact coordinates, an infinite construction, and a
  shape-only classification of every admitted tiling component.

### Current state

- The repository has no convex shape-only forcing construction. Its convex
  aperiodic-looking patches come from selected substitutions or multigrids and
  therefore do not establish anything about the full hull admitted by the
  bare shapes.
- A primary-source screen on 2026-07-25 used web/arXiv queries
  `"unmarked aperiodic protoset convex polygons tiling plane"`,
  `"two prototiles" "aperiodic" unmarked polygons geometry`,
  `"three convex polygons" aperiodic Penrose`, and
  `convex polygons hat decomposition aperiodic set reflections allowed`.
  Teruhisa Sugimoto, *Aperiodic sets of three types of convex polygons*,
  arXiv:2404.00534v5 (2025), is a near match but explicitly treats reflected
  copies as different, forbidden tile types (pp. 2–3). It states that its
  Tile(1,1)-derived three-convex sets form periodic tilings when reflections
  are admitted (p. 4). The construction is therefore a counterexample to
  treating “no edge markings” as equivalent to the two-sided shape-only model
  of this run.
- David Smith, Joseph Samuel Myers, Craig S. Kaplan, and Chaim
  Goodman-Strauss, *An aperiodic monotile*, arXiv:2303.10798v3 / Combinatorial
  Theory 4(1) (2024), proves the Hat and every positive `Tile(a,b)` with
  `a != b` strongly aperiodic with reflections allowed. A convex dissection
  that is forced to recompose uniquely into such a tile would establish
  aperiodicity, but would remain merely MLD to the Hat hull and fail this
  prompt's distinctness gate unless it carries a proved additional component
  or hull invariant.
- The closest historical convex set needs a model correction. The three-tile
  `A3` in Robert Ammann, Branko Grünbaum, and G. C. Shephard, *Aperiodic
  Tiles*, Discrete & Computational Geometry 8 (1992), pp. 1–25,
  DOI `10.1007/BF02293033`, is not the convex Ammann recomposition. Its
  Figure 22(a) uses three nonconvex curvilinear jigsaw tiles; Figure 22(b) uses
  three marked concave rectilinear tiles. Section 5 imposes a no-turning-over
  condition, and when reflected marked tiles are restored the paper explicitly
  leaves the classification of the additional tilings as a conjecture.
- The actual convex Ammann family is treated by L. Healey, *A Family of
  Recompositions of the Penrose Aperiodic Protoset*, arXiv:0912.3814.
  Algorithm 4.1 chooses an interior point in a thin Penrose rhomb, transports
  it to thick rhombs, and erases rhomb boundaries to obtain two convex
  pentagons and one convex hexagon. Four relevant edge lengths are required to
  be pairwise distinct. Theorem 4.6 recovers Penrose rhombs from admitted
  vertex stars, but the proof enumerates meetings of polygon vertices and does
  not first exclude a vertex lying in the relative interior of another tile's
  side. It therefore does not certify unrestricted contacts. It is also an
  explicit Penrose recomposition and fails this run's distinctness gate.
- First attack: seek angle/length spectra whose arbitrary contacts can be
  reduced to finitely many edge-to-edge coronas without assuming that
  reduction. Any candidate must also survive a direct search for strip and
  reflected periodic escapes.
- No exact candidate has yet survived local scrutiny.

### Resume point

Move beyond constant-angle, length-only carriers. Any variable-angle carrier
must retain the proved no-T-junction property, encode edge polarity despite
reflections, satisfy exact polygon closure, and exclude monohedral periodic
escapes before attempting a global aperiodicity proof.

### Exact 120-degree hexagon reduction and obstruction

- Let every prototile be a strictly convex equiangular hexagon with interior
  angles `2*pi/3`. At any boundary contact point an incident tile contributes
  either `2*pi/3` at a vertex or `pi` along the relative interior of a side.
  The angle equation is `2n + 3m = 6`; its only nonnegative solutions are
  `(n,m) = (3,0)` and `(0,2)`. Hence a tile vertex is exactly a meeting of
  three tile vertices, never a T-junction. A changeover between two neighbors
  along one side would itself create a forbidden T-junction, so every side
  meets one entire equal-length side.
- Replacing each face by a regular unit hexagon gives a complete, simply
  connected, locally Euclidean hexagonal complex. Its developing map identifies
  the abstract complex with the standard `{6,3}` honeycomb. Edge adjacency also
  propagates one global triple of unoriented edge directions in the original
  geometry. Thus unrestricted contacts really do reduce to a face-to-face
  honeycomb symbolic system in this class.
- If successive side lengths are `(s0,s1,s2,s3,s4,s5)`, exact vector closure is
  equivalent to
  `s3 - s0 = s1 - s4 = s5 - s2 = delta`.
- The direct square-Wang-to-hexagon compiler is killed exactly. Its two added
  opposite neutral sides require `s2 = s5`, hence `delta = 0`, then
  `s0 = s3` and `s1 = s4`. Every produced hexagon is centrally symmetric with
  edge vectors `(u,v,w,-u,-v,-w)` and tiles periodically by translations
  `u+v` and `v+w`; `det(u+v,v+w)` equals its area. Any one prototile is
  therefore a periodic escape.
- The Kari–Culik arithmetic variant does not repair the obstruction.
  Eigen–Navarro–Prasad's construction distinguishes numerical-zero colors
  `0`, `0'`, and `0_3`; collapsing them restores periodically tiling
  `a/0/0/a` tiles. Encoding only numerical values as edge lengths collapses
  these colors, while assigning them different lengths destroys the arithmetic
  closure identity. Constant 120-degree endpoint angles provide no second
  polarity channel.
- Exact primary-source replay:
  `curl -sS https://faculty.washington.edu/moishe/branko/BG186.Aperiodic%20tiles.pdf -o /tmp/ammann-aperiodic-1992.pdf`.
  The reductions above are hand-checkable equalities and use no
  floating-point computation.

### Exact convex-honeycomb compiler theorem: forcing passes, priority narrowed

- A stronger convex carrier starts with a face SFT on the honeycomb, collars
  its faces and vertices, and assigns each allowed collared vertex state `q`
  a small displacement `z_q`. An allowed collared face is represented by the
  convex hexagon through its six displaced honeycomb vertices. Unlike
  independently chosen side lengths or angles, this makes every intended
  polygon close identically and supplies an infinite geometric tiling from
  every source tiling.
- The proposal can be made exact over `Q(sqrt(3))`: choose rational
  displacements, and verify strict convexity plus angles greater than
  `pi/2` using determinant and dot-product signs. The latter condition again
  forces every unrestricted tiling to be edge-to-edge with exactly three
  tile vertices at each contact point. Squared edge lengths, polygon
  congruences, and unintended angle sums are then finite polynomial
  conditions, so a lexicographic rational enumeration can avoid any
  non-identically-zero bad condition and yield explicit coordinates.
- Generic angle separation is not enough. If an oriented displaced ray is
  `r(s,t,k) = e_k + z_t - z_s`, then reversing an edge gives
  `r(t,s,k+3) = -r(s,t,k)`. A corner angle is a quotient of two such ray
  directions. Three corner turns sum to `2*pi` identically whenever their
  ray factors form a closed three-cycle under this reversal, even if the
  corners came from three mutually incompatible collared source vertices.
  These “Frankenstein vertices” lie on structural algebraic identities and
  cannot be removed by a generic coordinate choice.
- A flag construction appears to close this gap without testing angle sums.
  Let each honeycomb vertex state `q` contain its black/white vertex class, a
  finite coordinate phase, and the ordered triple of symbols on its incident
  source faces. Form the simple bipartite compatibility graph `G` whose edge
  `{q,r}` records a compatible pair of endpoint states on one honeycomb edge;
  the phase distinguishes the three directions and rules out parallel edges.
  Give every graph edge a distinct side length by choosing small rational
  displacements outside the finite union of squared-length equality
  hypersurfaces.
- In an arbitrary geometric tiling, a side length now decodes one edge of
  `G`. At a physical vertex the three intervening polygon corners show that
  each pair among the three decoded graph edges shares an endpoint. Thus they
  form a triangle in the line graph `L(G)`. Every triangle of the line graph
  of a simple triangle-free graph is a star: otherwise the three original
  edges form a triangle. Because `G` is bipartite, the three edges therefore
  share one vertex state `q`. The coordinate phases make their directions
  distinct, so the whole intended source vertex star—and not a Frankenstein
  combination—is recovered. The same argument also forces the endpoint
  polarity of matched sides and makes local reflection choices propagate to
  one global reflection.
- A rational-coordinate base is available, strengthening the earlier
  `Q(sqrt(3))` observation. The centrally symmetric hexagon with vertices
  `(2,0),(1,3/2),(-1,3/2),(-2,0),(-1,-3/2),(1,-3/2)` is an affine image of a
  regular honeycomb hexagon and has every interior angle strictly greater
  than `pi/2`. Sufficiently small rational displacements therefore leave all
  coordinates rational, preserve strict convexity and the no-T-junction
  condition, and produce the same abstract honeycomb.
- The generic rational enumeration is in fact unnecessary. If the black
  states are indexed `b=0,...,B-1` and the white states
  `w=0,...,W-1`, put `D=4096*B*W` and use horizontal displacements
  `z_b=b/D` and `z_w=B(w+1)/D`. The oriented difference has numerator
  `B(w+1)-b`, whose possible values for fixed `w` are the disjoint block
  `{Bw+1,...,Bw+B}`. It therefore uniquely recovers `(b,w)`, and
  `0<z_w-z_b<=1/4096`. This mixed-radix assignment replaces the earlier
  exponential-bit dyadic proposal and stays usable in an ordinary renderer.
  The affine base has one black-to-white edge direction of squared length
  `4` and two of squared length `13/4`. For
  `delta=z_w-z_b`, their perturbed squared lengths are respectively
  `4+4*delta+delta^2` and `13/4-2*delta+delta^2`; the first is increasing,
  the second decreasing, and their ranges are disjoint. Thus every graph
  edge has a globally unique exact rational length.
- The finite phase object is now explicit. Let `H_2` have vertices
  `B_ij,W_ij`, with `i,j in Z/2`, and edges from `B_ij` to
  `W_ij,W_(i-1,j),W_(i,j-1)`. Its four faces are
  `C_ij=(B_ij,W_ij,B_(i+1,j),W_(i+1,j-1),B_(i+1,j-1),W_(i,j-1))`.
  Each boundary is a simple 6-cycle, `V=8,E=12,F=4`, and `H_2` is the
  `2 by 2` torus quotient of the honeycomb.
- Source faces have coordinates `(i,j) in Z^2`. Square-Wang west/east
  constraints are placed on the `i` axis, south/north constraints on the
  `j` axis, and the third triangular-lattice adjacency is unconstrained.
  At `B_ij`, the ordered face triple is
  `(x_ij,x_(i-1,j+1),x_(i-1,j))`; at `W_ij` it is
  `(x_ij,x_(i,j+1),x_(i-1,j+1))`. A state `q` is the appropriate phase
  vertex of `H_2` plus one locally legal ordered triple. The simple
  bipartite graph `G` contains a compatible black-white pair once, regardless
  of how many local witnesses realize it.
- A prototile is specified by one legal seven-face corona. Writing its center
  as `a` and its cyclic neighbors as `b,d,e,f,g,c`, require the eight square
  adjacencies `c-a`, `a-e`, `b-d`, `g-f`, `g-a`, `a-d`, `c-b`, and
  `f-e` in their corresponding west-east or south-north directions. Its
  graph cycle is
  `(B(a,b,c),W(a,d,b),B(e,d,a),W(f,e,a),B(f,a,g),W(g,a,c))`,
  with the phases inherited from `C_ij`. Add the mixed-radix displacement of
  each state to the corresponding vertex of
  `((2,0),(1,3/2),(-1,3/2),(-2,0),(-1,-3/2),(1,-3/2))`.
- The four adversarial proof obligations close.
  1. Replacing every physical face by a unit regular hexagon produces a
     complete, simply connected flat polyhedral surface: three `120`-degree
     sectors meet at every vertex. Its developing map is a global Euclidean
     isometry, so the cell complex is the standard `{6,3}` honeycomb.
  2. If a physical edge has graph label `{q,r}`, either incident face cycle
     assigns `q` to one endpoint and `r` to the other. The line-graph star
     argument makes all three incident assignments agree at each physical
     vertex. A reflection swaps endpoints but cannot make a local polarity
     defect. The phase labels give a cellular local isomorphism to the finite
     phased honeycomb; its universal-cover lift has one global orientation or
     one global reflection.
  3. For distinct simple graph edges `e` and `f`, the explicit dyadic
     displacement just given makes their squared lengths different. The
     earlier nonzero-polynomial/rational-enumeration proof remains an
     alternative but is no longer needed for instantiation.
  4. Every graph edge has a globally unique length and every phased face has
     six distinct boundary edges. A congruence must preserve its cyclic length
     word up to `D_6`; consecutive graph edges reconstruct their common
     vertex, so distinct collared face cycles cannot become congruent.
- The phase argument has survived an independent fold audit. The three
  decoded graph edges at a physical vertex project to three distinct edges
  of `H_2`: if two projected to the same one, the physical corner between
  them would project to a repeated consecutive edge of a simple `C_ij`.
  Hence every vertex star maps bijectively. Two physical faces across an edge
  cannot map to the same phase face, because their other rays would violate
  this star injectivity. The regularized physical complex therefore covers
  `H_2`; being a simply connected honeycomb, it is its universal cover.
  Orientation sign is locally constant for a surface covering, so all tile
  rotations and reflections reduce to one global `D_6` frame.
- The resulting constructive theorem is exact: every nonempty strongly
  aperiodic nearest-neighbor SFT on the honeycomb face lattice has an
  effectively constructible finite protoset of unmarked strictly convex
  rational hexagons, all angles in `(pi/2,pi)`, such that every unrestricted
  all-isometry tiling decodes to the phased source system up to one global
  reflection. A geometric translation period would induce a source period.
  Existence follows by extending the bounded vertex displacement over a fixed
  triangulation; the resulting proper local homeomorphism, being at bounded
  distance from the identity, is a plane homeomorphism.
- A primary-source search through 22:55 CEST initially found no comparable
  proved shape-only strictly convex polygon compiler under all isometries and
  unrestricted contacts. A later adversarial search found a decisive
  historical announcement on page 181 of R. M. Robinson,
  *Undecidability and Nonperiodicity for Tilings of the Plane*, Inventiones
  Mathematicae 12 (1971), 177--209, DOI `10.1007/BF01418780`. Robinson states
  that he had reduced Berger's theorem to arbitrary finite sets of convex
  lattice-coordinate hexagons or pentagons even with rotations and
  reflections, but immediately says that he hoped to publish those results
  later. The 1971 paper contains no proof of that assertion, and searches of
  Robinson's publication record and citation trails have not found the
  promised later proof. This announcement kills any priority claim for
  variable-cardinality convex-polygon undecidability. The present theorem can
  be described only as an explicit effective proof or rederivation, with the
  sharper output restriction to strictly convex rational hexagons whose
  angles all exceed `pi/2` and whose entire unrestricted-contact hull decodes.
- The other nearest proved results are nonconvex:
  Demaine–Langerman's wheel/shuriken/staple compiler; Jack Stade's
  two-polygon compiler in arXiv:2506.11628, which uses a highly concave
  polyhex stick with bumps and dents plus a small regular dodecagon; the jigsawed
  `(1+epsilon+epsilon^2)` pieces in Baake–Gähler–Grimm, *Hexagonal Inflation
  Tilings and Planar Monotiles*, Symmetry 4 (2012), 581–602; and
  Yang–Zhang's seven orthogonally convex but Euclidean-nonconvex polyominoes,
  arXiv:2506.12726, which also restrict to translations. Their Problem 2
  fixes the number `k` of input polygons before asking about undecidability.
  Because this compiler's output cardinality grows with the source alphabet
  and corona language, it does not resolve that fixed-cardinality problem.
  Frettlöh–Glazyrin–Lángi,
  arXiv:1911.12752, permits finitely many irregular/T vertices in general
  normal convex-hexagon tilings; it does not defeat the direct `>pi/2` angle
  exclusion used here.
- This theorem is still not the requested result. Instantiating it on
  Kari–Culik gives a collared presentation locally derivable from a finite
  phase extension of that known symbolic hull. Strict convexity under
  unrestricted contacts is a substantive geometric frontier, but the prompt
  separately requires the complete hull to differ materially from every
  comparison hull and expressly rejects MLD/collared presentations. The
  forcing and exactness gates pass; the distinctness gate does not.
- Exact enumeration is retained in
  `workbench/kc-convex-candidate.mjs`. Replay
  `node workbench/kc-convex-candidate.mjs 2 2` for the current smallest
  winding candidate. It reports 26 source symbols, 1,136 black states,
  1,200 white states, 7,264 graph edges, and 9,912 legal coronas; all 9,912
  cycles remain distinct modulo the dihedral action. Replay
  `node workbench/kc-convex-candidate.mjs 2 2 100` for the retained deeper
  audit: it checks all 59,472 exact corner convexity/obtuseness inequalities,
  all 7,264 exact unique lengths, and a `201 by 201` window containing all
  13 base tile types. The SHA-256 certificate over the ordered scaled-integer
  coordinate enumeration is
  `96b836e8490e292ce2b94f151945752aa53d61163e82195661c0384495ac9e2b`.
  For `m=5`, the analogous command reports 24,780 noncongruent hexagons and
  certificate
  `9f8202a849d35024bb5ef883d6eb9309e04788675fda43afc7fca846e7a50249`.

### Exact impossibility for three simple-cycle hexagons

- A possible route to the explicit three-convex-polygon frontier was to avoid
  collaring: take a finite simple bipartite graph `G`, assign every graph edge
  one globally unique side length, and let exactly three prototiles be the
  convex displaced realizations of three simple 6-cycles
  `C0,C1,C2` in `G`. The line-graph proof would make any tiling a cellular
  face-map from the honeycomb to those three cycles.
- This entire class has an exact periodic-escape theorem. At any physical
  vertex with graph-edge labels `a,b,c`, the incident face corners use the
  three pairs `{a,b}`, `{b,c}`, and `{c,a}`. One simple cycle cannot supply
  two pairs because that would give it three incident edges at one graph
  vertex. Hence all three cycle types meet at every physical vertex. Taking
  an occurrence of any cycle shows that every one of its six graph vertices
  belongs to all three cycles, so the cycles share a six-element vertex set.
- At each shared vertex the three active edges have exact cycle-membership
  types `01`, `12`, and `20`. Therefore those three membership classes are
  disjoint perfect matchings `M01,M12,M20`, with
  `C0=M01 union M20`, `C1=M01 union M12`, and
  `C2=M12 union M20`. Their union is a simple 3-regular bipartite graph on six
  vertices, hence `K_3,3`; up to relabeling its three matchings are the
  standard 1-factorization.
- There is then an explicit periodic honeycomb cover. Color a dual triangular
  face `(m,n)` by `m+2n mod 3`. Write the bipartition of `K_3,3` as
  `L_p,R_p`, with matchings
  `M01={L_p R_p}`, `M12={L_p R_(p+1)}`, and
  `M20={L_p R_(p+2)}`. Map the up-vertex at `(m,n)` to
  `L_(m+2n)` and the corresponding down-vertex to
  `R_(2(m+2n)+1)`, with subscripts modulo three. Direct substitution labels
  every edge between face types `ij` by `Mij`; every type-`i` face traces
  `Ci`. Translations `(3,0)` and `(1,1)` preserve the map.
- Consequently, every nonempty three-cycle system in this carrier class has
  a doubly periodic tiling. No choice of three graph cycles or rational vertex
  displacements can yield the requested aperiodic triple. This is a bounded
  negative theorem about one construction class, not a qualifying
  certification method for the broader task.
- Closest marked-hexagon literature does not evade the stated model:
  Socolar–Taylor, arXiv:1003.4279, needs both stripe continuation and a
  next-nearest flag rule; Walton–Whittaker, arXiv:1907.10139, uses
  orientation/charge-sensitive rules; and Baake–Gähler–Grimm's
  hexagonal-inflation family uses decorations or nonconvex key pieces.

### Extension of the periodic-escape theorem to four cycles

- The same conclusion holds for exactly four selected simple 6-cycles. Assume
  all four types occur, since otherwise the three-cycle theorem applies. Every
  active graph vertex belongs to exactly three or four cycles. Compatibility
  of the incident corner pairs makes the active graph cubic even in the
  four-cycle case: a fourth corner at a vertex must duplicate one of the three
  pairs formed by the same three incident graph edges.
- If `n3,n4` count graph vertices lying on three and four cycles, cycle
  incidence gives `3*n3+4*n4=24`. A cubic bipartite graph has an even number
  of vertices, leaving only `(n3,n4)=(8,0)` or `(0,6)`; the algebraic solution
  `(4,3)` has seven vertices and is impossible.
- In the `(8,0)` case every active graph edge lies in two cycles. Attaching
  the four hexagonal faces along their graph edges produces a closed surface
  with `V=8,E=12,F=4` and Euler characteristic zero. Its vertex links are
  triangles, so it is a torus or Klein bottle and its universal honeycomb
  cover is doubly periodic. The original tiling certifies that the three
  actual polygon corners assigned to each graph vertex sum to `2*pi`, so the
  compact flat surface and its Euclidean development use the actual shapes,
  not just their side words.
- In the `(0,6)` case the active graph is `K_3,3` and every cycle is
  Hamiltonian. The complement `Ni` of each cycle is a perfect matching. At
  every vertex the four corners use the three possible edge pairs with one
  repeated, so the multiset `N0+N1+N2+N3` is all of `K_3,3` plus one perfect
  matching `D`. Normalize `D` to the identity permutation. If `x,y,z` count
  identity, transposition, and 3-cycle matchings among the four `Ni`, the
  trace and count equations are `3x+y=6` and `x+y+z=4`, giving
  `(x,y,z)=(1,3,0)` or `(2,0,2)`. Either multiset contains a full
  1-factorization; the complementary three face cycles are the canonical
  three-cycle system and have its explicit periodic cover. If the selected
  factorization chooses either copy of a duplicated corner, both have equal
  angle because each occurs in an original vertex star with the same two
  other corners.
- Thus no nonempty system with at most four selected simple bipartite
  6-cycles is strongly aperiodic. The first possible native compression in
  this carrier has at least five prototiles.
- Literature anchor: Leão–Barbosa, *6-cycle double covers of cubic graphs*,
  arXiv:cs/0505088v4, gives the standard `6-CDC` language, proves that three
  cover cycles through every cubic vertex, classifies the three-cycle case,
  and relates girth-six instances to hexagonal torus/Klein-bottle tilings. It
  does not state the all-isometry polygon escape above; the additional step
  here is the reduction of every at-most-four-cycle carrier to one of the two
  compact flat quotients and the development using the actual corner angles.

## Nonhierarchical global obstruction

### Model

- Target: a finite unmarked polygon set whose aperiodicity follows from a
  global conserved quantity, orientation cocycle, incommensurate flux, or
  another mechanism not equivalent to a recognizable hierarchy.
- All isometries and unrestricted contacts remain allowed.

### Current state

- Repository mechanisms already excluded as substantive novelty for this
  route: chair and triangle substitutions, Conway–Radin pinwheel substitution,
  Robinson/Penrose triangles, Maloney oddfold rhomb substitutions, and
  de Bruijn/cut-and-project rhomb families (`ferniquilt`, `pontiquilt`,
  `starpoint`, and `subrisa`).
- A local additive invariant alone cannot force aperiodicity unless geometry
  also excludes zero-flux periodic assemblies. The first adversarial test for
  every proposal is therefore a reflected fundamental domain with cancelling
  invariant.
- No exact candidate has yet survived this test.

### Kari–Culik logarithmic winding cover: provisional distinctness repair

- A natural finite skew extension may repair the convex compiler's MLD
  failure. Let `K` be the 13-tile Kari–Culik SFT and choose a prime `m`. Its rows
  have a locally determined multiplier `lambda` in `{2,1/3}`. Give every base
  tile a sheet `r in Z/m`, require `r` to be constant across a row, and set
  the sheet above the tile to `r+w`, where `w=0` on multiplier-`2` rows and
  `w=1` on multiplier-`1/3` rows. This is a nearest-neighbor Wang SFT
  `K^(m)` with `13m` tile symbols: append `r` to both horizontal edge colors,
  append `r` to the south color, and append `r+w` to the north color.
- In `(S,W,N,E)` order the exact division tiles are
  `(1,0/3,0,1/3)`, `(1,1/3,0,2/3)`, `(1,2/3,1,0/3)`,
  `(2,0/3,0,2/3)`, `(2,1/3,1,0/3)`, and
  `(2,2/3,1,1/3)`. The doubling tiles are
  `(0,-1,0',-1)`, `(0,0,0',0)`, `(0,0,1,-1)`,
  `(1,-1,1,0)`, `(1,-1,2,-1)`, `(1,0,2,0)`, and
  `(0',0,1,-1)`; `0` and `0'` are distinct colors. Every tuple satisfies
  `lambda*S+W=N+E` after forgetting the prime.
- Every Kari–Culik configuration has exactly `m` lifts, obtained by choosing
  one row sheet and propagating it vertically. Thus `K^(m)` is nonempty.
  Projection to `K` is local, so every translational period upstairs would
  give one downstairs; the extension is strongly aperiodic. Its relative
  entropy is zero and it retains Kari–Culik's positive entropy and
  nonhierarchical multiplier dynamics.
- The cover is tied to the intrinsic logarithmic winding rather than a free
  site decoration. If `alpha` is the row average, put
  `u=(log(alpha)+log(3))/log(6)` and
  `theta=log(2)/log(6)`. The Kari–Culik row map satisfies
  `u_(j+1)=u_j+theta-w_j mod 1`; therefore
  `z=u+r in R/(mZ)` satisfies the lifted irrational rotation
  `z_(j+1)=z_j+theta`. The proposed invariant is the new vertical
  eigenvalue `exp(2*pi*i*theta/m)` on the connected `m`-fold logarithmic
  cover. Choosing `m` coprime to six is intended to rule out roots already
  present in the phase solenoid.
- The cocycle is not a split free decoration. The locally visible row-type
  factor is the generalized Sturmian shift `M_theta`. Its discrepancy
  satisfies `|sum_(j=0)^(n-1)c_j-n*theta|<=1`, so Gottschalk–Hedlund gives a
  continuous transfer `h` with `h after shift-h=c_0-theta`. Thus
  `F_m(x,r)=exp(2*pi*i*(r-h(c(x)))/m)` is invariant under horizontal shift
  and has vertical eigenvalue `exp(2*pi*i*theta/m)`. If `c` were a
  `Z/m` coboundary of radius `R`, a generic mechanical word and a sufficiently
  large continued-fraction return `q_k` would agree on the radius-`R`
  window while its cocycle sum is `p_k`. Consecutive `p_k` are coprime, so
  infinitely many are nonzero modulo prime `m`, contradicting a coboundary
  return sum.
- The complete invariant can be proved without the unjustified claim that
  every horizontal-invariant function factors through the row-average
  circle. Define `E_h^x(X)` as the vertical `mu` for which a continuous
  circle-valued `F` obeys `F after T=F` and `F after S=mu*F`. Circle-valued is
  essential: restriction to a closed invariant core never vanishes.
  Durand–Gamard–Grandjean's existence of every row average and the multiplier
  identity show that the local type factor `c(X)` lies in `M_theta`.
  Siefken's closed minimal core maps nontrivially into the minimal Sturmian
  shift, so its image, and therefore `c(X)`, is all of `M_theta`.
- For the upper bound, take an irrational continuity point of Siefken's
  coding in the lifted core. Given any sequence `q_j` with
  `q_j*theta mod m -> 0`, choose `p_j in m*Z` with
  `q_j*theta-p_j -> 0`. Away from the coding boundary the wrap count over
  `q_j` rows is eventually exactly `p_j`, so the lifted sheet returns.
  Siefken's horizontal-density argument supplies shifts `a_j` for which
  `T^(a_j) S^(q_j)y -> y`. Any `mu in E_h^x` then has
  `mu^(q_j)->1`. Thus the homomorphism on the dense subgroup
  `q*theta mod m -> mu^q` is continuous and extends to a character of
  `R/(mZ)`. Its characters give the upper bound
  `mu=exp(2*pi*i*k*theta/m)`, and powers of the explicit `F_m` give equality.
  Consequently
  `E_h^x(K^(m))={exp(2*pi*i*k*theta/m): k in Z}`. Equality for indices
  `m,n` forces both `m|n` and `n|m`, hence `m=n`.
- The upper-bound quantifier is essential: the return conclusion is required
  for every integer sequence `q_j` with `q_j*theta/m -> 0 mod 1`, not merely
  for one continued-fraction sequence. More explicitly, write
  `q_j*theta=m*p_j+delta_j`, with `delta_j->0`, at an irrational continuity
  point whose log coordinate is off the coding cut. The exact wrap sum is
  eventually `m*p_j`, so the sheet returns. The shifted solenoid phase may be
  arbitrary, but Siefken's Proposition 15 supplies horizontal corrections
  because the returning row slope is irrational; continuity only at the
  target point then gives the required recurrence. This controlled-return
  argument replaces the invalid shortcut that horizontal-invariant functions
  simply factor through row averages.
- `K^(m)` is a zero-dimensional SFT, not a connected topological cover. The
  connected object is its maximal equicontinuous circle factor
  `R/(mZ)`, on which vertical motion is rotation by `theta`; the finite
  cocycle is non-split because its eigenvalue group contains
  `exp(2*pi*i*theta/m)` rather than only the base eigenvalues.
- The full joint spectrum can also be closed. At an irrational continuity
  point of Siefken's coding, a horizontal eigenvalue `lambda` must satisfy
  `lambda=exp(2*pi*i*q*alpha)` for a character
  `q in Z[1/6]` of the 6-adic solenoid. This relation holds over an
  uncountable set of irrational row parameters. For fixed nontrivial
  `lambda`, the union over the countable nonzero character group of its
  solution sets is countable, a contradiction. Hence every joint eigenvalue
  has trivial horizontal coordinate. Fourier decomposition over the
  `(Z/2)^2` phase then gives exactly
  `{((-1)^e,(-1)^d*exp(2*pi*i*k*theta/m))}`.
- Let `a=(-3,3/2), b=(0,3)` be the affine face-center lattice and `a*,b*`
  its dual basis. The fixed-frame suspension eigenmodule is
  `M_m=(1/2 Z)a*+(1/2 Z+(theta/m)Z)b*`.
  Ordinary fixed-vector eigenfunctions disappear on the union of all global
  rotations, so use a relative eigenfield: a continuous translation-invariant
  covector `kappa(T)` and circle function `f` with
  `f(T-t)=exp(2*pi*i*kappa(T).t)f(T)`. Every tile has six distinct lengths and
  every tiling has one common, locally decoded frame `R(T)`, so
  `kappa(T)=R(T)k` extends each `k in M_m` over the complete hull.
  Translation conjugacies preserve these fields.
- If `X(P_m)` and `X(P_n)` were translation conjugate, restriction to the
  lifted Siefken minimal core would give an orthogonal `A` with
  `A M_n subset M_m`; the inverse gives the reverse inclusion with another
  orthogonal map. The closure of `M_m` is a union of parallel `b*`-lines,
  forcing `A b*=+/-b*`, and then
  `(1/2 Z+(theta/n)Z) subset (1/2 Z+(theta/m)Z)`.
  Irrationality forces `n|m`; the inverse forces `m|n`; hence `m=n`.
- The exact infinite point used for implementation takes
  `alpha_0=sqrt(2)`, `alpha_(j+1)=2*alpha_j` for `alpha_j<1` and
  `alpha_j/3` otherwise, and all phases `t_j=0`. At column `n`, let
  `A_j(n)=floor(n*alpha_j)`. The row-`j` tile has
  `S=A_j(n)-A_j(n-1)`,
  `N=A_(j+1)(n)-A_(j+1)(n-1)`,
  `W=lambda*A_j(n-1)-A_(j+1)(n-1)`, and
  `E=lambda*A_j(n)-A_(j+1)(n)`, with the published `0'` convention.
  Floors are decided by integer square roots, so no floating-point decision
  enters. `workbench/kc-convex-candidate.mjs` checks this point against the
  exact 13-tile list and checks the lifted edge matches.
- Primary-source boundary now includes Culik,
  *An aperiodic set of 13 Wang tiles*, Discrete Mathematics 160 (1996),
  DOI `10.1016/S0012-365X(96)00118-5`; Durand–Gamard–Grandjean,
  *Aperiodic tilings and entropy*, arXiv:1312.4126 / TCS 2017; and Siefken,
  *The minimal subsystem of the Kari–Culik tilings*, arXiv:1410.1572.
  Queries for Kari–Culik cyclic extensions, logarithmic covers, winding
  covers, and finite cocycles found Siefken's base skew-product model but no
  finite cover family.
- This route has passed the exactness, forcing, family-distinctness, and
  preliminary novelty screens. The defensible result is joint: an explicit
  all-obtuse strictly convex full-hull compiler, plus a non-split
  invariant-changing family. Demaine–Langerman's universal nonconvex compiler
  can also be instantiated on `K^(m)`, and that same-source output is expected
  to be locally equivalent. The novelty claim is therefore the convex
  all-obtuse output theorem and its complete unrestricted-contact proof, not
  a claim that the source dynamics has no concave geometric presentation.

### Resume point

Formalize the accepted joint theorem, implement `P_2` with the audited
`m=3,5` family choices, and keep the same-source concave-compiler limitation
explicit.

## Rational-coordinate polyforms and bounded exact certification

### Exact search model under consideration

- Candidate tiles: simply connected unions of unit lattice cells, represented
  by canonical finite cell sets.
- Isometries: the full dihedral group of the square lattice.
- Contact model: arbitrary polygon contacts in the plane; any lattice
  exact-cover computation is only a submodel until a theorem forces all
  tilings onto the lattice.
- Potential finite domain: enumerate small polyforms and search for periodic
  lattice witnesses and locally forced coronas before selecting a named
  bounded class.

### Current state

- The repository already contains exact finite rectangle-inventory cover
  enumeration through `rectipelago` and `or-tools-wasm@^0.9.1`. This is useful
  for bounded experiments but is neither an aperiodicity decision procedure
  nor a result.
- Existing repository polyform/packing hulls (`chair`, `rectipelago`, and
  dominoes) have obvious periodic components and are exclusion examples.
- A finite failure to find a periodic torus is not a certificate of
  aperiodicity. A qualifying method route must state and prove a completeness
  bound for a named class.

### Resume point

Before writing a search program, identify a class for which non-lattice
contacts and period size admit proved finite bounds. Otherwise use bounded
enumeration only to falsify proposed candidates and retain explicit periodic
witnesses.

## Geometric compilation with a substantive restriction

### Model

- Symbolic rules may be internal, but final tiles must be unmarked simple
  polygons and bare geometry must force all legal tilings.
- A routine jigsaw compilation is excluded. A route is worth retaining only
  if it proves an additional frontier such as exact rational coordinates, a
  named polyform class, bounded corona recognition, or a materially different
  complete hull.

### Current state

- Erik D. Demaine and Stefan Langerman, *Tiling with Three Polygons is
  Undecidable*, arXiv:2409.11582 (2024), supplies a much stronger published
  compiler than the elementary jigsaw routes initially screened. Lemma 2.2
  converts a translation-only Wang set into signed free Wang tiles while
  preserving tilings up to a global isometry and while allowing reflected
  copies. The geometric construction uses exactly three unmarked simple
  polygons (wheel, shuriken, and staple). Lemma 3.5 classifies every
  unrestricted polygon tiling as a square grid of wheels that decodes to a
  source Wang tiling; its proof explicitly covers rotations, reflections,
  partial contacts, and alternative assemblies. The construction uses
  `alpha = 3*pi/8`, `beta = 7*pi/16`, and clean angles supplied by a regular
  `4n`-gon, so its coordinates and edge lengths have exact constant-degree
  algebraic descriptions.
- Instantiating that theorem with the 13 Kari–Culik Wang tiles gives a
  nonempty three-simple-polygon protoset with all isometries and unrestricted
  contacts. Durand, Gamard, and Grandjean, arXiv:1312.4126, prove that the
  Kari–Culik shift has positive entropy. A translational period of a compiled
  polygon tiling would preserve the forced wheel grid and descend to a
  translational period of its decoded Kari–Culik tiling, so the compiled
  protoset is strongly aperiodic and nonhierarchical in the source-dynamical
  sense.
- This is nevertheless not a discovery under the task definition. It is the
  direct advertised use of a published arbitrary-Wang-set geometric compiler.
  The forced fillers and wheel grid make the geometric hull a finite,
  locally recognizable presentation of the Kari–Culik hull, so it advances
  no hull invariant beyond the known source. The prompt expressly excludes a
  routine geometric encoding and any merely MLD/collared presentation of an
  audited comparison hull. “The corollary was not explicitly named in the
  searched papers” is not a substantive novelty argument.
- The SoCG 2025 paper makes the priority failure decisive: its Figure 1
  explicitly uses the strongly aperiodic 11-tile Jeandel–Rao set, and its
  Figure 6 explicitly displays the resulting three polygons. A strongly
  aperiodic three-simple-polygon instance is therefore already the paper's
  worked output, not merely an unstated corollary. Substituting Kari–Culik
  changes the inherited entropy but not the geometric construction.
- Exact literature queries used to check whether the direct corollary had
  already been named were `"Kari-Culik" "Tiling with Three Polygons"`,
  `"positive entropy" "three polygons" aperiodic tiling`, and
  `"nonhierarchical" polygon protoset aperiodic`. No named construction was
  found in that boundary, but this negative search does not cure the
  mechanical-compilation disqualification.
- The central required lemma is stronger than faithful simulation of one
  intended assembly: every geometric contact, reflected tile, partial-edge
  contact, and alternative component must decode to the symbolic system.

### Resume point

Do not instantiate the Demaine–Langerman compiler in product code. Resume this
route only if a change creates a proved substantive frontier not inherited
from a chosen Wang shift—for example a convex or rational-coordinate output
class, or a genuinely new complete-hull invariant that is not an arbitrary
symbolic product. Independently, try to decide the finite flag-cycle condition
in the collared convex carrier; success there still requires a non-MLD source
or output before promotion.
