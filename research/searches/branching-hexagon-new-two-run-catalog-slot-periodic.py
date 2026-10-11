"""Exact full-native-slot balance in all81 ordered two-run catalog cases.
Read-only normal replay; --output explicitly retains the complete result.
No finite assembly failure is an infinite impossibility result.
"""
import argparse,json,itertools
from pathlib import Path
from collections import Counter,defaultdict
from fractions import Fraction
from sage.all import QQbar,AA
import z3
z=QQbar.zeta(24)

def canonical(t):return min(tuple(t[i:]+t[:i]) for i in range(len(t)))
def geometry(quad):
    a,b,c,d=quad
    P=[QQbar(1),z**((180-a)//15),z**((360-a-b)//15)]
    Q=[QQbar(1),z**((180-c)//15),z**((360-c-d)//15)]
    ps,qs=sum(P),sum(Q);p=AA((qs*qs.conjugate()).real()/(ps*ps.conjugate()).real()).sqrt()
    if p==1:return None
    R=-QQbar(p)*ps/qs
    edges=[[QQbar(p)*z**i if k%2==0 else z**i for k,i in enumerate((0,5,8,13,16,21))],
           [QQbar(p)*x for x in P]+[R*x for x in Q]]
    labels=[['p','q']*3,['p']*3+['q']*3]
    angles=[];points=[]
    for es,ls in zip(edges,labels):
        pp=[];v=QQbar(0)
        for e in es:pp.append(v);v+=e
        assert v==0
        assert all((es[i].conjugate()*(pp[j]-pp[i])).imag()>0 for i in range(6) for j in range(6) if j not in(i,(i+1)%6))
        units=[es[i]/(QQbar(p) if ls[i]=='p' else 1) for i in range(6)]
        angles.extend([-((units[i]/units[i-1]).conjugate()) for i in range(6)])
        points.append(pp)
    return p,labels,angles,points

def balance(quad):
    g=geometry(quad)
    if g is None:return {'quad':quad,'status':'equal-lengths'}
    p,labels,angles,points=g;corners=[(s,i) for s in(0,1) for i in range(6)]
    legal=[]
    for tri in itertools.combinations_with_replacement(range(12),3):
        if angles[tri[0]]*angles[tri[1]]*angles[tri[2]]==1:legal.append(tri)
    oriented=[]
    for cid,(s,i) in enumerate(corners):
        out,prev=labels[s][i],labels[s][i-1]
        oriented.extend([(cid,0,out,prev,(s,i),(s,(i-1)%6),0,1),
                         (cid,1,prev,out,(s,(i-1)%6),(s,i),1,0)])
    stars=set()
    for tri in legal:
        for order in set(itertools.permutations(tri)):
            for flips in itertools.product((0,1),repeat=3):
                t=[2*c+f for c,f in zip(order,flips)]
                if all(oriented[t[i]][3]==oriented[t[(i+1)%3]][2] for i in range(3)):stars.add(canonical(t))
    stars=sorted(stars);C=[];S=[];keys=set()
    for star in stars:
        cc=Counter();ss=Counter()
        for i,o in enumerate(star):
            a=oriented[o];b=oriented[star[(i+1)%3]];cc[a[0]]+=1
            x,y=a[5],b[4];px,py=a[7],b[6]
            if x==y and px!=py:continue
            if x<=y:key=(x,y,px^py);sign=1 if px==0 else -1
            else:key=(y,x,px^py);sign=1 if py==0 else -1
            ss[key]+=sign
        C.append(cc);S.append(ss);keys.update(ss)
    keys=sorted(keys);W=[z3.Real('W'+str(i)) for i in range(12)];Y=[z3.Real('Y'+str(i)) for i in range(len(keys))]
    f=z3.Reals('FA FB');x=[z3.Real('X'+str(i)) for i in range(len(stars))]
    solver=z3.Solver();solver.add(*(v>=0 for v in list(f)+x),sum(f)==1)
    for c in range(12):solver.add(sum(x[i]*row[c] for i,row in enumerate(C) if row[c])==f[c//6])
    for key in keys:solver.add(sum(x[i]*row[key] for i,row in enumerate(S) if row[key])==0)
    status=solver.check();r={'quad':quad,'status':str(status),'corner_slots':corners,'oriented_stars':stars,
                           'star_corner_counts':[dict(c) for c in C],'seam_keys':keys,
                           'star_seam_counts':[[s[k] for k in keys] for s in S]}
    frac=lambda e,m:str(Fraction(m.eval(e,model_completion=True).numerator_as_long(),m.eval(e,model_completion=True).denominator_as_long()))
    if status==z3.sat:
        solver.push();solver.add(f[0]>0,f[1]>0);mixed=solver.check();r['mixed_status']=str(mixed)
        if mixed!=z3.sat:solver.pop();assert solver.check()==z3.sat
        m=solver.model();r['species_frequencies']=[frac(v,m) for v in f];r['star_frequencies']=[frac(v,m) for v in x]
    elif status==z3.unsat:
        kid=dict(zip(keys,Y));dual=z3.Solver()
        for cc,ss in zip(C,S):dual.add(sum(W[c]*v for c,v in cc.items())+sum(kid[k]*v for k,v in ss.items() if v)>=0)
        for s in(0,1):dual.add(sum(W[c] for c in range(6*s,6*s+6))<=-1)
        assert dual.check()==z3.sat;m=dual.model();r['corner_dual']=[frac(v,m) for v in W];r['seam_dual']=[frac(v,m) for v in Y]
        ww=list(map(Fraction,r['corner_dual']));yy=list(map(Fraction,r['seam_dual']));yy=dict(zip(keys,yy))
        assert all(sum(ww[c]*v for c,v in cc.items())+sum(yy[k]*v for k,v in ss.items())>=0 for cc,ss in zip(C,S))
        assert all(sum(ww[c] for c in range(6*s,6*s+6))<=-1 for s in(0,1))
    else:raise RuntimeError(status)
    print(quad,str(status),'mixed',r.get('mixed_status'),'stars',len(stars),'seams',len(keys),'frequencies',r.get('species_frequencies'),flush=True)
    return r

def main(output=None):
    records=[]
    for quad in itertools.product((90,120,150),repeat=4):records.append(balance(quad))
    r={'domain':'all81 ordered (B1,B2,B4,B5) in {90,120,150}^4, A delta15, q1; complete trivalent native-slot assembly balance','records':records}
    if output:Path(output).write_text(json.dumps(r,indent=2)+'\n')
    print('COUNTS',dict(Counter(row['status'] for row in records)))
    return r
if __name__=='__main__':
    p=argparse.ArgumentParser();p.add_argument('--output');a=p.parse_args();main(a.output)
