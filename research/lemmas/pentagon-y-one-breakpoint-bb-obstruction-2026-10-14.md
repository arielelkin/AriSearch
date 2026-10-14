# Every Y-pair BB side has a full native mate

Date: 2026-10-14. Status: independently reviewed VALID for the scoped full-BB-mate theorem.
[Fresh hostile review](../reviews/pentagon-y-bb-partial-hostile-review-2026-10-14.md).

Let

    P=((0,0),(2,0),(3,2),(2,3),(0,2)),
    Q=((2,3),(1,4),(-1,4),(-2,3),(0,2)).

**Theorem (scoped).** In any tiling by isometric copies of these polygons,
including reflections and unrestricted partial contacts, every native `BB`
side of a `P` tile has exactly one full native side of length `sqrt(2)` as
its opposite mate. The mate can be a `P` `BB` side or a `Q` `CG` side. This
does not imply whole-edge contacts on other native sides or exclude a mixed
plane tiling.

## Exact angle and length facts

Write `theta=atan(2)`. The native corner angles are

    r=pi/2, a=pi-theta, b=pi/4+theta,
    c=3pi/4-theta, g=3pi/4, d=2theta.

The smallest is `c`. Indeed `pi/3<theta<3pi/8`, from
`2>sqrt(3)=tan(pi/3)` and `tan(3pi/8)=1+sqrt(2)>2`.
Therefore the three residual angles

    pi-g=pi/4,   pi-a=theta,   pi-d=pi-2theta

are all strictly smaller than every native corner angle. At a T-junction
on a straight native side, the other half-plane is filled by either `rr`
or `bc`, the complete flat-star palette established in the interface
lemma. These statements include reflected copies.

Normalize the host `P` side to the interval `BB=[0,sqrt(2)]` on the x-axis,
with its tile below the axis, and put the sole opposite-side native vertex
at `T=t`, where `0<t<sqrt(2)`. Each of the two guest native sides along
`BB` has length at least `sqrt(2)`; thus the left guest side extends through
`x=0` and the right guest side through `x=sqrt(2)`. At both host endpoints a
guest tile consequently supplies a flat angle. Since the host angle there
is `b`, the missing corner is `c`. Its edge shared with the host's adjacent
`AB` side must be its `CD` edge of length `sqrt(5)`, leaving its `CG` edge
of length `sqrt(2)` along the continuation of the x-axis. Hence forced `Q`
tiles place `G` corners at `x=-sqrt(2)` and `x=2sqrt(2)`. This is an actual
native-edge assertion: `C` has only `CD` and `CG` arms.

Call those two forced horizontal `CG` segments the *end guards*. An
additional native corner of type `A`, `D`, or `G` strictly inside an end
guard, on its other side, is impossible: that corner plus the guard's flat
angle leaves respectively `theta`, `pi-2theta`, or `pi/4`, all smaller than
`c`. Conversely, a forced guard `G` strictly inside a guest horizontal edge
is impossible because `pi-g=pi/4<c`. Thus, for a guest horizontal edge with
far endpoint of type `A`, `D`, or `G`, its outward endpoint must coincide
with the corresponding guard `G`. Any strict inequality makes one of these
forbidden flat vertices. This elementary endpoint interleaving test is
independent of the rest of the patch.

## One interior transition: the two possible T-junction types

If the guest corners at `T` are `rr`, they are two `P` right corners. Each
horizontal arm is `RA` of length `2`, with far corner `A`. Guard equality
on the left and right requires simultaneously

    t-2=-sqrt(2),       t+2=2sqrt(2).

Subtracting gives `4=3sqrt(2)`, false (squares `16` and `18`). The two
`R` sectors may be interchanged or reflected, but both horizontal arms
still end in `A`, so the same equations apply.

Suppose the guest corners are `bc`, in either order. If the `C` tile uses
its short `CG` horizontal arm, its far `G` lies strictly inside the
corresponding end guard: the horizontal distance from `T` to the host
endpoint is positive and smaller than `sqrt(2)`. This is forbidden. Hence
the `C` tile must use its long `CD` horizontal arm, and its other arm along
the internal `B/C` ray is `CG` of length `sqrt(2)`.

If the `B` tile uses its short `BB` horizontal arm, its internal arm is
`BA` of length `sqrt(5)`. The `C` tile's `G` endpoint at distance
`sqrt(2)` along that common internal ray then lies strictly inside the
`BA` edge, again a forbidden `G` against a flat side. Thus the `B` tile
uses its long `BA` horizontal arm. The two internal arms are now both of
length `sqrt(2)`, so this branch passes the immediate internal-ray check;
its horizontal far corners are `A` and `D`.

The end-guard test forces both long horizontal arms to have the same
outward endpoints as the guards. If `B` is left and `C` right, this says

    t-sqrt(5)=-sqrt(2),   t+sqrt(5)=2sqrt(2).

If their positions are reversed, the equations are identical because
both horizontal lengths are `sqrt(5)`. They imply `2sqrt(5)=3sqrt(2)`,
false (squares `20` and `18`). This exhausts the two flat-star types,
both orders, both arm choices at `B` and `C`, all offsets `t` in the open
interval, and reflections. No grid, solver, or bounded placement search
enters the proof.

## Two or more interior transitions

The tiling is locally finite: each of the two fixed convex polygons contains
a disk of uniformly positive radius, and tiles meeting a bounded region
have their contained disks in a larger bounded region, with disjoint
interiors. Thus only finitely many tiles meet `BB`. A convex guest meets
its supporting line along a single native-side interval when it shares a
positive-length contact. At a transition in the interior of `BB`, neither
of the two adjoining guests can supply a flat sector: that would occupy
the entire opposite half-plane and leave no room for the other guest.
Both guests therefore have native corners at the transition. If two or
more distinct interior contact transitions existed, choose two consecutive
ones. The guest covering the open segment between them would have its
full native side between those points, of length strictly less than
`sqrt(2)`. Every native side of either tile has length at least `sqrt(2)`.
Thus no such pair of transitions exists.

## Zero transitions: one containing guest side

Let one guest side contain `[0,sqrt(2)]`. If its length is `sqrt(2)`, its
endpoints coincide with the host endpoints and the theorem holds. A longer
side has length `L=2` or `L=sqrt(5)`, both less than `2sqrt(2)`. The
complete list of longer native sides and endpoint types is

    P RA: R,A (L=2);       Q GG: G,G (L=2);
    P AB: A,B (L=sqrt(5)); Q CD: C,D (L=sqrt(5)).

Each has at least one endpoint of forbidden type `A`, `D`, or `G`. The
guest cannot overhang both host endpoints. At such endpoints the forced
end guards above exist. A forbidden guest endpoint strictly inside its
adjacent guard is impossible; if it lies beyond the guard, the guard's
`G` lies strictly inside the guest edge, also impossible. Equality at a
left guard `G` at `x=-sqrt(2)` would require `L>=2sqrt(2)` to cover the
host's right endpoint, and equality at the right guard requires the same
to cover the host's left endpoint. Therefore one guest endpoint is flush
with one host endpoint, and the guest overhangs the other.

Its far endpoint lies strictly inside the sole end guard because
`sqrt(2)<L<2sqrt(2)`. Thus the far type cannot be `A`, `D`, or `G`. This
removes `Q GG`, `P RA` flush at `R`, `P AB` flush at `B`, and `Q CD` flush
at `C`. The three survivors have flush types `D` on `Q CD`, `A` on `P RA`,
or `A` on `P AB`; in every case the host contributes a `B` corner there.

For `D+B`, the remaining angle is `7pi/4-3theta`. It is smaller than
`2c` because `theta>pi/4`, so exactly one native corner would have to
fill it. Its theta coefficient `-3` differs from every native angle's
coefficient, using the established irrationality of `theta/pi`. This
flush end is impossible.

For `A+B`, the missing corner is uniquely `G`, since `a+b+g=2pi` and
`2c>g`. The nonhorizontal rays are the host `BA` edge of length
`sqrt(5)` and the guest's other `A` edge. A `G` corner has `GG` and `GC`
arms of lengths `2` and `sqrt(2)`.

If the guest horizontal edge is `P RA`, its other `A` edge is `AB`, also
length `sqrt(5)`. Whichever long ray receives the `GG` arm, its `G`
endpoint lies strictly inside a native length-`sqrt(5)` edge. There a
flat angle plus `G` would leave `pi-g=pi/4<c`, impossible.

If the guest horizontal edge is `P AB`, its other `A` edge is `AR` of
length `2`. The `GG` arm along the host `BA` ray would produce the same
forbidden interior `G`, so it must match the guest `AR` edge. The `GC`
arm follows the host `BA` ray for `sqrt(2)`, ending at `C` strictly
inside the host's length-`sqrt(5)` side. At this T-junction, the host
provides a flat sector, forcing a `B` corner because `b+c=pi`. An arm
of this new `P` tile must follow the remaining host `BA` ray toward its
`A` endpoint. Either possible `B` arm has length at least `sqrt(2)`,
whereas the remaining distance to host `A` is
`sqrt(5)-sqrt(2)<sqrt(2)`. Consequently host `A` lies strictly inside
that arm and has a flat-plus-`A` residual `pi-a=theta<c`, impossible.

This exhausts the zero, one, and at least two transition cases. The
conclusion is specific to `BB`.

## Scope and next obligation

The final `P AB` profile admits an exact overlap-free four-tile contact
patch before its forced fifth corner is placed. Its immediate far-endpoint
obstruction shows why a finite local witness would not establish extension.
A full `BB`/`BB` mate remains an angular possibility: the `bb` pair can
be completed by `cc` in the angle palette, but this does not establish a
larger patch. A positive construction with this pair must keep each `BB`
side full while supplying a repeatable partial-contact rule on other
native sides, and then prove infinite extension and universal
nonperiodicity. Neither is established here.

Dependencies: exact geometry and complete flat-star palette in
`research/searches/pentagon-y-interface-2026-10-14.md`. The whole-edge
obstruction in `research/lemmas/pentagon-y-whole-edge-native-propagation-2026-10-14.md`
motivates the seam but is not used in this proof.

The four-tile diagnostic and its endpoint inequalities replay exactly with

    mise exec -- conda run --no-capture-output -n arisearch python research/searches/pentagon-y-bb-contact-check-2026-10-14.py

The script checks the local fixture; the unrestricted theorem follows from
the case proof above, not from running the fixture.
