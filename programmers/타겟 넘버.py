import sys
input = sys.stdin.readline

cnt = 0

def dfs(numbers, target, cur):
    global cnt
    if cur == len(numbers):
        if sum(numbers) == target: cnt += 1
        return

    dfs(numbers, target, cur + 1)
    numbers[cur] *= -1
    dfs(numbers, target, cur + 1)
    numbers[cur] *= -1

    return

def solution(numbers, target):
    global cnt
    dfs(numbers, target, 0)
    return cnt


numbers = list(map(int, input().split(',')))
target = int(input())

print(solution(numbers, target))