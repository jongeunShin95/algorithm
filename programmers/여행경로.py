visited = []

def dfs(src, tickets, ret):
    global visited
    
    if False in visited: pass
    else: return ret

    for i in range(len(tickets)):
        if src == tickets[i][0] and visited[i] == False:
            visited[i] = True
            ret.append(tickets[i][1])
            dfs(tickets[i][1], tickets, ret)
            if False in visited: pass
            else: return ret
            visited[i] = False
            ret.pop()
            
    return ret