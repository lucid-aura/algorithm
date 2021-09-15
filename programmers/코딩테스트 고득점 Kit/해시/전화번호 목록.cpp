#include <string>
#include <vector>
#include <iostream>
#include <algorithm>

using namespace std;

bool comp(string s1, string s2){
	return s1 > s2;	//string 사전 역순 
}

bool solution(vector<string> phone_book) {
    sort(phone_book.begin(), phone_book.end());
    bool answer = true;
    for (int i=0; i<phone_book.size()-1; i++){
        for (int j=i+1; j<phone_book.size(); j++){
            if (phone_book[i].size() < phone_book[j].size())
                if (phone_book[j].find(phone_book[i]) != string::npos){
                    cout << phone_book[i] << ' ' << phone_book[j] << '\n';
                    answer = false;
                    return answer;
                }
        }
    }

    cout << answer;
    return answer;
}

int main()
{
	ios::sync_with_stdio(false);
    vector<string> phone_book = {"12", "88","123","567","1235"};
    //phone_book = {"123", "456", "789"};
    solution(phone_book);
	return 0;
}