def solution(places):
    answer = []
    dir_1 = [[0, 1], [0, -1], [1, 0], [-1, 0]] # 거리 1
    dir_2 = [[0, 2], [0, -2], [2, 0], [-2, 0]] # 거리 2 직석
    dir_3 = [[1, 1], [-1, 1], [-1, -1], [1, -1]] # 거리 2 대각선
    for place in places:
        flag = False # True가 되면 거리두기 지키지 않음
        for x in range(5):
            if flag: break
            for y in range(5):
                if flag: break
                if place[x][y] != 'P': continue
                
                # 거리 1 체크
                for d in dir_1:
                    dx, dy = x + d[0], y + d[1]
                    if dx < 0 or dx >= 5 or dy < 0 or dy >= 5: continue
                    if place[dx][dy] == 'P': 
                        flag = True
                        answer.append(0)
                        break
                if flag: break
                # 거리 2 직선 체크
                for d in dir_2:
                    dx, dy = x + d[0], y + d[1]
                    if dx < 0 or dx >= 5 or dy < 0 or dy >= 5: continue
                    if place[dx][dy] != 'P': continue
                    if place[x + (d[0] // 2)][y + (d[1] // 2)] == 'O':
                        flag = True
                        answer.append(0)
                        break
                if flag: break
                # 거리 2 대각선 체크
                for d in dir_3:
                    dx, dy = x + d[0], y + d[1]
                    if dx < 0 or dx >= 5 or dy < 0 or dy >= 5: continue
                    if place[dx][dy] != 'P': continue
                    if place[dx][y] == 'O' or place[x][dy] == 'O':
                        flag = True
                        answer.append(0)
                        break
        if flag == False: answer.append(1)
    return answer