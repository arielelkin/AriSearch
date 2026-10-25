"""Exact mesh checks plus an unpruned connected-enumeration cross-check."""
from collections import Counter

from research.discovery.kite_grid import (
    boundary_polygon, canonical_cells, canonical_polygon, cell_polygon,
    convex_closure, cross, double_area, enumerate_convex, face_vertices,
    finite_cells, grid_orientations, neighbors, placements, squared_distance,
    transform_cell, transform_point, translate_cell,
)


def _boundary_turn_convex(cells):
    """Independent filter: cancel interior edges and walk the directed boundary."""
    edge_set=set()
    for cell in cells:
        p=cell_polygon(cell)
        for a,b in zip(p,p[1:]+p[:1]):
            if (b,a) in edge_set:
                edge_set.remove((b,a))
            else:
                edge_set.add((a,b))
    following={}
    for a,b in edge_set:
        if a in following:
            return False
        following[a]=b
    start=min(following)
    vertices=[start]
    p=following[start]
    while p != start:
        if p in vertices or p not in following:
            return False
        vertices.append(p)
        p=following[p]
    if len(vertices)!=len(edge_set):
        return False
    return all(cross(vertices[i-1],p,vertices[(i+1)%len(vertices)])>=0
               for i,p in enumerate(vertices))


def test_mesh_geometry_and_adjacency():
    for cell in finite_cells(-1,2,-1,2):
        p=cell_polygon(cell)
        assert double_area(p)==24
        assert all(cross(p[i-1],v,p[(i+1)%4])>0 for i,v in enumerate(p))
        assert len(neighbors(cell))==4
        for other in neighbors(cell):
            assert cell in neighbors(other)
        for r in range(6):
            for f in (False,True):
                transformed=transform_cell(cell,r,f)
                assert set(cell_polygon(transformed))=={transform_point(v,r,f) for v in p}
                assert {transform_cell(n,r,f) for n in neighbors(cell)}==set(neighbors(transformed))
    for o in range(2):
        assert sum(double_area(cell_polygon((0,0,o,k))) for k in range(3))==double_area(face_vertices(0,0,o))


def test_congruence_preserves_scale_and_ignores_isometries():
    p=cell_polygon((0,0,0,0))
    sig=canonical_polygon(p)
    for r in range(6):
        for f in (False,True):
            transformed=tuple((v[0]+72,v[1]-30) for v in map(lambda x:transform_point(x,r,f),p))
            assert canonical_polygon(transformed)==sig
    assert canonical_polygon(tuple((2*x,2*y) for x,y in p))!=sig


def test_closure_can_jump_over_nonconvex_sizes():
    face=frozenset((0,0,0,k) for k in range(3))
    assert boundary_polygon(face) is not None
    for k in range(3):
        pair=face-{(0,0,0,k)}
        assert boundary_polygon(pair) is None
        assert convex_closure(pair,2) is None
        assert convex_closure(pair,3)==face


def test_unpruned_connected_enumeration_agrees_through_eight():
    # No convexity pruning: independently generate every connected polyform,
    # then classify via directed-boundary turn signs, not hull-area equality.
    states={canonical_cells({(0,0,0,0)})}
    expected=set()
    connected_counts=[]
    convex_counts=[]
    for size in range(1,9):
        connected_counts.append(len(states))
        convex_states={s for s in states if _boundary_turn_convex(s)}
        convex_counts.append(len(convex_states))
        expected.update(canonical_polygon(boundary_polygon(s)) for s in convex_states)
        if size<8:
            states={canonical_cells(s|{n}) for s in states for c in s
                    for n in neighbors(c) if n not in s}
    assert connected_counts==[1,2,4,10,27,85,262,873]
    assert convex_counts==[1,1,2,0,0,2,0,0]
    actual=enumerate_convex(8)
    assert {c.signature for c in actual}==expected
    assert sum(len(c.embeddings) for c in actual)==sum(convex_counts)


def test_catalogue_eight_and_metadata():
    candidates=enumerate_convex(8)
    assert Counter(c.area_cells for c in candidates)=={1:1,2:1,3:2,6:2}
    for candidate in candidates:
        data=candidate.to_dict()
        assert data["area_cells"]==len(data["cells"])
        assert data["side_count"]==len(data["polygon"])
        assert len(data["angle_cos_data"])==data["side_count"]
        assert len(data["edge_squared_lengths"])==data["side_count"]
        assert double_area(candidate.polygon)==24*candidate.area_cells
        for embedding in candidate.embeddings:
            assert canonical_polygon(boundary_polygon(embedding))==candidate.signature


def test_placements_are_complete_for_single_cell():
    region=finite_cells(-1,2,-2,1)
    placed=placements({(0,0,0,0)},region)
    assert {next(iter(s)) for s in placed}==set(region)
    assert len(grid_orientations({(0,0,0,0)}))==6
    translated={translate_cell(c,7,-11) for c in region}
    assert len(placements({(0,0,0,0)},translated))==len(region)
