numbers = [6, 10, 2]
numbers = [3, 30, 34, 5, 9]
answer = ''
sorting = []

#for i, v in enumerate(numbers): #1 가장 높은 자리수 숫자 뽑아내기.
    #sorting.append(v // pow(10, len(str(v))-1))
#1. 가장 높은 자리수의 숫자 비교
# -> 가장 높은 자리수의 숫자를 뽑아내야함.
# -> 가장 높은 자리수가 같은 숫자들은 다음 자리수 값들로 비교(한자리수는 그대로)
# -> 뽑는 다는 것이 필요없는(낮은거로 판별된) 원소는 원본 리스트에서 없애는 것?
#2. 차례대로 높은 자리수의 숫자 비교


result = []

# while(len(numbers) > 0):
#     for i, v in enumerate(numbers): # [index, value]
#         # result.append([i,v//pow(10, len(str(v))-1)])
#         result.append([i,v])
#     sorted(result, key=lambda x:(x[1]//pow(10, len(str(x[1]))-1), len(str(x[1])), reverse=True)
#     # sorted(result, reverse=True)
#     for i in result:
#         print(i)
#         if i[1] == 0:
#             sorting.append(numbers[i][v])
#             numbers.pop(i[0])
#     result.clear()

for i, v in enumerate(numbers): # [index, value]
        # result.append([i,v//pow(10, len(str(v))-1)])
    result.append([i,v])
result = sorted(result, key=lambda x:x[1]//pow(10, len(str(x[1]))-1), reverse=True)
for i in range(len(result)):
    if result[i][0] != result[i+1][0]:
        pass
# result = sorted(result, key=lambda x: x[1]//pow(10, len(str(x[1]))-1), reverse=True)
for i in result:
    print(i)

#return answer