################################## 복서 정렬하기 ####################################

def solution(weights, head2head):
    record = [[i+1] for i in range(len(weights))]
    over_win = [0 for i in range(len(weights))]
    win = [0 for i in range(len(weights))]
    lose = [0 for i in range(len(weights))]
    win_rate = [0 for i in range(len(weights))]

    for i in range(len(head2head)):
        for j in range(len(head2head[i])):
            if i != j: # 자기 자신은 항상 N이므로 제외
                if head2head[i][j] == 'W': # i+1 번째 복서가 j+1 복서를 이겼을 경우
                    if weights[i] < weights[j]: # i+1 번째 복서가 j+1번째 복서보다 가벼울 경우
                        over_win[i] += 1
                    win[i] += 1
                elif head2head[i][j] == 'L':
                    lose[i] += 1
        if win[i] != 0: # 적어도 한번이라도 이겼을 경우 (승률 0퍼가 아닐 경우)
            win_rate[i] = win[i]/(win[i] + lose[i]) * 100
        record[i].append(win_rate[i])
        record[i].append(over_win[i])
        record[i].append(weights[i])
    #print(win_rate)
    answer = [i[0] for i in sorted(record, key= lambda x:(-x[1], -x[2], -x[3]))]
    return answer

weights   = [50,82,75,120]
head2head =   ["NLWL","WNLL","LWNW","WWLN"]
result = [3,4,1,2]
solution(weights, head2head)