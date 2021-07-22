from collections import deque

col,row, depth = map(int,input().split())

graph = [[list(map(int,input().split())) for _ in range(row)] for _ in range(depth)]

dr = [-1,1,0,0,0,0]
dc = [0,0,-1,1,0,0]
dd = [0,0,0,0,-1,1]

queue = deque([])

for d in range(depth):
    for r in range(row):
        for c in range(col):
            if graph[d][r][c] == 1:
                queue.append([d,r,c])
def bfs():
    while queue:
        d,r,c = queue.popleft()
        for i in range(6):
            nc = c + dc[i]
            nr = r + dr[i]
            nd = d + dd[i]

            if 0 <= nc < col and 0 <= nr < row and 0<= nd < depth:
                if graph[nd][nr][nc] == 0:
                    queue.append([nd,nr,nc])
                    graph[nd][nr][nc] = graph[d][r][c] + 1

bfs()
total = graph[0][0][0]
endFlag = False

for d in range(depth):
    for r in range(row):
        for c in range(col):
            if graph[d][r][c] != 0:
                total = max(graph[d][r][c], total)
            else:
                print(-1)
                endFlag = True
                break
        
        if endFlag:
            break

if not endFlag:
    print(total-1)
