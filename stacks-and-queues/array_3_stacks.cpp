#include <vector>
using namespace std;

class FixedMultistack {
    private:
        int numStacks = 3;
        int stackCapacity;
        vector<int> values;
        vector<int> sizes;

        int indexOfTop(int stackNum) {
            int offset = stackNum * stackCapacity;
            int size = sizes[stackNum];
            return offset + size - 1;
        }

    public:
        FixedMultistack(int stackSize) {
            stackCapacity = stackSize;
            values = vector<int>(stackSize * numStacks);
            sizes = vector<int>(numStacks);
        }

        bool isFull(int stackNum) {
            return sizes[stackNum] == stackCapacity;
        }

        bool isEmpty(int stackNum) {
            return sizes[stackNum] == 0;
        }

        void push(int stackNum, int value) {
            // Check that we have space for the next element
            if (isFull(stackNum)) {
                throw invalid_argument("Stack is full");
            }
            sizes[stackNum]++;
            values[indexOfTop(stackNum)] = value;
        }

        int pop(int stackNum) {
            if (isEmpty(stackNum)) {
                throw invalid_argument("Empty Stack Exception");
            }
            int topIndex = indexOfTop(stackNum);
            int value = values[topIndex];
            values[topIndex] = 0;
            sizes[stackNum]--;
            return value;
        }

        int peek(int stackNum) {
            if (isEmpty(stackNum)) {
                throw invalid_argument("Empty Stack Exception");
            }
            return values[indexOfTop(stackNum)];
        }
};


class MultiStack {
    // StackInfo is a simple class that holds a set of data about each stack. It does not hold
    // the actual items int he stack. We could have done with just a bunch of individual variables, but that's messy
    // and won't gain us much

    private:
        class StackInfo {
            public:
                int start, size, capacity;

                StackInfo(int start, int capacity) {
                    start = start;
                    capacity = capacity;
                }

                bool isWithinStackCapacity(int index, vector<int> values) {
                    if (index < 0 || index >= values.size()) {
                        return false;
                    }
                    int contiguousIndex = index < start ? index + values.size() : index;
                    int end = start + capacity;
                    return start <= contiguousIndex && contiguousIndex < end;
                }

                int lastCapacityIndex(){
                    return 1;
                }
        };

        vector<StackInfo> info;
        vector<int> values;
}