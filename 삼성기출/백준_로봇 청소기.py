import sys

from collections import deque

n, m =map(int, sys.stdin.readline().split())

r, c, d =map(int, sys.stdin.readline().split())

cnt = 0

board = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]

dr = [-1, 0, 1, 0]
dc = [0, 1, 0, -1]

def clean(r, c, d):
    global cnt
    if board[r][c] == 0:
        board[r][c] = 2
        cnt += 1
    for _ in range(4):
        nd = (d + 3) % 4
        nr = r + dr[nd]
        nc = c + dc[nd]
        if board[nr][nc] == 0:
            clean(nr, nc, nd)
            return
        d = nd
    nd = (d + 2) % 4
    nr = r + dr[nd]
    nc = c + dc[nd]
    if board[nr][nc] == 1:
        return
    clean(nr, nc, d)

clean(r,c,d)
print(cnt)
