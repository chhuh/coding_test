import heapq
import sys

T = int(sys.stdin.readline())
        
def D(src):
    distance = [sys.maxsize for _ in range(n)]
    distance[src] = 0
        
    hpq = [[0, src]]
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
                    
    return distance

for _ in range(T):
    n, m, t = map(int, sys.stdin.readline().split())
    s, g, h = map(int, sys.stdin.readline().split())

    graph = [[]for _ in range(n)]
    can = []
    
    for _ in range(m) :
        a, b, d = map(int, sys.stdin.readline().split())
        graph[a-1].append([b-1, d])    
        graph[b-1].append([a-1, d])

    for _ in range(t):
        can.append(int(sys.stdin.readline())-1)

    start_dist = D(s-1)
    g_dist = D(g-1)
    h_dist = D(h-1)

    answer = []

    for c in can:
        if start_dist[g-1] + g_dist[h-1] + h_dist[c] == start_dist[c] or start_dist[h-1] + h_dist[g-1] + g_dist[c] == start_dist[c]:
            answer.append(c)
    answer.sort()

    for a in answer:
        print(a+1, end = ' ')
    print()
