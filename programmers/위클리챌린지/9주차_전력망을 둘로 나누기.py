def solution(n, wires):
    def area(trees, node):
        length = 0
        while length != len(node):
            length = len(node)
            for i in node:
                for j in trees:
                    if i == j[0] and j[1] not in node:
                        node.append(j[1])
                    elif i == j[1] and j[0] not in node:
                        node.append(j[0])
        return len(node)

    answer = n
    for i in range(n):
        new_tree = wires[:i] + wires[i+1:]
        node = [new_tree[0][0]]
        length = area(new_tree, node)
        answer = min(answer, abs(n- 2*length))
    return answer

n = 9
wires = [[1,3],[2,3],[3,4],[4,5],[4,6],[4,7],[7,8],[7,9]]
solution(n, wires)

########################################################
# 전력망을 하나씩 끊어보면서 차가 최소인 값을 찾는다.
# 다음 노드가 없을때까지 한 노드에서 다른 노드로 가는 경로가 있을 경우 방문 노드에 추가한다.
# 더이상 방문하지 않은 노드가 없을 경우 길이가 변하지 않는다. - 탈출 조건 (노드 추가가 되지 않았기 때문에)
# 방문한 노드 개수와 전체 노드의 차이가 전력망을 하나 끊었을 때의 두 트리의 노드 개수의 차이다.
########################################################