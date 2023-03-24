import itertools

def solution(number):
    answer = 0
    com = list(itertools.combinations(number, 3))
    for c in com:
        if sum(c) == 0: answer += 1
    return answer


print(solution([-3, -2, -1, 0, 1, 2, 3]))