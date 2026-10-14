"""Symbolic boundary-cancellation proof for the four-P/noQQ grouped-Q carrier.
Domain: all positive X,Y,V with u=V+r*c*(Y-X)>0 and w>0.
"""
from sage.all import QQ,AA,PolynomialRing,NumberField
from itertools import product
import json,argparse,sys
from pathlib import Path
from sage.env import SAGE_VERSION
R=PolynomialRing(QQ,'s');s=R.gen();K=NumberField(8*s**4-8*s**2+1,'c',embedding=((2+AA(2).sqrt())/4).sqrt());c=K.gen();r=4*c*c-2;t=r/(4*c)
T=PolynomialRing(K,('X','Y','V'));X,Y,v=T.gens();u=v+r*c*(Y-X);w=(u+v)/r-t*(X+Y);a=X*c+u/r;Cy=-w-X*t+u/r;z=(X-Y)*(c+t)/2
assert a==Y*c+v/r and z==-Cy-w/2 and w==2*a-(c+t)*(X+Y)
def add(a,b):return(a[0]+b[0],a[1]+b[1])
def sub(a,b):return(a[0]-b[0],a[1]-b[1])
def mul(s,a):return(s*a[0],s*a[1])
def neg(a):return(-a[0],-a[1])
def cross(a,b):return a[0]*b[1]-a[1]*b[0]
def edges(p):return list(zip(p,p[1:]+p[:1]))
def area(p):return sum(cross(q,p) for q,p in edges(p))/2
A=(-a,-w-Cy);B=(-u/r,-u/r);C=(T(0),T(0));D=(-v/r,v/r);E=(-a,-Cy);P=(A,B,C,D,E)
F=lambda p:(p[1],p[0]);G=lambda p:(-p[1],-p[0])
M=(P,tuple(F(p) for p in P[::-1]),tuple(neg(p) for p in P),tuple(G(p) for p in P[::-1]))
East=(2*a,-2*z);North=(-2*z,2*a);NW=sub(North,East)
Q=(D,G(E),add(North,B),add(North,A),sub(NW,D),sub(NW,G(E)),sub(neg(East),B),sub(neg(East),A))
word=(Y,X,X,Y,Y,X,X,Y);direction=(t,c)
for (p,q),L in zip(edges(Q),word):
    assert sub(q,p)==mul(L,direction)
    direction=((direction[0]-direction[1])/r,(direction[0]+direction[1])/r)
assert direction==(t,c)
assert all(area(p)==area(P) for p in M)
determinant=cross(East,North)
assert determinant==4*(a*a-z*z) and determinant==4*area(P)+area(Q)
# Exact symbolic native edge pairing modulo the lattice, finite domain28edges and9 shifts.
all_edges=[(i,j,p,q) for i,poly in enumerate(M+(Q,)) for j,(p,q) in enumerate(edges(poly))]
unused=set(range(len(all_edges)));pairs=[]
while unused:
    k=min(unused);unused.remove(k);i,j,p,q=all_edges[k];matches=[]
    for l in sorted(unused):
        ii,jj,pp,qq=all_edges[l]
        for m,n in product((-1,0,1),repeat=2):
            shift=add(mul(m,East),mul(n,North))
            if p==add(qq,shift) and q==add(pp,shift):matches.append((l,m,n))
    assert len(matches)==1,(i,j,matches)
    l,m,n=matches[0];unused.remove(l);ii,jj,_,_=all_edges[l]
    pairs.append({'first':[i,j],'second':[ii,jj],'second_translation':[m,n]})
assert len(pairs)==14
result={'status':'PASS','field':'8c^4-8c²+1,9/10<c<1;r=4c²-2;t=r/(4c)','symbolic_parameters':['X','Y','V'],'domain':'X,Y,V,u,w>0; u=V+r*c*(Y-X); w=(u+V)/r-t*(X+Y)','Q_word':['Y','X','X','Y','Y','X','X','Y'],'edge_count':len(all_edges),'native_edge_pairs':pairs,'covolume':str(determinant),'one_P_area':str(area(P)),'Q_area':str(area(Q)),'signed_area_equals_covolume':True}
result['coefficient_verification']={'coefficient_ring':'Q(c)[X,Y,V]','quartic_degree':4,'paired_edges':14,'coordinate_endpoint_identities':56,'all_endpoint_residual_polynomials_zero':True,'oriented_area_residual_polynomial_zero':True,'Q_vector_identities':16,'all_Q_vector_residual_polynomials_zero':True}
result['software']={'python':sys.version.split()[0],'sage':SAGE_VERSION}
result=json.loads(json.dumps(result))
parser=argparse.ArgumentParser();mode=parser.add_mutually_exclusive_group()
mode.add_argument('--output',type=Path,help='Create a new exact certificate; refuses overwrite.')
mode.add_argument('--check',type=Path,help='Nondestructively recompute all symbolic identities and compare certificate.')
args=parser.parse_args()
if args.output:
    with args.output.open('x') as handle:handle.write(json.dumps(result,indent=2)+'\n')
if args.check:
    assert json.loads(args.check.read_text())==result
    print(json.dumps({'status':'PASS','certificate':str(args.check),'paired_edges':len(pairs),'coordinate_endpoint_identities':56}))
else:print(json.dumps(result))
