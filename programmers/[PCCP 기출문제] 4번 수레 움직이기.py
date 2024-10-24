from collections import deque
import copy

def solution(maze):
    answer = 0
    _dir = [[-1, 0], [1, 0], [0, -1], [0, 1]]
    x, y = len(maze), len(maze[0]) # 세로, 가로
    r_start, r_end, b_start, b_end = [], [], [], []
    r_visited = [[False for _ in range(y)] for _ in range(x)]
    b_visited = [[False for _ in range(y)] for _ in range(x)]
    
    for i in range(x):
        for j in range(y):
            if maze[i][j] == 1: r_start = [i, j]
            elif maze[i][j] == 2: b_start = [i, j]
            elif maze[i][j] == 3: r_end = [i, j]
            elif maze[i][j] == 4: b_end = [i, j]
    
    q = deque()
    q.append([r_start, b_start, r_visited, b_visited, 0])
    
    while q:
        r_c, b_c, r_v, b_v, cnt = q.popleft()
        
        if r_c == r_end and b_c == b_end: return cnt;
    
        c_r_v = copy.deepcopy(r_v)
        c_b_v = copy.deepcopy(b_v)
        c_r_v[r_c[0]][r_c[1]] = True
        c_b_v[b_c[0]][b_c[1]] = True
        
        for idx in range(4):            
            if r_c == r_end:
                d_b_c = [b_c[0] + _dir[idx][0], b_c[1] + _dir[idx][1]]
                if d_b_c[0] >= x or d_b_c[0] < 0 or d_b_c[1] >= y or d_b_c[1] < 0: continue
                if maze[d_b_c[0]][d_b_c[1]] == 5: continue
                if maze[d_b_c[0]][d_b_c[1]] == 3: continue
                if c_b_v[d_b_c[0]][d_b_c[1]]: continue
                q.append([r_c, d_b_c, c_r_v, c_b_v, cnt + 1])
            elif b_c == b_end:
                d_r_c = [r_c[0] + _dir[idx][0], r_c[1] + _dir[idx][1]]
                if d_r_c[0] >= x or d_r_c[0] < 0 or d_r_c[1] >= y or d_r_c[1] < 0: continue
                if maze[d_r_c[0]][d_r_c[1]] == 5: continue
                if maze[d_r_c[0]][d_r_c[1]] == 4: continue
                if c_r_v[d_r_c[0]][d_r_c[1]]: continue
                q.append([d_r_c, b_c, c_r_v, c_b_v, cnt + 1])
            else:
                d_r_c = [r_c[0] + _dir[idx][0], r_c[1] + _dir[idx][1]]
                if d_r_c[0] >= x or d_r_c[0] < 0 or d_r_c[1] >= y or d_r_c[1] < 0: continue
                if maze[d_r_c[0]][d_r_c[1]] == 5: continue
                if c_r_v[d_r_c[0]][d_r_c[1]]: continue
                
                for idx2 in range(4):
                    d_b_c = [b_c[0] + _dir[idx2][0], b_c[1] + _dir[idx2][1]]
                    if d_b_c[0] >= x or d_b_c[0] < 0 or d_b_c[1] >= y or d_b_c[1] < 0: continue
                    if d_r_c == d_b_c: continue
                    if r_c == d_b_c and b_c == d_r_c: continue
                    if maze[d_b_c[0]][d_b_c[1]] == 5: continue
                    if c_b_v[d_b_c[0]][d_b_c[1]]: continue
                    q.append([d_r_c, d_b_c, c_r_v, c_b_v, cnt + 1])
    
    
    return answer