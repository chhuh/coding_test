from collections import deque

col,row = map(int,input().split())

graph = [list(map(int,input().split())) for _ in range(row)]

dr = [-1,1,0,0]
dc = [0,0,-1,1]

queue = deque([])

for r in range(row):
    for c in range(col):
        if graph[r][c] == 1:
            queue.append([r,c])

while queue:
    r,c = queue.popleft()
    for i in range(4):
        nc = c + dc[i]
        nr = r + dr[i]

        if 0 <= nc < col and 0 <= nr < row:
            if graph[nr][nc] == 0:
                queue.append([nr,nc])
                graph[nr][nc] = graph[r][c] + 1


total = graph[0][0]
endFlag = False
for r in range(row):
    for c in range(col):
        if graph[r][c] != 0:
            total = max(graph[r][c], total)
        else:
            print(-1)
            endFlag = True
            break
        
    if endFlag:
        break

if not endFlag:
    print(total-1)
