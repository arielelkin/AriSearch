"""Independent81-case raw geometry, cyclic-slot inventory and rational proof audit.
No producer, solver, retained primal discovery or development imports.
"""
from pathlib import Path
from itertools import product,combinations_with_replacement
from collections import Counter
from fractions import Fraction
import json
from sage.all import QQbar,AA
ROOT=Path(__file__).resolve().parents[2]
data=json.loads((ROOT/'research/certificates/branching-hexagon-new-two-run-catalog-slot-balance.json').read_text())
records={tuple(r['quad']):r for r in data['records']}
assert len(records)==81 and set(records)==set(product((90,120,150),repeat=4))
z=QQbar.zeta(24); assert z.real()>0 and z.imag()>0 and z**6==QQbar.gen()
def turn(deg):return z**(deg//15)
def seam_key(a,b,pa,pb):
    if a==b and pa!=pb:return None,0
    if a>b:a,b,pa,pb=b,a,pb,pa
    return (a,b,pa^pb),(1 if pa==0 else -1)
counts=Counter()
for quad in sorted(records):
    row=records[quad];b1,b2,b4,b5=quad
    p_arc=[turn(d)for d in(0,180-b1,360-b1-b2)]
    q_arc=[turn(d)for d in(0,180-b4,360-b4-b5)]
    sp=sum(p_arc);sq=sum(q_arc)
    p_norm=(sp*sp.conjugate()).real();q_norm=(sq*sq.conjugate()).real()
    assert p_norm>0 and q_norm>0
    if p_norm==q_norm:
        assert row['status']=='equal-lengths';counts['equal-lengths']+=1;continue
    p=QQbar(AA(q_norm/p_norm).sqrt())
    q_rotation=-p*sp/sq;assert q_rotation*q_rotation.conjugate()==1
    A=[(p if i%2==0 else 1)*turn(d)for i,d in enumerate((0,75,120,195,240,315))]
    B=[p*v for v in p_arc]+[q_rotation*v for v in q_arc]
    labels=[['p','q']*3,['p']*3+['q']*3]
    angle_units=[]
    for species,edges in enumerate((A,B)):
        assert sum(edges)==0
        pts=[];at=QQbar(0)
        for edge in edges:pts.append(at);at+=edge
        for i,edge in enumerate(edges):
            assert all((edge.conjugate()*(v-pts[i])).imag()>0
                       for j,v in enumerate(pts)if j not in(i,(i+1)%6))
            angle_units.append(-(edges[i]/(p if labels[species][i]=='p'else 1)).conjugate()
                               *(edges[i-1]/(p if labels[species][i-1]=='p'else 1)))
    legal={tri for tri in combinations_with_replacement(range(12),3)
           if angle_units[tri[0]]*angle_units[tri[1]]*angle_units[tri[2]]==1}
    # Direct ray-compatible cyclic DFS, avoiding producer's permutation/
    # mirror expansion of angle multisets. Nativecorner parity and side
    # indices remain separate even when angle and length values coincide.
    typed=[]
    for c in range(12):
        s,i=divmod(c,6);prev=(i-1)%6
        typed.append((c,(s,prev),(s,i),1,0,labels[s][prev],labels[s][i]))
        typed.append((c,(s,i),(s,prev),0,1,labels[s][i],labels[s][prev]))
    stars=set()
    for a in range(24):
        for b in range(a,24):
            if typed[a][5]!=typed[b][6]:continue
            for c in range(a,24):
                if typed[b][5]!=typed[c][6]or typed[c][5]!=typed[a][6]:continue
                if tuple(sorted((a//2,b//2,c//2)))in legal:
                    orbit=(a,b,c);stars.add(min(orbit[i:]+orbit[:i]for i in range(3)))
    assert stars=={tuple(s)for s in row['oriented_stars']}
    vectors={};allkeys=set()
    for star in stars:
        corners=Counter(i//2 for i in star);flux=Counter()
        for j,a in enumerate(star):
            b=star[(j+1)%3]
            key,sign=seam_key(typed[a][1],typed[b][2],typed[a][3],typed[b][4])
            if key is not None:flux[key]+=sign
        vectors[star]=(corners,flux);allkeys.update(flux)
    certkeys=[(tuple(x),tuple(y),parity)for x,y,parity in row['seam_keys']]
    assert len(certkeys)==len(set(certkeys))and set(certkeys)==allkeys
    for i,star in enumerate(row['oriented_stars']):
        corners,flux=vectors[tuple(star)]
        assert dict(corners)=={int(c):v for c,v in row['star_corner_counts'][i].items()}
        assert [flux[k]for k in certkeys]==row['star_seam_counts'][i]
    if row['status']=='unsat':
        w=list(map(Fraction,row['corner_dual']));y=dict(zip(certkeys,map(Fraction,row['seam_dual'])))
        assert len(w)==12 and len(y)==len(certkeys)
        assert all(sum(w[c]*v for c,v in corner.items())+sum(y[k]*v for k,v in flux.items())>=0
                   for corner,flux in vectors.values())
        assert sum(w[:6])<=-1 and sum(w[6:])<=-1
        counts['verified dual']+=1
    elif row['status']=='sat':
        assert row['mixed_status']=='sat'
        f=list(map(Fraction,row['species_frequencies']));freq=list(map(Fraction,row['star_frequencies']))
        assert len(freq)==len(stars)and all(v>=0 for v in freq)
        assert all(v>0 for v in f)and sum(f)==1
        ordered=[vectors[tuple(s)]for s in row['oriented_stars']]
        assert all(sum(v*feature[0][c]for v,feature in zip(freq,ordered))==f[c//6]for c in range(12))
        assert all(sum(v*feature[1][k]for v,feature in zip(freq,ordered))==0 for k in certkeys)
        counts['verified primal']+=1
    else:raise AssertionError(row['status'])
    print('PASS',quad,row['status'],len(stars),'stars',len(certkeys),'seam keys',flush=True)
assert counts=={'equal-lengths':15,'verified dual':54,'verified primal':12}
print('PASS independent complete81 nativegeometry/raycycles/seamvectors;15equal-length exclusions,54 rational separatingduals,12 necessarymixedprimals. Positiveperiodicconstruction for12SAT is a separate obligation.')
