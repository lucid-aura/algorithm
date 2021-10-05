################################## 최소직사각형 ####################################

def solution(sizes):
    row = []
    col = []
    for i in sizes:
        row.append(i[0])
        col.append(i[1])
    row_max = max(row)
    col_max = max(col)
    answer = row_max * col_max
    if row_max > col_max: # row 기준
        for i in sizes:
            if i[1]  > i[0]:
                temp = i[1]
                i[1] = i[0]
                i[0] = temp
    else:
         for i in sizes:
            if i[0]  > i[1]:
                temp = i[1]
                i[1] = i[0]
                i[0] = temp       
    row = []
    col = []
    for i in sizes:
        row.append(i[0])
        col.append(i[1])
    row_max = max(row)
    col_max = max(col)
    answer = row_max * col_max

    return answer


size = [[60, 50], [30, 70], [60, 30], [80, 40]]	
size = [[10, 7], [12, 3], [8, 15], [14, 7], [5, 15]]
size = [[14, 4], [19, 6], [6, 16], [18, 7], [7, 11]]
print(solution(size))