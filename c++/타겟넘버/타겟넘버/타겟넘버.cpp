#include <string>
#include <vector>
#include <iostream>
using namespace std;

int recursion(vector<int>* numbers, int index, int value, int target, int* ptr) {
    if (numbers->size()-1 == index) {
        if ((value + numbers->at(index) == target) || (value - numbers->at(index) == target)) {
            *ptr += 1;
        }
        return 0;
    }
    value += numbers->at(index);
    recursion(numbers, index+1, value, target, ptr);
    value -= numbers->at(index);
    value -= numbers->at(index);
    recursion(numbers, index+1, value, target, ptr);
    return 0;
}
int solution(vector<int> numbers, int target) {
    int length = numbers.size();
    int answer = 0;
    return length;
}

int main() {
    vector<int> numbers = { 1, 1, 1, 1, 1 };
    int target = 3;
    int answer = 0;
    int* ptr = &answer;
    recursion(&numbers, 0, 0, 3, ptr);
    cout << answer << endl;

}

/*

numbers 	target	return
[1, 1, 1, 1, 1]	 3	             5

-1+1+1+1+1 = 3
+1-1+1+1+1 = 3
+1+1-1+1+1 = 3
+1+1+1-1+1 = 3
+1+1+1+1-1 = 3

*/