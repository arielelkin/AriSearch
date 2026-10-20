# Interior-Q parent-corner branching gate

2026-10-19. Status: **analytic obstruction for simple triangulated dual disks; no incidence pair, angle witness, or metric candidate**. Independent hostile review pending. The unrestricted problem is unresolved.

## Scope and rigorous budgets

Retain inventories P parent 11P+2Q and Q parent 9P+3Q, exactly one split parent corner, trivalent seam vertices, no flats or excess degrees, and distinct single-arc boundary children. Work in the same simple oriented triangulated-dual-disk class as the preceding corner-branching generator. A dual vertex is a child and its degree counts its distinct seam neighbors. This simplicity hypothesis is explicit: no claim about parallel-seam multigraphs or repeated boundary arcs is made here.

For P, n=13,b=7, six interior children, E=3n-b-3=29, F=2n-b-2=17. For Q, n=12,b=6, six interior children, E=27,F=16. The ordinary boundary transitions are respectively B=6,5 and J=1. Native ledgers are 69=3*17+2*7+4 and 66=3*16+2*6+6. A boundary child has native count degree+1+u, where u is the number of untouched parent corners on its single boundary arc. An interior P has degree5 and an interior Q degree7.

Let q be the number of interior Q children, c>=0 the number of boundary-to-boundary chords beyond the outer boundary cycle, e the number of edges induced by the six interior children, and x their edges to boundary children. Then

    2e+x=30+2q,
    E=e+x+b+c,
    e=30+2q-E+b+c.

Thus P requires e=8+2q+c, while Q requires e=9+2q+c. Any Q-parent interior Q requires e>=11. This already demands changing the outerplanar all-P core, whose six vertices have at most9 edges.

## Six-interior-core obstruction

In a simple triangulated disk, six interior vertices all of full degree at least5 induce at most10 edges.

Proof. Suppose the induced plane graph H has e>=11. A disconnected simple planar graph on six vertices has at most9 edges (the extremal split is five plus one). If it has a cut vertex, split the other five vertices into nonempty blocks at that vertex. A block with s other vertices has at most 1 edge for s=1, and at most3s-3 edges for s>=2. The maximum sum over partitions of5 with at least two parts is10, attained by 4+1. Hence H is 2-connected.

Every bounded face of H is a triangle. Indeed its Jordan boundary encloses no boundary vertex of the whole disk; every disk vertex inside it would therefore be another interior vertex and already belong to H. The triangulated disk cannot leave a larger empty face. Euler and edge-face incidence give outer boundary length l=3*6-3-e=15-e. Simplicity gives e<=12 and l>=3, so either (e,l)=(11,4) or (12,3). The outer boundary is a simple cycle by 2-connectivity.

A vertex strictly inside that cycle cannot connect to any boundary child of the whole disk. Its degree in H therefore equals its full degree, at least5. Since H has only six vertices, that degree is exactly5, and the child is P.

For e=11,l=4 there are two such vertices. Each is adjacent to every other vertex, giving 2*4+1=9 edges incident to these vertices, in addition to the four edges of the outer cycle. This requires at least13 edges, contradiction.

For e=12,l=3 there are three such vertices. Their mutual triangle, all nine edges to the three exterior vertices, and the exterior triangle require15 edges, contradiction. Therefore e<=10.

Applying the Q budget e=9+2q+c gives 2q+c<=1. Consequently **q=0** in every Q-parent simple triangulated dual disk at these budgets. In particular the requested pair with an interior Q in each parent cannot exist in this class, independently of child phases, reflections, angle values, or corner allocations. P alone has only the weaker restriction 2q+c<=2, permitting q=1,c=0; no P map is asserted.

## The one changed design and stopping gate

The natural analytic replacement was a pentagonal wheel core: five ring vertices around one deep P of degree5. It has10 edges and might meet the P q=1,c=0 ledger, but Q needs11. Adding a ring chord must use the exterior of the already triangulated wheel; it cuts a ring vertex off the exterior, leaving it of induced/full degree3, violating the minimum5 requirement. The theorem proves that this failure cannot be fixed by another simple six-vertex core at the Q budget.

No complete requested pair exists in the stated simple-dual class. Hence no simultaneous strict angle system was instantiated, no SMT result or rational angle witness is claimed, and no exact metric gate is justified. All phases and reflections would remain allowed; the topology fails before those choices arise. There was no graph enumeration, count increase, second split corner, coordinate claim, Git edit, or discovery-log edit.

For broader interpretations allowing parallel dual edges, the precise remaining obligation is to establish simplicity from convex geometric dissections or separately treat such maps. This artifact does not silently extend its theorem to that class. Stop this changed cycle at the incidence gate.

Replay the small arithmetic certificate:

    mise exec -- conda run --no-capture-output -n arisearch python research/searches/interior-q-branching-sol-2026-10-19.py

The certificate checks only the displayed scalar inequalities; the planar argument above is the proof and requires independent review.
