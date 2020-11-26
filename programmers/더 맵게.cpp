#include <string>
#include <vector>
#include <iostream>
#include <algorithm>

using namespace std;


vector<int> insert(vector<int> heap, int value){
    heap.push_back(value);
    int idx = heap.size()-1;
    while(idx > 1){
        if (heap[idx] < heap[idx/2]){
            int temp = heap[idx];
            heap[idx] = heap[idx/2];
            heap[idx/2] = temp;
        }
        idx /= 2;
    }
    return heap;
}

vector<int> pop(vector<int> heap){
    int size = heap.size()-1;
    int result = heap[1];
    heap[1] = heap[heap.size()-1];
    heap.pop_back();

    int idx = 1;
    int left = idx*2;
    int right = idx*2+1;
    while(idx < size){
        if (left > size) {
            //자식 불가(단말 노드)
            return heap;
        }
        else if (left == size){
            //왼쪽만 있음.
            if (heap[idx] > heap[left]){
                int temp = heap[idx];
                heap[idx] = heap[left];
                heap[left] = temp;
            }
            return heap;
        }
        else {
            //왼쪽 오른쪽 자식 전부 있음.
            int child = (heap[left] > heap[right] ? right : left);
            if (heap[idx] > heap[child]){
                int temp = heap[idx];
                heap[idx] = heap[child];
                heap[child] = temp;
            }
            else {
                return heap;
            }
        }
        idx *= 2;
        left = idx*2;
        right = idx*2+1;
    }
    return heap;
}
int solution(vector<int> scoville, int K) {
    vector<int> heap;
    heap.push_back(-1);
    int answer = 0;
    //sort(scoville.begin(), scoville.end());
    for (int i=0; i< scoville.size(); i++){
        heap = insert(heap, scoville[i]);
    }

    /*
    for (int j=1; j<heap.size(); j++){
        cout << heap[j] << ' ';
    }
    cout << '\n';
    */

    int del1 = heap[1];
    while (del1 < K){

        heap = pop(heap);

        int del2 = heap[1];
        if (heap.size() < 2) {answer = -1; break;}
        heap = pop(heap);

        heap = insert(heap, del1+del2*2);
        del1 = heap[1];

        answer++;
    }
    
    /*
    for (int j=1; j<heap.size(); j++){
        cout << heap[j] << ' ';
    }
    cout << '\n';
    */
    
    cout << answer;
    
    return answer;
    
}

int main()
{
	ios::sync_with_stdio(false);
	vector<int> scoville = {1, 2, 3, 9, 10, 12};
    int K = 1000000000;
    scoville = {100000,100001,100002};
    solution(scoville, K);
	return 0;
}