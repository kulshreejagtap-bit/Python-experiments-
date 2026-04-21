start = int(input())
stop = int(input())
f= False
for num in range(start, stop + 1):
	if num > 1:
		is_prime = True
		for i in range(2, int(num ** 0.5) + 1):
			if num % i == 0:
				is_prime = False
				break
		if is_prime:
			print(num)
			f = True
if not f:
	print("No primes")
