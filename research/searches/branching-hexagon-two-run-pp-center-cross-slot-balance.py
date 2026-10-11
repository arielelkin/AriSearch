"""Complete exceptional-equation arrangement plus fullnative-slot LP envelope.
The angle envelope may include unrealized metric strata; SAT is not a tiling.
Read-only normally; explicit--output retains fullrecords. No timeout is UNSAT.
"""
import argparse,json,itertools,importlib.util
from pathlib import Path
from collections import Counter
from fractions import Fraction
from sage.all import QQ,matrix,vector
import z3
labels=[['p','q']*3,['p']*3+['q']*3]
angles=[(120,1,0,0),(120,-1,0,0)]*3+[(240,1,-1,0),(120,0,0,0),(120,0,0,0),(240,-1,0,-1),(0,0,1,0),(0,0,0,1)]
corners=[(s,i) for s in(0,1) for i in range(6)]
def cyc(t):return min(tuple(t[i:]+t[:i]) for i in range(len(t)))
def fraction(e,m):
    x=m.eval(e,model_completion=True);return str(Fraction(x.numerator_as_long(),x.denominator_as_long()))
def model(flat,index):
    space=flat.row_space();legal=[]
    for tri in itertools.combinations_with_replacement(range(12),3):
        v=[sum(angles[c][j] for c in tri) for j in range(4)];v[0]-=360
        if vector(QQ,v) in space and any(c<6 for c in tri):legal.append(tri)
    oriented=[]
    for cid,(s,i) in enumerate(corners):
        out,prev=labels[s][i],labels[s][i-1]
        oriented.extend([(cid,0,out,prev,(s,i),(s,(i-1)%6),0,1),(cid,1,prev,out,(s,(i-1)%6),(s,i),1,0)])
    stars=set()
    for tri in legal:
        for order in set(itertools.permutations(tri)):
            for flips in itertools.product((0,1),repeat=3):
                t=[2*c+f for c,f in zip(order,flips)]
                if all(oriented[t[i]][3]==oriented[t[(i+1)%3]][2] for i in range(3)):stars.add(cyc(t))
    stars=sorted(stars);C=[];S=[];keys=set()
    for star in stars:
        cc=Counter();ss=Counter()
        for i,o in enumerate(star):
            a=oriented[o];b=oriented[star[(i+1)%3]];cc[a[0]]+=1;x,y=a[5],b[4];px,py=a[7],b[6]
            if x==y and px!=py:continue
            if x<=y:key=(x,y,px^py);sign=1 if px==0 else -1
            else:key=(y,x,px^py);sign=1 if py==0 else -1
            ss[key]+=sign
        C.append(cc);S.append(ss);keys.update(ss)
    keys=sorted(keys);f=z3.Reals('FA FB');x=[z3.Real('X'+str(i)) for i in range(len(stars))]
    solver=z3.Solver();solver.set(timeout=10000);solver.add(*(v>=0 for v in list(f)+x),sum(f)==1)
    for c in range(12):solver.add(sum(x[i]*row[c] for i,row in enumerate(C) if row[c])==f[c//6])
    for key in keys:solver.add(sum(x[i]*row[key] for i,row in enumerate(S) if row[key])==0)
    status=solver.check();r={'index':index,'status':str(status),'oriented_stars':stars,'star_corner_counts':[dict(c) for c in C],
                            'seam_keys':keys,'star_seam_counts':[[s[k] for k in keys] for s in S]}
    if status==z3.sat:
        solver.push();solver.add(f[0]>0,f[1]>0);mixed=solver.check();r['mixed_status']=str(mixed)
        if mixed!=z3.sat:solver.pop();assert solver.check()==z3.sat
        m=solver.model();r['species_frequencies']=[fraction(v,m) for v in f];r['star_frequencies']=[fraction(v,m) for v in x]
        ff=list(map(Fraction,r['species_frequencies']));xx=list(map(Fraction,r['star_frequencies']));assert sum(ff)==1 and min(ff+xx)>=0
        assert all(sum(xx[i]*row[c] for i,row in enumerate(C))==ff[c//6] for c in range(12))
        assert all(sum(xx[i]*row[k] for i,row in enumerate(S))==0 for k in keys)
    elif status==z3.unsat:
        W=[z3.Real('W'+str(i)) for i in range(12)];Y=[z3.Real('Y'+str(i)) for i in range(len(keys))];kid=dict(zip(keys,Y));dual=z3.Solver();dual.set(timeout=10000)
        for cc,ss in zip(C,S):dual.add(sum(W[c]*v for c,v in cc.items())+sum(kid[k]*v for k,v in ss.items() if v)>=0)
        for s in(0,1):dual.add(sum(W[c] for c in range(6*s,6*s+6))<=-1)
        ds=dual.check();r['dual_status']=str(ds)
        if ds==z3.sat:
            m=dual.model();r['corner_dual']=[fraction(v,m) for v in W];r['seam_dual']=[fraction(v,m) for v in Y]
            ww=list(map(Fraction,r['corner_dual']));yy=dict(zip(keys,map(Fraction,r['seam_dual'])))
            assert all(sum(ww[c]*v for c,v in cc.items())+sum(yy[k]*v for k,v in ss.items())>=0 for cc,ss in zip(C,S))
            assert all(sum(ww[c] for c in range(6*s,6*s+6))<=-1 for s in(0,1))
        else:r['status']='unknown';r['reason']='dual not retained:'+str(ds)
    else:r['reason']=solver.reason_unknown()
    print('stratum',index,'rank',flat.nrows(),r['status'],'stars',len(stars),'seams',len(keys),'f',r.get('species_frequencies'),flush=True)
    return r

def run(output=None):
    rec=model(matrix(QQ,0,4),0)
    out={'scope':'genericcenter-cross four mixedstar identities;allpAB actualsaturatedlimit;homppstars omitted onlyunderseparateprovenlimit;extraanglespecials notcovered','record':rec}
    if output:Path(output).write_text(json.dumps(out,indent=2)+'\n')
    return out
if __name__=='__main__':
    parser=argparse.ArgumentParser();parser.add_argument('--output');args=parser.parse_args();run(args.output)
