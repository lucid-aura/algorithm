// 단어변환.cpp : 이 파일에는 'main' 함수가 포함됩니다. 거기서 프로그램 실행이 시작되고 종료됩니다.
//

// temp.cpp : 이 파일에는 'main' 함수가 포함됩니다. 거기서 프로그램 실행이 시작되고 종료됩니다.
//

#include <iostream>
#include <vector>
#include <string>
#include <algorithm>

using namespace std;

int diff_value(string a, string b) {
    int count = 0;
    for (unsigned int i = 0; i < a.size(); i++) {
        if (a.at(i) != b.at(i)) count++;
    }
    return count;
}

int DFS(vector<string>& words, string begin, string& target, int count, int& min, vector<string> already) {
    already.push_back(begin); // 새로받은 시작할 노드 들린 노드에 추가
    count++; // 바꾼 횟수도 추가
    if (begin == target) { // 올바른 단어를 완성했으면
        if (min > count) { // 최소값이 변경되었으면
            min = count;
        }
        return 1;
    }

    vector<string> candidate = {}; // 후보벡터
    vector<string> before = already; // 이전 벡터 보존용

    for (unsigned int i = 0; i < words.size(); i++) { // 후보노드 찾기
        if (diff_value(words.at(i), begin) == 1) {
            auto idx = find(already.begin(), already.end(), words.at(i));
            if (idx == already.end()) { // 이미 들린 노드 아니면
                candidate.push_back(words.at(i)); // 후보에 추가
            }
        }
    }

    if (candidate.size() == 0) { // 후보가 없으면 (문자 하나만 다른 단어들)
        return -1; //불가능 표시
    }
    for (unsigned int i = 0; i < candidate.size(); i++) { // 추가한 후보들 중에서
        DFS(words, candidate.at(i), target, count, min, already); // 반복 진행
    }
    return 0;
}
int solution(string begin, string target, vector<string> words) {
    int answer = words.size() + 1;
    int count = -1;
    vector<string> candidate = {};
    vector<string> already = {};
    for (unsigned int i = 0; i < words.size(); i++) {
        if (diff_value(words.at(i), begin) == 1) {
            candidate.push_back(words.at(i));
        }
    }
    for (unsigned int i = 0; i < candidate.size(); i++) {
        DFS(words, begin, target, count, answer, already);
        already = {};
    }
    return answer;
}

int main()
{
    string begin = "hit";
    string target = "cog";
    vector<string> words = { "hot", "dot", "dog", "lot", "log", "cog" };
}

// 시작을 위한 팁: 
//   1. [솔루션 탐색기] 창을 사용하여 파일을 추가/관리합니다.
//   2. [팀 탐색기] 창을 사용하여 소스 제어에 연결합니다.
//   3. [출력] 창을 사용하여 빌드 출력 및 기타 메시지를 확인합니다.
//   4. [오류 목록] 창을 사용하여 오류를 봅니다.
//   5. [프로젝트] > [새 항목 추가]로 이동하여 새 코드 파일을 만들거나, [프로젝트] > [기존 항목 추가]로 이동하여 기존 코드 파일을 프로젝트에 추가합니다.
//   6. 나중에 이 프로젝트를 다시 열려면 [파일] > [열기] > [프로젝트]로 이동하고 .sln 파일을 선택합니다.
// 프로그램 실행: <Ctrl+F5> 또는 [디버그] > [디버깅하지 않고 시작] 메뉴
// 프로그램 디버그: <F5> 키 또는 [디버그] > [디버깅 시작] 메뉴

