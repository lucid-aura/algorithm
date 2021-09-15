############################### 상호 평가 ##########################################
answer = ""
scores = [[100,90,98,88,65],[50,45,99,85,77],[47,88,95,80,67],[61,57,100,80,65],[24,90,94,75,65]]
new = [[scores[x][y] for x in range(len(scores))] for y in range(len(scores))]
print(new)
for i in range(len(new)):
    score = 0
    if max(new[i]) != new[i][i] and min(new[i]) != new[i][i] :
        score = sum(new[i])/len(new[i])
    elif len(list(filter(lambda x: new[i][x] == new[i][i], range(len(new[i])))))  != 1:
        score = sum(new[i])/len(new[i])
    else:
        score = (sum(new[i])-new[i][i])/(len(new[i])-1)
        
    if score >= 90:
        answer += 'A'
    elif score >= 80:
        answer += 'B'
    elif score >= 70:
        answer += 'C'
    elif score >= 50:
        answer += 'D'
    else:
        answer += 'F'
print(answer)
   # answer = ''
   # return answer