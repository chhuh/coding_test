import sys

V, E = map(int, sys.stdin.readline().split())

distance = [[sys.maxsize for _ in range(V)] for _ in range(V)]

for _ in range(E):
    start, end, dist = map(int, sys.stdin.readline().split())
    distance[start-1][end-1] = dist

#플로이드-워셜
for k in range(V):
    for i in range(V):
        for j in range(V):
            distance[i][j] = min(distance[i][j], distance[i][k] + distance[k][j])

min_cycle = sys.maxsize
for i in range(V):
    min_cycle = min(min_cycle, distance[i][i])

if min_cycle >= sys.maxsize:
    print(-1)
else:
    print(min_cycle)
