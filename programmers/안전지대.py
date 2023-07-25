dir = [[0, -1], [1, -1], [1, 0], [1, 1], [0, 1], [-1, 1], [-1, 0], [-1, -1]]

def solution(board):
    answer = 0
    
    for x in range(len(board)):
        for y in range(len(board[0])):
            if board[x][y] == 1: continue
            flag = False
            for d in dir:
                dx = x + d[0]
                dy = y + d[1]
                
                if dx < 0 or dy < 0 or dx >= len(board) or dy >= len(board[0]): continue
                if board[dx][dy] == 1: 
                    flag = True
                    break
            if flag == False: answer += 1
    return answer