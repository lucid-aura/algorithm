// 단체사진.cpp : 이 파일에는 'main' 함수가 포함됩니다. 거기서 프로그램 실행이 시작되고 종료됩니다.
//

#include <iostream>
#include <string>
#include <vector>
#include <algorithm>

using namespace std;

bool except(string line, vector<string> data) {
    for (int i = 0; i < data.size(); i++) {
        char a = data[i][0];
        char b = data[i][2];
        char exp = data[i][3];
        char c = data[i][4];
        int idx_a = line.find(a);
        int idx_b = line.find(b);
        if (idx_a != string::npos && idx_b != string::npos) {
            int int_a = a - '0';
            int int_b = b - '0';
            int int_c = c - '0';
            if (exp == '<') {
                if (abs(idx_a - idx_b) >= int_c + 1) {
                    return true;
                }
            }
            else if (exp == '>') {
                if (abs(idx_a - idx_b) <= int_c + 1) {
                    return true;
                }
            }
            else {
                if (abs(idx_a - idx_b) != 1) {
                    return true;
                }
            }
        }
        //cout << a << " " << b << " " << exp << " " << c << endl;
    }
    return false;
}
int DFS(vector<char>& name, string line, vector<string> &lines, vector<string> &data) {
    if (line.size() == 8 && (find(lines.begin(), lines.end(), line) == lines.end())) {
        lines.push_back(line);
        //cout << line << endl;
        return 0;
    }
    //cout << line << endl;
    for (int i = 0; i < 8; i++) {
        int idx = line.find(name[i]);
        
        if (idx == string::npos) {
            string new_line = line + name[i];
            if (!except(new_line, data)) {
                DFS(name, new_line, lines, data);
            }
        }
    }
    return 0;
}

int solution(int n, vector<string> data) {
    vector<string> friends = { "A", "C", "F" , "J", "M", "N" , "R", "T"};
    vector<char> name = { 'A','C','F','J','M','N','R','T' };
    //string test = "ACFJMNRTSP";
    string line = "";
    vector<string> lines;
    for (int i = 0; i < 8; i++) {
        line = friends[i];
        DFS(name, line, lines, data);
    }
    cout << lines.size() << endl;
    

    int answer = 0;
    return answer;
}

int main()
{
    vector<string> data = { "N~F=0", "R~T>2" };
    int n = 2;
    // 3048
    solution(n, data);
    //except("a", data);
}