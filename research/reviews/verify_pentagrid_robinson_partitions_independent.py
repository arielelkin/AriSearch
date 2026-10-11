#!/usr/bin/env python3
"""Exact independent geometric/contact and necessary-boundary audit.

No producer imports. Geometry uses real support inequalities and separating
axes. Boundary fan counts use an integer transfer recurrence; ordered words
are reconstructed by fixed-length Cartesian products, not producer recursion.
"""
from collections import Counter
from itertools import combinations, product
import json
from pathlib import Path
from sage.all import AA, QQ, QQbar

if not __debug__: raise RuntimeError('Assertions required')
ROOT=Path(__file__).resolve().parents[2]
CP=ROOT/'research/certificates/pentagrid-golden-metric-robinson-partitions.json'
CB=ROOT/'research/certificates/pentagrid-golden-metric-robinson-boundary.json'
Z=QQbar.zeta(10); PHI=Z+Z.conjugate()
assert Z**4-Z**3+Z**2-Z+1==0 and Z.real()>QQ(4)/5 and Z.imag()>0
assert PHI.imag()==0 and PHI**2==PHI+1 and PHI.real()>1


def value(coeffs):
    assert len(coeffs)==4
    return sum(QQ(c)*Z**j for j,c in enumerate(coeffs))
def point(z): return (AA(z.real()),AA(z.imag()))
def sub(a,b): return (a[0]-b[0],a[1]-b[1])
def add(a,b): return (a[0]+b[0],a[1]+b[1])
def scale(c,p): return (c*p[0],c*p[1])
def dot(a,b): return a[0]*b[0]+a[1]*b[1]
def cross(a,b): return a[0]*b[1]-a[1]*b[0]
def edges(p): return [(p[i],p[(i+1)%len(p)]) for i in range(len(p))]
def area(p): return sum(cross(a,b) for a,b in edges(p))/2


def separated(a,b):
    for p,q in edges(a)+edges(b):
        v=sub(q,p); normal=(-v[1],v[0])
        x=[dot(normal,p) for p in a]; y=[dot(normal,p) for p in b]
        if max(min(x),min(y))>=min(max(x),max(y)): return True
    return False


def strict_convex(p):
    assert area(p)>0
    for i,(a,b) in enumerate(edges(p)):
        assert all(cross(sub(b,a),sub(w,a))>0
                   for j,w in enumerate(p) if j not in (i,(i+1)%len(p)))


def audit_geometry():
    c=json.loads(CP.read_text())
    references={'thin':[QQbar(0),QQbar(1),Z],'fat':[QQbar(0),QQbar(1),Z**3]}
    assert {name:[value(v) for v in p] for name,p in c['reference_triangles'].items()}==references
    source={'U':[QQbar(0),PHI**3,Z+Z**2+Z**3,Z**2+Z**3,Z**3],
            'V':[QQbar(0),QQbar(1),1+(1+3*PHI)*Z**3,2*PHI**2*Z**3,2*PHI*Z**4]}
    result={}
    for name in ('U','V'):
        record=c[name]; parent_complex=[value(v) for v in record['parent_vertices']]
        assert parent_complex==source[name]
        parent=[point(v) for v in parent_complex]; strict_convex(parent)
        triangles=[]; counts=Counter()
        for t in record['triangles']:
            vs=[value(v) for v in t['vertices']]; tri=[point(v) for v in vs]
            strict_convex(tri); kind=t['kind']; counts[kind]+=1
            iso=t['reference_isometry']; r=value(iso['rotation']); shift=value(iso['translation'])
            assert r*r.conjugate()==1 and r in [Z**k for k in range(10)]
            ref=references[kind]
            image=[r*(v.conjugate() if iso['reflected'] else v)+shift for v in ref]
            assert set(image)==set(vs)
            assert area(tri)==area([point(v) for v in ref])
            for a,b in edges(parent):
                assert all(cross(sub(b,a),sub(p,a))>=0 for p in tri)
            triangles.append(tri)
        assert counts==record['triangle_counts']==({'thin':7,'fat':9} if name=='U' else {'thin':9,'fat':16})
        tests=0
        for i,j in combinations(range(len(triangles)),2):
            tests+=1; assert separated(triangles[i],triangles[j]),(name,i,j)
        assert tests==record['pair_separation_tests']==(120 if name=='U' else 300)
        assert sum(area(p) for p in triangles)==area(parent)
        found=[]
        for i,j in combinations(range(len(triangles)),2):
            for e,(a,b) in enumerate(edges(triangles[i])):
                v=sub(b,a)
                for f,(p,q) in enumerate(edges(triangles[j])):
                    if cross(v,sub(p,a)) or cross(v,sub(q,a)): continue
                    ends=[dot(sub(w,a),v)/dot(v,v) for w in (p,q)]
                    lo=max(AA(0),min(ends)); hi=min(AA(1),max(ends))
                    if lo>=hi: continue
                    found.append((i,e,j,f,set((a,b))==set((p,q)),add(a,scale(lo,v)),add(a,scale(hi,v))))
        retained=[(t['first_triangle'],t['first_edge'],t['second_triangle'],t['second_edge'],
                   t['whole_edge_on_both'],point(value(t['overlap_start'])),point(value(t['overlap_end'])))
                  for t in record['positive_internal_contacts']]
        assert found==retained
        assert sum(not t[4] for t in found)==record['partial_contact_count']==(4 if name=='U' else 15)
        result[name]=(triangles,dict(counts))
    reject=c['minimal_medial_interface_rejection']; m=PHI**2*Z**3
    assert value(reject['mandatory_cap_vertex'])==m
    assert [value(v) for v in reject['row_whole_edge']]==[2*Z**3,3*Z**3]
    fraction=value(reject['fraction_of_row_edge'])
    assert fraction.imag()==0 and fraction==PHI**2-2 and 0<fraction.real()<1
    cap=[i for i,p in enumerate(result['V'][0][:12]) if point(m) in p]
    assert cap==reject['cap_unit_triangle_indices_with_vertex']==[5,6,10,11]
    assert reject['row_unit_triangle']==16
    assert {point(2*Z**3),point(3*Z**3)}.issubset(set(result['V'][0][16]))
    assert c['content_matrix_thin_fat_rows_U_V_columns']==[[7,9],[9,16]]
    return result


SYMBOLS=('u','l','s')
LENGTHS={'u':(1,0),'l':(0,1),'s':(-1,1)}
NATIVE={'thin36':('u','u',1),'thin72':('u','s',2),
        'fat108':('u','u',3),'fat36':('u','l',1)}


def all_words(a,b):
    out=[]
    # Since n_l+n_s=b and n_u-n_s=a, total edges <= a+2b.
    for n in range(1,a+2*b+1):
        for w in product(SYMBOLS,repeat=n):
            if tuple(sum(LENGTHS[s][i] for s in w) for i in (0,1))==(a,b): out.append(w)
    assert len(out)==len(set(out)); return out


def fan_table():
    table={(a,b,0):int(a==b) for a,b in product(SYMBOLS,repeat=2)}
    transitions=[]
    for name,(a,b,w) in NATIVE.items():
        transitions.append((a,b,w))
        if a!=b: transitions.append((b,a,w))
    for budget in range(1,6):
        for a,b in product(SYMBOLS,repeat=2):
            table[a,b,budget]=sum(table[t,b,budget-w] for s,t,w in transitions if s==a and w<=budget)
    return table


def validate_witness(witness,side_lengths,angles,available,table):
    words=[tuple(w) for w in witness['side_words']]
    assert len(words)==5
    tests=[]
    for i,w in enumerate(words):
        assert w in all_words(*side_lengths[i])
        tests.extend((w[j],w[j+1],5) for j in range(len(w)-1))
        tests.append((w[-1],words[(i+1)%5][0],angles[i]))
    fans=witness['boundary_fans_in_side_order']; assert len(fans)==len(tests)
    demand=Counter()
    for fan,(a,b,angle) in zip(fans,tests):
        assert (fan['from'],fan['to'],fan['angle_pi_over_5'])==(a,b,angle)
        current=a; budget=0
        for name,x,y,w in fan['corners']:
            p,q,weight=NATIVE[name]
            assert w==weight and ((x,y)==(p,q) or (x,y)==(q,p))
            assert x==current; current=y; budget+=w; demand[name]+=1
        assert current==b and budget==angle and table[a,b,angle]>0
    assert dict(demand)==witness['witness_native_corner_demand']
    assert witness['available_native_corners']==available
    assert all(demand[k]<=available[k] for k in demand)
    return sum(map(len,words))


def audit_boundary(geometry):
    c=json.loads(CB.read_text()); table=fan_table()
    assert c['length_symbols_in_basis_1_phi']=={k:list(v) for k,v in LENGTHS.items()}
    assert c['native_corner_classes']==[[k,*v] for k,v in NATIVE.items()]
    assert {(r['from'],r['to'],r['angle_pi_over_5']):r['walks'] for r in c['fan_counts']}=={
        k:v for k,v in table.items() if k[2]>0}
    assert all(table[a,b,5]>0 for a,b in product(SYMBOLS,repeat=2))
    for name in ('U','V'):
        record=c['fixtures'][name]; lengths=record['side_lengths_in_basis_1_phi']
        angles=record['angle_after_side_pi_over_5']; words=[all_words(*v) for v in lengths]
        assert list(map(len,words))==record['ordered_words_per_side']
        passing=[]
        for boundary in product(*words):
            if all(table[boundary[i][-1],boundary[(i+1)%5][0],angles[i]]>0 for i in range(5)):
                passing.append(boundary)
        assert len(passing)==record['boundary_choices_passing']==(299 if name=='U' else 18576)
        assert len(words[0])*len(words[1])*len(words[2])*len(words[3])*len(words[4])==record['boundary_choices_checked']==(625 if name=='U' else 21801)
        counts=geometry[name][1]; available={'thin36':counts['thin'],'thin72':2*counts['thin'],
                                           'fat108':counts['fat'],'fat36':2*counts['fat']}
        boundary_edges=validate_witness(record['first_witness'],lengths,angles,available,table)
        F=sum(counts.values())
        assert record['first_witness']['total_boundary_edge_count']==boundary_edges
        assert record['first_witness']['disk_euler_parity_passes']==((F-boundary_edges)%2==0)==False
        # The first witness is a local fan test; it need not meet disk Euler parity.
        print(name,'first local witness B=',boundary_edges,'F=',F,
              'disk parity=',(F-boundary_edges)%2==0)
        parity_pass=[w for w in passing if (F-sum(map(len,w)))%2==0 and sum(map(len,w))<=F+2]
        assert len(parity_pass)==record['boundary_choices_passing_fans_and_disk_euler']==(150 if name=='U' else 9288)
        parity_witness=record['first_witness_also_passing_disk_euler']
        B=validate_witness(parity_witness,lengths,angles,available,table)
        assert B==parity_witness['total_boundary_edge_count']==(10 if name=='U' else 11)
        assert parity_witness['disk_euler_parity_passes']==((F-B)%2==0)==True
        assert (F-B+2)//2==parity_witness['required_interior_vertex_count']==(4 if name=='U' else 8)
        print(name,'local passes=',len(passing),'also disk parity/nonnegative-I=',len(parity_pass))
    print('VALID: exact 16/25 partitions, 120/300 pair tests, all contacts and 4/15 partial counts;')
    print('mandatory cap midpoint T-junction; complete integer boundary-word/fan replay passed.')


if __name__=='__main__': audit_boundary(audit_geometry())
