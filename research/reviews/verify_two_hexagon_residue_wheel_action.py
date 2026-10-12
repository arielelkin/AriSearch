#!/usr/bin/env python3
"""Independent solver-free wheel actions and twelve-cell residue tori.
Imports no SFT, pruning producer, CP-SAT, or metric solver.
"""
import argparse
import hashlib
import itertools
import json
from pathlib import Path

D = [(1,0),(0,1),(-1,1),(-1,0),(0,-1),(1,-1)]


def add(a,b):
    return (a[0]+b[0],a[1]+b[1])


def corner(symbol,k):
    q, v = divmod(symbol,12)
    r, s = v%6, (1 if v<6 else -1)
    return 6*q+(r+s*k)%6


def side(symbol,k):
    q, v = divmod(symbol,12)
    r, s = v%6, (1 if v<6 else -1)
    return 6*q+((r+k)%6 if s==1 else (r-k-1)%6)


def equivalent_pairs(classes):
    return {(i,j) for i in range(12) for j in range(i+1,12) if classes[i]==classes[j]}


def closure(pairs):
    parents=list(range(12))
    def find(a):
        while parents[a]!=a:
            a=parents[a]
        return a
    for a,b in pairs:
        parents[find(a)]=find(b)
    return {(i,j) for i in range(12) for j in range(i+1,12) if find(i)==find(j)}


def b_symbol(state):
    r,s=state['B']
    return 12+r+(6 if s==-1 else 0)


def ring_pairs(state,T):
    b=b_symbol(state); A=state['A_ring']; pairs=set()
    for k in range(6):
        triple=tuple(sorted((corner(b,k),corner(A[k],k+2),corner(A[(k+1)%6],k+4))))
        assert triple in T
        pairs.add(tuple(sorted((side(b,k-1),side(A[k],k+2)))))
        pairs.add(tuple(sorted((side(A[k],k+1),side(A[(k+1)%6],k+4)))))
    return {p for p in pairs if p[0]!=p[1]}


def overlap(states,C):
    return [{(u,v) for u in C for v in C
             if states[u]['A_ring'][k]==states[v]['A_ring'][(k+4)%6]
             and states[u]['A_ring'][(k+1)%6]==states[v]['A_ring'][(k+3)%6]}
            for k in range(6)]


def wheel_maps(R,C):
    W={}
    for u in C:
        choices=[[v for v in C if(u,v) in R[k]] for k in range(6)]
        wheels=[list(v) for v in itertools.product(*choices)
                if all((v[k],v[(k+1)%6]) in R[(k+2)%6] for k in range(6))]
        assert len(wheels)==1,(u,len(wheels))
        W[u]=wheels[0]
    assert all({W[u][k] for u in C}==set(C) for k in range(6))
    assert all(W[W[u][k]][(k+3)%6]==u for u in C for k in range(6))
    assert all(W[W[u][0]][1]==W[W[u][1]][0] for u in C)
    assert all(W[u][2]==W[W[u][3]][1] for u in C)
    return W


def power(W,u,k,n):
    if n<0:
        k=(k+3)%6;n=-n
    for _ in range(n):
        u=W[u][k]
    return u


def orbit_of(W,u):
    orbit={u}; todo=[u]
    while todo:
        q=todo.pop()
        for v in W[q]:
            if v not in orbit:
                orbit.add(v);todo.append(v)
    return sorted(orbit)


def action(W,u,a,b):
    return power(W,power(W,u,0,a),1,b)


def torus_for_origin(states,W,origin,T,classes):
    orbit=orbit_of(W,origin)
    assert len(orbit)==4
    def cell_state(z):
        x,y=z
        assert (x-y)%3==0
        a,b=(2*x+y)//3,(-x+y)//3
        return action(W,origin,a,b)
    def period(z):
        return (z[0]-z[1])%3==0 and cell_state(z)==origin
    n=next(n for n in range(1,13) if period((n,0)))
    s,m=next((s,m) for m in range(1,13) for s in range(n) if period((s,m)))
    assert n*m==12
    def label(z):
        if (z[0]-z[1])%3==0:
            return b_symbol(states[cell_state(z)])
        choices=[]
        for k,d in enumerate(D):
            w=(z[0]-d[0],z[1]-d[1])
            if (w[0]-w[1])%3==0:
                choices.append(states[cell_state(w)]['A_ring'][k])
        assert len(choices)==3 and len(set(choices))==1
        return choices[0]
    labels={(x,y):label((x,y)) for x in range(n) for y in range(m)}
    def wrap(z):
        quotient=z[1]//m
        return ((z[0]-s*quotient)%n,z[1]-m*quotient)
    U,E=set(),set()
    for z,a in labels.items():
        assert label(add(z,(n,0)))==a and label(add(z,(s,m)))==a
        for k in range(6):
            b=labels[wrap(add(z,D[k]))]
            c=labels[wrap(add(z,D[(k+1)%6]))]
            triple=tuple(sorted((corner(a,k),corner(b,k+2),corner(c,k+4))))
            assert triple in T
            U.add(triple)
            b=labels[wrap(add(z,D[(k+1)%6]))]
            p=tuple(sorted((side(a,k),side(b,k+3))))
            assert classes[p[0]]==classes[p[1]]
            if p[0]!=p[1]:E.add(p)
    assert U==T
    assert closure(E)==equivalent_pairs(classes)
    return dict(origin_state=origin,orbit=orbit,lattice=[n,s,m],
                labels=[[x,y,v] for (x,y),v in sorted(labels.items())],
                used_triples=sorted(U),side_pairs=sorted(E))


def analyze(row,metric):
    C=row['surviving_states']; states=row['states']
    assert len(C)==len(states)==12
    T={tuple(sorted((a,b,6+j))) for j,(a,b) in enumerate(row['B_pair_order'])}
    classes=metric['length_classes']
    forced=equivalent_pairs(classes)
    assert metric['state_indices']==C
    for u in C:
        assert closure(ring_pairs(states[u],T))==forced
    R=overlap(states,C)
    assert all(R[k]==set(map(tuple,row['compatibility'][k])) for k in range(6))
    W=wheel_maps(R,C)
    orbits=[]; unseen=set(C)
    while unseen:
        orb=orbit_of(W,min(unseen));assert len(orb)==4
        orbits.append(orb);unseen-=set(orb)
    # Verify one native twelve-cell torus for each of the three distinct
    # occurring wheel orbits, not only one accidental favorable origin.
    tori=[torus_for_origin(states,W,min(orb),T,classes) for orb in orbits]
    stripes=[]
    for k in range(6):
        fixed={u for u in C if W[u][k]==u}
        for orb in orbits:
            if set(orb)<=fixed:
                stripes.append(dict(direction=k,orbit=orb))
    return dict(id=row['id'],T=sorted(T),length_classes=classes,
                common_forced_side_pairs=sorted(forced),
                unique_wheels=[[u,*W[u]] for u in C],
                commuting_basis_maps=True,opposite_maps_inverse=True,
                diagonal_map_identity=True,orbits=orbits,
                stripe_directions=stripes,tori=tori,
                verdict='UNIVERSAL_PERIODIC_ESCAPE_INDEX_12')


def main():
    p=argparse.ArgumentParser();p.add_argument('--output',type=Path);p.add_argument('--check',type=Path)
    args=p.parse_args();root=Path(__file__).resolve().parents[1]
    dp=root/'certificates/two-hexagon-odd-pair-graph-orders.json'
    mp=root/'certificates/two-hexagon-odd-pair-graph-ring-metrics.json'
    Ddata=json.loads(dp.read_text());Mdata=json.loads(mp.read_text())
    rows={r['id']:r for r in Ddata['rows']}
    result=[]
    for m in Mdata['rows']:
        residual=[q for q in m['queries'] if q['verdict']=='NO_TORUS_AT_INDEX_LE_8']
        if not residual:continue
        assert len(residual)==len(m['queries'])==1
        result.append(analyze(rows[m['id']],residual[0]))
    assert len(result)==12
    artifact=dict(scope='Twelve branching metric residues; exact unique-wheel action and independently checked twelve-cell torus for every four-state orbit',
                  source_orders_sha256=hashlib.sha256(dp.read_bytes()).hexdigest(),
                  source_metrics_sha256=hashlib.sha256(mp.read_bytes()).hexdigest(),
                  residual_rows=12,orbits_checked=36,torus_index=12,rows=result)
    normalized=json.loads(json.dumps(artifact))
    if args.check:
        assert json.loads(args.check.read_text())==normalized
    if args.output:
        args.output.write_text(json.dumps(artifact,indent=2)+'\n')
    print(json.dumps({'residual_rows':12,'orbits_checked':36,'torus_index':12,
                      'row_lattices':[[r['id'],[t['lattice'] for t in r['tori']]] for r in result]}))

if __name__=='__main__':
    main()
