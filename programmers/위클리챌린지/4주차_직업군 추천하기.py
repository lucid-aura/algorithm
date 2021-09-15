########################### 직업군 추천하기 ##############################
table = ["SI JAVA JAVASCRIPT SQL PYTHON C#", "CONTENTS JAVASCRIPT JAVA PYTHON SQL C++", "HARDWARE C C++ PYTHON JAVA JAVASCRIPT", "PORTAL JAVA JAVASCRIPT PYTHON KOTLIN PHP", "GAME C++ C# JAVASCRIPT C JAVA"]
languages = ["PYTHON", "C++", "SQL"]	
preference = [7, 5, 5]



split_table = []
for i in table:
    split_table.append(i.split(' '))

score = dict()
for i in split_table:
    score[i[0]] = 0

for jobs in split_table:
    for language in languages:
        if language in jobs:
            print(language)
            print(len(jobs) - jobs.index(language))
            score[jobs[0]] = score[jobs[0]] + (len(jobs) - jobs.index(language))*preference[languages.index(language)]
print(score)

## C -> G -> H -> P -> S
order = ["SI", "PORTAL", "HARDWARE", "GAME", "CONTENTS"]
answer = 'SI'

i = 0
j = 1
while i+j < 5:
    if score[order[i]] <= score[order[i+j]]:
        i = i+j
        answer = order[i]
        j = 1
    else:
        j += 1


print(answer)
