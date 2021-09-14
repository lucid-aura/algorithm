import math

def solution(n, k):
    answer = ''
    token = ''
    test = []
    while n>0:
        quo = n//k
        re = n%k
        answer =  answer +str(re)
        if re == 0:
            test.append(token[::-1])
            token = ''
        else:
            token = token + str(re)

        n = quo
    test.append(token[::-1])
    answer = 0
    for i in test:
        if len(i) > 0:
            switch = False
            if int(i)>1:
                for j in range(2,int(math.sqrt(int(i)))+1):
                    if int(i) % j == 0:
                        switch = True
                        break
                if switch == False:
                    answer += 1
    return answer

n = 110011	
k = 10

print(solution(n,k))