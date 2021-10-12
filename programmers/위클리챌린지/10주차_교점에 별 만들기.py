def solution(line):
    point = []
    answer = []
    min_x = 10000000001
    min_y = 10000000001
    max_x = -10000000001
    max_y = -10000000001
    for i in range(len(line)-1):
        for j in range(i+1, len(line)):
            denominator = line[i][0]*line[j][1] - line[i][1]*line[j][0]
            if denominator: # AD - BD != 0
                numerator_x = line[i][1]*line[j][2] - line[i][2]*line[j][1]   
                if numerator_x % denominator == 0:
                    numerator_y = line[i][2]*line[j][0] - line[i][0]*line[j][2]  
                    if numerator_y % denominator == 0:
                        x = int(numerator_x / denominator)
                        y = int(numerator_y / denominator)
                        if x > max_x:
                            max_x = x
                        if y > max_y:
                            max_y = y
                        if x < min_x:
                            min_x = x
                        if y < min_y:
                            min_y = y
                        point.append([x, y])

    table = [['.' for i in range(max_x-min_x+1)] for j in range(max_y-min_y+1)]

    for i in point:
        table[max_y-i[1]][i[0]-min_x] = '*'
    for i in table:
        answer.append("".join(i))
    
    print(answer)
    return answer


line = [[2, -1, 4], [-2, -1, 4], [0, -1, 1], [5, -8, -12], [5, 8, 12]]
# line = [[0, 1, -1], [1, 0, -1], [1, 0, 1]]
#line = [[0, 1, -1], [1, 0, -1], [1, 0, 1], [0, 1 ,1]]
line = [[1, -1, 0], [2, -1, 0], [4, -1, 0]]
line = [[1, -1, 0], [2, -1, 0]]
line = [[0, 1, -1], [1, 0, -1], [1, 0, 1]]
line = [[1,-1,1],[1,-1,-1],[-1,-1,1], [-1,-1,-1]]
solution(line)


########################################################
# Ax + By + E = 0
# Cx + Dy + F = 0
# 교점 x = (BF - ED) / (AD - BC)
# 교점 y = (BF - AF) / (AD - BC)
# 선분 하나씩 교점을 구한다
# 교점을 저장하면서 x, y좌표의 min/max 값을 갱신한다.
# '.'의 이중리스트로 table을 초기화 한다.
# 범위는 아래의 치환될 index와 동일하게 한다.
# 값 대입을 위해 좌표 값을 배열의 index 값으로 치환한다.
# 치환된 index_x = [0:max_x-min_x+1]
# 치환된 index_y = [0:max_y-min_y+1]
# 저장한 교점에 해당하는 값을 '.'에서 '*'로 변환한다.
# join 함수를 이용해 한 행을 string으로 answer에 추가한다.
#########################################################

