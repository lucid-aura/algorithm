#include <string>
#include <vector>
#include <iostream>
#include <map>

using namespace std;

int solution(vector<vector<string>> clothes) {
    //cout << clothes.size();
    map<string, vector<string> > m;
    int answer = 1;
    for (int i=0; i<clothes.size(); i++){ //맵에 옷 넣기
        string key = clothes[i][1];
        m[key].push_back(clothes[i][0]);
    }
    //cout << m["headgear"][0] << ' ' <<m["headgear"][1];
    for(auto it = m.begin(); it != m.end(); it++){
		answer *= (it->second.size()+1);
	}
    answer--;
    return answer;
}

int main()
{
	ios::sync_with_stdio(false);
	vector<vector<string>> clothes = {{"yellow_hat", "headgear"}, {"blue_sunglasses", "eyewear"}, {"green_turban", "headgear"}};
    solution(clothes);
	return 0;
}