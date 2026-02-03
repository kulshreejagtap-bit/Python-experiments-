# Type Content here...
seta=set(map(int,input("Set A: ").split()))
setb=set(map(int,input("Set B: ").split()))
u=seta | setb
i=seta & setb
d=seta - setb
print(f"Union: {u}")
print(f"Intersection: {i}")
print(f"Difference: {d}")
