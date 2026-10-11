# Exact swapped-arm Cairo partial-contact periodic cone

Date2026-10-10. **Status:** complete full-cone mathematical proof and exact
computation; independent hostile review pending.

Question: does the k=2 generic cross-arm survivor P0=Q2,P2=Q0 support an
actual infinite tiling? Yes: the linked
[proof](../lemmas/partial-contact-cairo-swapped-arms-periodic.md) constructs a
periodic four-face tiling throughout the stated4D positive cone. It uses
directed interval-bank cancellation and positive multiplicity/area1, not
finite-patch extension. Both boundaries b=D,d=B are included.

Exact finite computation domain:

* All12 whole-seam endpoint equations for the fixed six seam pairs.
* All bank-chain outer endpoint and internal collinearity identities for
  two paired straight banks, with8 native bank edge vectors.
* The full polynomial motif area/covolume identity over QQ(sqrt3)[a,c,d,D].
* The exact fixture(a,c,d,D)=(1,2,3,4), convex supporting-edge tests for
  both polygons, and all44 possible nonidentity translated ordered motif
  pairs in the complete exact lattice-coordinate bounding ranges.

The field uses positive w=sqrt3. No float, random seed, SAT solver, symmetry
quotient, deadline, resource truncation or heuristic periodic search is
used. Sage10.9/Python3.12.13. An initial shell-only fixture run failed due
to the typo notdisjoint instead of not disjoint, before any conclusion was
retained. The fixture was rerun from the saved corrected script and passed.
During addition of polynomial bank-vector assertions, a sign error in the
assertions for clockwise Q side1 was detected and corrected before producing
a certificate. The proof already used the negative clockwise boundary and
was unchanged. The retained producer checks exact corrected oriented vectors.

[Producer](partial-contact-cairo-swapped-arms-periodic.py),
[certificate](../certificates/partial-contact-cairo-swapped-arms-periodic.json).
The certificate retains polynomial coordinates, all4 motifs, periods,
positive forms, fixture coordinates and all44 comparisons. No part of the
proof depends on discarded shell reconnaissance.

Nondestructive replay:

    conda run --no-capture-output -n arisearch python research/searches/partial-contact-cairo-swapped-arms-periodic.py

Explicit output production:

    conda run --no-capture-output -n arisearch python research/searches/partial-contact-cairo-swapped-arms-periodic.py --output research/certificates/partial-contact-cairo-swapped-arms-periodic.json

Completed result: PASS full4D polynomial seams, bank chains, covolume and44
complete exact fixture separations. A fresh reviewer must check the global
zero-boundary/multiplicity step and every real parameter case before the
family is promoted. This is only sufficient periodic existence for the
selected arm compatibility cone. It does not prove every tiling periodic
or classify the other39 generic necessary survivors.
