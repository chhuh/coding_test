import sys
import copy

N = int(sys.stdin.readline())
board = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]

ans = 0

def move(det):
    if det == 0:
        for c in range(N):
            idx = 0
            for r in range(1,N):
                if board[r][c]:
                    temp = board[r][c]
                    board[r][c] = 0
                    if board[idx][c] == 0:
                        board[idx][c] = temp
                    elif board[idx][c] == temp:
                        board[idx][c] = temp * 2
                        idx += 1
                    else:
                        idx += 1
                        board[idx][c] = temp

    elif det == 1:
        for c in range(N):
            idx = N - 1
            for r in range(N - 2, -1, -1):
                if board[r][c]:
                    temp = board[r][c]
                    board[r][c] = 0
                    if board[idx][c] == 0:
                        board[idx][c] = temp
                    elif board[idx][c] == temp:
                        board[idx][c] = temp * 2
                        idx -= 1
                    else:
                        idx -= 1
                        board[idx][c] = temp

    elif det == 2:
        for r in range(N):
            idx = 0
            for c in range(1, N):
                if board[r][c]:
                    temp = board[r][c]
                    board[r][c] = 0
                    if board[r][idx] == 0:
                        board[r][idx] = temp
                    elif board[r][idx] == temp:
                        board[r][idx] = temp * 2
                        idx += 1
                    else:
                        idx += 1
                        board[r][idx] = temp

    else:
        for r in range(N):
            idx = N - 1
            for c in range(N - 2, -1, -1):
                if board[r][c]:
                    temp = board[r][c]
                    board[r][c] = 0
                    if board[r][idx] == 0:
                        board[r][idx] = temp
                    elif board[r][idx] == temp:
                        board[r][idx] = temp * 2
                        idx -= 1
                    else:
                        idx -= 1
                        board[r][idx] = temp

def dfs(count):
    global ans,board
    if count == 5:
        for i in range(N):
            ans = max(ans,max(board[i]))
        return

    tmp_board = copy.deepcopy(board)
    for i in range(4):
        move(i)
        dfs(count+1)
        board = copy.deepcopy(tmp_board)

dfs(0)
print(ans)
