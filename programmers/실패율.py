import sys
input = sys.stdin.readline

def solution(N, stages):
    answer = []
    total = len(stages)
    failure_rate = {}

    for i in range(1, N+1):
        if total == 0: failure_rate.update({i: 0})
        else:
            cur = stages.count(i)
            failure_rate.update({i: cur/total})
            total -= cur

    failure_rate = dict(sorted(failure_rate.items(), key=lambda item: item[1], reverse=True))
    for key, _ in failure_rate.items(): answer.append(key)
    return answer

N = int(input())
stages = list(map(int, input().split(',')))

print(solution(N, stages))