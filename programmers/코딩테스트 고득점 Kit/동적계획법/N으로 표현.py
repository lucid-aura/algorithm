def solution(N, number):
    def DFS(Ns, target, number, count, exp):
        if target == number:
            print(exp)
            return count

        mins = []
        for i in Ns:
            # if target == 22 and i == 2:
            #     print(target, i)
            # if target == 22222 and i == 22:
                #print(exp, target, i)
            plus, minus, multi, div = 8,8,8,8
            if count+Ns.index(i)+1 < 8:
                plus = DFS(Ns, target+i, number, count+Ns.index(i)+1, exp + '+'+str(i))
                minus = DFS(Ns, target-i, number, count+Ns.index(i)+1, exp +  '-'+str(i))
                multi = DFS(Ns, target*i, number, count+Ns.index(i)+1, exp +  '*'+str(i))
                div = DFS(Ns, target//i, number, count+Ns.index(i)+1, exp +  '/'+str(i))
            mins.append(min(plus, minus, multi, div))
        return min(mins)
        # if target == 22 and i == 2:
        #     print(target, min(plus, minus, multi, div))
        #print(exp)
       

    # if N < 3:
    #     Ns = [int(str(N)*i) for i in range(1, 6)]
    # else:
    #     Ns = [int(str(N)*i) for i in range(1, 5)]
    Ns = [int(str(N)*i) for i in range(1, 8)]
    print(Ns)

    answer = []
    for i in Ns:
        count = Ns.index(i)+1
        answer.append(DFS(Ns, i, number, count, str(i)))
    print(answer)
    if min(answer) == 8:
        return -1
    return min(answer)


N = 5
number = 12

# 4

# N = 2
# number = 11

# N = 5
# number = 31168
# number = 100
# 3
N=2
number=22244
solution(N, number)

