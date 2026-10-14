"""Independent necessary-invariant checker for directed-offset 3+1 branches.

No construction-code imports. Exact necessary-invariant ideals and real-domain contradictions exclude the four stated residual branches; this is not a source-partition feasibility checker.
"""
import sympy as S
import argparse

p, t, a, b, x, y = S.symbols("p t a b x y", real=True)
R = S.groebner([p*p-p-1, 4*t*t-3+p], t,p,a,b,x,y,
               order="lex", domain=S.QQ)

def red(z):
    num, den = S.fraction(S.cancel(S.expand(z)))
    return S.factor(R.reduce(S.expand(num))[1]/R.reduce(S.expand(den))[1])

def plus(u,v): return (u[0]+v[0],u[1]+v[1])
def minus(u,v): return (u[0]-v[0],u[1]-v[1])
def mul(k,u): return (k*u[0],k*u[1])
def squared(u): return u[0]**2+u[1]**2

def pentagons(thin):
    c,s=(p/2,t) if thin else ((p-1)/2,p*t)
    A,B,C,D=(0,0),(1,0),(1+c,s),(c,s)
    v,n=(c,s),(s,-c)
    P=(a,t*x)
    Q=(c+1-b,s-t*y) if thin else (c+b,s-t*y)
    Z=plus(B,plus(mul(1-a if thin else b,v),mul(t*(x if thin else y),n)))
    W=plus(mul(b if thin else a,v),mul(-t*(y if thin else x),n))
    return [(B,Z,C,Q,P),(D,W,A,P,Q)]

def area(V):
    return red(sum(V[i][0]*V[(i+1)%5][1]-V[i][1]*V[(i+1)%5][0]
                   for i in range(5))/2)

def edge_squares(V):
    return [red(squared(minus(V[(i+1)%5],V[i]))) for i in range(5)]

def moments(V):
    E=edge_squares(V)
    return red(sum(E)),red(sum(z*z for z in E))

def main():
    cli=argparse.ArgumentParser()
    cli.add_argument("--ideals",action="store_true")
    args=cli.parse_args()
    V=pentagons(True)+pentagons(False)
    A=[red(area(z)/t) for z in V]
    M=[moments(z) for z in V]
    assert red(A[0]+A[1]-1)==0
    assert red(A[2]+A[3]-p)==0
    assert red(M[0][0]-M[1][0]-2*((a-b)*(a+b-2)+t*t*(x*x-y*y)))==0
    assert red(M[2][0]-M[3][0]+2*(a*a-b*b+2*b+t*t*(x*x-y*y)-1))==0
    labels=("T0","T1","K0","K1")
    for singleton in range(4):
        triple=[j for j in range(4) if j!=singleton]
        pair=(2,3) if singleton<2 else (0,1)
        cross=next(j for j in triple if j not in pair)
        eq=[red(A[pair[0]]-A[pair[1]]),red(A[cross]-A[pair[0]])]
        eq += [red(M[pair[0]][k]-M[pair[1]][k]) for k in (0,1)]
        eq += [red(M[cross][k]-M[pair[0]][k]) for k in (0,1)]
        print("singleton",labels[singleton],"triple",*[labels[j] for j in triple],flush=True)
        if args.ideals:
            golden=(1+S.sqrt(5))/2
            eq=[S.expand(z.subs(p,golden)) for z in eq]
            G=S.groebner(eq,a,b,x,y,order="grevlex",extension=S.sqrt(5))
            if singleton in (1, 2):
                assert len(G.polys) == 1 and G.polys[0].as_expr() == 1
            else:
                r5 = S.sqrt(5)
                target = y*y-(S.Rational(3,2)+3*r5/10)*y + (S.Rational(1,2)+r5/10 if singleton == 0 else 1+2*r5/5)
                for necessary in (a-S.Rational(1,2), x-(r5-1)*(y-S.Rational(1,2)), target):
                    assert S.simplify(G.reduce(necessary)[1]) == 0
                if singleton == 0:
                    assert S.simplify(target.subs(y,S.Rational(1,2))) == -r5/20
                    assert S.simplify(target.subs(y,1)) == -r5/5
                else:
                    assert S.simplify(S.discriminant(target,y)) == -(13+7*r5)/10
            print("  ideal",[S.factor(g.as_expr(),extension=S.sqrt(5)) for g in G.polys],flush=True)
        else:
            for name,z in zip(("area pair","area cross","edge-square pair","edge-fourth pair","edge-square cross","edge-fourth cross"),eq):
                print(" ",name,":",z)

if __name__=="__main__": main()
