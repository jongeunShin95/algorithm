from itertools import product

def solution(word):
    answer = 0
    dic = []
    for i in range(6):
        for j in product(['A', 'E', 'I', 'O', 'U'], repeat=i):
            dic.append(''.join(s for s in j))

    dic.sort()
    answer = dic.index(word)
    return answer

print(solution(input()))