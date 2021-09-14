def solution(id_list, report, k):
    answer = [0 for i in range(len(id_list))]
    warn_num = {} # 경고 횟수
    warn_target = {} # 경고한 사람
    for i in id_list:
        warn_num[i] = 0
        warn_target[i] = []
    
    for i in report:
        token = i.split()
        if token[0] not in warn_target[token[1]]:
            warn_num[token[1]] += 1
            warn_target[token[1]].append(token[0])
            print(warn_target)
            print(warn_num[token[1]])

    for i in warn_num:
        if warn_num[i] >= k:
            for j in warn_target:
                if i == j:
                    for l in warn_target[i]:
                        print(l)
                        answer[id_list.index(l)] += 1

    return answer


id_list = ["muzi", "frodo", "apeach", "neo"]
report = ["muzi frodo","apeach frodo","frodo neo","muzi neo","apeach muzi"]
id_list = ["con", "ryan"]
report = ["ryan con", "ryan con", "ryan con", "ryan con"]
k=3
print(solution(id_list, report, k))
