// generator.cpp : 이 파일에는 'main' 함수가 포함됩니다. 거기서 프로그램 실행이 시작되고 종료됩니다.
//

#include <iostream>

using namespace std;

int d(int n) {
    char c[256] = { 0, };
    int answer = n;
    _itoa_s(n, c, 10);
    for (int i = 0; i < strlen(c); i++) {
        answer = answer +  int(c[i]) - '0';
    }
    return answer;
}

int main()
{
    int answer = 0;
    int arr[5001] = { 0, };
    for (int i = 1; i < 5001; i++) {
        int gen = d(i);
        if (gen <= 5000) {
            arr[gen] = 1;
        }
    }
    for (int i = 1; i < 5001; i++) {
        if (arr[i] == 0) {
            answer += i;
        }
    }
    cout << answer << endl;;
}

/*
어떤 자연수 n이 있을 때, d(n)을 n의 각 자릿수 숫자들과 n 자신을 더한 숫자라고 정의하자.
예를 들어 d(91) = 9 + 1 + 91 = 101
이 때, n을 d(n)의 제네레이터(generator)라고 한다. 위의 예에서 91은 101의 제네레이터이다.
어떤 숫자들은 하나 이상의 제네레이터를 가지고 있는데, 101의 제네레이터는 91 뿐 아니라 100도 있다.
그런데 반대로, 제네레이터가 없는 숫자들도 있으며, 이런 숫자를 인도의 수학자 Kaprekar가

셀프 넘버(self-number)라 이름 붙였다.
예를 들어 1,3,5,7,9,20,31 은 셀프 넘버 들이다.
1 이상이고 5000 보다 작은 모든 셀프 넘버들의 합을 구하라.
*/