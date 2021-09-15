def solution(price, money, count):
    total = count*(count+1)/2*price
    return 0 if total - money < 0 else total - money