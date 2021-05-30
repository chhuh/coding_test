from collections import deque

def solution(maps):
    
    def my_append(me, d):
        if me not in visited:
            queue.append((me, d+1))
            visited.add(me)
    
    row = len(maps)
    col = len(maps[0])
    
    queue = deque()
    queue.append(((0,0), 1))
    visited = set()
    visited.add((0,0))
    
    while queue:
        me, d = queue.popleft()
        r, c = me
        
        if r == row - 1 and c == col - 1:
            return d
        
        # 오른쪽으로 이동
        if c + 1 < col and maps[r][c+1] == 1:
            me = (r, c+1)
            my_append(me, d)
        
        # 왼쪽으로 이동
        if c-1 >= 0 and maps[r][c-1] == 1:
            me = (r, c-1)
            my_append(me, d)
        
        # 위로 이동
        if r - 1 >= 0 and maps[r-1][c] == 1:
            me = (r-1, c)
            my_append(me, d)
        
        # 아래로 이동
        if r + 1 < row and maps[r+1][c] == 1:
            me = (r+1, c)
            my_append(me, d)
        
    return -1
