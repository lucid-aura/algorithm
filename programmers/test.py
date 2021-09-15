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