import math 

def calc_fee(fees, in_time, out_time):
    in_time = int(in_time[0:2])*60 + int(in_time[3:])
    out_time = int(out_time[0:2])*60 + int(out_time[3:])
    return out_time-in_time

def solution(fees, records):
    answer = []
    car_fees = {}
    car_token = []
    for i in records:
        token = i.split()
        car_token.append(token)
    for i in car_token:
        car_fees[i[1]] = 0
    for i in range(len(car_token)):
        if car_token[i][2] == "IN": # 들어온 차량 검사
            switch = False
            for j in range(i+1, len(car_token)):
                if car_token[j][2] == 'OUT' and car_token[i][1] == car_token[j][1]: # 차가 나갔을 경우
                    car_fees[car_token[i][1]] += calc_fee(fees, car_token[i][0], car_token[j][0])
                    switch = True
                    break
            if switch == False: # 차가 안나갔을 경우
                car_fees[car_token[i][1]] += calc_fee(fees, car_token[i][0], "23:59")
    car_fees = sorted(car_fees.items())
    for i in car_fees:
        if i[1] <= fees[0]: # 기본 요금 이하이면
            answer.append(fees[1])
        else:
            answer.append(fees[1] + math.ceil((i[1]-fees[0])/fees[2])*fees[3])
    return answer


fees = [180, 5000, 10, 600]
records =["05:34 5961 IN", "06:00 0000 IN", "06:34 0000 OUT", "07:59 5961 OUT", "07:59 0148 IN", "18:59 0000 IN", "19:09 0148 OUT", "22:59 5961 IN", "23:00 5961 OUT"]
#calc_fee(1, "06:00","06:34")
solution(fees, records)