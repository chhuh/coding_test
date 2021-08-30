import sys

n = int(sys.stdin.readline())
my_point = []


for _ in range(n):
    my_point.append(list(map(int, sys.stdin.readline().split())))

my_point = sorted(my_point, key = lambda x : (x[0], x[1]))

for x, y in my_point:
    print("%d %d" %(x, y))
