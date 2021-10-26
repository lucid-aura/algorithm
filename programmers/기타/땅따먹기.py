import copy

def solution(land):
    # dp[i] = dp[i-1] + dp[1]
    dp = [[] for i in range(101)]
    for i in range(len(land[0])):
        dp[land[0][i]].append([i])
    print(dp)
    
land = [[1,2,3,5],[5,6,7,8],[4,3,2,1]]
solution(land)


# def solution(land):
#     def DFS(n, prev, result, arr):
#         if n == len(land):
#             if len(arr) == 0:
#                 arr.append(result)
#             else:
#                 if arr[0] < result:
#                     arr.pop()
#                     arr.append(result)
#             return 
#         for i in range(4):
#             if i != prev:
#                 new_result = result
#                 new_result += land[n][i]
#                 DFS(n+1, i, new_result, arr)
#         return

#     for i in range(len(land[0])):
#         arr = []
#         DFS(1, i, land[0][i], arr)

#     answer = arr[0]
#     print(arr[0])
#     return answer