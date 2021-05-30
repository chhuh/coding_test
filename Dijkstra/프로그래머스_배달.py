import sys

def solution(N, road, K):
    answer = 0
    
    roads = {i : {} for i in range(N)}
    
    # 초기 roads작성
    for r in road:
        if r[0]-1 in roads and r[1]-1 in roads[r[0] - 1]:
            if r[2] < roads[r[0] - 1][r[1] - 1]:
                roads[r[0] - 1][r[1] - 1] = r[2]
                roads[r[1] - 1][r[0] - 1] = r[2]       
        else:
            roads[r[0] - 1][r[1] - 1] = r[2]
            roads[r[1] - 1][r[0] - 1] = r[2]
    
    # 0을 기준으로 한 초기 distance작성
    distance = [0] + [sys.maxsize for _ in range(N-1)]
    
    for i in roads[0]:
        distance[i] = roads[0][i]
    
    # 0을 기준으로 최단거리 검거된 마을 모임
    visited = []
    
    while len(visited) != N:
        mini = sys.maxsize
        
        for i in range(1, N):
            if i not in visited and distance[i] < mini:
                mini  = distance[i]
                town = i
        
        visited.append(town)
        
        for i in roads[town]:
            if distance[i] > roads[town][i] + mini:
                distance[i] = roads[town][i] + mini
                
    for d in distance:
        if d <= K:
            answer += 1
        
    return answer
