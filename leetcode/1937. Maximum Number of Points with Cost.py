class Solution:
    def maxPoints(self, points: List[List[int]]) -> int:
        dp: List[List[int]] = [[0 for _ in range(len(points[0]))] for _ in range(len(points))]
        left: List[List[int]] = [[0 for _ in range(len(points[0]))] for _ in range(len(points))]
        right: List[List[int]] = [[0 for _ in range(len(points[0]))] for _ in range(len(points))]

        for i in range(len(points[0])):
            dp[0][i] = points[0][i]

        for m in range(1, len(points)):
            left[m][0] = dp[m-1][0]
            right[m][-1] = dp[m-1][-1]

            # left
            for n in range(1, len(points[0])):
                left[m][n] = max(left[m][n-1]-1, dp[m-1][n])
            # right
            for n in range(len(points[0])-2, -1, -1):
                right[m][n] = max(right[m][n+1]-1, dp[m-1][n])
            # dp
            for n in range(0, len(points[0])):
                dp[m][n] = points[m][n] + max(left[m][n], right[m][n])

        return max(dp[-1])