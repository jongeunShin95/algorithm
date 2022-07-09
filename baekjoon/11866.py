from collections import deque
import sys
input = sys.stdin.readline

N, K = map(int, input().split())

ans = []
q = deque(range(1, N+1))

while q:
    q.rotate(-K)
    ans.append(str(q.pop()))

print('<' + ', '.join(ans) + '>')