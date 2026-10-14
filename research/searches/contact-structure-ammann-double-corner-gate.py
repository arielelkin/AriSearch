import runpy,json,io
from contextlib import redirect_stdout
with redirect_stdout(io.StringIO()):d=runpy.run_path("research/searches/contact-structure-ammann-corner-triad-gate.py")
z=d["z"];rot=d["rot"];cross=d["cross"];A=d["A"];B=d["B"]
psiH=[rot+z**(-1)*q for q in d["H"]]
psiP=[q+rot-z**2 for q in d["P2"]]
assert psiH[5]==psiP[3]==A[3]
results=[]
patches={}
for kn,K in [("H",d["H"]),("P1",d["P1"])]:
 for ln,L in [("H",psiH),("P2",psiP)]:
  faces=[A,B,K,L]
  for F in faces:
   assert all(cross(F[(i+1)%len(F)]-p,q-p)>0 for i,p in enumerate(F) for j,q in enumerate(F) if j not in (i,(i+1)%len(F)))
  for i,F in enumerate(faces):
   for G in faces[i+1:]:assert any(all(cross(F[(k+1)%len(F)]-p,q-p)<=0 for q in G) for k,p in enumerate(F))
  edges=[(p,F[(i+1)%len(F)]) for F in faces for i,p in enumerate(F)]
  outer=[e for e in edges if (e[1],e[0]) not in edges]
  word=[outer[0][0]]
  while len(word)<len(outer):
   nxt=[q for p,q in outer if p==word[-1]];assert len(nxt)==1;word.append(nxt[0])
  assert (word[-1],word[0]) in outer and len(set(word))==len(word)
  turns=[cross(word[i]-word[i-1],word[(i+1)%len(word)]-word[i]) for i in range(len(word))]
  assert all(t!=0 for t in turns)
  refs=[i for i,t in enumerate(turns) if t<0]
  expected={('H','H'):(12,3),('H','P2'):(11,2),('P1','H'):(11,3),('P1','P2'):(10,2)}
  assert (len(word),len(refs))==expected[kn,ln]
  if len(refs)==3:assert cross(word[refs[1]]-word[refs[0]],word[refs[2]]-word[refs[0]])!=0
  else:
   assert len(refs)==2
   gap=(refs[1]-refs[0])%len(word);assert gap==5 and len(word)-gap in (5,6)
   chord=word[refs[1]]-word[refs[0]]
   for k in refs:
    assert cross(chord,word[k]-word[k-1])!=0
    assert cross(chord,word[(k+1)%len(word)]-word[k])!=0
  patches[kn,ln]=dict(word=word,reflex=refs,faces=faces)
  results.append(dict(K_neighbor=kn,L_neighbor=ln,outer_sides=len(word),reflex_indices=refs,corner_points=[[str(word[i].real()),str(word[i].imag())] for i in refs]))
print(json.dumps(results,indent=2))
