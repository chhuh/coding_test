def turn_board(m, n, board):
    newboard = [[0]*m for i in range(n)]
    for i in range(m):
        for j in range(n):
            newboard[j][i] = board[i][j] 
    return newboard

def del_board(m, n, board):
    newboard = turn_board(m,n,board)
    for i in range(n):
        newboard[i] = ''.join(newboard[i]).replace("del", "").rjust(m, " ")
    newboard = turn_board(n,m,newboard)
    return newboard

def solution(m, n, board):
    answer = 0
    del_set = set()
    board = list(map(list, board))
    
    while True:
        del_set = set()
        for i in range(m-1):
            for j in range(n-1):
                if board[i][j] != " " and board[i][j] == board[i+1][j] and board[i+1][j] == board[i+1][j+1] and board[i+1][j+1] == board[i][j+1]:
                    del_set.update([(i,j), (i+1, j), (i, j+1), (i+1, j+1)])

        if del_set:
            answer += len(del_set)
            for ds in del_set:
                board[ds[0]][ds[1]] = "del"
            board = del_board(m, n, board)
            
        else:
            break
    return answer
