def is_cyclic_rotation(a,b):

	return (b*2).find(a) != -1 and len(a) == len(b)



print "Yes" if is_cyclic_rotation(raw_input("Enter the first word : "),raw_input("Enter the second word : ")) else "No"

