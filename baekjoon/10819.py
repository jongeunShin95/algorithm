import sys
input = sys.stdin.readline

N = int(input())
arr = list(map(int, input().split()))
arr2 = []
visited = [False] * N

ans = 0

def calc():
    n = 0
    for i in range(N-1):
        n += abs(arr2[i] - arr2[i+1])
    return n

def nPr(cnt):
    global ans

    if cnt == N:
        ans = max(ans, calc())

    for i in range(N):
        if visited[i]: continue
        visited[i] = True
        arr2.append(arr[i])

        nPr(cnt + 1)

        visited[i] = False
        arr2.pop()

nPr(0)
print(ans)