def solution(msg):
    answer = []
    dic = {}
    s = ''

    for i in range(65, 91): dic[chr(i)] = i - 64
            
    for i in range(0, len(msg)):
        s += msg[i]
        if i == len(msg) - 1:
            answer.append(dic[s])
            break
        if s in dic:
            temp = s + msg[i+1]
            if temp in dic: continue
            else:
                answer.append(dic[s])
                dic[temp] = len(dic) + 1
                s = ''
    return answer