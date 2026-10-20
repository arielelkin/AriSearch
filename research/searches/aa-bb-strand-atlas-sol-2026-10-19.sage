# Fixed immediate seam atlas only. No quotient or corona enumeration.
import json
from pathlib import Path
from itertools import product
K=CyclotomicField(180); z=K.gen(); I=z**45
conj=lambda x: K(x).conjugate()
real=lambda x:(x+conj(x))/2
imag=lambda x:(x-conj(x))/(2*I)
cross=lambda a,b: real(a)*imag(b)-imag(a)*real(b)
from functools import lru_cache
@lru_cache(maxsize=None)
def sign(x):
    if x==0: return 0
    prec=80
    while True:
        C=ComplexIntervalField(prec); zz=C(0,2*RealIntervalField(prec).pi()/180).exp()
        v=x.polynomial()(zz).real()
        if v.lower()>0:return 1
        if v.upper()<0:return -1
        prec*=2
def enc(x): return str(K(x))
def point(p): return [enc(real(p)),enc(imag(p))]
def same(p,q): return set(p)==set(q)
def overlap(p,q):
    # Strict interior intersection for convex polygons, including coincident ones.
    for poly in (p,q):
        for a,b in zip(poly,poly[1:]+poly[:1]):
            vals=[cross(b-a,v-a) for v in poly]
            orient=next(sign(v) for v in vals if v)
            if all(orient*sign(cross(b-a,v-a))<=0 for v in (q if poly is p else p)):
                return False
    return True
P=[K(0)]
for i in range(5): P.append(P[-1]+z**(36*i))
assert P[-1]==0
P=P[:-1]
def attach(poly,e):
    a,b=poly[e],poly[(e+1)%len(poly)]
    assert (b-a)*conj(b-a)==1
    return [b+(a-b)*v for v in P]
def apply(poly,c,t,r): return [c*(conj(v) if r else v)+t for v in poly]
def matrix_record(c,t,r):
    a,b=real(c),imag(c)
    return {'reflection':r,'linear':[[enc(a),enc(b if r else -b)],[enc(b),enc(-a if r else a)]], 'translation':point(t),'complex_c':enc(c),'complex_t':enc(t)}
results=[]
for word in ['AABBAB','AABBBA','ABAABB','BAAABB']:
    ang=[144]+[124 if x=='A' else 128 for x in word]
    dirs=[K(1)];
    for a in ang[1:]: dirs.append(dirs[-1]*z**((180-a)//2))
    types={e:''.join('A' if ang[j]==124 else 'B' for j in [e,(e+1)%7]) for e in [1,3,5]}
    aa=next(e for e in types if types[e]=='AA'); bb=next(e for e in types if types[e]=='BB')
    M=matrix(K,[[real(dirs[e]) for e in [1,3,5]],[imag(dirs[e]) for e in [1,3,5]],[int(e==aa)-int(e==bb) for e in [1,3,5]]])
    rhs=vector(K,[-sum(real(dirs[e]) for e in [0,2,4,6]),-sum(imag(dirs[e]) for e in [0,2,4,6]),0])
    sol=M.solve_right(rhs); lengths=[K(1)]*7
    for e,l in zip([1,3,5],sol): lengths[e]=l; assert sign(l)>0
    Q=[K(0)]
    for d,l in zip(dirs,lengths): Q.append(Q[-1]+d*l)
    assert Q[-1]==0; Q=Q[:-1]
    baseP={e:attach(Q,e) for e in [0,2,4,6]}
    root_bad=[(e,f) for e in baseP for f in baseP if e<f and overlap(baseP[e],baseP[f])]
    common144=set(baseP[0]) & set(baseP[6])
    assert len(common144)==2
    a144,b144=list(common144)
    assert (b144-a144)*conj(b144-a144)==1
    root_check={'P_overlap_edge_pairs':root_bad,'Q144_PP_common_vertices':[point(v) for v in sorted(common144,key=str)]}
    print(word,'root P check',root_bad,flush=True)
    seams=[]
    for e,f,r in product([1,3,5],[1,3,5],[False,True]):
        # Opposite polygon interiors require reversed endpoints iff orientation preserved.
        j,k=(f,(f+1)%7) if r else ((f+1)%7,f)
        if ang[e]+ang[j]!=252 or ang[(e+1)%7]+ang[k]!=252:continue
        if lengths[e]!=lengths[f]:continue
        u,v=(conj(Q[j]),conj(Q[k])) if r else (Q[j],Q[k])
        c=(Q[(e+1)%7]-Q[e])/(v-u); t=Q[e]-c*u
        assert c*conj(c)==1
        other=apply(Q,c,t,r)
        assert not overlap(Q,other)
        endpoint=[]; ok=True
        for a,b in [(e,j),((e+1)%7,k)]:
            pe=next(h for h in [0,2,4,6] if a in [h,(h+1)%7])
            pf=next(h for h in [0,2,4,6] if b in [h,(h+1)%7])
            qP=apply(baseP[pf],c,t,r)
            equal=same(baseP[pe],qP); assert equal
            endpoint.append({'root_vertex':a,'other_vertex':b,'root_P_edge':pe,'other_P_edge':pf,'P_vertices':[point(x) for x in qP],'coincident':equal})
        # Fixed seam neighborhood includes all forced pentagons adjacent to either Q.
        tiles=[Q,other]+list(baseP.values())+[apply(p,c,t,r) for p in baseP.values()]
        unique=[]
        for p in tiles:
            if not any(same(p,q) for q in unique):unique.append(p)
        bad=[(a,b) for a in range(len(unique)) for b in range(a+1,len(unique)) if overlap(unique[a],unique[b])]
        entry={'id':len(seams),'root_edge':e,'other_edge':f,'types':[types[e],types[f]],'isometry':matrix_record(c,t,r),'endpoints':endpoint,'full_forced_P_neighborhood_overlap_pairs':bad,'compatible':not bad}
        seams.append(entry)
    local=[]
    # At one Q, select its incoming AA seam and outgoing BB seam, and test their complete forced P neighborhoods together.
    for s,u in product([s for s in seams if s['root_edge']==aa],[s for s in seams if s['root_edge']==bb]):
        tiles=[Q]+list(baseP.values())
        for entry in [s,u]:
            iso=entry['isometry']; c=K(iso['complex_c']); t=K(iso['complex_t']); r=iso['reflection']
            tiles += [apply(Q,c,t,r)]+[apply(p,c,t,r) for p in baseP.values()]
        unique=[]
        for p in tiles:
            if not any(same(p,q) for q in unique):unique.append(p)
        bad=[(a,b) for a in range(len(unique)) for b in range(a+1,len(unique)) if overlap(unique[a],unique[b])]
        local.append({'AA_seam':s['id'],'BB_seam':u['id'],'compatible':not bad,'overlap_pairs':bad})
    holonomy=[]
    for entry in seams:
        if entry['root_edge']!=bb:continue
        iso=entry['isometry']; c=K(iso['complex_c']); t=K(iso['complex_t'])
        if iso['reflection']:
            drift=t+c*conj(t)
            holonomy.append({'seam':entry['id'],'square_linear_identity':c*conj(c)==1,'square_translation':point(drift),'square_translation_nonzero':drift!=0,'scope':'formal isometry composition, no embedded infinite ribbon assertion'})
        else:
            n=next(n for n in range(1,181) if c**n==1)
            drift=sum(c**j*t for j in range(n))
            holonomy.append({'seam':entry['id'],'rotation_order':n,'power_translation':point(drift),'scope':'formal isometry composition only'})
    results.append({'holonomy':holonomy,'word' :word,'root_P_check':root_check,'Q_vertices':[point(x) for x in Q],'QQ_lengths':{str(e):enc(lengths[e]) for e in [1,3,5]},'types':{str(k):v for k,v in types.items()},'seams':seams,'strand_at_Q':local})
    print(word,[(s['id'],s['types'],s['isometry']['reflection'],s['compatible']) for s in seams],local,flush=True)
Path('research/searches/aa-bb-strand-atlas-sol-2026-10-19.json').write_text(json.dumps({'field':'Q(z), z=exp(2*pi*i/180), minimal polynomial Phi_180','scope':'fixed native seams and two strand seams at one Q; all forced adjacent P placements','results':results},indent=2,default=int)+'\n')
