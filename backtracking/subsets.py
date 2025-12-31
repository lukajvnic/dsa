
oset = [1,2,3]
powerset = [[]]


def backtrack(subset, i):
	if i == len(oset):
		return
	powerset.append(subset + [oset[i]])
	backtrack(subset + [oset[i]], i + 1)
	backtrack(subset, i + 1)

backtrack([], 0)
print(powerset)


