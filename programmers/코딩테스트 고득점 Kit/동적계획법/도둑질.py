import copy
def solution(money):
    def DFS(money, cannot, total, house, dp, i):
        if len(cannot) == len(money):
            return total
        new_total = dp[str(new_house)][1]
    answer = []
    dp = dict()
    for i in range(len(money)):
        cannot = {(i-1)%len(money), i, (i+1)%len(money)}
        house = [i]
        total = money[i]
        dp[str(house)] = total
        DFS(money, cannot, total, house, dp, i)
        #answer.append(DFS(money, cannot, total, house, dp))

    answer = max(dp.values())
    print(answer)
    print(dp)
    return answer

money = [1, 2, 3, 1]
solution(money)

# a = {1,2}
# for i in range(len(a)):
#     print(i)
# print(len(a))
# a = {1,2}
# a.add(3)
# print(a)
# 4


# def solution(money):
#     def DFS(money, cannot, total, house, dp, target):
#         if len(cannot) == len(money):
#             return total
#         for i in [x for x in range(len(money)) if x not in cannot]:
#             print(i, house)
#             if str(house) in dp:
#                 total = dp[str(house)]
#             else:
#                 dp[str(house)] = total
#                 #print(dp)

#             update = copy.deepcopy(cannot)
#             update.add(target)
#             update.add((target+1)%len(money))
#             update.add((target-1)%len(money))
#             new_house = house + [i]
#             new_house.sort()
#             #print(new_house, cannot, update)
#             total += money[i]
#             #dp[str(new_house)] = total
#             if len(new_house)*2 <= len(money):
#                 DFS(money, update, total, new_house, dp, i)
            
#         return total