import sys
input = sys.stdin.readline

def solution(sizes):
    ws, hs = [], []
    for w, h in sizes:
        ws.append(max(w, h))
        hs.append(min(w, h)) 
    return max(ws) * max(hs)

n = int(input())
sizes = [list(map(int, input().split())) for _ in range(n)]

print(solution(sizes))