import sys

n, k = list(map(int, sys.stdin.readline().split()))

A = list(map(int, sys.stdin.readline().split()))
B = list(map(int, sys.stdin.readline().split()))

A = sorted(A)
B = sorted(B, reverse = True)

    
my_A = A[:k]
my_B = B[n-k:n]


max_list = []

for i in range(k):
    max_list.append(my_A[i] + my_B[i])

print(max(max_list))

