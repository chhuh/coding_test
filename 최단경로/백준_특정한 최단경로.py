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
        
def D(src, dst):
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
                    
    return distance[dst]

if D(0,p1-1) != sys.maxsize and D(p1-1,p2-1) != sys.maxsize and D(p2-1,V-1) != sys.maxsize:
    print(D(0,p1-1) + D(p1-1,p2-1) + D(p2-1,V-1))
    
