# A monohedral adjacent-repeat Cairo obstruction, including the e=2d stratum

**Status:** freshly independently hostile-reviewed **VALID**; see [review](../reviews/partial-contact-cairo-adjacent-repeat-obstruction-review.md). This is a
necessary monohedral condition, not a complete Cairo classification and not
a two-species obstruction. It strengthens the retained exact repeated-arm
counterexample without using Rao classification or a periodicity theorem.

## Statement and native conventions

Let w=sqrt(3)>0. A genuine convex Cairo pentagon has sides(a,b,c,d,e) in
counterclockwise directions0,90,150,240,300 degrees. Its closure is

    b-c=w(d-a),  e=w*c+d-2*a,

and its corner angle pairs are the two90 corners(a,b),(c,d) and the three
120 corners(a,e),(b,c),(d,e). Suppose a=b.

**Necessary condition.** If this pentagon admits any monohedral plane tiling
with all isometries and arbitrary side contacts, then either

    a=b=c=d,  or  e=2*a.                              (1)

Equivalently, every a=b pentagon outside these two metric strata is
monohedrally untileable. This includes the positive e=2d stratum, which the
previous no-e-subdivision counterexample left open. Native reflection gives
the corresponding c=d statement. The proof establishes necessity only;
periodic sufficiency on the two retained strata is not asserted here.

## Proof

If any two among a,c,d are equal, closure with a=b forces all three equal.
We therefore assume a,c,d pairwise distinct and e!=2a.

At a T-junction the two90 sectors have a perpendicular full native arm
seam. Their120 endpoints cannot be interior points of a native side. For
perpendicular arm length a, the possible native slots are a and b, and
both have other arm a. For perpendicular c the other arm is d; for
perpendicular d the other arm is c. Thus every possible T has two equal
collinear bank arms.

The independently reviewed exact two-T switch lemma excludes every unequal
opposing pair of90-to120 arms: if lengths m<M opposed from a120 endpoint,
the two switches would require equal total banks, but here those totals
would be2m and2M. Therefore no90-to120 arm can host a T, and any arm/arm
contact from a120 corner is a whole native match of equal length.

An e side can host at most one T. If it does, its endpoints must be the two
120 bank endpoints, since an intervening120 cannot lie inside a native
side and no arm can host an earlier T. Its equal banks of length r therefore
give e=2r, with r among a,c,d. In addition to the assumed e!=2a, positive
closure gives the exact identity

    e-2c=(w-3)*(2c+a)/3 < 0.                          (2)

So the only possible e-hosted T has banks d,d, on the exceptional e=2d
stratum. In that case each incident native arm faces one complete half of
e and has length d. In every case considered, neither a nor c can face an
e side along an initial ray from a120 corner. Whole e/arm matches are also
impossible since their other native endpoints have different angle types.

Now inspect the isolated120 corner whose two native arms are b=a and c.
Its c ray must whole-match another c arm. The only120 corner incident to
c is another isolated(a,c) corner. These two120 sectors force a third120
sector, whose two boundary rays must each be compatible with an a arm.
Neither a arm can face a partially matched e, since e!=2a. It also cannot
face an unequal native arm. Thus both rays of the third corner must be
native arms of length a. No120 corner has that pair: the isolated corner
has(a,c), while the e-adjacent corners have(a,e),(d,e); c!=a,d!=a, and
e is not an eligible arm mate on either ray. This is a contradiction.
Every copy has an isolated120 corner, so no tiling exists. This proves(1).

The argument allows e=2d contacts explicitly rather than silently assuming
all contacts are whole native sides. It uses only the exact contact lemma,
positive closure and the native corner incidence ledger.

## Exact arithmetic and explicit exceptional fixture

The independently replayable checker
[adjacent-repeat checker](../searches/partial-contact-cairo-adjacent-repeat-obstruction.py)
verifies identity(2) symbolically over Q(sqrt3), the closure consequences of
all possible internal equalities, the equal-bank event inventory, and a
genuine positive fixture on the formerly open e=2d stratum:

    (a,b,c,d,e)=(1,1,(1+3w)/4,(1+w)/4,(1+w)/2).

It checks closure, all5 native side lengths and15 strict supporting-edge
determinants. The three arm values are distinct; e=2d but e!=2a,2c. No
search, numerical angle decision or solver is involved. The geometric
switch theorem is the separately reviewed
[two-T contact invariant](partial-contact-cairo-two-t-switch.md).

This restricted monohedral obstruction does not show the pentagon cannot
participate in a two-species tiling, or settle aperiodicity of any pair.
