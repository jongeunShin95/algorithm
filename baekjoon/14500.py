import sys
input = sys.stdin.readline

N, M = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(N)]

visited = [[False] * M for _ in range(N)]
dir = [[0, -1], [0, 1], [-1, 0], [1, 0]]
ans = 0

def dfs(y, x, s, c):
    global ans

    if c == 4:
        ans = max(ans, s)
        return

    for d in range(4):
        dx = x + dir[d][0]
        dy = y + dir[d][1]

        if dx < 0 or dy < 0 or dx >= M or dy >= N: continue
        if visited[dy][dx] == True: continue

        visited[dy][dx] = True
        dfs(dy, dx, s + board[dy][dx], c + 1)
        visited[dy][dx] = False

def f(y, x):
    global ans

    if y + 2 < N and x + 1 < M:
        ans = max(ans, board[y][x] + board[y+1][x] + board[y+2][x] + board[y+1][x+1])
    if y + 2 < N and x - 1 >= 0:
        ans = max(ans, board[y][x] + board[y+1][x] + board[y+2][x] + board[y+1][x-1])
    if y + 1 < N and x + 2 < M:
        ans = max(ans, board[y][x] + board[y][x+1] + board[y][x+2] + board[y+1][x+1])
    if y - 1 >= 0 and x + 2 < M:
        ans = max(ans, board[y][x] + board[y][x+1] + board[y][x+2] + board[y-1][x+1])

for y in range(N):
    for x in range(M):
        visited[y][x] = True
        dfs(y, x, board[y][x], 1)
        visited[y][x] = False

        f(y, x)

print(ans)