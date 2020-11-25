#include <string>
#include <vector>
#include <iostream>

using namespace std;

int solution(vector<int> priorities, int location) {
    vector<int> doc_num;
    int answer = 0;
    int cnt = 0;
    for (int i=0; i<priorities.size(); i++){
        doc_num.push_back(i);
    }
    int length = priorities.size();
    bool most=true;
    while(priorities.size()){
        for (int i=1; i<length; i++){
            if (priorities[0] < priorities[i]){ // 더 중요한게 있다.
                most = false;
                break;
            }
        }
        if (most){ // 인쇄한다.
            cnt++;
            if (doc_num[0] == location){
                answer = cnt;
                break;
            }
            else{
                length = priorities.size();
                priorities.erase(priorities.begin());
                doc_num.erase(doc_num.begin());
            }
        }
        else {
            priorities.push_back(priorities[0]);
            doc_num.push_back(doc_num[0]);
            priorities.erase(priorities.begin());
            doc_num.erase(doc_num.begin());
            most = true;
        }
    }
    cout << answer;
    return answer;
}

int main()
{
	ios::sync_with_stdio(false);
	vector<int> priorities = {1,1,9,1,1,1};
    int location = 0;
    solution(priorities, location);
	return 0;
}

/*
priorities	location	return
[2, 1, 3, 2]	2	1
[1, 1, 9, 1, 1, 1]	0	5
*/