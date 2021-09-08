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







#################### 카펫 ##########################



# def solution(brown, yellow):
#     length = []
#     poss = []
#     area = brown+yellow
#     for i in range(2, int((area)**0.5)+1):
#         if area%i == 0:
#             poss.append(area//i)
#             poss.append(i)
#     for i in range(0, len(poss), 2):
#         diff = poss[i]*poss[i+1] - (poss[i]-2)*(poss[i+1]-2)
#         if diff == brown:
#             length = [poss[i], poss[i+1]]
#     print(length)

# brown = 10
# yellow = 2
# solution(brown, yellow)

####################### 체육복 ###########################
# def solution(n, lost, reserve):
#     answer = n
#     for i in lost:
#         if i in reserve:
#             lost.remove(i)
#             reserve.remove(i)

#     l1 = list(reserve)
#     l2 = list(reserve)
#     l3 = list(reserve)
#     l4 = list(reserve)
#     l5 = list(reserve)
#     l6 = list(reserve)    
#     a1 = answer
#     a2 = answer
#     a3 = answer
#     a4 = answer
#     a5 = answer
#     a6 = answer
#     for i in lost:
#         if len(lost) > 0:
#             if i-1 in reserve:
#                 reserve.remove(reserve[reserve.index(i-1)])
#             elif i+1 in reserve:
#                 reserve.remove(reserve[reserve.index(i+1)])
#             else:
#                 answer -= 1
#         else:
#             answer  -= 1

#     for i in lost: 
#         if len(l1) > 0:
#             if i-1 in l1:
#                 l1.remove(l1[l1.index(i-1)])
#             elif i+1 in l1:
#                 l1.remove(l1[l1.index(i+1)])
#             elif i in l1:
#                 l1.remove(l1[l1.index(i)])
#             else:
#                 a1 -= 1
#         else:
#             a1 -= 1
#         if len(l2) > 0:
#             if i+1 in l2:
#                 l2.remove(l2[l2.index(i+1)])
#             elif i-1 in l2:
#                 l2.remove(l2[l2.index(i-1)])
#             elif i in l1:
#                 l2.remove(l2[l2.index(i)])
#             else:
#                 a2 -= 1
#         else:
#             a2 -= 1
#         if len(l3) > 0:
#             if i in l3:
#                 l3.remove(l3[l3.index(i)])
#             elif i-1 in l3:
#                 l3.remove(l3[l3.index(i-1)])
#             elif i+1 in l3:
#                 l3.remove(l3[l3.index(i+1)])
#             else:
#                 a3 -= 1
#         else:
#             a3 -= 1
#         if len(l4) > 0:
#             if i in l4:
#                 l4.remove(l4[l4.index(i)])
#             elif i+1 in l4:
#                 l4.remove(l4[l4.index(i+1)])
#             elif i-1 in l4:
#                 l4.remove(l4[l4.index(i-1)])
#             else:
#                 a4 -= 1
#         else:
#             a4 -= 1
#         if len(l5) > 0:
#             if i-1 in l5:
#                 l5.remove(l5[l5.index(i-1)])
#             elif i in l5:
#                 l5.remove(l5[l5.index(i)])
#             elif i+1 in l5:
#                 l5.remove(l5[l5.index(i+1)])
#             else:
#                 a5 -= 1
#         else:
#             a5 -= 1
#         if len(l6) > 0:
#             if i+1 in l6:
#                 l6.remove(l6[l6.index(i+1)])
#             elif i in l6:
#                 l6.remove(l6[l6.index(i)])
#             elif i-1 in l6:
#                 l6.remove(l6[l6.index(i-1)])
#             else:
#                 a6 -= 1
#         else:
#             a6 -= 1
#     answer = max(a1,a2,a3,a4,a5,a6)
    
#     return answer

    
# reserve = [3]
# lost = [2,4]
# n = 5

# print(solution(n,lost,reserve))

############################### 상호 평가 ##########################################
# answer = ""
# scores = [[100,90,98,88,65],[50,45,99,85,77],[47,88,95,80,67],[61,57,100,80,65],[24,90,94,75,65]]
# new = [[scores[x][y] for x in range(len(scores))] for y in range(len(scores))]
# print(new)
# for i in range(len(new)):
#     score = 0
#     if max(new[i]) != new[i][i] and min(new[i]) != new[i][i] :
#         score = sum(new[i])/len(new[i])
#     elif len(list(filter(lambda x: new[i][x] == new[i][i], range(len(new[i])))))  != 1:
#         score = sum(new[i])/len(new[i])
#     else:
#         score = (sum(new[i])-new[i][i])/(len(new[i])-1)
        
#     if score >= 90:
#         answer += 'A'
#     elif score >= 80:
#         answer += 'B'
#     elif score >= 70:
#         answer += 'C'
#     elif score >= 50:
#         answer += 'D'
#     else:
#         answer += 'F'
# print(answer)
#    # answer = ''
#    # return answer


################################## 퍼즐 조각 채우기 ###################################
# import copy

# game_board = [[1,1,0,0,1,0],[0,0,1,0,1,0],[0,1,1,0,0,1],[1,1,0,1,1,1],[1,0,0,0,1,0],[0,1,1,1,0,0]]
# #game_board = [[0, 0, 0, 0, 0, 0, 1, 0, 1, 0, 0, 0], [1, 1, 1, 1, 1, 1, 0, 0, 0, 1, 0, 0], [0, 0, 0, 0, 0, 1, 0, 1, 0, 1, 1, 0], [1, 0, 1, 1, 1, 0, 1, 0, 1, 0, 0, 1], [0, 1, 0, 0, 0, 0, 1, 0, 1, 0, 0, 0], [0, 0, 1, 1, 1, 0, 1, 0, 1, 1, 0, 1], [0, 1, 0, 0, 0, 1, 1, 0, 0, 0, 1, 0], [0, 0, 1, 0, 1, 0, 0, 1, 1, 1, 0, 0], [1, 1, 0, 0, 1, 0, 0, 1, 1, 1, 1, 0], [0, 0, 1, 1, 0, 1, 0, 1, 1, 1, 0, 0], [0, 0, 1, 0, 0, 1, 0, 1, 1, 0, 1, 1], [0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 0, 0]]
# table = [[1,0,0,1,1,0],[1,0,1,0,1,0],[0,1,1,0,1,1],[0,0,1,0,0,0],[1,1,0,1,1,0],[0,1,0,0,0,0]]
# #table = [[1, 1, 1, 0, 1, 1, 1, 0, 0, 0, 1, 1], [1, 1, 0, 0, 0, 0, 1, 1, 1, 0, 1, 1], [1, 0, 1, 0, 1, 0, 0, 0, 0, 1, 1, 0], [0, 0, 1, 1, 1, 0, 0, 1, 1, 0, 0, 0], [1, 1, 0, 1, 0, 0, 0, 1, 1, 1, 0, 0], [1, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0], [1, 0, 0, 1, 0, 1, 1, 1, 0, 0, 0, 1], [1, 1, 0, 1, 0, 1, 1, 1, 0, 0, 0, 1], [0, 0, 0, 1, 1, 0, 0, 0, 1, 1, 0, 1], [1, 1, 0, 1, 1, 0, 1, 0, 0, 1, 0, 1], [1, 1, 1, 0, 0, 0, 1, 0, 1, 1, 0, 1], [1, 0, 0, 1, 1, 1, 1, 0, 0, 1, 0, 1]]

# def solution(game_board, table):
#     def rotate(table, length):
#         rotate_table = copy.deepcopy(table)
#         for i in range(length):
#             for j in range(length):
#                 rotate_table[j][length - i - 1] = table[i][j]
#         return rotate_table

#     answer = 0
#     length = len(game_board[0])
#     for i in range(length):
#         for j in range(length):
#             table[i][j] = 1-table[i][j]


#     def ishole(i, j, board, block):
#         board[i][j] = 1
#         block.append([i,j])
#         if j < length-1:
#             if board[i][j+1] == 0:
#                 ishole(i, j+1, board, block)
#         if j > 0:
#             if board[i][j-1] == 0:
#                 ishole(i, j-1, board, block)
#         if i < length-1:
#             if board[i+1][j] == 0:
#                 ishole(i+1, j, board, block)
#         if i > 0:
#             if board[i-1][j] == 0:
#                 ishole(i-1, j, board, block)
#         return 0

#     # resize
#     def resize(holes):
#         for i in holes:
#             x = i[0][0]
#             y = i[0][1]
#             for j in i:
#                 j[0] = j[0] - x
#                 j[1] = j[1] - y

#     def task(game_board, table, answer):
#         origin_board = copy.deepcopy(game_board)
#         origin_table = copy.deepcopy(table)

#         # find board hole 
#         holes = list()
#         for i in range(length):
#             for j in range(length):
#                 if game_board[i][j] == 0:
#                     hole = list()
#                     ishole(i, j, game_board, hole)
#                     holes.append(hole)

#         origin_hole = copy.deepcopy(holes)
#         resize(holes)

#         # find block
#         blocks = list()
#         for i in range(length):
#             for j in range(length):
#                 if table[i][j] == 0:
#                     block = list()
#                     ishole(i, j, table, block)
#                     blocks.append(block)

#         # compare block and hole
#         block_number = []
#         hole_number = []
#         origin_block = copy.deepcopy(blocks)
#         resize(blocks)
#         for i in range(len(holes)):
#             for j in range(len(blocks)):
#                 if holes[i] == blocks[j] and j not in block_number and i not in hole_number:
#                     block_number.append(j)
#                     hole_number.append(i)

#         # remove holes
#         for i in hole_number:
#             for j in origin_hole[i]:
#                 origin_board[j[0]][j[1]] = 1
#                 answer += 1

#         # remove blocks
#         for i in block_number:
#             for j in origin_block[i]:
#                 origin_table[j[0]][j[1]] = 1


#         # update board and table
#         game_board = origin_board
#         table = origin_table
#         return game_board, table, answer

#     # task1 - 0 degree
#     game_board, table, answer = task(game_board, table, answer)

#     # rotate table
#     table = rotate(table, length)

#     # task2 - 90 degree
#     game_board, table, answer = task(game_board, table, answer)

#     # rotate table
#     table = rotate(table, length)

#     # task3 - 180 degree
#     game_board, table, answer = task(game_board, table, answer)

#     # rotate table
#     table = rotate(table, length)

#     # task4 - 270 degree
#     game_board, table, answer = task(game_board, table, answer)
#     return answer

########################### 직업군 추천하기 ##############################
# table = ["SI JAVA JAVASCRIPT SQL PYTHON C#", "CONTENTS JAVASCRIPT JAVA PYTHON SQL C++", "HARDWARE C C++ PYTHON JAVA JAVASCRIPT", "PORTAL JAVA JAVASCRIPT PYTHON KOTLIN PHP", "GAME C++ C# JAVASCRIPT C JAVA"]
# languages = ["PYTHON", "C++", "SQL"]	
# preference = [7, 5, 5]



# split_table = []
# for i in table:
#     split_table.append(i.split(' '))

# score = dict()
# for i in split_table:
#     score[i[0]] = 0

# for jobs in split_table:
#     for language in languages:
#         if language in jobs:
#             print(language)
#             print(len(jobs) - jobs.index(language))
#             score[jobs[0]] = score[jobs[0]] + (len(jobs) - jobs.index(language))*preference[languages.index(language)]
# print(score)

# ## C -> G -> H -> P -> S
# order = ["SI", "PORTAL", "HARDWARE", "GAME", "CONTENTS"]
# answer = 'SI'

# i = 0
# j = 1
# while i+j < 5:
#     if score[order[i]] <= score[order[i+j]]:
#         i = i+j
#         answer = order[i]
#         j = 1
#     else:
#         j += 1


# print(answer)


################################### 모음 사전 #######################################
 
words = ['A', 'E', 'I', 'O', 'U']
word = "EIO" # ["AAAAE", "AAAE", "I", "EIO"]
answer = 0
offset = [781, 156, 31, 6, 1]
for i in range(len(word)):
    print(words.index(word[i])*offset[i])
    answer += words.index(word[i])*offset[i] + 1

print(answer)