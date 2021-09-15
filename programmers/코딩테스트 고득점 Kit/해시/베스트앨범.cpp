#include <string>
#include <vector>
#include <iostream>
#include <map>
#include <algorithm>

using namespace std;

bool cmp(const pair<string, int> &a, const pair<string, int> &b)
{
    if (a.second == b.second) return a.first > b.first;
    return a.second > b.second;
}

vector<int> solution(vector<string> genres, vector<int> plays) {
    vector<int> answer;
    map<string, int> temp;
    map<string, vector<pair<int, int>> > m; // 키를 장르로. <plays, index>
    for (int i=0; i<genres.size(); i++){ //맵에 값 넣기
        string key = genres[i];
        pair<int, int> value = make_pair(plays[i], i);
        m[key].push_back(value);
        temp[key] += plays[i];
    }


    for(auto it = m.begin(); it != m.end(); it++){
        sort(it->second.begin(), it->second.end(), greater<>());

        
        for(auto it2 = it->second.begin(); it2 != it->second.end(); it2++){
		    cout << it2->first << ' ' << it2->second << '\n';
	    }
        cout << '\n';
        sort(it->second.begin(), it->second.end(), greater<>());
        for(auto it2 = it->second.begin(); it2 != it->second.end(); it2++){
		    cout << it2->first << ' ' << it2->second << '\n';
	    }
        
		//cout << it->second[1].first << ' ';
	}



    vector<pair<string, int>> vec( temp.begin(), temp.end() );
    // 장르, 총합
    /*
    for(auto it = vec.begin(); it != vec.end(); it++){
		cout << it->first << ' ' << it->second << ' ';
	}
    cout << '\n';
    */
    sort(vec.begin(), vec.end(), cmp);
    for(auto it = vec.begin(); it != vec.end(); it++){
        
        if (m[it->first].size() > 1){
            if (m[it->first][0].first == m[it->first][1].first && m[it->first][0].second > m[it->first][1].second){
                answer.push_back(m[it->first][1].second);
                answer.push_back(m[it->first][0].second);
            }
            else{
                answer.push_back(m[it->first][0].second);
                answer.push_back(m[it->first][1].second);
            } 
        }
        else{
            answer.push_back(m[it->first][0].second);
        }
        
		//cout << it->first << ' ' << it->second << ' ';
	}
    for (int i=0; i<answer.size(); i++){
        cout << answer[i] << ' ';
    }
    return answer;
}

int main()
{
	ios::sync_with_stdio(false);
	vector<string> genres = {"classic", "pop", "classic", "classic", "pop"};
    vector<int> plays = {500, 600, 150, 800, 2500};
    genres = {"a","b","c","a"};
    plays = {400,200,300,400};
    solution(genres, plays);
	return 0;
}