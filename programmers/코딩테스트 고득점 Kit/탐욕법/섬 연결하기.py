def solution(n, costs):
    parent = [i for i in range(100)]
    costs.sort(key = lambda x:x[2])
    answer = 0
    for i in costs:
        if parent[i[0]] != parent[i[1]]:
            before = parent[i[1]]
            for j in range(len(parent)):
                if parent[j] == before:
                    parent[j] = parent[i[0]]
            answer += i[2]
    print(answer)
    return answer
    
# n = 4
# costs = [[0,1,1],[0,2,2],[1,2,5],[1,3,1],[2,3,8]]

# n = 4
# costs = [[0, 1, 5], [1, 2, 3], [2, 3, 3], [3, 1, 2], [3, 0, 4]]
#output: 9

n = 6
costs = [[0, 1, 5], [0, 3, 2], [0, 4, 3], [1, 4, 1], [3, 4, 10], [1, 2, 2], [2, 5, 3], [4, 5, 4]]
#output: 11

# n = 4
# costs = [[0, 1, 5], [1, 2, 3], [2, 3, 3], [3, 1, 2], [3, 0, 4]]
#output: 9

# n = 5
# costs = [[0, 1, 1], [0, 2, 2], [1, 2, 5], [1, 3, 3], [2, 3, 8], [3, 4, 1]]
#output: 7

# n = 5
# costs = [[0, 1, 1], [3, 4, 1], [1, 2, 2], [2, 3, 4]]
#output: 8

n = 4
costs = [[2, 3, 3], [2, 4, 4], [3, 4, 7], [3, 5, 3], [4, 5, 10]]
output: 10

# n = 1
# costs = [[]]
solution(n, costs)

#############################################################
# 크루스칼 알고리즘을 적용한 최소 신장 트리 문제이다.
# union-find를 위한 parent 리스트를 선언한다.
# parent의 값은 해당 인덱스의 부모 노드를 의미한다.
# edge를 cost기준으로 오름차순 정렬한다.
# 차례대로 엣지로 연결된 두 노드의 부모를 확인한다.
# 각 노드의 부모가 같으면 싸이클이 생성되므로 제외한다.
# costs[1]의 부모를 costs[0]의 부모로 바꾼다.
# costs[1]을 부모로 했던 다른 노드들도 costs[0]의 부모로 바꾼다.
# 선택한 edge의 cost를 추가한다.
##############################################################