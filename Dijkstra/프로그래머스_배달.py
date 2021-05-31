import heapq

def solution(N, road, K):
    answer = 0
    
    graph = [[] for _ in range(N)]
    
    for i, j, r in road:
        graph[i-1].append([j-1, r])
        graph[j-1].append([i-1, r])
        
    distance = [0] + [sys.maxsize for _ in range(N-1)]
    hpq = [[0,0]]
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
            
    for d in distance:
        if d <= K:
            answer += 1
    return answer
