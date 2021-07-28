import sys

n = int(sys.stdin.readline())

seq = list(map(int, sys.stdin.readline().split()))

oh_big = [-1]*n
stack = []

for i in range(n):
    while stack and (stack[-1][0] < seq[i]):
        tmp, idx = stack.pop()
        oh_big[idx] = seq[i]
    stack.append([seq[i], i])

print(*oh_big)
