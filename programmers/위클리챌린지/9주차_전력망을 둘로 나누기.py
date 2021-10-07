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