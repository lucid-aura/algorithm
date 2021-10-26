import math

import math

def solution(w, h):
    if w==h:
        return w*(h-1)
    answer = w*h
    gcd = math.gcd(w, h)
    min_w = w//gcd
    min_h = h//gcd
    hole = 0
    if  min_w > min_h:
        gradient = min_w/min_h
        for i in range(1, (min_h+1)//2+1):
            hole += ( math.ceil(i*gradient) - math.floor((i-1)*gradient))
        if min_h > 1:
            hole *= 2
            if min_h % 2 == 1:
                hole -= ( math.ceil((min_w//2+1)*gradient) - math.floor((min_w//2)*gradient))
        answer -= (hole*gcd)
    else:
        gradient = min_h/min_w
        for i in range(1, (min_w+1)//2+1):
            hole += ( math.ceil(i*gradient) - math.floor((i-1)*gradient))
        if min_w > 1:
            hole *= 2
            if min_w % 2 == 1:
                hole -= ( math.ceil((min_w//2+1)*gradient) - math.floor((min_w//2)*gradient))
        answer -= (hole*gcd)
    print(answer)
    return answer

w = 2
h = 4
solution(w, h)
