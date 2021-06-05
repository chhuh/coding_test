from collections import deque
import copy

def solution(n, computers):
    answer = 0
    queue = deque()
    visited = [i for i in range(n)]

    while visited:
        queue.append(visited.pop(0))
        while queue:
            node = queue.popleft()
            temp = copy.deepcopy(visited)
            for j in temp:
                if computers[node][j] == 1:
                    queue.append(j)
                    visited.remove(j)
        answer += 1
    return answer
