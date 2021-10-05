import copy

# def solution(number, k):
#     answer = ''
    # print(number)
    # print(number[0:7])
    # print(number[0:8])
    
    # while  k > 0 and k < len(number):
    #     token = max(number)
    #     token_idx = number.index(token)
    #     print(token_idx)
    #     print(k, number)
    #     if token_idx < k:
    #         answer += number[token_idx]
    #         k -= token_idx
    #         number = number[token_idx+1:]
    #     else:
    #         temp = number[0:k+1]
    #         temp_token = max(temp)
    #         temp_token_idx = temp.index(temp_token)
    #         answer += number[temp_token_idx]
    #         k -= temp_token_idx
    #         number = number[temp_token_idx+1:]
    #     if k == 0 :
    #         answer += number       
            
    # print(answer)

    # pos = 0
    # while(k > 0 and k < len(number[pos:])):
    #     token = number[pos:pos+k+1]
    #     print(token)
    #     max_idx = token.index(max(token))
    #     answer += number[pos + max_idx]
    #     k -= max_idx
    #     pos += max_idx+1
    #     print(answer, pos)
    #     print(k, len(number[pos:]))
    # if k == 0 :
    #     answer += number[pos:]
    # print(answer)
    # return answer


# def solution(number, k):
#     answer = ''
#     while k < len(number) and k > 0:
#         max_idx = number.index(max(number[0:k+1]))
#         print(number)
#         print(max_idx, number[max_idx], k)
        
#         while number[max_idx] == number[max_idx+1] and max_idx < len(number):
#             max_idx += 1
#         answer += number[max_idx]
#         k -= max_idx
#         number = number[max_idx+1:]
#     if k == 0 :
#         answer += number
#     print(answer)
#     return answer

# def solution(number, k):
#     answer = ''
#     while k < len(number):
        
#         max_idx = number.index(max(number[0:k+1]))
#         answer += number[max_idx]
#         k -= max_idx
#         number = number[max_idx+1:]
#     if k == 0 :
#         answer += number
#     print(answer)
#     return answer

def find_number(number, k):
    answer = ""
    while k < len(number) and k > 0:
        for i in range(9, 0, -1):
            if str(i) in number[:k+1]:
                max_idx = number[:k+1].index(str(i))
                answer += number[max_idx]
                number = number[max_idx + 1:]
                k = k - max_idx + 1
                break
        #print(k)
        #print(number[:k+1])
        print(answer)
    if k == 0 :
        answer += number
    print(answer)


def solution(number, k):
    #find_number(number, k)
    answer = '9'*(len(number)-k)
    before = 0
    max_idx = 0
    for i in range(1, 9):
        if str(i) in number:
            answer = ''
            break
    if answer != '':
        print(answer)
        return answer
    
    while k < len(number) - max_idx and k > 0:
        print("while")
        while number[max_idx] == '9' and max_idx  < len(number) and len(number) - max_idx < k:
            max_idx += 1
            answer += number[max_idx]

        max_idx = number[before:before + k+1].index(max(number[before:before + k+1])) + before - 1
        print(k, max_idx, before, number[before:before + k+1])
        answer += number[max_idx]
        print(k, max_idx, before, answer)
        
        k = k + before - max_idx 
        before = max_idx + 1
        

        print(k, max_idx, before, answer)

    # if k == 0 :
    #     answer += number[:max_idx]
    print(answer)
    return answer

# def solution(number, k):
#     answer = '9'*(len(number)-k)
#     for i in range(1, 9):
#         if str(i) in number:
#             answer = ''
#             break
#     if answer != '':
#         return answer
#     while k < len(number) and k > 0:
#         max_idx = 0
#         if len(number) > 0:
#             while number[max_idx] == '9' and len(number) - max_idx < k:
#                 max_idx += 1
#                 answer += number[max_idx]
#                 number = number[max_idx:]
#         max_idx = number.index(max(number[:k+1]))
#         answer += number[max_idx]
#         k -= max_idx
#         number = number[max_idx+1:]
        

#     if k == 0 :
#         answer += number
#     return answer

number = "1231234"
k = 3
number = "99999"
k=3
# number = "1924"
# k =2
# number = "987654321"
# k = 8
# number = "1924"
# k = 2
# number = "999999"
# k=5
# number = "9998887776665554443332221110009"
# k = 30
number = "4177252841"
k = 4
# k = 639
# number = "99999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999991"
solution(number, k)