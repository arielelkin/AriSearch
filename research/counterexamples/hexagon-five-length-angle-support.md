# Abstract angles do not select consistent repeated-side torus slots

**Status:** exact diagnostic counterexample, internally checked. These are
abstract side orders and corner angles, **not a certified pair of closed
convex polygons**. No polygon closure or plane tilability is claimed.

The claim refuted is: every twelve-corner-covering legal angle support for
A=(0,1,0,2,3,4), B=(0,3,0,5,1,6) contains one of the two four-star supports
arising from consistent formal splitting of the repeated length-0 slots.

Let angles, in units of pi, be

    a = (7/10,3/5,7/10,7/10,13/20,13/20),
    b = (7/10,3/5,13/20,13/20,7/10,7/10).

Every angle is strictly between pi/2 and pi, and each list sums to 4pi. The
only legal corner-typed stars are

    015: (a_0,b_2,b_3),
    016: (a_1,b_4,b_5),
    023: (a_2,a_3,b_1),
    034: (a_4,a_5,b_0).

They cover all twelve actual corner slots once. The consistent formal-slot
supports are either

    (015 uses a_0, 016 uses a_1, 023 uses b_0, 034 uses b_1)

or

    (015 uses a_1, 016 uses a_0, 023 uses b_1, 034 uses b_0).

Neither support is contained in the legal stars above. The full-edge test
kills the displayed abstract support: its 015 occurrence forces A side slot0
and B side slot2 to meet at numerical length0. At the other endpoint the
corners are a_5,b_1 and the third is a_4, whose sum is 19pi/10, not 2pi.
Thus this support cannot describe a trivalent edge-to-edge tiling.

This exposes why two independent corner-matchings cannot be substituted for
side-slot compatibility. It does not falsify the sparse-sharing theorem,
which uses the other-endpoint relation to choose a consistent support.

Replay:

```text
conda run --no-capture-output -n arisearch python3 research/reviews/hexagon-five-length-verify.py
```
