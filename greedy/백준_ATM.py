import sys
N = int(sys.stdin.readline())

P = list(map(int, sys.stdin.readline().split()))

P = sorted(P)

min_sum = 0

for i in range(1,N+1):
    min_sum += sum(P[:i])

print(min_sum)
