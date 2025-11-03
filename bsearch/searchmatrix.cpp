#include <iostream>
#include <vector>

using namespace std;


int max(int a, int b) {
    return (a > b) ? a : b;
}

int find_row(vector<int> leads, int target, int left, int right) {
    if (right < left)
        return -1;

    int mid = (left + right) / 2;
    if (target == leads[mid])
        return mid;

    int index = (target < leads[mid]) ?
                find_row(leads, target, left, mid - 1) :
                find_row(leads, target, mid + 1, right);
    
    return index == -1 ? mid - 1 : index;
}

bool find_val(vector<int> row, int target, int left, int right) {
    if (right < left)
        return false;

    int mid = (left + right) / 2;
    if (target == row[mid])
        return true;
    return (target < row[mid]) ?
           find_val(row, target, left, mid - 1) :
           find_val (row, target, mid + 1, right);
}

bool searchMatrix(vector<vector<int>>& matrix, int target) {
    
    vector<int> leads = {};
    int row;

    for (int i = 0; i < matrix.size(); i++) {
        leads.push_back(matrix[i][0]);
    }

    if (target < leads[0])
        return false;
    if (target > leads[matrix.size() - 1])
        row = matrix.size() - 1;
    else
        row = find_row(leads, target, 0, matrix.size() - 1);

    return find_val(matrix[row], target, 0, matrix[0].size() - 1);
}

int main() {
    cout << "hello" << endl;

    vector<vector<int>> matrix = {{1,3,5,7},{10,11,16,20},{23,30,34,50}};
    cout << searchMatrix(matrix, 30) << endl;

    return 0;
}

