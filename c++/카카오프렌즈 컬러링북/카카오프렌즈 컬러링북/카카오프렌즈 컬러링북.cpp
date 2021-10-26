// 카카오프렌즈 컬러링북.cpp : 이 파일에는 'main' 함수가 포함됩니다. 거기서 프로그램 실행이 시작되고 종료됩니다.
//

#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

void print(vector<vector<int>> picture, int m, int n) {
    for (int i = 0; i < m; i++) {
        for (int j = 0; j < n; j++) {
            cout << picture[i][j] << " ";
        }
        cout << endl;
    }
    cout << "############################" << endl;
}
int DFS(vector<vector<int>> &picture, int n, int m,  int i, int j, int color, int &area) {
    if (picture[i][j] != color) {
        return 0;
    }
    area++;
    picture[i][j] = 0;
    if (i-1 > 0) {
        DFS(picture, n, m, i - 1, j, color, area);
    }
    if (i+1 < m) {
        DFS(picture, n, m, i + 1, j, color, area);
    }
    if (j-1 > 0) {
        DFS(picture, n, m, i , j - 1, color, area);
    }
    if (j+1 < n) {
        DFS(picture, n, m, i, j + 1, color, area);
    }
    return 0;
}
vector<int> solution(int m, int n, vector<vector<int>> picture) {
    int number_of_area = 0;
    int max_size_of_one_area = 0;

    int area = 0;
    for (int i = 0; i < m; i++) {
        for (int j = 0; j < n; j++) {
            if (picture[i][j] > 0) {
                DFS(picture, n, m, i, j, picture[i][j], area);
                number_of_area++;
                if (area > max_size_of_one_area) {
                    max_size_of_one_area = area;
                }
                area = 0;            }
        }
    }
    vector<int> answer(2);
    answer[0] = number_of_area;
    answer[1] = max_size_of_one_area;
    return answer;
}

int main()
{
    std::cout << "Hello World!\n";
    vector<vector<int>> picture = { {1,1,1,0},{1,2,2,0},{1,0,0,1},{0,0,0,1},{0,0,0,3},{0,0,0,3} };
    int m = 6;
    int n = 4;

    m = 13;
    n = 16;
    picture = { {0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 0, 0, 0}, {0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0}, {0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0}, {0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0}, {0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0}, {0, 1, 1, 1, 1, 2, 1, 1, 1, 1, 2, 1, 1, 1, 1, 0}, {0, 1, 1, 1, 2, 1, 2, 1, 1, 2, 1, 2, 1, 1, 1, 0}, {0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0}, {0, 1, 3, 3, 3, 1, 1, 1, 1, 1, 1, 3, 3, 3, 1, 0}, {0, 1, 1, 1, 1, 1, 2, 1, 1, 2, 1, 1, 1, 1, 1, 0}, {0, 0, 1, 1, 1, 1, 1, 2, 2, 1, 1, 1, 1, 1, 0, 0}, {0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0}, {0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0} };
    vector<int> answer(2);
    answer = solution(m, n, picture);
    cout << answer[0] << " " << answer[1] << endl;
}
