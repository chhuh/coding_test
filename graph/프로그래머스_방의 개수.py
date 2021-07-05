from collections import defaultdict
from collections import deque

def solution(arrows):
    answer = 0
    
    move = [(-1, 0), (-1, 1), (0, 1), (1, 1), (1, 0), (1, -1), (0, -1), (-1, -1)]
    
    now = (0,0)
    queue = deque([now])
    
    visited = defaultdict(int)
    visited_dir = defaultdict(int)
    
    for arrow in arrows:
        for _ in range(2):
            new = (now[0] + move[arrow][0], now[1] + move[arrow][1])
            queue.append(new)
            now = new
            
    now = queue.popleft()
    visited[now] = 1
    
    while queue:
        new = queue.popleft()
        
        if visited[new] == 1:
            if visited_dir[(now, new)] == 0:
                answer += 1
        
        else:
            visited[new] = 1
        
        visited_dir[(now, new)] = 1
        visited_dir[(new, now)] = 1
        now = new
    
    return answer
