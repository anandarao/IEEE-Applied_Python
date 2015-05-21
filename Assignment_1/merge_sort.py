def merge_sort(arr,low,high):
	if(low<high):
		mid = (low + high)/2
		merge_sort(arr,low,mid)
		merge_sort(arr,mid+1,high)
		merge(arr,low,mid,high)
	return

def merge(arr,low,mid,high):
	c = []
	i = low
	k = 0
	j = mid + 1
	while i <= mid and j <= high :
		if a[i] < a[j]:
			c.append(a[i])
			k +=1
			i +=1
		else:
			c.append(a[j])
			k +=1
			j +=1
	while i <= mid:
		c.append(a[i])
		k += 1
		i += 1
	while j <= high:
		c.append(a[j])
		k += 1
		j += 1
	for i in range(0,k):
		a[i+low] = c[i]
		
list = raw_input("Enter the array elements : ").split()
a = []
for i in list:
	a.append(int(i))
merge_sort(a,0,len(a)-1)
print "Sorted Array : ",
for i in a:
	print "%d " % i,
