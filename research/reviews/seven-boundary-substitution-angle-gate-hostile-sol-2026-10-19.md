# Independent hostile review of the retained angle gate

Date: 2026-10-19.

## Scope and audit

Reviewed the retained six-boundary manuscript and JSON certificate, and the seven-boundary angle-gate Python and JSON result. Input SHA256 is `0089ecc0cd79b1253db3b0d18ac84a7aafb87a98a2e1845c0243f377c3e53045`. Only this review file was edited; no metric search, git mutation, or log edit was performed.

The production gate correctly uses twelve shared real native angles, five for P and seven for Q. Their sums are 3 and 5 in units pi, and every entry is strictly between zero and one. These are necessary for genuine convex native polygons. No regularity, distinctness of angles, rational denominator, or numerical tolerance is imposed. Repeated equal angles and symmetric polygons remain allowed.

Each child independently receives all 2n cyclic or reversed cyclic native angle words. The selector value 2*phase+r is unique for each of the n phases and two signs, and the finite disjunction both bounds the selector and binds every corner value. There are 20 P children and five Q children across both parents, hence 10^20 * 14^5 possible formal assignments before duplicate angle values are identified. The solver does not explicitly enumerate that many cases; its exact linear-real/integer formula represents them all. No child phase or reflection is fixed.

The node equations are correct: each f has three child corners totaling 2, each t has two totaling 1, and each u has one equal to the corresponding parent native angle. Independently checked counts are P: 16 f, eight t, five u; Q: 15 f, seven t, seven u. The explicit parent-role maps equal the numeric u suffixes. In particular Q u1,u2 belong to e0, u3 to a2, u4,u5 to a3, and u6 to a5; P u0,u1 belong to e0, u2 to a2, and u3,u4 to e1. No parent corner is omitted or merged.

Fixing parent index j at u_j is justified. The prototype native cyclic labels can be chosen along its own parent boundary, independently for P and Q; each child's unrestricted dihedral assignment then expresses its correspondence to that labeled prototype. Introducing an additional parent phase would only relabel a whole species and would not enlarge geometric possibilities. There is no false symmetry fixing in the code.

## Interpretation attacks

The input is the exact retained oriented incidence pair, including its species assignments and positions of parent corners. Permitting reflections does not miss rotated physical copies: physical rotation has no effect on an angle word, while a different starting vertex is precisely a cyclic phase. Uniform inflation has no effect on native angles. Omitting edge lengths, closure, common similarity scale, edge matching, and nonoverlap makes this a necessary relaxation of geometric realization. Consequently UNSAT of this relaxation excludes geometric realization of this exact pair; those omitted constraints cannot restore feasibility.

This conclusion does not exclude all incidence maps with these inventories, all seven-boundary designs, a different parent corner distribution, another species assignment, or the unrestricted two-polygon problem. No recognizability, plane tiling, shape-only forcing, or aperiodicity conclusion follows. The source verifier is a SAT-witness checker, not an independent UNSAT proof checker. The reported UNSAT is an exact solver decision and carries the usual trust in Z3 rather than a separately checked proof artifact.

## Replay

An independent reconstruction was run without importing the production solver: for each child use an integer selector in [0,2n), list permutations in reflection-major rather than phase-major order, and express each corner directly as a nested If over the shared native angle variables. Sum those expressions at each node and impose the independently checked targets above. This removes all production per-corner variables and its disjunction of conjunctions, while preserving the same finite real feasibility problem. A separate direct production replay was also launched without writing its output certificate.

The independent nested-If reconstruction returned **UNSAT in 107.587444081 seconds**, Z3 4.16.0, with timeout 180000 ms. The direct production replay returned **UNSAT in 51.470937448 seconds**, timeout 120000 ms, Z3 4.16.0, formula SHA256 `882c2a435be5d7a1154ab0db3ee082f1a588828062781dd66f2bf9c337b65e2c`. Both used the input hash above. The original retained 43.2578-second result is therefore independently corroborated by a differently structured exact encoding, as well as replayed directly. No finite rational grid was used.

Verdict: **VALID within the stated finite scope.** The retained two-parent incidence pair has no simultaneous strict native-angle assignment and therefore no realization by the intended two convex native polygons. The broader construction problem remains unresolved. The parent agent additionally reports a P-only UNSAT diagnostic; that stronger localization is not independently replayed by this review and is unnecessary for this verdict.

## Retained independent reconstruction source

Run from the repository root. This is the exact independent reconstruction source used above; elapsed time may vary.

```bash
mise exec -- conda run --no-capture-output -n arisearch python - <<'PY'
import json,z3,time,hashlib
from collections import defaultdict
from pathlib import Path
p=Path('research/searches/six-boundary-substitution-2026-10-19.json'); d=json.loads(p.read_text()); s=z3.Solver();s.set(timeout=180000)
a={k:[z3.Real('ind_'+k+str(i)) for i in range(n)] for k,n in [('P',5),('Q',7)]}
for k,v in a.items():
 s.add(z3.Sum(v)==len(v)-2)
 for x in v:s.add(x>0,x<1)
counts={}
for par,m in d.items():
 nodes=defaultdict(list)
 for child,w in m['corner_words'].items():
  aa=a[m['species'][child]];n=len(aa); sel=z3.Int('ind_sel_'+par+child);s.add(sel>=0,sel<2*n)
  perms=[[(r+e*k)%n for k in range(n)] for e in (-1,1) for r in range(n)]
  assert len({tuple(v) for v in perms})==2*n
  for k,node in enumerate(w):
   expr=aa[perms[-1][k]]
   for j in reversed(range(2*n-1)):expr=z3.If(sel==j,aa[perms[j][k]],expr)
   nodes[node].append(expr)
 counts[par]={c:sum(node.startswith(c) for node in nodes) for c in 'ftu'}
 for node,v in nodes.items():
  typ=node[0];assert len(v)=={'f':3,'t':2,'u':1}[typ]
  target={'f':2,'t':1}.get(typ)
  if typ=='u':
   assert m['parent_corner_roles'][node]==int(node[1:]);target=a[par][int(node[1:])]
  s.add(z3.Sum(v)==target)
print('input_sha256',hashlib.sha256(p.read_bytes()).hexdigest(), 'counts',counts,flush=True)
t=time.monotonic();res=s.check();print('independent_nested_if_result',res,'elapsed',time.monotonic()-t,'z3',z3.get_version_string(),flush=True)
PY
```
