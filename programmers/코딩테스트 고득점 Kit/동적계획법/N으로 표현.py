def solution(N, number):
    def calc(a, b, c):
        for i in a:
            for j in b:
                c.add(i+j)
                c.add(i-j)
                c.add(i*j)
                if j != 0:
                    c.add(i//j)
        return c

    Ns = [{int(str(N)*(i+1))} for i in range(9)]
    for i in range(1, 9):
        for j in range(0, i):
            Ns[i] = calc(Ns[j], Ns[i-j-1], Ns[i])
    
    for i in range(len(Ns)):
        if number in Ns[i]:
            print(i+1)
            return i+1
    print(-1)
    return -1

N = 5
number = 12
# 4

N = 2
number = 11
# 3

solution(N, number)

########################################
# 초기값으로 [{N}. {NN}. {NNN} ... ] 으로 리스트를 생성한다.
# 중복을 방지하기 위해 set를 Ns의 원소로 잡아 생성한다.
# Ns[i] = Ns[j] (+,-,*,//) Ns[i-j-1] 이다 ( 단,  i = 1~8, j = 0~i )
# 분모가 0이 되어 나누는 경우는 제외한다.
# number가 Ns[i]번째에 들어있으면 i+1번을 사용하면 해당 값을 얻을 수 있다.
########################################