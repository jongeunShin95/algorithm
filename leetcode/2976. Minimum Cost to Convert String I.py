class Solution:
    def minimumCost(self, source: str, target: str, original: List[str], changed: List[str], cost: List[int]) -> int:
        answer: int = 0
        graph: List[int][int] = [[float('inf') for _ in range(27)] for _ in range(27)]

        for i in range(1, 27): graph[i][i] = 0
        for i in range(len(original)):
            graph[ord(original[i]) - 96][ord(changed[i]) - 96] = min(graph[ord(original[i]) - 96][ord(changed[i]) - 96], cost[i])
        for k in range(1, 27):
            for i in range(1, 27):
                for j in range(1, 27):
                    graph[i][j] = min(graph[i][k] + graph[k][j], graph[i][j])
        
        for i in range(len(source)):
            if source[i] == target[i]: continue
            answer += graph[ord(source[i]) - 96][ord(target[i]) - 96]

        return answer if answer < float('inf') else -1