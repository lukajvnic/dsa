from random import randint


def pivot(arr, low, high):
	i = low - 1
	for j in range(low, high):
		if arr[j] < arr[high]:
			i += 1
			if arr[j] < arr[i]:
				arr[j], arr[i] = arr[i], arr[j]
	i += 1
	arr[high], arr[i] = arr[i], arr[high]
	return i


def quicksort(arr, low, high):
	if low < high:
		p = pivot(arr, low, high)
		quicksort(arr, low, p - 1)
		quicksort(arr, p + 1, high)
	return arr


l = [randint(0,1000) for _ in range(100)]
print(quicksort(l, 0, len(l) - 1))

