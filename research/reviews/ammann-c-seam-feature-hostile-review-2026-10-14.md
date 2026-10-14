# Independent hostile review: intrinsic Ammann c seam

Date: 2026-10-14. Verdict: **VALID as a negative local feature gate**. The unique c edge is intrinsic to each unmarked source pentagon under `(G1)`, but the isolated rule that a full c contact must be P1–P2 is false as a local contact rule. No two-convex-polygon compiler, full-plane counterexample, or general impossibility theorem is inferred.

I checked the five-side words against the reviewed source reconstruction and independently checked all five cyclic positions and their reversals. `P1=(a,b,a,c,a)` and `P2=(c,r,r,a,b)` each contain one c edge because `(G1)` makes a,b,r,c pairwise distinct. Reflection reverses the flanking order and does not supply absolute ambient handedness. The asymmetric side cycles can intrinsically distinguish the c endpoints and canonically name all vertices and diagonals; that fact does not by itself prove an X/Y rhomb-arrow rule. Each pentagon has five undirected diagonals. This audit retains all five as alternatives and supplies no proof selecting the source chord.

The half-turn of P1 about its c-edge midpoint produces a second isometric P1 on the opposite side of the supporting line. Convexity makes their interiors disjoint, and the complete c edges coincide. At each endpoint a K angle and an L angle sum to `kappa+(216-kappa)=216` degrees, leaving 144 degrees. Two source 72-degree corners have the correct angular sum. This is a genuine positive-length homotypic contact with endpoint angular feasibility. It is only a two-tile patch: no claim that the residual sectors can be filled consistently over the plane follows. Reflection across the c supporting line instead produces K–K and L–L, so it is a distinct contact and cannot be substituted for the half-turn witness.

The source's P1–P2 c matching follows from its full three-shape vertex atlas and the no-flat-relation theorem. Those proofs use H6 sectors and forced contacts one edge away. They do not transfer merely because the new output polygon has a recognizable c-length edge. The c seam itself joins the two thick-rhomb pentagons; the X/Y arrow data are on reconstructed unit rhomb edges. A proposed two-polygon output needs a separate all-tilings decoder that handles alternate chords, reflections, partial contacts, both species omissions and homogeneous wrong-arrow coverings.

Independent replay, with no author imports:

```text
mise exec -- conda run --no-capture-output -n arisearch python research/reviews/ammann-c-seam-feature-independent-2026-10-14.py
```

It passed. Its finite assertions establish only dihedral c-edge recognition, retained chord alternatives and the exact half-turn endpoint angle identity. The convex contact geometry and source-atlas dependence are checked mathematically above.
