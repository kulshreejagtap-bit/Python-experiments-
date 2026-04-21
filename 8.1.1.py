n = int(input("dimension: "))
print("first matrix:")
first = []
for i in range(n):
	row = list(map(int, input().split()))
	first.append(row)
print("second matrix:")
second = []
for i in range(n):
	row = list(map(int, input().split()))
	second.append(row)
result = []
for i in range(n):
	result.append([0] * n)
for i in range(n):
	for j in range(n):
		for k in range(n):
			result[i][j] += first[i][k] * second[k][j]
print("Resultant Matrix:")
for row in result:
	print(*row)
