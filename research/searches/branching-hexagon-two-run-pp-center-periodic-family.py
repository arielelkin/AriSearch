"""Exact new pp-center periodic family on the existing indexed four-face carrier.
Read-only replay normally; writes require explicit --output.
"""
import argparse,json
from pathlib import Path
from collections import defaultdict,deque
from sage.all import CyclotomicField,PolynomialRing,QQbar,AA,QQ,ZZ,matrix,vector,lcm
K=CyclotomicField(24);zk=K.gen();ik=zk**6
C=(zk+zk**-1)/2;S=(zk-zk**-1)/(2*ik);wk=zk**2+zk**-2;rk=wk/2-S
R=PolynomialRing(K,'X');X=R.gen();L=K.extension(X**2-(1-rk*rk),'k');k=L.gen();z=L(zk);ii=L(ik);r=L(rk)
p=(L(QQ(1)/2)+L(C)+k)/2
zembed=QQbar.zeta(24)
def baseembed(x):return sum(QQ(c)*zembed**i for i,c in enumerate(K(x).list()))
kembed=baseembed(1-rk*rk).sqrt();assert AA(kembed.real())>0 and kembed.imag()==0

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
      [(240,1,0,-1),(120,0,0,0),(120,0,0,0),(240,-1,-1,0),(0,0,1,0),(0,0,0,1)]]
dirs=[[z**i for i in[0,5,8,13,16,21]],[L(1),z**4,z**8,z**12,z**17,z**4*(-k-ii*r)]]
angleunits=[[z**i for i in[9,7,9,7,9,7]],
            [z**4*(k+ii*r),z**8,z**8,z**8,z**7,z**13*(k-ii*r)]]

def run(output=None):
    source=Path(__file__).parents[1]/'certificates/branching-hexagon-new-two-run-four-face-periodic.json'
    raw=json.loads(source.read_text());faces=raw['faces'];pairs=raw['paired_edges'];classes=raw['vertex_classes']
    assert [f['species'] for f in faces]==['A','A','B','B'] and all(not f['mirror'] for f in faces)
    assert positive(p-1) and positive(r) and positive(1-r) and positive(k)
    # The q5 unit is exact, and the prescribed chi105,psi195-arcsin(r) are strict.
    assert k*k+r*r==1
    # delta15; chi105; arcsin(r)>delta15 and<90 imply105<psi<180, hencepsi>75.
    assert positive(r-L(S));assert positive(r-L(QQ(1)/2)) and positive((z**3+z**-3)/2-r)
    pts=[];edges=[]
    for face in faces:
        s=0 if face['species']=='A' else 1;assert face['labels']==labels[s]
        ee=[(p if lab=='p' else L(1))*d for lab,d in zip(labels[s],dirs[s])];pp=[];cur=L(0)
        for e in ee:pp.append(cur);cur+=e
        assert cur==0
        for i,e in enumerate(ee):
            assert -conj(dirs[s][i]/dirs[s][i-1])==angleunits[s][i]
            assert all(positive(cross(e,pp[j]-pp[i])) for j in range(6) if j not in(i,(i+1)%6))
        pts.append(pp);edges.append(ee)
    used=defaultdict(int);adj=defaultdict(list);graph=defaultdict(list)
    for (u,i),(v,j) in pairs:
        used[u,i]+=1;used[v,j]+=1
        assert edges[u][i]*conj(edges[u][i])==edges[v][j]*conj(edges[v][j])
        for a,b in[((u,i),(v,(j+1)%6)),((u,(i+1)%6),(v,j))]:adj[a].append(b);adj[b].append(a)
        graph[u].append((i,v,j));graph[v].append((j,u,i))
    assert set(used)=={(u,i) for u in range(4) for i in range(6)} and set(used.values())=={1}
    allnodes=set();linkrows=[]
    for cls in classes:
        nodes=set(map(tuple,cls));assert not allnodes.intersection(nodes);allnodes.update(nodes)
        assert all(len(adj[v])==2 for v in nodes)
        seen=set();todo=[next(iter(nodes))]
        while todo:
            x=todo.pop()
            if x not in seen:seen.add(x);todo+=adj[x]
        assert seen==nodes and len(nodes)==3
        row=tuple(sum(rows[0 if faces[u]['species']=='A' else 1][i][j] for u,i in nodes) for j in range(4))
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
    assert len(trans)==4
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
    # Exact symbolic unit reconstruction and p quadratic on arbitrary real parameters.
    T=PolynomialRing(QQ,names=('cd','sd','cx','sx','p'));cd,sd,cx,sx,pp=T.gens()
    # |1-e^ichi-2p e^-idelta|^2-1, reducing cd²+sd²=cx²+sx²=1.
    norm=(1-cx-2*pp*cd)**2+(-sx+2*pp*sd)**2-1
    reduced=norm.reduce(T.ideal([cd*cd+sd*sd-1,cx*cx+sx*sx-1]))
    quadratic=4*pp*pp-4*(cd-cd*cx+sd*sx)*pp+1-2*cx
    assert (norm-quadratic) in T.ideal([cd*cd+sd*sd-1,cx*cx+sx*sx-1])
    out={'source_indexed_quotient':source.name,'field':'Q(zeta24)[k], kpositive, k^2=1-(sqrt3/2-sin15)^2; basis z^j k^b,b0or1,j0..7',
         'fixture':'delta15,chi105,psi195-arcsin(sqrt3/2-sin15),150<psi<165,p=(1/2+cos15+k)/2>1;qqnohomogeneousandnotpaired',
         'p':enc(p),'reference_vertices':[[enc(v) for v in pp] for pp in pts],
         'face_transforms':[{'rotation':enc(trans[u][0]),'translation':enc(trans[u][1])} for u in range(4)],
         'seam_holonomies':[enc(v) for v in hol],'primitive_period_lattice':[enc(v) for v in lattice],
         'tile_areas':[enc(a) for a in areas],'covolume':enc(covol),
         'all8_symbolic_link_rows':linkrows,'symbolic_row_order':['constant','delta','chi','psi'],
         'phase_quadratic':'4p^2-4Kp+1-2coschi=0;K=cosdelta-cos(delta+chi)',
         'checks':'exactclosure;nativeangleunits;strict48supports;p>1;all24sidepiecesonce;8singlecircularlinks360symbolic;connectedorientabletorus;12puretranslationholonomies;primitiveintegralrank2lattice;covolume=totalmotifarea'}
    if output:Path(output).write_text(json.dumps(out,indent=2)+'\n')
    print('PASSnewppcenter4facefixtureandfull8symboliclinks;fielddegree16;primitiveperiodlatticeandareaverified');return out
if __name__=='__main__':
    parser=argparse.ArgumentParser();parser.add_argument('--output');args=parser.parse_args();run(args.output)
