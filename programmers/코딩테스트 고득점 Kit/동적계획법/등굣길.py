def solution(m, n, puddles):
    road = [[0 for i in range(m)] for j in range(n)]
    for i in range(n):
        for j in range(m):
            if i == 0 and j == 0:
                road[i][j] = 1
            elif [j+1, i+1] in puddles:
                road[i][j] = 0
            else:
                left, up = 0, 0
                if i > 0:
                    left = road[i-1][j]
                if j > 0:
                    up = road[i][j-1]
                road[i][j] = left + up
    answer = road[-1][-1]%1000000007
    return answer


m = 4
n = 3
puddles = [[2, 2], [2, 3], [2, 4]]
# puddles = [[1, 2], [2, 1]]
# puddles = []
# 4

solution(m, n, puddles)

########################################################
# 자식노드의 값은 더 큰 부모의 값과 자신의 합이다.
# 왼쪽 부모는 항상 자식의 노드보다 index가 1이 작다
# 오른쪽 부모는 항상 자식의 노드와 같은 index를 가진다.
# 자식의 index가 0일 때는 오른쪽 부모밖에 없다.
# 마찬가지로 자식의 index가 마지막을 때 왼쪽 부모밖에 없다.
# 가장 마지막 단말노드까지 순차적으로 계산한다.
########################################################