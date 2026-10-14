"""Exact symmetric-invariant elimination for the four 3+1 residual assignments.

Replay: mise exec -- conda run --no-capture-output -n arisearch python
        research/searches/ammann-directed-offset-residual-invariants-2026-10-14.py
"""
import importlib.util
from pathlib import Path
import sympy as S

source = Path(__file__).with_name('ammann-directed-offset-gate-2026-10-14.py')
spec = importlib.util.spec_from_file_location('gate', source)
gate = importlib.util.module_from_spec(spec)
spec.loader.exec_module(gate)

phi = (1 + S.sqrt(5))/2
t2 = (3-phi)/4
phi_sym,t_sym = S.symbols('phi t', real=True)
a,b,x,y = S.symbols('a b x y')
reps = [gate.outputs()[i] for i in (0,1,4,5)]

def reduce(expr):
    expr = S.expand(expr.subs({gate.aX:a,gate.aY:b,gate.hX:t_sym*x,gate.hY:t_sym*y}))
    expr = S.expand(expr.subs(t_sym**2,t2).subs(phi_sym,phi))
    result = S.simplify(expr)
    assert not ({phi_sym,t_sym} & result.free_symbols)
    return result

def polys(i):
    kind = reps[i][0]
    p = reps[i][4]
    edge = [reduce(gate.substitute_source(gate.d2(p[j],p[(j+1)%5]),kind)) for j in range(5)]
    return edge

def main():
    ed=[polys(i) for i in range(4)]
    ar=[reduce(gate.substitute_source(gate.signed_area(reps[i][4]),reps[i][0])/t_sym) for i in range(4)]
    L=[S.expand(sum(e)) for e in ed]
    Q=[S.expand(sum(e*e for e in edges)) for edges in ed]
    assert [S.simplify(ar[0]+ar[1]),S.simplify(ar[2]+ar[3])] == [1,phi]
    P=y*y-(S.Rational(3,2)+3*S.sqrt(5)/10)*y+S.Rational(1,2)+S.sqrt(5)/10
    Qpoly=y*y-(S.Rational(3,2)+3*S.sqrt(5)/10)*y+1+2*S.sqrt(5)/5
    x_relation=x+(1-S.sqrt(5))*y-S.Rational(1,2)+S.sqrt(5)/2
    for singleton in range(4):
        triple=[i for i in range(4) if i!=singleton]
        eq=[S.expand(ar[triple[0]]-ar[j]) for j in triple[1:]]
        eq += [S.expand(L[triple[0]]-L[j]) for j in triple[1:]]
        eq += [S.expand(Q[triple[0]]-Q[j]) for j in triple[1:]]
        gb=S.groebner(eq,a,b,x,y,order='grevlex',extension=S.sqrt(5))
        if singleton in (1,2):
            assert len(gb.polys)==1 and gb.polys[0].as_expr()==1
            print('singleton',reps[singleton][0],singleton%2,'unit ideal',flush=True)
        else:
            target = P if singleton==0 else Qpoly
            for f in (a-S.Rational(1,2),x_relation,target):
                assert S.simplify(gb.reduce(f)[1])==0
            print('singleton',reps[singleton][0],singleton%2,
                  'basis',len(gb.polys),'and required eliminants verified',flush=True)
    assert S.simplify(P.subs(y,S.Rational(1,2))) == -S.sqrt(5)/20
    assert S.simplify(P.subs(y,1)) == -S.sqrt(5)/5
    assert S.simplify(S.discriminant(Qpoly,y)) == -(13+7*S.sqrt(5))/10
    print('four residual assignments excluded exactly',flush=True)

if __name__=='__main__': main()
