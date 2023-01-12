def solution(s):
    answer = []
    lst = []
    s = s.replace('{', '')
    s = s.strip('}')
    s = s.split('},')
    s.sort(key=len)

    for i in s:
        t = i.split(',')
        for a in lst:
            del t[t.index(a)]
        lst.append(t[0])
        answer.append(int(t[0]))

    return answer

print(solution("{{123}}"))