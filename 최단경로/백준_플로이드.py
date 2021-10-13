import sys

n = int(sys.stdin.readline())
m = int(sys.stdin.readline())
bus_cost = [[sys.maxsize for _ in range(n+1)] for _ in range(n+1)]

for _ in range(m):
    start, end, cost = map(int, sys.stdin.readline().split())
    bus_cost[start][end] = min(cost, bus_cost[start][end])

#플로이드-워셜 알고리즘
for k in range(1, n+1):
    for i in range(1, n+1):
        for j in range(1, n+1):
            if i == j:
                bus_cost[i][j] = 0 
            else:
                bus_cost[i][j] = min(bus_cost[i][j],
                                     bus_cost[i][k] + bus_cost[k][j])

for row in bus_cost[1:]:
    for col in row[1:]:
        if col >= sys.maxsize:
            print(0, end = " ")
        else:
            print(col, end = " ")
    print()
