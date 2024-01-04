from collections import deque
import sys

def solution(n, s, a, b, fares):
    answer = sys.maxsize
    
    graph = [[] for _ in range(n+1)]
    for fare in fares:
        graph[fare[0]].append((fare[1], fare[2]))
        graph[fare[1]].append((fare[0], fare[2]))
        
        
        def dijkstra(s):
            q = deque()
            distance = [sys.maxsize] * (n + 1)
            q.append((0, s)) # 금액, 노드
            distance[s] = 0

            while q:
                fare, node = q.popleft()
                if distance[node] < fare: continue

                for g in graph[node]:
                    cost = fare + g[1]
                    if cost < distance[g[0]]:
                        distance[g[0]] = cost
                        q.append((cost, g[0]))
            return distance

    distance_list = [[]] + [dijkstra(i) for i in range(1, n + 1)]

    for i in range(1, n + 1):
        answer = min(distance_list[s][i] + distance_list[i][a] + distance_list[i][b], answer)
    
    return answer