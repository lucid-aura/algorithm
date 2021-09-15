import heapq

scoville = [1, 2, 3, 9, 10, 12]
K = 7
answer = 0
heapq.heapify(scoville)
print(scoville)
while(scoville[0] < K):
    least = scoville[0] # 첫번째 안매운 거 뽑기.
    heapq.heappop(scoville) 
    less = scoville[0] # 두번째 안매운거 뽑기
    heapq.heappop(scoville)
    mix = least + less*2
    heapq.heappush(scoville, mix)
    answer += 1
    if len(scoville) == 1 and scoville[0] < K:
        answer = -1
        break
    print(scoville)
print(answer)
