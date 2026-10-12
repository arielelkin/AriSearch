#!/usr/bin/env python3
"""Controls for P2 search encoding; not independent review of enumeration.

Compares full distance polynomials against direct conjugate products in a
separate polynomial ring over Q(w); tests integer sign routines against
Sage algebraic signs; checks retained source frames and checkpoint coverage.
"""
import argparse, hashlib, importlib.util, json, random
from pathlib import Path
from sage.all import CyclotomicField, PolynomialRing, QQbar, AA

ROOT=Path(__file__).resolve().parents[2];HERE=ROOT/'research/searches'
s=importlib.util.spec_from_file_location('metric',HERE/'penrose-kite-dart-metric-collapse.py');met=importlib.util.module_from_spec(s);s.loader.exec_module(met)
K=CyclotomicField(10);w=K.gen();phi=w+w**-1;emb=K.hom([QQbar.zeta(10)])

def main():
    a=argparse.ArgumentParser();a.add_argument('--output',required=True);args=a.parse_args()
    nframes=0
    for level in (3,4):
        P=json.loads((ROOT/f'research/certificates/penrose-kite-dart-patch{level}.json').read_text())
        V=[K(v) for v in P['verts']]
        for kind,gv,orientation in P['tiles']:
            ref=[K(0),K(1),w if kind=='kite' else w/phi,w**2]
            assert all(V[i]-V[gv[0]]==w**orientation*r for i,r in zip(gv,ref))
            nframes+=1
    cp=ROOT/'research/certificates/penrose-kite-dart-recomposition-patch3.jsonl'
    rows=[json.loads(s) for s in cp.read_text().splitlines()]
    assert {(r['kite'],r['dart']) for r in rows}==set((i,j) for i in range(98) for j in range(98))
    norms_checked=0
    for row in rows:
        if row['dead'] is not None or not row['interior_faces']:continue
        R,active,D,norms=met.polynomials(row['classes'])
        S=PolynomialRing(K,R.variable_names());X=S.gens()
        for ci,c in enumerate(row['classes']):
            V=[];B=[]
            for f in c['forms']:
                z=S(0);zb=S(0)
                for key,vec in f.items():
                    coeff=K(vec)
                    if key=='c':z+=coeff;zb+=coeff.conjugate()
                    else:
                        k=active.index(int(key));q=X[2*k]+w*X[2*k+1];qb=X[2*k]+w**-1*X[2*k+1]
                        z+=coeff*q;zb+=coeff.conjugate()*qb
                V.append(z);B.append(zb)
            for i in range(len(V)):
                for j in range(i+1,len(V)):
                    direct=(V[i]-V[j])*(B[i]-B[j]);encoded=S(0)
                    for mon,c in D[ci][i][j].dict().items():
                        term=S(met.lin.f_to_k(c))
                        for x,power in zip(X,mon):term*=x**int(power)
                        encoded+=term
                    assert encoded==direct
                    norms_checked+=1
    rng=random.Random(431);checks=200
    for _ in range(checks):
        va=tuple(rng.randint(-6,6) for _ in range(4));vb=tuple(rng.randint(-6,6) for _ in range(4))
        q=K(list(va)).conjugate()*K(list(vb));area=AA(emb((q-q.conjugate())/(w-w.conjugate())))
        assert met.lin.p2.cross_sign(va,vb)==int(area>0)-int(area<0)
        real=q+q.conjugate();exact=AA(emb(real))
        assert met.lin.p2.real_sign(tuple(int(x) for x in real.vector()))==int(exact>0)-int(exact<0)
    joint=json.loads((ROOT/'research/certificates/penrose-kite-dart-joint-collapse-summary.json').read_text())
    assert joint['complete'] and joint['partitions_completed']==128 and joint['retained_loci']==0
    # Check the exact mirror certificate used to transfer the completed
    # flat-cell exclusion; the source-coordinate map is an involution.
    mirror=json.loads((ROOT/'research/certificates/penrose-kite-dart-flat-mirror-map.json').read_text())
    A=next(r for r in rows if [r['kite'],r['dart']]==mirror['source_pair'])
    B=next(r for r in rows if [r['kite'],r['dart']]==mirror['target_pair'])
    R,active,DA,_=met.polynomials(A['classes']);R2,active2,DB,_=met.polynomials(B['classes'])
    assert R==R2 and active==active2
    sub=[]
    for i in range(len(active)):sub.extend([-R.gen(2*i),met.phi*R.gen(2*i)+R.gen(2*i+1)])
    h=R.hom(sub,R);assert all(h(h(x))==x for x in R.gens())
    for ci,cj,o,shift in mirror['class_map']:
        n=len(DA[ci]);perm=[(shift+o*k)%n for k in range(n)]
        assert all(h(DA[ci][i][j])==DB[cj][perm[i]][perm[j]] for i in range(n) for j in range(n))
    for ref in ([K(0),K(1),w,w**2],[K(0),K(1),w/phi,w**2]):
        assert set(ref)=={w**2*z.conjugate() for z in ref}
    flat=json.loads((ROOT/'research/certificates/penrose-kite-dart-flat-collapse.json').read_text())
    completed=next(r for r in flat if [r['kite'],r['dart']]==mirror['target_pair'])
    assert completed['complete'] and completed['retained_loci']==0
    result={'status':'encoding controls passed','source_frames_checked':nframes,
            'flat_mirror_transfer_checked':True,'checkpoint_pairs':len(rows),'full_symbolic_norm_identities_checked':norms_checked,
            'exact_sign_controls':checks,'seed':431,
            'scope':'encoding controls only; not independent verification of exhaustive enumeration or ideal pruning',
            'checkpoint_sha256':hashlib.sha256(cp.read_bytes()).hexdigest()}
    Path(args.output).write_text(json.dumps(result,indent=1)+'\n');print(json.dumps(result))

if __name__=='__main__':main()
