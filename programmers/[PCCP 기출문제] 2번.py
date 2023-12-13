from collections import deque

def bfs(x, y, n, visited, frag, dir, land, frag_cnt):
    cnt = 0
    visited[x][y] = True
    q = deque()
    q.append((x, y))
    
    while q:
        x, y = q.popleft()
        cnt += 1
        frag[x][y] = n
        for i in range(4):
            dx, dy = x + dir[i][0], y + dir[i][1]
            if dx < 0 or dx >= len(visited) or dy < 0 or dy >= len(visited[0]): continue
            if visited[dx][dy]: continue
            if land[dx][dy] == 0: continue
            visited[dx][dy] = True
            q.append((dx, dy))
    
    frag_cnt.append(cnt)

def solution(land):
    answer, n = 0, -1
    dir = [[1, 0], [-1, 0], [0, 1], [0, -1]]
    visited = [[False for i in range(len(land[0]))] for j in range(len(land))]
    frag = [[-1 for i in range(len(land[0]))] for j in range(len(land))]
    frag_cnt = []
    
    for y in range(len(land[0])):
        for x in range(len(land)):
            if visited[x][y] == False and land[x][y] == 1:
                n += 1
                bfs(x, y, n, visited, frag, dir, land, frag_cnt)
                
    for y in range(len(land[0])):
        temp = []
        temp_cnt = 0
        for x in range(len(land)):
            temp.append(frag[x][y])
        temp = set(temp)
        for i in temp:
            if i == -1: continue
            temp_cnt += frag_cnt[i]
        answer = max(answer, temp_cnt)
            
    return answer