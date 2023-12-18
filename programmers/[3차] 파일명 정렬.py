def solution(files):
    answer = []
    arr = []
    for file in files:
        head, number, tail = '', '', ''
        cnt = 0
        flag = 0 # 0 - head, 1 - number, 2 - tail
        for c in file:
            if flag == 0 and c.isdigit(): flag = 1
            if flag == 1 and c.isdigit() == False: flag = 2
            if cnt >= 5: flag = 2
            
            if flag == 0: head += c
            elif flag == 1:
                number += c
                cnt += 1
            elif flag == 2: tail += c
        arr.append([head, number, tail])
    arr.sort(key=lambda x: (x[0].upper(), int(x[1])))

    for a in arr: answer.append(''.join(a))
    return answer