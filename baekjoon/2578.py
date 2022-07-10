import sys
input = sys.stdin.readline

ans = 0
arr1 = [list(map(int, input().split())) for _ in range(5)]
arr2 = []
visited = [[False] * 5 for _ in range(5)]

for _ in range(5):
    arr2.extend(list(map(int, input().split())))

def check():
    cnt = 0

    # 가로
    for i in range(5):
        tmp = 0
        for j in range(5):
            if visited[i][j]: tmp += 1
        if tmp == 5: cnt += 1

    # 세로
    for j in range(5):
        tmp = 0
        for i in range(5):
            if visited[i][j]: tmp += 1
        if tmp == 5: cnt += 1

    # 아래로 대각선
    tmp = 0
    for i in range(5):
        if visited[i][i]: tmp += 1
        if tmp == 5: cnt += 1

    # 위로 대각선_2
    tmp = 0
    for i in range(5):
        if visited[i][4-i]: tmp += 1
        if tmp == 5: cnt += 1

    if cnt >= 3: return True
    else: return False

def bingo(x):
    for i in range(5):
        for j in range(5):
            if arr1[i][j] == x:
                return (i, j)

for i in range(len(arr2)):    
    loc = bingo(arr2[i])
    visited[loc[0]][loc[1]] = True

    if check():
        print(i + 1)
        break