x = input()
count = 0
for ch in x:
	if ch in "aeiouAEIOU":
		count += 1
print(count)
