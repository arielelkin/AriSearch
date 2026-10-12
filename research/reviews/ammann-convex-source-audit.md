# Source audit: Ammann's three unmarked convex polygons

**Date:** 2026-10-02
**Status:** historical source audit; its missing-source conclusion is
**superseded on the explicit generic G* domain** by the
[reviewed exact forcing theorem](../lemmas/ammann-forcing-aperiodicity.md).
The [corrected literature record](../literature/2026-10-11-convex-aperiodic-boundary.md)
recognizes Healey 2011. Non-generic parameters and two-shape fusion remain
separate obligations. Findings below describe the sources available on
2026-10-02, not the current restart state.

## Claim audited

The often-cited benchmark is a set of two convex pentagons and one convex
hexagon obtained by recomposing Penrose rhombi.  The claim needed by the
current fusion route is stronger than existence of its displayed tiling: all
tilings by those three unmarked shapes must lack every nonzero translation
when reflections and arbitrary contacts are allowed.

## Sources

* Branko Gruenbaum and G. C. Shephard, *Tilings and Patterns* (1987),
  pp. 580--582, Internet Archive record
  <https://archive.org/details/isbn_0716711931>.  The relevant scan pages
  were loan-restricted during this audit.
* Teruhisa Sugimoto, *Convex Polygons for Aperiodic Tiling*,
  arXiv:1602.06372v2, Section 2.2 and Figure 4,
  <https://arxiv.org/abs/1602.06372>.
* Teruhisa Sugimoto, *Aperiodic sets of three types of convex polygons*,
  arXiv:2404.00534v5, <https://arxiv.org/abs/2404.00534>.
* Robert Ammann, Branko Gruenbaum, and G. C. Shephard, *Aperiodic Tiles*,
  Discrete & Computational Geometry 8 (1992), 1--25,
  DOI `10.1007/BF02293033`.

## Exact data recovered

A normalized thin Penrose rhombus may be written

\[
A=(0,0),\quad B=(1,0),\quad
D=(\cos36^\circ,\sin36^\circ),\quad C=B+D,
\]

and a normalized thick rhombus as

\[
E=(0,0),\quad F=(1,0),\quad
H=(\cos72^\circ,\sin72^\circ),\quad G=F+H.
\]

These coordinates lie in an explicitly embedded real cyclotomic field.  The
recomposition chooses interior points \(J,K,L\) satisfying

\[
GL=DJ,\qquad FL=CJ=EK,\qquad HK=BJ,
\]

and the stated encoding condition is that \(DJ,CJ,BJ,KL\) are pairwise
distinct.  The accessible sources do not select a particular exact
algebraic \(J\), list the resulting polygon vertices, or give a substitution
matrix for the three recomposed shapes.

## Findings

1. The displayed edge-to-edge recomposition supports existence of a
   nonperiodic tiling in the intended Penrose construction.
2. The later Sugimoto paper explicitly says reflected pieces do not occur in
   the displayed tiling and adopts a no-reflection convention for its own
   constructions.  This is not a proof that allowing reflections introduces
   no periodic tiling.
   For Sugimoto's *new* three-type sets obtained by dividing Tile(1,1), the
   paper in fact says the opposite: allowing reflected pieces gives periodic
   tilings.  Those sets are therefore unusable here, independently of their
   other unconfirmed forcing claims.  This statement does not automatically
   transfer to Ammann's different three-polygon recomposition.
3. Calling the displayed tiling edge-to-edge is not a proof that every tiling
   by the shapes is edge-to-edge.  No accessible local classification was
   found excluding T-junctions, partial-edge contacts, or additive edge-length
   coincidences.
4. Pairwise distinctness of four lengths alone does not exclude all sums of
   shorter edges equalling a longer edge.
5. The rigorous 1992 paper concerns different marked/concave Ammann A2--A5
   families.  It points to book pages 550--558, not the convex construction
   on pages 580--582, and cannot be cited as its missing proof.
6. The A2/A3 frequency ratios in that 1992 paper likewise belong to those
   other families.  They cannot be transferred to the convex recomposition.

## Historical verdict and restart obligation

The benchmark cannot presently serve as the proved source set in the
convex-cluster fusion lemma.  Before using it, give exact coordinates and
prove a local reconstruction theorem covering reflections and all contacts,
or find a primary proof that does so.  Frequency calculations for the three
convex shapes must be derived independently from their actual recomposition,
not borrowed from the 1992 Ammann A3 system.
