import sys

N = int(sys.stdin.readline())

paper = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]

white = 0
blue = 0

def divide(r, c, n):
    global white, blue
    color = paper[r][c]
    for i in range(r, r+n):
        for j in range(c, c+n):
            if paper[i][j] != color:
                divide(r,c,n//2)
                divide(r,c+n//2,n//2)
                divide(r+n//2,c,n//2)
                divide(r+n//2,c+n//2,n//2)
                return

    if color == 0:
        white += 1
        return

    if color == 1:
        blue += 1
        return

divide(0,0,N)
print("{}\n{}".format(white, blue))
