def solution(quiz):
    answer = []

    for q in quiz:
        arr = q.split()
        if arr[1] == '+':
            if (int(arr[0]) + int(arr[2])) == int(arr[4]): answer.append('O')
            else: answer.append('X')
        elif arr[1] == '-':
            if (int(arr[0]) - int(arr[2])) == int(arr[4]): answer.append('O')
            else: answer.append('X')
    return answer

print(solution(["3 - -4 = -3", "5 + 6 = 11"]))