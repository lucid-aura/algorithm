#include <string>
#include <vector>
#include <iostream>
#include <queue>
#include <algorithm>

using namespace std;

int now = 0;
bool cmp(const vector<int> &a, const vector<int> &b){
    return a[0] < b[0];
}

struct cmpQ{
    bool operator()(vector<int> &a, vector<int> &b){
        return a[1] > b[1];
    }
};

int solution(vector<vector<int>> jobs) {
    int answer = 0;
    int num = jobs.size();
    priority_queue<vector<int>, vector<vector<int>>, cmpQ> jobs_Q;
    sort(jobs.begin(), jobs.end(), cmp);
    now = jobs[0][0]; // 처음 작업 시작 시간 = 가장 먼저 도착한 작업 시간
    while(!(jobs.empty() && jobs_Q.empty())){
        if (!jobs.empty()){ 
            while(jobs[0][0] <= now){ // 현재 시간까지의 모든 작업 큐에 넣음
                jobs_Q.push(jobs[0]);
                jobs.erase(jobs.begin());
                if (jobs.empty()) break; // 마지막 작업이면 break
            }       
            if(jobs_Q.empty()){ //작업이 하나도 안들어갔으면
                now = jobs[0][0]; // 시간 점프
            }
        }
        if (!jobs_Q.empty()){
            now += jobs_Q.top()[1]; // 완료시간 = 현재시간
            answer += (now - jobs_Q.top()[0]); // 완료 - 들어온 시점
            jobs_Q.pop(); // 작업 하나 끝.
        }
    }
    cout << answer/num;
    return 0;
}

int main()
{
	ios::sync_with_stdio(false);
	vector<vector<int>> jobs = {{0,3}, {1,9}, {500,6}};
    //jobs = {{0, 9}, {0, 4}, {0, 5}, {0, 7}, {0, 3}};
    jobs = {{0,3},{4,4},{5,3},{4,1}};
    solution(jobs);
	return 0;
}