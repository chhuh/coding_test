import sys
sys.setrecursionlimit(100001)

n = int(sys.stdin.readline().rstrip())

board = []

for _ in range(n):
    board.append(list(map(int, sys.stdin.readline().rstrip().split())))
    
visited = [0 for _ in range(n)]
ans = sys.maxsize

#재귀 함수
def dfs(idx, cnt):
    global ans

    # 정답이 될 수 있다면
    if cnt == n//2:
        team1, team2 = 0,0
        
        for i in range(n):
            for j in range(n):
                if visited[i] and visited[j]:
                    team1 += board[i][j]
                    
                elif not visited[i] and not visited[j]:
                    team2 += board[i][j]
        
        ans = min(ans, abs(team1-team2))
        
    # 정답이 아니라면
    # 뻗을 수 있는 모든 자식 노드에 대하여    
    for i in range(idx, n) :
        if visited[i]:
            continue
        # 정답후보가 될 수 있는 경우
        else:
            # 자식 노드로 이동
            visited[i] = 1
            # 재귀함수 + 1
            dfs(i+1, cnt+1)
            # 부모노드로 이동
            visited[i] = 0
            
dfs(0,0)
print(ans)
