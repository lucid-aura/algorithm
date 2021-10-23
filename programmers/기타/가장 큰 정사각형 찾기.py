def solution(board):
    dp = [[0 for i in range(len(board[0]))] for j in range(len(board))]
    answer = 0
    for i in range(len(dp)):
        dp[i][0] = board[i][0]
        if dp[i][0] == 1:
            answer = 1
    for j in range(len(dp[0])):
        dp[0][j] = board[0][j]
        if dp[0][j] == 1:
            answer = 1

    for i in range(1, len(dp)):
        for j in range(1, len(dp[0])):
            if board[i][j] == 1: 
                dp[i][j] = min(dp[i-1][j], dp[i][j-1], dp[i-1][j-1]) + 1
            if dp[i][j] > answer:
                answer = dp[i][j]

    answer = answer ** 2
    print(answer)
    return answer
    
board = [[0,1,1,1],[1,1,1,1],[1,1,1,1],[0,0,1,0]]
# 9

# board = [[0, 0, 1, 1], [1, 1, 1, 1]]
# 4 

# board = [[1,1],[1,1]]
# 4

solution(board)


###########################################################
# 동적프로그래밍으로 해결하는 문제
# 마지막 꼭지점 사각형은 왼, 위, 대각 점의 최소 + 1과 같다.
# dp[i][j] = min(dp[i-1][j], dp[i][j-1], dp[i-1][j-1]) + 1
# 해당 리스트에서 변의 길이가 나오므로 답은 제곱을 한다.
###########################################################