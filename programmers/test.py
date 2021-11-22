import math
from itertools import permutations
N, M = input().split()
N, M = int(N), int(M)
num = list(map(int, input().split()))
num.sort()
print(num)
    
permute = permutations(num,M)
for i in permute:
    answer = ''
    for a in i:
        answer += str(a) + ' '
    print(answer)
# [(1,2),(1,3),(2,1),(2,3),(3,1),(3,2)]

    
#  import sys
# N = int(sys.stdin.readline().strip())
# queue = [-1 for i in range(2000001)]
# front = 0
# rear = 0
# for i in range(N):
#     order = sys.stdin.readline().split()
#     if order[0] == 'push':
#         queue[front] = order[1]
#         front = (front+1)%2000001
#     elif order[0] == 'pop':
#         if front-rear == 0:
#             print(-1)
#         else:
#             print(queue[rear])
#             queue[rear] = -1
#             rear = (rear+1)%2000001
#     elif order[0] == 'size':
#         if front >= rear:
#             print(front - rear)
#         else:
#             print(2000001 - rear + front)
#     elif order[0] == 'front':
#         if front-rear == 0:
#             print(-1)
#         else:
#             print(queue[rear-1])
#     elif order[0] == 'empty':
#         if front-rear == 0:
#             print(1)
#         else:
#             print(0)
#     else:
#         if front-rear != 0:
#             print(queue[front-1])
#         else:
#             print(-1)

# 15
# push 1
# push 2
# front
# back
# size
# empty
# pop
# pop
# pop
# size
# empty
# pop
# push 3
# empty
# front


# num = [[0 for j in range(N+1)] for i in range(10)]
# num[0] = [0]
# for i in range(num[1]):
#     num[1][i] = 
# num[1] = 9
# for i in range(2, N+1):
#     num[i] = ((num[i-1]-i+1)*2 + i-1) % 1000000000
# print(num[N]%1000000000)

# N = int(input())
# choice = [0]
# wine = [0 for i in range(N+1)]
# for i in range(N):
#     choice.append(int(sys.stdin.readline()))
# if N==1:
#     print(choice[1])
# elif N==2:
#     print(choice[1] + choice[2])
# else:
#     wine[1] = choice[1]
#     wine[2] = choice[1] + choice[2]
#     for i in range(3, N+1):
#         wine[i] = max(wine[i-2] , wine[i-3] + choice[i-1]) + choice[i]
#     print(wine[-1])

# 4 = 1 + 3
# 5 = 1 + 3
# 6 = 1 + 5
# 7 = 2 + 6
# 8 = 3 + 7
# 9 = 4 + 8

# 10 = 5 + 9

    # print(A[i], B[i])


# func = [0 for i in range(100)]
# func[0] = 2
# for i in range(1, 100):
#     func[i] = func[i-1] + 6*(i-1)

# 1 2 6
# 3 5
# 4


# 1     2   4   7  11  16
# 3    5   8  12 17
# 6    9  13 18
# 10 14 19
# 15 20
# 21

# import copy

# def solution(numbers):
#     answer = 0
#     number = ""
#     idx = []
#     prime = set()
#     # prime = list()
#     for i in range(len(numbers)):
#         idx.append(True)
#     for i in range(1, len(numbers)+1):
#         # idx.append(i-1)
#         combi(numbers, number, i, idx, prime)
#         for i in range(len(numbers)):
#             idx[i] = True
#     for i in prime:
#         if i > 1:
#             answer += 1
#             for j in range(2,i):
#                 if i % j == 0:
#                     answer -= 1
#                     break

#     print(prime)
#     print(answer)

# def combi(numbers, number, length, idx, prime):
#     for i in range(len(numbers)):
#         index = list(idx)
#         num = number
#         if (index[i]):
#             index[i] = False
#             num += numbers[i]
#             if (len(num) < length): # 진입부분
#                 print(length, number, num, index, idx, prime, numbers[i])
#                 combi(numbers, num, length, index, prime)
#             else: # 추가 부분 (체크 부분)
#                 # prime.append(int(num))
#                 prime.add(int(num))
#     return prime

# numbers = "11"
# solution(numbers)