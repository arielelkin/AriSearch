"""Complete exact resonance domain for Q=(a,d,b,c), normalized a=1.
Normal replay is read-only; --output explicitly writes the domain certificate.
"""
import argparse,json
from pathlib import Path
from itertools import combinations
from sage.all import QuadraticField,AA
K=QuadraticField(3,'w',embedding=AA(3).sqrt());w=K.gen()

def main(output=None):
    # A linear metric is encoded as constant + slope*k, k=b/a.
    a=(K(1),K(0));b=(K(0),K(1));c=((3+w)/4,(1-w)/4);d=((3-w)/4,(1+w)/4)
    e=((w-1)/2,(w-1)/2);f=((w-5)/4,(1+3*w)/4)
    add=lambda u,v:tuple(x+y for x,y in zip(u,v))
    sums={'2a':add(a,a),'2b':add(b,b),'2c':add(c,c),'2d':add(d,d),'a+c':add(a,c),'b+d':add(b,d)}
    lo=(5-w)/(1+3*w);hi=(3+w)/(w-1)
    collisions=[]
    for (name,u),(other,v) in combinations(sums.items(),2):
        assert u[1]!=v[1]
        root=(v[0]-u[0])/(u[1]-v[1]);assert root==1
        collisions.append((name,other))
    hits={};all_comparisons=[]
    for name,u in (('e',e),('f',f)):
        for other,v in sums.items():
            assert u[1]!=v[1]
            root=(v[0]-u[0])/(u[1]-v[1])
            valid=lo<root<hi and root!=1
            all_comparisons.append((name,other,root,valid))
            if valid:hits.setdefault(root,[]).append((name,other))
    expected={(28*w+13)/37:[('f','2c')],w:[('f','a+c')],(20*w-11)/13:[('f','2a')],
              1+w:[('e','2c')],1+4*w/3:[('e','a+c')],1+2*w:[('e','2a')]}
    assert hits==expected
    values=lambda k:[u[0]+u[1]*k for u in (a,b,c,d,e,f)]
    geometry=[]
    for k in sorted(hits):
        aa,bb,cc,dd,ee,ff=values(k)
        assert 0<cc<aa<dd<bb and ee>0 and ff>0 and ee!=ff
        for label,word in [('P',(aa,bb,cc,dd,ee)),('Q',(aa,dd,bb,cc,ff))]:
            A,B,C,D,E=word
            assert E==w*C+D-2*A and B-C==w*(D-A)
            pts=((K(0),K(0)),(A,K(0)),(A,B),(A-w*C/2,B+C/2),(-E/2,w*E/2))
            for i in range(5):
                edge=tuple(pts[(i+1)%5][j]-pts[i][j] for j in range(2))
                assert sum(x*x for x in edge)==word[i]**2
                for h in range(5):
                    if h not in (i,(i+1)%5):
                        vec=tuple(pts[h][j]-pts[i][j] for j in range(2))
                        assert edge[0]*vec[1]-edge[1]*vec[0]>0
        geometry.append(k)
    coeff=lambda q:[str(x) for x in q.list()]
    cert={'field':'Q(w),w^2=3,1<w<2','positive_bounds':[coeff(lo),coeff(hi)],
          'linear_metrics':{n:[coeff(x) for x in u] for n,u in zip(('a','b','c','d','e','f'),(a,b,c,d,e,f))},
          'event_sum_collisions_only_at_one':collisions,
          'all_host_comparisons':[(n,m,coeff(q),valid) for n,m,q,valid in all_comparisons],
          'admissible_resonances':[(coeff(k),hits[k]) for k in sorted(hits)],
          'geometry_verified_ratios':[coeff(k) for k in geometry]}
    if output:Path(output).write_text(json.dumps(cert,indent=2)+'\n')
    print('PASS complete alternate Cairo domain: positive cone;15 event comparisons;12 host comparisons; exactly6 resonances; all12 exact polygons strictly convex')

if __name__=='__main__':
    parser=argparse.ArgumentParser();parser.add_argument('--output');args=parser.parse_args();main(args.output)
