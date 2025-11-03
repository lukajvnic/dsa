#include <iostream>
#include <vector>

using namespace std;


/*
Binary Search:
finding an element in an array by eliminating half the array each time.
the array must be sorted.
*/

// takes array and target, returns index of target
int bsearch(const vector<int>& arr, int target, int left, int right) {
	if (right < left)
		return -1;

	int mid = (left + right) / 2;
	if (target == arr[mid])
		return mid;
	else if (target < arr[mid])
		return bsearch(arr, target, left, mid - 1);
	else if (target > arr[mid])
		return bsearch(arr, target, mid + 1, right);

	return -1;
}


int main() {

	vector<int> test_array = {1, 2, 3, 5, 6, 7, 8, 9, 10};
	cout << bsearch(test_array, 9, 0, 9 - 1) << endl;

	return 0;
}
