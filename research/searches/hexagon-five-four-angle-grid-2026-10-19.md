# Exact local metric witness on the first minimal support

Date: 2026-10-19. Status: explicit exact candidate, independently checked by a separate small geometric implementation. No claim of plane tilability, periodicity, aperiodicity, or corona extension.

## Object and domain

The native side words are A=(0,1,2,0,3,4) and B=(0,1,1,0,2,3). A native corner j means the corner between side j and side j+1, so the interior angle is at the END of directed side j. The support stars 3,7,9,15 forget handedness to (0,7,6),(1,9,8),(2,3,10),(4,5,11).

The exact finite domain is all 3^12 native interior angle assignments in {90,120,150} degrees, with each polygon total720 and those four triples total360. Each polygon has141 sequences meeting its total. Exactly609 ordered pairs meet all four stars. No symmetry quotient, random seed, heuristic pruning, or nonlinear solver timeout is used.

For every such pair, both vector closures are represented as four homogeneous linear equations on the shared five lengths over Q(sqrt3). The polyhedral cone is their common kernel intersected with the nonnegative orthant. A positive vector exists exactly when the sum of all extreme rays has positive coordinates. Positive pairwise-distinct coordinates exist exactly when no coordinate difference vanishes identically on every extreme ray: a positive weighted sum of rays with coefficients powers of an integer parameter avoids the finitely many roots of those differences. Tested integer parameters are at most 10*(raycount-1)+1, which exceeds the total possible roots of the ten nonzero difference polynomials. Normalize the resulting first length to1. Each accepted polygon then passes exact strict supporting-halfplane inequalities.

The runtime predeclared to the root agent was120 seconds; completed enumeration took2.13 seconds excluding interpreter startup. There were76 cones containing positive vectors and39 allowing all five coordinates distinct. The certificate preserves the ascending lexicographic angle-assignment SHA256. Software: Python3.12.13, SageMath10.9, Sage exact number-field polyhedron backend. Runtime is recorded but no solver timeout changes the domain.

## Exact witness

Write r=sqrt3>0. The lengths are (1,2,3,r,4). Interior angles at side ends are

- A: (90,120,150,120,90,150).
- B: (150,120,90,150,90,120).

Counterclockwise vertices, starting at side0, are

A: (0,0), (1,0), (1,2), (1-3r/2,7/2), (-3r/2,7/2), (-2r,2).

B: (0,0), (1,0), (1+r,1), (1+r,3), (r,3), (-r/2,3/2).

Both close exactly with their given side words. Every nonincident vertex lies strictly to the left of every native directed side; both are therefore simple strictly convex hexagons. Their side-length multisets differ, so they represent distinct congruence classes. All four support angle sums equal360 exactly. This establishes feasibility of the local angle-and-closure metric gate; it does not establish all local patch compatibility or any infinite tiling.

## Replay and evidence

Producer: research/searches/hexagon-five-four-angle-grid-2026-10-19.py

Certificate: research/certificates/hexagon-five-four-angle-grid-2026-10-19.json

Independent verifier: research/reviews/verify_hexagon_five_four_angle_grid_witness.py

Run either Python file with the prefix mandated by AGENTS.md:

    mise exec -- conda run --no-capture-output -n arisearch python research/searches/hexagon-five-four-angle-grid-2026-10-19.py
    mise exec -- conda run --no-capture-output -n arisearch python research/reviews/verify_hexagon_five_four_angle_grid_witness.py

The verifier imports no producer and does not reconstruct a cone. It verifies encoded exact coordinates, side lengths, angle cosines, supporting halfplanes, star sums and distinct congruence classes. It passed. Exhaustion counts remain producer computation rather than independently audited classification. Local dimer and corona overlap checks are a separate obligation.
