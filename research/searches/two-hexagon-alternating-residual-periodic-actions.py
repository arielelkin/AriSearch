#!/usr/bin/env python3
"""Seven positive full-native tori from exact commuting ring actions.

Checks all action identities, constructs a stabilizer HNF of exact index
3*orbit size, then verifies canonical stars and whole-side class matches.
No bounded periodic absence search or solver is used.
"""
import importlib.util
import json
import sys

def module(name,path):
    spec=importlib.util.spec_from_file_location(name,path)
    result=importlib.util.module_from_spec(spec);spec.loader.exec_module(result)
    return result

local=module('periodic_action_native','research/searches/two-hexagon-interleaved-local-side-gate.py')
colour=module('periodic_action_directions','research/searches/two-hexagon-rank-nine-colour-transport.py')

def inverse(p):
    q=[None]*len(p)
    for i,j in enumerate(p):q[j]=i
    assert all(v is not None for v in q)
    return q

def apply_power(p,n,i):
    if n<0:p=inverse(p);n=-n
    for _ in range(n):i=p[i]
    return i

def orbits(f0,f1):
    unseen=set(range(len(f0)));out=[]
    while unseen:
        seen={min(unseen)};todo=list(seen)
        while todo:
            i=todo.pop()
            for p in (f0,f1):
                j=p[i]
                if j not in seen:seen.add(j);todo.append(j)
        unseen-=seen;out.append(sorted(seen))
    return out

def torus(row,core,successors,orbit):
    q0=orbit[0];n=3*len(orbit)
    def act(z):
        x,y=z;assert (x-y)%3==0
        a=(2*x+y)//3;b=(y-x)//3
        return apply_power(successors[1],b,apply_power(successors[0],a,q0))
    hnfs=[]
    for a in range(1,n+1):
        if n%a or a%3:continue
        c=n//a
        for b in range(a):
            if (b-c)%3==0 and act((a,0))==q0 and act((b,c))==q0:hnfs.append((a,b,c))
    assert hnfs
    a,b,c=min(hnfs)
    def reduce(z):
        x,y=z;q,y=divmod(y,c)
        return ((x-q*b)%a,y)
    labels={}
    def put(z,sym):
        z=reduce(z);assert labels.get(z,sym)==sym,(row['joint_metric_orbit_id'],z)
        labels[z]=sym
    for y in range(c):
        for x in range(a):
            if (x-y)%3:continue
            state=core[act((x,y))]
            put((x,y),12+state['B'])
            for k,(dx,dy) in enumerate(colour.D):put((x+dx,y+dy),state['A_ring'][k])
    assert len(labels)==n
    lengths=row['A_native_side_partition']+row['B_native_side_word']
    stars=[];seams=[];parent=list(range(12))
    def find(i):
        while parent[i]!=i:i=parent[i]
        return i
    def union(i,j):parent[find(j)]=find(i)
    for y in range(c):
        for x in range(a):
            sym=labels[(x,y)];t=sym//12;p=sym%12
            for k in (0,1):
                native=[];species=[];colours=[]
                for dx,dy,slot in [(0,0,k),(*colour.D[k],(k+2)%6),(*colour.D[(k+1)%6],(k+4)%6)]:
                    z=labels[reduce((x+dx,y+dy))];tz=z//12;j=local.corner(z%12,slot)
                    native.append(6*tz+j);species.append(tz);colours.append(local.WORDS['ALT'][j])
                assert sorted(species)==[0,0,1] and len(set(colours))==1
                stars.append(native)
            for k in range(6):
                dx,dy=colour.D[(k+1)%6];z=labels[reduce((x+dx,y+dy))]
                i=6*t+local.side(p,k);j=6*(z//12)+local.side(z%12,k+3)
                assert lengths[i]==lengths[j],(row['joint_metric_orbit_id'],x,y,k,i,j)
                union(i,j);seams.append([i,j])
    names={};closure=[]
    for i in range(12):
        f=find(i)
        if f not in names:names[f]=len(names)
        closure.append(names[f])
    for i in range(12):
        for j in range(12):
            if closure[i]==closure[j]:assert lengths[i]==lengths[j]
    return {'base_state':q0,'coarse_B_orbit':orbit,'hnf':[a,b,c],'index':n,
            'period_generators':[[a,0],[b,c]],
            'cell_order':[[x,y] for y in range(c) for x in range(a)],
            'labels':[labels[(x,y)] for y in range(c) for x in range(a)],
            'vertex_stars':stars,'side_equalities':seams,
            'actual_side_length_classes':lengths,'required_side_closure':closure}

def main(source,path):
    ledger=json.load(open(source));records=[]
    for row in ledger['rows']:
        if row['verdict']=='EMPTY':continue
        assert row['maximum_successor_degrees']==[1]*6
        alive=row['survivors'];core=[row['canonical_ring_states'][i] for i in alive]
        index={i:j for j,i in enumerate(alive)};successors=[]
        for edges in row['compatibility']:
            p=[]
            for i in alive:
                choices=[index[j] for x,j in edges if x==i and j in index]
                assert len(choices)==1;p.append(choices[0])
            assert sorted(p)==list(range(len(alive)));successors.append(p)
        for k in range(3):assert successors[k+3]==inverse(successors[k])
        for i in range(len(core)):
            assert successors[0][successors[1][i]]==successors[1][successors[0][i]]
            assert successors[2][i]==successors[1][inverse(successors[0])[i]]
        components=orbits(successors[0],successors[1])
        witness=torus(row,core,successors,components[0])
        records.append({'joint_metric_orbit_id':row['joint_metric_orbit_id'],
                        'A_native_side_partition':row['A_native_side_partition'],
                        'B_native_side_word':row['B_native_side_word'],
                        'core_original_indices':alive,'core_states':core,'successor_permutations':successors,
                        'commuting_action_orbits':components,'torus':witness})
        print(row['joint_metric_orbit_id'],'orbit',components[0],'index',witness['index'],'HNF',witness['hnf'],flush=True)
    assert len(records)==7
    result={'scope':'Direct positive metric tori for all seven final ALT canonical cases; preserves every actual metric in each side word; no additional equality or generic angle assumption',
            'native_transport_source':source,'rows':records}
    with open(path,'w') as f:json.dump(result,f,indent=2)

if __name__=='__main__':main(sys.argv[1],sys.argv[2])
