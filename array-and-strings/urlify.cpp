#include <iostream>
using namespace std;

int countOfChar(char str[], int start, int end, int target) {
    int count = 0;
    for (int i = start; i < end; i++) {
        if (str[i] == target) {
            count++;
        }
    }
    return count;
}

void replaceSpaces(char str[], int trueLength) {
    int numSpaces = countOfChar(str, 0, trueLength, ' ');
    int newIndex = trueLength - 1 + numSpaces * 2;
    int len = *(&str + 1) - str;
    if (newIndex + 1 < len) str[newIndex + 1] = '\0';

    for (int oldIndex = trueLength - 1; oldIndex >= 0; oldIndex--) {
        if (str[oldIndex] == ' ') {
            str[newIndex] = '0';
            str[newIndex - 1] = '2';
            str[newIndex - 2] = '%';
            newIndex -= 3;
        } else {
            str[newIndex] = str[oldIndex];
            newIndex -= 1;
        }
    }

}

int main() {
    char input[] = "Mr John Smith    ";
    replaceSpaces(input, 13);
    cout << input << endl;
    return 0;
}