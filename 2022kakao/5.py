def DP(now, info, edges, sheep, wolf):
    if info[now] == 0: # ���� �ִ� ���
        sheep += 1
    else:
        wolf += 1
    if sheep <= wolf: #���� ���� ���� �������� �Ұ����ϴ�
        return -1
    else:
        for i in edges:
            if i[0] == now: # ���� ���� ���ϴ�.
                DFS(now, sheep, wolf)

def solution(info, edges):
    update = []
    dp = [[0 for i in range(len(info))] for j in range(len(info))]
    dp[0][0] = 1
    # edges[a][b] == a에서 b로가는 선 (반대도 가능하다)
    for i in range(len(edges)):
        for j in range(len(edges)):
            #if [i,j] in edges: #서로 하나의 엣지로 이어져있으면
            comp_list = []
            for j in update:
                comp_list.append(dp[i][j])
            dp[i][j] = max(comp_list) + info[j]
            #     if info[i] == 1: #양이면
            #         dp[0][edges[i][1]]  = dp[0][0] + info[edges[i][1]]
            # else: # 루트 노드가 아닐 때
            #     dp[i]
        update.append(i)
    a = 0

    for i in dp:

        print(a, i)
        a +=1
    dp[0][0] = 1

    answer = 0
    sheep = 0
    wolf = 0
    count = 0
    return answer

info = [0,0,1,1,1,0,1,0,1,0,1,1] #1�� ���� 0�� ��
for i in range(len(info)):
    info[i] = info[i]*-2 + 1
print(info)
edges = [[0,1],[1,2],[1,4],[0,8],[8,7],[9,10],[9,11],[4,3],[6,5],[4,6],[8,9]]
solution(info, edges)