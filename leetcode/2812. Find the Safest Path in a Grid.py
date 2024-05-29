from collections import deque
import heapq

class Solution:
    def __init__(self):
        self.dir = [[0, 1], [0, -1], [1, 0], [-1, 0]]

    def bfs(self, grid, score, n):
        q = deque()

        for x in range(n):
            for y in range(n):
                if grid[x][y]:
                    score[x][y] = 0
                    q.append((x, y))

        while q:
            x, y = q.popleft()
            s = score[x][y]

            for i in range(4):
                dx = x + self.dir[i][0]
                dy = y + self.dir[i][1]

                if 0 <= dx < n and 0 <= dy < n and score[dx][dy] > s + 1:
                    score[dx][dy] = s + 1
                    q.append((dx, dy))

    def maximumSafenessFactor(self, grid: List[List[int]]) -> int:
        n = len(grid)

        if grid[0][0] or grid[n-1][n-1]: return 0

        score = [[float('inf')] * n for _ in range(n)]
        self.bfs(grid, score, n)
        print(score)

        visited = [[False] * n for _ in range(n)]
        pq = [(-score[0][0], 0, 0)]
        heapq.heapify(pq)

        while pq:
            safe, x, y = heapq.heappop(pq)
            safe = -safe

            if x == n - 1 and y == n - 1:
                return safe
            
            visited[x][y] = True

            for i in range(4):
                dx = x + self.dir[i][0]
                dy = y + self.dir[i][1]

                if 0 <= dx < n and 0 <= dy < n and not visited[dx][dy]:
                    s = min(safe, score[dx][dy])
                    heapq.heappush(pq, (-s, dx, dy))
                    visited[dx][dy] = True

        
        return 0
        