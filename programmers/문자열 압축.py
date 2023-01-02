def solution(s):
    answer = len(s)

    for i in range(1, len(s) // 2 + 1):
        ss = s[:i]
        sss = ""
        cnt = 1

        for j in range(i, len(s) + i, i):
            if s[j:j+i] == ss:
                cnt += 1
            else:
                if cnt > 1: sss = sss + str(cnt) + ss
                else: sss = sss + ss

                cnt = 1
                ss = s[j:j+i]
        answer = min(answer, len(sss))
    return answer

s = input()

print(solution(s))