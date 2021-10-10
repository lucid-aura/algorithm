def solution(number, k):
    answer = []
    idx = 0
    while len(number) - idx > k:
        if number[idx] == '9':
            answer.append('9')
            idx += 1
        else:
            max_val = '-1'
            max_idx = -1
            for i in range(idx, idx+k+1): # 내장함수 max를 이용하면 테스트케이스 10번을 통과할 수 없다.
                if number[i] > max_val:
                    max_val = number[i]
                    max_idx = i
                    if number[i] == '9':
                        break
            k = k - max_idx + idx
            idx = max_idx + 1
            answer.append(number[max_idx])
    if k == 0 and idx < len(number):
        answer.append(number[idx:])
    print(''.join(answer))
    return answer


number = "1924"
k = 2
number = "1231234"
k = 3	
number = "4177252841"
k = 4
number = "7111133"
k = 3
number = "99999"
k = 2
solution(number, k)

# idx:idx+k 중에 최대값을 가지는 index를 찾고 index앞 숫자들을 전부 지운다
# 지운 개수만큼 k값 또한 감소시킨다.
# 최대값을 가진 숫자는 answer에 추가한다.
# idx += 1 후에 위 과정을 반복한다.
# 9는 항상 max값이므로 이후 비교 없이 바로 추가한다.