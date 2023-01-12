def solution(brown, yellow):
    answer = []
    size = brown + yellow

    for b in range(3, (brown-2) // 2 + 1):
        for y in range(1, size):
            if b * y == size and ((b * 2) + ((y - 2) * 2)) == brown:
                answer.append(max(b, y))
                answer.append(min(b, y))
                return answer
            elif b * y > size: break

    return answer

brown, yellow = map(int, input().split())
print(solution(brown, yellow))