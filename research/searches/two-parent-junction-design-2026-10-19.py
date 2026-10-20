"""Exact arithmetic only; the report supplies the planar proofs."""
for name,p,F,total,B,J in [("P",5,9,49,2,1),("Q",7,8,46,1,1)]:
    I=2*F-2-B-J
    E=I+F-1
    assert 2*E==3*I+B+J
    assert 6*F-total==6-p+B+2*J
    assert total-2*F==2*I+p-2+B
    print(name, dict(F=F,I=I,E=E,active=B+J,total_native=total))
allocations=[(b,j,d,h) for b in range(4) for j in range(2)
             for d in range(2) for h in range(4)
             if b+2*j+2*d+h==3 and b+j>=3]
assert allocations==[(3,0,0,0)]
assert 25-(18-3)==10>3*5-6
print("Unique Q allocation with >=3 active nodes:",allocations)
print("PASS: arithmetic only; topology theorem is analytic")
