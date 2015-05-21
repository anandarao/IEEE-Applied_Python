def insertion_sort(arr):
	n = len(arr)
	for i in range(0,n):
		j = i
		x = arr[i]
		while j>0 and arr[j-1]>x:
			arr[j] = arr[j-1]
			j = j-1
		arr[j] = x
	return arr
	
list = raw_input("Enter the array elements : ").split()
arr = []
for i in list:
	arr.append(int(i))
sorted = insertion_sort(arr)
print "Sorted Array : ",
for i in sorted:
	print "%d " % i,