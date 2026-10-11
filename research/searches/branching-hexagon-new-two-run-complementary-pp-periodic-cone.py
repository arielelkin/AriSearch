"""Exact affine-angle and topology certificate for complementary-pp eight-face periodic cone.
Normal replay read-only; explicit --output required to retain a certificate.
Closure/strict-convexity proof and necessity classification are analytic in lemma.
"""
import argparse,json
from pathlib import Path
from collections import Counter,defaultdict
A=[(120,1,0),(120,-1,0)]*3
B=[(240,-1,-1),(0,0,1),(180,0,-1),(60,1,1),(120,-2,0),(120,2,0)]
AD=[(0,0,0),(60,1,0),(120,0,0),(180,1,0),(240,0,0),(300,1,0)]
BD=[(0,0,0),(180,0,-1),(180,0,0),(300,-1,-1),(360,1,-1),(420,-1,-1)]
AT=[(60,1,0),(60,-1,0)]*3
BT=[(180,0,-1),(0,0,1),(120,-1,-1),(60,2,0),(60,-2,0),(-60,1,1)]
VERTICES=[(0,60),(0,120),(30,90),(30,30)]

def prove(output=None):
    root=Path(__file__).parents[1];source=root/'certificates/branching-hexagon-new-two-run-third-orbit-eight-face-periodic.json'
    r=json.loads(source.read_text());faces=r['faces'];pairs=r['paired_edges'];classes=r['vertex_classes']
    used=Counter();adj=defaultdict(list);graph=defaultdict(set)
    for (u,i),(v,j) in pairs:
        assert faces[u]['labels'][i]==faces[v]['labels'][j]
        used[u,i]+=1;used[v,j]+=1;graph[u].add(v);graph[v].add(u)
        for x,y in[((u,i),(v,(j+1)%6)),((u,(i+1)%6),(v,j))]:adj[x].append(y);adj[y].append(x)
    assert set(used)=={(u,i) for u in range(8) for i in range(6)} and set(used.values())=={1}
    reached={0};todo=[0]
    while todo:
        for v in graph[todo.pop()]-reached:reached.add(v);todo.append(v)
    assert reached==set(range(8));assert len(classes)-len(pairs)+len(faces)==0
    allnodes=set();sums=[];native_link_types=Counter()
    for cls in classes:
        nodes=set(map(tuple,cls));assert len(nodes)==3 and not allnodes.intersection(nodes);allnodes.update(nodes)
        assert all(len(adj[x])==2 for x in nodes)
        reached=set();todo=[next(iter(nodes))]
        while todo:
            v=todo.pop()
            if v not in reached:reached.add(v);todo+=adj[v]
        assert reached==nodes
        vals=[];names=[]
        for u,i in cls:
            f=faces[u];aa=A if f['species']=='A' else B;j=(-i)%6 if f['mirror'] else i;vals.append(aa[j]);names.append(('AH' if j%2==0 else 'AL') if f['species']=='A' else 'B'+str(j))
        sm=tuple(sum(v[k] for v in vals) for k in range(3));assert sm==(360,0,0);sums.append(sm);native_link_types[tuple(sorted(names))]+=1
    assert allnodes==set(used)
    assert native_link_types==Counter({('AH','B0','B1'):4,('AL','B2','B3'):4,('AH','AH','B4'):4,('AL','AL','B5'):4})
    bounds=[]
    for species,turns in[('A',AT),('B',BT)]:
        for coeff in turns:
            values=[coeff[0]+coeff[1]*d+coeff[2]*g for d,g in VERTICES]
            assert min(values)>=0 and max(values)<180 and max(values)>0
            bounds.append({'species':species,'coefficients':coeff,'closed_domain_min':min(values),'closed_domain_max':max(values)})
    out={'domain':'0<delta<30 degrees;60-delta<alpha<120-delta degrees;positive common scale arbitrary',
         'p_formula':'2*cos(delta)','q':1,'affine_coefficient_order':['constant','delta','alpha'],
         'A_angles':A,'B_angles':B,'A_edge_directions':AD,'B_edge_directions':BD,
         'A_turns':AT,'B_turns':BT,'turn_bounds':bounds,'closed_parameter_polygon_vertices':VERTICES,
         'faces':faces,'paired_edges':pairs,'vertex_classes':classes,'angle_sums':sums,
         'fixed_carrier_necessity':{'native_link_types':[[list(k),v] for k,v in sorted(native_link_types.items())],'required_angles':['B0+B1=240-delta','B2+B3=240+delta','B4=120-2delta','B5=120+2delta'],'closure_times_exp_i_alpha':'p*(exp(i*alpha)-1+exp(-i*beta))+2*cos(delta)=0','imaginary_condition':'sin(alpha)=sin(beta)','branches':['beta=alpha; gamma=180-alpha; 0<gamma<120-delta; p=2*cos(delta)/(1+2*cos(gamma))','beta=180-alpha;60-delta<alpha<120-delta;p=2*cos(delta)'],'scope':'only this fixed indexed carrier, not every two-run tiling'},
         'native_closure_factors':{'P_chain':'p*exp(i*(180-alpha))','Q_chain':'2*cos(delta)*exp(-i*alpha)'},
         'exact_fixture_parameters':{'delta':15,'alpha':75},'exact_fixture_quotient':source.name,'exact_fixture_development':'branching-hexagon-new-two-run-complementary-pp-eight-face-development.json',
         'checks':'48unique sides,24equal-label pairs,8connected oriented faces,16single circular links,all affine angle sums(360,0,0),all native turns strict(0,180) on opendomain'}
    if output:Path(output).write_text(json.dumps(out,indent=2)+'\n')
    print('PASS complementary-pp exact2Dperiodiccone;8faces24seams16links allsymbolic360;turnbounds',[(x['closed_domain_min'],x['closed_domain_max']) for x in bounds]);return out
if __name__=='__main__':
    p=argparse.ArgumentParser();p.add_argument('--output');args=p.parse_args();prove(args.output)
