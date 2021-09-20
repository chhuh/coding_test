import sys

N, A_M = map(int, sys.stdin.readline().split())
A = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]
B_M, K = map(int, sys.stdin.readline().split())
B = [list(map(int, sys.stdin.readline().split())) for _ in range(B_M)]

result = [[0 for _ in range(K)] for _ in range(N)] 
for n in range(N): 
    for k in range(K): 
        for m in range(A_M): 
            result[n][k] += A[n][m] * B[m][k] 
            
for row in result: 
    for num in row: 
        print(num,end=' ') 
    print()
