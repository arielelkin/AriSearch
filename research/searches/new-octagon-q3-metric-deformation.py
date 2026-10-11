#!/usr/bin/env python3
"""Exact fixed-six-face Q3 torus metric deformation reconnaissance.

No period bound is enlarged. All native cyclic/reflection length assignments
of the four P copies are tried, with first copy normalized by D5 relabeling.
The known whole-side quotient and physical edge directions are fixed.
"""
import argparse
import json
from pathlib import Path
from itertools import product
from sage.all import QQ, AA, QQbar, CyclotomicField, QuadraticField, PolynomialRing, matrix, vector, Polyhedron, ceil, floor

K = CyclotomicField(10)
z = K.gen()
phi = z+z**-1
F = QuadraticField(5, "s", embedding=AA(5).sqrt())
pf = (1+F.gen())/2
basis = matrix(QQ, [K(q).list() for q in (1, phi, z, phi*z)]).transpose()


def real_pair(q):
    v = basis.solve_right(vector(QQ, K(q).list()))
    return (F(v[0]+v[1]*pf), F(v[2]+v[3]*pf))


def cross(p, q):
    return (p.conjugate()*q-p*q.conjugate())/(z-z.conjugate())


def walk(lengths, dirs, start=0):
    out = [start]
    for length, direction in zip(lengths, dirs):
        out.append(out[-1]+length*z**direction)
    return out[:-1]


def fixed_model():
    dirs = [j+int(j>=3) for j in range(8)]
    Q = walk([2,1,1,phi,1,1,1,1], dirs)
    H = Q[3]+Q[4]
    Q2 = [H-q for q in Q]
    u = H-Q[1]
    w = 2*phi+3-2*phi*z
    polygons = [Q, Q2]
    for q, j in ((Q,1),(Q,2),(Q2,5),(Q2,6)):
        e = q[(j+1)%8]-q[j]
        polygons.append(walk([1]*5, [0,2,4,6,8], q[(j+1)%8]))
        polygons[-1] = [q[(j+1)%8]-e*(p-q[(j+1)%8]) for p in polygons[-1]]
    det = cross(u,w)
    mates = {}
    for i, first in enumerate(polygons):
        for h, origin in enumerate(first):
            end = first[(h+1)%len(first)]
            found = []
            for j, second in enumerate(polygons):
                for g, mate_origin in enumerate(second):
                    mate_end = second[(g+1)%len(second)]
                    delta = origin-mate_end
                    n,m = cross(delta,w)/det,cross(u,delta)/det
                    if n in QQ and m in QQ and QQ(n).denominator()==QQ(m).denominator()==1 and end == mate_origin+n*u+m*w:
                        found.append((j,g,int(n),int(m)))
            assert len(found)==1,(i,h,found)
            mates[i,h] = found[0]
    seams = []
    for i,h in mates:
        j,g,n,m = mates[i,h]
        if (i,h)<(j,g):
            seams.append((i,h,j,g,n,m))
    assert len(mates)==36 and len(seams)==18
    return dirs,seams


def deformation(choices, dirs, seams):
    names = [f"p{j}" for j in range(5)]+[f"q{j}" for j in range(8)]+["w0","w1"]
    R = PolynomialRing(K, names)
    values = R.gens()
    p,q = values[:5],values[5:13]
    Q = walk(q, dirs)
    H = Q[3]+Q[4]
    Q2 = [H-t for t in Q]
    u,w = H-Q[1],values[13]+values[14]*z
    polygons = [Q,Q2]
    for index,(placed,j) in enumerate(((Q,1),(Q,2),(Q2,5),(Q2,6))):
        shift,sign = choices[index]
        lengths = [p[(shift+sign*h)%5] for h in range(5)]
        rotation = -z**dirs[j] if index<2 else z**dirs[j]
        start = placed[(j+1)%8]
        points = [start]
        for h,length in enumerate(lengths):
            points.append(points[-1]+length*rotation*z**(2*h))
        polygons.append(points[:-1])
    equations = [sum(q[j]*z**dirs[j] for j in range(8)),
                 sum(p[j]*z**(2*j) for j in range(5)), q[0]-q[3]]
    for i,h,j,g,n,m in seams:
        equations.extend((polygons[i][h]-polygons[j][(g+1)%len(polygons[j])]-n*u-m*w,
                          polygons[i][(h+1)%len(polygons[i])]-polygons[j][g]-n*u-m*w))
    rows = []
    for equation in equations:
        coefficients = [real_pair(R(equation).monomial_coefficient(v)) for v in values]
        rows.extend([[c[h] for c in coefficients] for h in (0,1)])
    kernel = matrix(F,rows).right_kernel().basis()
    if not kernel:
        return None
    # Positive side lengths are scale-free; all can be required>=1.
    inequalities = [[-1]+[v[j] for v in kernel] for j in range(13)]
    region = Polyhedron(ieqs=inequalities,base_ring=F,backend="field")
    if region.is_empty():
        return None
    witnesses = list(region.vertices())
    if not witnesses:
        return None
    point = vector(F,witnesses[0])
    witness = sum((point[h]*vector(F,kernel[h]) for h in range(len(kernel))), vector(F,[0]*15))
    assert all(witness[j]>=1 for j in range(13))
    return witness, len(kernel)


def exact_fixture():
    dirs,seams = fixed_model()
    lengths_p = [2*phi-2, phi, K(1), phi, 2*phi-2]
    lengths_q = [phi**2, 2*phi-2, phi, phi**2, K(1), 2*phi-2, phi, phi]
    Q = walk(lengths_q, dirs)
    assert Q[-1]+lengths_q[-1]*z**dirs[-1] == 0
    H = Q[3]+Q[4]
    Q2 = [H-t for t in Q]
    choices = [(0,1),(1,-1),(0,1),(1,-1)]
    polygons = [Q,Q2]
    for index,(placed,j) in enumerate(((Q,1),(Q,2),(Q2,5),(Q2,6))):
        shift,sign = choices[index]
        lengths = [lengths_p[(shift+sign*h)%5] for h in range(5)]
        rotation = -z**dirs[j] if index<2 else z**dirs[j]
        start = placed[(j+1)%8]
        points = [start]
        for h,length in enumerate(lengths):
            points.append(points[-1]+length*rotation*z**(2*h))
        assert points[-1] == start
        polygons.append(points[:-1])
    u,w = -3*phi+(7*phi-1)*z,3*phi+4-2*phi**2*z
    assert u == H-Q[1]
    det = cross(u,w)
    assert det == -(34*phi+11)
    def positive(q):
        assert QQbar(q).imag()==0
        return AA(QQbar(q).real())>0
    for polygon in polygons:
        for h,origin in enumerate(polygon):
            edge = polygon[(h+1)%len(polygon)]-origin
            assert all(positive(cross(edge,t-origin)) for j,t in enumerate(polygon)
                       if j not in(h,(h+1)%len(polygon)))
    mates,shifts = {},{}
    for i,h,j,g,n,m in seams:
        assert polygons[i][h] == polygons[j][(g+1)%len(polygons[j])]+n*u+m*w
        assert polygons[i][(h+1)%len(polygons[i])] == polygons[j][g]+n*u+m*w
        assert (i,h) not in mates and (j,g) not in mates
        mates[i,h],mates[j,g] = (j,g),(i,h)
        shifts[i,h],shifts[j,g] = (n,m),(-n,-m)
    assert len(mates)==36
    angles = [[3,4,4,3,4,4,4,4]]*2+[[3]*5]*4
    remaining,links = set(mates),[]
    while remaining:
        start = min(remaining)
        current,link,total_shift = start,[],[0,0]
        while current not in link:
            assert current in remaining
            remaining.remove(current)
            link.append(current)
            total_shift = [total_shift[h]+shifts[current][h] for h in range(2)]
            j,g = mates[current]
            current = j,(g+1)%len(polygons[j])
        assert current==start and total_shift==[0,0]
        assert sum(angles[i][h] for i,h in link)==10
        links.append(link)
    assert len(links)==12 and len(links)-len(seams)+len(polygons)==0
    areas = [sum(cross(p[j],p[(j+1)%len(p)]) for j in range(len(p)))/2
             for p in polygons]
    assert all(positive(q) for q in areas) and sum(areas)==-det
    # Convex inverse-lattice boxes give a complete finite intersection domain.
    boxes = []
    for polygon in polygons:
        coordinates = [(AA(QQbar(cross(t,w)/det).real()),
                        AA(QQbar(cross(u,t)/det).real())) for t in polygon]
        boxes.append([(min(t[h] for t in coordinates),max(t[h] for t in coordinates))
                      for h in range(2)])
    def separated(first,second):
        for polygon in(first,second):
            for h,origin in enumerate(polygon):
                edge = polygon[(h+1)%len(polygon)]-origin
                a = [AA(QQbar(cross(edge,t)).real()) for t in first]
                b = [AA(QQbar(cross(edge,t)).real()) for t in second]
                if max(a)<=min(b) or max(b)<=min(a):
                    return True
        return False
    comparisons = []
    for i,j in product(range(6),repeat=2):
        ranges = [range(int(ceil(boxes[i][h][0]-boxes[j][h][1])),
                        int(floor(boxes[i][h][1]-boxes[j][h][0]))+1) for h in range(2)]
        for n,m in product(*ranges):
            if i==j and n==m==0:
                continue
            assert separated(polygons[i],[t+n*u+m*w for t in polygons[j]]),(i,j,n,m)
            comparisons.append([i,j,n,m])
    # Only possible nonidentity Q symmetries must swap its two alpha corners.
    assert not any({h%8,(3+h)%8}=={0,3} for h in range(1,8))
    assert lengths_q[0] != lengths_q[2]  # reflection v ->3-v sends edge0 to2.
    def coefficient_vector(q):
        out = K(q).list()
        return [str(out[j]) if j<len(out) else "0" for j in range(4)]
    def phi_vector(q):
        a,b = real_pair(q)
        assert b==0
        coeff = a.list()+[QQ(0),QQ(0)]
        return [str(coeff[0]-coeff[1]),str(2*coeff[1])]
    return {"status":"exact completed plane-witness checks; fresh proof review retained in counterexample",
            "field":{"polynomial":"z^4-z^3+z^2-z+1","embedding":"z=exp(pi*i/5),Im(z)>0,4/5<Re(z)<81/100","phi":"z+z^-1"},
            "P_native_lengths":["2phi-2","phi","1","phi","2phi-2"],
            "Q_native_lengths":["phi^2","2phi-2","phi","phi^2","1","2phi-2","phi","phi"],
            "Q_native_vertex_angles_pi_over_5":[3,4,4,3,4,4,4,4],
            "P_native_vertex_angles_pi_over_5":[3]*5,
            "private_Q_slots":[0,3],"private_length":"phi^2 absent P and occurs twice Q",
            "Q_has_no_nonidentity_symmetry":True,
            "P_physical_native_assignments":[list(q) for q in choices],
            "motif_coefficients":[[coefficient_vector(q) for q in p] for p in polygons],
            "period_coefficients":list(map(coefficient_vector,(u,w))),
            "periods":["u=-3phi+(7phi-1)z","w=3phi+4-2phi^2z"],
            "normalized_areas_phi_basis_A_plus_B_phi":list(map(phi_vector,areas)),
            "normalized_determinant_phi_basis_A_plus_B_phi":phi_vector(det),
            "whole_side_seams":seams,"actual_corner_links":links,
            "all_link_lattice_shifts_zero":True,"all_link_angles_pi_over_5":10,
            "surface_euler_characteristic":0,"area_abs_determinant_identity":True,
            "complete_overlap_comparisons":comparisons,"comparison_count":len(comparisons),
            "all_complete_domain_pairs_have_disjoint_interiors":True,
            "search_domain":{"fixed_quotient":"known Q3 2Q+4P eighteen-seam torus and physical directions",
                             "native_choices":"first P normalized(0,+); remaining3 independently(shift0..4,sign+-)",
                             "total_normalized_choices":1000,"choices_examined_before_first_witness":304,
                             "method":"linear endpoint/closure equations over Q(sqrt5); exact positive cone via Sage field polyhedron",
                             "completion":"SAT exact witness; search stopped at first witness, not exhaustive classification",
                             "solver_timeout":None,"seed":None},
            "software":{"SageMath":"10.9","Python":"3.12.13"}}


if __name__ == "__main__":
    if not __debug__:
        raise RuntimeError("Run without Python -O")
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--search",action="store_true",help="replay fixed-quotient metric search until first nonregular witness")
    parser.add_argument("--output",type=Path)
    args = parser.parse_args()
    if args.search:
        dirs,seams = fixed_model()
        transforms = [(j,sign) for j in range(5) for sign in(1,-1)]
        found = False
        for index,tail in enumerate(product(transforms,repeat=3),start=1):
            choices = [(0,1),*tail]
            result = deformation(choices,dirs,seams)
            if result and len(set(result[0][:5]))>1:
                assert index==304 and choices==[(0,1),(1,-1),(0,1),(1,-1)]
                found = True
                break
        assert found
    rendered = json.dumps(exact_fixture(),indent=2)+"\n"
    if args.output:
        args.output.write_text(rendered)
    else:
        print(rendered,end="")
