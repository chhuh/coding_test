import sys
from collections import deque

t = int(sys.stdin.readline())

for _ in range(t):
    n, target = map(int, sys.stdin.readline().split())
    queue = deque(list(map(int, input().split())))

    check = deque([0 for _ in range(n)])
    check[target] = 1
    cnt = 0

    while True:
        if queue[0] == max(queue):
            cnt += 1
            if check[0] == 1:
                print(cnt)
                break
            else:
                queue.popleft()
                check.popleft()
        else:
            queue.append(queue.popleft())
            check.append(check.popleft())
