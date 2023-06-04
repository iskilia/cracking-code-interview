#include <iostream>
#include <vector>
using namespace std;

bool rotateMatrix(vector<vector<int> > matrix) {
    if (matrix.size() == 0 || matrix.size() != matrix[0].size()) {
        return false;
    }
    int n = matrix.size();

    for (int layer = 0; layer < n / 2; layer++) {
        int first = layer;
        int last = n - 1 - layer;
        for (int i = first; i < layer; i++) {
            int offset = i - first;
            int top = matrix[first][i];

            // left => top
            matrix[first][i] = matrix[last-offset][first];

            // bottom -> left
            matrix[last-offset][first] = matrix[last][last - offset];

            // right -> bottom
            matrix[last][last - offset] = matrix[i][last];

            // top -> right
            matrix[i][last] = top;
        }
    }
    for (int i = 0; i < matrix.size(); i++) {
        for (int j = 0; j < matrix.size(); j++) {
            cout << matrix[i][j] << endl;
        }
    }
    return true;
}

int main() {
    vector<vector<int> > vec{ { 1, 2, 3 }, { 4, 5, 6 }, { 7, 8, 9 } };
    rotateMatrix(vec);
    return 0;
}