import sys

T = int(sys.stdin.readline())

for _ in range(T):
    N, M, K = map(int, sys.stdin.readline().split())
    cost = [[]for _ in range(N)]
    for _ in range(K):
        u, v, c, d = map(int, sys.stdin.readline().split())
        cost[u-1].append([v-1,c,d])

    DP = [[sys.maxsize for _ in range(M+1)] for _ in range(N)]
    DP[0][0] = 0

    for c in range(M+1):
        for d in range(N):
            if DP[d][c] >= sys.maxsize:
                continue
            t = DP[d][c]
            for dv, dc, dd in cost[d]:
                if dc +c > M:
                    continue
                DP[dv][dc+c] = min(DP[dv][dc+c], t+dd)

    if min(DP[N-1]) >= sys.maxsize:
        print("Poor KCM")
    else:
        print(min(DP[N-1]))
