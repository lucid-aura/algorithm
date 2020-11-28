numbers = [6, 10, 2]
numbers = [3, 30, 34, 5, 9]
numbers = [9,98,987,9876,98765, 0]
numbers = [10, 11, 21, 3]
numbers = [2,20,200]
numbers = [40,403]
#numbers = [9,98,987,9876,98765, 0, 1]
answer = ""
intlen = []
maxval = []
for i in numbers:
    intlen.append(len(str(i)))
for i in range(len(numbers)):
    maxval.append(str(numbers[i])[0])
    print(maxval[i])

print((300//10)%10)
sorting = sorted(numbers, key=lambda x:str(x)[0], reverse= True)
if sorting[0] == 0:
    answer = "0"
for i in sorting:
    answer += str(i)
print(answer)

#다른 자리수라도 각각 첫 자리부터 봐서 sort 해야함.
for i in numbers:
    print(len(str(i)))