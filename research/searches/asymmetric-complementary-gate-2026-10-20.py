"""First exact gate for Astra's asymmetric complementary-corner proposal."""
from itertools import product
from importlib.util import spec_from_file_location,module_from_spec
from pathlib import Path
from sage.all import AA, QQ, CyclotomicField

K=CyclotomicField(36)
z=K.gen()
I=z**9

def re(w): return (w+w.conjugate())/2
def im(w): return (w-w.conjugate())/(2*I)
def cr(u,v): return re(u)*im(v)-im(u)*re(v)
def dt(u,v): return re(u)*re(v)+im(u)*im(v)
def solve2(u,v,w):
    d=cr(u,v)
    return cr(w,v)/d,cr(u,w)/d
def poly(ds,ls):
    out=[K(0)]
    for d,l in zip(ds,ls): out.append(out[-1]+l*z**d)
    assert out[-1]==0
    return out[:-1]
def pAA(p): return AA(re(p)),AA(im(p))
def sep(a,b):
    A=[pAA(p) for p in a]; B=[pAA(p) for p in b]
    for poly in (A,B):
        for k in range(len(poly)):
            x,y=poly[k],poly[(k+1)%len(poly)]
            v=(y[0]-x[0],y[1]-x[1])
            f=lambda p:v[0]*(p[1]-x[1])-v[1]*(p[0]-x[0])
            aa=[f(p) for p in A]; bb=[f(p) for p in B]
            if max(aa)<=min(bb) or max(bb)<=min(aa): return False
    return True
def place(poly,idx_a,idx_b,A,B,conj):
    src=lambda w:w.conjugate() if conj else w
    u=(B-A)/(src(poly[idx_b])-src(poly[idx_a]))
    assert u*u.conjugate()==1
    return tuple(A+u*(src(p)-src(poly[idx_a])) for p in poly)

def start_corner(poly,lens,j,at,ray_unit,attach_neighbor,conj):
    k=(j+attach_neighbor)%5
    slot=(j-1)%5 if attach_neighbor==-1 else j
    src=lambda w:w.conjugate() if conj else w
    u=ray_unit*lens[slot]/src(poly[k]-poly[j])
    assert u*u.conjugate()==1
    out=tuple(at+u*(src(p)-src(poly[j])) for p in poly)
    other=(j-attach_neighbor)%5
    other_slot=(j-1)%5 if attach_neighbor==1 else j
    other_unit=(out[other]-at)/lens[other_slot]
    return out,other_unit

def endpoint_completions(existing,at,start_unit,end_unit,corner_sequences):
    out=[]
    for seq in corner_sequences:
        states=[(start_unit,(),())]
        for name,j in seq:
            poly,lens=(P,PL) if name=='P' else (Q,QL)
            nxt=[]
            for ray,tiles,ids in states:
                for side,conj in product((-1,1),(0,1)):
                    candidate,new_ray=start_corner(poly,lens,j,at,ray,side,conj)
                    if any(sep(candidate,z) for z in existing+tiles):continue
                    nxt.append((new_ray,tiles+(candidate,),ids+((name,j,side,conj),)))
            states=nxt
        out.extend((seq,ids,tiles) for ray,tiles,ids in states if ray==end_unit)
    return out

# Angles P=(80,110,100,120,130), Q=(60,100,120,130,130).
# Direction exponents are 10-degree units.
PD=(0,7,15,21,26)
QD=(0,8,14,19,24)
qfix={0:K(1),1:K(2),4:K(QQ(23)/10)}
q2,q3=solve2(z**14,z**19,-sum((v*z**QD[k] for k,v in qfix.items()),K(0)))
QL=(K(1),K(2),q2,q3,K(QQ(23)/10))
pfix={0:K(3),1:K(3),3:K(3)}
p2,p4=solve2(z**15,z**26,-sum((v*z**PD[k] for k,v in pfix.items()),K(0)))
PL=(K(3),K(3),p2,K(3),p4)
assert all(AA(x)>0 for x in PL+QL)
P=poly(PD,PL);Q=poly(QD,QL)

def rao_hits(angles,lengths):
    src=Path(__file__).with_name('convex-substitution-shapes.py')
    spec=spec_from_file_location('rao_asymmetric',src)
    mod=module_from_spec(spec);spec.loader.exec_module(mod)
    L=[AA(x) for x in lengths]
    hits=[]
    for typ,(aeqs,leqs) in mod.RAO.items():
        for sign in (1,-1):
            for off in range(5):
                amap=[(off+sign*i)%5 for i in range(5)]
                a=[angles[i] for i in amap]
                if not all(sum(c*x for c,x in zip(row,a))==36*target
                           for row,target in aeqs):continue
                smap=[(off+i)%5 if sign==1 else (off-i-1)%5 for i in range(5)]
                if all(sum((c*L[i] for c,i in zip(row,smap)),AA(0))==0
                       for row in leqs):hits.append((typ,sign,off))
    return hits

def main():
    print('P lengths AA',tuple(AA(x) for x in PL))
    print('Q lengths AA',tuple(AA(x) for x in QL))
    print('P exact lengths',PL)
    print('Q exact lengths',QL)
    print('Rao P/Q hits',rao_hits((80,110,100,120,130),PL),
          rao_hits((60,100,120,130,130),QL))
    print('P turn signs',tuple(AA(cr(P[(i+1)%5]-P[i],P[(i+2)%5]-P[(i+1)%5]))>0 for i in range(5)))
    print('Q turn signs',tuple(AA(cr(Q[(i+1)%5]-Q[i],Q[(i+2)%5]-Q[(i+1)%5]))>0 for i in range(5)))
    A=P[3];B=P[4]
    assert AA((B-A)*(B-A).conjugate())==9
    for order in (0,1):
        # order=0 has length 1 from A, length 2 toward B.
        M=A+(B-A)*(QQ(1)/3 if order==0 else QQ(2)/3)
        left=(Q,0,1,M,A) if order==0 else (Q,2,1,M,A)
        right=(Q,2,1,M,B) if order==0 else (Q,0,1,M,B)
        branches=[]
        for ca,cb in product((0,1),repeat=2):
            qa=place(left[0],left[1],left[2],left[3],left[4],ca)
            qb=place(right[0],right[1],right[2],right[3],right[4],cb)
            if sep(P,qa) or sep(P,qb) or sep(qa,qb):continue
            ra=qa[4]-M if order==0 else qa[3]-M
            rb=qb[3]-M if order==0 else qb[4]-M
            branches.append((ca,cb,qa,qb,cr(ra,rb)==0 and AA(dt(ra,rb))>0))
        print('order',order,'nonoverlap branches',[(x[0],x[1],x[4]) for x in branches])
        print('endpoint angular residuals',(360-120-100,360-130-100))
        if branches:
            ca,cb,qa,qb,closed=branches[0]
            print('order',order,'closed split',closed,'seam Q rays',pAA(qa[4]-M if order==0 else qa[3]-M),pAA(qb[3]-M if order==0 else qb[4]-M))
            qa_other=2 if order==0 else 0
            qb_other=0 if order==0 else 2
            qa_len=QL[1] if order==0 else QL[0]
            qb_len=QL[0] if order==0 else QL[1]
            split=(P,qa,qb)
            left=endpoint_completions(split,A,(P[2]-A)/PL[2],(qa[qa_other]-A)/qa_len,
                 ((('P',0),('Q',0)),(('Q',0),('P',0))))
            right=endpoint_completions(split,B,(P[0]-B)/PL[4],(qb[qb_other]-B)/qb_len,
                 ((('P',4),),(('Q',3),),(('Q',4),)))
            print('order',order,'endpoint full-corner completions A',[(x[1]) for x in left])
            print('order',order,'endpoint full-corner completions B',[(x[1]) for x in right])
            both=[(x[1],y[1]) for x,y in product(left,right)
                  if all(not sep(u,v) for u,v in product(x[2],y[2]))]
            print('order',order,'simultaneous endpoint completion count',len(both))
    for mode,second,ia,ib in (
        ('mirror',place(P,3,4,A,B,1),3,4),
        ('halfturn',place(P,3,4,B,A,0),4,3)):
        assert not sep(P,second)
        if mode=='mirror':
            aseq=((('P',3),),(('Q',2),),(('Q',0),('Q',0)))
            bseq=((('P',2),),(('Q',1),))
        else:
            aseq=bseq=((('P',1),),)
        anbr=2 if ia==3 else 0
        bnbr=0 if ib==4 else 2
        alen=PL[2] if ia==3 else PL[4]
        blen=PL[4] if ib==4 else PL[2]
        aout=endpoint_completions((P,second),A,(P[2]-A)/PL[2],
                                  (second[anbr]-A)/alen,aseq)
        bout=endpoint_completions((P,second),B,(P[0]-B)/PL[4],
                                  (second[bnbr]-B)/blen,bseq)
        print('P/P',mode,'endpoint A completions',[(x[1]) for x in aout])
        print('P/P',mode,'endpoint B completions',[(x[1]) for x in bout])
        print('P/P',mode,'simultaneous count',sum(
            all(not sep(u,v) for u,v in product(x[2],y[2]))
            for x,y in product(aout,bout)))
    print('scope: exact closure, positivity, split and P/P endpoint atlas only')

if __name__=='__main__':main()
