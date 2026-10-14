"""Independent exact P5/Q14 reconstruction and fixed one-Q periodic attack.
No author module, native guest list, or producer verdict is imported.
One-Q domain: all Q copies are translates of this Q, fundamental counts8P/1Q.
"""
from sage.all import CyclotomicField, QQbar, AA, QQ, ZZ, PolynomialRing, matrix, vector, lcm
from itertools import combinations
from functools import cache
from pathlib import Path
import argparse,json,runpy
K=CyclotomicField(28);z=K.gen();i=z**7
embedding=K.hom([QQbar.zeta(28)],QQbar)
def conj(w):return w.conjugate()
def real(w):return (w+conj(w))/2
def imag(w):return (w-conj(w))/(2*i)
@cache
def sign(w):
    assert imag(w)==0
    q=AA(embedding(w).real());return 1 if q>0 else -1 if q<0 else 0

def cross(a,b):return imag(conj(a)*b)
def area(F):return sum(cross(a,b) for a,b in zip(F,F[1:]+F[:1]))/2

def polygon(edges):
    out=[K(0)]
    for e in edges:out.append(out[-1]+e)
    assert out[-1]==0
    return out[:-1]

def convex(F):
    return all(sign(cross(F[(k+1)%len(F)]-a,b-a))>0 for k,a in enumerate(F)
               for j,b in enumerate(F) if j not in [k,(k+1)%len(F)])

s=(z-z**-1)/(2*i);y=2*s+4*s*s;v=1+2*s*(1-y)
P=polygon([length*z**power for length,power in zip([1,1,1,v,y],[-5,1,7,13,19])])
assert convex(P) and sign(y)>0 and sign(1-y)>0 and sign(v-1)>0

def options(Q,k,word):
    A=Q[k];B=Q[(k+1)%14];out=[]
    native=1 if word[k]==0 else 3
    a=P[native];b=P[(native+1)%5]
    for hand in [-1,1]:
        for reverse in [False,True]:
            ta,tb=(B,A) if reverse else (A,B)
            rotation=(tb-ta)/((b-a) if hand==1 else conj(b-a))
            shift=ta-rotation*(a if hand==1 else conj(a))
            F=[shift+rotation*(p if hand==1 else conj(p)) for p in P]
            centre=sum(F)/5
            if sign(cross(B-A,centre-A))>=0:continue
            assert real(rotation*conj(rotation))==1
            # Noncontact edge endpoints at each native Q endpoint.
            ends=[]
            for endpoint in [A,B]:
                corner=F.index(endpoint)
                adjacent=[F[(corner-1)%5],F[(corner+1)%5]]
                other=next(t for t in adjacent if t not in [A,B])
                ends.append(other)
            out.append({'hand':hand,'rotation':rotation,'shift':shift,'face':F,'ends':ends,'native':native})
    assert len(out)==2
    return out

def cycles(opts):
    out=[]
    def extend(indices):
        k=len(indices)
        if k==14:
            if opts[13][indices[13]]['ends'][1]==opts[0][indices[0]]['ends'][0]:out.append(indices)
            return
        for c in range(2):
            if k and opts[k-1][indices[-1]]['ends'][1]!=opts[k][c]['ends'][0]:continue
            extend(indices+[c])
    extend([]);return out

@cache
def disjoint(F,G):
    for H in [F,G]:
        for a,b in zip(H,H[1:]+H[:1]):
            ff=[cross(b-a,p) for p in F];gg=[cross(b-a,p) for p in G]
            loF=hiF=ff[0];loG=hiG=gg[0]
            for t in ff[1:]:
                if sign(t-loF)<0:loF=t
                if sign(t-hiF)>0:hiF=t
            for t in gg[1:]:
                if sign(t-loG)<0:loG=t
                if sign(t-hiG)>0:hiG=t
            if sign(hiF-loG)<=0 or sign(hiG-loF)<=0:return True
    return False

def mate(F):
    a,b=F[4],F[0];e=b-a
    return [a+e/conj(e)*conj(p-a) for p in F]

def one_Q_attack(Q,word,opts,cycle):
    gains=[]
    for k,c in enumerate(cycle):
        if word[k]:continue
        guest=opts[k][c];F=guest['face'];a,b=F[3],F[4]
        wanted=-(b-a) if guest['hand']==1 else b-a
        matches=[j for j in range(14) if word[j] and Q[(j+1)%14]-Q[j]==wanted]
        if not matches:return {'status':'NO_WITNESS_IN_ONE_Q_DOMAIN','reason':'mandatory v-neighbor cannot be translated Q','failed_u_slot':k}
        assert len(matches)==1
        target=b if guest['hand']==1 else a
        gains.append(target-Q[matches[0]])
    assert len(gains)==6
    return {'status':'UNRESOLVED_IN_ONE_Q_DOMAIN','reason':'mandatory translation bridges survived; further exact motif check required'}

def run():
    R=PolynomialRing(ZZ,'t');t=R.gen();phi=t**6-t**5+t**4-t**3+t**2-t+1
    words=[];allmask=0
    for slots in combinations(range(14),8):
        allmask+=1;word=tuple(int(k in slots) for k in range(14))
        if sum(word[k]*t**k for k in range(14))%phi==0:
            assert all(word[k]==word[k+7] for k in range(7));words.append(word)
    assert allmask==3003 and len(words)==35
    rows=[];surviving=0;total=0;completed_count=0;attack_counts={}
    for word in words:
        Q=polygon([(v if bit else 1)*z**(2*k) for k,bit in enumerate(word)]);assert convex(Q)
        opts=[options(Q,k,word) for k in range(14)];native=cycles(opts)
        if native:surviving+=1
        reports=[]
        for cycle in native:
            faces=[Q]+[opts[k][c]['face'] for k,c in enumerate(cycle)]
            assert all(disjoint(tuple(F),tuple(G)) for F,G in combinations(faces,2))
            # Radius-one placement and mandatory alpha-y mates are checked
            # independently from producer clipping, via separating axes.
            completed=faces[:]
            for F in faces[1:]:
                M=mate(F)
                if not any(set(M)==set(G) for G in completed):completed.append(M)
            assert len(completed)==21
            overlap=next(((f,g) for f,g in combinations(range(len(completed)),2) if not disjoint(tuple(completed[f]),tuple(completed[g]))),None)
            if overlap is None:
                completed_count+=1
                report=one_Q_attack(Q,word,opts,cycle)
            else:
                report={'status':'FORCED_LOCAL_OVERLAP','reason':'mandatory alpha-y dimer completion overlaps','faces':list(overlap)}
            reports.append({'cycle':cycle,'completed_faces':len(completed),'one_Q_attack':report})
            key=report['reason'];attack_counts[key]=attack_counts.get(key,0)+1
        total+=len(native)
        rows.append({'word':list(word),'native_cycles':reports})
        print('Independent word', ''.join(map(str,word)), 'native cycles',len(native),'completed total',completed_count,flush=True)
    assert surviving==14 and total==896 and completed_count==364
    adversary=runpy.run_path(str(Path(__file__).resolve().parents[1]/'searches'/'construction-adversary-2026-10-14.py'))
    PAA=[vector(AA,[embedding(p).real(),embedding(p).imag()]) for p in P]
    omission=adversary['omission_search'](PAA)
    raw_u=adversary['native_attachments'](PAA,vector(AA,[0,0]),vector(AA,[1,0]))
    raw_v=adversary['native_attachments'](PAA,vector(AA,[0,0]),vector(AA,[AA(embedding(v).real()),0]))
    assert len(raw_u)==6 and len(raw_v)==2
    assert {o['native_side'] for o in raw_u}=={0,1,2}
    assert {o['determinant'] for o in raw_u}=={-1,1}
    p_stars=adversary['angle_stars']([QQ(5)/7,QQ(4)/7],QQ(2))
    assert p_stars==[[2,1]] and not adversary['angle_stars']([QQ(5)/7,QQ(4)/7],QQ(1))
    q_omission=adversary['palette_obstruction']([QQ(6)/7])
    return {'schema':'independent-P5Q14-adversary-v1','complete_binary_masks':allmask,
            'closed_opposite_paired_words':len(words),'words_with_disjoint_cycles':surviving,
            'total_disjoint_native_cycles':total,'disjoint_forced_dimer_patches':completed_count,'forced_dimer_overlap_rejections':total-completed_count,'rows':rows,
            'one_Q_attack_counts':attack_counts,'P_restricted_omission_search':omission,'raw_native_u_v_attachment_counts':[len(raw_u),len(raw_v)],
            'P_monohedral_native_balance':{'status':'UNTILEABLE','full_stars':p_stars,'native_tile_counts':[1,4],'star_zero_weight':[1,-2],'tile_weight':-7},
            'Q_omission_palette':q_omission,
            'scope':'Fixed P metric; all binary Q8v6u words. One-Q negatives concern only translation orbit model.'}

def main():
    p=argparse.ArgumentParser();p.add_argument('--output');p.add_argument('--check');a=p.parse_args();r=run()
    if a.check:assert json.loads(Path(a.check).read_text())==r
    if a.output:
        with Path(a.output).open('x') as f:json.dump(r,f,indent=2);f.write('\n')
    print(json.dumps({k:v for k,v in r.items() if k!='rows'},indent=2))
if __name__=='__main__':main()
