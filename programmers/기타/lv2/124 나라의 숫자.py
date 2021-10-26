def solution(n):
    answer = ''
    
    while n > 0:
        k = n%3

        if k == 0:
            answer = '4' + answer
            n -= 1
        elif k == 1:
            answer = '1' + answer
        else:
            answer = '2' + answer
        n //= 3
    return answer