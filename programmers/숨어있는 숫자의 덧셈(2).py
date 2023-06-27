def solution(my_string):
    answer = 0
    f = False
    num = 0

    for i in range(len(my_string)):
        if my_string[i] >= '0' and my_string[i] <= '9':
            if f is True: num += my_string[i]
            else:
                f = True 
                num = my_string[i]
        else:
            if f is True: answer += int(num)
            f = False
            num = 0
    
    if num != 0: answer += int(num)

    return answer

print(solution("AAA10"))