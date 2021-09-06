import sys
sys.setrecursionlimit(100001)

n = int(sys.stdin.readline().rstrip())

board = []

for _ in range(n):
    board.append(list(map(int, sys.stdin.readline().rstrip().split())))
    
visited = [0 for _ in range(n)]
ans = sys.maxsize

def dfs(idx, cnt):
    global ans
    if cnt == n//2:
        team1, team2 = 0,0
        
        for i in range(n):
            for j in range(n):
                if visited[i] and visited[j]:
                    team1 += board[i][j]
                    
                elif not visited[i] and not visited[j]:
                    team2 += board[i][j]
        
        ans = min(ans, abs(team1-team2))
        
    for i in range(idx, n) :
        if visited[i]:
            continue
        else:
            visited[i] = 1
            dfs(i+1, cnt+1)
            visited[i] = 0
            
dfs(0,0)
print(ans)
