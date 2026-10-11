"""Independent exact lift/window test of retained finite geometric rhomb clusters."""
from sage.all import CyclotomicField, QuadraticField, QQ, Polyhedron, matrix, vector
from collections import defaultdict,deque,Counter
from itertools import product,combinations
from pathlib import Path
import json

K=CyclotomicField(10);z=K.gen();phik=z+1/z
F=QuadraticField(5,'rt5');phi=(1+F.gen())/2
basis=matrix(K,[K(1).list(),phik.list()]).transpose()
def real(x):
    sol=basis.solve_right(vector(K,K(x).list()))
    assert all(t in QQ for t in sol)
    return F(sol[0])+F(sol[1])*phi
COS=[real((z**(4*j)+z**(-4*j))/2) for j in range(5)]
SIN=[real((z**(4*j)-z**(-4*j))/(z-1/z)) for j in range(5)]
def iproj(n):return (F(sum(n)),sum(F(n[j])*COS[j] for j in range(5)),sum(F(n[j])*SIN[j] for j in range(5)))
WINDOW=Polyhedron(vertices=[iproj(t) for t in product((0,1),repeat=5)],base_ring=F,backend='field')
FACETS=[tuple(h) for h in WINDOW.inequality_generator()]
assert WINDOW.dim()==3 and len(FACETS)==20
assert all(h[2]!=0 or h[3]!=0 for h in FACETS)
LIFT={z**k:tuple((1 if k<5 else -1) if i==k%5 else 0 for i in range(5)) for k in range(10)}

def cluster(label,row):
    polys=[[K(list(map(QQ,p))) for p in r] for r in row['whole_rhombs']]
    dirs=[0,4,6,7,8] if label=='U' else [0,3,6,7,9]
    parent=[K(0),phik**3,z+z**2+z**3,z**2+z**3,z**3] if label=='U' else [K(0),K(1),1+(1+3*phik)*z**3,2*phik**2*z**3,2*phik*z**4]
    completed=[]
    for i,(word,k) in enumerate(zip(row['side_words'],dirs)):
        x=parent[i]
        for symbol in word:
            y=x+{'u':1,'l':phik,'s':phik-1}[symbol]*z**k
            if symbol!='u':
                apex=x+z**(k+(1 if symbol=='l' else 2))
                completed.append([x,x+y-apex,y,apex])
            x=y
        assert x==parent[(i+1)%5]
    polys+=completed
    adj=defaultdict(list)
    for p in polys:
        for a,b in zip(p,p[1:]+p[:1]):
            h=LIFT[b-a]
            adj[a].append((b,h));adj[b].append((a,tuple(-t for t in h)))
    H={K(0):(0,0,0,0,0)};todo=deque(H)
    while todo:
        a=todo.popleft()
        for b,h in adj[a]:
            hb=tuple(x+y for x,y in zip(H[a],h))
            if b in H:assert H[b]==hb
            else:H[b]=hb;todo.append(b)
    assert len(H)==len(adj)
    # Signed permutation converts z^i basis to rho^(3i) with rho=z^2.
    N={}
    for p,h in H.items():
        n=[0]*5
        for i,t in enumerate(h):n[(3*i)%5]=(-1)**i*t
        N[p]=tuple(n)
        assert sum(h[i]*z**i for i in range(5))==p
        assert sum(n[j]*z**(2*j) for j in range(5))==p
    layers=[sum(n) for n in N.values()]
    return polys,H,N,min(layers),max(layers)


def dual_obstruction(rows):
    # The strongest bound for each of the20 normals suffices.
    grouped={}
    for i,(c,a,b,eps) in enumerate(rows):
        key=(a,b)
        if key not in grouped or c<grouped[key][1]:grouped[key]=(i,c,a,b)
    small=list(grouped.values())
    for subset in combinations(small,2):
        (ix,cx,ax,bx),(iy,cy,ay,by)=subset
        if ax*by-bx*ay!=0:continue
        weights=[abs(ay),abs(ax)] if ax!=0 or ay!=0 else [abs(by),abs(bx)]
        if sum(weights)==0:continue
        if weights[0]*ax+weights[1]*ay!=0 or weights[0]*bx+weights[1]*by!=0:continue
        total=weights[0]*cx+weights[1]*cy
        if total<=0:
            return {'row_indices':[ix,iy],'selected_rows':[[str(cx),str(ax),str(bx)],[str(cy),str(ay),str(by)]],'positive_weights':[str(w) for w in weights],'constant_sum':str(total),
                    'normal_sum':[str(weights[0]*ax+weights[1]*ay),str(weights[0]*bx+weights[1]*by)]}
    for subset in combinations(small,3):
        vectors=[(r[2],r[3]) for r in subset]
        cr=lambda p,q:p[0]*q[1]-p[1]*q[0]
        weights=[cr(vectors[1],vectors[2]),cr(vectors[2],vectors[0]),cr(vectors[0],vectors[1])]
        if all(w<=0 for w in weights):weights=[-w for w in weights]
        if any(w<0 for w in weights) or sum(weights)==0:continue
        assert sum(w*r[2] for w,r in zip(weights,subset))==0
        assert sum(w*r[3] for w,r in zip(weights,subset))==0
        total=sum(w*r[1] for w,r in zip(weights,subset))
        if total<=0:return {'row_indices':[r[0] for r in subset], 'selected_rows':[[str(r[1]),str(r[2]),str(r[3])] for r in subset], 'positive_weights':[str(w) for w in weights],
                             'constant_sum':str(total),'normal_sum':['0','0']}
    raise AssertionError('Missing two-dimensional Farkas witness')

def boundary_lifts(label,words):
    dirs=[0,4,6,7,8] if label=='U' else [0,3,6,7,9]
    parent=[K(0),phik**3,z+z**2+z**3,z**2+z**3,z**3] if label=='U' else [K(0),K(1),1+(1+3*phik)*z**3,2*phik**2*z**3,2*phik*z**4]
    H={K(0):(0,0,0,0,0)}
    def plus(a,b):return tuple(x+y for x,y in zip(a,b))
    def put(p,h):
        if p in H:assert H[p]==h
        else:H[p]=h
    for i,(word,k) in enumerate(zip(words,dirs)):
        x=parent[i];hx=H[x]
        for symbol in word:
            y=x+{'u':1,'l':phik,'s':phik-1}[symbol]*z**k
            steps=[k] if symbol=='u' else [k-1,k+1] if symbol=='l' else [k-2,k+2]
            dh=tuple(sum(LIFT[z**t][j] for t in steps) for j in range(5))
            hy=plus(hx,dh);put(y,hy)
            if symbol!='u':
                a=x+z**(k+(1 if symbol=='l' else 2));ha=plus(hx,LIFT[z**(k+(1 if symbol=='l' else 2))])
                put(a,ha);put(x+y-a,tuple(hx[j]+hy[j]-ha[j] for j in range(5)))
            x,hx=y,hy
        assert x==parent[(i+1)%5]
    assert H[K(0)]==(0,0,0,0,0)
    N={}
    for p,h in H.items():
        n=[0]*5
        for i,t in enumerate(h):n[3*i%5]=(-1)**i*t
        assert sum(h[i]*z**i for i in range(5))==p
        N[p]=tuple(n)
    vals=[sum(n) for n in N.values()]
    return H,N,min(vals),max(vals)


def region(N,lo,hi):
    if hi-lo>3:return {'verdict':'fails Penrose four-layer necessity'}
    internal=[iproj(n) for n in N.values()]
    cases=[]
    for m in range(hi-4,lo):
        rows=[]
        for k,a,b in internal:
            for h0,hk,ha,hb in FACETS:
                rows.append([h0+hk*(k-m)+ha*a+hb*b,-ha,-hb,F(-1)])
        rows+=[[F(0),F(0),F(0),F(1)],[F(1),F(0),F(0),F(-1)]]
        poly=Polyhedron(ieqs=rows,base_ring=F,backend='field')
        pts=list(poly.vertex_generator())
        if not pts:
            cases.append({'integer_intercept_sum':m,'verdict':'closed-window intersection empty','dual_obstruction':dual_obstruction(rows[:-2])})
            continue
        best=max(pts,key=lambda p:p[2]);margin=best[2]
        record={'integer_intercept_sum':m,'star_shift':[str(best[0]),str(best[1])], 'margin':str(margin),
                'verdict':'strict shifted-window witness' if margin>0 else 'only boundary-window feasibility'}
        if margin>0:
            assert all(r[0]+r[1]*best[0]+r[2]*best[1]>=margin for r in rows[:-2])
            record['facet_slack_at_shift_min']=str(min(r[0]+r[1]*best[0]+r[2]*best[1] for r in rows[:-2]))
        if margin<=0:record['dual_obstruction']=dual_obstruction(rows[:-2])
        cases.append(record)
    return {'verdict':'strict shifted-window witness' if any(c['verdict']=='strict shifted-window witness' for c in cases) else 'no strict shifted-window witness','cases':cases}

if __name__=='__main__':
    source=json.loads(Path('research/certificates/pentagrid-robinson-residual-rhombs.json').read_text())
    out={'scope':'All retained SAT geometric assemblies, each completed with ALL mandatory boundary parent rhombs; exact source-height and shifted-window test, no macro partition/shape forcing',
         'primary_dependency':'Fernique-Lutfalla arXiv2211.08239v2 Section2.3 Definition2 and integer-intercept Penrose specialization',
         'window_facets':[[str(t) for t in h] for h in FACETS],'fixtures':{}}
    for label,rec in source['fixtures'].items():
        rows=[];hist=Counter();first_global=None
        for ix,row in enumerate(rec['results']):
            if not row['verdict'].startswith('SAT'):continue
            polys,H,N,lo,hi=cluster(label,row);hist[hi-lo]+=1
            reg=region(N,lo,hi)
            result={'source_row_index':ix,'side_words':row['side_words'],'whole_rhomb_count':len(polys),
                    'vertex_count':len(H),'layer_interval':[lo,hi],'layer_span':hi-lo,'window_gate':reg}
            if ix==0 or hi-lo<=3:
                result['lifted_vertices']=[{'physical_coefficients':[str(t) for t in p.list()], 'H_z_basis':H[p], 'N_rho_basis':N[p]} for p in sorted(H,key=lambda p:tuple(p.list()))]
            rows.append(result)
            if first_global is None and reg['verdict']=='strict shifted-window witness':first_global=result
        out['fixtures'][label]={'retained_SAT_rows':len(rows),'full_cluster_layer_span_histogram':{str(k):v for k,v in sorted(hist.items())},
                                 'four_layer_pass_count':sum(r['layer_span']<=3 for r in rows),
                                 'strict_window_pass_count':sum(r['window_gate']['verdict']=='strict shifted-window witness' for r in rows),
                                 'first_global_source_candidate':first_global,'results':rows}
        print(label,len(rows),'layer histogram',dict(hist),'strict-window passes',out['fixtures'][label]['strict_window_pass_count'],flush=True)
    boundary_source=json.loads(Path('research/certificates/pentagrid-robinson-boundary-completion.json').read_text())
    out['boundary_only']={}
    for label,rec in boundary_source['fixtures'].items():
        rows=[];hist=Counter()
        for ix,words in enumerate(rec['surviving_boundary_words']):
            H,N,lo,hi=boundary_lifts(label,words);hist[hi-lo]+=1
            reg=region(N,lo,hi)
            result={'source_boundary_index':ix,'side_words':words,'vertex_count':len(H),'layer_interval':[lo,hi], 'layer_span':hi-lo,'window_gate':reg}
            if hi-lo<=3:result['lifted_vertices']=[{'physical_coefficients':[str(t) for t in p.list()], 'H_z_basis':H[p], 'N_rho_basis':N[p]} for p in sorted(H,key=lambda p:tuple(p.list()))]
            rows.append(result)
        out['boundary_only'][label]={'boundary_count':len(rows),'layer_span_histogram':{str(k):v for k,v in sorted(hist.items())},'strict_window_pass_count':sum(r['window_gate']['verdict']=='strict shifted-window witness' for r in rows),'results':rows}
        print(label,'boundary-only',len(rows),'strict-window passes',out['boundary_only'][label]['strict_window_pass_count'],flush=True)
    Path('research/certificates/pentagrid-robinson-penrose-window.json').write_text(json.dumps(out,indent=2)+'\n')
