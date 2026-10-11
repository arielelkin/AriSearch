"""One mirror-V dimer octagon and two congruent W faces: exact torus search."""
from sage.all import QuadraticField, CyclotomicField, Polyhedron, matrix, vector
from math import prod
import json
from pathlib import Path

F=QuadraticField(5,'rt5');phi=(1+F.gen())/2
K=CyclotomicField(10);z=K.gen();phik=z+1/z
basis=matrix(K,[K(1).list(),phik.list()]).transpose()
def to_real(x):
    x=K(x);sol=basis.solve_right(vector(K,x.list()))
    assert all(t in __import__('sage.all',fromlist=['QQ']).QQ for t in sol)
    return F(sol[0])+F(sol[1])*phi
cos=[to_real((z**(2*i)+z**(-2*i))/2) for i in range(5)]
sin=[to_real((z**(2*i)-z**(-2*i))/(z-1/z)) for i in range(5)]
assert all(t in F for t in cos+sin)
# Q's boundary starts at an endpoint of the deleted D seam.
Qangles=[4,4,3,4,4,4,3,4]  # vertex angles; afterword=(4,3,4,4,4,3,4,4)
Qlabels=[0,1,1,0,0,1,1,0]
SIZES=[8,5,5];OFF=[0,8,13]
def nxt(i):
    f=0 if i<8 else 1 if i<13 else 2
    return OFF[f]+(i-OFF[f]+1)%SIZES[f]
def find(i,p):
    while p[i]!=i:i=p[i]
    return i

def canonical(p):
    roots=[find(i,p) for i in range(7)]
    remap={};out=[]
    for x in roots:
        if x not in remap:remap[x]=len(remap)
        out.append(remap[x])
    return tuple(out)

cache={}
metric_checks=0
def metrics(p):
    global metric_checks
    part=canonical(p)
    if part in cache:return cache[part]
    metric_checks+=1
    k=max(part)+1
    # k length classes and one delta; b=1, E-phi*b>=delta,
    # all length classes>=delta, delta in[0,1].
    eq=[]
    for vals in (cos,sin):
        row=[F(0)]*(k+2)
        for i,v in enumerate(vals):row[part[2+i]+1]+=v
        eq.append(row)
    row=[F(-1)]+[F(0)]*(k+1);row[part[0]+1]=1;eq.append(row)
    ie=[]
    for q in range(k):
        row=[F(0)]*(k+2);row[q+1]=1;row[-1]=-1;ie.append(row)
    row=[F(0)]*(k+2);row[part[1]+1]=1;row[part[0]+1]-=phi;row[-1]=-1;ie.append(row)
    ie.append([F(0)]+[F(0)]*k+[F(1)])
    ie.append([F(1)]+[F(0)]*k+[F(-1)])
    poly=Polyhedron(eqns=eq,ieqs=ie,base_ring=F,backend='field')
    pts=list(poly.vertex_generator())
    if not pts or max(v[-1] for v in pts)<=0:
        cache[part]=None;return None
    v=max(pts,key=lambda v:v[-1])
    out={'length_partition':list(part),'b':str(v[part[0]]),'E':str(v[part[1]]),
         'W_sides':[str(v[part[2+i]]) for i in range(5)],'margin':str(v[-1])}
    cache[part]=out;return out

branches=0;leaves=0

def search(parity):
    labels=Qlabels+list(range(2,7))+(list(reversed(range(2,7))) if parity else list(range(2,7)))
    angles=Qangles+[3]*10
    def rec(rem,vp,vs,lp,pairs):
        global branches,leaves
        if not rem:
            leaves+=1
            roots={find(i,vp) for i in range(18)}
            if len(roots)!=6 or any(vs[r]!=10 for r in roots):return None
            reach={0}
            for _ in range(3):
                for i,j in pairs:
                    fi=0 if i<8 else 1 if i<13 else 2
                    fj=0 if j<8 else 1 if j<13 else 2
                    if fi in reach:reach.add(fj)
                    if fj in reach:reach.add(fi)
            if len(reach)!=3:return None
            m=metrics(lp)
            if m is None:return None
            links=[[i for i in range(18) if find(i,vp)==r] for r in sorted(roots)]
            return {'W_second_reflected':bool(parity),'pairs':pairs,'corner_classes':links,'metric':m}
        i=rem[0]
        for j in rem[1:]:
            branches+=1
            lp2=lp[:]
            a,b=find(labels[i],lp2),find(labels[j],lp2)
            lp2[b]=a
            if find(0,lp2)==find(1,lp2):continue
            vp2=vp[:];vs2=vs[:];okay=True
            for a,b in [(i,nxt(j)),(nxt(i),j)]:
                a,b=find(a,vp2),find(b,vp2)
                if a!=b:
                    vp2[b]=a;vs2[a]+=vs2[b]
                if vs2[a]>10:okay=False;break
            if not okay:continue
            ans=rec(tuple(t for t in rem if t not in (i,j)),vp2,vs2,lp2,pairs+[(i,j)])
            if ans:return ans
        return None
    return rec(tuple(range(18)),list(range(18)),angles,list(range(7)),[])

if __name__=='__main__':
    result=None
    for parity in [False,True]:
        result=search(parity)
        if result:break
    out={'domain':'one mirror-V dimer octagon and two congruent108-equiangular W pentagons; full-edge oriented quotient; all matchings and relative W reflection; V b>0,E>phi*b; positive W metrics exact',
         'status':'witness' if result else 'complete_domain_no_witness','complete':result is None,
         'pairing_domain_all_parities':2*prod(range(1,18,2)),
         'branches':branches,'completed_angular_matches':leaves,'distinct_exact_metric_checks':metric_checks,
         'witness':result}
    Path('research/certificates/pentagrid-v-w-dimer-torus.json').write_text(json.dumps(out,indent=2)+'\n')
    print(json.dumps(out,indent=2),flush=True)
