"""Exact native similarities transfer three explicit quotients to all12 slot survivors.
Common positive rescaling required for both prototiles; independent rotations
and native reflections allowed. Read-only replay; explicit --output for writes.
"""
import argparse,json,runpy
from pathlib import Path
from itertools import combinations_with_replacement
helper=runpy.run_path(str(Path(__file__).with_name('branching-hexagon-new-two-run-catalog-slot-periodic.py')))
QQbar=helper['QQbar']
REPS=[([120,120,90,150],'branching-hexagon-new-two-run-four-face-periodic.json'),
      ([90,90,90,150],'branching-hexagon-new-two-run-sqrt2plus3-four-face-periodic.json'),
      ([150,150,90,150],'branching-hexagon-new-two-run-third-orbit-eight-face-periodic.json')]

def congruence(src,tgt,scale):
    for ori in(1,-1):
        for k in range(6):
            den=src[1]-src[0]
            if ori==-1:den=den.conjugate()
            rot=(tgt[(k+ori)%6]-tgt[k])/den
            if rot*rot.conjugate()!=scale*scale:continue
            image=lambda i:rot*(src[i] if ori==1 else src[i].conjugate())
            shift=tgt[k]-image(0)
            if all(tgt[(k+ori*i)%6]==image(i)+shift for i in range(6)):
                return {'native_vertex_shift':k,'native_orientation':ori}
    return None

def transfers(output=None):
    root=Path(__file__).parents[1];catalog=json.loads((root/'certificates/branching-hexagon-new-two-run-catalog-slot-balance.json').read_text())
    srcs=[(q,name,helper['geometry'](q)) for q,name in REPS];results=[]
    for row in catalog['records']:
        if row['status']!='sat':continue
        q=row['quad'];tg=helper['geometry'](q);found=None
        for sq,name,sg in srcs:
            for scalename,scale in [('1',QQbar(1)),('target_p',QQbar(tg[0]))]:
                maps=[congruence(sg[3][i],tg[3][i],scale) for i in(0,1)]
                if all(maps):found=(sq,name,scalename,maps);break
            if found:break
        assert found,('No explicit periodic source congruence',q)
        sq,name,scalename,maps=found;src=json.loads((root/'certificates'/name).read_text());faces=[];offsets=[]
        for face in src['faces']:
            s=0 if face['species']=='A' else 1;m=maps[s];mirror=bool(face['mirror'])^(m['native_orientation']==-1)
            offset=(-1 if mirror else 1)*m['native_vertex_shift']%6;offsets.append(offset)
            faces.append({'species':'A' if s==0 else 'B','mirror':mirror,'labels':tg[1][s][::-1] if mirror else tg[1][s]})
        pairs=[((u,(i+offsets[u])%6),(v,(j+offsets[v])%6)) for (u,i),(v,j) in src['paired_edges']]
        classes=[[(u,(i+offsets[u])%6) for u,i in cls] for cls in src['vertex_classes']]
        # Exact verification of the transferred seam lengths and native stars.
        for (u,i),(v,j) in pairs:assert faces[u]['labels'][i]==faces[v]['labels'][j]
        for cls in classes:
            prod=QQbar(1)
            for u,i in cls:
                s=0 if faces[u]['species']=='A' else 1;ni=(-i)%6 if faces[u]['mirror'] else i
                prod*=tg[2][6*s+ni]
            assert len(cls)==3 and prod==1
        rec={'quad':q,'source_quad':sq,'source_quotient':name,'common_scale':scalename,'native_congruences':maps,
             'faces':faces,'paired_edges':pairs,'vertex_classes':classes}
        results.append(rec);print('PERIODIC',q,'source',sq,'scale',scalename,'faces',len(faces),flush=True)
    assert len(results)==12
    out={'domain':'all12 exact native-slot survivors; complete native common-scale congruences to3 explicit periodic quotients','records':results}
    if output:Path(output).write_text(json.dumps(out,indent=2)+'\n')
    print('PASS all12 explicit periodic transfers')
    return out
if __name__=='__main__':
    p=argparse.ArgumentParser();p.add_argument('--output');a=p.parse_args();transfers(a.output)
