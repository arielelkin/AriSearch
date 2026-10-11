#!/usr/bin/env python3
"""Exact fixed-quotient replay for a four-dimensional hexagon metric cone.

No bounded torus search. The finite domains are four faces/twelve prescribed
side pairs, twenty ray-length multisets for the repeated subfamily, and the
complete inverse-lattice bounding-box overlap domain at one exact fixture.
General metric statements are polynomial identities and flat-torus links.
"""
if not __debug__:
    raise RuntimeError('Exact verification requires assertions')

from itertools import combinations_with_replacement, product
import argparse
import json
import platform
import sys
from sage.all import AA, QQ, QuadraticField, PolynomialRing, vector, matrix, identity_matrix
from sage.env import SAGE_VERSION

parser=argparse.ArgumentParser(description=__doc__)
parser.add_argument('--json',action='store_true',help='Suppress stderr PASS summary; stdout always gives the certificate')
args=parser.parse_args()

K=QuadraticField(3,'h');h=K.gen()
real_embedding=K.hom([AA(3).sqrt()],AA)
real=lambda z:real_embedding(K(z))
U=[vector(K,w) for w in [(1,0),(K(1)/2,h/2),(-K(1)/2,h/2),
                         (-1,0),(-K(1)/2,-h/2),(K(1)/2,-h/2)]]
# Derive, rather than assume, the four dependent side lengths b,d,r,s.
# A=(p,a,q,b,c,d), B=(r,c,s,b,a,d), columns free=(p,q,a,c).
M=matrix(K,[[U[3][j],U[5][j],0,0] for j in range(2)]+
           [[U[3][j],U[5][j],U[0][j],U[2][j]] for j in range(2)])
N=matrix(K,[[U[0][j],U[2][j],U[1][j],U[4][j]] for j in range(2)]+
           [[0,0,U[4][j],U[1][j]] for j in range(2)])
assert M.rank()==4
assert -M.inverse()*N==matrix(K,[[1,0,1,-1],[0,1,1,-1],
                                [1,0,2,-2],[0,1,2,-2]])
S=PolynomialRing(K,names=('p','q','a','c'));p,q,a,c=S.gens()
b=p+a-c;d=q+a-c;r=p+2*(a-c);s=q+2*(a-c)
lengths=[[p,a,q,b,c,d],[r,c,s,b,a,d]]
ZERO=vector(S,[0,0])
polys=[]
for ls in lengths:
    poly=[];v=ZERO
    for length,w in zip(ls,U):
        poly.append(v);v=v+length*vector(S,w)
    assert v==ZERO
    polys.append(poly)
polys=[polys[0],polys[0],polys[1],polys[1]]
# A0,A1,B0,B1. Side slots are zero-based, endpoints always reversed.
pairs=[(0,0,1,0),(0,2,1,2),(2,0,3,0),(2,2,3,2),
       (0,1,2,4),(1,1,3,4),(0,3,3,3),(1,3,2,3),
       (0,4,2,1),(1,4,3,1),(0,5,3,5),(1,5,2,5)]
rots=[None]*4;shifts=[None]*4
rots[0]=identity_matrix(K,2);shifts[0]=ZERO

def seam_rotation(f,e):
    src=U[f];dst=-U[e]
    co=src.dot_product(dst);si=src[0]*dst[1]-src[1]*dst[0]
    return matrix(K,[[co,-si],[si,co]])

while any(R is None for R in rots):
    before=sum(R is not None for R in rots)
    for i,e,j,f in pairs:
        if rots[i] is None and rots[j] is not None:
            i,e,j,f=j,f,i,e
        if rots[i] is not None and rots[j] is None:
            rots[j]=rots[i]*seam_rotation(f,e)
            shifts[j]=(rots[i]*polys[i][(e+1)%6]+shifts[i]
                       -rots[j]*polys[j][f])
    assert sum(R is not None for R in rots)>before
assert rots==[identity_matrix(K,2),-identity_matrix(K,2),
              identity_matrix(K,2),-identity_matrix(K,2)]
assert shifts==[ZERO,vector(S,[p,0]),vector(S,[p+d/2,-h*d/2]),
               vector(S,[-d/2,h*d/2])]
placed=[[rots[i]*v+shifts[i] for v in polys[i]] for i in range(4)]
u=vector(S,[2*p+q+3*a-3*c,-h*d])
v=vector(S,[p-q/2+a,h*(q/2+a)])
seam_coords=[(0,0),(0,1),(1,0),(1,1),(0,0),(0,0),
             (0,1),(0,-1),(-1,0),(1,0),(0,0),(0,0)]
twin={};adj={i:set() for i in range(4)}
for (i,e,j,f),(n,m) in zip(pairs,seam_coords):
    assert rots[j]==rots[i]*seam_rotation(f,e)
    assert placed[i][(e+1)%6]==placed[j][f]+n*u+m*v
    assert placed[i][e]==placed[j][(f+1)%6]+n*u+m*v
    assert (i,e) not in twin and (j,f) not in twin
    twin[i,e]=(j,f);twin[j,f]=(i,e)
    adj[i].add(j);adj[j].add(i)
domain=set(product(range(4),range(6)))
assert set(twin)==domain
successor={t:(z[0],(z[1]+1)%6) for t,z in twin.items()}
unseen=set(domain);cycles=[]
while unseen:
    start=min(unseen);cur=start;cycle=[]
    while cur not in cycle:
        cycle.append(cur);cur=successor[cur]
    assert cur==start
    assert set(cycle)<=unseen
    unseen.difference_update(cycle);cycles.append(cycle)
assert len(cycles)==8 and all(len(C)==3 for C in cycles)
seen={0}
while seen!=set(range(4)):
    expanded=seen|{j for i in seen for j in adj[i]}
    assert expanded!=seen;seen=expanded
assert len(cycles)-len(pairs)+4==0
cross=lambda x,y:x[0]*y[1]-x[1]*y[0]
area=lambda poly:sum(cross(w,poly[(i+1)%6]) for i,w in enumerate(poly))/2
D=h*(2*p*q+3*p*a+3*q*a+4*a*a-p*c-q*c-4*a*c)
assert cross(u,v)==D==sum(map(area,placed))
# Every formal convexity check follows from positive side lengths alone.
# For vertex offsets 2,3,4,5 the supporting-edge cross products are these
# positive combinations, using closure in the offset-5 case.
for face in range(4):
    ls=lengths[face//2];poly=polys[face]
    for e in range(6):
        edge=poly[(e+1)%6]-poly[e]
        expected=[ls[e]*ls[(e+1)%6]*h/2,
                  ls[e]*(ls[(e+1)%6]+ls[(e+2)%6])*h/2,
                  ls[e]*(ls[(e+1)%6]+ls[(e+2)%6])*h/2,
                  ls[e]*ls[(e-1)%6]*h/2]
        assert [cross(edge,poly[(e+k)%6]-poly[e]) for k in (2,3,4,5)]==expected

# Special repeated family p=a,q=c. Numeric length labels are distinct for
# c != a; this is an exact finite local-star domain, not a tiling search.
Aword=('a','a','c','b','c','a');Bword=('r','c','b','b','a','a')
pair=lambda x,y:tuple(sorted((x,y)))
corner_graph=lambda word:{pair(word[i-1],word[i]) for i in range(6)}
GA,GB=corner_graph(Aword),corner_graph(Bword)
star=lambda rays:{pair(rays[i-1],rays[i]) for i in range(3)}
all_rays=list(combinations_with_replacement(('a','b','c','r'),3))
assert len(all_rays)==20
valid=[rays for rays in all_rays if star(rays)<=GA|GB]
expected_stars=[('a','a','a'),('a','a','b'),('a','a','c'),('a','a','r'),
                ('a','b','b'),('a','b','c'),('a','c','r'),('b','b','b'),('b','b','c')]
assert valid==expected_stars
monoA=[rays for rays in all_rays if star(rays)<=GA]
monoB=[rays for rays in all_rays if star(rays)<=GB]
assert not any(pair('c','b') in star(rays) for rays in monoA)
assert not any(pair('r','c') in star(rays) for rays in monoB)
special_lengths=[Aword,Aword,Bword,Bword]
used=[]
for cycle in cycles:
    actual_edges={pair(special_lengths[i][e-1],special_lengths[i][e]) for i,e in cycle}
    ray_labels=[rays for rays in valid if star(rays)==actual_edges]
    assert len(ray_labels)==1
    used.append(ray_labels[0])
assert sorted(used)==sorted([expected_stars[i] for i in (0,5,6,8) for repeat in range(2)])

# Two actual full-side mates of native A side0 in the repeated family.
# The accompanying left/right B tiles complete both endpoint stars. These
# finite patches are locally compatible; only the A-mate branch is asserted
# to extend by the retained periodic quotient.
repeat=lambda z:z(a,c,a,c)
A=[vector(S,[repeat(z) for z in w]) for w in polys[0]]
B=[vector(S,[repeat(z) for z in w]) for w in polys[2]]
R4=matrix(K,[[-K(1)/2,h/2],[-h/2,-K(1)/2]])
F=matrix(K,[[-K(1)/2,-h/2],[-h/2,K(1)/2]])
assert R4.det()==1 and F.det()==-1
native_start=A[0];native_end=A[1]
A_mate=[native_end-w for w in A]
B_mate=[R4*w for w in B]
left_A=[B[5]-w for w in B]
left_B=[F*w for w in B]
right=[native_end-B[5]+w for w in B]
assert A_mate[1]==B_mate[0]==native_start
assert A_mate[0]==B_mate[5]==native_end
assert left_A[5]==left_B[0]==native_start and right[5]==native_end
# A has one reflection symmetry; B has none. Quotienting intrinsic polygon
# symmetries cannot identify the branches since their neighbor types differ.
rotate_word=lambda word,k:tuple(word[(i+k)%6] for i in range(6))
reflect_word=lambda word,k:tuple(word[(k-i)%6] for i in range(6))
assert sum(rotate_word(Aword,k)==Aword for k in range(6))==1
assert sum(reflect_word(Aword,k)==Aword for k in range(6))==1
assert sum(rotate_word(Bword,k)==Bword for k in range(6))==1
assert sum(reflect_word(Bword,k)==Bword for k in range(6))==0
assert [vector(S,[a-w[0],w[1]]) for w in A]==[A[i] for i in (1,0,5,4,3,2)]
local_patches=[[A,A_mate,left_A,right],[A,B_mate,left_B,right]]
def same_edge(poly,e,other,f):
    lhs=(poly[e],poly[(e+1)%6]);rhs=(other[f],other[(f+1)%6])
    return lhs==rhs or lhs==(rhs[1],rhs[0])
for patch,contacts in zip(local_patches,
    [[(0,0,1,0),(0,5,2,5),(1,1,2,4),(0,1,3,4),(1,5,3,5)],
     [(0,0,1,5),(0,5,2,5),(1,0,2,0),(0,1,3,4),(1,4,3,5)]]):
    for i,e,j,f in contacts:
        assert same_edge(patch[i],e,patch[j],f)
assert lengths[1][5](a,c,a,c)==a and lengths[1][0](a,c,a,c)==3*a-2*c

# Exact asymmetric fixture (p,q,a,c)=(1,3/4,1,3/4).
fixture=[QQ(1),QQ(3)/4,QQ(1),QQ(3)/4]
evaluate=lambda w:vector(AA,[real(z(*fixture)) for z in w])
actual=[[evaluate(w) for w in poly] for poly in placed]
u0,v0=evaluate(u),evaluate(v)
assert u0==vector(AA,[QQ(7)/2,-AA(3).sqrt()])
assert v0==vector(AA,[QQ(13)/8,QQ(11)/8*AA(3).sqrt()])
assert cross(u0,v0)==QQ(103)/16*AA(3).sqrt()
for i,poly in enumerate(actual):
    ls=[real(length(*fixture)) for length in lengths[i//2]]
    assert min(ls)>0
    for e,w in enumerate(poly):
        edge=poly[(e+1)%6]-w
        assert edge.norm()==ls[e]
        assert all(cross(edge,poly[j]-w)>0 for j in range(6)
                   if j not in (e,(e+1)%6))
        previous=poly[e]-poly[(e-1)%6]
        assert -previous.dot_product(edge)==-ls[e-1]*ls[e]/2
assert sum(map(area,actual))==cross(u0,v0)>0
basis=matrix(AA,[[u0[0],v0[0]],[u0[1],v0[1]]]);inverse=basis.inverse()
boxes=[]
for poly in actual:
    coords=[inverse*w for w in poly]
    boxes.append([(min(w[j] for w in coords),max(w[j] for w in coords)) for j in (0,1)])

def separated(poly,other):
    # Exact separating-axis theorem. Equality means boundary contact only.
    for face in (poly,other):
        for e,w in enumerate(face):
            edge=face[(e+1)%6]-w
            lhs=[cross(edge,z) for z in poly];rhs=[cross(edge,z) for z in other]
            if max(lhs)<=min(rhs) or max(rhs)<=min(lhs):
                return True
    return False

checks=0
overlap_domains=[]
for i,j in product(range(4),repeat=2):
    ranges=[range(int((boxes[i][k][0]-boxes[j][k][1]).ceil()),
                  int((boxes[i][k][1]-boxes[j][k][0]).floor())+1) for k in (0,1)]
    translations=[]
    for n,m in product(*ranges):
        if i==j and n==m==0:
            continue
        translations.append([n,m])
        other=[w+n*u0+m*v0 for w in actual[j]]
        assert separated(actual[i],other),(i,j,n,m)
        checks+=1
    overlap_domains.append({'faces':[i,j],'coordinate_integer_bounds':
                            [[bounds.start,bounds.stop-1] for bounds in ranges],
                            'translations':translations})
patch_checks=0
for patch in local_patches:
    values=[[evaluate(w) for w in poly] for poly in patch]
    for i in range(4):
        for j in range(i+1,4):
            assert separated(values[i],values[j]),('branch',i,j)
            patch_checks+=1
assert patch_checks==12
def point_strings(poly,params=None):
    return [[str(z if params is None else z(*params)) for z in w] for w in poly]
certificate={
    'schema':'hexagon-adjacent-repeat-periodic-cone/v1',
    'source_lemma':'research/lemmas/hexagon-adjacent-repeat-periodic-cone.md',
    'producer':'research/searches/hexagon-adjacent-repeat-periodic-cone.py',
    'coefficient_field':{'h':'positive sqrt(3)','minimal_polynomial':'h^2-3'},
    'formal_free_parameters':['p','q','a','c'],
    'open_cone_inequalities':[str(z)+' > 0' for z in (p,q,a,c,b,d,r,s)],
    'native_side_words':[[str(z) for z in ls] for ls in lengths],
    'dependent_closure_matrix':[['1','0','1','-1'],['0','1','1','-1'],
                                 ['1','0','2','-2'],['0','1','2','-2']],
    'units':[[str(z) for z in w] for w in U],
    'motif_vertices':[point_strings(poly) for poly in placed],
    'periods':[list(map(str,u)),list(map(str,v))],
    'area_covolume':str(D),
    'seams':[{'first':[i,e],'second':[j,f],'shift':[n,m]}
             for (i,e,j,f),(n,m) in zip(pairs,seam_coords)],
    'circular_corner_links':[[list(z) for z in cycle] for cycle in cycles],
    'repeat_subfamily':{
        'specialization':{'p':'a','q':'c'},
        'domain':['a > 0','c > 0','c < 3*a/2','c != a'],
        'distinct_numeric_labels':['a','b=2*a-c','c','r=3*a-2*c'],
        'native_words':[list(Aword),list(Bword)],
        'ray_multiset_domain_size':len(all_rays),
        'legal_ray_multisets':[list(rays) for rays in valid],
        'monohedral_corner_obstructions':{'A':['b','c'],'B':['c','r']},
        'intrinsic_symmetry_counts':{'A':2,'B':1},
        'branched_native_side':['A',0],
        'local_branch_patches':[
            {'mate':['A',0],'vertices':[point_strings(poly) for poly in local_patches[0]],
             'endpoint_third_pairs':[['a','a'],['a','a']],
             'global_extension':'four-face torus constructed in source'},
            {'mate':['B',5],'vertices':[point_strings(poly) for poly in local_patches[1]],
             'endpoint_third_pairs':[['a','r'],['a','a']],
             'reflected_left_filler_matrix':[[str(z) for z in row] for row in F.rows()],
             'scope':'locally compatible whole-tile patch; extension not asserted'}]},
    'exact_fixture':{
        'free_values':list(map(str,fixture)),
        'motif_vertices':[point_strings(poly,fixture) for poly in placed],
        'periods':[[str(z(*fixture)) for z in w] for w in (u,v)],
        'area_covolume':str(D(*fixture)),
        'complete_overlap_domain':overlap_domains,
        'ordered_face_pairs':16,
        'translated_overlap_comparisons':checks,
        'local_branch_pairwise_separations':patch_checks},
    'environment':{'python':platform.python_version(),'sage':SAGE_VERSION}}
print(json.dumps(certificate,indent=2,sort_keys=True))
if not args.json:
    print('PASS general 4D closure: unique b,d,r,s; strict formal convexity;',file=sys.stderr)
    print('PASS 12 polynomial seam equalities; 8 circular triple links; rank2 periods;',file=sys.stderr)
    print('PASS area = covolume polynomial identity; 20 multisets -> 9 legal repeat stars;',file=sys.stderr)
    print('PASS both repeated prototiles have a monohedral corner-star obstruction;',file=sys.stderr)
    print('PASS native A side0: distinct A/B placed mates, both complete endpoint stars;',file=sys.stderr)
    print('PASS 12 exact local-patch separations; intrinsic symmetries A=2,B=1;',file=sys.stderr)
    print('PASS asymmetric fixture a=1,c=3/4:',checks,'complete exact overlap comparisons; density1;',file=sys.stderr)
    print('Python',platform.python_version(),'Sage',SAGE_VERSION,file=sys.stderr)
