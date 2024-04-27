from itertools import combinations

def solution(orders, course):
    answer = []
    
    for c in course:
        dic = {}
        for order in orders:
            coms = list(combinations(order, c))
            
            for com in coms:
                com = ''.join(sorted(com))
                if com in dic: dic[com] += 1
                else: dic[com] = 1
        if len(dic) != 0:
            for k, v in dic.items():
                if v == max(dic.values()) and v >= 2:
                    answer.append(k)
    answer.sort()
    return answer