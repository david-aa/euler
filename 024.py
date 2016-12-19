
def get_permutations (arr):
	if len(arr) < 2:
		return [[arr]]
	elif len(arr) == 2:
		return [[arr[0], arr[1]], [arr[1], arr[0]]]
	else:
		permuts = []
		for a in arr:
			arr2 = arr[:]
			arr2.remove(a)
			for p in get_permutations(arr2):
				p.insert(0, a)
				permuts.append(p)
		return permuts

res = get_permutations([0, 1, 2, 3, 4, 5, 6, 7, 8, 9])
print res[999999]
