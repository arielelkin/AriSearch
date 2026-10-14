"""Exact radius-one ring for one equal-private distance-three mask pair."""
from sage.all import NumberField,PolynomialRing,QQ,AA,matrix,vector
from itertools import product
import json,argparse,sys
from pathlib import Path
from sage.env import SAGE_VERSION
R=PolynomialRing(QQ,'z');z=R.gen();K=NumberField(8*z**4-8*z**2+1,'c',embedding=((2+AA(2).sqrt())/4).sqrt())
c=K.gen();r=4*c*c-2;t=r/(4*c);x=K(1);y=K(2);v=K(5)/2;u=v+r*c;w=(u+v)/r-t*(x+y)
H1=v+w-u+r*(w-u);H2=H1
assert all(AA(h)>0 and h not in(x,y,u,v,w) for h in(H1,H2))
assert x not in(H1,u,u,H2,v,w,w,v) and y not in(H1,u,u,H2,v,w,w,v)
def add(a,b):return(a[0]+b[0],a[1]+b[1])
def sub(a,b):return(a[0]-b[0],a[1]-b[1])
def mul(s,a):return(s*a[0],s*a[1])
def dot(a,b):return a[0]*b[0]+a[1]*b[1]
def cross(a,b):return a[0]*b[1]-a[1]*b[0]
def edges(p):return list(zip(p,p[1:]+p[:1]))
def disjoint(p,q):
    for a,b in edges(p)+edges(q):
        e=sub(b,a);n=(-e[1],e[0]);pp=[dot(z,n) for z in p];qq=[dot(z,n) for z in q]
        if AA(max(pp,key=AA))<=AA(min(qq,key=AA)) or AA(max(qq,key=AA))<=AA(min(pp,key=AA)):return True
    return False
A=(K(0),-w);B=(x*c,-w-x*t);C=add(B,(u/r,u/r));D=add(C,(-v/r,v/r));P=(A,B,C,D,(K(0),K(0)))
lengths=(H1,u,u,H2,v,w,w,v)
dirs=((1,0),(1/r,1/r),(0,1),(-1/r,1/r),(-1,0),(-1/r,-1/r),(0,-1),(1/r,-1/r))
Q=[(K(0),K(0))]
for L,d in zip(lengths[:-1],dirs[:-1]):Q.append(add(Q[-1],mul(L,d)))
Q=tuple(Q);assert add(Q[-1],mul(lengths[-1],dirs[-1]))==Q[0]

def attachments(poly,ei,a,b):
    p,q=edges(poly)[ei]; f=sub(q,p);e=sub(b,a);assert dot(f,f)==dot(e,e);J=(-e[1],e[0]);out=[]
    for swap in (False,True):
        aa,bb=(b,a) if swap else(a,b);e=sub(bb,aa);J=(-e[1],e[0])
        for sign in(-1,1):
            image=tuple(add(aa,add(mul(dot(sub(z,p),f)/dot(f,f),e),mul(sign*cross(f,sub(z,p))/dot(f,f),J))) for z in poly)
            if disjoint(Q,image) and image not in out:out.append(image)
    assert len(out)==2
    return out
options=[]
for i,(a,b) in enumerate(edges(Q)):
    if i in(0,3):
        raw=attachments(Q,0,a,b)+attachments(Q,3,a,b)
        unique={}
        for cand in raw:unique[frozenset(cand)]=cand
        candidates=list(unique.values())
    else:
        ei={u:1,v:2,w:4}[lengths[i]]
        candidates=attachments(P,ei,a,b)
        # u/v edges have one acute endpoint, which must be adjacent to a QQ-private slot.
        if lengths[i] in(u,v):
            target=a if(i-1)%8 in(0,3) else b
            assert ((i-1)%8 in(0,3)) != ((i+1)%8 in(0,3))
            candidates=[p for p in candidates if p[2]==target]
    assert candidates
    options.append(candidates)
def ete(p,q):
    for a in p:
        for b,d in edges(q):
            if cross(sub(a,b),sub(d,b))==0 and AA(dot(sub(a,b),sub(a,d)))<0:return False
    for a in q:
        for b,d in edges(p):
            if cross(sub(a,b),sub(d,b))==0 and AA(dot(sub(a,b),sub(a,d)))<0:return False
    return True
assert all(L not in(2*u,2*v) for L in(x,w,y))
valid=[];failures=[]
for choices in product(*(range(len(opts)) for opts in options)):
    ring=[options[i][k] for i,k in enumerate(choices)]
    clashes=[(i,j,'overlap' if not disjoint(ring[i],ring[j]) else 'forbidden_partial_contact') for i in range(8) for j in range(i) if not disjoint(ring[i],ring[j]) or not ete(ring[i],ring[j])]
    if clashes:failures.append({'choices':choices,'first_clash':clashes[0]})
    else:valid.append(choices)
assert len(valid)==1
choice=valid[0];basis=matrix(K,2,2,lambda i,j:Q[j+1][i]-Q[0][i]);maps=[]
for i in(0,3):
    image=options[i][choice[i]]
    linear=matrix(K,2,2,lambda a,b:image[b+1][a]-image[0][a])*basis.inverse()
    offset=vector(K,image[0])-linear*vector(K,Q[0]);maps.append((linear,offset))
M,b=maps[0];N,a=maps[1]
assert M*M==matrix.identity(K,2) and M.det()==-1 and N==-matrix.identity(K,2)
period=M*b+b;assert period!=vector(K,[0,0])
assert frozenset(tuple(M*N*vector(K,p)+M*a+b) for p in Q)==frozenset(Q)
result={'domain':'one exact asymmetric P and equal-private distance3 equiangular Q, all full-side first neighbors, all isometries','field':'8c^4-8c²+1,9/10<c<1','Q_lengths':[str(L) for L in lengths],'option_counts':[len(o) for o in options],'rings_tested':len(valid)+len(failures),'valid_rings':valid,'failure_witnesses':failures,'QQ_maps':[{'linear':[str(z) for z in M.list()],'offset':[str(z) for z in b]} for M,b in maps],'glide_squared_period':[str(z) for z in period],'glide_times_other_neighbor_fixes_Q':True}
result['software']={'python':sys.version.split()[0],'sage':SAGE_VERSION}
result=json.loads(json.dumps(result))  # canonical JSON lists instead of native tuple rows
parser=argparse.ArgumentParser()
mode=parser.add_mutually_exclusive_group()
mode.add_argument('--output',type=Path,help='Create new exact certificate; refuses overwrite.')
mode.add_argument('--check',type=Path,help='Nondestructively compare retained exact certificate.')
args=parser.parse_args()
if args.output:
    with args.output.open('x') as handle:handle.write(json.dumps(result,indent=2)+'\n')
if args.check:
    assert json.loads(args.check.read_text())==result
    print(json.dumps({'status':'PASS','certificate':str(args.check),'rings_tested':result['rings_tested'],'valid_ring_count':len(result['valid_rings'])}))
else:print(json.dumps(result))
