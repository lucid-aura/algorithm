from itertools import permutations

numbers="173"
number = []
for i in numbers:
    number.append(int(i))
for i in range(2, len(numbers)+1):
    combi = list(permutations(numbers, i))
    for i in combi:
        result = ""
        for j in i:
            result += j
        number.append(int(result))
    #number.append(list(permutations(numbers, i)))

#print(number)
print(number)