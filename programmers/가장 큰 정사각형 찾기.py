def solution(board):
    answer = 0
    dp = [[0 for _ in range(len(board[0]))] for _ in range(len(board))]
    
    for i in range(len(board)):
        for j in range(len(board[0])):
            if (j - 1 < 0) or (i - 1 < 0): dp[i][j] = board[i][j]
            elif board[i][j] == 0: dp[i][j] = 0
            else:
                t = min(dp[i][j-1], dp[i-1][j])
                t = min(t, dp[i-1][j-1])
                dp[i][j] = t + 1
    
    for x in dp:
        answer = max(answer, max(x))

    return answer * answer