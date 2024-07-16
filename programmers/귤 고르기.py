def solution(k, tangerine):
    answer = 0
    dic = {}
    
    for i in tangerine:
        if i in dic: dic[i] += 1
        else: dic[i] = 1
        
    dic = sorted(dic.items(), key=lambda x: x[1], reverse=True)
    
    for _, value in dic:
        k -= value
        answer += 1
        
        if k <= 0: break
    
    return answer