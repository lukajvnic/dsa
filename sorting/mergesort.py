from random import randint


lst = [randint(0,10000) for _ in range(100)]


def merge(a, b):
	g = len(a) + len(b)
	f = []
	while g != len(f):
		if len(a) == 0:
			return f + b
		if len(b) == 0:
			return f + a
		elif a[0] < b[0]:
			f.append(a[0])
			a.pop(0)
		else:
			f.append(b[0])
			b.pop(0)
	return f


def mergesort(l):
	if len(l) == 1:
		return l
	mid = len(l) // 2
	return merge(mergesort(l[:mid]), mergesort(l[mid:]))


print(mergesort(lst))

