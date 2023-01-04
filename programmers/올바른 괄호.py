def solution(s):
    answer = True
    lst = []

    for c in s:
        if c == '(': lst.append(c)
        else:
            if len(lst) == 0:
                answer = False
                break
            elif lst.pop() == ')':
                answer = False
                break
    if len(lst) > 0: answer = False

    return answer

solution(input())