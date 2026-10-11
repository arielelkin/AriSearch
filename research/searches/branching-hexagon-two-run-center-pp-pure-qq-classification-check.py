"""Read-only exact synthesis checker; no producer imports or solver calls.
All 130 subsets/31 flats, full oriented native inventory, retained duals and
necessary primals are reconstructed. SAT is never interpreted as existence.
Run: conda run --no-capture-output -n arisearch python <this file>
"""
from collections import Counter
from fractions import Fraction as F
from itertools import combinations, combinations_with_replacement, product
from functools import reduce
from math import gcd
from pathlib import Path
import json
from sage.all import QQ, matrix, vector, SR, I, pi, sqrt, cos, sin

ROOT = Path(__file__).resolve().parents[2]
CERT = ROOT / 'research/certificates/branching-hexagon-two-run-center-pp-pure-qq-strata-slot-balance.json'
doc = json.loads(CERT.read_text())
rows = {'H': (120,1,0,0), 'L': (120,-1,0,0),
        'u': (300,0,-1,-1), 'alpha': (120,0,0,0),
        'beta': (120,0,0,0), 'v': (60,0,0,1),
        'chi': (120,0,0,0), 'psi': (0,0,1,0)}
names = ['H','L']*3 + ['u','alpha','beta','v','chi','psi']
lengths = [['p','q']*3, ['p']*3+['q']*3]

def canon(row):
    g = reduce(gcd, map(abs,row))
    z = tuple(v//g for v in row) if g else tuple(row)
    return z if next((v for v in z if v),1)>0 else tuple(-v for v in z)

def residual(ns):
    z = [sum(rows[n][j] for n in ns) for j in range(4)]
    z[0] -= 360
    return tuple(z)

raw = []
for mixed in combinations_with_replacement(['H','L','u','v'],2):
    for hom in ['alpha','beta','chi','psi']:
        raw.append(mixed+(hom,))
for arc in [('alpha','beta'),('chi','psi')]:
    raw.extend(combinations_with_replacement(arc,3))
assert len(raw)==48
classes = {}
identities = []
for ns in raw:
    r = canon(residual(ns))
    if any(r): classes.setdefault(r,[]).append(ns)
    else: identities.append(ns)
assert len(identities)==9 and len(classes)==11
inv = doc['inventory']
assert [list(z) for z in identities] == inv['permanent_identities']
assert [{'coefficients':list(r),'types':[list(t) for t in ts]}
        for r,ts in sorted(classes.items())] == inv['nonidentity11']
planes = sorted(set(classes)-{(0,1,0,0),(120,0,-1,0)})
assert list(map(list,planes))==inv['exception_planes9']
assert planes == [(60,-1,0,-1),(60,0,0,-1),(60,1,0,-1),
                  (120,-2,-1,0),(120,2,-1,0),
                  (180,-1,-1,-1),(180,0,-1,-1),(180,1,-1,-1),
                  (240,0,-1,-2)]

# An active set of affine equations on three variables has a basis of at
# most three independent rows; inconsistent constant-only systems are omitted.
flats = {}
subset_count = 0
for k in range(4):
    for subset in combinations(range(9),k):
        subset_count += 1
        m = matrix(QQ,[planes[i] for i in subset]) if subset else matrix(QQ,0,4)
        if m.rank()!=m[:,1:].rank(): continue
        m = m.row_space().basis_matrix()
        key = tuple(tuple(str(x) for x in row) for row in m.rows())
        flats.setdefault(key,[]).append(list(subset))
assert subset_count==130 and len(flats)==31
saved = doc['records']+doc['linear_infeasible_flats']
assert len(saved)==31
seen = set()
for r in saved:
    key = tuple(map(tuple,r['flat_basis']))
    assert key in flats and key not in seen
    seen.add(key)
    assert flats[key] == r['generating_subsets']
    m = matrix(QQ,[[QQ(x) for x in row] for row in key]) if key else matrix(QQ,0,4)
    active = [i for i,p in enumerate(planes) if vector(QQ,p) in m.row_space()]
    assert active == r['active_exception_planes']
    if 'strict_linear_sample' not in r:
        # Every rejected flat forces one of the two expressly excluded loci.
        assert (vector(QQ,[0,1,0,0]) in m.row_space()
                or vector(QQ,[120,0,-1,0]) in m.row_space())
    else:
        d,t,rho = map(F,r['strict_linear_sample'])
        point = vector(QQ,[1,d,t,rho])
        assert 0<d<30 and 0<t<180 and t!=120
        assert 0<rho<90 and rho+t>120
        assert all(row*point==0 for row in m.rows())
        assert all((vector(QQ,p)*point==0)==(i in active)
                   for i,p in enumerate(planes))
assert len(seen)==31

# Fully indexed states: no species ratio, mirror restriction, AA exclusion,
# forbidden homogeneous star or nonnative identification is imposed.
def state(code):
    cid,mirror = divmod(code,2)
    s,i = divmod(cid,6)
    after=(s,i); before=(s,(i-1)%6)
    if mirror:
        return cid, lengths[s][i-1], lengths[s][i], before,after,1,0
    return cid, lengths[s][i], lengths[s][i-1], after,before,0,1
states = [state(i) for i in range(24)]

def cyclic(st):
    return min(st,st[1:]+st[:1],st[2:]+st[:2])

def feature(x,y,px,py):
    if x==y and px!=py: return None,0
    if x<y or x==y: return (x,y,px^py),1-2*px
    return (y,x,px^py),1-2*py

# Verify endpoint cancellation for every possible same-length native pairing.
for x in product(range(2),range(6)):
    for y in product(range(2),range(6)):
        if lengths[x[0]][x[1]]!=lengths[y[0]][y[1]]: continue
        for px,py in product((0,1),repeat=2):
            k,a=feature(x,y,px,py); l,b=feature(x,y,1-px,1-py)
            assert k==l and a+b==0

counts = Counter()
num_stars = num_dual_inequalities = 0
for r in doc['records']:
    key=tuple(map(tuple,r['flat_basis']))
    m=matrix(QQ,[[QQ(x) for x in row] for row in key]) if key else matrix(QQ,0,4)
    legal=set()
    # Ordered indexed states instead of producer multiset/permutation expansion.
    for st in product(range(24),repeat=3):
        if any(states[st[j]][2]!=states[st[(j+1)%3]][1] for j in range(3)): continue
        if vector(QQ,residual([names[states[i][0]] for i in st])) not in m.row_space(): continue
        legal.add(cyclic(st))
    legal=sorted(legal)
    assert list(map(list,legal))==r['oriented_stars']
    cs=[]; ss=[]; keys=set()
    for st in legal:
        c=Counter(); seam=Counter()
        for j,code in enumerate(st):
            a=states[code]; b=states[st[(j+1)%3]]
            c[a[0]]+=1
            k,v=feature(a[4],b[3],a[6],b[5])
            if k is not None: seam[k]+=v
        cs.append(c); ss.append(seam); keys.update(seam)
    keys=sorted(keys)
    assert [[list(x),list(y),p] for x,y,p in keys]==r['seam_keys']
    assert [{str(k):v for k,v in c.items()} for c in cs]==r['star_corner_counts']
    assert [[s[k] for k in keys] for s in ss]==r['star_seam_counts']
    num_stars+=len(legal); counts[r['status']]+=1
    if r['status']=='unsat':
        w=list(map(F,r['corner_dual'])); y=dict(zip(keys,map(F,r['seam_dual'])))
        assert len(w)==12
        for c,s in zip(cs,ss):
            assert sum(w[k]*v for k,v in c.items())+sum(y[k]*v for k,v in s.items())>=0
            num_dual_inequalities+=1
        assert sum(w[:6])<=-1 and sum(w[6:])<=-1
    elif r['status']=='sat':
        f=list(map(F,r['species_frequencies'])); x=list(map(F,r['star_frequencies']))
        assert len(x)==len(legal) and len(f)==2
        assert sum(f)==1 and min(f+x)>=0
        assert all(sum(x[j]*c[k] for j,c in enumerate(cs))==f[k//6] for k in range(12))
        assert all(sum(x[j]*s[k] for j,s in enumerate(ss))==0 for k in keys)
        # This is just the exact necessary union; primal does not prove tilability.
        assert set(r['active_exception_planes']) & {0,2,5,7}
    else: raise AssertionError('Uncertified or UNKNOWN record')
assert counts=={'unsat':10,'sat':14}

# Exact affine angle and full direction transfer, both reflections included.
e=vector(QQ,[1,0,0,0]); dr=vector(QQ,[0,1,0,0]); tr=vector(QQ,[0,0,1,0])
vrow=lambda n: vector(QQ,rows[n])
for idx,kind,mirror in [(0,'same',False),(2,'same',True),(5,'cross',False),(7,'cross',True)]:
    u,v,c,t = vrow('u'),vrow('v'),vrow('chi'),vrow('psi')
    if mirror: u,v,c,t=v,u,t,c
    if kind=='same':
        want=[240*e+dr-t,120*e,120*e,240*e-dr-c,c,t]
        qdirs=[60*e+dr+c,240*e+dr,420*e+dr-t]
    else:
        want=[240*e+dr-c,120*e,120*e,240*e-dr-t,c,t]
        qdirs=[60*e+dr+t,240*e+dr+t-c,420*e+dr-c]
    span=matrix(QQ,[planes[idx]]).row_space()
    actual=[u,120*e,120*e,v,c,t]
    assert all(a-b in span for a,b in zip(actual,want))
    native_qdirs=[300*e-v,480*e-v-c,660*e-v-c-t]
    assert all(a-b in span for a,b in zip(native_qdirs,qdirs))

# Exact trig identities used by the phase/domain argument; no numeric sample.
z=SR.var('z'); ph=(240*pi/180)-z
px=1+cos(pi/3)+cos(ph); py=sin(pi/3)+sin(ph)
assert (px**2+py**2 -4+2*sqrt(3)*cos(z-pi/6)).simplify_trig()==0
im_rot=sin(z-2*pi/3)*px+cos(z-2*pi/3)*py
assert (im_rot-sqrt(3)*(QQ(1)/2-cos(z))).simplify_trig()==0
print('PASS complete 48-type inventory; 130 subsets/31 flats/24 strata; '
      f'{num_stars} indexed oriented stars; {num_dual_inequalities} strong-dual inequalities; '
      '10 exact exclusions/14 necessary-only primals; every seam endpoint cancellation; '
      'all four full native angle/direction transfers; exact phase identities.')
