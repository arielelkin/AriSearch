# Fresh hostile review: universal pentagon rigidity and private-octagon periods

**Verdict: VALID.** The reviewer did not propose or author the reviewed
new lemma. The exact source is
`research/lemmas/private-octagon-adjacent-corner-rigidity.md`, including
its subsequent universal repeated-length strengthening. This approval is
independent of the author's review of the earlier weaker escape theorem.

## Reviewed claims and exact scope

1. Every genuine convex equiangular108 pentagon has adjacent-corner placement
   rigidity under all isometries: two whole incident sides and their interior
   wedge determine its actual polygon subset uniquely.
2. Any repeated native length forces an actual reflection. Nonregular
   reflection words are (a,b,c,b,a), c=phi*a-b/phi, with three distinct values.
3. For ANY such pentagon P and a genuine convex octagon Q having two
   nonadjacent108 corners and six144 corners, two distinct length values
   each unique on Q and absent from P force a nonzero period in EVERY
   original admitted tiling. The remaining Q sides are unrestricted.

No source compiler, saturation limit, exact search, periodic metric existence,
rank-two period or original-problem resolution is asserted.

## Universal repeated-length algebra

The key quantifier is arbitrary positive real lengths, not rational or
algebraic lengths. Let w=exp(2pi*i/5), and write the closed walk
v_(h+1)-v_h=L_h*w^h. Conjugating its zero closure and multiplying by
w^(i+j) proves that the rho-permuted length vector also closes, where
rho(h)=i+j-h mod5. This involution swaps the prescribed equal pair i,j,
one other pair p,q, and fixes one index. Subtraction leaves exactly
(L_p-L_q)(w^p-w^q)=0, so L_p=L_q. No independence of all five root
powers, number-field restriction on L, or unjustified rational coefficient
comparison occurs.

An explicit actual polygon reflection is available, which removes any
possible ambiguity between a palindromic length vector and a geometric
symmetry. With indices modulo5, set s=i+j and

    r(x)=-w^s*conjugate(x)+v_(s+1).

The now invariant length word gives

    r(v_h)=v_(s+1-h).

The linear part has unit modulus and reverses orientation; the displayed
vertex permutation is an involution. Thus r is an actual reflection of
P. In particular the minus sign in the geometric edge reversal is required;
the zero-closure permutation formula alone should not be mistaken for
this explicit geometric map. The source's walk argument has the correct
orientation-reversing conclusion and contains no defect.

As a supplementary independent check, the reviewer encoded the two real
closure rows in Q(zeta20). For every one of the ten unordered i,j pairs,
adding L_i=L_j gives rank3 and a two-dimensional real kernel; the other
equality is already in its row span. The explicit reflected-walk formula
above was verified on that entire kernel basis. This is exact linear
algebra over the full length space, not a metric sample.

```text
conda run --no-capture-output -n arisearch python research/reviews/verify_private_octagon_pentagon_rigidity.py
```

The replay passed all ten cases. The analytic proof does not require this
computation, whose domain is retained only as an audit check.

## Corner placement, including repeated lengths

Five distinct lengths identify both native sides and their common vertex.
Three noncollinear endpoints fix the placement, with reflected placements
included. In the nonregular reflection word (a,b,c,b,a), closure makes
any equality among a,b,c imply all equal, so the only pair types are
(a,a), two(a,b), and two(b,c). The repeated corner choices are exactly
orbits of the actual reflection. Exchanging the equal segments at (a,a)
is that same reflection. Thus every labeled ambiguity is already a symmetry
of the geometric subset. Regular pentagon dihedral symmetries likewise
identify all corner/assignment choices. There is no surviving accidental
repeated-length branch.

The converse classification's distance-one/distance-two five-cycle argument
is valid: placing two native corners on the same wedge gives a genuine
nonidentity self-isometry. A nontrivial orientation-preserving symmetry
of a pentagon forces order5 and regularity; an orientation-reversing
symmetry of a compact polygon is a reflection. There is no omitted
repeated-length or reflection case.

## Original-tiling chains and period transfer

The independently reviewed all-obtuse theorem supplies full native-side
contacts and trivalent vertices. The sole angle star is108+108+144, so
no two144 sectors may meet. Unique private Q side matching excludes
144/144 sides; nonadjacent108 corners exclude108/108 sides. A private
108/144 mate must exchange its endpoints. The two endpoint-exchanging
isometries are the midpoint half-turn and perpendicular-bisector
reflection; the latter preserves the interior supporting half-plane
and overlaps. Thus every selected private mate is exactly the half-turn,
including arbitrary reflected initial Q copies.

The two selected contacts give degree2 chains even when other Q-Q seams
occur. Open midpoint chords lie in tile interiors, and the half-turns
extend them to complete straight lines with fixed two-step period magnitude.
Distinct chain lines cannot cross either in open chord interiors or at
native-side midpoints, where exactly the two same-chain tiles occur.
Consequently all chains are parallel, and congruence fixes their periods
to the two signs of one common nonzero vector. The ENTIRE Q occurrence
set is invariant under both signs. No exceptional-density count or
unproved finite-state synchronization is used.

A P has at most two nonadjacent P-neighbor sides, hence at least three Q
neighbors and a consecutive Q-neighbor pair. Its PQQ corner supplies the
two whole P sides, wedge and location required by universal rigidity.
Translation of the two actual Q tiles preserves this data. If the third
tile at the translated residual108 sector were Q, Q-set invariance under
the opposite translation would pull a positive Q corner sector into the
original P interior. That is a real overlap, even when the third Q has
an108 corner. Thus the third tile is P, and universal corner rigidity
makes it precisely the translated P. Applying both period signs proves
set equality. This argument works in every original tiling and permits
extra Q-Q contacts; it does not secretly use the defect-free chain limit.

## Attacks, repairs and remaining uncertainty

I attacked irrational/transcendental native lengths, adjacent equal sides,
nonadjacent equal sides, accidental fourth/fifth length values in a
reflection word, different native corner placements, the geometric versus
closure reflection sign, glide reflections, reflected private mates,
additional Q-Q contacts, crossed chain axes, and a Q filling the translated
residual sector. Each is handled by an exact identity or an explicit
geometric hypothesis. No repair is needed and no mathematical uncertainty
remains in the stated theorem. The author should reconcile the source's
pending-review status with this independent verdict.

Repeated private Q values, loss of uniqueness/absence from P, only one
private side, adjacent108 Q corners and different angular families remain
outside the theorem. The unrestricted aperiodic-pair objective remains
unresolved, with no novelty claim made here.
