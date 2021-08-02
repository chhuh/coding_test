import heapq
import sys

n = int(sys.stdin.readline().rstrip())

hpq = []
heapq.heapify(hpq)

for i in range(n):
    given = int(sys.stdin.readline().rstrip())
    if given == 0:
        if hpq:
            print(-heapq.heappop(hpq))
        else:
            print(0)
    else:
        heapq.heappush(hpq, -given)
