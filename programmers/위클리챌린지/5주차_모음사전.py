################################### 모음 사전 #######################################
 
words = ['A', 'E', 'I', 'O', 'U']
word = "EIO" # ["AAAAE", "AAAE", "I", "EIO"]
answer = 0
offset = [781, 156, 31, 6, 1]
for i in range(len(word)):
    print(words.index(word[i])*offset[i])
    answer += words.index(word[i])*offset[i] + 1

print(answer)