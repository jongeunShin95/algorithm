def solution(friends, gifts):
    answer = {}
    dic = {}
    idx = {}
    
    for friend in friends:
        dic[friend] = {}
        for f in friends:
            if f == friend: continue
            dic[friend][f] = 0
        idx[friend] = 0
        answer[friend] = 0
    for gift in gifts:
        sender, receiver = gift.split()
        dic[sender][receiver] += 1
        idx[sender] += 1
        idx[receiver] -= 1
        
    for i in range(len(friends)):
        a = friends[i]
        for j in range(len(friends)):
            if i == j: continue
            b = friends[j]
            if dic[a][b] > dic[b][a]: answer[a] += 1
            elif (dic[a][b] == dic[b][a]) and idx[a] > idx[b]: answer[a] += 1
    
    return answer[max(answer, key = answer.get)]