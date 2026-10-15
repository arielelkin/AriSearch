# Fresh direction advice: 09:00 UTC cycle, 2026-10-15

Status: concrete research recommendation and one new internally proved lemma;
not a main-problem solution. This advisory was delivered after the originally
scheduled adviser failed to start. No discovery log or verification registry
was modified. Read: research-problem.md, research-protocol.md, current
mechanism registry and Y closure, all three six/five hexagon proofs, intrinsic
determinism, and the three-sector fractional construction's area obstruction.
The root reports that all three six/five components have now passed review.

## Immediate structural result, before another census

The accompanying author proof is
[hexagon-six-distinct-three-shared-periodicity-2026-10-15.md](../lemmas/hexagon-six-distinct-three-shared-periodicity-2026-10-15.md).
Fresh independent hostile review has been requested through the root.
It derives periodic escape when A has six distinct side lengths and at most
three lengths are shared with B. Its new mechanism is the actual full
AA-seam involution, not enlarged support enumeration:

1. A-private sides are isolated, so at least three lengths must be shared
   in a mixed defect-free tiling.
2. At exactly three, A alternates shared/private. All vertices become AAB,
   all B sides AB, and exact incidence balance forces B to have exactly the
   three shared lengths, each twice.
3. A B-side's two endpoints must use the two different private arms adjacent
   to A's unique corresponding side. This corona rule forces only
   B=xyzxyz or B=xxy zzy, up to cyclic symmetry and label renaming.
4. The first B is centrally symmetric. In the second case A's three private
   neighbor maps are two midpoint half-turns and one side-line reflection.
   The private AA graph is connected because the six As around every B
   form an AA cycle. Isometries between A copies propagate globally;
   complement components recover B, and a discrete cocompact symmetry group
   supplies a rank-two translation lattice.

The root supplied the simpler connected-AA propagation while the artifact
was being written. It avoids the global-indexing issue caused by B symmetry.
This proof is not promoted here before the independent reviewer returns.
If valid, together with the six/five theorem it leaves only A-six/B-four
with ALL FOUR B lengths shared in the one-six-distinct hexagon domain.
This does not address the both-repeated hexagon domain or pentagon pairs.

## Next invariant for the remaining A-six/B-four domain

Normalize the two private A slots to u,v. They are isolated, so the two
cyclic patterns, up to reversal and rotation, are

    A=(u,x,v,y,z,t) or A=(u,x,y,v,z,t),

where x,y,z,t are the four shared values. B uses exactly those four values,
with multiplicity partition (3,1,1,1) or (2,2,1,1).

The same signed seam law gives a NEW forced periodic skeleton. A reflected
private AA seam needs B loops at BOTH DISTINCT shared labels flanking that
private slot. Unless B has two different loop labels, every private seam
is therefore a midpoint half-turn. This includes all (3,1,1,1) B words and
all (2,2,1,1) words except those with both equal pairs adjacent.

In the forced half-turn domain, the private AA graph has degree two.
Alternating its u,v steps composes to the nonzero translation

    T_A = 2(m_v-m_u),

where m_u,m_v are the native side midpoints. Hence its components are
bi-infinite periodic A chains; finite cycles would contradict this nonzero
translation and disjoint interiors. In a placed chain the vector is the
linear placement image of T_A, up to sign. This is a real geometric period
of the A chain, not a bound on a symbolic state graph.

**Exact next object:** for each occurring B native corona, record the placed
chain vectors of all incident As and the endpoint maps relating them. Seek
a proof that all these vectors coincide up to sign, or an explicit corona
showing they need not. Use the two full AA-seam endpoints; mere compatible
corner triples are insufficient. For the exceptional double-loop B words,
record exactly which private slot can reflect and whether both signs can
occur. This isolates the genuinely new holonomy branch.

**Decisive gates:**

- If a B bridge forces a common nonzero vector for every A chain, prove
  propagation through the full adjacency graph. Then audit B-B components:
  periodicity of the A union alone does not imply periodicity of its B
  filling. Either prove that filling is uniquely determined or construct
  an explicit periodic filling with matched links.
- If a corona permits incompatible chain directions, preserve that exact
  counterexample to the proposed invariant. Do not treat its local legality
  as plane existence, and do not expand quotient sizes on that basis.
- The root has authorized a bounded A-six/B-four support gate. Its value is
  to extract a universal periodic witness or a precise obstruction to this
  skeleton argument; a count of surviving supports is not the research goal.

Do not claim that a finite local rule, a degree-two chain, or an apparent
strip independently gives a global periodic tiling. The earlier strip theorem
requires complete reusable boundary states, which are not established here.

## Root follow-up: periodic strip filling is the decisive next lemma

After the initial recommendation the root proposed a stronger route for
fixed AA endpoint modes. This deserves a proof attempt before expanding a
support census. It is not established by the present advisory.

For two half-turn modes every private AA chain has the same intrinsic
period vector T_A up to its placed orthogonal map. Choose in each chain a
proper path through A interiors and private-side midpoints, staying bounded
distance from the period axis. Two nonparallel such proper paths must
intersect topologically, contradicting disjoint A interiors and the fact
that shared private edges join the same graph component. Proving this
carefully would force all chain axes parallel. Equal period norms then
make the common plane period T the same up to sign, so the ENTIRE A union
is T-invariant.

The remaining B filling need not be unique or itself periodic. If B tiles
alone, the monohedral hexagon theorem already gives a periodic escape.
Otherwise the reviewed uniform-density theorem makes A syndetic in every
admitted tiling, and consequently bounds all gaps between chain barriers.
A B tile in such a bounded-width gap can be connected to a chosen boundary
chain by a uniformly bounded number K of full-side steps: use a bounded
connecting disk and the uniform diameter/inradius packing bound. Each
step has finitely many native side/endpoint choices. This derives finitely
many exact B placements modulo T, rather than assuming finitely many
absolute orientations. The number of possibilities has a uniform bound.

Once candidate placements are finite modulo T, encode overlap and coverage
on the finite polygonal arrangement in a T-slab. A finite memory of adjacent
slabs gives a one-dimensional finite-state language. The given filling
makes this language nonempty, so some directed cycle gives a periodic B
filling for this gap. A uniform state-count bound M would allow all gaps
to use the common period lcm(1,...,M)*T, even when their chosen cycles differ.
This constructs a periodic escape rather than proving the original filling
periodic.

Required hostile-review points: proper barrier separation and bounded gap
width; anchoring ALL B components to a periodic boundary by bounded full-side
paths; exact finite coverage encoding, including tiles straddling slab cuts;
T-invariance of each unbounded gap rather than only of their union; and
separate treatment of bounded complement cavities that T may permute. A
bounded cavity orbit may be filled by translated copies of one retained
filling. No generic strip theorem may silently supply these hypotheses.

The same mechanism may apply when one private mode is a fixed half-turn
and the other a fixed reflection: their product is a glide reflection, with
nonzero glide because the other side midpoint is strictly off the reflected
side's supporting line; squaring gives a four-tile chain period. Both private
slots cannot reflect in A-six/B-four: their flank pairs collectively contain
at least three distinct shared values, while B has at most two loop labels.
A mode that genuinely branches along one private slot remains outside this
fixed-mode argument.

## One genuinely changed construction topology, if resources permit

The new three-sector construction is now closed when both source species
own the identical count vector (P,H)=(2,6) and mark-local transfers cancel.
A concrete topological escape is available before any coordinate search:
retain the thin-source topology, but SPLIT EACH OF THE TWO THICK-SOURCE
HEXAGONAL CAPS into two pentagons by a chord joining interior points of
opposite cap edges. A strictly convex hexagon cut this way gives two genuine
convex pentagons: each boundary path has four edges, plus the chord.
Use the source-arrow orientation to index the six cap rays, then always cut
between cap edges 0 and 3. The cuts lie inside existing caps, so they define
a repeatable global partition and cannot create gaps between source cells.

The source count vectors become

    thin:  (2 pentagons, 6 hexagons),
    thick: (6 pentagons, 4 hexagons).

They are independent. If the mark-local transfer cancellation is retained,
write a for the thin-rhomb area and phi=(1+sqrt(5))/2. Two common output areas
would satisfy

    2P+6H=a,    6P+4H=phi*a,
    P=(3phi-2)*a/14,    H=(3-phi)*a/14.

Both are strictly positive. Thus the old equal-count area contradiction no
longer applies. If changing the cap cuts makes transferred slices depend on
source type, replace these equations by the exact incoming-minus-outgoing
area identities; do not silently retain cancellation.

**First finite gate:** spell out the cap edge indices and all new piece
boundary words in the four source-type/role cases. Derive whether a cap
split can have two congruent pentagonal children while those children are
also congruent to the receiving pentagons, and the remaining caps congruent
to the receiving hexagons. Equal areas are only necessary. The old tiny-cap
fixture fails these size equalities and is merely a proof that the changed
partition topology is geometrically nonempty. Do not run a metric census
until an exact identity or low-dimensional algebraic family survives this
boundary/congruence gate.

**Stop conditions:** an exact congruence contradiction closes this specified
cap-split scheme; a two-class fixture without a periodic-omission attack and
universal intrinsic decoder remains a construction candidate only. Preserving
a marked Ammann source partition does not itself impose source markings on
unmarked output tiles. This direction is independent of the hexagon theorem,
but there is no evidence yet that it will survive its first congruence gate.

## The 1982 two-size pentagon lead

I inspected the original Danzer–Grünbaum–Shephard paper, printed pp.569–570,
especially Figure 3. The paper describes a plane tiling using two sizes of
mutually similar affinely regular pentagons. The diagram visibly repeats a
four-pentagon hexagonal motif; exact coordinates and a period certificate
have not been recovered in this advisory.
[Primary PDF](https://faculty.washington.edu/moishe/branko/BG136.Tiles.with.5-foldSymm.pdf).

One bounded recovery of that fixture is worthwhile as a positive existence
and periodic-escape calibration. Its published existence is not new, and
its apparent periodic motif supplies no new hierarchy. Prefer the changed
cap-split incidence above for an independent construction experiment unless
exact recovery reveals a specific deformable interface with a new forcing
mechanism. Do not frame this old tiling as a candidate aperiodic pair.

## Relation to the full target

Even closing all A-six/B-four cases would leave pairs of two repeated-side
hexagons and all surviving pentagon-containing domains. The present strategy
therefore keeps one positive construction mechanism separate from the
structural theorem. Neither the current family exclusions nor the new
periodic skeleton is a complete impossibility proof. The full unrestricted
two-convex-polygon problem remains unresolved.
