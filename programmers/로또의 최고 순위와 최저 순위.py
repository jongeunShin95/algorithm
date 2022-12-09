import sys
input = sys.stdin.readline

def solution(lottos, win_nums):
    answer = []
    _min = 0
    _max = 0
    for i in win_nums: 
        if i in lottos: _min += 1
    _max = _min + lottos.count(0)
    answer = [7-max(_max, 1), 7-max(_min, 1)]
    return answer

lottos = list(map(int, input().split(',')))
win_nums = list(map(int, input().split(',')))

print(solution(lottos, win_nums))