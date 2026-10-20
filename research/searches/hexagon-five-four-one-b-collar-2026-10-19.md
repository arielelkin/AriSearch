# One B collar gate for five residual strips

Date: 2026-10-19. Status: exact bounded computational failure; independently hostile-reviewed within its finite scope.

## Declared domain and result

Exactly rows 15,16,23,26,31 of the retained metric certificate, their six-tile translation-strip quotients, and the eight exposed whole-edge orbits are considered. Attach one layer of B polygons: every exposed edge must meet a whole native B edge, and a single B placement may satisfy multiple exposed edges. All six native B sides, both endpoint assignments and both orthogonal determinants are considered, subject only to exact length equality and placement on the exterior side of the exposed edge. This is at most 24 raw placements per edge and 24^8 raw assignments per metric. A 180-second cap is declared before product enumeration; no timeout occurred. No larger layer, metric family, or partial-edge placement is searched.

There is no compatible one-B-layer collar in this domain. Strip-compatible candidate counts in exposed chain order (B2,B0,B5,B4 repeated twice) are:

|row|counts|complete product assignments tested|
|---|---|---|
|15|4,3,2,1,4,3,2,1|576|
|16|2,2,2,1,2,2,2,1|64|
|23|0,2,2,1,0,2,2,1|0 (empty candidate orbit)|
|26|0,2,2,0,0,2,2,0|0 (empty candidate orbit)|
|31|0,1,2,1,0,1,2,1|0 (empty candidate orbit)|

Rows 15 and 16 fail because every complete assignment contains interior overlap between two distinct attached B tile orbits. The remaining rows already have at least one exposed edge with no B placement compatible with the original strip. Candidate equality is geometric equality modulo the existing translation, so multiple-edge contact by one B is permitted and consistently identified. None of the five metrics has even an open one-layer collar. Consequently there is no residual exposed word to report and no positive carrier requiring vertex-link, area, or transverse-period verification. These later acceptance checks were not reached; no flat quotient is claimed.

## Exact geometry and completeness

Arithmetic uses Sage QuadraticField(3), positive generator r. For a native side u and target side d of equal squared length, the script constructs the unique orthogonal map with each determinant taking u to d, for each endpoint assignment. Every full-edge congruent B placement is represented. Exterior placements are selected by the exact boundary interior-left convention.

All polygons are canonically translated by integer multiples of the retained longitudinal period v. For any polygon pair p,q, every possibly overlapping translate q+n*v lies in the strict projection interval

    (min(p.v)-max(q.v))/|v|^2 < n < (max(p.v)-min(q.v))/|v|^2.

Exact floor and ceiling enumerate precisely those integers. The convex separating-axis test uses all polygon sides, with equality allowing boundary contact. Geometrically equal tile translates are identified. Each candidate is checked against all original strip tile orbits and against its own nonzero translates. Every complete assignment is then checked between distinct new tile orbits. Thus an overlapping assignment cannot yield any periodic flat quotient containing the unchanged strip and these attached tiles, irrespective of a proposed transverse period.

The certificate retains all candidate attachment coordinates, determinant, native side, endpoint assignment, strip-compatibility flag, complete counts, and final completion status. The script is finite and deterministic. No floating-point geometric decision is used.

## Scope and restart

This is failure of exactly one B collar layer with whole-edge attachment to these eight orbits. It proves no unrestricted tiling obstruction, aperiodicity, or absence of a larger periodic completion. The bounded gate stops here. There is no instruction to open a second collar layer.

Inputs are the 39-omissions metric certificate, five-residual-coronas certificate, and strip-boundary-completion certificate. The [Sol hostile review](../reviews/hexagon-five-four-one-b-collar-hostile-sol-review-2026-10-19.md) independently checked placement completeness, exterior orientation, periodic overlap bounds, geometric deduplication when one B touches multiple edges, and the limited scope of failure. The discovery log records the reviewed result.

Replay:

    mise exec -- conda run --no-capture-output -n arisearch python research/searches/hexagon-five-four-one-b-collar-2026-10-19.py

Certificate: research/certificates/hexagon-five-four-one-b-collar-2026-10-19.json.
