def solution(name):
    def diff_idx(name):
        init = "A"*len(name)    
        result = []
        for i in range(len(name)):
            if init[i] != name[i]:
                result.append(i)
        return result

    def calc_cost(name, idx):
        cost = [0 for i in range(len(idx))]
        for i in range(len(idx)):
            if 91 - ord(name[idx[i]]) < ord(name[idx[i]]) - 65:
                cost[i] = 91 - ord(name[idx[i]])
            else:
                cost[i] = ord(name[idx[i]]) - 65
        return cost

    def calc_range(pos, name, idx):
        dis = [0 for i in range(len(idx))]
        for i in range(len(dis)):
            dis[i] = min(abs(pos - idx[i]), pos + len(name)-idx[i])
        return dis

    idx = diff_idx(name)
    cost = calc_cost(name, idx)
    pos = 0
    dis = calc_range(pos, name, idx)

    print(idx)
    print(cost)
    print(dis)
    answer = 0
    while len(idx) > 1:
        total = [0 for i in range(len(idx))]
        for i in range(len(total)):
            total[i] = cost[i] + dis[i]

        select = dis.index(min(dis))
        answer += dis[select] + cost[select]
        print(select)
        pos = idx.pop(select)
        print(name[pos])
        #idx = diff_idx(name)
        cost = calc_cost(name, idx)
        dis = calc_range(pos, name, idx)
        print(idx)
        print(cost)
        print(dis)
    answer += dis[0] + cost[0]
    print(answer)
    return answer
    # pos = 0
    # init = "A"*len(name)
    # cost = [0 for i in range(len(name))]
    # left = 0
    # right = 0
     
    # # 각각의 알파벳을 바꾸는데 필요한 cost 계산
    # for i in range(len(name)):
    #     if 91 - ord(name[i]) < ord(name[i]) - 65:
    #         cost[i] = 91 - ord(name[i])
    #     else:
    #         cost[i] = ord(name[i]) - 65
    
    # while ''.join(init) != name:
    #     init = list(init)
    #     init[pos] = name[pos]
    #     right += cost[pos] # 값 변경 버튼
    #     right += 1 # 오른쪽 버튼
    #     pos += 1 # 위치 변경
    # right -= 1
    # if right == -1:
    #     right = 0

    # init = 'A'*len(name)
    # pos = 0
    # while ''.join(init) != name:
    #     init = list(init)
    #     init[pos] = name[pos]
    #     left += cost[pos] # 값 변경
    #     left += 1 # 위치 변경
    #     pos -= 1
    # left -= 1
    # if left == -1:
    #     left = 0

    # return min(right, left)

name = "JAZ"
name = "JEROEN"
solution(name)