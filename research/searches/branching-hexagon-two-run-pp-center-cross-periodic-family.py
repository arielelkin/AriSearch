"""Exact new pp-center periodic family on the existing indexed four-face carrier.
Read-only replay normally; writes require explicit --output.
"""
import argparse,json
from pathlib import Path
from collections import defaultdict,deque
from sage.all import CyclotomicField,PolynomialRing,QQbar,AA,QQ,ZZ,matrix,vector,lcm
K=CyclotomicField(24);zk=K.gen();ik=zk**6
C=(zk+zk**-1)/2;S=(zk-zk**-1)/(2*ik)
R=PolynomialRing(K,'X');X=R.gen();L=K.extension(X**2-(1+S*S),'k');k=L.gen();z=L(zk);ii=L(ik)
p=(k-L(S))/2;psiunit=(-2*p/z+ii)/(1+ii)
zembed=QQbar.zeta(24)
def baseembed(x):return sum(QQ(c)*zembed**i for i,c in enumerate(K(x).list()))
kembed=baseembed(1+S*S).sqrt();assert AA(kembed.real())>0 and kembed.imag()==0
def embed(x):return sum(baseembed(c)*kembed**i for i,c in enumerate(L(x).list()))
def conj(x):return sum(L(c.conjugate())*k**i for i,c in enumerate(L(x).list()))
def cross(x,y):return (conj(x)*y-x*conj(y))/(2*ii)
def positive(x):
    ex=embed(x);assert ex.imag()==0;return AA(ex.real())>0
def coords(x):
    cs=L(x).list()+[K(0)]*(2-len(L(x).list()))
    return [QQ(v) for c in cs for v in K(c).list()]
def uncoords(v):return L(K(list(v[:8])))+k*L(K(list(v[8:])))
labels=[['p','q']*3,['p','p','p','q','q','q']]
rows=[[(120,1,0,0),(120,-1,0,0)]*3,
      [(240,1,-1,0),(120,0,0,0),(120,0,0,0),(240,-1,0,-1),(0,0,1,0),(0,0,0,1)]]
dirs=[[z**i for i in[0,5,8,13,16,21]],[L(1),z**4,z**8,z**5*psiunit,z**11*psiunit,z**23]]
angleunits=[[z**i for i in[9,7,9,7,9,7]],[z**11,z**8,z**8,z**15/psiunit,ii,psiunit]]

def run(output=None):
    source=Path(__file__).parents[1]/'certificates/branching-hexagon-two-run-pp-center-cross-eight-face.json'
    raw=json.loads(source.read_text());assert raw['status']=='positive_witness';raw=raw['witness'];faces=raw['faces'];pairs=raw['paired_edges'];classes=raw['vertex_classes']
    assert [f['species'] for f in faces]==['A']*4+['B']*4 and [f['mirror'] for f in faces]==[False,False,True,True]*2
    assert positive(p) and positive(L(QQ(1)/2)-p)
    assert psiunit*conj(psiunit)==1
    cpsi=(psiunit+conj(psiunit))/2;spsi=(psiunit-conj(psiunit))/(2*ii)
    assert positive(cpsi) and positive(spsi) and positive(spsi-cpsi) #45<psi<90
    pts=[];edges=[];face_rows=[]
    for face in faces:
        sp=0 if face['species']=='A' else 1;mir=face['mirror']
        ll=labels[sp][::-1] if mir else labels[sp];assert face['labels']==ll
        dd=[-conj(dirs[sp][(5-i)%6]) if mir else dirs[sp][i] for i in range(6)]
        aa=[angleunits[sp][(-i)%6] if mir else angleunits[sp][i] for i in range(6)]
        rr=[rows[sp][(-i)%6] if mir else rows[sp][i] for i in range(6)];assert [tuple(x) for x in face['angle_rows']]==rr
        ee=[(p if lab=='p' else L(1))*d for lab,d in zip(ll,dd)];pp=[];cur=L(0)
        for e in ee:pp.append(cur);cur+=e
        assert cur==0
        for i,e in enumerate(ee):
            assert -conj(dd[i]/dd[i-1])==aa[i]
            assert all(positive(cross(e,pp[j]-pp[i])) for j in range(6) if j not in(i,(i+1)%6))
        pts.append(pp);edges.append(ee);face_rows.append(rr)
    used=defaultdict(int);adj=defaultdict(list);graph=defaultdict(list)
    for (u,i),(v,j) in pairs:
        used[u,i]+=1;used[v,j]+=1
        assert edges[u][i]*conj(edges[u][i])==edges[v][j]*conj(edges[v][j])
        for a,b in[((u,i),(v,(j+1)%6)),((u,(i+1)%6),(v,j))]:adj[a].append(b);adj[b].append(a)
        graph[u].append((i,v,j));graph[v].append((j,u,i))
    assert set(used)=={(u,i) for u in range(8) for i in range(6)} and set(used.values())=={1}
    allnodes=set();linkrows=[]
    for cls in classes:
        nodes=set(map(tuple,cls));assert not allnodes.intersection(nodes);allnodes.update(nodes)
        assert all(len(adj[v])==2 for v in nodes)
        seen=set();todo=[next(iter(nodes))]
        while todo:
            x=todo.pop()
            if x not in seen:seen.add(x);todo+=adj[x]
        assert seen==nodes and len(nodes)==3
        row=tuple(sum(face_rows[u][i][j] for u,i in nodes) for j in range(4))
        assert row==(360,0,0,0);linkrows.append(row)
    assert allnodes==set(used)
    trans={0:(L(1),L(0))}
    def proposal(u,i,v,j):
        ru,tu=trans[u];rv=-ru*edges[u][i]/edges[v][j];assert rv*conj(rv)==1
        tv=ru*pts[u][i]+tu-rv*pts[v][(j+1)%6];return rv,tv
    todo=deque([0])
    while todo:
        u=todo.popleft()
        for i,v,j in graph[u]:
            if v not in trans:trans[v]=proposal(u,i,v,j);todo.append(v)
    assert len(trans)==8
    hol=[]
    for (u,i),(v,j) in pairs:
        rr,tt=proposal(u,i,v,j);assert rr==trans[v][0];hol.append(tt-trans[v][1])
    M=matrix(QQ,[coords(t) for t in hol if t]);assert M.rank()==2
    den=lcm([v.denominator() for v in M.list()]);H=matrix(ZZ,M*den).hermite_form(include_zero_rows=False);assert H.nrows()==2
    lattice=[uncoords([v/den for v in row]) for row in H.rows()]
    det=cross(*lattice);covol=det if positive(det) else -det
    areas=[sum(cross(x,pp[(i+1)%6]) for i,x in enumerate(pp))/2 for pp in pts]
    assert all(positive(a) for a in areas) and covol==sum(areas)
    enc=lambda x:[str(v) for v in coords(x)]
    # Cleared exact unit reconstruction norm yields the cross-family quadratic.
    T=PolynomialRing(QQ,names=('cd','sd','cx','sx','p'));cd,sd,cx,sx,pp=T.gens()
    norm=(-2*pp*cd-cx)**2+(2*pp*sd+sx)**2-(2-2*cx)
    quadratic=4*pp*pp+4*(cd*cx+sd*sx)*pp+2*cx-1
    assert (norm-quadratic) in T.ideal([cd*cd+sd*sd-1,cx*cx+sx*sx-1])
    out={'source_indexed_quotient':source.name,'field':'Q(zeta24)[k], kpositive, k^2=1+sin15^2; basis z^j k^b,b0or1,j0..7',
         'fixture':'delta15,chi90,ei_psi=(-2p*exp(-i15)+i)/(1+i),45<psi<90,p=(k-sin15)/2 in(0,1/2);qqnohomogeneousandnotpaired',
         'p':enc(p),'reference_vertices':[[enc(v) for v in pp] for pp in pts],
         'face_transforms':[{'rotation':enc(trans[u][0]),'translation':enc(trans[u][1])} for u in range(8)],
         'seam_holonomies':[enc(v) for v in hol],'primitive_period_lattice':[enc(v) for v in lattice],
         'tile_areas':[enc(a) for a in areas],'covolume':enc(covol),
         'all16_symbolic_link_rows':linkrows,'symbolic_row_order':['constant','delta','chi','psi'],
         'phase_quadratic':'4p^2+4cos(delta-chi)p+2coschi-1=0',
         'checks':'exactclosure;nativeangleunits;strict48supports;pbetween0and1/2;all48sidepiecesonce;16singlecircularlinks360symbolic;connectedorientabletorus;24puretranslationholonomies;primitiveintegralrank2lattice;covolume=totalmotifarea'}
    if output:Path(output).write_text(json.dumps(out,indent=2)+'\n')
    print('PASSnewppcentercross8facefixtureandfull16symboliclinks;fielddegree16;primitiveperiodlatticeandareaverified');return out
if __name__=='__main__':
    parser=argparse.ArgumentParser();parser.add_argument('--output');args=parser.parse_args();run(args.output)
