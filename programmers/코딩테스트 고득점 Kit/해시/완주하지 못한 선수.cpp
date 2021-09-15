#include <string>
#include <vector>
#include <iostream>
#include <algorithm>

using namespace std;

string solution(vector<string> participant, vector<string> completion) {
    sort(participant.begin(), participant.end());
    sort(completion.begin(), completion.end());
    string answer = "";
    for (int i=0; i<completion.size(); i++){
        if (participant[i] != completion[i]){
            answer = participant[i];
            break;
        }
    }
    if (answer.size() == 0) {
        answer = participant[participant.size()-1];
    }
    
    cout <<answer;
    return  answer;
}

int main()
{
	ios::sync_with_stdio(false);
	vector<string> participant = {"leo", "kiki", "eden"};
    vector<string> completion = {"eden", "kiki"};
    solution(participant, completion);
	return 0;
}

/*
participant	completion	return
[leo, kiki, eden]	[eden, kiki]	leo
[marina, josipa, nikola, vinko, filipa]	[josipa, filipa, marina, nikola]	vinko
[mislav, stanko, mislav, ana]	[stanko, ana, mislav]	mislav
*/