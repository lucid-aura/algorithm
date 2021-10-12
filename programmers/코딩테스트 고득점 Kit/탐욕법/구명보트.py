def solution(people, limit):
    people.sort()
    answer = 0
    boat = [0 for i in range(len(people))]
    p_idx = 0
    answer = 0
    while p_idx < len(people):
        switch = True
        while switch:
            if boat[answer] == 0:
                boat[answer] = people[-1]
                people.pop()
                switch = False
            else:
                boat[answer] += people[p_idx]
                if boat[answer] <= limit: # 추가 탑승
                    p_idx += 1
                    switch = False
                else: # 보트 출발
                    answer += 1 
    print(answer+1)
    return answer+1


people = [70, 50, 80, 50]
limit = 100
people = [70, 80, 50]
limit = 100
solution(people, limit)

########################################################
# 몸무게를 오름차순으로 정렬한다.
# append와 pop을 자주 사용하면 시간 초과가 발생한다.
# 따라서 index 변수를 만들어서 배열의 값 변경만 진행한다.
# 아무도 배를 타지 않았으면 가장 무거운 사람이 먼저 탄다.
# 가장 무거운 배에 가장 가벼운 사람이 탈 수 있으면 태운다.
# 탈 수 없으면 해당 배의 다음 배로 넘어간다.
# 이 풀이는 한 배에 최대 2명이 적용 안된 알고리즘이다...
#########################################################