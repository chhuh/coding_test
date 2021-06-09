import sys
import heapq

def solution(n, edge):
    answer = 0
    
    graph = [[] for _ in range(n)]
    
    for i, j in edge:
        graph[i-1].append([j-1, 1])
        graph[j-1].append([i-1, 1])
    
    my_edge = [sys.maxsize for _ in range(n)]
    my_edge[0] = 0
    
    hpq = [[0,0]]
    heapq.heapify(hpq)
    
    while hpq:
        d, node = heapq.heappop(hpq)
        
        if d > my_edge[node]:
            continue
        
        for g in graph[node]:
            new_node, new_d = g[0], g[1]
            new_d += d
            
            if new_d < my_edge[new_node]:
                my_edge[new_node] = new_d
                heapq.heappush(hpq, [new_d, new_node])
    
    print(my_edge)
    answer = my_edge.count(max(my_edge))
    
    return answer
