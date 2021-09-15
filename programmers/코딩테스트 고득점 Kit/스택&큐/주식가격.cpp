#include <iostream>
#include <string>
#include <vector>

using namespace std;

int T, N;

vector<int> solution(vector<int> prices) {
    int length = prices.size();
    int pivot = 0;
    vector<int> answer(length, 0);

    vector< vector<int> > test;
    for (int i=1; i<100001; i++){
        vector<int> v(0);
        test.push_back(v);
    }
    for (int i=1; i<length+1; i++){
        test[prices[i-1]].push_back(i);
    }
    for (int i=1; i<length+1; i++){
        for (int j=0; j<test[i].size(); j++){
            cout << test[i][j] << " ";
        }
        cout << '\n';
    }
    /*
    for (int i = 1; i<length; i++){
        if (prices[i] < prices[i-1]){ // 가격이 떨어졌다.
            for (int j=0; j<i; j++){
                answer[j] += i-j-pivot;
            }
            pivot = i;
        }
        else if (i == length-1){
            for (int j=0; j<i; j++){ // 마지막 값이다.
                answer[j] += i-pivot;
            }
        }

    }
    
    for (int i=0; i<length; i++){
        cout << answer[i] << ' ';
    }
    */
    return answer;
}

int main()
{
	ios::sync_with_stdio(false);
	vector<int> v = {1,2,3,2,3};
    solution(v);
	return 0;
}