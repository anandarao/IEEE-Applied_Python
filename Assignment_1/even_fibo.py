def even_fibo_sum(n):
	if n == 0:
		return -1
	elif n == 1:
		return 0
	else:
		list = [0,1]
		i = 2
		while True:
			num = list[i-1]+list[i-2]
			if num > n:
				break
			i += 1
			list.append(num)
		sum = 0
		for i in list:
			sum += i if i % 2 == 0 else 0
		return sum

print even_fibo_sum(int(raw_input("Enter the value of n : ")))