def solution(m, n, board):
    answer = 0
    flag = True
    board = [list(x) for x in board]
    dir = [[0, 1], [1, 0], [1, 1]] # (y, x) 우, 하, 오른쪽대각아래
    
    # 현재 좌표 기준으로 2,2 탐색 / 성공 - True, 실패 - False 반환
    def search(x, y):
        cur = board[y][x]
        for d in dir:
            dx, dy = d[1] + x, d[0] + y
            if cur != board[dy][dx]: return False
        return True
    
    # 내리기
    def down():
        for x in range(0, n):
            for y in range(m-2, -1, -1):
                if board[y][x] == '0': continue
                for dy in range(y+1, m):
                    if board[dy][x] != '0': break
                    board[dy][x] = board[dy-1][x]
                    board[dy-1][x] = '0'
                    
    def play():
        coordinates = []
        cnt = 0
        for y in range(m-1):
            for x in range(n-1):
                if board[y][x] == '0': continue
                if search(x, y): coordinates.append([x, y])

        if len(coordinates) > 0:
            for coordinate in coordinates:
                x, y = coordinate
                if board[y][x] != '0':
                    board[y][x] = '0'
                    cnt += 1
                for d in dir:
                    dx, dy = d[1] + x, d[0] + y
                    if board[dy][dx] != '0':
                        board[dy][dx] = '0'
                        cnt += 1
            down()
        return cnt

    while flag:
        num = play()
        if num > 0: answer += num
        else: flag = False

    return answer