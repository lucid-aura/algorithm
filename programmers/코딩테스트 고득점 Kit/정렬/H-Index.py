citations = [10,50,100]
#citations = [0,15,4,0,7,10,0]
n = len(citations)
choice = []
# n편 중, h번 이상 인용된 논문이 h편 이상이고 나머지 논문이 h번 이하 적용
# h의 최대값이 H-Index
# 1 <= n <= 1000
# 0 <= h <= 10000
# [3 0 6 1 5] 에서
# 논문 5편 3편의 논문이 3회이상, 나머지 2편의 논문 3회 이하
# 그러므로 H-Index = 3
answer = 0
citations.sort(reverse=True)
for i in range(citations[0]):
    cnt = 0
    for v in citations:
        if i <= v : # i번 이상 인용된 논문 개수를 구한다.
            cnt += 1
    if cnt >= i and i > answer: #인용된 논문의 개수가 i개 이상이면
        answer = i

# 정렬 후 for문 순서만 바꿨을 뿐인데 오답이 나온다....;;
for i in range(citations[len(citations)-1]):
    cnt = 0
    for v in citations:
        if i >= v :
            cnt += 1
    if cnt >= i and i > answer: #인용된 논문의 개수가 i개 이상이면
        answer = i 


print(answer)
