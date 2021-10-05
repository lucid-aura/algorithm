################################## 입실 퇴실 ####################################

def solution(enter, leave):
    room = []
    answer  = [0 for i in range(len(enter))]
    while(len(enter) > 0 or len(leave) > 0):
        if leave[0] in room:
            answer[leave[0]-1] += len(room) - 1
            room.remove(leave[0])
            leave.remove(leave[0])
            for i in room:
                answer[i-1] += 1
        else:
            room.append(enter[0])
            enter.remove(enter[0])     
    print(answer)
    return answer

enter = [1,3,2]
leave = [1,2,3]
enter = [1,4,2,3]
leave = [2,1,3,4]
# 답은 2,2,1,3
# enter = [1,4,2,3]
# leave = [2,1,4,3]
# 답은 2,2,0,2
# enter = [3,2,1]
# leave = [1,3,2]
solution(enter, leave)