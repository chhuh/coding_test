import sys

def multi(a,b):
    res = [[0]*len(b[0]) for _ in range(len(a))]
    for i in range(len(a)):
        for j in range(len(b[0])):
            for k in range(len(b)):
                res[i][j] += a[i][k]*b[k][j]
    for i in range(len(a)):
        for j in range(len(b[0])):
            res[i][j] %= 1000000007
    return res
                

def power(mat, b):
    if b == 1:
        return mat
    elif b%2 == 1:
        return multi(mat, power(mat,b-1))
    else:
        return power(multi(mat,mat),b//2)

N = int(sys.stdin.readline())

start = [[1],[1]]
fib = [[1,1],[1,0]]


if N < 3:
    print(1)

else:
    print(multi(power(fib, N-2), start)[0][0]%1000000007)
