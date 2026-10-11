# Primary-source boundary for the pentagrid monohedral filter

Inspected2026-10-10 for the user-proposed golden-length pentagon avenue.

Primary source: Michaël Rao, *Exhaustive search of convex pentagons which tile
the plane*, [arXiv1708.00274v1](https://arxiv.org/pdf/1708.00274).
The author's [publications page](https://perso.ens-lyon.fr/michael.rao/publi.php?lang=en)
was also checked; it lists the pentagon work as a draft. This record imports
the classification explicitly, rather than claiming to independently verify
its complete implementation.

The relevant scope was inspected in the actual PDF: arbitrary isometries
on page1; full and half native vertices on page2; sides joining consecutively
indexed vertices on page10; family data in Table2 on page14; the reduction
of extra computational branches on pages14–15. The resulting monohedral
filter therefore covers reflections and partial contacts.

The new computation tests the three surviving fixed angle words against
all fifteen families and ten dihedral relabelings each. Reflection sends
outgoing side i to incoming old side h-i-1. Exact closure and strict metric
positivity are checked separately from the angle equations. Its theorem
and finite certificate are linked from
[the monohedral filter](../lemmas/pentagrid-pentagon-monohedral-filter.md).

This source only supplies a **one-shape** classification. It supplies no
two-pentagon periodicity theorem, aperiodic pair, mixed extension theorem,
or proof that the golden-length avenue is exhausted. The
[fresh independent source comparison](../reviews/pentagrid-monohedral-filter-review.md)
is valid. No novelty claim is made for the imported
classification or for the known monohedral tilings.
