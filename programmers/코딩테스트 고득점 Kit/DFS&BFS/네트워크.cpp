#include <string>
#include <vector>
#include <iostream>
#include <algorithm>

using namespace std;

vector<int> DFS(vector<vector<int>>& computers, vector<int>& network, int source) {
    network.push_back(source); // 방문한 노드 추가
    for (unsigned int i = 0; i < computers.at(source).size(); i++) { // 해당 노드의 엣지들 확인
        if (computers.at(source).at(i) == 1) { // 다른 노드와 연결되어 있다면
            auto idx = find(network.begin(), network.end(), i); // 이미 들린 노드인지 확인해보자.
            if (idx == network.end()) { // 아직 순회 안한 노드이면
                DFS(computers, network, i); // 해당 노드로 이동하여 반복.
            }
        }
    }
    return network;
}

int solution(int n, vector<vector<int>> computers) {
    vector<int> network = {};
    vector<int> check = {};
    int answer = 1;
    for (unsigned int i = 0; i < computers.size(); i++) {
        int before = check.size();
        if (check.size() != 0) { // 돌아본 구간이 존재한다면
            auto idx = find(check.begin(), check.end(), i);
            if (idx == check.end()) { // 만약 돌아본 구간이 미 개척지라면
                DFS(computers, network, i); // 순회공연 진행
                for (unsigned int j = 0; j < network.size(); j++) {
                    check.push_back(network.at(j)); // 돌아본 구간으로 추가
                }
            }
        }
        else { // 존재하지 않는다면 (첫 실행)
            DFS(computers, network, i); // 순회공연 진행
            for (unsigned int j = 0; j < network.size(); j++) {
                check.push_back(network.at(j)); // 돌아본 구간으로 추가
            }
        }
        if (check.size() == computers.size()) { // 전 노드를 탐색했다면
            return answer; // 돌기 끝낸다.
        }
        else if (before != check.size()){ // 남은 노드가 있다면
            answer += 1;
        }
        network = {}; // 한번 순회 경로 초기화
    }
    return answer;
}

int main()
{
    int n = 3;
    vector<vector<int>> computers = { {1, 1, 0}, {1, 1, 0}, {0, 0, 1} };
    cout << solution(n, computers) << endl;
}

// 프로그램 실행: <Ctrl+F5> 또는 [디버그] > [디버깅하지 않고 시작] 메뉴
// 프로그램 디버그: <F5> 키 또는 [디버그] > [디버깅 시작] 메뉴

// 시작을 위한 팁: 
//   1. [솔루션 탐색기] 창을 사용하여 파일을 추가/관리합니다.
//   2. [팀 탐색기] 창을 사용하여 소스 제어에 연결합니다.
//   3. [출력] 창을 사용하여 빌드 출력 및 기타 메시지를 확인합니다.
//   4. [오류 목록] 창을 사용하여 오류를 봅니다.
//   5. [프로젝트] > [새 항목 추가]로 이동하여 새 코드 파일을 만들거나, [프로젝트] > [기존 항목 추가]로 이동하여 기존 코드 파일을 프로젝트에 추가합니다.
//   6. 나중에 이 프로젝트를 다시 열려면 [파일] > [열기] > [프로젝트]로 이동하고 .sln 파일을 선택합니다.
