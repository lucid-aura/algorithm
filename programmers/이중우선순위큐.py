import heapq

operations = ["I 16","D 1"]
operations = ["I 7","I 5","I -5","D -1"]
heap = []
answer = []
for i in operations:
    opcode, operand = i.split(" ")
    if opcode == "I":
        heapq.heappush(heap, int(operand))
    elif len(heap) > 0:
        if operand == "1":
            heap.pop(heap.index(heapq.nlargest(1, heap)[0]))
        else:
            heapq.heappop(heap)
if len(heap) == 0:
    answer.append(0)
    answer.append(0)
else:
    answer.append(heapq.nlargest(1,heap)[0])
    answer.append(heapq.nsmallest(1,heap)[0])

print(answer)


# heap = [121,121,3,4,5,6,7,8,9,10]
# heapq.heapify(heap)
# print(heap)
# heap.pop(heap.index(heapq.nlargest(1, heap)[0]))
# print(heap)