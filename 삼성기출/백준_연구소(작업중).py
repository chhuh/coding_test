import sys

n = int(sys.stdin.readline().rstrip())

work_list = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]

dp = []

for work in work_list:
    dp.append(work[1])

dp.append(0)

for i in range(n-1, -1, -1):
    if work_list[i][0] + i > n:
        dp[i] = dp[i+1]
    else:
        dp[i] = max(dp[i+1], work_list[i][1] + dp[i+work_list[i][0]])

print(dp[0])
