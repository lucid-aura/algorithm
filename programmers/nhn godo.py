# goods = [0,0,0]
# answer = goods[0] +goods[1] +goods[2]
# over = []
# for i in range(3):
#     if goods[i] < 50:
#         over.append(i)

# if len(over) == 3: # 전품목 50 미만
#     if goods[0] + goods[1] + goods[2] >= 50:
#         answer -= 10
#         print(answer)
# elif len(over) == 2: # 50 미만 가격이 2개
#     if goods[over[0]]+goods[over[1]] >= 50: #미만인 2개 물품 더해서 50 넘으면
#         answer -= 20
#         print(answer)
#     else: #넘지 못하면
#         answer -= 10
#         print(answer)
# elif len(over) == 1: # 50 미만 가격이 1개
#     answer -= 20
#     print(answer)
# else: # 전 품목 50 이상
#     answer -= 30
#     print(answer)


# # page = 5457
# # broken = [6,7,8]
# # page = 99999
# # broken = [0,2,3,4,5,6,7,8,9]
# # page = 158
# # broken = [1,9,2,5,4]
# # page = 99999
# # broken = [0,2,3,4,5,6,7,8,9]
# # page = 158
# # broken = [1,9,2,5,4]
# page = 151241
# broken = [0,1,2,3,4,7,8,9]
# # page = 100
# # broken = [1,0,5]
# pages = [] # 각 숫자를 토큰화하여 넣은 리스트
# mins = [] # 여러 최소값을 찾기 위한 리스트
# avail = [] # 숫자 차이가 작은 mins( 최대 2개 )
# can = [] # 누를 수 있는 버튼 리스트
# choice = [] #선택할 번호
# for i in range(10):
#     if i not in broken:
#         can.append(i)

# for i in range(len(str(page))):
#     pages.append(int(str(page)[i]))
#     #print(pages[i])


# for i, value in enumerate(pages):
#     if value in can: #가능한 버튼일 경우
#         choice.append(value) # 그 숫자 선택
#     else: # 고장난 버튼일 경우
#         #print(pages[i])
#         for j in can:
#             mins.append(abs(pages[i]-j)) #차이가 최소인 값을 찾는다.
#         print(len(mins))
#         if len(mins) == 1:    
#             m = mins[0]
#         else:
#             m = min(mins)
#         #print(min)
#         for idx, j in enumerate(mins):
#             if m == j:
#                 avail.append(can[idx])         

#         if i < len(str(page))-1: # 일의 자리 숫자가 아닌 경우
#             if len(avail) == 1:
#                 # 가능한 최소값이 하나다 = 그냥 그 숫자 선택
#                 choice.append(avail[0])
#             else:
#                 if pages[i+1] < 5: # 01234면
#                     choice.append(avail[0]) # 작은 값으로 한다. [0]
#                 else: #56789 이면
#                     choice.append(avail[1]) # 큰 값으로 한다. [1]
#         else: # 일의 자리 숫자인 경우
#             if len(avail) == 1:
#                 choice.append(avail[0])
#             else:
#                 if pages[i] < 5: # 01234면
#                     choice.append(avail[0]) # 작은 값으로 한다. [0]
#                 else: #56789 이면
#                     choice.append(avail[1]) # 큰 값으로 한다. [1]
#         mins = []
#         m = 10

# string=""
# for i in choice:
#     string += str(i)
#     print(i)
# print(int(string))
# answer = []
# answer.append(abs(page - 100)) # + 만
# answer.append(abs(500000 - page - 100)) # - 만
# answer.append(abs(500000 - int(string) - page) + len(pages)) # 
# answer.append(abs(int(string) - page) + len(pages))
# print(min(answer))
# # for i in len(pages)
# # pages.append(page//1000)
# # pages.append(page//1000)
# # pages.append(page//1000)
# # pages.append(page//1000)


# 거친 정도 (s) =  
# 가장 많이 등장 하는 글자 횟수 (c1) 
# - 가장 적게 등장 하는 글자 횟수 (c2)
# 0개 이상 n 개 이하 삭제하는 방법으로 가장 적은 거친 정도

# s = "aaaaabbc"
# n = 1

# c1 = 0
# c2 = 0
# v = 0
# li_num = []
# li_char = []
# for i in range(len(s)-1):
#     if s[i] != s[i+1]:
#         li_char.append(s[i])
#         li_num.append(s.count(s[i]))
# if s[len(s)-1] != s[len(s)-2]:
#     li_char.append(s[len(s)-1])
#     li_num.append(1)

# max_index = li_num.index(max(li_num))
# min_index = li_num.index(min(li_num))

# print(li_char[max_index])
# print(li_char[min_index])
# v = li_num[max_index] - li_num[min_index]

cardNumber = "21378"
token = []
answer = ""
for i in range(len(cardNumber)):
    token.append(cardNumber[i])
    print(token[i])

if len(token) == 1:
    if token[0] == "0":
        answer = "VALID"
    else:
        answer = "INVALID"
else:
    for i in range(1, len(token), 2):
        token[i] = str(int(token[i])*2)
    for i in range(len(token)):
        answer += int(token[i])
if answer % 10 == 0:
    answer ="VALID"
else:
    answer ="INVALID"
