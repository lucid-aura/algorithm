import copy
def solution(N, number):
    com = []
    def combi(n, ns):
        if n == 0:
            com.append(copy.deepcopy(ns))
            return ns

        for i in range(1, n+1):
            if n-i >= 0:
                ns.append(i)
                combi(n-i, ns)
                ns.pop()
        return ns

    def partition(ans, Ns):
        branch.append(ans + k)
        branch.append(ans - k)
        branch.append(ans * k)
        branch.append(ans // k)

    def index_to_value(index, Ns):
        return Ns[index-1]

    def DFS(idx_list, idx, Ns, N):
        
        if len(idx_list) == 1 and int(str(N)*(idx+1)) not in Ns[idx]:

            Ns[idx].append(int(str(N)*(idx+1)))
            return int(str(N)*(idx+1))

        for i in idx_list:
            ans = index_to_value(idx, Ns)
            plus, minus = 0, 0
            multi, div = 1, 0
            for j in ans:
                first = j
                
                plus += j
                minus -= j
                multi *= j
                div //= j
            print(idx_list, idx, ans)


                    

    coms = []
    for i in range(1,8):
        combi(i, [])
        coms.append(com)
        com = []
    print(coms)

    Ns = [[int(str(N)*(i+1))] for i in range(8)]
    Ns = [[] for i in range(7)]
    for i in range(0,7):
        for j in coms[i]:
            DFS(j, i, Ns, N)

    # for i in Ns[0]:
    #     for j in Ns[0]:
    #         Ns[1].append(i+j)
    #         Ns[1].append(i-j)
    #         Ns[1].append(i*j)
    #         Ns[1].append(i//j)
    print(Ns)



N = 5
number = 12

# 4

# N = 2
# number = 11

# N = 5
# number = 31168
# number = 100
# 3

N = 8
number = 53
# 8*8 - 88/8

N = 5
number = 14
solution(N, number)


# def solution(N, number):
#     def DFS(Ns, target, number, count, exp):
#         if target == number:
#             print(exp, target, count)
#             return count
    
#         mins = []
#         for i in Ns:
#             # if target == 22 and i == 2:
#             #     print(target, i)
#             # if target == 22222 and i == 22:
#                 #print(exp, target, i)
#             plus, minus, multi, div = 8,8,8,8
#             if count+Ns.index(i)+1 < 8:
#                 plus = DFS(Ns, target+i, number, count+Ns.index(i)+1, exp + '+'+str(i))
#                 minus = DFS(Ns, target-i, number, count+Ns.index(i)+1, exp +  '-'+str(i))
#                 multi = DFS(Ns, target*i, number, count+Ns.index(i)+1, exp +  '*'+str(i))
#                 div = DFS(Ns, target//i, number, count+Ns.index(i)+1, exp +  '/'+str(i))
#             mins.append(min(plus, minus, multi, div))
#         return min(mins)
#         # if target == 22 and i == 2:
#         #     print(target, min(plus, minus, multi, div))
#         #print(exp)
       

#     # if N < 3:
#     #     Ns = [int(str(N)*i) for i in range(1, 6)]
#     # else:
#     #     Ns = [int(str(N)*i) for i in range(1, 5)]
#     Ns = [int(str(N)*i) for i in range(1, 8)]
#     print(Ns)

#     answer = []
#     for i in Ns:
#         count = Ns.index(i)+1
#         answer.append(DFS(Ns, i, number, count, str(i)))
#     print(answer)
#     if min(answer) == 8:
#         return -1
#     return min(answer)
