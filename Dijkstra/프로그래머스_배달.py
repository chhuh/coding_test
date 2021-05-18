import math

def solution(N, road, K):
    answer = 0
    visited = []
    distance = [0] + [math.inf for i in range(1,N)]
    roads = {i : {} for i in range(N)}
    # 주어진 road로 초기 roads작성
    for r in road:
        if r[1] - 1 in roads and r[0] - 1 in roads[r[1] - 1]:
            if roads[r[1] - 1][r[0] - 1] > r[2]:
                roads[r[1] - 1][r[0] - 1] = r[2]
                roads[r[0] - 1][r[1] - 1] = r[2]
        else:
            roads[r[1] - 1][r[0] - 1] = r[2]
            roads[r[0] - 1][r[1] - 1] = r[2]

    for i in roads[0]:
        distance[i] = roads[0][i]
        
    while len(visited) != N:
        minimum = math.inf
        for i in range(1, N):
            if i not in visited and distance[i] < minimum:
                minimum = distance[i]
                town = i
                
        visited.append(town)
        for i in roads[town]:
            if distance[i] > distance[town] + roads[town][i]:
                distance[i] = distance[town] + roads[town][i]

    for d in distance:
        if d <= K:
            answer += 1                
    return answer
