def num_of_sublists(lst):
	return sum(isinstance(i, list) for i in lst)
print(num_of_sublists([[1, 2, 3], [1, 2, 3], [1, 2, 3]]))