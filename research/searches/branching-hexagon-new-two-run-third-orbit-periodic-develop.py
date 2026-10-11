"""Exact zeta24 geometry and flat-torus lattice of four-face 1/sqrt2 third-orbit two-run witness.
Read-only by default; explicit --output required for retained development.
"""
import argparse,json
from pathlib import Path
from collections import defaultdict,deque
from sage.all import CyclotomicField,QQbar,AA,matrix,vector,ZZ,lcm
K=CyclotomicField(24);z=K.gen();ii=z**6;p=(z**3+z**-3)/2
assert AA(QQbar(z).real())>AA(96)/100 and AA(QQbar(z).imag())>AA(25)/100
labels=[['p','q']*3,['p','p','p','q','q','q']]
angles=[[135,105]*3,[75,150,150,105,90,150]]
directions=[[0,75,120,195,240,315],[0,30,60,135,225,255]]
def cross(x,y):return (x.conjugate()*y-x*y.conjugate())/(2*ii)
def positive(x):return AA(QQbar(x).real())>0

def develop(output=None):
    source=Path(__file__).parents[1]/'certificates/branching-hexagon-new-two-run-third-orbit-eight-face-periodic.json'
    r=json.loads(source.read_text());fs=r['faces'];pairs=r['paired_edges'];pts=[];edges=[]
    for f in fs:
        s=0 if f['species']=='A' else 1
        expected_labels=labels[s][::-1] if f['mirror'] else labels[s]
        expected_angles=[angles[s][0]]+angles[s][:0:-1] if f['mirror'] else angles[s]
        assert f['labels']==expected_labels
        if 'angles' not in f:f['angles']=expected_angles
        assert f['angles']==expected_angles
        ee=[(p if label=='p' else K(1))*z**(d//15) for label,d in zip(labels[s],directions[s])]
        pp=[];cur=K(0)
        for e in ee:pp.append(cur);cur+=e
        assert cur==0
        for i,e in enumerate(ee):assert -(z**((directions[s][i]-directions[s][i-1])//15)).conjugate()==z**(angles[s][i]//15)
        if f['mirror']:pp=[pp[(-i)%6].conjugate() for i in range(6)]
        ee=[pp[(i+1)%6]-pp[i] for i in range(6)]
        for i,e in enumerate(ee):
            norm=p if f['labels'][i]=='p' else K(1);prevnorm=p if f['labels'][i-1]=='p' else K(1)
            assert -((e/norm)/(ee[i-1]/prevnorm)).conjugate()==z**(f['angles'][i]//15)
            assert all(positive(cross(e,pp[j]-pp[i])) for j in range(6) if j not in(i,(i+1)%6))
        pts.append(pp);edges.append(ee)
    used=defaultdict(int);adj=defaultdict(list);graph=defaultdict(list)
    for (u,i),(v,j) in pairs:
        used[u,i]+=1;used[v,j]+=1
        assert edges[u][i]*edges[u][i].conjugate()==edges[v][j]*edges[v][j].conjugate()
        for a,b in [((u,i),(v,(j+1)%6)),((u,(i+1)%6),(v,j))]:adj[a].append(b);adj[b].append(a)
        graph[u].append((i,v,j));graph[v].append((j,u,i))
    assert set(used)=={(u,i) for u in range(len(fs)) for i in range(6)} and set(used.values())=={1}
    allnodes=set()
    for cls in r['vertex_classes']:
        nodes=set(map(tuple,cls));assert not allnodes.intersection(nodes);allnodes.update(nodes)
        assert all(len(adj[x])==2 for x in nodes)
        seen=set();todo=[next(iter(nodes))]
        while todo:
            x=todo.pop()
            if x not in seen:seen.add(x);todo+=adj[x]
        assert seen==nodes and len(nodes)==3 and sum(fs[u]['angles'][i] for u,i in nodes)==360
    assert allnodes==set(used)
    trans={0:(K(1),K(0))}
    def proposal(u,i,v,j):
        ru,tu=trans[u];rv=-ru*edges[u][i]/edges[v][j]
        assert rv*rv.conjugate()==1
        tv=ru*pts[u][i]+tu-rv*pts[v][(j+1)%6]
        return rv,tv
    todo=deque([0])
    while todo:
        u=todo.popleft()
        for i,v,j in graph[u]:
            if v not in trans:trans[v]=proposal(u,i,v,j);todo.append(v)
    assert len(trans)==len(fs)
    hol=[]
    for (u,i),(v,j) in pairs:
        rv,tv=proposal(u,i,v,j);assert rv==trans[v][0];hol.append(tv-trans[v][1])
    coeff=matrix([list(t) for t in hol if t]);assert coeff.rank()==2
    den=lcm([x.denominator() for x in coeff.list()]);hnf=matrix(ZZ,coeff*den).hermite_form(include_zero_rows=False)
    assert hnf.nrows()==2
    lattice=[K([x/den for x in row]) for row in hnf.rows()]
    area=cross(lattice[0],lattice[1]);covol=area if positive(area) else -area
    areas=[sum(cross(v,pp[(i+1)%6]) for i,v in enumerate(pp))/2 for pp in pts]
    assert all(positive(a) for a in areas) and covol==sum(areas)
    enc=lambda x:[str(c) for c in K(x).list()]
    out={'source_quotient':source.name,'field':'Q(zeta24), z=exp(i*pi/12)','p':enc(p),
         'reference_vertices':[[enc(x) for x in pp] for pp in pts],
         'face_transforms':[{'rotation':enc(trans[u][0]),'translation':enc(trans[u][1])} for u in range(len(fs))],
         'seam_holonomies':[enc(t) for t in hol],'period_lattice':[enc(t) for t in lattice],
         'tile_areas':[enc(a) for a in areas],'covolume':enc(covol),
         'checks':'strictconvexity, exactnativeangles,48uniquesidepieces,16singlecircular360links,connected8faces,allholonomiestranslational,fullintegralrank2lattice,covolume=totalarea'}
    if output:Path(output).write_text(json.dumps(out,indent=2)+'\n')
    print('PASS exactthirdorbit8faceperiodicdevelopment; periods',lattice,'covolume',covol,'areas',areas)
    return out
if __name__=='__main__':
    parser=argparse.ArgumentParser();parser.add_argument('--output');args=parser.parse_args();develop(args.output)
