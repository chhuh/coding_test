from itertools import permutations
import sys

N, M = map(int, sys.stdin.readline().split())
P = list(permutations(range(1, N+1), M))

P_list = []

for i in P:
    temp = sorted(list(i))
    if temp not in P_list:
        P_list.append(temp)

for i in P_list:
    print(" ".join(map(str, i)))

