def solution(prices):
    answer = []
    price = 0
    prices.reverse()
    for i in prices:
        if (price < i):

        #price = i
            answer.append(0)

    print(prices)

price = [1, 2, 3, 2, 3]	
solution(price)