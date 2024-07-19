def solution(sequence, k):
    answer = []
    start, end, s = 0, 0, sequence[0]
    
    while (start < len(sequence)) and (end < len(sequence)):
        if k > s:
            end += 1
            if end >= len(sequence): break
            s += sequence[end]
        elif k < s:
            s -= sequence[start]
            start += 1
        else:
            if len(answer) == 0:
                answer.append(start)
                answer.append(end)
            else:
                if (answer[1] - answer[0]) > (end - start):
                    answer[0] = start
                    answer[1] = end
            s -= sequence[start]
            start += 1

    return answer