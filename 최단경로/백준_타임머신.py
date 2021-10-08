import sys
INF = float('inf')
N, M = map(int, sys.stdin.readline().split())

graph = [[] for _ in range(N)]

for _ in range(M):
    A, B, C = map(int, sys.stdin.readline().split())
    graph[A-1].append([B-1,C])

def b_f(src):
    dist = [INF for _ in range(N)]
    dist[src] = 0

    for _ in range(N-1):
        for i in range(N):
            for node, cost in graph[i]:
                if dist[node] > dist[i] + cost:
                    dist[node] = dist[i] + cost

    for i in range(N):
        for node, cost in graph[i]:
            if dist[node] > dist[i]+cost:
                return False

    return dist

dist = b_f(0)

if dist == False:
    print(-1)

else:
    for i in range(1, N):
        print(dist[i] if dist[i]<INF else -1)
