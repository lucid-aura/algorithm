import copy
def solution(k, dungeons):
    def DFS(dungeons, index, route, life, order):
        print(route)
        if dungeons[index][1] > life or dungeons[index][0] > life:
            if len(order) == 0:
                order.append(len(route))
                return
            if order[0] < len(route):
                order[0] = len(route)
            return
        route.append(index)
        life -= dungeons[index][1]
        if len(order) > 0 and order[0] < len(route):
            order[0] = len(route)
        for i in range(len(dungeons)):
            if i not in route:
                new_route = copy.deepcopy(route)
                new_life = life
                print(new_route, new_life, i)
                DFS(dungeons, i, new_route, new_life, order)

    answer = 0
    order = []
    for i in range(len(dungeons)):
        route = []
        DFS(dungeons, i, route, k, order)
    print(order[0])
    return answer

k = 80
# ["최소 필요 피로도", "소모 피로도]
dungeons = [[80,20],[50,40],[30,10]]	
solution(k, dungeons)


###################################################################
# 완전 탐색으로 가능한 모든 조합의 경우를 확인해야한다.(Permutation)
# 최소 필요 피로도를 넘거나 피로도가 음수가 되지 않을 경우를 정한다.
# 경로를 route 리스트에 추가하고 개수는 order 리스트에 추가한다.
# order 리스트는 최대 개수를 가지는 하나의 원소를 갖는다.
#################################################################