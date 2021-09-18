import sys

N = int(sys.stdin.readline())

board = [list(map(int, input())) for _ in range(N)]

def quad_tree(row, col, n):
    num = board[row][col]
    
    for r in range(row, row+n):
        for c in range(col, col+n):
            if num != board[r][c]:
                print("(", end ="")
                quad_tree(row, col, n//2)
                quad_tree(row, col+n//2, n//2)
                quad_tree(row+n//2, col, n//2)
                quad_tree(row+n//2, col+n//2, n//2)
                print(")", end ="")
                return 
    
    if num == 1:
        print(1, end ="")
    else:
        print(0, end ="")        

quad_tree(0,0,N)
