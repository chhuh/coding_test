import sys

N, M = map(int, sys.stdin.readline().split())
out = []

def solve(depth, N, M):
    if depth == M:
        print(' '.join(map(str, out)))
        return
    for i in range(N):
        out.append(i+1)
        solve(depth+1, N, M)
        out.pop()

solve(0, N, M)
