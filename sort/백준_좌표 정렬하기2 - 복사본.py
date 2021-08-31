import sys

n = int(sys.stdin.readline())

point = list(map(int, sys.stdin.readline().split()))

pp = sorted(list(set(point)))
dic = {pp[i] : i for i in range(len(pp))}

for i in point:
    print(dic[i], end = " ")
