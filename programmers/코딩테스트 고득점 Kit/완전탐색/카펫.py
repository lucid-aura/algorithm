#################### Ä«Æê ##########################

def solution(brown, yellow):
    length = []
    poss = []
    area = brown+yellow
    for i in range(2, int((area)**0.5)+1):
        if area%i == 0:
            poss.append(area//i)
            poss.append(i)
    for i in range(0, len(poss), 2):
        diff = poss[i]*poss[i+1] - (poss[i]-2)*(poss[i+1]-2)
        if diff == brown:
            length = [poss[i], poss[i+1]]
    print(length)

brown = 10
yellow = 2
solution(brown, yellow)