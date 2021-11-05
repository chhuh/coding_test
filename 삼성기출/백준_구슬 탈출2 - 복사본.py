import sys

N, M = map(int, sys.stdin.readline().split())

board = []

dr = [1,-1,0,0]
dc = [0,0,1,-1]
visited = [[[[False] * M for _ in range(N)] for _ in range(M)] for _ in range(N)]

def tilt(r, c, dr, dc):
    cnt = 0  
    while board[r+dr][c+dc] != '#' and board[r][c] != 'O':
        r += dr
        c += dc
        cnt += 1
    return r, c, cnt

for r in range(N):
    board.append(str(sys.stdin.readline().rstrip()))
    for c in range(M):
        if board[r][c] == "B":
            br, bc = r, c
        if board[r][c] == "R":
            rr, rc = r, c
        if board[r][c] == "O":
            gr, gc = r, c

queue = []
queue.append((br,bc,rr,rc,0))
visited[br][bc][rr][rc] = True

def bfs():
    while queue:
        br, bc, rr, rc, depth = queue.pop(0)
        if depth > 1:
            break
        for i in range(4):
            nrr, nrc, rcnt = tilt(rr, rc, dr[i], dc[i])
            nbr, nbc, bcnt = tilt(br, bc, dr[i], dc[i])
            if board[nbr][nbc] != "O":
                if board[nrr][nrc] =="O":
                    print(depth+1)
                    return
                if nrr == nbr and nrc == nbc:
                    if rcnt > bcnt:
                        nrr -= dr[i]
                        nrc -= dc[i]
                    else:
                        nbr -= dr[i]
                        nbc -= dc[i]
                if not visited[nrr][nrc][nbr][nbc]:
                    visited[nrr][nrc][nbr][nbc] = True
                    queue.append((nrr, nrc, nbr, nbc, depth+1))
    print(-1)

bfs()

