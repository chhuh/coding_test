import sys
import heapq

# def dij(src, dst):
#     global graph, length
    
#     my_fare = [sys.maxsize for _ in range(length)]
#     my_fare[src] = 0
#     hpq = [[0, src]]
#     heapq.heapify(hpq)
    
#     while hpq:
#         fare, node = heapq.heappop(hpq)
        
#         if fare > my_fare[node]:
#             continue
            
#         for g in graph[node]:
#             new_node, new_fare = g[0], g[1]
#             new_fare += fare
            
#             if new_fare < my_fare[new_node]:
#                 my_fare[new_node] = new_fare
#                 heapq.heappush(hpq, [new_fare, new_node])
    
#     return my_fare[dst]

# def solution(n, s, a, b, fares):
#     answer = sys.maxsize
    
#     global graph, length
#     length = n   
#     graph = [[] for _ in range(length)]
    
#     for i, j, fare in fares:
#         graph[i-1].append([j-1, fare])
#         graph[j-1].append([i-1, fare])
        
#     for i in range(length) :
#         answer = min(answer, dij(s-1, i) + dij(i, a-1) + dij(i, b-1))
    
#     return answer


def solution(n, s, a, b, fares):
    length = n
    graph = [[]for _ in range(length)]
    answer = sys.maxsize
    
    for i, j, fare in fares:
        graph[i-1].append([j-1, fare])
        graph[j-1].append([i-1, fare])
    
    def D(src, dst):
        my_fare = [sys.maxsize for _ in range(length)]
        my_fare[src] = 0
        
        hpq = [[0, src]]
        heapq.heapify(hpq)
        
        while hpq:
            fare, node = heapq.heappop(hpq)
            
            if fare > my_fare[node]:
                continue
            
            for g in graph[node]:
                new_node, new_fare = g[0], g[1]
                new_fare += fare
                
                if new_fare < my_fare[new_node]:
                    my_fare[new_node] = new_fare
                    heapq.heappush(hpq, [new_fare, new_node])
        
        return my_fare[dst]
        
    for i in range(length):
        answer = min(answer, D(s-1, i) + D(i, a-1) + D(i, b-1))
        
    return answer
