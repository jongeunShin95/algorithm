def solution(n, m, section):
    answer = 0
    visited = [True for _ in range(n+1)]
    for s in section: visited[s] = False
    i = 1
    
    while i < len(visited):
        if visited[i] == False:
            answer += 1
            for j in range(m):
                if i+j > n: break
                visited[i+j] = True
            i += m
        else: i += 1
    return answer