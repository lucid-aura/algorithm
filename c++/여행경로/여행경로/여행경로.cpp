// 여행경로.cpp : 이 파일에는 'main' 함수가 포함됩니다. 거기서 프로그램 실행이 시작되고 종료됩니다.
//

#include <iostream>
#include <vector>
#include <algorithm>
#include <string>

using namespace std;

vector<int> find_airline(string target, vector<vector<string>>& tickets) {
    vector<int> possible = {};
    for (unsigned int i = 0; i < tickets.size(); i++) {
        if (tickets.at(i).at(0) == target) { // 현재 지역이 출발지인 노드들 후보의 인덱스 전부 추가
            possible.push_back(i);
        }
    }
    return possible;
}

int DFS(vector<vector<string>> tickets, vector<string> node, int now_idx, string now, vector<int> root_idx, vector<vector<string>> root, vector<vector<string>>& candidates) {
    root.push_back(node); // 도착했으므로 사용한 티켓 추가
    root_idx.push_back(now_idx); // 도착했으므로 사용한 티켓의 인덱스 추가
    now = node.at(1); // 현재 위치 갱신
    if (root.size() == tickets.size()) { // 모든 티켓을 전부 사용했으면
        vector<string> candidate = {}; // 티켓 경로의 후보를 정답 후보에 추가
        candidate.push_back(root.at(0).at(0));
        candidate.push_back(root.at(0).at(1));
        for (unsigned int i = 1; i < root.size(); i++) {
            candidate.push_back(root.at(i).at(1));
        }
        vector<vector<string>>::iterator index = find(candidates.begin(), candidates.end(), candidate); // 해당 후보가 들린곳인지
        if (index == candidates.end()) {
            candidates.push_back(candidate);
        }
        return root.size();
    }

    vector<int> airline = find_airline(now, tickets); // 후보 노드 인덱스 추출
    for (unsigned int i=0; i<airline.size(); i++) { // 후보 노드들에 대해서
        
        vector<int>::iterator index = find(root_idx.begin(), root_idx.end(), airline.at(i)); // 해당 후보가 들린곳인지
        if (index == root_idx.end()) { // 들린 적 없는 공항이면
            node = tickets.at(airline.at(i)); // 다음으로 향할 티켓 설정
            now_idx = airline.at(i); // 다음경로 위치를 현재 경로로 변경
            DFS(tickets, node, now_idx, now, root_idx, root, candidates); // 다음으로 출발
        }
    }
    return 0;
}

vector<string> solution(vector<vector<string>> tickets) {
    vector<string> answer;
    vector<vector<string>> canditates = {};
    vector<vector<string>> root = {};
    vector<int> root_idx = {};
    if (tickets.size() == 1) return tickets.at(0);
    for (unsigned int i = 0; i < tickets.size(); i++) {
        if (tickets.at(i).at(0) == "ICN") {
            DFS(tickets, tickets.at(i), i, "INC", root_idx, root, canditates);
        }
    }
    sort(canditates.begin(), canditates.end(), std::less<vector<string>>());
    
    answer = canditates.at(0);
    return answer;
}

int main()
{
    vector<vector<string>> tickets = { {"ICN", "JFK"},{"HND", "IAD"},{"JFK", "HND"} };
    vector<string> answer = { "ICN", "JFK", "HND", "IAD" };
    tickets = { {"ICN", "SFO"},{"ICN", "ATL"},{"SFO", "ATL"},{"ATL", "ICN"},{"ATL", "SFO"} };
    //tickets = { {"ICN", "AAA"},{"ICN", "AAA"},{"ICN", "AAA"},{"AAA", "ICN"},{"AAA", "ICN"} };
    vector<string> a = solution(tickets);
    for (unsigned int i = 0; i < a.size(); i++) {
        cout << a.at(i) << " ";
    }
}


/*
tickets	                                                                            return
[["ICN", "JFK"], ["HND", "IAD"], ["JFK", "HND"]]	["ICN", "JFK", "HND", "IAD"]
*/
// 프로그램 실행: <Ctrl+F5> 또는 [디버그] > [디버깅하지 않고 시작] 메뉴
// 프로그램 디버그: <F5> 키 또는 [디버그] > [디버깅 시작] 메뉴

// 시작을 위한 팁: 
//   1. [솔루션 탐색기] 창을 사용하여 파일을 추가/관리합니다.
//   2. [팀 탐색기] 창을 사용하여 소스 제어에 연결합니다.
//   3. [출력] 창을 사용하여 빌드 출력 및 기타 메시지를 확인합니다.
//   4. [오류 목록] 창을 사용하여 오류를 봅니다.
//   5. [프로젝트] > [새 항목 추가]로 이동하여 새 코드 파일을 만들거나, [프로젝트] > [기존 항목 추가]로 이동하여 기존 코드 파일을 프로젝트에 추가합니다.
//   6. 나중에 이 프로젝트를 다시 열려면 [파일] > [열기] > [프로젝트]로 이동하고 .sln 파일을 선택합니다.
