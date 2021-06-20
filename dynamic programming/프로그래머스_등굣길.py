def solution(m, n, puddles):
    answer = 0
    dp = [[1]*m for _ in range(n)]
    
    for puddle in puddles:
        a, b = puddle
        dp[b-1][a-1] = 0
        if a-1 == 0:
            for i in range(b-1, n):
                dp[i][a-1] = 0
        if b-1 == 0:
            for i in range(a-1, m):
                dp[b-1][i] = 0
                
    for i in range(1,n):
        for j in range(1,m):
            if dp[i][j] != 0:
                dp[i][j] = dp[i-1][j] + dp[i][j-1]
    answer = dp[n-1][m-1] % 1000000007
    
    return answer
