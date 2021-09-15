################################## 입실 퇴실 ####################################

# 확정적으로 만난 사람 정하고
# 그 사람들의 정보를 통해 추가 해야함

def solution(enter, leave):
    record = [[] for i in range(len(enter))]
    test = [0 for i in range(len(enter))]
    print("# 답은 2,2,1,3")
    while(len(enter) > 1):
        # test[enter[0] - 1] += 1
        if enter[0] != leave[0]:
            for i in leave[: leave.index(enter[0])]:
                #print(i)
                #print(leave[: leave.index(enter[0])])
                #print(enter.index(enter[i]))
                test[enter[0] - 1] += 1
                test[i-1] += 1
                print(0,enter[0], i )
                for j in leave[:]:
                        test[enter[0] - 1] += 1
                        test[j-1] += 1
                        print(1,enter[0],j)
                # for j in range(len(enter[1:enter.index(i)])):
                #     #print(enter[0], i, j)
                #    # if i != j: # and enter.index(j) != len(enter)-1:
                    
                #         test[enter[0] - 1] += 1
                #         test[enter[1:enter.index(i)][j]-1] += 1
                #     print(1,enter[0],j)
        leave.remove(enter[0])
        del(enter[0])


    # while(len(enter) > 0):    
    #     leave_idx = leave.index(enter[0])
    #     temp = []
    #     for j in leave[:leave_idx]:
    #         if j != enter[0] and j in enter[1:]:
    #             record[enter[0]-1].append(j)
    #             record[j-1].append(enter[0])
    #             temp.append(j)
    #     leave.remove(enter[0])
    #     for j in temp:
    #         for k in enter[:enter.index(j)]:
    #             if k != enter[0] and k not in record[enter[0]-1]:
    #                 record[enter[0]-1].append(k)
    #                 record[k-1].append(enter[0])
    #     del(enter[0])
        
    answer = [len(i) for i in record]

    # for i in range(len(record)):
    #     for j in range(len(record[i])):
    #         if record[i][j] not in record[j-1] and j-1 != record[i][j]-1:
    #             record[j+1].append(i+1)

    #print(answer)
    print(test)
    # for i in enter:
    #     enter_idx = enter.index(i)
    #     leave_idx = leave.index(i)
    #     temp = []
    #     for j in enter[enter_idx:]: # 나중에 들어옴
    #         if j in leave[:leave_idx]: # 먼저 나감
    #             temp.append(j)
    #             record[i-1].append(j)
    #     for j in temp:
    #         for k in enter[enter_idx+1: enter.index(j)]:
    #             print(i, j, k)
    #             if k not in record[i-1]:
    #                 record[i-1].append(k)

    #     temp = []
    # for i in leave:
    #     enter_idx = enter.index(i)
    #     leave_idx = leave.index(i)       
    #     for j in leave[:leave_idx]: # 먼저 나감
    #         if j in enter[enter_idx:]: # 나중에 들어옴
    #             # print(i, j)
    #             temp.append(j)
    #             record[i-1].append(j)
    #     for j in temp:
    #         print(i, j)
    #         print(leave[j+1:leave_idx])
    #         for k in leave[leave.index(j)+1:leave_idx]:
    #             print(i, j, k)
    #             if k not in record[i-1]:
    #                 record[i-1].append(k)
        
    #     for j in enter[0:enter_idx]: # i번 보다 먼저 출입한 사람은
    #         if j in leave[leave_idx:]: # i번보다 나중에 나가야 확실히 만난다.
    #             record[i-1].append(j)
    #     temp = []
    #     for j in record[i-1]: # 먼저 출입하고 나중에 나간 사람들 중
    #         temp = enter[leave_idx:leave.index(j):] # 그사람과 i번째 사이에 나간 사람은 확실히 만난다.
    #     for j in temp:
    #         if i != j:
    #             record[i-1].append(j)
    #     print(record)
    #     for j in enter[enter_idx:]: # i번 보다 나중에 출입한 사람은
    #         #print(j)
    #         if j in leave[0:leave_idx]: # i번 보다 먼저 나가야 확실이 만난다.
    #             print(j)
    #             record[i-1].append(j)
    #     for j in record[i-1]: # 나중에 출입하고 먼저 나간 사람들 중 
    #         temp = enter[enter.index(j):enter_idx] # 그 사람과 i번째 사이에 들어온 사람은 확실히 만난다.
    #         print(j)
    #         print(enter.index(j), enter_idx)
    #     for j in temp:
    #         if i != j:
    #             record[i-1].append(j)
    #     print(record)
    # answer = [len(i) for i in record]

    print(record)
    answer = 0
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