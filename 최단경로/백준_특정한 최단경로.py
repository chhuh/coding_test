import heapq
import sys

V, E = map(int, sys.stdin.readline().split())
road = []
for _ in range(E):
    road.append(list(map(int, sys.stdin.readline().split())))
p1, p2 = map(int, sys.stdin.readline().split())
    
graph = [[] for _ in range(V)]
    
for i, j, dist in road:
    graph[i-1].append([dist, j-1])
    graph[j-1].append([dist, i-1])
        
def D(src):
    distance = [sys.maxsize for _ in range(V)]
    distance[src] = 0
        
    hpq = [[0, src]]
    heapq.heapify(hpq)
        
    while hpq:
        dist, node = heapq.heappop(hpq)
            
        if dist > distance[node]:
            continue
                
        for g in graph[node]:
            new_dist, new_node = g[0], g[1]
            new_dist += dist
                
            if new_dist < distance[new_node]:
                distance[new_node] = new_dist
                heapq.heappush(hpq, [new_dist, new_node])
                    
    return distance

start_distance = D(0)
p1_distance = D(p1-1)
p2_distance = D(p2-1)

answer = min(start_distance[p1-1] + p1_distance[p2-1] + p2_distance[V-1], start_distance[p2-1] + p2_distance[p1-1] + p1_distance[V-1])

print(answer if answer < sys.maxsize else -1)
