# The entire normalized acute/obtuse contact family is untileable

Status: historical restricted argument; superseded for these native words by
the [reviewed all-metric untileability theorem](acute-obtuse-native-word-untileability.md).
This intermediate derivation has no separate completed review verdict.

Use native angle words

    A=(65,140.5,147.5,75,112),
    B=(40,144.5,136,47,172.5).

Normalize A2=B4=1, set A1=t>0, and require A3=A4. Assume each polygon
is strictly convex and closes with positive side lengths. B0,B1 may be
arbitrary positive values compatible with B closure. Then **no plane
tiling by the pair exists**, with arbitrary reflections, orientations,
vertex valences and partial side contacts.

This excludes the entire three-parameter family underlying the actual
four-tile module, not just its strict-longest or strict-shortest samples.
No periodic search, frequency argument or substitution hypothesis is used.

## Exact native facts and metric lower bounds

Write z=140.5 and x=147.5 for the endpoints of A1. The sole native180
multiset is(65A,75A,40B); hence every other native corner is non-flat-eligible.
Both z and x cannot lie strictly inside another tile's side.

The complete native360 census, verified over doubled integer degrees in
the [feature certificate](../certificates/acute-obtuse-long-edge-feature.json), is

* (65,147.5,147.5);
* (140.5,75,144.5);
* (140.5,47,172.5);
* (147.5,40,172.5);
* (112,112,136);
* (65,112,136,47);
* (65,65,136,47,47);
* (65,65,75,75,40,40);
* nine40 corners.

In particular the sole B144.5 star requires z and A75. The sole full
stars containing z are(z,75,144.5) and(z,47,172.5).

Let D=sin65−sin3>0, with angles in degrees. Closure gives

    A3=A4=(t*sin39.5+sin72)/D > 1,
    A0=(sin75+sin7)/D + t*(sin42.5−sin25.5)/D > 1.

The strict bounds follow from monotonicity of sine between0 and90.
They hold for all t>0, not only for a designated long-edge cone.

## A1 has either a whole neighbour or a flat T junction

Local finiteness gives a finite positive interval cover of A1 by neighbouring
native sides. Neither endpoint z,x may be inside a neighbour side. If there
are no interior junctions, there is exactly one whole equal-length native
partner. Any interior junction instead has a flat A sector180 and exactly
the native corners A65,A75,B40.

At such a T junction, every side of any of these three acute native corners
has a non-flat-eligible far endpoint:

| Acute corner | Incident side | Far endpoint |
|---|---|---|
| A65 | A0 | z=140.5 |
| A65 | A4 | A112 |
| A75 | A2 | x=147.5 |
| A75 | A3 | A112 |
| B40 | B0 | B144.5 |
| B40 | B4 | B172.5 |

The two outer sides of the native half-plane star lie along A1. Neither
may end in its interior (its far native endpoint would be flat), nor
extend past either endpoint (the heavy host endpoint would be flat).
Therefore each ends exactly at a host endpoint. They cover the two parts
of A1 with no further interior junctions. Thus an A1 containing a T has
exactly one such junction and exactly two native side pieces.

## Every partial A1 has the z/47/172.5 endpoint star

At the host z endpoint, far native endpoint z,112 or147.5 yields no full
completion, whereas144.5 and172.5 yield A75 and B47 respectively. Thus
the outer acute corner there must be B40. At the host x endpoint, the
remaining outer corner must be A75 via its A2 side, whose far endpoint
is x; an outer A65 has far z or112 and cannot complete that endpoint.
Consequently A65 is the middle corner of the T.

The internal A75/A65 ray has far endpoints112/112 if their incident
native sides are A3/A4, and112/z if A65 instead uses A0. Both far
endpoints are non-flat-eligible, so that internal seam must whole-match.
The112/z pair has no completion;112/112 admits B136. Therefore the
internal ray uses A3/A4. The remaining internal A65/B40 ray uses A0.

If B40's outer side were B0, its internal side would be B4=1. A0>1,
and their far endpoints z and B172.5 are both non-flat-eligible, so this
unequal internal seam is impossible. Hence B40's outer side is B4=1,
its internal side B0=A0, and the host z endpoint has star

    (z,B172.5,B47).

The other outer side is A2=1, so in fact partial A1 is possible only at
t=2 and B0=A0. This exceptional equality does not evade the endpoint
conclusion: z still belongs to(z,47,172.5), never(z,75,144.5).

## Whole A1 partners also cannot supply the B144.5 star

Checking both endpoint orders against the full census leaves only native
partners A2,B0,B3,B4. This is a necessary angular table independent of
length coincidences; the same-A1 reflection and half-turn orders fail.

The B0 order pairs z with B144.5 and x with B40. At its z endpoint the
third tile has A75. A1 already meets B0, so A0 must meet either A2 or
A3 incident to that A75 corner. Meeting A2=1<A0 puts its far x endpoint
inside A0, impossible. Meeting A3 instead leaves an A2/B1 seam between
the other two tiles. Its far endpoints x and B136 are non-flat-eligible,
so the seam must have equal lengths and a common endpoint. But147.5+136
leaves76.5, below two minimum40 angles and equal to no native angle.
Thus B0 is impossible for every t.

An A2 partner requires t=1 and pairs x with x. The third tile at that
endpoint must have A65. Of the two x copies, one used its A2 in the
shared seam and retains a unit A1 side ending at z. That unit side faces
one side of A65, both of whose lengths A0,A4 exceed1. Its z endpoint
would lie inside that longer side. Thus A2 is impossible as well.

A B3 partner uses only the order z-to-B47, x-to-B172.5, and has the
star(z,47,172.5) at z. A B4 partner uses only z-to-B172.5, x-to-B40,
and has the same z star. These are the only remaining whole possibilities.

## Contradiction

Every A1, whether whole or partially matched, therefore puts its native
z endpoint in(z,47,172.5). No native z corner can occur in
(z,75,144.5). But every B144.5 corner must have exactly that second
star, and cannot lie at a flat vertex. Thus no B tile can occur. Every
remaining whole/partial A1 possibility requires B, so no A can occur
either. A plane covering is impossible.

The geometric local cap remains valid with some boundary sectors unfilled.
It cannot complete those sectors in any infinite tiling of this family.
Changing a specified native angle word, A2=B4 or A3=A4 changes a premise;
the theorem makes no claim about such different construction families.
