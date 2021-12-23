import sys

N, M, x, y, K = map(int, sys.stdin.readline().split())

board = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]

command = list(map(int, sys.stdin.readline().split()))

dice = [0,0,0,0,0,0]

def move_dice(dir):
    # 대충 방향에 따라 주사위 굴림
    if dir == 1:
        dice[0], dice[2], dice[3], dice[5] = dice[2], dice[5], dice[0], dice[3]
    elif dir == 2:
        dice[0], dice[2], dice[3], dice[5] = dice[3], dice[0], dice[5], dice[2]
    elif dir == 3:
        dice[0], dice[1], dice[4], dice[5] = dice[1], dice[5], dice[0], dice[4]
    elif dir == 4:
        dice[0], dice[1], dice[4], dice[5] = dice[4], dice[0], dice[5], dice[1]

def move_floor(dir):
    # 방향에따른 보드 위치
    if dir == 1:
        return 0,1
    elif dir == 2:
        return 0,-1
    elif dir == 3:
        return -1,0
    else:
        return 1,0

for c in command:
    dr, dc = move_floor(c)
    if 0 <= x + dr < N and 0 <= y + dc < M:
        x += dr
        y += dc
        move_dice(c)
        if board[x][y] != 0:
            dice[0] = board[x][y]
            board[x][y] = 0
        else:
            board[x][y] = dice[0]
        print(dice[5])

"""
for c in command:
    print(r,c)
    dr, dc = move_floor(c)
    print(r,c)
    print(dr, dc)
    if 0 <= r + dr < N and 0 <= c + dc < M:
        r += dr
        c += dc
        print(r,c)

        move_dice(c)
        if board[r][c] != 0:
            dice[0] = board[r][c]
            board[r][c] = 0
        else:
            board[r][c] = dice[0]
        print(dice[5])
"""
            

