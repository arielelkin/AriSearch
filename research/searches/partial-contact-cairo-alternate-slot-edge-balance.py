"""Necessary actual-slot star and two-ended seam frequency at f2a.
Full whole/T variants; no extension is inferred from feasible marginals.
Read-only normal runs; --output explicitly retains a certificate.
"""
import argparse,json,lzma,runpy
from pathlib import Path
from itertools import product
from collections import Counter,defaultdict
from fractions import Fraction
import z3
helper=runpy.run_path(str(Path(__file__).with_name('partial-contact-cairo-alternate-endpoint-marginals.py')))


def canonical(cycle):
    return min(tuple(cycle[i:]+cycle[:i]) for i in range(len(cycle)))


def main(output=None):
    variants=helper['variants']('f2a')
    corner_records=[];index={}
    for s,row in enumerate(variants):
        # Recreate directed sides from an ordered corner-kind list. Kinds
        # have their sides sorted, so rebuild the actual reference side
        # lengths using the variant's flags and exact metric separately.
        species,sa,sb,cut,_=row
        w=helper['w'];a=helper['K'](1);b=helper['RATIOS']['f2a']
        c=((3+w)+(1-w)*b)/4;d=((3-w)+(1+w)*b)/4;e=(w-1)*(1+b)/2;f=2*a
        vals={'a':a,'b':b,'c':c,'d':d,'e':e,'f':f,'h':a-c,'j':b-d}
        if species=='P':labels=['a','b','c','d','e'];angs=[120,90,120,90,120]
        else:
            labels=['a','d','b','c']+(['f'] if cut==-1 else ['a','a'])
            angs=[120,90,120,90,120]+([] if cut==-1 else [180])
        edges=[];angles=[]
        for i,label in enumerate(labels):
            pieces=[label]
            if i==0 and sa:pieces=['c','h']
            if label=='b' and i<4 and sb:pieces=['j','d'] if species=='P' else ['d','j']
            for j,piece in enumerate(pieces):edges.append(vals[piece]);angles.append(angs[i] if j==0 else 180)
        n=len(edges)
        colors=[(edges[i],int(angles[i]==120)+int(angles[(i+1)%n]==120)) for i in range(n)]
        for i,angle in enumerate(angles):
            cid=len(corner_records);index[s,i]=cid
            corner_records.append((s,i,angle,colors[i],colors[i-1],n))
    oriented=[]
    for cid,(s,i,ang,out,prev,n) in enumerate(corner_records):
        oriented.extend(((cid,0,ang,out,prev,(s,i),(s,(i-1)%n),0,1),
                         (cid,1,ang,prev,out,(s,(i-1)%n),(s,i),1,0)))
    by_first=defaultdict(list)
    for k,entry in enumerate(oriented):by_first[entry[3]].append(k)
    star_set=set()
    def extend(chain,total):
        if total==360:
            if len(chain) not in (3,4):return
            last,first=oriented[chain[-1]],oriented[chain[0]]
            if last[4]!=first[3]:return
            if last[2]==first[2]==90 and last[4][1]!=1:return
            star_set.add(canonical(chain));return
        if total>360 or len(chain)>=4:return
        last=oriented[chain[-1]]
        for nxt in by_first[last[4]]:
            entry=oriented[nxt]
            if last[2]==entry[2]==90 and last[4][1]!=1:continue
            extend(chain+[nxt],total+entry[2])
    for start in range(len(oriented)):extend([start],oriented[start][2])
    stars=sorted(star_set)
    print("Generated actual-slot stars",len(stars),flush=True)
    seam_features=[];seam_keys=set();star_corners=[]
    for cycle in stars:
        ccounts=Counter();seams=Counter()
        for i,oid in enumerate(cycle):
            entry=oriented[oid];nextentry=oriented[cycle[(i+1)%len(cycle)]]
            ccounts[entry[0]]+=1
            # Shared ray is last side of current, first side of next.
            x,y=entry[6],nextentry[5];px,py=entry[8],nextentry[7]
            if x<=y:key=(x,y,px^py);sign=1 if px==0 else -1
            else:key=(y,x,px^py);sign=1 if py==0 else -1
            if x==y and px!=py:
                continue  # identical slot pair has no distinguished end
            seams[key]+=sign
        seam_features.append(seams);seam_keys.update(seams);star_corners.append(ccounts)
    fs=[z3.Real('f'+str(i)) for i in range(len(variants))]
    xs=[z3.Real('x'+str(i)) for i in range(len(stars))]
    solver=z3.Solver();solver.add(*(x>=0 for x in fs+xs),sum(fs)==1)
    corner_columns=defaultdict(list);seam_columns=defaultdict(list)
    for j,(corners,seams) in enumerate(zip(star_corners,seam_features)):
        for c,v in corners.items():
            if v:corner_columns[c].append((j,v))
        for key,v in seams.items():
            if v:seam_columns[key].append((j,v))
    for cid,entry in enumerate(corner_records):solver.add(sum(xs[j]*v for j,v in corner_columns[cid])==fs[entry[0]])
    for key in seam_keys:solver.add(sum(xs[j]*v for j,v in seam_columns[key])==0)
    print("Solving exact seam system",len(stars),"variables and",len(seam_keys),"seam equations",flush=True)
    result=solver.check()
    def frac(expr,model):
        v=model.eval(expr,model_completion=True)
        return str(Fraction(v.numerator_as_long(),v.denominator_as_long()))
    record={'kind':'f2a','variants':[row[:4] for row in variants],
            'corners':[(s,i,ang) for s,i,ang,*rest in corner_records],
            'oriented_stars':stars,'star_corner_counts':[dict(cs) for cs in star_corners],
            'seam_keys':sorted(seam_keys),
            'star_seam_counts':[[cs[key] for key in sorted(seam_keys)] for cs in seam_features],
            'result':str(result)}
    if result==z3.sat:
        m=solver.model();record['type_frequencies']=[frac(f,m) for f in fs];record['star_frequencies']=[frac(x,m) for x in xs]
        print('types',[(row[:4],record['type_frequencies'][i]) for i,row in enumerate(variants) if record['type_frequencies'][i]!='0'])
    elif result==z3.unsat:
        # Equation feature vector of a star consists of corner counts and
        # signed seam features. Tile feature vectors have one per corner.
        ws=[z3.Real('w'+str(i)) for i in range(len(corner_records))]
        ys=[z3.Real('y'+str(i)) for i in range(len(seam_keys))];keys=sorted(seam_keys)
        dual=z3.Solver();ykeys=dict(zip(keys,ys))
        for ccounts,seams in zip(star_corners,seam_features):
            dual.add(sum(ws[c]*v for c,v in ccounts.items())+sum(ykeys[k]*v for k,v in seams.items() if v)>=0)
        for s,row in enumerate(variants):dual.add(sum(ws[i] for i,c in enumerate(corner_records) if c[0]==s)<=-1)
        assert dual.check()==z3.sat;m=dual.model();record['corner_dual']=[frac(v,m) for v in ws];record['seam_dual']=[frac(v,m) for v in ys]
    else:raise RuntimeError(result)
    if output:
        text=json.dumps(record,indent=2)+'\n'
        if output.endswith('.xz'):
            with lzma.open(output,'wt') as f:f.write(text)
        else:Path(output).write_text(text)
    print('f2a actual-slot two-ended seam system',result,'variants',len(variants),'typed corners',len(corner_records),'oriented stars',len(stars),'seam types',len(seam_keys))

if __name__=='__main__':
    parser=argparse.ArgumentParser();parser.add_argument('--output');args=parser.parse_args();main(args.output)
