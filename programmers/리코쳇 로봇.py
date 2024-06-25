from collections import deque

def solution(board):
    dir = [[0, 1], [0, -1], [1, 0], [-1, 0]] # x, y
    visited = [[False for _ in range(len(board[0]))] for _ in range(len(board))]
    q = deque()
    r, g = [], []
    
    for x in range(len(board)):
        for y in range(len(board[0])):
            if board[x][y] == 'R': r = [x, y]
            if board[x][y] == 'G': g = [x, y]
    
    q.append([0, r[0], r[1]]) # cnt, x, y
    
    while q:
        c, x, y = q.popleft()
        
        if x == g[0] and y == g[1]: return c
    
        if visited[x][y]: continue
        visited[x][y] = True
        
        for i in range(4):
            dx, dy = x + dir[i][0], y + dir[i][1]
            
            if dx < 0 or dy < 0 or dx >= len(board) or dy >= len(board[0]) or board[dx][dy] == 'D':
                continue
                
            while (0 <= dx < len(board)) and (0 <= dy < len(board[0])) and (board[dx][dy] != 'D'):
                dx, dy = dx + dir[i][0], dy + dir[i][1]
            
            dx, dy = dx - dir[i][0], dy - dir[i][1]
            if visited[dx][dy]: continue
            q.append([c + 1, dx, dy])
                
    return -1