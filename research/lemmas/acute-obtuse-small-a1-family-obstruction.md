# The normalized acute/obtuse family is untileable for every A1<=1

Status: historical restricted argument; superseded for these native words by
the [reviewed all-metric untileability theorem](acute-obtuse-native-word-untileability.md).
This intermediate derivation has no separate completed review verdict.

Use native words A=(65,140.5,147.5,75,112) and
B=(40,144.5,136,47,172.5), in degrees. Let A2=B4=1, A1=t>0,
and A3=A4. Require the polygons to close with positive side lengths.
The feature's closure formulas determine A0 and A3 from t, while B0,B1
remain free positive parameters subject to positive B closure. No maximum
length assumption on A0 or B0 is imposed here.

**Theorem.** For0<t<=1 no tiling by this fixed metric pair exists, with
arbitrary reflections, orientations and partial contacts. Thus varying
the B host length or making another B side shorter than A1 cannot repair
any such family member.

## Exact native angle facts

The complete native180 census contains only(65A,75A,40B). In particular
every other native corner is non-flat-eligible. The full360 census,
with species understood from the distinct angle values, is

* (65,147.5,147.5);
* (140.5,75,144.5);
* (140.5,47,172.5);
* (147.5,40,172.5);
* (112,112,136);
* (65,112,136,47);
* (65,65,136,47,47);
* (65,65,75,75,40,40);
* nine40 corners.

These are exact doubled-integer degree enumerations, of valence at most9.
The [feature certificate](../certificates/acute-obtuse-long-edge-feature.json)
retains the complete census. In particular B144.5 must meet A140.5 and
A75 in its unique full star, and no B144.5 can occur at a flat vertex.

The fixed closure formulas give A3>1 and A0>1 for every t>0. For A3,
its positive intercept is `sin72/(sin65−sin3)>1` and its coefficient
of t is positive. For A0 its expression is c0+c1*t, where sine addition
identities give, in degrees,

    c0=(sin75+sin7)/(sin65−sin3)>1,
    c1=(sin42.5−sin25.5)/(sin65−sin3)>0.

The inequalities follow from monotonicity of sine between0 and90.
Consequently every side incident to native A65 or A75 has length at
least1: A0,A4 at65 and A2=1,A3 at75.

## A1 cannot carry a partial contact, even if another side is shorter

Neither endpoint140.5 or147.5 of A1 can lie inside a neighbour side.
If an interior vertex existed on A1, its flat star would consist exactly
of the native corners A65,A75,B40. The two outer rays of that native
half-plane star belong to two distinct incidences among those three;
at least one is an A65 or A75 incidence. Its side on the outer ray has
length at least1>=t. Starting in the relative interior of A1, it extends
past one A1 endpoint and puts that non-flat-eligible endpoint strictly
inside the side, a contradiction.

Thus there are no interior contact junctions on A1 and neither endpoint
can lie inside another side. Local finiteness then forces a whole-side
match of length t. This is stronger than a minimum-side argument: it
does not assume t is the smallest B length.

Exhausting both endpoint orders against the full-star census, an A1
whole seam can have only native partners A2, B0, B3 or B4. The A2 and
B4 options have length1, so for t<1 only B0 or B3 can remain. All
other native partner types fail at least one endpoint angle star.

## The B0=t possibility is locally impossible

The only legal endpoint order pairs A140.5 with B144.5 and A147.5
with B40. At the first endpoint the third tile has native A75, since
the full star is(140.5,144.5,75). A1 already faces B0. Hence the other
side A0 of A140.5 must face one incident side of that A75 copy.

If it faces A2=1, the far A147.5 endpoint of that A2 side lies inside
the longer A0 side, contradicting non-flat-eligibility. If A0 instead
faces A3, the third seam from this vertex is A2 against B1. Their far
native endpoints are A147.5 and B136, both non-flat-eligible. Therefore
neither can terminate strictly inside the other side: their lengths must
agree and their other endpoints coincide. But147.5+136 leaves76.5,
which is below two minimum40 corners and equals no single native angle.
That seam cannot occur. Thus no A1/B0 whole matching exists.

## The B3=t possibility excludes every B144.5 corner

The only legal order pairs A140.5 with B47 and A147.5 with B172.5.
The A140.5 endpoint therefore has the complete star
(140.5,47,172.5). Once the previous B0 possibility is excluded, every
A1 must have this B3 match, so **every native A140.5 corner belongs to
this star**. None is available for a B144.5 star, which must instead
be(140.5,75,144.5). Thus no B tile can occur. But any A1 would require
a B3 neighbour, so no A can occur either. Equivalently a B-only plane is
already impossible by its pure angle census.

## The boundary t=1 also fails

The no-interior-T argument still applies at equality: a side of length1
starting at an interior point of the length1 host necessarily overruns
an endpoint. Thus A1 still whole-matches. The additional equal native
partner types are now A2 and B4.

An A1/A2 match pairs A140.5 with A75 and the two A147.5 corners with
each other. At the latter endpoint the only full star is
(147.5,147.5,65), with a third A65 tile. One of the two first A copies
uses its A2 side in the shared seam and has its other unit A1 side
running from that147.5 vertex to140.5. It must meet one incident side
of the third A65 tile, both of whose lengths A0,A4 exceed1. The far
140.5 endpoint would then lie inside that longer side, impossible.
Therefore the additional A2 partner is geometrically forbidden.

The B4 partner has only the legal order A140.5-to-B172.5 and
A147.5-to-B40. At A140.5 the resulting full star is again
(140.5,47,172.5). The B0 branch was excluded above without assuming
t<1, and the same-A1 endpoint orders remain angle-forbidden. Thus
every A140.5 corner belongs to(140.5,47,172.5), whether its A1 partner
is B3 or B4. No corner is available for any B144.5 star, exactly as
before. No tiling exists at t=1 either.

This is a direct local/inventory contradiction, not a positive-frequency
argument. It excludes all positive B metrics on the0<t<=1 branch,
including sparse species or arbitrary side subdivisions. For t>1 the
A75 corner's incident unit A2 side is now shorter than the A1 host and
the no-interior-T argument changes. That branch remains outside this
theorem and is the actual next parameter escape to investigate.
