one = [1,2,3,4,5]
two = [2,1,2,3,2,4,2,5]
three = [3,3,1,1,2,2,4,4,5,5]

answers = [1,3,2,4,2]
answer = []
count = [0,0,0]
for i in range(len(answers)):
    if one[i%len(one)] == answers[i%len(answers)]:
        count[0] += 1
    if two[i%len(two)] == answers[i%len(answers)]:
        count[1] += 1
    if three[i%len(three)] == answers[i%len(answers)]:
        count[2] += 1
print(count)

score = max(count)

for i, v in enumerate(count):
    if v == score:
        answer.append(i+1)

print(answer)
