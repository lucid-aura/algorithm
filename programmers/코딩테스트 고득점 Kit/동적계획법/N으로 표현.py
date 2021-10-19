def solution(N, number):
    def DFS(N, Ns, target, number, count):
        #print(target, count)
        if count > 8:
            return -1

        if target == number:
            return count

        for i in Ns:
            # if target == 22 and i == 2:
            #     print(target, i)
            count += Ns.index(i)+1
            plus = DFS(i, Ns, target+i, number, count)
            if plus == -1:
                plus  = 9

            minus = DFS(i, Ns, target-i, number, count)
            if minus == -1:
                minus  = 9

            multi = DFS(i, Ns, target*i, number, count)
            if multi == -1:
                multi  = 9   

            div = DFS(i, Ns, target//i, number, count)
            if div == -1:
                div  = 9
        # if target == 22 and i == 2:
        #     print(target, min(plus, minus, multi, div))
        if min(plus, minus, multi, div) == 9:
            return -1
        return min(plus, minus, multi, div)

    if N < 3:
        Ns = [int(str(N)*i) for i in range(1, 6)]
    else:
        Ns = [int(str(N)*i) for i in range(1, 5)]
    print(Ns)

    answer = []
    for i in Ns:
        count = Ns.index(i)+1
        answer.append(DFS(i, Ns, i, number, count))
        print(answer)
    print(min(answer))
    return min(answer)


N = 5
number = 12

# 4

N = 2
number = 11
# 3

solution(N, number)

print(22//2)