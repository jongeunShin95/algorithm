class Solution:
    def numTeams(self, rating: List[int]) -> int:
        answer, n = 0, len(rating)

        for j in range(1, n-1):
            rl, rm, ll, lm = 0, 0, 0, 0

            for i in range(j):
                if rating[i] < rating[j]: ll += 1
                elif rating[i] > rating[j]: lm += 1
            
            for k in range(j+1, n):
                if rating[j] < rating[k]: rm += 1
                elif rating[j] > rating[k]: rl += 1
            
            answer += ll * rm + lm * rl
            
        return answer