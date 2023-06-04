#include <iostream>
#include <vector>
using namespace std;

void nullifyCol(vector<vector<int> > matrix, int col) {
    for (int i = 0; i < matrix[0].size(); i++) {
        matrix[i][col] = 0;
    }
}

void nullifyRow(vector<vector<int> > matrix, int row) {
    for (int j = 0; j < matrix[0].size(); j++) {
        matrix[row][j] = 0;
    }
}

void setZeros(vector<vector<int> > matrix) {
    vector<bool> row = vector<bool>(matrix.size());
    vector<bool> col = vector<bool>(matrix[0].size());
    for (int i = 0; i < matrix.size(); i++) {
        for (int j = 0; j < matrix[0].size(); j++) {
            if (matrix[i][j] == 0) {
                row[i] = true;
                col[j] = true;
            }
        }
    }

    for (int i = 0; i < row.size(); i++) {
        if (row[i]) nullifyRow(matrix, i);
    }

    for (int j = 0; j < col.size(); j++) {
        if (col[j]) nullifyCol(matrix, j);
    }
}

int main() {
    vector<vector<int> > vec{ { 0, 2, 3 }, { 4, 5, 6 }, { 7, 8, 9 } };
    setZeros(vec);
    return 0;
}