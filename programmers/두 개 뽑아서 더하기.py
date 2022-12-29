import sys
from itertools import combinations

input = sys.stdin.readline

def solution(numbers):
    answer = set()
    for i in combinations(numbers, 2):
        answer.add(sum(i))
    return sorted(list(answer))

numbers = list(map(int, input().split(',')))

print(solution(numbers))