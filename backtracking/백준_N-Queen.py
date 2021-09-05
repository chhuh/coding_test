import sys

def check(n) :
    for i in range(n):
        if row[n] == row[i] or abs(row[n] - row[i]) == n - i:
            return 0
    return 1

def dfs(n):
    global ans
    if n == N:
        ans += 1
    else:
        for i in range(N):
            row[n] = i
            if check(n):
                dfs(n+1)

N = int(sys.stdin.readline())
row = [0] * N
ans = 0
dfs(0)
print(ans)
