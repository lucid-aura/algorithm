from itertools import permutations

items = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '10']
items = ['1', '2', '3', '4', '5']

print(list(permutations(items, 5)))

def solution(n, info):
    ryan = 0
    apeach = 0

    info = info[::-1]
    apeach = 0
    for i in range(len(info)):
        apeach += i*info[i]
    info = info[::-1]        

    info2 = [0,0,0,0,0,0,0,0,0,0,0]
    if info == [1,0,0,0,0,0,0,0,0,0,0]:
        return [-1]
    else:
        # info = info[::-1]
        answer = []
        arrow = n
        idx = 0
        for i in info:
            if arrow > i:
                ryan += (len(info)-1)
                apeach -= (len(info)-1)
                info2[idx] = i+1
            idx += 1
    return answer

n = 5
info = [2,1,1,1,0,0,0,0,0,0,0]
info = info[::-1]
apeach = 0
for i in range(len(info)):
    apeach += i*info[i]

print(apeach)
solution(n, info)