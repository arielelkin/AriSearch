# A four-dimensional periodic cone containing branching repeated-side hexagons

**Status:** freshly adversarially reviewed as valid (2026-10-10), with a
[whole-domain proof and geometry review](../reviews/hexagon-adjacent-repeat-periodic-cone-fresh-review.md)
and a [no-author-import exact checker](../reviews/verify_hexagon_adjacent_repeat_cone_independent.py).
This is a constructive exclusion family, not a classification of repeated-side
hexagons and not an aperiodic pair. The construction extends the formal
four-triangle ring of Section 2 of
[hexagon-holonomy-distinct-lengths.md](hexagon-holonomy-distinct-lengths.md)
through numerical length collisions. Its metric cone, explicit developing
coordinates, adjacent-repeat subfamily and physical-neighbor branching are
established here without an internal-distinctness hypothesis. No novelty claim.

## 1. The full family and theorem

Put h=sqrt(3) and take directed unit sides

    U0=(1,0), U1=(1/2,h/2), U2=(-1/2,h/2),
    U3=(-1,0), U4=(-1/2,-h/2), U5=(1/2,-h/2).

The native vertices of either polygon start at (0,0), and its j-th edge is
its j-th listed length times Uj. All native interior angles are 120 degrees.
The four free parameters are p,q,a,c. Set

    b=p+a-c, d=q+a-c, r=p+2(a-c), s=q+2(a-c).

Assume exactly the open cone

    p,q,a,c,b,d,r,s > 0.                                  (1)

Define native side words

    A=(p,a,q,b,c,d), B=(r,c,s,b,a,d).                      (2)

**Theorem.** Every metric in (1) produces closed, strictly convex A and B,
and these whole polygons admit a doubly periodic plane tiling with two copies
of each per four-face torus. Numerical coincidences among the formal lengths
are allowed. If the two shapes are noncongruent this is an exactly two-class
periodic witness; if they happen to be congruent the construction still tiles.
Neither an already admitted tiling nor a finite-patch extension is assumed.

The following are periods of the constructed tiling:

    u=(2p+q+3a-3c, -h(q+a-c)),
    v=(p-q/2+a, h(q/2+a)).                                (3)

They are independent throughout (1). The construction uses translations and
half-turns only; reflected copies are permitted by the research problem but
are not required by this periodic witness.

### Closure and convexity

For A, the two closure equations give b=p+a-c and d=q+a-c. Substitution
in the two B equations gives r=p+2(a-c), s=q+2(a-c). Conversely these four
expressions make both vector sums zero. The coefficient matrix for the four
dependent variables b,d,r,s has full rank four; thus this describes the full
closed metric cone for the formal words (2), rather than a smaller subcone.
It is nonempty and four-dimensional, for example near p=q=a=c=1.

A closed path with positive lengths in the directions U0,...,U5 is strictly
convex. Here is a direct supporting-line proof. For edge i of length Li,
the cross products with the vectors from its start to vertices at cyclic
offsets 2,3,4,5 are, respectively,

    (h/2)Li Li+1,
    (h/2)Li(Li+1+Li+2),
    (h/2)Li(Li+1+Li+2),
    (h/2)Li Li-1.

All are positive; the offset-5 expression uses closure. Therefore every
nonadjacent vertex is strictly on the inner side of every supporting edge.
This proves simplicity, strict convexity and six actual 120-degree corners.

## 2. Explicit four-face gluing and the global proof

Let A and B also denote their native vertex lists and let e0=(1,0). Place
four faces, preserving their native side slots:

    face0=A,
    face1=p e0-A,
    face2=(p+d/2,-h d/2)+B,
    face3=(-d/2,h d/2)-B.                                 (4)

The minus sign means central inversion, so all four boundary orientations
remain counterclockwise. Pair the following complete side slots, reversing
the boundary endpoint order. In the final column, add that translation to
the second face to make the two side segments coincide.

| First face,side | Second face,side | Shift of second face |
|---|---|---|
| 0,0 | 1,0 | 0 |
| 0,2 | 1,2 | v |
| 2,0 | 3,0 | u |
| 2,2 | 3,2 | u+v |
| 0,1 | 2,4 | 0 |
| 1,1 | 3,4 | 0 |
| 0,3 | 3,3 | v |
| 1,3 | 2,3 | -v |
| 0,4 | 2,1 | -u |
| 1,4 | 3,1 | u |
| 0,5 | 3,5 | 0 |
| 1,5 | 2,5 | 0 |

All endpoint equalities are polynomial identities in p,q,a,c. One may also
construct the quotient abstractly using just these twelve reversed full-side
pairings; numerical private/common collisions do not alter that selected
quotient.

Write a corner as (face,vertex), using zero-based native vertex indices.
Following a paired outgoing side and then the incoming corner on its mate
gives the following eight actual circular links:

    (0,0),(1,1),(3,5);      (0,1),(2,5),(1,0);
    (0,2),(1,3),(2,4);      (0,3),(3,4),(1,2);
    (0,4),(2,2),(3,3);      (0,5),(3,0),(2,1);
    (1,4),(3,2),(2,3);      (1,5),(2,0),(3,1).

These account for all 24 corners once. Each link has exactly three distinct
120-degree sectors and total angle 360 degrees. The side-pairing surface is
closed, orientable and connected. It has 8 vertices, 12 edges and 4 faces,
so its Euler characteristic is zero and it is a torus. The Euclidean face
metrics match across edges and the links have no cone singularities.

This compact flat torus is complete. Its universal cover is complete, flat
and simply connected; developing its Euclidean charts is a global isometry
with the Euclidean plane. For example, completeness makes this local isometry
a covering of the complete Euclidean plane, and simple connectivity of that
plane makes the covering one-sheeted. Consequently the lifted whole faces
cover the plane with disjoint interiors. This is the global extension proof:
a locally compatible finite patch is not being presumed extendible.

The displayed zero-shift side graph already connects all four faces. Every
nonzero seam shift thus represents a holonomy loop completed by zero-shift
paths. Both u and v occur, and every other seam shift is an integer combination
of them. The deck translations are therefore generated by u,v. Directly,

    det(u,v)
      =h(2pq+3pa+3qa+4a^2-pc-qc-4ac)
      =2 area(A)+2 area(B) > 0.                           (5)

The last inequality follows from strict convexity and positive side lengths.
Thus (3) is a rank-two period basis for this chosen four-face quotient. Extra
symmetries of the final tiling are not excluded.

## 3. An exact adjacent-repeat subfamily with no monohedral escape

Specialize p=a,q=c. Then

    A=(a,a,c,2a-c,c,a),
    B=(3a-2c,c,2a-c,2a-c,a,a),
    a>0, 0<c<3a/2, c != a.                               (6)

Write b=2a-c and r=3a-2c. All four numerical labels a,b,c,r are different
in this domain. A uses three labels with multiplicities 3,2,1; B uses four
with multiplicities 2,2,1,1. Hence A and B are noncongruent. Opposite lengths
are unequal in both polygons, so neither is centrally symmetric. The periods
simplify to

    u=(5a-2c,-h a), v=(2a-c/2,h(a+c/2)),
    det(u,v)=h(7a^2-c^2)>0.                               (7)

In any tiling by 120-degree convex polygons, a vertex containing a tile corner
cannot have a straight-side contribution: 120 m+180=360 has no integer m.
Two straight sectors would already exhaust the full angle. Thus every such
tiling is edge-to-edge with exactly three actual corners per vertex. This
argument permits reflected copies and unrestricted contacts at the outset.

For a single type, put a graph edge xy at every native corner between side
lengths x,y, retaining loops. At a three-corner vertex with ray lengths x,y,z,
all of xy,yz,zx must occur in its type's corner graph. Reflections preserve
these unordered pairs.

A's corner graph is {aa,ac,bc}. Its actual bc corner belongs to no three-ray
star using only this graph: b has only neighbor c, but neither bb nor cc is
available. Consequently A cannot tile alone.

B's graph is {ar,rc,bc,bb,ab,aa}. Its actual rc corner likewise belongs to no
B-only star: the only other neighbor of r is a, but ac is missing, and rr/cc
are missing. Consequently B cannot tile alone. These are direct local
obstructions, not an invocation of a monohedral classification. A limit or
reduction cannot remove an actual corner from a monohedral whole-tile tiling.

For the mixed pair the exact complete list of possible ray-length multisets is

    aaa, aab, aac, aar, abb, abc, acr, bbb, bbc.            (8)

There are only twenty multisets of size three on four labels; the retained
checker tests them all. Every listed combination has available 120-degree
corners. This list describes local length/angle legality, not global extension
of all choices. The chosen periodic quotient uses aaa,abc,acr,bbc, twice each.

## 4. Physical branching, both seam endpoints, and reflection quotients

The local ambiguity is not just a graph count. Fix native A side0, the segment
[(0,0),(a,0)]. Let B5 denote B's native vertex5; in (6), B5=a U2.
Put

    R4=[[-1/2,h/2],[-h/2,-1/2]],
    F =[[-1/2,-h/2],[-h/2,1/2]],
    G=(a,0)-B5+B.

R4 is a 240-degree rotation. F is reflection in the line of direction
120 degrees through (0,0). There are two distinct geometric placed mates:

* **A mate:** M_A=(a,0)-A, matching its native side0. Add the left filler
  L_A=B5-B and the right filler G. The third-corner pair at each endpoint is
  (a,a), supplied by B corner5. This is exactly the four-face periodic motif
  in (4) specialized to (6), so this branch has the proved global extension.
* **B mate:** M_B=R4 B, matching its native side5. Add left filler L_B=F B
  and the same right filler G. At (0,0), the third-corner pair is (a,r),
  supplied by reflected B corner0; at (a,0) it is (a,a), supplied by B corner5.
  This gives a locally compatible whole-tile patch. No infinite extension of
  this second branch is asserted here.

For M_A, its side0 endpoints are (a,0),(0,0). For M_B, its side5 endpoints
are (a,0),(0,0). All five contacts in either four-tile patch are full sides:

| Branch | Contacts beyond the selected A/mate seam |
|---|---|
| A mate | A5/L_A5, M_A1/L_A4, A1/G4, M_A5/G5 |
| B mate | A5/L_B5, M_B0/L_B0, A1/G4, M_B4/G5 |

Reflected L_B has clockwise native boundary order; its displayed equal sides
may therefore have the same native endpoint order. They are opposite boundary
orders when the reflected face is reoriented. Endpoint coordinates, rather
than an orientation convention, establish these geometric contacts.

The complete tiles in either patch have pairwise disjoint interiors throughout
(6), not just infinitesimal corner compatibility. At (0,0), the native A,
its selected mate, and the left filler lie in the closed convex corner cones
with angular sectors [0,120], [240,360], [120,240], respectively. At (a,0),
the native A, mate and right filler lie in [60,180], [180,300], [300,420].
Their interiors separate at each endpoint. The left filler has x<=0 and the
right filler x>=a, so those two also have disjoint interiors. Convexity puts
each whole polygon in its stated endpoint cone and proves every pairwise
separation.

Finally, quotient genuine intrinsic symmetries. The distinct length labels
in (6) give A exactly the identity and one reflection (x,y)->(a-x,y);
B has identity only. This follows either from the native coordinates or from
the twelve dihedral side-word permutations: A has one matching reflection,
B none, and both have only the identity rotation. The two specified neighbor
placements have noncongruent prototile types and remain distinct under every
intrinsic reflection quotient. Reflection is required for the B branch's
chosen left filler and is explicitly allowed by the research problem.

## 5. Exact replay, finite domains and result

Run from the repository root:

```text
conda run --no-capture-output -n arisearch python3 research/searches/hexagon-adjacent-repeat-periodic-cone.py
```

The producer is nondestructive: it writes no artifacts. A normal invocation
prints the exact status-neutral certificate JSON to standard output and a
concise PASS summary to standard error. Passing `--json` suppresses that summary.
The JSON gives the formal coordinates, side/vertex identifications and complete
fixture overlap domains.
The retained
[JSON certificate](../certificates/hexagon-adjacent-repeat-periodic-cone.json)
contains the same data. It records mathematical scope but no mutable review
status, so a completed review does not invalidate replay metadata.

The script independently derives the four dependent closure variables from
the unit-direction matrices, develops placements through the prescribed side
maps, verifies all twelve polynomial seam endpoints and eight actual circular
links, proves the supporting-edge cross-product identities and the area identity,
and enumerates all twenty local ray multisets. It also checks the side contacts
and intrinsic dihedral quotients of the two physical branches.

The exact asymmetric fixture a=1,c=3/4 has

    A=(1,1,3/4,5/4,3/4,1),
    B=(3/2,3/4,5/4,5/4,1,1),
    u=(7/2,-sqrt(3)), v=(13/8,11sqrt(3)/8),
    det(u,v)=103sqrt(3)/16.

For each ordered pair of motif faces, the checker transforms the polygons into
lattice coordinates. If their translated closed boxes intersect, each integer
translation coordinate is in the exact interval

    [ceil(min_i-max_j), floor(max_i-min_j)].

It checks every translation in that finite product by the exact convex
separating-axis theorem over the real algebraic field. Thus the 24 overlap
comparisons cover every potentially intersecting lattice translate, rather
than an arbitrary neighborhood. Their interiors are disjoint and motif area
equals covolume. Closedness of this locally finite periodic union upgrades
full area to complete coverage. The separate two local branch patches pass
12 unordered pairwise exact separations.

Replay (2026-10-10): Python 3.12.13, Sage 10.9; all assertions pass. The general
family theorem rests on the flat-torus proof and polynomial identities, not
extrapolation from this fixture. The concrete first global lemma is resolved.
This eliminates the full cone (1), including the physically branching and
monohedrally obstructed subfamily (6), as a universal-aperiodicity source.
It leaves other repeated-side hexagon families open.
