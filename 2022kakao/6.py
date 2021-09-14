
def solution(board, skill):
    x1 = 0
    x2 = 0
    y1  = 0
    y2 = 0
    answer = 0
    for i in skill:
        if i[0] == 1:
            for j in range(i[1],i[3]+1):
                for k in range(i[2],i[4]+1):
                    board[j][k] -= i[5]
        else:
            for j in range(i[1],i[3]+1):
                for k in range(i[2],i[4]+1):
                    board[j][k] += i[5]
        for j in board:
            print(j)
    for i in range(len(board)):
        for j in range(len(board[i])):
            if board[i][j] > 0:
                answer += 1
    return answer

board = [[5,5,5,5,5],[5,5,5,5,5],[5,5,5,5,5],[5,5,5,5,5]]
board = [[1,2,3],[4,5,6],[7,8,9]]
skill = [[1,0,0,3,4,4],[1,2,0,2,3,2],[2,1,0,3,1,2],[1,0,1,3,3,1]]
skill = [[1,1,1,2,2,4],[1,0,0,1,1,2],[2,2,0,2,0,100]]	

print(solution(board, skill))