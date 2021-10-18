def solution(routes):
    routes.sort()
    camera = routes.pop(0)
    answer = 1
    while len(routes) > 0:
        route = routes.pop(0)
        if route[0] > camera[1]:
            answer += 1
            camera = route
        else:
            camera[1] = min(route[1], camera[1])
    print(answer)
    return answer

routes = [[-20,-15], [-14,-5], [-18,-13], [-5,-3]]
# 2

routes = [[1, 10], [3, 5], [7, 9]]
# 2
solution(routes)

########################################################
# 기준을 잡기 위해 routes를 오름차순으로 정렬한다.
# 카메라를 하나로 잡을 수 있는 기준은 R_s < C_e이다
# R_s : 차량 출발, C_e 카메라 끝
# 따라서 새로운 카메라가 추가 될 경우는 위 명제의 반대이다.
# 카메라의 범위를 비교 할때마다 줄여나간다.
########################################################