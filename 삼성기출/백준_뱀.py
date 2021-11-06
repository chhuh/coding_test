import sys

N, M = map(int, sys.stdin.readline().split())
B = [list(sys.stdin.readline().rstrip()) for _ in range(N)]

dr = [0, 0, -1, 1]
dc = [-1, 1, 0, 0]

queue = []
visited = [[[[False] * M for _ in range(N)] for _ in range(M)] for _ in range(N)]

def init():
    rr, rc, br, bc = 0, 0, 0, 0  # 초기화
    for r in range(N):
        for c in range(M):
            if B[r][c] == 'R':
                rr, rc = r, c
            elif B[r][c] == 'B':
                br, bc = r, c
    queue.append((rr, rc, br, bc, 1))
    visited[rr][rc][br][bc] = True

def tilt(r, c, dr, dc):
    cnt = 0
    while B[r+dr][c+dc] != '#' and B[r][c] != 'O':
        r += dr
        c += dc
        cnt += 1
    return r, c, cnt

def bfs():
    init()
    while queue:
        rr, rc, br, bc, depth = queue.pop(0)
        if depth > 10:
            break
        for i in range(4):
            nrr, nrc, rcnt = tilt(rr, rc, dr[i], dc[i])
            nbr, nbc, bcnt = tilt(br, bc, dr[i], dc[i])
            if B[nbr][nbc] != 'O':
                if B[nrr][nrc] == 'O':
                    print(depth)
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
