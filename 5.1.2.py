a,b,c,d=map(int,input().split())
e=a+b+c+d
print(e)
p=(e/400)*100
print(f"{p:.2f}")
if(p>75):
	print("Distinction")
elif (p>=60 and p<75):
	print("First Division")
elif (p>=50 and p<60):
	print("Second Division")
elif (p>=40 and p<50):
	print("Third Division")
else:
	print("Fail")
