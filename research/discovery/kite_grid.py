"""Exact convex polykites on the hat kite mesh.

Coordinates (x,y) mean Euclidean (x, sqrt(3)*y). Translation indices use
U=(12,0), V=(6,6). A cell is (i,j,face,corner); faces and corners are CCW.
The catalogue is complete through its size bound, modulo geometric congruence.
``embeddings`` retains every mesh-equivalence class realizing each polygon.
No aperiodicity conclusions follow from this catalogue.
"""
from __future__ import annotations

from collections import deque
from dataclasses import dataclass
from functools import lru_cache
from typing import Iterable

Point = tuple[int, int]
Cell = tuple[int, int, int, int]
Polygon = tuple[Point, ...]
Mask = frozenset[Cell]


def cross(a: Point, b: Point, c: Point) -> int:
    return (b[0]-a[0])*(c[1]-a[1])-(b[1]-a[1])*(c[0]-a[0])


def double_area(poly: Polygon) -> int:
    return abs(sum(a[0]*b[1]-a[1]*b[0] for a,b in zip(poly,poly[1:]+poly[:1])))


@lru_cache(None)
def face_vertices(i: int, j: int, orientation: int) -> Polygon:
    x,y=12*i+6*j,6*j
    if orientation == 0:
        return ((x,y),(x+12,y),(x+6,y+6))
    if orientation == 1:
        return ((x+12,y),(x+18,y+6),(x+6,y+6))
    raise ValueError("face orientation must be 0 or 1")


@lru_cache(None)
def cell_polygon(cell: Cell) -> Polygon:
    i,j,o,k=cell
    if k not in range(3):
        raise ValueError("corner must be 0, 1, or 2")
    vs=face_vertices(i,j,o)
    a,b,c=vs[k],vs[(k+1)%3],vs[(k-1)%3]
    return (a,((a[0]+b[0])//2,(a[1]+b[1])//2),
            (sum(v[0] for v in vs)//3,sum(v[1] for v in vs)//3),
            ((a[0]+c[0])//2,(a[1]+c[1])//2))


def edges(poly: Polygon):
    return tuple(tuple(sorted((a,b))) for a,b in zip(poly,poly[1:]+poly[:1]))


@lru_cache(None)
def neighbors(cell: Cell) -> tuple[Cell, ...]:
    i,j,_,_=cell
    own=set(edges(cell_polygon(cell)))
    result=[]
    for di in range(-1,2):
        for dj in range(-1,2):
            for o in range(2):
                for k in range(3):
                    other=(i+di,j+dj,o,k)
                    if other != cell and own.intersection(edges(cell_polygon(other))):
                        result.append(other)
    assert len(result)==4, (cell,result)
    return tuple(sorted(result))


def translate_cell(cell: Cell, di: int, dj: int) -> Cell:
    i,j,o,k=cell
    return (i+di,j+dj,o,k)


def transform_point(p: Point, rotation: int=0, reflect: bool=False) -> Point:
    x,y=p
    if reflect:
        y=-y
    for _ in range(rotation%6):
        assert (x-3*y)%2==0 and (x+y)%2==0
        x,y=(x-3*y)//2,(x+y)//2
    return (x,y)


@lru_cache(None)
def transform_cell(cell: Cell, rotation: int=0, reflect: bool=False) -> Cell:
    i,j,o,k=cell
    original=face_vertices(i,j,o)
    transformed=tuple(transform_point(p,rotation,reflect) for p in original)
    acute=transform_point(original[k],rotation,reflect)
    # Recover the unique indexed face from its transformed lattice vertices.
    js=[p[1]//6 for p in transformed]
    ais=[(p[0]-p[1])//12 for p in transformed]
    ii,jj=min(ais),min(js)
    for oo in range(2):
        vs=face_vertices(ii,jj,oo)
        if set(vs)==set(transformed):
            return (ii,jj,oo,vs.index(acute))
    raise AssertionError((cell,rotation,reflect,transformed))


def normalize_cells(cells: Iterable[Cell]) -> Mask:
    cells=frozenset(cells)
    if not cells:
        return cells
    mi=min(c[0] for c in cells)
    mj=min(c[1] for c in cells)
    return frozenset(translate_cell(c,-mi,-mj) for c in cells)


def grid_orientations(cells: Iterable[Cell]) -> tuple[Mask,...]:
    cells=frozenset(cells)
    return tuple(sorted({normalize_cells(transform_cell(c,r,f) for c in cells)
                         for r in range(6) for f in (False,True)}, key=lambda s:tuple(sorted(s))))


def finite_cells(i_min: int, i_max: int, j_min: int, j_max: int) -> Mask:
    """All six cells per lattice parallelogram, with half-open index bounds."""
    return frozenset((i,j,o,k) for i in range(i_min,i_max)
                     for j in range(j_min,j_max) for o in range(2) for k in range(3))


def placements(cells: Iterable[Cell], region: Iterable[Cell]) -> tuple[Mask,...]:
    """All D6 images and lattice translates wholly contained in a finite region.

    For a geometric candidate, call for every one of its ``embeddings`` to
    include possible alternative mesh phases.
    """
    region=frozenset(region)
    found=set()
    for oriented in grid_orientations(cells):
        if not oriented:
            continue
        anchor=min(oriented)
        for target in region:
            if anchor[2:] != target[2:]:
                continue
            placed=frozenset(translate_cell(c,target[0]-anchor[0],target[1]-anchor[1])
                             for c in oriented)
            if placed<=region:
                found.add(placed)
    return tuple(sorted(found,key=lambda s:tuple(sorted(s))))


def canonical_cells(cells: Iterable[Cell]) -> Mask:
    return min(grid_orientations(cells),key=lambda s:tuple(sorted(s)))


def convex_hull(points: Iterable[Point]) -> Polygon:
    ps=sorted(set(points))
    if len(ps)<3:
        return tuple(ps)
    lower=[]
    for p in ps:
        while len(lower)>1 and cross(lower[-2],lower[-1],p)<=0:
            lower.pop()
        lower.append(p)
    upper=[]
    for p in reversed(ps):
        while len(upper)>1 and cross(upper[-2],upper[-1],p)<=0:
            upper.pop()
        upper.append(p)
    return tuple(lower[:-1]+upper[:-1])


def boundary_polygon(cells: Iterable[Cell]) -> Polygon | None:
    """Return the strict-corner convex boundary, or None for nonconvex unions."""
    cells=frozenset(cells)
    if not cells:
        return None
    hull=convex_hull(p for c in cells for p in cell_polygon(c))
    return hull if double_area(hull)==24*len(cells) else None


def squared_distance(a: Point,b: Point) -> int:
    return (a[0]-b[0])**2+3*(a[1]-b[1])**2


def canonical_polygon(poly: Polygon) -> tuple[int,...]:
    """Complete congruence invariant: cyclic pairwise squared distances.

    It allows reflections and arbitrary rigid rotations, and preserves scale.
    The polygon must have its collinear boundary vertices removed.
    """
    n=len(poly)
    words=[]
    for seq in (poly,tuple(reversed(poly))):
        for start in range(n):
            ordered=seq[start:]+seq[:start]
            words.append(tuple(squared_distance(a,b) for a in ordered for b in ordered))
    return (n,)+min(words)


def _positive_overlap(a: Polygon,b: Polygon) -> bool:
    # Separating-axis theorem, with strict interval overlap excluding mere contact.
    for poly in (a,b):
        for p,q in zip(poly,poly[1:]+poly[:1]):
            nx,ny=p[1]-q[1],q[0]-p[0]
            aa=[nx*x+ny*y for x,y in a]
            bb=[nx*x+ny*y for x,y in b]
            if max(aa)<=min(bb) or max(bb)<=min(aa):
                return False
    return True


def cells_meeting_hull(hull: Polygon):
    """All cells whose interiors intersect hull, using a provably covering halo.

    In lattice coordinates a=(x-y)/12,b=y/6 each triangular face spans one
    index interval in each coordinate. Thus floor(min)-1..floor(max) covers it.
    An extra index at either side is harmless and guards boundary contacts.
    """
    aa=[(x-y)//12 for x,y in hull]
    bb=[y//6 for x,y in hull]
    for i in range(min(aa)-2,max(aa)+2):
        for j in range(min(bb)-2,max(bb)+2):
            for o in range(2):
                for k in range(3):
                    c=(i,j,o,k)
                    if _positive_overlap(hull,cell_polygon(c)):
                        yield c


def convex_closure(cells: Iterable[Cell], max_cells: int) -> Mask | None:
    """Least convex whole-cell superset, or None if its size exceeds the bound.

    Every convex whole-cell superset must include each cell with positive-area
    overlap with the current hull. Iterating that forced inclusion is safe.
    """
    current=frozenset(cells)
    while current and len(current)<=max_cells:
        hull=convex_hull(p for c in current for p in cell_polygon(c))
        area=double_area(hull)
        if area==24*len(current):
            return current
        if area>24*max_cells:
            return None
        added=set(current)
        for c in cells_meeting_hull(hull):
            added.add(c)
            if len(added)>max_cells:
                return None
        assert len(added)>len(current), "nonconvex union must force a cell"
        current=frozenset(added)
    return None


@dataclass(frozen=True)
class Candidate:
    cells: Mask
    polygon: Polygon
    signature: tuple[int,...]
    embeddings: tuple[Mask,...]

    @property
    def area_cells(self) -> int:
        return len(self.cells)

    def to_dict(self) -> dict:
        poly=self.polygon
        angle_data=[]
        for i,p in enumerate(poly):
            a,b=poly[i-1],poly[(i+1)%len(poly)]
            u=(a[0]-p[0],a[1]-p[1]); v=(b[0]-p[0],b[1]-p[1])
            angle_data.append({"dot":u[0]*v[0]+3*u[1]*v[1],
                               "norm_product_squared":squared_distance(a,p)*squared_distance(b,p)})
        return {"cells":[list(c) for c in sorted(self.cells)],
                "embeddings":[[list(c) for c in sorted(s)] for s in self.embeddings],
                "polygon":[list(p) for p in poly], "area_cells":self.area_cells,
                "side_count":len(poly),
                "edge_squared_lengths":[squared_distance(a,b) for a,b in zip(poly,poly[1:]+poly[:1])],
                "angle_cos_data":angle_data,
                "signature":list(self.signature)}


def enumerate_convex(max_cells: int, *, progress=None) -> list[Candidate]:
    """Enumerate all convex unions with at most max_cells primitive kites.

    Completeness: a convex target is edge-connected. Starting from any one of
    its cells, an adjacent target cell can be adjoined until the target is
    reached; every forced convex closure stays inside that target. All single
    cells form one mesh-symmetry orbit. State reduction uses ONLY mesh
    isometries; geometric congruence grouping happens after the full search.
    """
    if max_cells<1:
        return []
    first=canonical_cells({(0,0,0,0)})
    seen={first}
    queue=deque([first])
    while queue:
        current=queue.popleft()
        if len(current)==max_cells:
            continue
        adjacent=set(n for c in current for n in neighbors(c))-current
        for n in sorted(adjacent):
            closed=convex_closure(current|{n},max_cells)
            if closed is None:
                continue
            key=canonical_cells(closed)
            if key not in seen:
                seen.add(key)
                queue.append(key)
                if progress:
                    progress(len(seen),len(key))
    grouped={}
    for cells in seen:
        poly=boundary_polygon(cells)
        assert poly is not None
        grouped.setdefault(canonical_polygon(poly),[]).append(cells)
    result=[]
    for signature,masks in grouped.items():
        masks.sort(key=lambda s:tuple(sorted(s)))
        cells=masks[0]
        result.append(Candidate(cells,boundary_polygon(cells),signature,tuple(masks)))
    return sorted(result,key=lambda c:(c.area_cells,c.signature))
