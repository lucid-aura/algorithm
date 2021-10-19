def solution(rectangle, characterX, characterY, itemX, itemY):
    def route_cw(rectangle): # 모든 방향은 시계방향을 도는 것으로 기준을 잡는다.
        route = []
        for i in range(rectangle[1], rectangle[3]):
            route.append([rectangle[0], i])
        for i in range(rectangle[0], rectangle[2]):
            route.append([i, rectangle[3]])
        for i in range(rectangle[3], rectangle[1], -1):
            route.append([rectangle[2], i])
        for i in range(rectangle[2], rectangle[0], -1):
            route.append([i, rectangle[1]])
        return route

    def cross_point(route): # 모든 사각형의 교점을 찾고 사각형 순서번호와 함께 cross 리스트에 저장한다.
        cross = []
        for i in range(len(route)-1):
            for j in range(i+1, len(route)):
                for k in route[i]:
                    if k in route[j]:
                        cross.append([k, i, j])
        return cross

    def check_cross(point, cross): # 교점이면 cross 원소를, 교점이 아니면 False를 반환한다.
        for i in cross:
            if point == i[0]:
                return i
        return False

    rectangle.sort()

    # 각각의 사각형의 경로를 생성한다.
    route = []
    for i in rectangle:
        route.append(route_cw(i))

    # 현재 위치한 사각형의 번호, 경로 위치 번호를 저장한다.
    cross = cross_point(route)
    rectangle_index = 0
    point_index = 1
    path = [route[rectangle_index][0]]
    start = route[rectangle_index][0]
    now = route[rectangle_index][point_index]
    while start != now: # 한 바퀴 돌때까지 반복한다.
        path.append(now)
        check = check_cross(now, cross)
        if check: # 교점이면 현재 사각형 index 변경
            rectangle_index = check[(check.index(rectangle_index)) % 2 + 1]
            print(rectangle_index)
            point_index = (route[rectangle_index].index(now)+1) % len(route[rectangle_index])
            now = route[rectangle_index][point_index]
        else: # 교점이 아니면 그대로 다음 점으로 옮긴다.
            point_index = (point_index+1) % len(route[rectangle_index])
            now = route[rectangle_index][point_index]

    character_index = path.index([characterX, characterY])
    item_index = path.index([itemX, itemY])

    answer = min(len(path) - max(character_index, item_index) + min(character_index, item_index), max(character_index, item_index) - min(character_index, item_index))
    print(answer)
    return answer

rectangle = [[1,1,7,4],[3,2,5,5],[4,3,6,9],[2,6,8,8]]
characterX = 1
characterY = 3
itemX = 7
itemY = 8
# 17

# rectangle = [[1,1,8,4],[2,2,4,9],[3,6,9,8],[6,3,7,7]]
# characterX = 9
# characterY = 7
# itemX = 6
# itemY = 1
# 11

rectangle = [[1,1,5,7]]
characterX = 1
characterY = 1
itemX = 4
itemY = 7
# 9

solution(rectangle, characterX, characterY, itemX, itemY)

##########################################################
# 경로는 시계방향/반시계방향 중 하나이다.
# rectangle list를 오름차순 정렬해 시작을 x의 최소로 한다.
# 각각 사각형의 시계방향 둘레 경로를 route 리스트에 넣는다.
# 모든 사각형들의 교점을 cross 리스트에 넣는다.
# route 리스트들의 중복 값(점)이 교점임을 알 수 있다.
# 현재 돌고 있는 둘레의 사각형을 rectangle_index로 설정한다.
# 둘레 리스트의 현재 점 위치를 point_index로 설정한다.
# 현재 점이 교점인 경우 반드시 사각형 번호가 변하게 된다.
# 교점일 경우 현재 사각형과 점 index를 업데이트한다.
# 교점이 아닐 경우 같은 사각형의 둘레를 따라 계속 이동한다.
# 시계방향의 이동경로를 path리스트에 [x,y] 형태로 저장한다.
# 한바퀴를 돌았을 경우 시계방향의 둘레 경로가 완성된다.
# 시계 방향과 반시계 방향 중 최소값을 반환한다.
# min(큰idx - 작은idx, len(path) - 큰idx, 작은idx)
# 전자 : 시계방향 / 후자 : 반시계 방향
##########################################################