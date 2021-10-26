import sys

N = int(sys.stdin.readline())

road = list(map(int, sys.stdin.readline().rstrip().split()))

city = list(map(int, sys.stdin.readline().rstrip().split()))

city.pop()

s = 0

for i, c in enumerate(city):
    if c != min(city[i:]):
        s += c * road[i]
    else:
        s += c * (sum(road[i:]))
        break
print(s)
