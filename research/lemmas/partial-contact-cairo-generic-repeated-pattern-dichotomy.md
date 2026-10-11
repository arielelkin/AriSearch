# A generic Cairo-pair dichotomy including every monohedrally untileable arm partition

**Status:** freshly independently hostile-reviewed **VALID** in the stated
generic scope; see [review](../reviews/partial-contact-cairo-generic-repeated-patterns-review.md). This extends the reviewed four-distinct-arm
classification to internally repeated shapes. No unrestricted Cairo-pair
classification is claimed: the exceptional metric hyperplanes are explicit.

## Exact internal types and exhaustive finite scope

Use the Cairo conventions and closure

    b-c=w(d-a), e=wc+d-2a, w=sqrt3.

The direct monohedral classification separately supplies periodic escape
whenever one member is a monotile. For a pair without such a member, its
possible exact internal arm partitions are

    D:    {a},{b},{c},{d};
    R01:  {a,b},{c},{d};
    R23:  {a},{b},{c,d};
    S:    {a,d},{b,c}.

The braces denote exact equality classes, with different classes required
to have distinct lengths. This is exhaustive: an a=c or b=d equality gives
a monohedral periodic escape; b=c is equivalent to a=d; an adjacent repeat
has three distinct arm values unless all four agree, also a periodic escape.
The additional monohedral rays e=2a for R01 or S and e=2d for R23 are
excluded from an aperiodic candidate but remain exact exceptional strata.

For each of the16 ordered internal-type pairs, enumerate all partial
bijections between its distinct internal length classes. Such a bijection
specifies exactly the cross-species arm equalities; it does not identify the
geometric native slots. With k classes matched among m,n, there are
binom(m,k)*binom(n,k)*k! patterns. Summing all four type counts gives738.
No symmetry quotient or bounded patch enumeration is used.

## Generic metric meaning and exact result

For each pattern impose both Cairo closure rows, its internal equalities,
and its selected cross equalities. On the resulting real kernel with
coefficients in Q(sqrt3), require all8 arms and both e sides positive and
exactly the declared length classes.

The generic subset additionally avoids every nonidentically zero linear
hyperplane of these kinds:

* equality between two distinct right-corner event totals;
* equality of either e side with any right-corner event total;
* equality of eP and eQ when it is not an identity of the pattern.

Identically equal bank totals are grouped and retained, including identities
created by the repeated native slots. No genericity is assumed inside such
a group. Only the listed proper hyperplanes are excluded.

**Scoped theorem.** For every exact pattern and positive metric in this
generic subset, the pair either has no unrestricted plane tiling or admits
a doubly periodic tiling. All original isometries, arbitrary partial
contacts and species omission are allowed. Each generic local survivor
belongs to a separately reviewed sufficient periodic partner cone.

Exact exhaustive output:

    738 total collapsed-label patterns;
     70 force an undeclared arm equality (no stated exact stratum);
    668 consistent positive patterns;
    517 generic beta-contact obstructions;
    151 generic local survivors, all explicitly periodically covered.

There are no consistent patterns with an empty positive cone, identically
forced e/event equality, or uncovered generic local survivor. The D/D
subcase independently reproduces22/155/32, leaving48 extra inconsistent
patterns,362 additional obstructions and119 newly periodically covered
survivors in the repeated-type extension.

## Necessary contact filter: native complements are never collapsed

Index native arms0..7 as(Pa,Pb,Pc,Pd,Qa,Qb,Qc,Qd), with perpendicular
complements o=(1,0,3,2,5,4,7,6). An event bank pair i,j is available only
if arm_o(i)=arm_o(j), and its total is arm_i+arm_j. For each actual slot,

    S_i={arm_i+arm_j: arm_o(i)=arm_o(j)}.

The reviewed two-T invariant makes unequal opposing arm slots i,j possible
only if S_i intersects S_j. Equal arms can whole-match. The producer uses
that safe necessary relation, dropping strict switch inequalities. It adds
no transitive closure, and never infers compatibility of two slots merely
because another slot of the same numerical length was compatible.

Both e sides avoid all event totals, so neither can host a T. Every e side
must whole-match an equal e side. A whole arm/e match is forbidden by its
90/120 endpoint types; a partial arm/e contact from a120 endpoint would
put a90 T on the e or a120 endpoint inside its mate, also forbidden. Thus
at either endpoint of every e/e seam, the third120 tile must use its native
isolated(b,c) corner. The two orientation signs are retained separately:
the seam exposes(d_H,d_G)/(a_H,a_G), or(d_H,a_G)/(a_H,d_G).

Each exposed pair must be compatible, in either order, with the ACTUAL b,c
slots of an isolated corner from P or Q. This gives the finite list of
allowed native e seams. Each species must have at least one available e
seam: neither member is a monotile in the generic subset by the direct
monohedral classification, so a tiling cannot omit either. If this fails,
any actual tiling would have an e side without a possible120 endpoint star,
which is a proved obstruction. This is not an extension heuristic.

## Every surviving pattern gives a reviewed periodic witness

The eight sufficient two-native-equality patterns are the reflection/species
swap orbits of

    swapped cone:  Pa=Qc, Pc=Qa;
    reviewed Y:    Pb=Qd, Pc=Qa.

Native reflection maps a↔d,b↔c, and species swap exchanges P,Q. The exact
producer expands every collapsed-class equality to native slot equalities,
then checks containment of a member of these orbits. Every one of151 local
survivors contains one; its certificate stores the concrete native equality
pair, cone name, two reflection flags and species-swap flag.

The first orbit is the independently reviewed
[swapped-arm4D cone](partial-contact-cairo-swapped-arms-periodic.md).
For the second, native reindexing(a,b,c,d,e) to(b,c,d,e,a) gives the reviewed
Y angle convention at theta120. Its partner criterion Q_Y2=P_Y0,
Q_Y4=P_Y1 is exactly Qd=Pb,Qa=Pc; thus the actual metric lies in the reviewed
[general Y periodic cone](general-y-pentagon-periodic-partner.md).
Extra shared-length relations or internal repeats only restrict those
positive sufficient cones; they do not invalidate their exact periodic
motifs. Consequently the stored equality containment proves a periodic
escape throughout each surviving generic stratum, not just at a fixture.

## Positivity, generic nonemptiness and replay

The producer computes every quotient kernel exactly over Q(sqrt3). It
checks forced equality by comparing full linear forms, not a single metric
sample. Strict positivity is decided by the homogeneous cone feasibility
problem arm_i>=1,eP>=1,eQ>=1 over that exact field. All668 consistent
patterns have a positive witness; each certificate retains its actual eight
arm values, both e values and kernel coordinates. The inequality>=1 is
equivalent to existence of strictly positive homogeneous metrics by scaling.

These witnesses need not themselves avoid every undeclared metric
hyperplane. Instead strict positivity gives a nonempty relatively open set
in the exact kernel. Each excluded hyperplane is explicitly nonidentical,
and finitely many proper linear hyperplanes cannot cover a nonempty open
set. No e/event equality is forced in any consistent pattern, as the
producer verifies. Thus every consistent pattern has an actual nonempty
generic positive stratum. This states exactly what the fixtures certify.

[Producer](../searches/partial-contact-cairo-generic-repeated-patterns.py),
[certificate](../certificates/partial-contact-cairo-generic-repeated-patterns.json),
[record](../searches/partial-contact-cairo-generic-repeated-patterns.md).
The independent checker reconstructs all 738 patterns without importing
the producer and passes the stated classification, forms, fixtures and
carrier mappings; see the linked review. No generic
conclusion covers a proper excluded e/event or event/event hyperplane;
those exceptional mixed-contact metrics are the next remaining boundary.
