#include <iostream>
#include <string>
#include <vector>

using namespace std;

int T, N;

vector<int> solution(vector<int> progresses, vector<int> speeds) {
    vector<int> answer;
    int length = progresses.size();
    int now = 0;
    int cnt = 0;
    while(now < length){
        for (int i=now; i<length; i++){
            progresses[i] += speeds[i];
        }
        while(progresses[now] >= 100){
            now++;
            cnt++;
            if (now == length){ //끝
                break;
            }
        }

        if (cnt > 0){
            answer.push_back(cnt);
            cnt = 0;
        }
    }
    return answer;
}

int main()
{
	ios::sync_with_stdio(false);
	vector<int> progresses = {95, 90, 99, 99, 80, 99};
    vector<int> speeds = {1, 1, 1, 1, 1, 1};
    solution(progresses, speeds);
	return 0;
}

/*
[93, 30, 55]	[1, 30, 5]	[2, 1]
[95, 90, 99, 99, 80, 99]	[1, 1, 1, 1, 1, 1]	[1, 3, 2]
*/