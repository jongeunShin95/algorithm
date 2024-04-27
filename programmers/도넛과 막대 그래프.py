from collections import defaultdict

def solution(edges):
    answer = [0, 0, 0, 0]
    g = defaultdict(list)
    indgree = defaultdict(int)
    outdgree = defaultdict(int)
    visited = defaultdict(bool)
    
    for edge in edges:
        g[edge[0]].append(edge[1])
        indgree[edge[1]] += 1
        outdgree[edge[0]] += 1
    
    for k in g.keys():
        if indgree[k] == 0 and outdgree[k] >= 2:
            answer[0] = k
            break
    
    for n in g[answer[0]]:
        visited[n] = True
        cur = n
        
        while cur != 0:
            if outdgree[cur] == 0:
                answer[2] += 1
                break
            elif outdgree[cur] >= 2:
                answer[3] += 1
                break
            cur = g[cur][0]
            if visited[cur] and outdgree[cur] == 1:
                answer[1] += 1
                break
            visited[cur] = True
    return answer