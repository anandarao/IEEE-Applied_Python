def get_primes(n):
	check = []
	for i in range(0,n+1):
		check.append(1)
	for i in range(2,n+1):
		if check[i] == 1:
			j = 2*i
			while j <= n :
				check[j] = 0
				j += i
	primes = []
	for i in range(2,n+1):
		if check[i] == 1:
			primes.append(i)
	return primes
	
n = int(raw_input("Enter the value of n : "))
for i in get_primes(n):
	print i,