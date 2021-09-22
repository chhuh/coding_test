import sys

def multi(a,b):
    res = [[0]*len(b[0]) for _ in range(len(a))]
    for i in range(len(a)):
        for j in range(len(b[0])):
            for k in range(len(b)):
                res[i][j] += a[i][k]*b[k][j]
    for i in range(len(a)):
        for j in range(len(b[0])):
            res[i][j] %= 1000
    return res
                

def power(mat, b):
    if b == 1:
        return mat
    elif b%2 == 1:
        return multi(mat, power(mat,b-1))
    else:
        return power(multi(mat,mat),b//2)

N, B = map(int, sys.stdin.readline().split())

matrix = [list(map(int, sys.stdin.readline().split()))for _ in range(N)]

ans = power(matrix,B)

for r in range(len(ans)):
    for c in range(len(ans[0])):
        print(ans[r][c], end =" ")
    print()
