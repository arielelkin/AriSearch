# Fresh hostile review of the three-angle periodic pentagon family

**Reviewed claim:** the positive Y/Y construction in
[new-angle-three-pentagon-private-length-counterexample.md](../lemmas/new-angle-three-pentagon-private-length-counterexample.md)
forms a genuine whole-plane periodic pair tiling for90<theta<135 degrees,
with the stated positive length coefficients and all t,s>0. In particular,
the exact theta105 and cos(theta)=-2/5 instances with t=1,s=sqrt5 are
noncongruent convex pentagon pairs with mixed doubly periodic tilings.
The latter has irrational theta/pi, irrational private side-length ratio,
and irrational polygon-area ratio.

**Reviewer:** root, independent of the construction agent. Root proposed an
irrational-angle stress test after receiving the105 construction, but did
not develop the general coefficients, side lengths, coordinate definition,
seam table or proof. The checker does not import the author's scripts.

**Verdict:** valid for the positive periodic family and both exact instances.
No mathematical proof repair was needed. The separate bounded X/Y mixed-word
967680-case claim is outside this review and has another fresh reviewer.

## Geometry and angle audit

I independently substituted a=h,b=(1-2k^2)/(2k),c=h/(2k) into both closure
pairs and used only h^2+k^2=1 to obtain zero. For0<k<sqrt2/2, all coefficients
and all lengths are positive. The five unit directions wind once with all
successive turns strictly between0 andpi. The source's side-height argument
therefore proves convexity for the continuum: relative heights increase on
the positive transverse semicircle, then decrease to closure, staying
strictly positive at nonincident vertices. Maximum angular gap belowpi
ensures a positive ascent and a negative final descent for every side.
This supplies global supporting-side convexity, rather than merely local
positive turns.

The fresh [exact verifier](verify_three_angle_pentagon_periodic_independent.py)
uses Sage's exact real algebraic field AA, independently derives all side
vectors, and verifies every nonincident vertex against every supporting
line. It checks closure, squared lengths and actual native-angle cosines,
including both right angles and gamma. The saved radical coefficient
coordinates and side lengths are decoded independently and compared exactly.
No tolerance or floating-point equality decision is used.

For both concrete instances all six numerical labels are distinct and the
private length1 is absent from Q while sqrt5 is absent from P. Thus the
side-length multisets differ, proving noncongruence. Irrational private
lengths do not force a one-dimensional rational grid.

## Actual quotient links and direct planar tiling

The ten actual whole-side pairs use every side slot once with equal length.
All face references are counterclockwise and each seam reverses endpoint
order, making the quotient orientable. I used a corner-successor permutation,
not the author's endpoint union-find, and found exactly two4-cycles and four
3-cycles. Their angle sums are identically2pi as formal coefficients of pi
and theta. Face adjacency is connected and6-10+4=0. Thus the compact flat
surface argument has its full local manifold and no-cone hypotheses.

The verifier additionally develops a dual spanning tree by actual relative
plane isometries. Every residual seam holonomy has identity linear part.
It finds a rank-two translation basis with determinant equal in absolute
value to the area of the four placed whole faces, and confirms all seam
periods are integer combinations of that basis. Exact lattice-coordinate
bounding boxes give a finite complete overlap domain:52 polygon comparisons
for theta105 and48 for cos(theta)=-2/5. Separating supporting edges exclude
all interior overlaps, including reflected boundary descriptions and motif
self-translates.

With this motif and lattice, area equality gives covering multiplicity1
almost everywhere in a fundamental cell. The union of all lattice translates
is closed and locally finite, so a missing point would have an uncovered open
neighbourhood of positive area. Hence it covers every point of the plane.
This is a second global coverage proof and requires neither extension of a
finite patch nor a conjectural substitution. Both species occur and both
translation generators are periods.

## Irrationality and scope attacks

If theta/pi were rational, zeta=exp(i*theta) would be a root of unity, and
zeta+zeta^-1=2cos(theta) an algebraic integer. The source's monic recurrence
is valid; at cos(theta)=-2/5 that rational value is-4/5 and is not an integer,
a contradiction. Gamma/pi=2-2theta/pi is irrational as well. The stated
area formulas agree with independently computed shoelace areas. A rational
area ratio would require simultaneously101=151r and1=r by independence of
sqrt21 andsqrt5 over Q, which is impossible.

I attacked angle indexing, reversal/orientation, shape congruence, side-slot
reuse, disconnected or noncircular links, residual rotations, a rank-one
period group, missed overlaps outside a diagnostic window, and area-only
coverage gaps. All were excluded by the actual computations and mathematical
arguments above. The claim is a periodic counterexample for this exact
family. It does not exclude different three-angle pairs and does not classify
individual monohedral tilings of these members.

Replay:

```text
conda run --no-capture-output -n arisearch python3 research/reviews/verify_three_angle_pentagon_periodic_independent.py
```

## Independent replay and literal-irrational-length audit, 2026-10-10

**Reviewer:** the fresh `periodic_counterexample_audit` agent, independent
of the construction author and the earlier root review. This audit reread
the governing target and protocol, reviewed the exact coordinate and seam
definitions, and replayed the independent AA checker without importing an
author verifier. **Verdict: valid** for both original exact instances and
the sqrt(2)-scaled irrational-angle instance described below. No defect in
the mathematical proof of those instances was found.

The original irrational-angle normalization has private lengths 1 and
sqrt(5). This establishes an irrational private-length ratio, but does not
make both private lengths individually irrational. To meet the latter
literal condition, uniformly scale both exact polygons by sqrt(2). Their
private lengths are then sqrt(2) and sqrt(10), both irrational, and their
ratio is sqrt(5). The checker verifies these statements in AA by their
exact squares and nonmembership in QQ. It verifies that both private
lengths remain absent from the opposite shape and all six labels remain
distinct. The shapes have different side-length multisets, hence remain
distinct congruence classes. Both occur twice in the four-face motif.

The replay rederives all five side vectors and all vertex coordinates from
k=2/5, h=sqrt(21)/5, t=sqrt(2), s=sqrt(10), rather than relying only on a
verbal similarity argument. Exact supporting-line tests prove convexity,
exact cosines give the native angle word, and the same actual endpoint
seams produce six circular vertex links. The irrationality argument is
unchanged: a rational theta/pi would make 2cos(theta)=-4/5 an algebraic
integer, contradicting that a rational algebraic integer is an integer.
Then gamma/pi=2-2theta/pi is irrational too. Both shapes have the same
angle-multiplicity vector (2,2,1), so this instance is outside the
*different*-multiplicity hypothesis of the reviewed rationality lemma.

For the scaled instance, developing the face adjacencies independently
produces a translation basis

    u=(4sqrt(42)/25, sqrt(210)/2+42sqrt(2)/25),
    v=(17sqrt(42)/50+42sqrt(10)/25, -33sqrt(210)/50-42sqrt(2)/25).

All residual seam holonomies have identity linear part and lie in the
integer span of u,v. Both basis vectors themselves arise from residual
seams. Their determinant is nonzero and its absolute value equals the
whole motif area

    252sqrt(21)/25+861sqrt(5)/50.

The new readable radical outputs are converted through the exact field
with generator sqrt(21)+sqrt(5), defining polynomial
x^4-52x^2+256, and the indicated positive real embedding. Every displayed
radical expression is converted back to AA and checked exactly. This is
an output simplification, not an equality decided by approximation.

I specifically attacked the completeness of the overlap enumeration. Let
B_f[d]=[m_f[d],M_f[d]] be the exact coordinate interval of motif polygon f
in the basis (u,v). An overlap with polygon g+n*u+r*v can occur only for

    ceil(m_f[d]-M_g[d]) <= offset[d] <= floor(M_f[d]-m_g[d]),

for d=0,1, where offset=(n,r). These are necessary interval-intersection
conditions, so every possible overlap is in this finite product domain.
The verifier checks all ordered f,g in {0,1,2,3}, includes distinct-copy
self-translates, includes boundary endpoints in the ranges, and excludes
only f=g,n=r=0. Exactly 48 comparisons are made for the irrational-angle
instance and again 48 for its scaled version. Each is excluded by an
actual directed supporting edge of one of the two convex polygons; all
vertices of the other lie on its noninterior side. This proves disjoint
interiors, including tangencies and contacts involving partial edges.
The exact lattice-coordinate boxes and the complete comparison count are
unchanged under the scale, which the checker also asserts directly.

I also attacked area-only coverage. Periodicity and pairwise disjoint
interiors imply that the periodic covering multiplicity is at most one
almost everywhere in a fundamental parallelogram. Its integral is the
whole motif area, equal to the lattice determinant, so multiplicity is one
almost everywhere. The rank-two lattice and compact polygons give local
finiteness; their union is therefore closed. An uncovered point would
belong to a nonempty open complement, of positive area, a contradiction.
Thus every point is covered. This argument certifies an infinite legal
plane tiling directly, without an extension conjecture or a numerical
patch argument.

The exact shoelace areas are twice the original values, and the checker
additionally tests that their ratio is not in QQ. The earlier proof by
independence of sqrt(21),sqrt(5) still applies. Uniform scaling is only a
normalization change; it supplies no new forcing mechanism.

**Defects found:** none in the claimed exact periodic witnesses. The only
wording distinction was an irrational private-length *ratio* versus both
private lengths individually irrational; the exact scaled corollary
settles both readings. **Repairs:** none to the original proof. The
independent verifier was extended with the scaled replay and exact
irrationality membership checks. **Remaining uncertainty:** arbitrary
other three-angle pairs remain unclassified. The continuum construction
also allows t=s, when P,Q coincide; distinctness is asserted here only for
the checked exact t!=s witnesses, not for every family parameter.

Replay environment: Python 3.12.13 and SageMath 10.9.
Replay (no configured timeout or memory cap):

```text
conda run --no-capture-output -n arisearch python3 research/reviews/verify_three_angle_pentagon_periodic_independent.py
```

The replay passes the original 52- and 48-comparison domains and the added
scaled 48-comparison domain. It ends with the exact-scaling and both-private-
lengths-irrational PASS line.
