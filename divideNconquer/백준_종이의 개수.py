import sys

N = int(sys.stdin.readline())

paper = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]

minus = 0
zero = 0
plus = 0

def divide(row, col, n):
    global minus, zero, plus
    num = paper[row][col]

    for r in range(row, row + n):
        for c in range(col, col + n):
            if num != paper[r][c]:
                divide(row, col, n//3)
                divide(row+n//3, col, n//3)
                divide(row, col+n//3, n//3)
                divide(row+n//3, col+n//3, n//3)
                
                divide(row, col+(n//3)*2, n//3)
                divide(row+n//3, col+(n//3)*2, n//3)
                divide(row+(n//3)*2, col+(n//3)*2, n//3)
                divide(row+(n//3)*2, col, n//3)
                divide(row+(n//3)*2, col+n//3, n//3)

                return
            
    if num == -1:
        minus += 1
        return
        
    if num == 0:
        zero += 1
        return

    if num == 1:
        plus += 1
        return

    

divide(0,0,N)
print("{}\n{}\n{}".format(minus, zero, plus))

