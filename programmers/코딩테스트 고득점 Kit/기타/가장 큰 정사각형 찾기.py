def solution(board):
    def check_stream(col, row, n, board):
        for i in range(len(col)-n+1):
            for j in range(len(row)-n+1):
                for k in range(i, i+n):
                    for l in range(j, j+n):
                        ret = True
                        print(i, j, k, l, n)
                        for a in board:
                            print(a)
                        print("#########")
                        if col[k] < n or row[l] < n or board[l][k] == 0:
                            board[k][l] = 7

                            ret = False
                            break
                if ret:
                    return ret
                else:
                    break
        return False

    col = []
    row = []
    for i in board:
        row.append(i.count(1))
    print(row)

    for i in range(len(board[0])):
        value = 0
        for j in range(len(board)):
            value += board[j][i]
        col.append(value)
    print(col)

    max_length = min(max(col), max(row))
    print(max_length)
    for i in range(max_length, 0, -1):
        if check_stream(col, row, i, board): # and check_stream(row, i):
            answer = i**2
            print(answer)
            return answer
    return 0
    # for i in range(len(board)):
    #     for j in range(len(board[0])):




board = [[0,1,1,1],[1,1,1,1],[1,1,1,1],[0,0,1,0]]
board = [[0,1,1,1],[1,1,1,1],[1,1,1,1],[0,1,1,1]]
board = [[0,1,1,1],[0,1,1,1],[1,0,1,1],[0,1,1,1]]
# 9

board = [[0, 0, 1, 1], [1, 1, 1, 1]]
# 4 

# board = [[1,1],[1,1]]
# 4
solution(board)


# def solution(board):
#     def isSquare(col, row, length, board):
#         for i in range(col, col+length):
#             for j in range(row, row+length):
#                 if board[i][j] == 0:
#                     return False
#         return True

#     def find_length(x1, y1, x2, y2, board):
#         answer = 0
#         max_length = min(y2-y1, x2-x1)
#         for i in range(y1, y2):
#             for j in range(x1, x2):
#                 if board[i][j] == 1:
#                     answer = 1
#                     break
#         if answer == 1:
#             return 0
#         else:
#             answer = 0

#         for length in range(max_length, 0, -1):
#             if length == 1:
#                 return 1
#             for i in range(y2-y1 - length + 1):
#                 for j in range(x2-x1 - length + 1):
#                     if isSquare(i, j, length, board):
#                         answer = length ** 2
#                         break
#                 if answer > 0:
#                     break
#             if answer > 0:
#                 break
#         return answer
    
#     answer = 0
#     for i in range(len(board)):
#         for j in range(len(board)):
#             if board[i][j] == 0:
#                 one, two, three, four = 0, 0, 0, 0
#                 one = find_length(0, j+1, 0, i+1, board)
#                 two = find_length(j, len(board[0]), 0, i+1, board)
#                 three = find_length(0, j+1, i, len(board), board)
#                 four = find_length(j, len(board[0]), i, len(board), board)
#                 answer = max(answer, one, two, three, four)
    
#     print(answer)
#     return answer


# def solution(board):
#     def check_stream(arr, n):
#         for i in range(len(arr)-n+1):
#             for j in range(i, i+n):
#                 ret = True
#                 if arr[j] < n or board[i][j] == 0:
#                     ret = False
#                     break
#             if ret:
#                 return ret
#         return False
    
#     col = []
#     row = []
#     for i in board:
#         row.append(i.count(1))

#     for i in range(len(board[0])):
#         value = 0
#         for j in range(len(board)):
#             value += board[j][i]
#         col.append(value)
#     max_length = min(max(col), max(row))
#     for i in range(max_length, 0, -1):
#         if check_stream(col, i) and check_stream(row, i):
#             answer = i**2
#             return answer
#     return 0