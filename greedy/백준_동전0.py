import sys
N, K = map(int, sys.stdin.readline().split())

coin = []

for _ in range(N):
    coin.append(int(sys.stdin.readline()))

count = 0

for i in range(N-1, -1, -1):
    if coin[i] > K :
        continue
    else:
        count += K//coin[i]
        K -= coin[i]*(K//coin[i])

print(count)
