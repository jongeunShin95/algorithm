import sys
input = sys.stdin.readline

# arr[현 숫자] = [현 숫자 전 최솟값까지 숫자, 횟수]
arr = [[0, 0]] * 1000001
arr[1] = [-1, 0]

N = int(input())

for i in range(2, N+1):
    arr[i] = [i-1, arr[i-1][1] + 1]
    if i % 3 == 0:
        if arr[i][1] > arr[i//3][1]+1:
            arr[i] = [i//3, arr[i//3][1]+1]

    if i % 2 == 0:
        if arr[i][1] > arr[i//2][1]+1:
            arr[i] = [i//2, arr[i//2][1]+1]

print(arr[N][1])
print(N, end=' ')
cur = arr[N][0]
while cur != -1:
    print(cur, end=' ')
    cur = arr[cur][0]

print()