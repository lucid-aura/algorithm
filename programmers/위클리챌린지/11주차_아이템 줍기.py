def solution(rectangle, characterX, characterY, itemX, itemY):
    table = [[0 for i in range(11)] for j in range(11)]
    line = [[0 for i in range(11)] for j in range(11)]
    
    # for i in table:
    #     print(i)
    # print("###############################")
    for rec in rectangle:
        for i in range(rec[1], rec[3]+1):
            for j in range(rec[0], rec[2]+1):
                table[i][j] = 1
                # if i == rec[1] or i == rec[3]:
                #     point.append([i,j])
                #     table[i][j] = 1
                # elif j == rec[0] or j == rec[2]:
                #     table[i][j] = 1
                #     point.append([i,j])
    for i in table:
        print(i)
    for i in range(10):
        for j in range(10):
            if table[i][j] == 0:
                token = True
                if i > 0:
                    if table[i-1][j] == 0:
                        token = False
                if i < 10:
                    if table[i+1][j] == 0:
                        token = False
                if j > 0:
                    if table[i][j-1] == 0:
                        token = False
                if j < 10:
                    if table[i][j+1] == 0:
                        token = False
                if token:
                    table[i][j] = 1

    for i in range(10):
        for j in range(10):
            if table[i][j] == 1:
                token = True
                if i > 0:
                    if j > 0:
                        if table[i-1][j-1] == 0:
                            token = False
                    if j < 10:
                        if table[i-1][j+1] == 0:
                            token = False
                    if table[i-1][j] == 0:
                        token = False
                if i < 10:
                    if j > 0:
                        if table[i+1][j-1] == 0:
                            token = False
                    if j < 10:
                        if table[i+1][j+1] == 0:
                            token = False
                    if table[i+1][j] == 0:
                        token = False
                if j > 0:
                    if table[i][j-1] == 0:
                        token = False
                if j < 10:
                    if table[i][j+1] == 0:
                        token = False
                if token:
                    line[i][j] = 0
                else:
                    line[i][j] = 1

    
    # route = []
    # for i in range(10):
    #     for j in range(10):
    #         if line[i][j] == 1:
                

    # print("###############################")
    # for i in table:
    #         print(i)
    # print("###############################")
    # for i in line:
    #         print(i)
    #line[characterY][characterX] = 7

    def find_point(characterX, characterY, route):

        point = []
        if line[characterY-1][characterX] == 1 and [characterY-1,characterX] not in route:
            point = [characterY-1,characterX]
        elif line[characterY+1][characterX] == 1 and [characterY+1,characterX] not in route:  
            point = [characterY+1,characterX]
        elif line[characterY][characterX-1] == 1 and [characterY,characterX-1] not in route:
            point = [characterY,characterX-1]
        elif line[characterY][characterX+1] == 1 and [characterY,characterX+1] not in route:
            point = [characterY,characterX+1]
        return point

                
    routeA = [[characterY, characterX]]
    point = find_point(characterX, characterY, routeA)
    routeA.append(point)
    answerA = 1
    xa = point[1]
    ya = point[0]

    routeA = [[characterY, characterX]]
    point = find_point(characterX, characterY, routeA)
    routeA.append(point)
    point = find_point(characterX, characterY, routeA)
    routeB = point
    #print(routeB)
    # xb = point[1]
    # yb = point[0]
    while [ya, xa] != [itemY, itemX]:
        point = find_point(xa, ya, routeA)
        routeA.append(point)
        ya = point[0]
        xa = point[1]
        print(point, ya, xa)
        answerA += 1
        print(routeA)
    print(answerA)
        
    for i in line:
        print(i)
    answer = 0
    return answer

# rectangle의 원소는 각 직사각형의 [좌측 하단 x, 좌측 하단 y, 우측 상단 x, 우측 상단 y] 좌표 형태입니다.

rectangle = [[1,1,7,4],[3,2,5,5],[4,3,6,9],[2,6,8,8]]
characterX = 1
characterY = 3
itemX = 7
itemY = 8
# 17

rectangle = [[1,1,8,4],[2,2,4,9],[3,6,9,8],[6,3,7,7]]
characterX = 9
characterY = 7
itemX = 6
itemY = 1
# 11



solution(rectangle, characterX, characterY, itemX, itemY)
