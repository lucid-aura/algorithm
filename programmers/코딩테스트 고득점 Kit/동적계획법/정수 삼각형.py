def solution(triangle):
    max_tree = [[] for i in range(len(triangle))]
    max_tree[0] = [triangle[0][0]]
    
    for depth in range(1, len(triangle)):
        for idx in range(len(triangle[depth])):
            left = 0
            right = 0
            if idx > 0:
                left = max_tree[depth-1][idx-1]
            if idx < len(triangle[depth])-1:
                right = max_tree[depth-1][idx]
            max_tree[depth].append(max(left, right) + triangle[depth][idx])
    
    answer = max(max_tree[-1])
    print(answer)
    return answer

triangle = [[7], [3, 8], [8, 1, 0], [2, 7, 4, 4], [4, 5, 2, 6, 5]]
solution(triangle)
# 30

########################################################
# 자식노드의 값은 더 큰 부모의 값과 자신의 합이다.
# 왼쪽 부모는 항상 자식의 노드보다 index가 1이 작다
# 오른쪽 부모는 항상 자식의 노드와 같은 index를 가진다.
# 자식의 index가 0일 때는 오른쪽 부모밖에 없다.
# 마찬가지로 자식의 index가 마지막을 때 왼쪽 부모밖에 없다.
# 가장 마지막 단말노드까지 순차적으로 계산한다.
########################################################