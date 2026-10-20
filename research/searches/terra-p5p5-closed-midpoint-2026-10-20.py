"""Exact changed P5/P5 local star fixture; uses rational geometry helpers beside this file."""
import importlib.util
from itertools import product
from pathlib import Path

source=Path(__file__).with_name('terra-p5p5-halfside-2026-10-20.py')
spec=importlib.util.spec_from_file_location('halfside',source)
m=importlib.util.module_from_spec(spec)
spec.loader.exec_module(m)

P=m.P
Q=((0,0),(5,0),(6,2),(3,8),(1,7))

def main():
    assert min(m.turns(Q))>0
    assert m.area2(Q)!=m.area2(P)
    assert any(x>0 for x in m.angle_dots(Q))
    assert not m.consecutive_supplementary(Q)
    pside2=m.norm2(m.sub(P[4],P[3]))
    assert pside2==20
    assert pside2 not in tuple(m.norm2(m.sub(v,u)) for u,v in m.edges(Q))
    mid,choices=m.half_contacts(Q)
    all_pairs=[(a,b) for a,b in product(*choices) if not m.interiors_intersect(a[3],b[3])]
    flat=[(a,b) for a,b in all_pairs if m.completed_midpoint(a[3],b[3],mid,m.sub(P[4],P[3]))]
    assert len(all_pairs)==len(flat)==1
    a,b=flat[0]
    # Independently exhibit the P/P whole-side alternative: reflect P across
    # the support of its own side and check disjoint interiors exactly.
    pp=m.mapped(P,m.edges(P)[3],m.edges(P)[3],True)
    assert not m.interiors_intersect(P,pp)
    print('P',P,'turns',m.turns(P),'angle_dots',m.angle_dots(P),'side2',tuple(m.norm2(m.sub(v,u)) for u,v in m.edges(P)))
    print('Q',Q,'turns',m.turns(Q),'angle_dots',m.angle_dots(Q),'side2',tuple(m.norm2(m.sub(v,u)) for u,v in m.edges(Q)))
    print('Q area2',m.area2(Q),'midpoint',mid,'individual half-side choices',tuple(map(len,choices)))
    print('only nonoverlapping split branch',a[:3],b[:3],'completed',len(flat))
    print('Q1',a[3]);print('Q2',b[3])
    print('P/P whole-side alternative',pp)

if __name__=='__main__': main()
