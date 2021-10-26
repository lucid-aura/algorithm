def solution(record):
    user_info = {}
    chat_room = []
    for line in record:
        i = line.split(' ')
        
        if i[0] == "Enter":
            user_info[i[1]] = i[2]
            chat_room.append([i[1], "님이 들어왔습니다."])
        elif i[0] == "Leave":
            chat_room.append([i[1], "님이 나갔습니다."])
        else: # Change
            user_info[i[1]] = i[2]
    answer = []
    for i in chat_room:
        answer.append(user_info[i[0]] + i[1])
    
    print(answer)
    return answer

record = ["Enter uid1234 Muzi", "Enter uid4567 Prodo","Leave uid1234","Enter uid1234 Prodo","Change uid4567 Ryan"]
solution(record)

a = {}
a['b'] = 'c'
a['d'] = 'e'
print(a)
a['b'] = 'f'
# a[1] = "d"
print(a)