def solution(n, costs):
    # kruskal algorithm 사용
    answer = 0
    costs = sorted(costs, key = lambda x : x[2])
    visited = set()
    visited.add(costs[0][0])
    
    while len(visited) != n:
        for i, cost in enumerate(costs):
            if cost[0] in visited and cost[1] in visited:
                continue
            elif cost[0] in visited or cost[1] in visited:
                answer += cost[2]
                visited.update([cost[0], cost[1]])
                break
    return answer
