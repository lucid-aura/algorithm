####################### Ã¼À°º¹ ###########################
def solution(n, lost, reserve):
    answer = n
    for i in lost:
        if i in reserve:
            lost.remove(i)
            reserve.remove(i)

    l1 = list(reserve)
    l2 = list(reserve)
    l3 = list(reserve)
    l4 = list(reserve)
    l5 = list(reserve)
    l6 = list(reserve)    
    a1 = answer
    a2 = answer
    a3 = answer
    a4 = answer
    a5 = answer
    a6 = answer
    for i in lost:
        if len(lost) > 0:
            if i-1 in reserve:
                reserve.remove(reserve[reserve.index(i-1)])
            elif i+1 in reserve:
                reserve.remove(reserve[reserve.index(i+1)])
            else:
                answer -= 1
        else:
            answer  -= 1

    for i in lost: 
        if len(l1) > 0:
            if i-1 in l1:
                l1.remove(l1[l1.index(i-1)])
            elif i+1 in l1:
                l1.remove(l1[l1.index(i+1)])
            elif i in l1:
                l1.remove(l1[l1.index(i)])
            else:
                a1 -= 1
        else:
            a1 -= 1
        if len(l2) > 0:
            if i+1 in l2:
                l2.remove(l2[l2.index(i+1)])
            elif i-1 in l2:
                l2.remove(l2[l2.index(i-1)])
            elif i in l1:
                l2.remove(l2[l2.index(i)])
            else:
                a2 -= 1
        else:
            a2 -= 1
        if len(l3) > 0:
            if i in l3:
                l3.remove(l3[l3.index(i)])
            elif i-1 in l3:
                l3.remove(l3[l3.index(i-1)])
            elif i+1 in l3:
                l3.remove(l3[l3.index(i+1)])
            else:
                a3 -= 1
        else:
            a3 -= 1
        if len(l4) > 0:
            if i in l4:
                l4.remove(l4[l4.index(i)])
            elif i+1 in l4:
                l4.remove(l4[l4.index(i+1)])
            elif i-1 in l4:
                l4.remove(l4[l4.index(i-1)])
            else:
                a4 -= 1
        else:
            a4 -= 1
        if len(l5) > 0:
            if i-1 in l5:
                l5.remove(l5[l5.index(i-1)])
            elif i in l5:
                l5.remove(l5[l5.index(i)])
            elif i+1 in l5:
                l5.remove(l5[l5.index(i+1)])
            else:
                a5 -= 1
        else:
            a5 -= 1
        if len(l6) > 0:
            if i+1 in l6:
                l6.remove(l6[l6.index(i+1)])
            elif i in l6:
                l6.remove(l6[l6.index(i)])
            elif i-1 in l6:
                l6.remove(l6[l6.index(i-1)])
            else:
                a6 -= 1
        else:
            a6 -= 1
    answer = max(a1,a2,a3,a4,a5,a6)
    
    return answer

    
reserve = [3]
lost = [2,4]
n = 5

print(solution(n,lost,reserve))