import sys
import heapq

# dijkstra
def dijkstra(src, dst):
    global graph, length
    
    visit = [sys.maxsize]*(length+1)
    
    visit[src] = 0
    
    hpq = [[0, src]]
    
    heapq.heapify(hpq)
    
    #bfs
    while hpq:
        cost, node = heapq.heappop(hpq)
        
        if cost > visit[node]:
            continue
        
        for g in graph[node]:
            new_node, new_cost = g[0], g[1]

            new_cost += cost
        
            if new_cost < visit[new_node]:
                visit[new_node] = new_cost        
                heapq.heappush(hpq, [new_cost, new_node])
        
    return visit[dst]
        
def solution(n, s, a, b, fares):
    global graph, length
    
    answer = sys.maxsize
    graph = [[] for _ in range(n+1)]
    length = n
    
    for i, j, cost in fares:
        graph[i].append([j, cost])
        graph[j].append([i, cost])
        
    for i in range(1, n+1):
        answer = min(answer, dijkstra(s, i) + dijkstra(i, a) + dijkstra(i, b))
    
    return answer
