#!/usr/bin/env python3
"""Independent local native seam census; no producer/global-SFT imports."""
import argparse, collections, hashlib, importlib.util, itertools, json
from pathlib import Path
HERE=Path(__file__).resolve().parent
spec=importlib.util.spec_from_file_location('canonical_colour_review',HERE/'check_two_hexagon_rank_nine_colour_transport.py')
g=importlib.util.module_from_spec(spec);spec.loader.exec_module(g)

def closure(bp,aa):
    # Build side equalities by coordinates of the seven cells; all edges
    # within this patch are included exactly once.
    cells={(0,0):(1,bp)}|{z:(0,aa[k]) for k,z in enumerate(g.D)}
    links=[]
    for z,(t,p) in cells.items():
        for k,d in enumerate(g.D):
            w=g.add(z,d)
            if w not in cells or z>=w:continue
            u,q=cells[w];opposite=g.D.index(g.sub(z,w))
            links.append((6*t+g.side(p,(k-1)%6),6*u+g.side(q,(opposite-1)%6)))
    assert len(links)==12
    classes=[{i} for i in range(12)]
    for i,j in links:
        left=next(c for c in classes if i in c);right=next(c for c in classes if j in c)
        if left!=right:classes.remove(left);classes.remove(right);classes.append(left|right)
    classes.sort(key=min)
    return tuple(next(k for k,c in enumerate(classes) if i in c) for i in range(12))

def main():
    ap=argparse.ArgumentParser();ap.add_argument('--output');args=ap.parse_args()
    path=Path('research/certificates/two-hexagon-interleaved-local-side-gate.json');cert=json.loads(path.read_text());summary=[]
    for row in cert['rows']:
        b=row['B'];counts=collections.Counter();total=0;killed=0
        for bp in g.P:
            bw=g.placed(g.WORDS[b],bp);choices=[]
            for k,z in enumerate(g.D):
                relevant=[inc for inc in g.INC if z in inc]
                assert len(relevant)==2
                choices.append([p for p in g.P if all(g.placed(g.WORDS['I'],p)[inc[z]]==bw[inc[(0,0)]] for inc in relevant)])
            for aa in itertools.product(*choices):
                eq=closure(bp,aa);counts[eq]+=1;total+=1
                killed+=eq[0]==eq[2]==eq[4] and eq[1]==eq[3]==eq[5]
        stored={tuple(r['closure']):r for r in row['distinct_closures']}
        assert set(counts)==set(stored)
        for eq,count in counts.items():
            r=stored[eq];assert r['count']==count
            assert r['forces_A_side_period_two']==(eq[0]==eq[2]==eq[4] and eq[1]==eq[3]==eq[5])
            rep=r['representative'];bp=g.P[rep['B_placement']];aa=[g.P[i] for i in rep['A_ring']]
            assert closure(bp,aa)==eq
            for inc in g.INC:
                colours=[g.placed(g.WORDS[b],bp)[inc[(0,0)]]]+[g.placed(g.WORDS['I'],aa[g.D.index(z)])[k] for z,k in inc.items() if z!=(0,0)]
                assert len(set(colours))==1
        assert total==row['native_ring_count'] and killed==row['period_two_rejections'] and total-killed==row['remaining_count']
        summary.append([b,total,killed,total-killed,len(counts)])
    assert summary==[['C',3072,384,2688,67],['I',12288,6264,6024,105],['ALT',49152,0,49152,1628]]
    # Exterior turns at the next vertex, coefficients of p and constants.
    native=((1,0),(1,0),(-1,240),(1,0),(-1,240),(-1,240))
    direction=(0,0);directions=[direction]
    for k in range(1,6):
        coefficient,constant=native[k]
        direction=(direction[0]-coefficient,direction[1]+180-constant);directions.append(direction)
    assert directions==[(0,0),(-1,180),(0,120),(-1,300),(0,240),(1,180)]
    result={'status':'PASSED','local_native_ring_census':summary,'derived_side_directions':directions,
            'source_sha256':hashlib.sha256(path.read_bytes()).hexdigest(),
            'scope':'Exact local period-two rejection only; all remaining rings unresolved globally'}
    if args.output:Path(args.output).write_text(json.dumps(result,indent=2)+'\n')
    print(json.dumps(result))
if __name__=='__main__':main()
