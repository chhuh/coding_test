import heapq
import sys

V, E = map(int, sys.stdin.readline().split())
K = int(sys.stdin.readline())
road = []
for _ in range(E):
    road.append(list(map(int, sys.stdin.readline().split())))
    
answer = 0
    
graph = [[] for _ in range(V)]
    
for i, j, r in road:
    graph[i-1].append([j-1, r])
        
distance = [sys.maxsize for _ in range(V)]
distance[K-1] = 0
hpq = [[0,K-1]]
heapq.heapify(hpq)
    
while hpq:
    dist, node = heapq.heappop(hpq)
        
    if dist > distance[node]:
        continue
        
    for g in graph[node]:
        new_node, new_dist = g[0], g[1]
        new_dist += dist
            
        if new_dist < distance[new_node]:
            distance[new_node] = new_dist
            heapq.heappush(hpq, [new_dist, new_node])

for i in distance:
    if i == sys.maxsize:
        print("INF")
    else:
        print(i)
